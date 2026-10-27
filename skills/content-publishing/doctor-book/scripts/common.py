"""Shared helpers for doctor-book scripts."""
import json, os, re

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
CJK_RE = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
LATIN_WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[.\-'][A-Za-z0-9]+)*")


def load_config():
    with open(os.path.join(SKILL_DIR, "scripts", "lint_config.json"), encoding="utf-8") as f:
        return json.load(f)


def split_front(text):
    m = FRONT_RE.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, text[m.end():]


def strip_markup(text):
    text = COMMENT_RE.sub("", text)
    text = re.sub(r"\[E\d{3,4}\]", "", text)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"[*_`>|]", "", text)
    return text


def count_chars(text):
    """Publishing-style count: CJK characters + CJK punctuation + latin words."""
    t = strip_markup(text)
    cjk = len(CJK_RE.findall(t))
    punct = len(re.findall(r"[，。！？；：、“”‘’（）《》【】—…]", t))
    latin = len(LATIN_WORD_RE.findall(t))
    return cjk + punct + latin


def load_state(project):
    with open(os.path.join(project, "state.json"), encoding="utf-8") as f:
        return json.load(f)


def save_state(project, state):
    with open(os.path.join(project, "state.json"), "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def evidence_ids(project):
    path = os.path.join(project, "06_evidence", "evidence_bank.md")
    if not os.path.exists(path):
        return {}
    text = open(path, encoding="utf-8").read()
    ids = {}
    for m in re.finditer(r"^###\s*(E\d{3,4})\s*(.*)$", text, re.M):
        ids[m.group(1)] = m.group(2).strip()
    return ids


def draft_files(project):
    d = os.path.join(project, "07_drafts")
    if not os.path.isdir(d):
        return []
    return sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".md"))
