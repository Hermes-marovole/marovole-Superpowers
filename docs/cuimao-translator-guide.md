# 萃猫翻译 (Cuimao Translator) — Claude Code 翻译技能

> 一键将英文 PDF 书籍翻译为地道中文的 Claude Code 技能  
> 来源：https://github.com/Cuimao777/cuimao-translator  
> 整理时间：2026-04-30  
> 来自翡冷翠

---

## 项目简介

**萃猫翻译** 是专为书籍级长文本设计的 Claude Code 翻译技能。核心承诺是**逐句忠实，读起来却像中文作者亲笔所写**。

### 核心特点

| 特性 | 说明 |
|------|------|
| 逐句忠实 | 零增译、零漏译——每句原文都有对应译文 |
| 中文自然度 | 自动检测并修正"被字泛滥""的的不绝""之一成灾"等欧化中文通病 |
| 术语一致 | 内置 100+ 常用术语表，全书术语一致 |
| 多模式适配 | 三种模式适配不同场景，从快速浏览到出版精翻 |
| 五风格预设 | 覆盖小说、学术、技术文档、散文等 |

---

## 快速安装

```bash
git clone https://github.com/Cuimao777/cuimao-translator.git ~/.claude/skills/cuimao-translator
```

安装后重启 Claude Code，直接说「翻译这个 PDF」即可自动激活。

---

## 使用方法

### 触发词

| 类别 | 触发词 |
|------|--------|
| 通用 | `翻译` `汉化` `英译中` `translate` |
| 格式 | `PDF翻译` `翻译这本书` `汉化这个PDF` |
| 速译模式 | `速译` / `快翻` → Quick 模式 |
| 精翻模式 | `精翻` / `精细翻译` / `出版级` → Refined 模式 |

### 三种翻译模式

| 模式 | 触发词 | 流程 | 适用场景 |
|------|--------|------|----------|
| ⚡ **Quick 速译** | `快翻` `速译` | 读取 → 直接翻译 | 快速浏览内容、短篇片段 |
| 📖 **Normal 标准** | 默认、`翻译` | 分析 → 翻译 | 大多数书籍章节、博客、通用内容 |
| 💎 **Refined 精翻** | `精翻` `精细翻译` | 分析 → 初译 → 审校 → 修订 → 润色 | 出版级输出、关键章节、最终交付 |

**模式升级**：标准模式完成后可随时升级，回复 `继续润色` 或 `refine` 即进入精翻流程。

### 五种风格预设

| 风格 | 适用 | 特点 |
|------|------|------|
| 📝 `storytelling` 叙事流畅 | 小说、传记、叙事非虚构 | 过渡自然、语言生动、中文节奏 |
| 🎓 `academic` 学术严谨 | 学术著作、教科书、研究报告 | 正式语域、术语精确、引文规范 |
| ⚙️ `literal` 逐句忠实 | 技术手册、法律文件、合同 | 贴近原文结构、最小改写 |
| ✨ `elegant` 文采典雅 | 文学小说、诗歌、散文 | 四字格运用、音韵美感、留白 |
| 💬 `conversational` 口语自然 | 对话密集、自助书籍、回忆录 | 轻松亲近、像在跟读者聊天 |

---

## 翻译哲学

```
信 → 达 → 雅
（忠实）→（流畅）→（文化适配）
```

### 信 — 忠实
- 每句英文必有对应中文
- 事实、数字、逻辑、专名完全一致
- 不概括、不跳过、不添油加醋

### 达 — 流畅
- 中文读起来**不像翻译的**
- 按中文话题-评论结构重组语序
- 拆长句为 7-15 字的自然意群
- 主动优于被动，补语优于状语

### 雅 — 文化适配
- 英文成语、俚语、文化梗 → 找到中文等值表达
- 双关语无法翻译时 → 译意并标注
- 中国读者不了解的引用 → 加简短译注

---

## 欧化中文六重检测

翻译完成后自动自查以下六种"翻译腔"通病：

| # | 问题 | 示例 |
|---|------|------|
| 1 | 被字句泛滥 | "He was praised" → `他受到了表扬`，而非 `他被表扬了` |
| 2 | 连接词堆砌 | 去掉多余的「因为…所以…」「虽然…但是…」 |
| 3 | 定语过长 | 英文长定语 → 拆成多个短句 |
| 4 | 之一滥用 | "one of the most…" → `极其…`，不一定总用 `…之一` |
| 5 | 的的的 | 一句中出现 ≥3 个「的」就重构 |
| 6 | 名词化过度 | "the implementation of…" → `实施…`（动词），而非 `…的实施` |

---

## 翻译示例

**输入**（英文 PDF 段落）：

> The old man had taught the boy to fish and the boy loved him. He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish.

**输出**（storytelling 风格）：

> 老头儿教过那孩子打鱼，孩子也爱他。他是个独自在湾流里的一只小船上打鱼的老头儿，如今已经接连八十四天一条鱼也没打着了。

---

## 仓库文件结构

```
cuimao-translator/
├── SKILL.md                    # 技能主文件（Claude Code 技能定义）
├── README.md                   # 项目介绍
└── references/
    ├── glossary-en-zh.md       # 100+ 术语英中对照表
    ├── translation-guide.md    # 句子转换模式、欧化中文诊断
    └── refined-workflow.md     # 精翻五步流水线详细指南
```

---

## 参考文档详解

### 1. 术语表 (glossary-en-zh.md)

收录 100+ 常用但易误译的术语，涵盖：

#### AI & 技术
| English | Chinese | 备注 |
|---------|---------|------|
| AI Agent | AI 智能体 | |
| Alignment | 对齐 | AI safety context |
| Hallucination | 幻觉 | AI 专用含义 |
| Vibe Coding | 凭感觉编程 | |
| RLHF | 基于人类反馈的强化学习 | |

#### 商业与策略
| English | Chinese | 备注 |
|---------|---------|------|
| Moat | 护城河 | 竞争优势 |
| Flywheel | 飞轮效应 | |
| Move the needle | 产生实质影响 | |
| Low-hanging fruit | 短期见效的事 | |

#### 叙事与写作
| English | Chinese | 备注 |
|---------|---------|------|
| Narrative | 叙事 | |
| World-building | 世界观构建 | |
| Foreshadowing | 伏笔 | |
| Trope | 套路/桥段 | |

#### 常见误译词
| English | 错误译法 | 正确译法 | 备注 |
|---------|----------|----------|------|
| Actually | 实际上 | 其实/竟然 | 依语境 |
| Quite | 十分 | 相当/颇为/挺 | 英式英语 |
| Honestly | 诚实地 | 说实在的 | |

### 2. 翻译指南 (translation-guide.md)

详细涵盖：

#### 欧化中文检测（六大红旗）
1. **被字句泛滥** → 替换为 由/受/得到/话题-评论结构
2. **连接词堆砌** → 删除冗余的 因为…所以/虽然…但是/当…的时候
3. **定语堆叠过长** → 拆分成长度适中的短句
4. **之一滥用** → 改用 极为/非常/…得很
5. **的密度过高** → 重构句子，控制 的 的数量
6. **名词化过度** → 将名词化表达转换为动词

#### 句子结构转换策略
- 英文长句 → 中文意群（7-15 字）
- 主谓宾 → 话题-评论结构
- 被动语态 → 由/受/得到/话题-评论

#### 分领域翻译要点
- **文学小说**：对话自然、意境营造、四字格节奏
- **学术论文**：术语规范、引文格式、论证结构
- **商业技术**：行话本地化、UX 文案优化
- **对话翻译**：角色区分、口语自然、言外之意

### 3. 精翻工作流 (refined-workflow.md)

五步出版级翻译流水线：

```
Step R1: 分析 → Step R2: 初译 → Step R3: 审校 → Step R4: 修订 → Step R5: 润色
```

| 步骤 | 任务 | 输出文件 |
|------|------|----------|
| R1 | 内容分析（术语提取、风格评估、难点预判） | `[book]-analysis.md` |
| R2 | 初译（逐段翻译，保持双语对照） | `[chapter]-draft.md` |
| R3 | 审校（准确性、中文自然度、文化适配） | `[chapter]-critique.md` |
| R4 | 修订（修正所有问题，提升流畅度） | `[chapter]-revision.md` |
| R5 | 润色（最终打磨，出版级输出） | `[chapter]-chinese.md` |

---

## 配置扩展 (EXTEND.md)

可选配置，在项目根目录创建 `.pdf-translator/EXTEND.md`：

```yaml
target_language: zh-CN
default_mode: normal        # quick | normal | refined
style: storytelling         # literal | storytelling | elegant | academic | conversational
audience: general           # general | technical | academic | young-readers
chunk_max_words: 3000

glossary:
  "custom term": "自定义翻译"
  "another term": "另一个翻译"

glossary_files:
  - custom-glossary.md
```

---

## 使用检查清单

翻译交付前确认：
- [ ] 每句英文都有对应中文句子
- [ ] 数字、日期、专名与原文完全一致
- [ ] 无"翻译腔"（被/的/之一滥用）
- [ ] 段落结构与原文匹配
- [ ] 术语一致（对照分析/术语表）
- [ ] 章节标题翻译正确、格式规范

---

## 项目信息

| 项目 | 详情 |
|------|------|
| 名称 | cuimao-translator |
| 作者 | @Cuimao777 |
| 许可证 | MIT |
| Stars | 32 |
| 最近更新 | 2026-04-29 |
| GitHub | https://github.com/Cuimao777/cuimao-translator |

---

*来自翡冷翠*
