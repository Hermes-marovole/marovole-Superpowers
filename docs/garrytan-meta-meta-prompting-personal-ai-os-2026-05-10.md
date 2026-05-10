# Garry Tan：Meta-Meta-Prompting 与个人 AI 神经系统 - X2Doc 整理

> 来源：https://x.com/garrytan/status/2053127519872614419
> 作者：@garrytan
> 发布时间：2026-05-10
> 整理时间：2026-05-10
> 来自翡冷翠

---

## TL;DR

- Garry Tan 这篇 X Article 的核心不是“怎么写更好的 prompt”，而是：个人 AI 的杠杆来自可复利的系统，而不是一次性聊天窗口。
- 他的架构公式是：thin harness + fat skills + fat data + interchangeable models。模型只是引擎，真正的车是技能、数据、路由和持续运行的自动化。
- 最关键概念是 Skillify / meta-skill：把一次手动完成的工作流提炼成可复用 skill，再让 skill 互相组合，形成自我增强系统。
- 文章的高价值在于：它把“第二大脑”从比喻拉回工程系统：知识库、实体页面、时间线、会议摄取、书籍镜像、cross-modal eval、cron job、模型路由。
- 对翡冷翠当前 Super Individual 路线高度相关：它验证了“Coding + 自媒体 + 第二大脑 + Hermes Agent”的复利方向，也提示 X2Doc 本身应该继续 skillify 和 cronify。

---

## 原帖核心内容

Garry Tan 的文章标题是：

> Meta-Meta-Prompting: The Secret to Making AI Agents Work

他解释自己为什么作为 Y Combinator CEO 仍然经常写代码到凌晨 2 点：过去 5 个月，AI 让他重新成为 builder。他认为 personal AI 不应该被当作 chat window，而应该被当作 operating system。

文章通过几个具体案例说明这个 operating system 的形态。

### 1. Book Mirror：把书映射到个人真实生活图谱

Garry 读 Pema Chödrön 的《When Things Fall Apart》时，让 AI 做了一个 “book mirror”。

系统做的不是普通总结，而是：

- 提取全书 22 章内容；
- 对每章启动 sub-agent；
- 同时总结作者观点，并映射到 Garry 自己的真实生活上下文；
- 上下文包括家庭背景、YC 工作、开源工具、创始人关系、阅读史、治疗进展等。

输出是一个 30,000 字的 brain page。每章呈现成两列：

- Pema 说了什么；
- 这如何映射到 Garry 正在经历的事情。

他强调：一个 300 美元/小时的治疗师即使读这本书，也无法在 40 小时内做到同等上下文映射，因为治疗师没有完整加载他的职业上下文、阅读历史、会议笔记和创始人关系图谱。

他已经对 20 多本书做过类似 book mirror，包括 Russell、Hesse、Hamming、Alan Watts、Feynman、Ken Wilber 等。系统越用越强，因为第二本知道第一本，第二十本知道前十九本。

### 2. 质量复利：从失败中 skillify

第一个 book mirror 很糟糕，出现了关于家庭背景的事实错误：

- 说父母离婚，实际没有；
- 说他在香港长大，实际出生在加拿大。

于是他加入 mandatory fact-check step。现在每次 mirror 都会对 brain 中已知事实做 cross-modal evaluation：

- Opus 4.7 1M：抓精度错误；
- GPT-5.5：抓缺失上下文；
- DeepSeek V4-Pro：抓“太 generic”的内容。

随后他又升级到 GBrain tool use 的 deep retrieval。新版 book mirror 会对每个 section 做 brain search，并引用真实 brain pages，而不是泛泛综合。

这里引出核心概念：skillification。第一次手动完成流程后，系统提取可重复模式，写成带触发条件和边界情况的 skill。之后所有 book mirror 都受益于这个修正。

### 3. Skillify：创建 skills 的 meta-skill

Garry 认为最大的洞察在递归层：

> The system that runs my life didn't exist as a monolith. It was assembled from skills. And those skills were themselves created by a skill.

Skillify 是一个 meta-skill。遇到会重复的 workflow，他会说 “skillify this”。系统会：

- 检查刚刚发生了什么；
- 提取可重复模式；
- 写一个经过测试的 skill file；
- 加入 triggers 和 edge cases；
- 注册到 resolver。

Book mirror、meeting prep 等流程都是从首次手动操作中 skillified 出来的。

Skills 可以组合。例如 book-mirror 会调用：

- brain-ops：存储；
- enrich：补上下文；
- cross-modal-eval：质量控制；
- pdf-generation：输出。

每个 skill 专注一件事，但链起来可以形成复杂工作流。改进一个 skill，所有调用它的 workflow 都自动变强。

### 4. Meeting Prep：不是搜索，而是基于个人上下文的角度生成

Demis Hassabis 来 YC 做 fireside chat 时，Garry 让系统为他做准备。系统在两分钟内拉取：

- Demis 的完整 brain page；
- 他关于 AGI timeline 的观点；
- Sebastian Mallaby 传记的 highlight；
- 他的研究优先级，如 continual learning、world models、long-term memory；
- Garry 自己关于 AI 的公开观点；
- 用于展示 brain multi-hop reasoning 的 demo scripts；
- 基于双方世界观重叠和分歧的 conversation hooks。

Garry 强调：这不是更好的 Google search，而是使用“我积累的关于 Demis 的上下文 + 我自己的立场 + 这场对话的战略目标”来准备角度。

### 5. 结构化知识库：从 filing cabinet 到 nervous system

他维护了一个结构化知识库：文章中提到约 100,000 pages。每个对象都有结构化页面：

- 每个人：timeline、state、open threads、score；
- 每场会议：transcript、structured summary；
- 每个被提到的人/公司：entity propagation 回写到对应 brain pages；
- 每本书：chapter-by-chapter mirror；
- 每篇文章、播客、视频：ingested、tagged、cross-referenced。

页面 schema 很简单：

- 顶部是 compiled truth：当前最佳理解；
- 下方是 append-only timeline：按时间累积的事件；
- 旁边有 raw data sidecars：原始来源材料。

他把这个比作 personal Wikipedia，但每一页都由 AI 持续更新。

他给出 founder office hours 的例子：见到创始人后，系统会更新 person page 和 company page，交叉引用会议记录，检查之前是否见过、公司 metrics、是否有 portfolio contacts 能帮忙。下一次会议前，系统已经准备好完整 context pack。

> This is the difference between having a filing cabinet and having a nervous system.

### 6. 架构：thin harness, fat skills, fat data, fat code

Garry 的架构分层：

#### Thin harness

OpenClaw 是 runtime，负责接收消息、判断哪个 skill 适用并 dispatch。它不需要知道书、会议或 founders 的领域细节。

#### Fat skills

100+ self-contained markdown files，每个处理一个具体任务。他提到的内置或公开 skills 包括：

- meeting-ingestion：会议后拉 transcript、生成 summary、传播实体更新；
- enrich：给定人名后，从多个来源合并成 brain page；
- media-ingest：处理 video、audio、PDF、screenshots、GitHub repos；
- perplexity-research：brain-augmented web research，先查 brain 再查 web。

#### Fat data

约 100,000 pages 的结构化知识。人、公司、会议、书、文章、想法都链接且可搜索。

#### Fat code

转录、OCR、社交媒体归档、日历同步、API 集成等脚本也很重要。它们支撑数据不断进入系统。

#### Interchangeable models

模型是可替换的：

- Opus 4.7 1M：precision；
- GPT-5.5：recall 和 exhaustive extraction；
- DeepSeek V4-Pro：creative work 和第三视角；
- Groq + Llama：speed。

Skill 决定哪个模型处理哪个任务。Harness 不关心。

> The model is just the engine. Everything else is the car.

### 7. 开源栈与行动建议

Garry 说他把整个 stack 开源了。文章中 Jina Reader 没能保留所有链接文字，但结合 GitHub 搜索可以确认核心项目：

- GBrain：https://github.com/garrytan/gbrain
- GBrain 描述：Garry's Opinionated OpenClaw/Hermes Agent Brain
- 当前 GitHub stars：约 14,276（2026-05-10 检索）

GBrain README 中自述：这是 Garry 用来运行自己 OpenClaw 和 Hermes deployments 的 production brain，并提供 local brain、hybrid search、knowledge graph、MCP server、skills、cron 等能力。

文章给出的构建建议：

1. Pick a harness：OpenClaw、Hermes Agent，或自己搭一个 thin router；
2. Start a brain：用 GBrain 建 git-based brain repo；
3. Do something interesting：不要先空谈 skill architecture，而是先做一件你真正关心的事；
4. Skillify：把成功的一次性流程提炼成 reusable skill；
5. Keep using it and evaluate：用 cross-modal eval 把错误修正 baked into skill。

最终命题：

> The future belongs to individuals who build compounding AI systems, not to individuals who use corporate-owned centralized AI tools.

---

## 关键信息与资源

| Type | Name | Link | Why it matters |
|---|---|---|---|
| X Article | Meta-Meta-Prompting: The Secret to Making AI Agents Work | https://x.com/garrytan/status/2053127519872614419 | 原始长文，阐述个人 AI OS 的完整理念 |
| GitHub Repo | GBrain | https://github.com/garrytan/gbrain | 文章中 second brain / knowledge infrastructure 的开源实现 |
| Skill concept | Skillify | 原文概念 | 把重复工作流自动提炼成 skill，是系统复利的关键递归层 |
| Architecture concept | Thin harness, fat skills | https://raw.githubusercontent.com/garrytan/gbrain/master/docs/ethos/THIN_HARNESS_FAT_SKILLS.md | Garry 对 agent 架构的核心抽象：把 intelligence 推到 skills，把 deterministic execution 下沉到工具 |
| Pattern | Book Mirror | 原文案例 | 用完整个人上下文映射书籍内容，比普通总结更接近“认知镜像” |
| Pattern | Entity propagation | 原文案例 / GBrain docs | 会议后将提到的人和公司回写到对应页面，让知识图谱持续自更新 |
| Pattern | Cross-modal eval | 原文案例 | 多模型互评，用不同模型发现事实错误、上下文缺失和 generic output |

---

## 我的吸收判断

### 可复用能力

这篇文章至少有 5 个值得吸收进 Superpowers / Hermes 工作系统的能力：

1. X2Doc 本身继续 skillify
   - 当前 X2Doc 已经可以把 X Article 变成文档；
   - 下一步应该沉淀“从 X → docs → 判断是否转 skill/cron”的完整闭环；
   - 如果同类任务出现两次，就应该自动形成 skill patch 或新 skill 候选。

2. Book Mirror / Article Mirror
   - 对书、长文、播客不只总结，而是映射到用户真实项目、身份、长期目标；
   - 对翡冷翠尤其适合映射到：Super Individual、AICoding、个人品牌、Neumina、Biohacking、BTC long-termism。

3. Cross-modal eval for skills
   - 新 skill 或重要文档可以用不同模型角色检查：
     - factual precision；
     - missing context；
     - generic / AI 味；
     - 是否符合用户长期路线。

4. Entity propagation
   - X2Doc 产出的文档可以自动识别：人物、公司、项目、工具、模型、概念；
   - 回写到 Obsidian 或 Superpowers index；
   - 未来查 Garry Tan / GBrain / OpenClaw 时能看到历史上下文。

5. Cron-driven compounding
   - 不是“有空整理知识”，而是通过定时任务让 newsletter、X、GitHub、Reddit、email 的高信号自动进入第二大脑；
   - 这和你已有的 night-research-cron、AI Newsletter digest、Obsidian Daily Brief 方向一致。

### 值得沉淀到 skill / workflow 吗

值得，而且优先级很高。

当前已有：

- x2doc skill；
- link2doc skill；
- night-research-cron；
- obsidian-ai-workflows；
- agent-workflow-system。

建议不是再创建一堆孤立 skill，而是做一个上层 workflow：

> signal → x2doc/link2doc → absorption judgment → skill patch/new skill → optional cron → Obsidian/Superpowers index

这正是 Garry 文章里的 Skillify loop。

### 对 AI × Product × Biohacking / Super Individual 的价值

这篇内容和翡冷翠的个人路线高度同频：

- AI：从“会用模型”升级到“拥有个人 agent OS”；
- Product：把 skills 当产品化能力单元，而不是 prompt 文案；
- Biohacking：book mirror / therapy mirror / cognition mirror 可用于自我观察和长期行为优化；
- 自媒体：这套系统本身就是高价值叙事，可以作为 X / 公众号长期内容主线；
- Super Individual：个人拥有自己的数据、skills、代码和自动化，而不是被 corporate-owned centralized AI tools 锁住。

### 风险或待验证点

- Garry 文中提到的规模数字与工具链在不同地方可能有更新：X Article 提到约 100,000 pages，GBrain README 当前写的是 17,888 pages、4,383 people、723 companies、21 cron jobs。应视为不同时间口径或生产/开源版本差异，不应混为一个精确指标。
- GBrain 是 TypeScript/Bun/PGLite 技术栈，是否要直接引入需要单独 spike，不能贸然替换现有 Obsidian + Hermes 体系。
- “100+ crons / 24/7”对个人系统有维护成本，翡冷翠当前应先做少量高价值 cron，而不是追求数量。
- Skillify 如果没有测试和质量门槛，会产生技能库膨胀和重复分类问题。需要沿用 GPT-5.5 Prompt Strategy 与 Superpowers 的 skill authoring discipline。

---

## 可执行下一步

- [ ] 单独 spike GBrain：clone、安装、跑 demo brain，评估是否能与 Obsidian / Hermes 共存。
- [ ] 给 X2Doc 增加“吸收判断”固定输出：是否转 skill、是否转 cron、是否写入 Obsidian index。
- [ ] 设计一个 Book Mirror skill：不是总结书，而是映射到翡冷翠个人项目和身份目标。
- [ ] 把 `x2doc → skillify candidate` 加入 Superpowers 工作流文档。
- [ ] 对当前 Hermes skills 做一次“thin harness / fat skills”视角的健康检查，减少重复、拆分过长 skill。

---

## 原文摘录

> In the last 5 months, AI made me a builder again.

> I want to show you, with specific examples, what personal AI actually looks like when you stop treating it as a chat window and start treating it as an operating system.

> The system that runs my life didn't exist as a monolith. It was assembled from skills. And those skills were themselves created by a skill.

> Skills compose.

> This is the difference between having a filing cabinet and having a nervous system.

> The model is just the engine. Everything else is the car.

> The future belongs to individuals who build compounding AI systems, not to individuals who use corporate-owned centralized AI tools.

> Fat skills. Fat code. Thin harness. The LLM on its own is just an engine. You can build your own car.

---

*来自翡冷翠*
