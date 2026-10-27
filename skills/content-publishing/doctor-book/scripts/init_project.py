#!/usr/bin/env python3
"""Create a doctor-book project skeleton and state file."""
import argparse, json, os, sys, datetime

DIRS = [
    "00_inputs", "01_materials", "02_voice", "03_positioning", "04_market",
    "05_architecture/briefs", "06_evidence", "07_drafts", "08_reviews",
    "09_backmatter", "10_package",
]

STAGES = [
    "intake", "materials", "voice", "positioning", "market", "architecture",
    "evidence", "briefs", "drafting", "review", "frontback", "assembly", "package",
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    p.add_argument("--doctor", default="")
    p.add_argument("--specialty", default="")
    p.add_argument("--topic", default="")
    p.add_argument("--target-chars", type=int, default=100000)
    a = p.parse_args()
    root = os.path.abspath(a.project_dir)
    for d in DIRS:
        os.makedirs(os.path.join(root, d), exist_ok=True)
    state_path = os.path.join(root, "state.json")
    if os.path.exists(state_path):
        print(f"state.json already exists at {state_path}; leaving it unchanged")
        return
    if not 80000 <= a.target_chars <= 120000:
        print("warning: target-chars outside 80000-120000", file=sys.stderr)
    state = {
        "created": datetime.date.today().isoformat(),
        "doctor": a.doctor,
        "specialty": a.specialty,
        "topic": a.topic,
        "target_chars": a.target_chars,
        "material_level": None,
        "stages": {s: "pending" for s in STAGES},
        "chapters": {},
        "notes": [],
    }
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"created project at {root}")


if __name__ == "__main__":
    main()
