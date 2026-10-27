---
name: doctor-book
description: 全自动为中国医生写一本叙事框架型大众健康书（8–12 万字），产出 Markdown 书稿、Word 书稿和出版社投稿包。Use when 用户要给医生出书、写健康科普书，或把医生的访谈、文章、讲座稿、病例做成一本书。
version: 0.1.0
author: Neuma Books
license: Proprietary
metadata:
  hermes:
    tags: [writing, publishing, medical, health, book]
    requires_toolsets: [terminal]
---

# doctor-book：医生叙事型健康书全自动流水线

把一位医生的素材变成一本可投稿的书。范式来自《超越百岁》《好能量》《营养圣经》的逐章拆解：**一个命名框架 + 三幕结构 + 固定章节节拍 + 可执行工具 + 证据与合规双保险**。

`SKILL_DIR` 指本文件所在目录（通常是 `~/.factory/skills/doctor-book` 或 `~/.hermes/skills/doctor-book`；不确定时用 `ls` 确认 `SKILL_DIR/scripts/lint_chapter.py` 存在）。所有脚本只用 python3 标准库；Word 导出需要 `pandoc`，中文字体设置用到 `python-docx`（可选）。

## 运行规则

- **全自动**：从头跑到交付，不中途停下来问用户。需要拍板的地方按阶段文件里的默认规则自己决定，把决定和理由追加到 `state.json` 的 `notes`。
- **断点续跑**：每个阶段结束就把 `state.json` 里该阶段改成 `done`。启动时先读 `state.json`，从第一个不是 `done` 的阶段继续。
- **真实性**：病例、医生本人的经历和原话，只能来自 `01_materials/material_bank.md`。素材里没有的，写成明确标注的 **情景示例**，或者放 `【待核实：……】` 占位。研究结论只能引用 `06_evidence/evidence_bank.md` 里的条目，正文用 `[E012]` 标注。
- **上下文纪律**：总控只看各阶段的产出文件和脚本输出，不把整章草稿读进自己的上下文。逐章写作和审稿交给子代理（Factory 用 Task，Hermes 用 delegate_task）；没有子代理就逐章顺序做，每章只读该章简报和需要的参考文件。
- **门槛靠脚本**：章节是否合格以 `scripts/lint_chapter.py` 的退出码为准，全书以 `scripts/book_check.py` 和 `scripts/book_stats.py` 为准，再叠加审稿评分。脚本报 FAIL 时改稿，不改阈值。

## 启动

1. 确定项目目录（用户给了就用，否则在当前目录建 `books/<医生拼音或主题>/`），把用户提供的所有素材复制进 `00_inputs/`。
2. 首次运行：`python3 SKILL_DIR/scripts/init_project.py <项目目录> --doctor "<姓名>" --specialty "<专科>" --topic "<主题>" --target-chars 100000`
3. 读 `state.json`，按下表从第一个未完成阶段开始。每进入一个阶段，先完整读它的阶段文件，再动手。

## 流水线

| # | 阶段 | 阶段文件 | 主要产出 | 完成标准 |
|---|---|---|---|---|
| 1 | intake | `stages/01-intake.md` | `01_materials/inventory.md` | 每份素材都已转成文本并登记；素材等级 A/B/C 已写入 state |
| 2 | materials | `stages/02-materials.md` | `01_materials/material_bank.md` | 每份素材都已挖完；各类素材条目数达到下限或已记录缺口 |
| 3 | voice | `stages/03-voice.md` | `02_voice/voice_profile.md` | 文风档案含 10 条以上原句样本（C 级素材用默认人设） |
| 4 | positioning | `stages/04-positioning.md` | `03_positioning/positioning.md` | 书名、核心框架、3–5 个命名概念、读者与承诺全部定稿，评分表全部 ≥4 |
| 5 | market | `stages/05-market.md` | `04_market/competitors.md` | 至少 5 本同类书已对比，差异点已写回 positioning |
| 6 | architecture | `stages/06-architecture.md` | `05_architecture/outline.md` | 三幕、10–14 章、每章章型与字数预算、概念复现表、病例分配表齐全，预算合计在目标 ±5% 内 |
| 7 | evidence | `stages/07-evidence.md` | `06_evidence/evidence_bank.md` | outline 里每个关键论断都有证据条目，每条都有来源、证据等级和绝对风险（适用时） |
| 8 | briefs | `stages/08-briefs.md` | `05_architecture/briefs/chNN.md` | 每章一份简报，节拍、比喻、病例、证据 ID、可带走物都已指定 |
| 9 | drafting | `stages/09-drafting.md` | `07_drafts/chNN.md` | 每章 lint 通过（退出码 0） |
| 10 | review | `stages/10-review.md` | `08_reviews/chNN.md` | 每章审稿各维度 ≥4、合规项满分，修改后 lint 仍通过 |
| 11 | frontback | `stages/11-frontback.md` | `09_backmatter/*.md` | 前言、结语、附录工具、术语表齐全；`book_stats.py` 退出码 0 |
| 12 | package | `stages/12-package.md` | `10_package/proposal.md`、`cover.jpg`、`figures/*.png` | 选题策划书与营销文案已填；样章已写入 state；封面与 8–12 幅章节信息图已渲染就绪 |
| 13 | assembly | `stages/13-assembly.md` | `book.md`、`book.docx`、`book.epub`、`投稿包.zip` | `render_visuals.py`、`assemble.py`、`export.py`、`audit_book.py` 全数 PASS（0 FAIL），交付报告已写 |

## 参考库

阶段文件会指明该读哪些参考文件，不要一次全读。

- `references/architecture.md`：三幕比例、章型、排序规则、章名模式、首尾闭环
- `references/chapter-template.md`：八拍章节模板与章型变体
- `references/patterns/`：写作模式卡片，按类别分文件（开篇、解释、病例、证据、说服、章尾与工具、标题、前言结语）
- `references/compliance-cn.md`：国内出版与医疗宣传的合规红线
- `references/voice-style.md`：文风量化指标与去 AI 腔规则
- `references/proposal-template.md`：选题策划书模板
- `references/visuals-and-cover.md`：图书封面（1600×2400）与章节信息图（1400×980）HTML/SVG 渲染规范及防折行/防裁切铁律
- `references/atlas/`：三本样书的逐章结构表，写某类章节前想看实例时查
- `templates/`：各阶段产出文件的格式

## 交付

最后向用户汇报：书名、章数、总字数、`10_package/` 下的文件清单、`【待核实】` 条目数量、仍然是警告级别的检查项。明确告诉用户：书稿必须由医生本人审阅待核实清单，并通过出版社医学审读后才能出版。
