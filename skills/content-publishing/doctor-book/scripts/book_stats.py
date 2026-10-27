#!/usr/bin/env python3
"""Report character counts per draft against the architecture budget."""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import split_front, count_chars, draft_files, load_state


def main():
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    a = p.parse_args()
    state = load_state(a.project_dir)
    total, rows, over = 0, [], False
    back = os.path.join(a.project_dir, "09_backmatter")
    back_files = sorted(os.path.join(back, x) for x in os.listdir(back) if x.endswith(".md")) if os.path.isdir(back) else []
    for f in draft_files(a.project_dir) + back_files:
        meta, body = split_front(open(f, encoding="utf-8").read())
        n = count_chars(body)
        total += n
        budget = int(meta.get("budget") or 0)
        dev = (n - budget) / budget * 100 if budget else 0
        flag = "" if not budget or abs(dev) <= 15 else "  <-- outside ±15%"
        over = over or bool(flag)
        rows.append(f"{os.path.basename(f):<28}{n:>8}{budget:>8}{dev:>+8.0f}%{flag}")
    print(f"{'file':<28}{'chars':>8}{'budget':>8}{'dev':>9}")
    print("\n".join(rows))
    target = state.get("target_chars", 100000)
    print(f"\nTOTAL {total} / target {target} ({total/target*100:.0f}%)")
    in_range = 80000 <= total <= 120000
    print("book length within 80k-120k:", in_range)
    sys.exit(0 if in_range and not over else 1)


if __name__ == "__main__":
    main()
