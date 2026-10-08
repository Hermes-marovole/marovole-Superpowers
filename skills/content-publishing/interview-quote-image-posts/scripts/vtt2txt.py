#!/usr/bin/env python3
"""vtt -> transcript.txt ([start-end] text)，处理 YouTube 自动字幕的滚动重复。usage: vtt2txt.py in.vtt out.txt"""
import re, sys, html
src, dst = sys.argv[1], sys.argv[2]
def ts(s):
    h, m, r = s.split(":"); return int(h)*3600 + int(m)*60 + float(r)
blocks = open(src, encoding="utf-8").read().split("\n\n")
cues = []
for b in blocks:
    lines = b.strip().splitlines()
    for i, l in enumerate(lines):
        m = re.match(r"(\d+:\d+:\d+\.\d+) --> (\d+:\d+:\d+\.\d+)", l)
        if m:
            txt = " ".join(lines[i+1:])
            txt = re.sub(r"<[^>]+>", "", txt)
            txt = html.unescape(re.sub(r"\s+", " ", txt)).strip()
            if txt: cues.append([ts(m[1]), ts(m[2]), txt])
            break
out = []
prev = ""
for s, e, t in cues:
    # auto-subs: each cue repeats previous line + new words
    if prev and t.startswith(prev):
        new = t[len(prev):].strip()
    else:
        new = t
        # 2-line rolling: drop first line if it equals prev tail
        if prev and prev in t:
            new = t.split(prev, 1)[1].strip()
    prev = t if len(cues) else t
    if not new: continue
    if out and abs(out[-1][1] - s) < 0.05 and out[-1][2] == new: continue
    out.append([s, e, new])
# drop exact consecutive duplicates
res = []
for s, e, t in out:
    if res and res[-1][2] == t:
        res[-1][1] = e; continue
    res.append([s, e, t])
with open(dst, "w", encoding="utf-8") as f:
    for s, e, t in res:
        f.write(f"[{s:8.2f}-{e:8.2f}] {t}\n")
print(len(res), "lines")
