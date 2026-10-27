#!/usr/bin/env python3
"""Regression tests for lint_chapter.py. Run after editing lint_config.json or the lint script.

Each probe is a tiny chapter plus the checks it must (or must not) trigger at FAIL level.
"""
import os, shutil, subprocess, sys, tempfile, json

HERE = os.path.dirname(os.path.abspath(__file__))
LINT = os.path.join(HERE, "lint_chapter.py")

EVIDENCE = """# 证据库

### E001 测试条目
- 来源：Test A. Test title. Test Journal, 2020;1:1.
"""

PROBES = [
    ("unqualified cure / replace drugs / pill count",
     "那天他来了。这个方法可以治愈糖尿病，保证有效，也可以代替药物。每天吃两片二甲双胍。",
     {"compliance", "dose"}, set()),
    ("negated claims are allowed",
     "那天他来了。糖尿病目前还不能治愈，生活方式也不能替代药物。这不是危言耸听。",
     set(), {"compliance"}),
    ("relative risk dodging via 降到",
     "那天他来了。一项研究显示，风险下降 58%[E001]，血糖降到 7.0。",
     {"risk"}, set()),
    ("relative risk with absolute risk is fine",
     "那天他来了。一项研究显示，风险下降 58%，相当于每 1000 人里少 60 人发病[E001]。",
     set(), {"risk"}),
    ("case without source (老X + 多岁)",
     "老周四十多岁，体检时血糖偏高，他一直没当回事。",
     {"fabrication"}, set()),
    ("case with source tag",
     "<!-- src: C01 -->\n老周四十多岁，体检时血糖偏高，他一直没当回事。",
     set(), {"fabrication"}),
    ("stop medication without doctor",
     "那天他来了。他听了邻居的话，自己停药了。",
     {"medication"}, set()),
    ("stop medication with doctor guard",
     "那天他来了。已经在吃药的人，不要自己停药，调整药量请和你的医生商量。",
     set(), {"medication"}),
    ("research claim without tag",
     "那天他来了。研究表明，散步对血糖有好处。",
     {"evidence"}, set()),
    ("definition opening",
     "所谓糖尿病前期，是指血糖高于正常但还没到糖尿病的阶段。",
     {"opening"}, set()),
    ("food counts are not doses",
     "那天他来了。早上他吃两片面包、一个鸡蛋。",
     set(), {"dose"}),
    ("hard-banned phrase",
     "那天他来了。他说这是医生不会告诉你的秘方。",
     {"compliance"}, set()),
]


def run_probe(proj, i, body):
    path = os.path.join(proj, "07_drafts", f"ch{i:02d}.md")
    budget = max(1, len(body))
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"---\nchapter: {i}\ntype: argument\ntitle: probe\nbudget: {budget}\n---\n\n{body}\n")
    r = subprocess.run([sys.executable, LINT, path, "--project", proj, "--json"], capture_output=True, text=True)
    data = json.loads(r.stdout)
    return {x["check"] for x in data["results"] if x["level"] == "FAIL"}


def main():
    proj = tempfile.mkdtemp(prefix="doctor-book-selftest-")
    try:
        os.makedirs(os.path.join(proj, "07_drafts"))
        os.makedirs(os.path.join(proj, "06_evidence"))
        with open(os.path.join(proj, "06_evidence", "evidence_bank.md"), "w", encoding="utf-8") as f:
            f.write(EVIDENCE)
        failures = 0
        for i, (name, body, must, must_not) in enumerate(PROBES, 1):
            got = run_probe(proj, i, body) - {"budget"}
            missing, unexpected = must - got, must_not & got
            ok = not missing and not unexpected
            failures += not ok
            print(f"{'ok  ' if ok else 'FAIL'} {name}: fails={sorted(got)}"
                  + (f" missing={sorted(missing)}" if missing else "")
                  + (f" unexpected={sorted(unexpected)}" if unexpected else ""))
        print(f"\n{len(PROBES) - failures}/{len(PROBES)} probes passed")
        sys.exit(1 if failures else 0)
    finally:
        shutil.rmtree(proj, ignore_errors=True)


if __name__ == "__main__":
    main()
