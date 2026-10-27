#!/usr/bin/env python3
"""Assemble drafts + front/back matter into 10_package/book.md, with numbered endnotes.

Also writes 10_package/verify_list.md (all 【待核实】 items) and 10_package/lint_report.md.
"""
import argparse, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import split_front, COMMENT_RE, draft_files, evidence_ids, count_chars

PARTS_ORDER = ["preface"]  # front matter files in 09_backmatter, in this order if present
BACK_ORDER = ["afterword", "appendix", "glossary", "acknowledgements"]


def read(path):
    return open(path, encoding="utf-8").read()


def evidence_sources(project):
    path = os.path.join(project, "06_evidence", "evidence_bank.md")
    if not os.path.exists(path):
        return {}
    text = read(path)
    out = {}
    for block in re.split(r"(?=^###\s*E\d{3,4})", text, flags=re.M):
        m = re.match(r"###\s*(E\d{3,4})", block)
        if not m:
            continue
        src = re.search(r"^-\s*来源[:：]\s*(.+)$", block, re.M)
        out[m.group(1)] = src.group(1).strip() if src else "（来源缺失）"
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    a = p.parse_args()
    proj = os.path.abspath(a.project_dir)
    back = os.path.join(proj, "09_backmatter")
    sources = evidence_sources(proj)
    title = ""
    pos = os.path.join(proj, "03_positioning", "positioning.md")
    if os.path.exists(pos):
        m = re.search(r"^-\s*书名[:：]\s*(.+)$", read(pos), re.M)
        title = m.group(1).strip() if m else ""

    subtitle, author = "", ""
    if os.path.exists(pos):
        m = re.search(r"^-\s*副标题[:：]\s*(.+)$", read(pos), re.M)
        subtitle = m.group(1).strip() if m else ""
    st = os.path.join(proj, "state.json")
    if os.path.exists(st):
        author = json.load(open(st, encoding="utf-8")).get("doctor", "")
    # JSON strings are valid YAML scalars, so quotes and colons in titles stay safe.
    meta_lines = [f"title: {json.dumps(title or '书稿', ensure_ascii=False)}"]
    if subtitle:
        meta_lines.append(f"subtitle: {json.dumps(subtitle, ensure_ascii=False)}")
    if author:
        meta_lines.append(f"author: {json.dumps(author, ensure_ascii=False)}")
    meta_lines.append("lang: zh-CN")
    out = ["---\n" + "\n".join(meta_lines) + "\n---\n"]
    notes_md = ["# 参考文献\n"]
    for name in PARTS_ORDER:
        f = os.path.join(back, name + ".md")
        if os.path.exists(f):
            pbody = split_front(read(f))[1].strip()
            porder = []
            def prepl(m):
                eid = m.group(1)
                if eid not in porder:
                    porder.append(eid)
                return f"^\\[{porder.index(eid) + 1}\\]^"
            pbody = re.sub(r"\[(E\d{3,4})\]", prepl, pbody)
            out.append(pbody + "\n")
            if porder:
                notes_md.append("## 前言\n")
                for i, eid in enumerate(porder, 1):
                    notes_md.append(f"{i}. {sources.get(eid, '（证据库中缺少 ' + eid + '）')}")
                notes_md.append("")
    verify = ["# 待核实清单\n", "以下内容需要医生本人或出版社医学审读确认后才能定稿。\n",
              "## 每本书都必须复核的项目\n",
              "- 书名、副标题、作者署名和人设表述是否符合医生本人意愿",
              "- 前言中的作者经历、家人故事是否属实、是否同意公开",
              "- 每个来自素材的病例（下方列出）是否已获患者同意或已充分去标识化",
              "- 所有药物名称、剂量、适用人群、禁忌（下方列出含药物或剂量的段落）",
              "- 所有指标参考范围和指南目标值是否与最新版指南一致",
              "- 证据库中标为“未联网核验”的条目",
              "- 选题策划书中的作者平台数据、门诊量、荣誉\n",
              "## 正文中的【待核实】\n"]
    verify_base = len(verify)
    case_refs, drug_paras, figures = [], [], []
    drug_re = re.compile(r"\d+(?:\.\d+)?\s*(?:mg|毫克|μg|微克|IU|国际单位)|(?:服|吃|口服)\s*(?:\d+|[一两二三四五六七八九十半]+)\s*(?:片|粒|袋|支|丸|颗)|二甲双胍|打胰岛素|注射胰岛素|胰岛素治疗|他汀|阿司匹林|降压药|降糖药")
    drafts = [(f, *split_front(read(f))) for f in draft_files(proj)]
    has_parts = any(meta.get("part") for _, meta, _ in drafts)
    # Drafts use "##" for their own subsections. Chapters sit one level below parts when parts exist.
    ch_level = 2 if has_parts else 1
    current_part = None
    for f, meta, body in drafts:
        part = meta.get("part")
        if part and part != current_part:
            out.append(f"# {part}\n")
            current_part = part
        raw_title = meta.get("title", os.path.basename(f))
        ch_num = str(meta.get("chapter", "")).strip()
        if ch_num.isdigit() and int(ch_num) > 0 and not raw_title.startswith("第"):
            CN_CH = {1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十",11:"十一",12:"十二",13:"十三",14:"十四",15:"十五"}
            cnum = CN_CH.get(int(ch_num), ch_num)
            heading = f"第{cnum}章  {raw_title}"
        else:
            heading = raw_title
        for cid in dict.fromkeys(re.findall(r"<!--\s*src:\s*(C\d+)", body)):
            case_refs.append(f"- {heading}：素材病例 {cid}")
        for para in re.split(r"\n\s*\n", COMMENT_RE.sub("", body)):
            if drug_re.search(para):
                clean_p = re.sub(r"\s+", " ", para.strip())[:80]
                drug_paras.append(f"- {heading}：{clean_p}…")
        for fig in re.findall(r"【插图[:：]([^】]*)】", body):
            figures.append(f"- {heading}：{fig.strip()}")
        body = COMMENT_RE.sub("", body).strip()
        body = re.sub(r"^#\s.*\n?", "", body, count=1) if body.startswith("# ") else body
        shift = ch_level - 1
        body = re.sub(r"^(#{2,5})(?=\s)", lambda m: "#" * min(6, len(m.group(1)) + shift), body, flags=re.M)
        order = []
        def repl(m):
            eid = m.group(1)
            if eid not in order:
                order.append(eid)
            # Escaped brackets: bare ^[...] is pandoc inline-footnote syntax.
            return f"^\\[{order.index(eid) + 1}\\]^"
        body = re.sub(r"\[(E\d{3,4})\]", repl, body)

        # Inject chapter infographic figure if present in 10_package/figures/
        # Priority: 1) 10_package/figures/manifest.json ({ "01": {"file": "figures/ch01.png", "caption": "图 1-1 ..."}, ... })
        #           2) Convention file 10_package/figures/ch<NN>.png (caption from chapter YAML `figure_caption` or auto-built)
        fig_manifest_path = os.path.join(proj, "10_package", "figures", "manifest.json")
        fig_manifest = json.load(open(fig_manifest_path, encoding="utf-8")) if os.path.exists(fig_manifest_path) else {}
        ch_key = str(meta.get("chapter", "")).zfill(2)
        fig_rel, fig_cap = None, None
        if ch_key in fig_manifest:
            entry = fig_manifest[ch_key]
            fig_rel = entry.get("file") if isinstance(entry, dict) else entry[0]
            fig_cap = entry.get("caption") if isinstance(entry, dict) else entry[1]
        else:
            for cand in (f"figures/ch{ch_key}.png", f"figures/fig{ch_key}.png"):
                if os.path.exists(os.path.join(proj, "10_package", cand)):
                    fig_rel = cand
                    fig_cap = meta.get("figure_caption") or f"图 {int(ch_key) if ch_key.isdigit() else ch_key}-1  {raw_title}核心图解"
                    break
        if fig_rel and os.path.exists(os.path.join(proj, "10_package", fig_rel)) and f"]({fig_rel})" not in body:
            fig_md = f"\n\n![{fig_cap}]({fig_rel})\n\n"
            # Insert right before the second subsection heading (so it sits after section 1)
            headings_iter = list(re.finditer(r"^#{2,5}\s+.+$", body, flags=re.M))
            if len(headings_iter) >= 2:
                pos_idx = headings_iter[1].start()
                body = body[:pos_idx].rstrip() + fig_md + body[pos_idx:]
            else:
                body = body + fig_md

        out.append("#" * ch_level + f" {heading}\n\n" + body + "\n")
        if order:
            notes_md.append(f"## {heading}\n")
            for i, eid in enumerate(order, 1):
                notes_md.append(f"{i}. {sources.get(eid, '（证据库中缺少 ' + eid + '）')}")
            notes_md.append("")
        for item in re.findall(r"【待核实[:：]?([^】]*)】", body):
            verify.append(f"- {heading}：{item.strip()}")

    if len(verify) == verify_base:
        verify.append("- （正文中没有【待核实】标记；仍需按上面的必查项逐条复核）")
    verify += ["\n## 素材病例\n"] + (case_refs or ["- （无）"])
    verify += ["\n## 含药物或剂量的段落\n"] + (drug_paras or ["- （无）"])
    verify += ["\n## 插图需求\n"] + (figures or ["- （无）"])

    for name in BACK_ORDER:
        for fn in sorted(os.listdir(back)) if os.path.isdir(back) else []:
            if fn.startswith(name) and fn.endswith(".md"):
                bmeta, bbody = split_front(read(os.path.join(back, fn)))
                bbody = bbody.strip()
                border = []
                def brepl(m):
                    eid = m.group(1)
                    if eid not in border:
                        border.append(eid)
                    return f"^\\[{border.index(eid) + 1}\\]^"
                bbody = re.sub(r"\[(E\d{3,4})\]", brepl, bbody)
                out.append(bbody + "\n")
                if border:
                    btitle = bmeta.get("title") or fn.replace(".md", "")
                    notes_md.append(f"## {btitle}\n")
                    for i, eid in enumerate(border, 1):
                        notes_md.append(f"{i}. {sources.get(eid, '（证据库中缺少 ' + eid + '）')}")
                    notes_md.append("")
    out.append("\n".join(notes_md))

    pkg = os.path.join(proj, "10_package")
    os.makedirs(pkg, exist_ok=True)
    book = "\n\n".join(out)
    open(os.path.join(pkg, "book.md"), "w", encoding="utf-8").write(book)
    open(os.path.join(pkg, "verify_list.md"), "w", encoding="utf-8").write("\n".join(verify) + "\n")

    lint = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lint_chapter.py")
    report, failed = ["# 逐章检查报告\n"], 0
    for f in draft_files(proj):
        r = subprocess.run([sys.executable, lint, f, "--project", proj], capture_output=True, text=True)
        failed += r.returncode != 0
        report.append("```\n" + r.stdout.strip() + "\n```\n")
    open(os.path.join(pkg, "lint_report.md"), "w", encoding="utf-8").write("\n".join(report))
    pending_n = len(re.findall(r"【待核实", book))
    print(f"book.md: {count_chars(book)} chars; chapters failing lint: {failed}; 【待核实】: {pending_n}; drug/dose paragraphs: {len(drug_paras)}; figures: {len(figures)}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
