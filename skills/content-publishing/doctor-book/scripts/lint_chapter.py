#!/usr/bin/env python3
"""Lint one chapter draft: style metrics, evidence tags, compliance, fabrication guards.

Exit 0 = pass (warnings allowed), 1 = at least one FAIL.
"""
import argparse, json, os, re, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load_config, split_front, strip_markup, count_chars, evidence_ids

SENT_SPLIT = re.compile(r"(?<=[。！？!?；])")
RISK_VERBS = "降低|减少|增加|升高|提高|下降|上升|增高"
RISK_RE = re.compile(rf"(?:{RISK_VERBS})[^。]{{0,12}}\d+(?:\.\d+)?\s*%[^。]{{0,10}}风险|风险[^。]{{0,12}}(?:{RISK_VERBS})[^。]{{0,8}}\d+(?:\.\d+)?\s*%|风险[^。]{{0,6}}\d+(?:\.\d+)?\s*倍")
LIST_LINE = re.compile(r"^\s*(?:[-*+]|\d+[.、)]|[①-⑳]|□|☐)\s+", re.M)


def paragraphs(body):
    paras = []
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if not b or b.startswith("#") or b.startswith("<!--") or b.startswith("|"):
            continue
        if LIST_LINE.match(b):
            continue
        paras.append(b)
    return paras


def per_k(n, chars):
    return n / chars * 1000 if chars else 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("draft")
    p.add_argument("--project", help="project dir (for evidence bank); default: inferred")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    cfg = load_config()
    raw = open(a.draft, encoding="utf-8").read()
    meta, body = split_front(raw)
    project = a.project or os.path.dirname(os.path.dirname(os.path.abspath(a.draft)))
    results = []

    def add(level, check, msg):
        results.append({"level": level, "check": check, "msg": msg})

    for k in ("chapter", "type", "title", "budget"):
        if k not in meta:
            add("FAIL", "frontmatter", f"missing '{k}' in YAML front matter")
    ctype = meta.get("type", "argument")
    if ctype not in cfg["types"]:
        add("FAIL", "frontmatter", f"unknown type '{ctype}', use one of {list(cfg['types'])}")
        ctype = "argument"
    th = cfg["types"][ctype]

    plain = strip_markup(body)
    chars = count_chars(body)
    paras = paragraphs(body)
    para_lens = [count_chars(x) for x in paras] or [0]
    sents = [s for s in SENT_SPLIT.split(re.sub(r"\s+", "", plain)) if count_chars(s) > 1]
    sent_lens = [count_chars(s) for s in sents] or [0]
    metrics = {
        "chars": chars,
        "para_median": statistics.median(para_lens),
        "sent_median": statistics.median(sent_lens),
        "headings_per_k": per_k(len(re.findall(r"^#{2,4}\s", body, re.M)), chars),
        "questions_per_k": per_k(len(re.findall(r"[？?]", plain)), chars),
        "first_person_per_k": per_k(len(re.findall(r"我", plain)), chars),
        "second_person_per_k": per_k(len(re.findall(r"[你您]", plain)), chars),
        "numbers_per_k": per_k(len(re.findall(r"\d+(?:\.\d+)?", plain)), chars),
        "research_per_k": per_k(len(re.findall(cfg["research_count_regex"], plain)), chars),
    }
    for key in ("para_median", "sent_median", "headings_per_k", "questions_per_k", "first_person_per_k",
                "second_person_per_k", "numbers_per_k", "research_per_k"):
        lo, hi = th[key]
        v = metrics[key]
        if not lo <= v <= hi:
            add("WARN", "style", f"{key}={v:.1f} outside [{lo}, {hi}] for type '{ctype}'")

    long_share = sum(1 for n in sent_lens if n >= cfg["long_sentence_chars"]) / len(sent_lens)
    if long_share > cfg["long_sentence_max_share"]:
        add("WARN", "style", f"{long_share:.0%} of sentences are ≥{cfg['long_sentence_chars']} chars (max {cfg['long_sentence_max_share']:.0%})")
    if per_k(len(re.findall(r"[！!]", plain)), chars) > cfg["exclamations_max_per_k"]:
        add("WARN", "style", "too many exclamation marks; let the facts carry the emotion")

    budget = int(meta.get("budget") or 0)
    if budget and abs(chars - budget) / budget > 0.15:
        add("FAIL", "budget", f"{chars} chars vs budget {budget} (>±15%)")

    # Take-away spacing: list items, bold lines, callouts, tables count as anchors.
    anchors = [m.start() for m in re.finditer(r"^\s*(?:[-*+]\s|\d+[.、)]\s|>\s|\||\*\*)", body, re.M)]
    gaps, prev = [], 0
    for pos in anchors + [len(body)]:
        gaps.append(count_chars(body[prev:pos]))
        prev = pos
    if gaps and max(gaps) > th["max_takeaway_gap"]:
        add("WARN", "takeaway", f"longest stretch without a take-away is {max(gaps)} chars (max {th['max_takeaway_gap']})")

    first = paras[0] if paras else ""
    if any(first[:40].find(w) >= 0 for w in cfg["definition_openings"]):
        add("FAIL", "opening", "chapter opens with a definition; open on a scene, person or moment")

    tail = body[int(len(body) * 0.70):]
    if th["ending_list_required"] and not LIST_LINE.search(tail):
        add("FAIL", "ending", f"type '{ctype}' needs an action list in the last 30% of the chapter")
    last = paras[-1] if paras else ""
    if any(last.startswith(w) for w in cfg["summary_endings"]):
        add("WARN", "ending", "last paragraph is a recap; end on a callback, an image, a question or the next step")

    if th["redflag_required"] and not re.search(cfg["redflag_regex"], plain):
        add("FAIL", "redflag", f"type '{ctype}' must tell readers when to see a doctor (就医红线)")
    if ctype not in ("essay", "plan") and not re.search(cfg["bridge_regex"], strip_markup(body)[-300:]):
        add("WARN", "bridge", "no hand-off to the next chapter in the last 300 chars")

    fear = re.compile(cfg["fear_regex"])
    action = re.compile(cfg["action_regex"], re.M)
    flagged_until = -1
    fear_hits = 0
    for m in fear.finditer(body):
        if m.start() < flagged_until:
            continue
        window = body[m.end(): m.end() + cfg["fear_action_window"]]
        if not action.search(window):
            fear_hits += 1
            flagged_until = m.end() + cfg["fear_action_window"]
            if fear_hits <= 3:
                ctx = strip_markup(body[max(0, m.start() - 10): m.end() + 20]).replace("\n", " ")
                add("WARN", "fear_action", f"frightening fact without an action within {cfg['fear_action_window']} chars: …{ctx}…")
    if fear_hits > 3:
        add("WARN", "fear_action", f"{fear_hits - 3} more fear passages without a nearby action")

    if (re.search(cfg["dose_regex"], plain) or re.search(cfg["pill_count_regex"], plain)) and not re.search(cfg["contraindication_regex"], plain):
        add("FAIL", "dose", "dose given without contraindications / interactions / 需医生评估")
    for para in paras:
        if re.search(cfg["score_regex"], para) and re.search(cfg["dose_regex"], para):
            add("FAIL", "dose", f"self-test score mapped directly to a dose; map it to an action level and a re-check instead: {strip_markup(para)[:40]}…")
    if re.search(cfg["child_scaling_regex"], plain):
        add("FAIL", "dose", "children's dose scaled by weight or halved; write 需儿科医生评估 instead")

    for w in cfg["banned_hard"]:
        for m in re.finditer(re.escape(w), plain):
            ctx = plain[max(0, m.start() - 15): m.end() + 15].replace("\n", " ")
            add("FAIL", "compliance", f"banned phrase '{w}': …{ctx}…")
    # Claims are allowed when negated ("目前还不能治愈", "不能替代药物").
    negation = re.compile(cfg["negation_regex"])
    for w in cfg["banned_claims"]:
        for m in re.finditer(re.escape(w), plain):
            before = plain[max(0, m.start() - 8): m.start()]
            for filler in ("不仅", "不但", "不只"):
                before = before.replace(filler, "")
            if negation.search(before):
                continue
            ctx = plain[max(0, m.start() - 15): m.end() + 15].replace("\n", " ")
            add("FAIL", "compliance", f"unqualified claim '{w}': …{ctx}…")

    for w in cfg["medication_change_terms"]:
        for m in re.finditer(re.escape(w), plain):
            window = plain[max(0, m.start() - 80): m.end() + 80]
            if not any(g in window for g in cfg["medication_guard_terms"]):
                add("FAIL", "medication", f"'{w}' without a see-your-doctor guard within 80 chars")

    bank = evidence_ids(project)
    tags = set(re.findall(r"\[(E\d{3,4})\]", body))
    for t in sorted(tags):
        if t not in bank:
            add("FAIL", "evidence", f"[{t}] not found in 06_evidence/evidence_bank.md")
    for para in paras:
        if any(w in para for w in cfg["research_terms"]) and not re.search(r"\[E\d{3,4}\]", para):
            add("FAIL", "evidence", f"research claim without [E###] tag: {strip_markup(para)[:50]}…")
        para_sents = [s for s in SENT_SPLIT.split(para) if s.strip()]
        for i, s in enumerate(para_sents):
            if RISK_RE.search(s):
                window = s + (para_sents[i + 1] if i + 1 < len(para_sents) else "")
                if not any(w in window for w in cfg["absolute_risk_terms"]):
                    add("FAIL", "risk", f"relative risk without absolute risk in the same or next sentence: {strip_markup(s)[:50]}…")

    has_src = re.search(r"<!--\s*src:\s*C\d+", body) is not None
    disclosed = any(w in plain for w in cfg["case_disclosure"])
    case_paras = [x for x in paras if re.search(cfg["age_regex"], x) and re.search(cfg["case_marker_regex"], x)]
    if case_paras and not (has_src or disclosed):
        add("FAIL", "fabrication", "patient case found but no <!-- src: C## --> tag and no 情景示例/复合案例 disclosure")

    ai_hits = sum(plain.count(w) for w in cfg["ai_flavour"])
    if per_k(ai_hits, chars) > cfg["ai_flavour_max_per_k"]:
        found = [w for w in cfg["ai_flavour"] if w in plain]
        add("WARN", "ai_flavour", f"{ai_hits} stock phrases ({per_k(ai_hits, chars):.2f}/k): {found}")

    contrast = len(re.findall(cfg["contrast_regex"], plain))
    if per_k(contrast, chars) > cfg["contrast_max_per_k"]:
        add("WARN", "ai_flavour", f"{contrast} '不是……而是……' turns ({per_k(contrast, chars):.2f}/k); keep the strongest one or two")
    scaffold = len(re.findall(cfg["scaffold_regex"], plain))
    if scaffold > cfg["scaffold_max"]:
        add("WARN", "ai_flavour", f"{scaffold} 第一/第二/第三 scaffolds; turn some into prose or a list")

    pending = re.findall(r"【待核实[:：]?[^】]*】", body)
    if pending:
        add("INFO", "verify", f"{len(pending)} 【待核实】 placeholders")

    fails = [r for r in results if r["level"] == "FAIL"]
    out = {"file": a.draft, "type": ctype, "metrics": {k: round(v, 1) for k, v in metrics.items()},
           "pass": not fails, "results": results}
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"{os.path.basename(a.draft)}  type={ctype}  " + "  ".join(f"{k}={v:.1f}" for k, v in metrics.items()))
        for r in results:
            print(f"  [{r['level']}] {r['check']}: {r['msg']}")
        print("PASS" if not fails else f"FAIL ({len(fails)})")
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
