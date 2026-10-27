#!/usr/bin/env python3
"""Export book.md to Word and build the publisher submission package (投稿包).

Needs pandoc on PATH. python-docx is optional (Chinese fonts, chapter page breaks, TOC auto-update).
"""
import argparse, os, re, shutil, subprocess, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import split_front, COMMENT_RE, draft_files, load_state


def build_reference_doc(path):
    """Reference doc lives in the project, so the skill directory can stay read-only."""
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return path
    subprocess.run(["pandoc", "-o", path, "--print-default-data-file", "reference.docx"], check=True)
    try:
        from docx import Document
        from docx.oxml.ns import qn
        from docx.shared import Pt
    except ImportError:
        print("python-docx not installed; using pandoc default fonts", file=sys.stderr)
        return path
    d = Document(path)
    for st in d.styles:
        if st.type != 1:
            continue
        is_heading = st.name.startswith("Heading") or st.name in ("Title", "Subtitle")
        st.font.name = "Times New Roman"
        rpr = st.element.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = rpr.makeelement(qn("w:rFonts"), {})
            rpr.append(rfonts)
        rfonts.set(qn("w:eastAsia"), "黑体" if is_heading else "宋体")
        if st.name in ("Normal", "Body Text", "First Paragraph"):
            st.font.size = Pt(11)
        if st.name in ("Heading 1",):
            st.paragraph_format.page_break_before = True
    d.save(path)
    return path


def mark_update_fields(docx_path):
    """Ask Word to refresh the TOC field on open; pandoc writes the field without cached entries."""
    try:
        from docx import Document
        from docx.oxml.ns import qn
    except ImportError:
        return
    d = Document(docx_path)
    settings = d.settings.element
    el = settings.find(qn("w:updateFields"))
    if el is None:
        el = settings.makeelement(qn("w:updateFields"), {})
        settings.append(el)
    el.set(qn("w:val"), "true")
    d.save(docx_path)


def to_docx(src_md, dst, ref, toc=False, chapter_breaks=False, book_title="糖前四型"):
    src_dir = os.path.dirname(os.path.abspath(src_md))
    cmd = ["pandoc", src_md, "-o", dst, "--reference-doc", ref, f"--resource-path={src_dir}", "--quiet"]
    if toc:
        cmd += ["--toc", "--toc-depth=2", "-M", "toc-title=目录"]
    subprocess.run(cmd, check=True)
    polish_publication_docx(dst, is_full_book=toc, chapter_breaks=chapter_breaks, book_title=book_title)
    if toc:
        mark_update_fields(dst)


def polish_publication_docx(docx_path, is_full_book=True, chapter_breaks=False, book_title="糖前四型"):
    """Apply Chinese trade-book publishing standards (16-mo B5, CJK indentation, three-line tables, headers/footers)."""
    try:
        from docx import Document
        from docx.oxml import OxmlElement, parse_xml
        from docx.oxml.ns import qn, nsdecls
        from docx.shared import Pt, Cm, RGBColor
        from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
        from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
    except ImportError:
        return

    d = Document(docx_path)

    # 1. 页面设置：标准 16 开图书（170mm × 240mm），装订版心留白
    for sec in d.sections:
        sec.page_width = Cm(17.0)
        sec.page_height = Cm(24.0)
        sec.top_margin = Cm(2.5)
        sec.bottom_margin = Cm(2.3)
        sec.left_margin = Cm(2.4)
        sec.right_margin = Cm(2.2)
        sec.header_distance = Cm(1.4)
        sec.footer_distance = Cm(1.4)
        sec.different_first_page_header_footer = True

        # 页眉（首页不显示，内文显示书名 + 细底线）
        hdr = sec.header
        hp = hdr.paragraphs[0] if hdr.paragraphs else hdr.add_paragraph()
        hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        hp.text = ""
        hrun = hp.add_run(f"《{book_title}》 · 临床营养精准干预读本")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)
        hrpr = hrun._element.get_or_add_rPr()
        hrf = hrpr.find(qn("w:rFonts"))
        if hrf is None:
            hrf = OxmlElement("w:rFonts")
            hrpr.append(hrf)
        hrf.set(qn("w:eastAsia"), "宋体")
        hpPr = hp._element.get_or_add_pPr()
        hpBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="4" w:color="D1D5DB"/></w:pBdr>')
        hpPr.append(hpBdr)

        # 页脚（居中页码：— PAGE —）
        ftr = sec.footer
        fp = ftr.paragraphs[0] if ftr.paragraphs else ftr.add_paragraph()
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fp.text = ""
        r1 = fp.add_run("— ")
        r1.font.size = Pt(9)
        r1.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)
        fld = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>')
        fp._element.append(fld)
        r2 = fp.add_run(" —")
        r2.font.size = Pt(9)
        r2.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)

    def set_east_asia_font(style_or_run, cn_font, en_font="Times New Roman", size_pt=None, bold=None, color_hex=None):
        f = style_or_run.font
        f.name = en_font
        if size_pt is not None:
            f.size = Pt(size_pt)
        if bold is not None:
            f.bold = bold
        if color_hex is not None:
            f.color.rgb = RGBColor.from_string(color_hex)
        el = style_or_run._element if hasattr(style_or_run, "_element") else style_or_run.element
        rpr = el.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts")
            rpr.append(rfonts)
        rfonts.set(qn("w:eastAsia"), cn_font)
        rfonts.set(qn("w:ascii"), en_font)
        rfonts.set(qn("w:hAnsi"), en_font)

    # 2. 全局样式规范化
    for st in d.styles:
        if st.type != 1:
            continue
        sname = st.name
        pf = st.paragraph_format
        pf.widow_control = True
        if sname in ("Normal", "Body Text", "First Paragraph"):
            set_east_asia_font(st, "宋体", size_pt=10.5, bold=False, color_hex="1F2328")
            pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
            pf.first_line_indent = Pt(21)  # 首行缩进 2 字符（10.5pt * 2）
            pf.space_before = Pt(0)
            pf.space_after = Pt(4)
        elif sname == "Compact":
            set_east_asia_font(st, "宋体", size_pt=10.0, bold=False, color_hex="1F2328")
            pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            pf.line_spacing = 1.35
            pf.first_line_indent = Pt(0)
            pf.space_before = Pt(2)
            pf.space_after = Pt(3)
        elif sname in ("Block Text", "Quote"):
            set_east_asia_font(st, "楷体", size_pt=10.0, bold=False, color_hex="374151")
            pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            pf.line_spacing = 1.4
            pf.left_indent = Cm(0.7)
            pf.right_indent = Cm(0.5)
            pf.first_line_indent = Pt(0)
            pf.space_before = Pt(6)
            pf.space_after = Pt(6)
        elif sname == "Title":
            set_east_asia_font(st, "黑体", size_pt=26, bold=True, color_hex="0F172A")
            pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.first_line_indent = Pt(0)
            pf.space_before = Pt(72)
            pf.space_after = Pt(14)
        elif sname == "Subtitle":
            set_east_asia_font(st, "楷体", size_pt=13, bold=False, color_hex="334155")
            pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.first_line_indent = Pt(0)
            pf.space_before = Pt(4)
            pf.space_after = Pt(36)
        elif sname == "Author":
            set_east_asia_font(st, "黑体", size_pt=12, bold=True, color_hex="1E293B")
            pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.first_line_indent = Pt(0)
            pf.space_before = Pt(18)
            pf.space_after = Pt(120)
        elif sname == "Heading 1":
            set_east_asia_font(st, "黑体", size_pt=18, bold=True, color_hex="0F172A")
            pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.first_line_indent = Pt(0)
            pf.space_before = Pt(30)
            pf.space_after = Pt(18)
            pf.keep_with_next = True
            pf.page_break_before = True
        elif sname == "Heading 2":
            set_east_asia_font(st, "黑体", size_pt=15, bold=True, color_hex="1E3A5F")
            pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
            pf.first_line_indent = Pt(0)
            pf.space_before = Pt(22)
            pf.space_after = Pt(12)
            pf.keep_with_next = True
        elif sname == "Heading 3":
            set_east_asia_font(st, "黑体", size_pt=12.5, bold=True, color_hex="1F2937")
            pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
            pf.first_line_indent = Pt(0)
            pf.space_before = Pt(14)
            pf.space_after = Pt(6)
            pf.keep_with_next = True
        elif sname == "TOC Heading":
            set_east_asia_font(st, "黑体", size_pt=16, bold=True, color_hex="0F172A")
            pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.first_line_indent = Pt(0)
            pf.space_before = Pt(18)
            pf.space_after = Pt(14)
            pf.page_break_before = True

    # 3. 逐段精细调整（区分卷/章分页、加粗金句框、参考文献与列表）
    in_references = False
    in_Main_Parts = False
    for p in d.paragraphs:
        sname = p.style.name if p.style else ""
        txt = (p.text or "").strip()

        if sname == "Heading 1":
            if txt == "参考文献":
                in_references = True
            if txt.startswith("第一部分") or txt.startswith("第二部分") or txt.startswith("第三部分"):
                in_Main_Parts = True
                p.paragraph_format.space_before = Pt(90)
                p.paragraph_format.space_after = Pt(24)
                pPr = p._element.get_or_add_pPr()
                pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:top w:val="single" w:sz="12" w:space="12" w:color="1E3A5F"/><w:bottom w:val="single" w:sz="12" w:space="12" w:color="1E3A5F"/></w:pBdr>')
                pPr.append(pBdr)
            elif txt.startswith("结语") or txt.startswith("附录") or txt.startswith("术语表") or txt.startswith("致谢") or txt == "参考文献":
                in_Main_Parts = False

        elif sname == "Heading 2":
            # 只有正三大幕里的“第X章”才另起一页并加章标题下划线；前言/结语/附录/参考文献内部的二级小节不另起一页
            if chapter_breaks and in_Main_Parts and not in_references:
                p.paragraph_format.page_break_before = True
                p.paragraph_format.space_before = Pt(24)
                p.paragraph_format.space_after = Pt(16)
                pPr = p._element.get_or_add_pPr()
                pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="8" w:space="6" w:color="1E3A5F"/></w:pBdr>')
                pPr.append(pBdr)
            else:
                p.paragraph_format.page_break_before = False
                p.paragraph_format.space_before = Pt(14)
                p.paragraph_format.space_after = Pt(6)
                for r in p.runs:
                    r.font.size = Pt(12.5)

        elif sname == "Heading 3":
            if in_references:
                p.paragraph_format.space_before = Pt(10)
                p.paragraph_format.space_after = Pt(4)
                for r in p.runs:
                    set_east_asia_font(r, "黑体", size_pt=11.0, bold=True, color_hex="1E3A5F")
            else:
                p.paragraph_format.space_before = Pt(14)
                p.paragraph_format.space_after = Pt(6)

        elif sname == "Captioned Figure" or sname == "Image Caption" or (txt.startswith("图 ") and len(txt) < 65):
            p.paragraph_format.first_line_indent = Pt(0)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(14)
            for r in p.runs:
                set_east_asia_font(r, "楷体", size_pt=9.5, bold=True, color_hex="475569")

        elif sname in ("Body Text", "First Paragraph", "Normal", "Compact"):
            if in_references:
                p.paragraph_format.first_line_indent = Pt(0)
                p.paragraph_format.left_indent = Pt(18)
                p.paragraph_format.first_line_indent = Pt(-18)
                p.paragraph_format.line_spacing = 1.25
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.size = Pt(9.0)
                    r.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)
            else:
                # 检查是否是整段加粗的核心结论卡（可带走物）
                non_empty_runs = [r for r in p.runs if (r.text or "").strip()]
                if non_empty_runs and all(r.bold for r in non_empty_runs) and len(txt) >= 18 and sname != "Compact":
                    p.paragraph_format.first_line_indent = Pt(0)
                    p.paragraph_format.left_indent = Cm(0.4)
                    p.paragraph_format.right_indent = Cm(0.4)
                    p.paragraph_format.space_before = Pt(8)
                    p.paragraph_format.space_after = Pt(8)
                    pPr = p._element.get_or_add_pPr()
                    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="F1F5F9"/>')
                    bdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:left w:val="single" w:sz="18" w:space="8" w:color="1E3A5F"/></w:pBdr>')
                    pPr.append(shd)
                    pPr.append(bdr)

    # 4. 全部表格升级为出版级“三线表 + 斑马纹 + 表头跨页重复”
    for tbl in d.tables:
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = True
        tblPr = tbl._tbl.tblPr
        if tblPr is not None:
            old_bdr = tblPr.find(qn("w:tblBorders"))
            if old_bdr is not None:
                tblPr.remove(old_bdr)
            borders = parse_xml(
                f'<w:tblBorders {nsdecls("w")}>'
                '<w:top w:val="single" w:sz="12" w:space="0" w:color="1E3A5F"/>'
                '<w:bottom w:val="single" w:sz="12" w:space="0" w:color="1E3A5F"/>'
                '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>'
                '<w:left w:val="none"/><w:right w:val="none"/><w:insideV w:val="none"/>'
                '</w:tblBorders>'
            )
            tblPr.append(borders)
            old_mar = tblPr.find(qn("w:tblCellMar"))
            if old_mar is not None:
                tblPr.remove(old_mar)
            cell_mar = parse_xml(
                f'<w:tblCellMar {nsdecls("w")}>'
                '<w:top w:w="110" w:type="dxa"/>'
                '<w:bottom w:w="110" w:type="dxa"/>'
                '<w:left w:w="140" w:type="dxa"/>'
                '<w:right w:w="140" w:type="dxa"/>'
                '</w:tblCellMar>'
            )
            tblPr.append(cell_mar)

        num_rows = len(tbl.rows)
        for r_idx, row in enumerate(tbl.rows):
            trPr = row._tr.get_or_add_trPr()
            cantSplit = OxmlElement("w:cantSplit")
            trPr.append(cantSplit)
            if r_idx == 0:
                tblHeader = OxmlElement("w:tblHeader")
                trPr.append(tblHeader)
            for cell in row.cells:
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                tcPr = cell._tc.get_or_add_tcPr()
                old_shd = tcPr.find(qn("w:shd"))
                if old_shd is not None:
                    tcPr.remove(old_shd)
                if r_idx == 0:
                    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="1E3A5F"/>')
                    tcPr.append(shd)
                elif r_idx % 2 == 0:
                    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="F8FAFC"/>')
                    tcPr.append(shd)

                for cp in cell.paragraphs:
                    cp.paragraph_format.first_line_indent = Pt(0)
                    cp.paragraph_format.line_spacing = 1.25
                    cp.paragraph_format.space_before = Pt(1)
                    cp.paragraph_format.space_after = Pt(1)
                    cp.paragraph_format.keep_together = True
                    # For medium/small tables (<= 9 rows), chain rows with keep_with_next so Word keeps the whole table on one page
                    if num_rows <= 9 and r_idx < num_rows - 1:
                        cp.paragraph_format.keep_with_next = True
                    cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    for cr in cp.runs:
                        set_east_asia_font(
                            cr,
                            "黑体" if r_idx == 0 else "宋体",
                            size_pt=9.5,
                            bold=(True if r_idx == 0 else cr.bold),
                            color_hex=("FFFFFF" if r_idx == 0 else "1F2328"),
                        )

    d.save(docx_path)


def build_epub_css(path):
    css = """body {
  font-family: "PingFang SC", "Songti SC", "STSong", "Noto Serif CJK SC", serif;
  line-height: 1.75;
  color: #1f2328;
  margin: 4%;
}
h1, h2, h3, h4 {
  font-family: "PingFang SC", "Heiti SC", "STHeiti", sans-serif;
  line-height: 1.35;
  margin-top: 1.2em;
  margin-bottom: 0.6em;
  color: #13293d;
}
h1 { font-size: 1.5em; border-bottom: 2px solid #16324f; padding-bottom: 0.35em; }
h2 { font-size: 1.28em; border-bottom: 1px solid #cbd5e1; padding-bottom: 0.25em; }
h3 { font-size: 1.12em; color: #1e3a5f; page-break-after: avoid; break-after: avoid; -webkit-column-break-after: avoid; }
p { margin: 0.6em 0; text-align: justify; }
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.75em 0;
  font-size: 0.84em;
  line-height: 1.42;
  page-break-inside: avoid;
  break-inside: avoid;
  -webkit-column-break-inside: avoid;
}
thead {
  display: table-header-group;
  page-break-after: avoid;
  break-after: avoid;
  -webkit-column-break-after: avoid;
}
tr {
  page-break-inside: avoid;
  break-inside: avoid;
  -webkit-column-break-inside: avoid;
}
th, td {
  border: 1px solid #cbd5e1;
  padding: 5px 7px;
  text-align: left;
  vertical-align: top;
  page-break-inside: avoid;
  break-inside: avoid;
  -webkit-column-break-inside: avoid;
}
th { background-color: #16324f; color: #ffffff; font-weight: bold; }
tbody tr:nth-child(even) { background-color: #f8fafc; }
blockquote { border-left: 3px solid #c87d55; padding-left: 0.9em; color: #475569; margin: 0.8em 0; background: #faf8f3; }
figure {
  margin: 0.8em auto;
  text-align: center;
  page-break-inside: avoid;
  break-inside: avoid;
  -webkit-column-break-inside: avoid;
  max-width: 100%;
}
figure img, img {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  max-height: 76vh;
  width: auto;
  height: auto;
  object-fit: contain;
  border-radius: 6px;
}
figcaption {
  font-size: 0.85em;
  line-height: 1.4;
  color: #475569;
  margin-top: 0.45em;
  font-weight: bold;
  text-align: center;
  page-break-before: avoid;
  break-before: avoid;
}
.part-banner {
  background: #16324f;
  color: #ffffff;
  padding: 0.7em 1em;
  border-radius: 6px;
  border-left: 5px solid #c87d55;
  margin: 0.4em 0 1em 0;
}
.part-banner-title {
  font-weight: bold;
  font-size: 1.05em;
  letter-spacing: 0.05em;
  color: #fde68a;
}
.part-banner-sub {
  font-size: 0.85em;
  color: #e2e8f0;
  margin-top: 0.25em;
  line-height: 1.45;
}
"""
    open(path, "w", encoding="utf-8").write(css)
    return path


def to_epub(src_md, dst, css_path, cover_path=None):
    src_dir = os.path.dirname(os.path.abspath(src_md))
    # For EPUB, merge part-header blocks (`# 第一部分 ...` + part intro quote) directly into
    # the top of the immediately following chapter so pandoc `--split-level=2` doesn't emit
    # standalone nearly-empty part-divider pages (`ch002.xhtml`, `ch006.xhtml`, `ch012.xhtml`).
    raw_md = open(src_md, encoding="utf-8").read()
    def _merge_part_into_chapter(m):
        part_title = m.group(1).strip()
        part_quote = (m.group(2) or "").strip()
        ch_heading = m.group(3).strip()
        q_lines = [ln.lstrip(">").strip() for ln in part_quote.splitlines() if ln.strip()]
        sub_txt = " · ".join(q_lines) if q_lines else ""
        banner = (
            f'<div class="part-banner">'
            f'<div class="part-banner-title">{part_title}</div>'
            + (f'<div class="part-banner-sub">{sub_txt}</div>' if sub_txt else "")
            + f'</div>'
        )
        return f"## {ch_heading}\n\n{banner}\n"

    epub_md_text = re.sub(
        r"^#\s+(第[一二三四五六七八九十]+部分[^\n]*)\n+((?:>[^\n]*\n)+)?\s*##\s+([^\n]+)",
        _merge_part_into_chapter,
        raw_md,
        flags=re.M,
    )
    tmp_epub_md = os.path.join(src_dir, "_book_epub.md")
    open(tmp_epub_md, "w", encoding="utf-8").write(epub_md_text)
    cmd = [
        "pandoc", tmp_epub_md, "-o", dst,
        "--toc", "--toc-depth=2", "--split-level=2",
        f"--css={css_path}", f"--resource-path={src_dir}",
        "-M", "toc-title=目录", "--quiet",
    ]
    if cover_path and os.path.exists(cover_path):
        cmd.append(f"--epub-cover-image={cover_path}")
    subprocess.run(cmd, check=True)
    if os.path.exists(tmp_epub_md):
        os.remove(tmp_epub_md)


def audit_epub(epub_path):
    """Verify EPUB quality: no raw [E0xx] leaks, no empty/stub chapter xhtml files, and table break-inside protection."""
    with zipfile.ZipFile(epub_path, "r") as z:
        css_files = [n for n in z.namelist() if n.endswith(".css")]
        css_blob = "\n".join(z.read(c).decode("utf-8", errors="ignore") for c in css_files)
        if "-webkit-column-break-inside: avoid" not in css_blob or "break-inside: avoid" not in css_blob:
            sys.exit("EPUB audit FAILED: CSS missing table/figure break-inside: avoid rules")
        xhtmls = sorted(n for n in z.namelist() if n.startswith("EPUB/text/ch") and n.endswith(".xhtml"))
        stub_pages = []
        e_leaks = []
        tbl_count = 0
        for n in xhtmls:
            raw = z.read(n).decode("utf-8", errors="ignore")
            tbl_count += len(re.findall(r"<table\b", raw))
            plain = re.sub(r"<[^>]+>", " ", raw)
            plain = re.sub(r"\s+", " ", plain).strip()
            leaks = re.findall(r"E0\d\d", plain)
            if leaks:
                e_leaks.append((n, leaks))
            if len(plain) < 120:
                stub_pages.append((n, len(plain), plain[:60]))
        if e_leaks:
            sys.exit(f"EPUB audit FAILED: raw [E0xx] tags leaked in {e_leaks}")
        if stub_pages:
            sys.exit(f"EPUB audit FAILED: nearly-empty stub pages (<120 chars) found: {stub_pages}")
        print(f"EPUB audit PASS: {len(xhtmls)} chapters, {tbl_count} tables protected against page-split, 0 stub/blank pages, 0 [E0xx] citation leaks")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    a = p.parse_args()
    proj = os.path.abspath(a.project_dir)
    if not shutil.which("pandoc"):
        sys.exit("pandoc not found; install it (brew install pandoc) and rerun")
    pkg = os.path.join(proj, "10_package")
    book_md = os.path.join(pkg, "book.md")
    if not os.path.exists(book_md):
        sys.exit("10_package/book.md missing; run assemble.py first")
    state = load_state(proj)
    pos_path = os.path.join(proj, "03_positioning", "positioning.md")
    book_title = "书稿"
    if os.path.exists(pos_path):
        m = re.search(r"^-\s*书名[:：]\s*(.+)$", open(pos_path, encoding="utf-8").read(), re.M)
        if m:
            book_title = m.group(1).strip().strip("《》")
    ref = build_reference_doc(os.path.join(pkg, "_reference.docx"))
    sub = os.path.join(pkg, "投稿包")
    os.makedirs(sub, exist_ok=True)

    has_parts = any(split_front(open(f, encoding="utf-8").read())[0].get("part") for f in draft_files(proj))
    to_docx(book_md, os.path.join(pkg, "book.docx"), ref, toc=True, chapter_breaks=has_parts, book_title=book_title)
    shutil.copy(os.path.join(pkg, "book.docx"), os.path.join(sub, "全书稿.docx"))

    # Export EPUB with embedded cover and chapter figures
    epub_css = build_epub_css(os.path.join(pkg, "_epub.css"))
    cover_img = None
    for cname in ("cover.jpg", "cover.png"):
        cpath = os.path.join(pkg, cname)
        if os.path.exists(cpath):
            cover_img = cpath
            shutil.copy(cpath, os.path.join(sub, "封面" + os.path.splitext(cname)[1]))
            break
    to_epub(book_md, os.path.join(pkg, "book.epub"), epub_css, cover_path=cover_img)
    audit_epub(os.path.join(pkg, "book.epub"))
    shutil.copy(os.path.join(pkg, "book.epub"), os.path.join(sub, "全书稿.epub"))

    proposal = os.path.join(pkg, "proposal.md")
    if os.path.exists(proposal):
        to_docx(proposal, os.path.join(sub, "选题策划书.docx"), ref)
    else:
        print("warning: 10_package/proposal.md missing", file=sys.stderr)
    marketing = os.path.join(pkg, "marketing.md")
    if os.path.exists(marketing):
        to_docx(marketing, os.path.join(sub, "营销文案.docx"), ref)

    samples = [str(x) for x in state.get("sample_chapters", [])]
    parts = []
    for f in draft_files(proj):
        meta, body = split_front(open(f, encoding="utf-8").read())
        if str(meta.get("chapter")) in samples or str(meta.get("chapter")).lstrip("0") in samples:
            body = re.sub(r"\[(?:E\d{3,4}(?:\s*[,，、/]\s*)*)+\]", "", COMMENT_RE.sub("", body))
            parts.append(f"# {meta.get('title', '')}\n\n" + body.strip())
    if parts:
        tmp = os.path.join(pkg, "_samples.md")
        open(tmp, "w", encoding="utf-8").write("\n\n".join(parts))
        to_docx(tmp, os.path.join(sub, "样章.docx"), ref)
        os.remove(tmp)
    else:
        print("warning: state.json sample_chapters empty or unmatched", file=sys.stderr)

    for src, out in ((os.path.join(pkg, "verify_list.md"), "待核实清单.md"),
                     (os.path.join(pkg, "lint_report.md"), "检查报告.md"),
                     (os.path.join(proj, "05_architecture", "outline.md"), "目录大纲.md")):
        if os.path.exists(src):
            shutil.copy(src, os.path.join(sub, out))

    zpath = os.path.join(pkg, "投稿包.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for fn in sorted(os.listdir(sub)):
            z.write(os.path.join(sub, fn), arcname=os.path.join("投稿包", fn))
    print("wrote", os.path.join(pkg, "book.docx"))
    print("wrote", zpath, "with", sorted(os.listdir(sub)))
    print("note: zip entries use UTF-8 names; `unzip -l` may show them garbled, use `unzip -O UTF-8` or Finder")


if __name__ == "__main__":
    main()
