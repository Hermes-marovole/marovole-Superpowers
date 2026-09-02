---
name: neumina-lifestyle-course-design
version: 1.0.0
description: "Use when designing Neumina 14-day lifestyle courses."
author: Neumina / Hermes
license: internal
category: autonomous-ai-agents
tags: [neumina, course-design, lifestyle, curriculum, miniprogram, health-education, cortisol, anti-inflammatory]
metadata:
  hermes:
    tags: [neumina, course-design, lifestyle, curriculum, miniprogram, health-education]
    related_skills: [neumina-agent-architecture]
    category: autonomous-ai-agents
---

# Neumina Lifestyle Course Design

## Goal

Turn one health theme into a shippable **14-day lifestyle course pack** for Neumina: curriculum doc + miniprogram detail-page copy + check-in / scoring / weekly-review / incentive skeleton — without diagnosis or cure claims.

Default audience: ages 40–60 Chinese women (do **not** brand as menopause product externally; internal mechanism language OK).

## Success Criteria

Deliver **all three** unless user asks for a subset:

1. `两周{主题}课程设计_YYYYMMDD.md` — full executable curriculum
2. `{主题}课程详情页文案_小程序_YYYYMMDD.md` — paste-ready detail page
3. (If productizing) config notes: Day0→14 unlock, 6-dim score, quiz/emotion/AI/rewards hooks

Quality bar:

- One-sentence positioning + one core formula + ≤6 memorable rules (e.g. 三增三减)
- Day 0 baseline (no teaching contamination) → W1 subtract → W2 add → Day7/14 review
- **Exactly one primary task per day** (doable today)
- Machine- or self-scorable dimensions + replace-not-shame feedback templates
- Compliance block: fit/unfit, red-flag seek-care, optional supplements as accelerator only
- Failure-friendly: “strict demo version” disclaimer, Quiz bonus, emotion unlock

## Constraints

- Behavior change is the spine; science is short support, not a textbook
- Less text: fold demos/lists; detail page stays scannable
- “Add / swap” > “ban”; no scare, shame, or hype
- Foundation = food/rhythm/sleep/boundaries; supplements never become the main line
- No diagnosis, no efficacy promises, no “two weeks to lab value X”
- Do not expand to 30-day fine grain on first pass — lock **Day0 + 14 days** first
- Bonus habits are optional capsules, not homework

**REQUIRED BACKGROUND:** Align tone and safety with `neumina-agent-architecture` (nutrition-led education, medical only for red flags / conflicts).

## When to Use (triggers)

- New Neumina lifestyle course (抗炎 / 降皮质醇 / 稳血糖 / 护睡眠 / …)
- Extract reusable framework from existing course docs + meeting notes
- Migrate a proven course skeleton to a new theme
- Write 小程序课程详情页 + 打卡评分骨架
- Co-create with AI using the fixed 11-layer pack

## How to Use

### A. New theme from scratch

1. Load this skill + skim `references/11-layer-framework.md`
2. Fill the **13-slot mapping** in `references/theme-mapping-checklist.md`
3. Write curriculum with the **11-layer skeleton** (below)
4. Write detail page with the **standard TOC**
5. Run **Verification** checklist before delivery

### B. Extract framework from existing courses

1. Read source docs (design + detail copy + meeting notes if any)
2. Map sections onto the 11 layers — keep structure, drop one-off content
3. Record product patches from meetings (quiz, emotion unlock, cost tiers, etc.)
4. Save/update this skill’s references if new reusable patches appear
5. Optionally migrate once to a second theme to prove the skeleton

### C. Migrate theme A → theme B

Keep layers 5–11 mechanics; swap metaphor, formula, lists, baseline evidence type, daily themes, score dims, somatic items. Reuse product chrome.

Proven pair: anti-inflammatory → lower cortisol (workspace samples under course demo repos).

## Core Skeleton (11 layers)

```text
① One-line positioning (metaphor + promise)
② Opening resonance (“not sick, but off”)
③ Short mechanism (2 concepts + 3–4 sources + one closing line)
④ Core rules (formula + 三增三减 + green/red lists + unified params)
⑤ Day 0 baseline (record only → 0–100 + one-line read)
⑥ Two-week arc (W1 clear triggers → W2 install recovery)
⑦ Daily quartet (theme / single task / demo / check-in) + optional knowledge/Quiz/emotion
⑧ Multi-dim scoring + feedback templates
⑨ Weekly review (rate, mean vs baseline, somatic 5, objective 2, encourage + one fix)
⑩ Bonus habits + optional supplement tiers
⑪ Product landing (unlock, AI float, badges/beans/share, cost-tier lists, fold text)
```

Detail page ≈ ①–④ + outcomes + honest timeline + fit/unfit + check-in + FAQ + CTA.  
Curriculum ≈ ④–⑪ executable.  
Meeting patches ≈ ⑪.

Full layer recipes: `references/11-layer-framework.md`  
Detail TOC + co-create prompt: `references/detail-page-and-prompts.md`  
Fill-in mapping: `references/theme-mapping-checklist.md`

### Positioning formula

```text
先看清你现在的 {状态隐喻} 有多大，再用 14 天，一点一点把它 {动作}。
```

One metaphor for the whole course. Teach one repeatable thing — not extreme deprivation.

### Daily quartet

```text
① 今日主题  ② 今日任务（只做这一件）  ③ 今日示范  ④ 打卡证据
```

### Score table shape

| Dim | Pts | Full | Penalize |
|-----|-----|------|----------|
| A–D | 20 each | observable rule | partial / none |
| Context bonus | 10 | season/scene | — |
| Red-list hit | −20 | — | −5 per trigger |

Feedback must say **what to add/swap**, never scold.

### Two-week rhythm

| Node | Job |
|------|-----|
| Day 1 | Cognition + environment clear |
| Day 2–6 | One rule per day (subtract) |
| Day 7 | Week-1 review |
| Day 8–13 | Install recovery / stabilize |
| Day 14 | Review + “3 long-term keeps” + graduation |

Front-load high-value tactics; declare strict demo + real-life downgrades; allow AI/preference swaps.

## Tone DNA

- Empathy → mechanism → small step
- Short sentences; translate jargon immediately
- Honest onset timeline (1–3d / 3–7d / 1–2w / deeper varies)
- Bad day: hold emotion, **do not cancel the day**; breath / quiz floor
- Seasonal/regional params are swappable skins — skeleton stays

## Stop Rules

Stop and deliver when the three artifacts (or requested subset) pass Verification.  

Ask user only if: theme metaphor conflicts, medical-risk audience unclear, or they want non-14-day length / paid packaging beyond skeleton.  

Do **not**: invent lab protocols, prescribe drugs, stack five supplements as core, or write 30 days before 14 is locked.

## Anti-Patterns

| Trap | Do instead |
|------|------------|
| Wall of text | Fold demos; tappable micro-knowledge |
| Hard tasks, no exit | Strict-demo note + Quiz floor + emotion unlock |
| Key tactic on Day 9+ | Front-load when possible |
| Fixed meal tyranny | AI / pantry personalization |
| Supplements as spine | Rhythm/food first |
| Only a pep line at review | Badge, beans, baseline chart, share card |
| Bonus = mandatory | Random daily capsule |
| Long pathophysiology | 4 sources + one line |

## Verification

Before “done”:

**Content**
- [ ] Stranger can restate the course in 30s
- [ ] Any day answers “only one thing today”
- [ ] Day0 / Day7 / Day14 comparable
- [ ] Core rules fit one screen

**Safety**
- [ ] No diagnosis / cure promise
- [ ] Fit/unfit + seek-care red flags present
- [ ] Supplements tiered + “ask professional”
- [ ] No scare/shame copy

**Product**
- [ ] Score dims implementable
- [ ] Feedback covers main low-score causes
- [ ] Quiz / emotion / bonus don’t steal the spine
- [ ] Detail page text tightened once

## Related

- `neumina-agent-architecture` — safety, voice, agent boundaries
- Source extraction provenance: anti-inflammatory 14-day course + meeting 2026-09-02 → general framework → cortisol migration

## Maintenance

When a new course surfaces a reusable product patch (e.g. new failure exit), **patch this skill’s references** — don’t leave truth only in one repo markdown file.
