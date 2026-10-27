#!/usr/bin/env python3
"""Book-level checks: chapter count, part shares, chapter sizes, disclaimers, concept recurrence, cross-references.

Usage: book_check.py <project_dir> [--concepts 概念A,概念B] [--sample]
Concepts default to 03_positioning/positioning.md (总概念 line + 子概念 table, with an optional 别名 column).
--sample checks only what makes sense for a partial manuscript (sample chapters): skips chapter count,
part shares and concept recurrence.
"""
import argparse, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load_config, split_front, strip_markup, count_chars, draft_files

CN_NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}


def cn_to_int(s):
    if s.isdigit():
        return int(s)
    if "十" in s:
        a, _, b = s.partition("十")
        return (CN_NUM.get(a, 1) if a else 1) * 10 + (CN_NUM.get(b, 0) if b else 0)
    return CN_NUM.get(s, 0)


def concepts_from_positioning(project):
    """Return [(name, [aliases...])]."""
    path = os.path.join(project, "03_positioning", "positioning.md")
    if not os.path.exists(path):
        return []
    text = open(path, encoding="utf-8").read()
    out = []
    m = re.search(r"^-\s*总概念[:：]\s*(.+)$", text, re.M)
    if m and m.group(1).strip():
        out.append((m.group(1).strip(), []))
    header, alias_col = None, None
    for line in text.splitlines():
        if line.startswith("| 子概念"):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            alias_col = header.index("别名") if "别名" in header else None
            continue
        if header is not None:
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not cells[0] or set(cells[0]) <= set("-: "):
                continue
            aliases = []
            if alias_col is not None and alias_col < len(cells):
                aliases = [x.strip() for x in re.split(r"[、,，/]", cells[alias_col]) if x.strip()]
            out.append((cells[0], aliases))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    p.add_argument("--concepts", default="")
    p.add_argument("--sample", action="store_true")
    a = p.parse_args()
    cfg = load_config()["book"]
    proj = a.project_dir
    fails, warns = [], []
    chapters = []
    for f in draft_files(proj):
        meta, body = split_front(open(f, encoding="utf-8").read())
        chapters.append((os.path.basename(f), meta, body, count_chars(body)))
    back = os.path.join(proj, "09_backmatter")
    back_files = sorted(x for x in os.listdir(back) if x.endswith(".md")) if os.path.isdir(back) else []
    back_text = "\n".join(split_front(open(os.path.join(back, x), encoding="utf-8").read())[1] for x in back_files)
    total_body = sum(c[3] for c in chapters) or 1
    planned = 0
    state_path = os.path.join(proj, "state.json")
    if os.path.exists(state_path):
        planned = len(json.load(open(state_path, encoding="utf-8")).get("chapters", {}))

    if not a.sample:
        lo, hi = cfg["chapters"]
        if not lo <= len(chapters) <= hi:
            fails.append(f"{len(chapters)} chapters; expected {lo}-{hi}")
        parts = {}
        for _, meta, _, n in chapters:
            part = meta.get("part", "")
            parts[part] = parts.get(part, 0) + n
        parts = list(parts.items())
        print("part shares (chapters only):")
        for name, n in parts:
            print(f"  {name or '(no part)'}: {n} chars, {n / total_body:.0%}")
        if len(parts) >= 2:
            first, last = parts[0][1] / total_body, parts[-1][1] / total_body
            if not cfg["first_part_share"][0] <= first <= cfg["first_part_share"][1]:
                warns.append(f"first part share {first:.0%} outside {cfg['first_part_share']}")
            if not cfg["last_part_share"][0] <= last <= cfg["last_part_share"][1]:
                fails.append(f"method part share {last:.0%} outside {cfg['last_part_share']}")
        else:
            warns.append("drafts have no 'part' field; cannot check the three-act split")
        for name, meta, _, n in chapters:
            if n / total_body > cfg["max_chapter_share"]:
                warns.append(f"{name} is {n / total_body:.0%} of the book (max {cfg['max_chapter_share']:.0%})")
    for name, meta, _, n in chapters:
        if n < cfg["min_chapter_chars"]:
            warns.append(f"{name} has only {n} chars (min {cfg['min_chapter_chars']})")

    everything = strip_markup("\n".join(c[2] for c in chapters) + "\n" + back_text)
    disclaimers = len(re.findall(cfg["disclaimer_regex"], everything))
    if disclaimers < cfg["disclaimer_min"]:
        fails.append(f"only {disclaimers} disclaimer / see-your-doctor statements (min {cfg['disclaimer_min']})")
    if back_files and not re.search(cfg["disclaimer_regex"], strip_markup(back_text)):
        warns.append("preface/backmatter has no disclaimer; the preface must carry one")

    concepts = [(c.strip(), []) for c in a.concepts.split(",") if c.strip()] or concepts_from_positioning(proj)
    if concepts:
        print("concept recurrence (chapters containing the concept or an alias):")
        for name, aliases in concepts:
            hits = [fn for fn, _, body, _ in chapters if any(t in body for t in [name] + aliases)]
            print(f"  {name}{' / ' + '、'.join(aliases) if aliases else ''}: {len(hits)} {hits}")
            if not a.sample and len(hits) < 3:
                warns.append(f"concept '{name}' appears in {len(hits)} chapters (min 3)")
    else:
        warns.append("no concepts found in positioning.md")

    limit = max(planned, len(chapters))
    refs = re.findall(r"第\s*([一二三四五六七八九十\d]+)\s*章", everything)
    bad = sorted({r for r in refs if not 1 <= cn_to_int(r) <= limit}, key=cn_to_int)
    if bad:
        fails.append(f"cross-references to chapters that are not in the plan (1-{limit}): 第{bad}章")

    for w in warns:
        print("[WARN]", w)
    for f in fails:
        print("[FAIL]", f)
    print("PASS" if not fails else f"FAIL ({len(fails)})")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
