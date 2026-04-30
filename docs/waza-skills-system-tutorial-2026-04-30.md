# Waza (技) - Claude Code 技能系统完整指南

> 来源：[tw93/Waza](https://github.com/tw93/Waza) — Engineering habits you already know, turned into skills Claude can run.  
> 整理时间：2026-04-30  
> 来自翡冷翠

---

## 简介

**Waza (技, わざ)** 是一个日语武术术语，指"技巧"：一种通过反复练习直到成为本能的动作。

优秀的工程师不只是写代码。他们会深入思考需求、审查自己的工作、系统化地调试、设计具有明确意图的界面，并阅读原始资料。他们清晰地写作，通过产出而非消费内容来学习新知识。

AI 比大多数初级工程师更有能力。但如果没有结构，这种能力就会退化为通用的、敷衍的工作。**Waza 将其转化为精确的工作流程**：设定明确目标和约束条件的八项技能，然后让模型尽其所能。

三部曲的一部分：
- **Kaku (書く)** 编写代码
- **Waza (技)** 训练习惯
- **Kami (紙)** 发布文档

---

## 核心技能总览

| 技能 | 触发场景 | 核心功能 | 版本 |
|------|----------|----------|------|
| `/think` | 构建新东西之前 | 压力测试设计、验证架构 | v3.16.0 |
| `/design` | 构建前端界面时 | 产生具有美学方向的独特 UI | v3.18.0 |
| `/check` | 任务完成后、合并前 | 审查差异、自动修复、安全验证 | v3.15.0 |
| `/hunt` | Bug 或意外行为 | 系统化调试、确认根本原因 | v3.17.0 |
| `/read` | 任何 URL 或 PDF | 获取为干净 Markdown | v3.14.0 |
| `/write` | 写作或编辑散文时 | 重写使其自然，去除 AI 味 | v3.18.0 |
| `/learn` | 深入不熟悉的领域时 | 六阶段研究工作流 | v3.15.0 |
| `/health` | 审计 Claude Code 设置时 | 检查配置栈健康度 | v3.16.0 |

---

## 技能详细指南

### 一、/think - 设计并验证后再构建

**名称**：think  
**版本**：v3.16.0  
**核心功能**：将粗略想法转化为经过批准的方案，在编写任何代码之前验证架构  

**触发条件**：
- 出方案、给方案、深入分析、怎么设计、用什么方案
- 判断一下、有没有必要、值不值得
- "what's the best approach", "plan this", "how should I", "should we keep this"

#### 三种模式

**1. 完整模式（Full Mode）**
默认模式。当需要从零构建新功能或做架构决策时激活。

**2. 轻量级模式（Lightweight Mode）**
当用户想要修复而非构建、问题已定义、唯一疑问是"怎么修复"时激活。

输出格式：
- 2-3 句的推荐修复方案
- 先命名暴力解法，默认采用除非用户要优雅方案
- 列出涉及文件（超过 5 个需明确标注）
- 陈述一个风险
- 等待批准后再实施

**3. 评估模式（Evaluation Mode）**
当用户想判断某物是否应存在、保留、暴露或移除时激活。

典型触发："判断一下"、"有没有必要"、"值不值得"、"should we keep this"、"is this worth it"

**流程**：
1. 陈述评估目标和判断类型（价值、风险、权衡）
2. 拍摄当前状态快照：功能、使用者、依赖者
3. grep 和阅读后再发表意见
4. 给出推荐结论和理由（不列选项）
5. 如结论是"移除"或"重大重构"，列出影响范围
6. 等待确认后再行动

#### 核心原则

**动手前检查**：
- 确认工作路径：`pwd` 或 `git rev-parse --show-toplevel`
- 如项目追踪过往决策（ADRs、设计文档），先浏览相关决策
- 如计划涉及默认值、环境变量或配置字段，打开实际配置文件获取实时值

**先检查官方方案**：
在提出自定义实现前，搜索框架内置、官方模式和生态系统标准。如有官方方案，除非能说明为什么不适用，否则作为默认推荐。

**提出方案**：
- 给一个带理由的推荐方案
- 包含工作量、风险和基于的现有代码
- 仅当权衡真的很接近时才提一个备选
- 始终包含一个最小选项
- 识别最脆弱的假设并明确陈述

**阻断性歧义**：
如需求有冲突需用户解决，用一句话命名具体冲突并问哪个优先。不要默默选择。

**额外攻击角度**（仅在涉及外部依赖、高并发或数据迁移时运行）：

| 攻击角度 | 问题 |
|---------|------|
| 依赖失败 | 如外部 API、服务或工具宕机，方案能否优雅降级？ |
| 规模爆炸 | 数据量或用户负载增加 10 倍时，哪一步先崩溃？ |
| 回滚成本 | 如方向错误，能回到什么状态、有多难？ |

#### 交付前验证

- 超过 8 个文件或 1 个新服务？明确承认
- 超过 3 个组件交换数据？画 ASCII 图，找循环
- 列出所有有意义的测试路径：正常路径、错误、边界情况
- 能否在不触碰数据的情况下回滚？
- 列出计划所需的所有 API 密钥、令牌和第三方账户
- 交付前验证所有 MCP 服务器、外部 API 和第三方 CLI 可访问

**批准的方案中禁止占位符**：
禁止模式：TBD、TODO、"implement later"、"similar to step N"、"details to be determined"

#### 输出格式

**已批准的设计摘要**：
- **Building**：这是什么（1 段话）
- **Not building**：明确的超出范围列表
- **Approach**：选定选项及理由
- **Key decisions**：3-5 个及推理
- **Unknowns**：仅明确推迟、有原因和明确负责人的项目

批准后输出：
> Plan approved. To implement: describe what you want built, or say "implement this plan". After implementation, run `/check` to review before merging.

---

### 二、/design - 带着观点构建

**名称**：design  
**版本**：v3.18.0  
**核心功能**：为任何组件、页面或视觉界面生成独特的、生产级 UI  

**触发条件**：
- 设计、做页面、做组件、不好看、不和谐、样式、前端、UI
- "build page", "create component", "make it look good", "style", "design"
- 截图 + 视觉投诉（"这里很丑"、"fix this"）

#### 核心原则

**如果它能被默认提示生成，那还不够好。**

#### 截图迭代模式

当用户发送截图或图片 + 投诉时激活。

**流程**：
1. 读取截图，用一句话陈述问题：具体哪里不对（间距、对比度、对齐、字体、颜色）
2. 等用户确认诊断后再碰代码
3. 如诊断是已知 UX 问题（分屏同步、无限滚动、虚拟列表、粘性头部），花一轮调研 2-3 个同类别成熟产品如何解决
4. 找到负责代码：grep 组件名或 class，读取实际文件
5. 应用最小修复：一个组件，一个问题
6. 请用户在浏览器中验证

**边界**：如修复需改 3 个以上组件，或揭示的是方向问题而非具体 bug，暂停并运行完整方向锁定。

**重构优先级顺序**（重构现有 UI 而非从零构建时）：
字体替换 → 颜色清理 → hover/active 状态 → 布局和留白 → 替换通用组件 → 添加 loading/empty/error 状态 → 字体排版润色

#### 先锁定方向

写任何代码前，列出 2-3 个同类别成熟产品（如 Notion、Linear、Typora、iA Writer、Raycast），各写一句他们如何解决当前问题。然后写代码。

用环境的原生提问机制直接问用户：

1. **谁使用这个，在什么场景？**（分析师仪表板 vs 落地页 vs 引导流程）
2. **美学方向是什么？**精确命名：密集编辑、原始终端、纸上墨水、野兽派网格、温暖模拟感。"Clean and modern" 不是方向。
3. **这个要留下什么记忆？**一种字体、颜色系统、意外动效、非对称布局。选一个并让它明显。
4. **硬约束是什么？**框架、包大小、对比度最低要求、键盘可访问性
5. **标志性微交互是什么？**按下时缩放、交错显示、上下文图标动画。选一个并确切知道怎么实现

**不回答完这五个问题不要继续。**

#### 源仓库作为参考

当用户提供仓库 URL 或粘贴现有产品源代码时：
- 文件树是菜单，不是大餐
- 读取实际源代码：theme.ts、colors.ts、tokens.css、全局样式表、布局脚手架、用户提到的具体组件
- 提取精确值：hex 代码、间距刻度、字体栈、边框半径

仅附加目标组件文件夹或包。排除 .git、node_modules、dist 和 lock 文件。

#### App Shell 例外（侧边栏 + 主工作区）

当问题 1 的答案是 app shell（Slack、Linear、Notion 类）：
- 装饰背景默认关闭
- 表面层次使用背景色阶梯和阴影
- 所有交互元素获得 active:scale-95
- 按钮半径在每个组件类型内一致
- 在第一个组件前提交一个命名的半径刻度

#### 非协商约束

- 禁止模板美学：三卡片、相同阴影、相同内边距
- 禁止 Inter 作为展示字体：它传达不了任何信息
- 禁止声称看起来对而不打开浏览器
- 浅模式应用：相邻嵌套表面必须视觉上不同

#### 被要求给选项时

至少给 3 个变化，跨 genuinely different 维度：
- **变化维度**：视觉密度、字体个性、色温、布局结构、动效特征、装饰量、抽象级别
- **混合方法**：一个紧跟现有惯例、一个以新方式重新混合品牌 DNA、一个故意意外
- **从安全到大胆**：第一个选项安全可理解，后面的推得更远

#### 交付

交付时包含：
- 美学方向，2-3 句话命名和论证
- 非明显选择解释：字体、颜色决策、布局逻辑
- 替换占位内容为真实内容的说明

---

### 三、/check - 交付前审查

**名称**：check  
**版本**：v3.15.0  
**核心功能**：审查代码差异、自动修复安全问题、用证据验证  

**触发条件**：
- review、看看代码、检查一下、有没有问题、是否需要优化、合并前
- 看看 issue、看看 PR
- "review my code", "check changes", "before merge", "code review"

#### 核心原则

读取差异，找到问题，安全地修复能修复的，询问其余的。**完成意味着本会话中运行并通过了验证。**

#### 分类模式（Triage Mode）

当用户提及：issue、PR、"review all"、triage、"批量处理" 时激活。

**流程**：
1. 拉取待办事项：`gh issue list -R <repo> --state open --limit 20` 和 `gh pr list -R <repo> --state open`
2. 对每个项目，检查修复是否已发布：`git log --oneline <latest-tag>..HEAD | grep -i "<keyword>"`
3. 如已发布：关闭并备注
4. 如已合并但未发布：回复"已修复，等下一个版本 release"并关闭
5. 如无修复：分析并行动

**签署行**：
```
triage:           N reviewed, N closed, N deferred
```

#### 审查深度

| 深度 | 标准 | 审查员 |
|------|------|--------|
| Quick | <100 行，1-5 个文件 | 基础审查 |
| Standard | 100-500 行，或 6-10 个文件 | 基础 + 条件专家 |
| Deep | 500+ 行，10+ 个文件，或触及 auth/payments/数据变更 | 基础 + 所有专家 + 对抗性测试 |

#### 硬性阻断（合并前修复）

- **破坏性自动执行**：任何标记"安全"或"自动运行"且修改用户可见状态的任务必须需要明确确认
- **发布产物缺失**：验证发布模板中列出的每个产物都存在并已上传
- **差异中的未知标识符**：grep 确认任何新引入的函数、变量或类型在代码库中存在
- **注入和验证**：系统入口点的 SQL、命令、路径注入；硬编码或日志记录的凭证
- **依赖变更**：package.json、Cargo.toml、go.mod、requirements.txt 中的意外添加或版本提升

#### 自动修复路由

| 类别 | 定义 | 操作 |
|------|------|------|
| safe_auto | 明确无误、无风险：拼写错误、缺失导入、风格不一致 | 立即应用 |
| gated_auto | 可能正确但改变行为：空检查、错误处理添加 | 批量到一个确认块 |
| manual | 需要判断：架构、行为变更、安全权衡 | 在签署中呈现 |
| advisory | 仅信息性 | 在签署中注明 |

#### 验证

运行测试脚本或项目已知验证命令。粘贴完整输出。

如脚本退出非零或打印"(no test command detected)"：停止。不要声称完成。

**对于 bug 修复**：在修复完成前，必须存在一个回归测试，在未修复代码上失败。

#### 签署格式

```
files changed:    N (+X -Y)
scope:            on target / drift: [what]
review depth:     quick / standard / deep
hard stops:       N found, N fixed, N deferred
specialists:      [security, architecture] or none
new tests:        N
verification:     [command] -> pass / fail
```

#### 文档审查模式

当：PDF、文档、发布说明、白皮书、最终版本、或"check this document"时激活。

**审查清单**：
- **隐私扫描**：检测 PII（姓名、公司、就业日期、薪资暗示、位置详情）
- **语调一致性**：标记声音转换、语域不匹配、公式化措辞
- **双语验证**：CN/EN 对，确认翻译准确性和术语一致性
- **渲染检查**：占位文本剩余、样式违规、字体回退、损坏的图片链接

---

### 四、/hunt - 先诊断再修复

**名称**：hunt  
**版本**：v3.17.0  
**核心功能**：找到错误、崩溃、意外行为和测试失败的根本原因  

**触发条件**：
- 排查、查查、报错、崩溃、不工作、不对、跑不通
- "debug", "why broken", "not working", "what's wrong", "fix error", "stack trace"

#### 核心原则

应用于症状的补丁会在别处制造新 bug。

**在触碰代码前，能用一句话陈述根本原因**：
> "I believe the root cause is [X] because [evidence]."

命名具体文件、函数、行或条件。"A state management issue" 不可测试。"Stale cache in useUser at src/hooks/user.ts:42 because the dependency array is missing userId" 可测试。

#### 诊断信号

**良好进展**：日志行匹配假设、能在运行前预测下一个错误、理解从根本原因到症状的传播路径、能写一个在未修复代码上失败的测试

**合理化警告**：
- "I'll just try this" = 无假设，先写出来
- "I'm confident" = 运行一个证明它的工具
- "Probably the same issue" = 从头重新读取执行路径
- "It works on my machine" = 在驳回前列举每个环境差异
- "One more restart" = 逐字读取最后一个错误；无新证据不要重启超过两次

#### 硬性规则

- 修复后相同症状 = 硬阻断；"let me just try this" 也是
- 三个失败假设后，停止，使用交接格式
- 验证后再声称：运行 `sw_vers` / `node --version` / `grep` 等，不要凭记忆陈述版本
- 外部工具失败：先诊断再切换
- 注意转移：当有人说"那部分不重要"时，将其视为信号
- 视觉/渲染 bug：先静态分析，再添加控制台日志
- 修复原因，而非症状：如修复触及超过 5 个文件，暂停并与用户确认范围

#### 二分模式（Bisect Mode）

当症状是"以前工作，现在坏了"或"更新后坏了"时激活。

**流程**：
1. 找到最后一个已知好的标签：`git tag --sort=-version:refname | head -5`
2. 定义非交互式通过/失败测试命令
3. 运行 `git bisect start / bad / good <tag>`
4. 让 bisect 驱动，不要跳跃
5. 大文件只读一次，从笔记引用而非每步重读
6. 当 bisect 指出罪魁祸首提交时，只读那个 diff 来确定引入回归的具体行

#### 确认或丢弃

添加一个针对性工具：日志行、失败断言、或最小的能在假设正确时失败的测试。运行它。如证据与假设矛盾，完全丢弃它并用刚学到的重新定向。

#### 结果格式

**成功格式**：
```
Root cause:        [what was wrong, file:line]
Fix:               [what changed, file:line]
Confirmed:         [evidence or test that proves the fix]
Tests:             [pass/fail count, regression test location]
Regression guard:  [test file:line] or [none, reason]
```

**交接格式**（三个失败假设后）：
```
Symptom:
[Original error description, one sentence]

Hypotheses Tested:
1. [Hypothesis 1] → [Test method] → [Result: ruled out because...]
2. [Hypothesis 2] → [Test method] → [Result: ruled out because...]
3. [Hypothesis 3] → [Test method] → [Result: ruled out because...]

Evidence Collected:
- [Log snippets / stack traces / file content]
- [Reproduction steps]
- [Environment info: versions, config, runtime]

Ruled Out:
- [Root causes that have been eliminated]

Unknowns:
- [What is still unclear]
- [What information is missing]

Suggested Next Steps:
1. [Next investigation direction]
2. [External tools or permissions that may be needed]
3. [Additional context the user should provide]

Status: blocked
```

---

### 五、/read - 获取任何 URL 或 PDF 为 Markdown

**名称**：read  
**版本**：v3.14.0  
**核心功能**：将任何 URL 或本地 PDF 转换为干净 Markdown  

**触发条件**：
- 消息中的任何 URL、看这个链接、总结一下、读一下、看看这个网页
- "read this", "check this URL", "summarize this"

#### 路由表

| 输入 | 方法 |
|------|------|
| feishu.cn, larksuite.com | 飞书 API 脚本 |
| mp.weixin.qq.com | 代理级联优先，内置微信文章脚本仅当代理失败 |
| .pdf URL 或本地 PDF 路径 | PDF 提取 |
| GitHub URLs | 优先 raw content 或 gh，代理级联仅作为 fallback |
| x.com, twitter.com | 代理级联（r.jina.ai 保留图片 URL） |
| 其他一切 | 代理级联 |

#### 输出格式

```
Title:  {title}
Author: {author} (if available)
Source: {platform}
URL:    {original url}

Content
{full Markdown, truncated at 200 lines if long}
```

#### 保存规则

默认保存到 `~/Downloads/{title}.md`，带 YAML frontmatter。仅当用户说"just preview"或"don't save"时跳过。

如文件已存在，追加 -1、-2 等。绝不未经明确确认就覆盖现有文件。

#### 图片下载

默认仅保存 Markdown。仅当用户明确要求："download images"、"save images"、"带图"、"下载图片" 时才下载图片。

---

### 六、/write - 去除 AI 味道

**名称**：write  
**版本**：v3.18.0  
**核心功能**：重写中英文散文使其自然，删除生硬、公式化的措辞  

**触发条件**：
- 帮我写、改稿、润色、去 AI 味、写一段
- "draft", "edit text", "proofread", "sound natural", "polish", "rewrite"

#### 核心原则

从散文中剥离 AI 模式并重写使其像人类写作。不要改进词汇；移除改进的表演。

**起飞前检查**：
- 文本存在？如用户只给指令无实际散文，用一句话询问文本
- 受众锁定？如目标受众不清且无法从文本推断，编辑前询问

#### 语言检测

从被编辑的文本检测，而非用户的命令：
- 含中文字符 → 加载 references/write-zh.md
- 否则 → 加载 references/write-en.md

#### 硬性规则

- 意义优先，风格其次。如移除 AI 模式会改变作者意图意义，保留原文
- 不静默重组。不要重组标题、重排序段落或合并章节，除非明确请求结构性变更
- 输出后停止。交付重写文本。不要附加变更列表、理由或结束语

#### 双语审查模式

当：中英文混合、"Chinese copywriting"、"bilingual consistency"、"release notes" 时激活

**中文规则**（来自 chinese-copywriting-guidelines）：
- 中英文之间加空格
- 不混用标点（中文用 、。？！；：）
- 所有实例术语一致

**中文文档中的英文**：标记未解释的英文，建议翻译或添加上下文

**双语对**：确认 EN 和 CN 版本传达相同含义；标记翻译损失

#### 发布说明模板模式

当："release"、"changelog"、"version"、"release notes" 时激活

从提交消息生成：
- Breaking Changes
- New Features
- Fixes & Improvements
- Deprecations

格式：tw93/Mole 风格（编号列表、粗体标签、一句用户效果、双语）

---

### 七、/learn - 六阶段研究工作流

**名称**：learn  
**版本**：v3.15.0  
**核心功能**：运行六阶段研究工作流，将不熟悉的领域或收集的来源转化为可发布的输出  

**触发条件**：
- 学习一下、深入研究、研究一下、整理成文章
- "research", "deep dive", "help me understand", "compile sources", "unfamiliar domain"

**不适用**：快速查找或单文件阅读

#### 三种模式

| 模式 | 目标 | 入口 | 出口 |
|------|------|------|------|
| **Deep Research** | 充分理解领域以便写作 | Phase 1 | Phase 6: 可发布草稿 |
| **Quick Reference** | 快速建立工作心理模型，无写作计划 | Phase 2 | Phase 2: 仅笔记 |
| **Write to Learn** | 已有材料，通过写作强制理解 | Phase 3 | Phase 6: 可发布草稿 |

#### 六阶段工作流

**Phase 1: Collect（收集）**
收集一级来源（论文、官方博客、构建者文章、权威仓库），非摘要/解释器

1. **Discover** - 搜索插件发现领域，深度搜索 2-3 个子主题
2. **Fetch** - 每个 URL 通过 `/read` 获取
3. **File** - 移动到子主题目录

目标：博客 5-10 来源，深度技术调研 15-20 来源

**Phase 2: Digest（消化）**
通读材料，保留好的，删除差的（最终删除约一半）

- 关键主张检验：是否在同一来源的两个不同上下文出现？能否预测？是否专家共识？
- 矛盾来源：记录双方立场和证据

**Phase 3: Outline（大纲）**
为文章撰写大纲，每节标注来源。无来源的节需处理。

**Phase 4: Fill In（填充）**
按大纲逐节撰写。卡顿时返回 Phase 2 该子主题。

**卡顿信号**：
- 重写开头三次以上
- 依赖单一来源
- 需新来源
- 无法口头解释主张

**Phase 5: Refine（精炼）**
- 删除冗余冗长段落
- 标记论证不流畅处
- 识别缺口：未解释概念、需来源的主张
- 去除 AI 模式：填充短语、二元对比、戏剧化碎片、过度副词

**Phase 6: Self-review and Publish Readiness（自检与发布准备）**
用户线性阅读整篇文章，标记问题并修复，至少两轮。用户确认准备发布后停止，不自动发布。

#### 注意事项

- 不要收集 30 个二手解释器而非一级来源
- 安装了 `/read` 时不要使用 `WebFetch` 或 `curl`
- 不要把有说服力的解释器当绝对真理
- Phase 2 是构建心理模型而非写摘要
- 用户说准备发布后不要主动上传到博客或社交平台

---

### 八、/health - 审计 Claude Code 配置栈

**名称**：health  
**版本**：v3.16.0  
**核心功能**：审计完整六层 Claude Code 配置栈  

**触发条件**：
- 检查 claude、健康度、配置检查、配置对不对
- "Claude ignoring instructions", "check config", "settings not working", "audit config"

**不适用**：调试代码或审查 PR

#### 六层框架

`CLAUDE.md → rules → skills → hooks → subagents → verifiers`

#### 项目层级评估

| 层级 | 信号 | 期望配置 |
|------|------|----------|
| **Simple** | <500 文件，1 贡献者，无 CI | 仅 CLAUDE.md；0-1 技能；hooks 可选 |
| **Standard** | 500-5K 文件，小团队或 CI | CLAUDE.md + 1-2 规则；2-4 技能；基本 hooks |
| **Complex** | >5K 文件，多贡献者，活跃 CI | 完整六层配置 |

#### 工作流程

**Step 0: 评估项目层级**
根据文件数、贡献者数、CI 活跃度判断

**Step 1: 收集数据**
```bash
bash "${CLAUDE_SKILL_DIR:-$HOME/.agents/skills/health}/scripts/collect-data.sh"
```

**Step 1b: MCP 实时检查**
测试每个 MCP 服务器：调用每个服务器一个无害工具，记录 `live=yes/no`

**Step 2: 分析**
- **Simple**: 本地分析，无 subagents
- **Standard/Complex**: 并行启动两个 subagents
  - Agent 1 (Context + Security)
  - Agent 2 (Control + Behavior)

**Step 3: 报告**
格式：`Health Report: {project} ({tier} tier, {file_count} files)`

#### 严重程度分级

- `[!] Critical` - 违规规则、危险 allowedTools、MCP 开销 >12.5%、安全发现、凭证泄漏
- `[~] Structural` - CLAUDE.md 内容层错误、缺失 hooks、描述过长、verifier 缺口
- `[-] Incremental` - 过时项、全局 vs 本地放置、上下文卫生、陈旧 allowedTools

#### 注意事项

- 未经确认不自动应用修复
- 不对简单项目应用复杂层级检查
- 不要遗漏本地覆盖（读取 `settings.local.json`）
- subagent 超时不是 MCP 失败
- 使用 CLAUDE.md 规定的语言报告

---

## 技能路由与串联

### 按工作流阶段分路

#### Pre-build（动手前）
| 触发 | 技能 |
|------|------|
| 新功能 / 架构决策 / "怎么设计" / "应该用什么方案" / "判断一下" / "有没有必要" / "值不值得" | `/think` |
| UI / 组件 / 页面 / 视觉界面 / 前端 | `/design` |

#### Post-build（交付前）
| 触发 | 技能 |
|------|------|
| 实现完成 / 合并前 / "review 一下" / "看看这段代码" | `/check` |
| review issue / review PR / triage / 批量处理 / "看看有没有 issue" | `/check` (Triage Mode) |

#### Diagnostic（出问题了）
| 触发 | 技能 |
|------|------|
| 报错 / 崩溃 / 测试失败 / 行为异常 / "为什么不工作" | `/hunt` |
| Claude 忽略指令 / hook 失灵 / MCP 异常 / 配置审计 | `/health` |

#### Content（内容进出）
| 触发 | 技能 |
|------|------|
| 消息含 http(s) URL / 任何网页链接 / PDF 路径 / "看一下这个", "总结这个" | `/read` |
| 写作 / 改稿 / 润色 / 去 AI 味（中英文） | `/write` |
| 深度研究一个陌生领域 / 六阶段研究到成稿 / 一批材料沉淀成文章 | `/learn` |

### 歧义消解规则

1. **最具体优先**：`/design` 比 `/think` 更具体（仅限 UI 决策）
2. **URL 按内容类型二次分流**：含 URL → 先 `/read` 取回 → 长文研究素材接 `/learn`；仅要一句总结停 `/read`
3. **改错 vs review**：代码交付/PR → `/check`；代码跑不通/行为错 → `/hunt`
4. **配置异常 vs 代码错误**：Claude 不听话/hook 不触发/MCP 掉链子 → `/health`；用户代码抛异常 → `/hunt`
5. **长文产出 vs 润色**：从零到成稿 → `/learn`；已有稿子要改 → `/write`
6. **判断 vs 调试**："判断一下" + 报错/异常/不工作 → `/hunt`；"判断一下" + 有没有必要/值不值得 → `/think` Evaluation Mode

### 常见串联工作流

技能转换需用户手动触发：

| 工作流 | 路径 |
|--------|------|
| 设计功能 | `/think` → 批准 → "实现 X" → `/check` → 合并 |
| 研究和写作 | `/read` (获取资源) → `/learn` (综合) → `/write` (润色) |
| 调试和验证 | `/hunt` (找到根本原因) → 修复 → `/check` (审查更改) |
| 配置修复 | `/health` (发现问题) → "修复" → `/health` (再审计) |

---

## 额外功能

### Statusline

Claude Code 的极简状态行：上下文窗口、5 小时配额和 7 天配额。

颜色编码：
- 上下文：低于 70% 绿色，70-85% 黄色，高于 85% 红色
- 配额：蓝色、洋红色、红色阈值

**安装命令**：
```bash
curl -sL https://raw.githubusercontent.com/tw93/Waza/main/scripts/setup-statusline.sh | bash
```

### English Coaching

大多数 AI 模型接受的英语训练远超其他任何语言，因此用你的母语发出的每个提示都要经过一层不可见的翻译层。切换到英语，推理会更清晰，答案会更准确。

---

## 使用 Waza 的最佳实践

### 1. 不要跳过 Pre-build 阶段
在写第一行代码前，先用 `/think` 锁定方案。看似慢，实则避免返工。

### 2. UI 工作必须有方向
使用 `/design` 时，先回答五个方向锁定问题。没有方向的"clean and modern"会沦为 AI 平庸。

### 3. 审查是质量保证
每次实现后用 `/check` 把关。发现问题的成本在交付前最低。

### 4. 调试要找到根因
使用 `/hunt` 时，在触碰代码前能用一句话陈述根本原因。修复症状会制造新 bug。

### 5. 内容工作流水线化
研究工作用 `/learn` 六阶段工作流，从收集到发布系统化完成。

---

## 相关资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/tw93/Waza |
| 作者 | tw93 (https://github.com/tw93) |
| Stars | 4.2k |
| Forks | 256 |

---

## 快速参考卡

```
┌─────────────────────────────────────────────────────────────┐
│  Waza (技) - Claude Code 技能系统                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Pre-build（动手前）                                         │
│  ─────────────────                                          │
│  /think    → 新功能、架构决策、方案设计                      │
│  /design   → UI、组件、页面、视觉界面                        │
│                                                             │
│  Post-build（交付前）                                        │
│  ──────────────────                                         │
│  /check    → 代码审查、合并前验证                            │
│                                                             │
│  Diagnostic（出问题了）                                      │
│  ───────────────────                                        │
│  /hunt     → 报错、崩溃、行为异常                            │
│  /health   → Claude 不听话、配置异常                          │
│                                                             │
│  Content（内容工作）                                         │
│  ────────────────                                           │
│  /read     → 获取任何 URL/PDF 为 Markdown                    │
│  /write    → 重写散文、去除 AI 味                            │
│  /learn    → 六阶段研究到成稿                                │
│                                                             │
│  Chaining（串联）                                            │
│  ────────────                                               │
│  /think → 实现 → /check                                     │
│  /read → /learn → /write                                    │
│  /hunt → 修复 → /check                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

*来自翡冷翠*
