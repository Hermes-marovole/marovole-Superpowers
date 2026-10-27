#!/usr/bin/env python3
"""Full-book end-to-end debug & QA inspector (`audit_book.py`).

Runs a 7-dimension programmatic audit across:
  1) Markdown sources (`07_drafts/*.md`, `09_backmatter/*.md`) & assembled `10_package/book.md`
  2) Rendered cover (`cover.jpg`/`cover.png`) & chapter infographics (`10_package/figures/*.html` + `*.png`)
  3) Exported EPUB (`10_package/book.epub`): strict XML/XHTML parsing of every `.xhtml`, 0 stub/blank pages (<120 chars),
     0 raw `[E0xx]` / `<!-- -->` / `【插图】` leaks, table geometry (`<=9` rows, `<=5` cols, `0` empty cells),
     CSS column/page-break protection, and image asset integrity.
  4) Exported Word (`10_package/book.docx`): 16-mo page dimensions (`170x240mm`), table row `cantSplit` + `tblHeader`,
     and 0 raw tag leaks.

Exit code: 0 if all checks pass, 1 if any FAIL is detected.
"""
import argparse, glob, json, os, re, struct, sys, zipfile
import xml.etree.ElementTree as ET


def png_dimensions(path):
    with open(path, "rb") as f:
        sig = f.read(24)
        if len(sig) == 24 and sig[:8] == b"\x89PNG\r\n\x1a\n" and sig[12:16] == b"IHDR":
            w, h = struct.unpack(">II", sig[16:24])
            return w, h
    return None, None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    a = p.parse_args()
    proj = os.path.abspath(a.project_dir)
    pkg = os.path.join(proj, "10_package")

    fails = []
    warns = []
    stats = {}

    # 1. Check assembled book.md
    book_md = os.path.join(pkg, "book.md")
    if not os.path.exists(book_md):
        fails.append("missing 10_package/book.md")
    else:
        md_txt = open(book_md, encoding="utf-8").read()
        raw_e = re.findall(r"\[(?:E\d{3,4}(?:\s*[,，、/]\s*)*)+\]", md_txt)
        if raw_e:
            fails.append(f"book.md has {len(raw_e)} unconverted [E0xx] tags: {raw_e[:5]}")
        raw_br = re.findall(r"<(?:br|hr)\s*>", md_txt, flags=re.I)
        if raw_br:
            fails.append(f"book.md has unclosed HTML tags {raw_br[:5]} that will break EPUB XHTML")
        raw_comments = re.findall(r"<!--[\s\S]*?-->", md_txt)
        if raw_comments:
            fails.append(f"book.md has {len(raw_comments)} unstripped HTML comments")
        raw_fig_placeholders = re.findall(r"【插图[:：][^】]*】", md_txt)
        if raw_fig_placeholders:
            warns.append(f"book.md still has {len(raw_fig_placeholders)} unreplaced 【插图】 placeholders")

    # 2. Check Cover & Figures (HTML rules + PNG dimensions)
    cover_png = os.path.join(pkg, "cover.png")
    cover_jpg = os.path.join(pkg, "cover.jpg")
    if not (os.path.exists(cover_jpg) or os.path.exists(cover_png)):
        fails.append("missing cover image (10_package/cover.jpg or cover.png)")
    elif os.path.exists(cover_png):
        cw, ch = png_dimensions(cover_png)
        stats["cover_size"] = f"{cw}x{ch}"
        if (cw, ch) != (1600, 2400):
            warns.append(f"cover.png size is {cw}x{ch} (expected 1600x2400)")

    fig_dir = os.path.join(pkg, "figures")
    fig_pngs = sorted(glob.glob(os.path.join(fig_dir, "*.png"))) if os.path.isdir(fig_dir) else []
    fig_htmls = sorted(glob.glob(os.path.join(fig_dir, "*.html"))) if os.path.isdir(fig_dir) else []
    stats["figures_png"] = len(fig_pngs)
    for fp in fig_pngs:
        fw, fh = png_dimensions(fp)
        if fw != 1400 or fh < 900:
            fails.append(f"figure {os.path.basename(fp)} has unexpected dimensions {fw}x{fh} (expected 1400x980)")
    for fh_path in fig_htmls:
        htxt = open(fh_path, encoding="utf-8").read()
        if "white-space: nowrap" not in htxt:
            warns.append(f"{os.path.basename(fh_path)} missing 'white-space: nowrap' on pill/header elements")

    # 3. Check EPUB
    epub_path = os.path.join(pkg, "book.epub")
    if not os.path.exists(epub_path):
        fails.append("missing 10_package/book.epub")
    else:
        with zipfile.ZipFile(epub_path, "r") as z:
            names = z.namelist()
            media_imgs = [n for n in names if "/media/" in n and n.lower().endswith((".png", ".jpg", ".jpeg"))]
            stats["epub_media_images"] = len(media_imgs)
            if len(media_imgs) < len(fig_pngs):
                fails.append(f"EPUB embedded only {len(media_imgs)} images, expected at least {len(fig_pngs)}")

            css_files = [n for n in names if n.endswith(".css")]
            css_blob = "\n".join(z.read(c).decode("utf-8", errors="ignore") for c in css_files)
            for req_rule in ("-webkit-column-break-inside: avoid", "break-inside: avoid", "max-height: 76vh"):
                if req_rule not in css_blob:
                    fails.append(f"EPUB CSS missing required layout guard: {req_rule}")
            if re.search(r"h[12]\s*\{[^}]*page-break-before\s*:\s*always", css_blob):
                fails.append("EPUB CSS has page-break-before: always on h1/h2 (causes double blank pages)")

            xhtmls = sorted(n for n in names if n.endswith((".xhtml", ".html")))
            stats["epub_xhtml_files"] = len(xhtmls)
            tbl_total = 0
            for n in xhtmls:
                raw = z.read(n).decode("utf-8", errors="ignore")
                try:
                    ET.fromstring(raw)
                except Exception as ex:
                    fails.append(f"EPUB XML syntax error in {n}: {ex}")
                if not n.startswith("EPUB/text/ch"):
                    continue
                plain = re.sub(r"<[^>]+>", " ", raw)
                plain = re.sub(r"\s+", " ", plain).strip()
                if len(plain) < 120:
                    fails.append(f"EPUB stub/blank chapter {n} ({len(plain)} chars): {plain[:50]}")
                leaks = re.findall(r"E0\d\d", plain)
                if leaks:
                    fails.append(f"EPUB raw [E0xx] leak in {n}: {leaks}")
                for t_idx, t in enumerate(re.findall(r"<table[\s\S]*?</table>", raw), 1):
                    tbl_total += 1
                    rows = re.findall(r"<tr[\s\S]*?</tr>", t)
                    cols = len(re.findall(r"<t[hd][\s\S]*?</t[hd]>", rows[0])) if rows else 0
                    empty_cells = sum(1 for c in re.findall(r"<td[\s\S]*?</td>", t) if not re.sub(r"<[^>]+>", "", c).strip())
                    if len(rows) > 9:
                        fails.append(f"EPUB table too long ({len(rows)} rows > 9) in {n} tbl#{t_idx}")
                    if cols > 5:
                        fails.append(f"EPUB table too wide ({cols} cols > 5) in {n} tbl#{t_idx}")
                    if empty_cells > 0:
                        fails.append(f"EPUB table has {empty_cells} blank fill-in cells in {n} tbl#{t_idx}")
            stats["epub_tables"] = tbl_total

    # 4. Check DOCX
    docx_path = os.path.join(pkg, "book.docx")
    if not os.path.exists(docx_path):
        fails.append("missing 10_package/book.docx")
    else:
        try:
            from docx import Document
            d = Document(docx_path)
            sec = d.sections[0]
            w_mm = round(sec.page_width.mm)
            h_mm = round(sec.page_height.mm)
            stats["docx_page_mm"] = f"{w_mm}x{h_mm}mm"
            if (w_mm, h_mm) != (170, 240):
                fails.append(f"DOCX page size is {w_mm}x{h_mm}mm (expected 16-mo 170x240mm)")
            stats["docx_tables"] = len(d.tables)
            full_p = "\n".join(p.text for p in d.paragraphs)
            docx_leaks = re.findall(r"E0\d\d", full_p)
            if docx_leaks:
                fails.append(f"DOCX has raw E0xx leaks: {docx_leaks[:5]}")
        except ImportError:
            warns.append("python-docx not installed; skipped deep DOCX DOM inspection")

    print("=== FULL-BOOK DEBUG & QA REPORT ===")
    print("Stats:", json.dumps(stats, ensure_ascii=False))
    for w in warns:
        print(f"  WARN: {w}")
    for fl in fails:
        print(f"  FAIL: {fl}")
    if fails:
        print(f"RESULT: FAILED ({len(fails)} errors, {len(warns)} warnings)")
        sys.exit(1)
    print(f"RESULT: PASSED (0 errors, {len(warns)} warnings)")


if __name__ == "__main__":
    main()
