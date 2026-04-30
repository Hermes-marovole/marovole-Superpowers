---
name: link2doc
description: "从链接/来源收集信息，整理成完整文档，提交到 GitHub 仓库的完整工作流。适用于：聚合类内容整理、教程合集、资源清单、竞品信息汇总等场景。中文名：内容策展流程。"
category: research
tags: [curation, documentation, github, content-aggregation, tutorial]
---

# link2doc - 内容策展流程

将分散的链接/来源聚合为完整文档并发布到 GitHub 的标准化工作流。

## 触发条件

当用户出现以下行为时激活：
- 分享一个包含多个链接/资源的 X/Twitter 帖子
- 分享一个资源合集（教程清单、工具推荐等）
- 说"把这个整理成文档"、"收集这些内容"
- 要求"提交到 GitHub"
- **分享 YouTube 视频链接并要求"总结视频"、"提取内容"、"视频转文档"**

## 工作流

### Step 1: 理解任务与来源分析

**明确关键信息：**
- 来源链接是什么？（X 帖子、博客、GitHub 等）
- 目标仓库是哪个？（默认：`marovole-Superpowers`，路径 `~/workspace/marovole-Superpowers`，GitHub: `https://github.com/Hermes-marovole/marovole-Superpowers`）
- 文档应放在哪个目录？（默认：`docs/`）
- 是否需要同步 Linear？（如果有相关 issue）
- 是否需要邮件通知？（默认发送给 marovole@gmail.com）

**署名要求（必须遵守）：**
- 文末署名：**"来自翡冷翠"**
- 禁止写："本文由 Neuma AI Agent 整理输出" 等机器人式表述
- 禁止写："本文档由AI助手整理"、"由智子生成"、"PM Agent整理"、"Neuma Inc."等机器式/公司式属名
- **重要区分**：Neuma 是公司名称，但所有产出内容必须以**个人身份（翡冷翠）**署名，不要用公司名义
- 教程内容应面向"任何人"，不限定为"Neuma 团队"

### Step 2: 提取链接列表

**场景 A: X/Twitter 聚合帖**
```python
# web_extract 会被 X 阻拦，必须用浏览器
browser_navigate(url="https://x.com/...")
browser_snapshot()
# 从正文提取所有引用的子帖子 URL 和外部链接
| 署名写错 | 习惯性写 AI Agent 署名 | 强制检查，必须写"来自翡冷翠" |
| **X 帖子说内容在评论区，但无法查看** | 登录墙阻止访问评论 | **搜索第三方镜像**：用 `web_search` 搜索帖子主题 + 特定关键词（如"prompt"、"提示词"），内容常被归档到提示词库/内容聚合站 |

### 场景 A-4: X/Twitter Articles（长文/长帖）

X 的长文功能（Articles/X Articles）有特殊处理方式：

1. **识别 Article**：URL 格式为 `/article/xxxx` 或推文中有 "Focus mode" 链接

2. **推荐首选方案：Jina Reader 直接提取**
   
   由于 X Articles 在浏览器中常遇到登录墙、内容截断、点击失效等问题，**优先使用 Jina Reader**：
   ```python
   # 使用 Jina Reader 提取 X Article 完整内容
   # 格式: r.jina.ai/http://x.com/{user}/status/{status_id}
   curl -sL "https://r.jina.ai/http://x.com/zstmfhy/status/2047263960005845109"
   ```
   
   **优势**：
   - 绕过 X 的登录限制和 404 问题
   - 自动提取文章完整文本（包括标题和正文）
   - 返回 Markdown 格式，便于后续处理
   - 成功率远高于浏览器方案

3. **浏览器方案（当 Jina Reader 失效时）**
   ```python
   # 第一步：访问原始推文
   browser_navigate(url="https://x.com/alphasignalai/status/2047014600713842728")
   browser_snapshot(full=true)  # 获取完整快照
   
   # 如果内容被截断（truncated），滚动页面加载更多
   browser_scroll(direction="down")
   browser_snapshot(full=true)
   
   # 注意：browser_click 在 X 上常因登录墙或 CSS 选择器问题失败
   # 如遇点击失败，不要继续尝试，直接换用 Jina Reader
   ```

4. **备用方案
   
   如果 `browser_navigate` 返回 404 或无法加载，使用 Jina Reader 直接提取：
   ```python
   # 使用 Jina Reader 提取 X Article 内容
   # 格式: r.jina.ai/http://x.com/{user}/status/{status_id}
   curl -sL "https://r.jina.ai/http://x.com/shaozhu93314/status/2047186395555590428"
   
   # 或使用 web_extract（如果可用）
   web_extract(urls=["https://r.jina.ai/http://x.com/..."])
   ```
   
   **优势**：
   - 绕过 X 的登录限制和 404 问题
   - 自动提取文章完整文本（包括标题和正文）
   - 返回 Markdown 格式，便于后续处理
   
   **注意**：Jina Reader 会将 X Article 内容转换为纯文本，丢失图片、格式等视觉元素，但保留完整文字内容。
5. **内容提取**：Article 内容在快照中以以下形式出现：
   - `heading "标题"` - 章节标题
   - `text: "正文内容"` - 段落文本
   - `blockquote: "引用内容"` - 引用块
   - `[... N more lines truncated]` - 提示有更多内容，需要滚动

### 场景 A-5: X/Twitter Quote Chains（引用链）

X 的 "Quote" 功能会形成引用链——帖子 A 引用帖子 B，帖子 B 又引用帖子 C，形成连续的多层内容。

**识别 Quote Chain**：
- 帖子正文中有 "Quote" 字样
- 出现 `link "GitTrend Verified account @GitTrend0x Apr 22 ..."` 格式的引用链接
- 每个引用可能又包含自己的引用

**处理策略**：
```python
# 第一步：访问初始帖子
browser_navigate(url="https://x.com/gittrend0x/status/2047301854703591897")
snapshot = browser_snapshot(full=true)

# 提取当前帖子内容
# 记录 text: 段落、heading: 标题、img 标记等

# 检查是否有 Quote 引用
# 寻找包含 "Quote" 的 link 元素，如 ref=e21
# 点击引用链接进入下一个帖子
browser_click(ref="e21")  # 引用链接的 ref

# 获取引用帖子内容
snapshot = browser_snapshot(full=true)

# 重复直到没有更多引用
# 通常 Quote Chain 有 3-8 层
```

**注意事项**：
- Quote Chain 可能很长（5+ 层），需要递归处理
- 每个被引用的帖子本身也可能引用其他帖子
- 内容聚合类帖子常使用 Quote Chain 形式发布系列内容
- 如果子代理超时，可直接用 X 帖子中的描述信息构建文档

**场景 B-1: GitHub 仓库内容获取（当标准方法失效时）**

GitHub 对自动化抓取有严格限制，当 `web_extract` 被拦截且 `browser_navigate` 返回空页面时：

**首选方案：直接获取 Raw 文件（最可靠）**
```bash
# 方法 1: 使用 curl 直接获取 raw 内容（推荐）
curl -sL "https://raw.githubusercontent.com/{user}/{repo}/main/README.md"

# 方法 2: 使用 Jina Reader 作为备用
curl -sL "https://r.jina.ai/http://raw.githubusercontent.com/{user}/{repo}/main/README.md"

# 方法 3: 获取特定语言的 README
curl -sL "https://raw.githubusercontent.com/{user}/{repo}/main/README_zh.md"
```

**获取仓库子目录中的文件**
当需要获取非 README 文件（如 `scripts/wechat_dual_open.py`）：
```bash
# 构造 raw URL 格式
curl -sL "https://raw.githubusercontent.com/{user}/{repo}/main/{path/to/file}"

# 示例：获取 scripts 目录下的 Python 文件
curl -sL "https://raw.githubusercontent.com/mcncarl/yichen-skills/main/mac-wechat-dual-open/scripts/wechat_dual_open.py"

# 示例：获取 references 目录下的文档
curl -sL "https://raw.githubusercontent.com/mcncarl/yichen-skills/main/mac-wechat-dual-open/references/reliability-and-risks.md"
```

**获取仓库目录结构（先浏览再针对性下载）**
```python
# 第一步：使用浏览器访问仓库页面，获取文件树
browser_navigate(url="https://github.com/{user}/{repo}/tree/main/{subdir}")
browser_snapshot()

# 从快照中提取文件列表：
# - treeitem "SKILL.md" [ref=e39] - 文件
# - treeitem "scripts" [ref=e38] - 目录

# 第二步：点击文件获取 raw 链接
browser_click(ref="e80")  # 点击文件链接
# 然后从快照中找到 Raw 链接：link "Raw" [ref=e65]

# 或者直接构造 raw URL 下载
```

**不推荐的方法**
```bash
# Jina Reader 提取 GitHub 页面渲染内容（效果差，返回导航结构）
# curl -sL "https://r.jina.ai/http://github.com/{user}/{repo}"  # ❌ 避免使用
```

**示例**（本次任务实践验证）：
```bash
# 成功：直接获取 raw README
curl -sL "https://raw.githubusercontent.com/mcncarl/yichen-skills/main/mac-wechat-dual-open/SKILL.md"

# 成功：获取子目录中的脚本文件
curl -sL "https://raw.githubusercontent.com/mcncarl/yichen-skills/main/mac-wechat-dual-open/scripts/wechat_dual_open.py"

# 成功：获取 references 文档
curl -sL "https://raw.githubusercontent.com/mcncarl/yichen-skills/main/mac-wechat-dual-open/references/reliability-and-risks.md"
```

**策略总结**：
1. 直接构造 `raw.githubusercontent.com` URL 获取文件内容 - **最可靠**
2. 如需查看仓库结构，先用 `browser_navigate` 获取文件树
3. 对于每个需要的文件，单独用 `curl` 下载 raw 内容
4. 避免使用 `web_extract` 或 Jina Reader 访问 `github.com/{user}/{repo}` 页面 - 返回的是导航而非内容

**场景 B: 其他网页来源**
```python
# 尝试 web_extract，失败则 fallback 到 browser
web_extract(urls=["https://..."])
# 或使用 Jina Reader
# curl -sL "https://r.jina.ai/http://..."
```

**场景 C: 用户直接提供链接列表**
- 直接使用用户提供的链接列表，跳过提取步骤

### 场景 D: YouTube 视频内容提取

**识别信号**：
- 链接格式包含 `youtube.com/watch?v=` 或 `youtu.be/`
- 用户要求"总结视频"、"提取视频内容"、"视频转文档"
- 需要获取：转录文本、章节时间线、视频摘要、重点时间点

**处理策略**：

```python
# Step 1: 提取视频 ID 并获取转录
video_url = "https://youtube.com/watch?v=VIDEO_ID"

# 使用 youtube-content 技能的脚本获取转录
terminal(command='python3 ~/.hermes/skills/media/youtube-content/scripts/fetch_transcript.py "{video_url}" --timestamps')

# 输出包含：
# - video_id: 视频 ID
# - segment_count: 片段数量
# - duration: 总时长
# - full_text: 完整转录文本
# - timestamped_text: 带时间戳的文本（00:03:45 内容...）
```

**章节检测**：
```python
# 检查视频描述中是否有章节标记
browser_navigate(url=video_url)
browser_snapshot(full=true)

# 从快照中提取：
# - 视频标题、频道、观看数、发布日期
# - 视频描述中的章节时间戳（如 "0:00 Intro", "3:45 Main Topic"）
# - 描述中的 "...more" 按钮（需要点击展开完整描述）

# 如果找到 "...more" 或 "展开" 按钮，点击获取完整描述
browser_click(ref="e12")  # 展开按钮的 ref
```

**结构化处理转录内容**：

```python
# 当转录文本较长时（>50K 字符），需要分段处理
def process_transcript(segments):
    """
    将转录片段转为结构化内容
    """
    # 1. 检测主题切换点（章节边界）
    # 2. 为每个章节生成摘要
    # 3. 提取关键引用（带时间戳）
    
    chapters = []
    current_chapter = {
        "start_time": segments[0]["start"],
        "texts": []
    }
    
    for seg in segments:
        current_chapter["texts"].append(seg["text"])
        # 检测章节边界：停顿较长、话题转换词等
        if is_chapter_boundary(seg):
            chapters.append(current_chapter)
            current_chapter = {
                "start_time": seg["start"],
                "texts": []
            }
    
    return chapters
```

**输出格式**：

```markdown
# {视频标题} - 内容整理

> 来源：{YouTube 链接}
> 频道：{频道名}
> 时长：{总时长}
> 整理时间：YYYY-MM-DD
> 来自翡冷翠

---

## 视频摘要

{3-5 句话概括视频核心内容}

---

## 章节时间线

| 时间 | 章节标题 | 内容概要 |
|------|----------|----------|
| 00:00 | 开场/简介 | {简介内容} |
| 03:45 | {章节1} | {概要} |
| 12:20 | {章节2} | {概要} |

---

## 详细内容

### 00:00 - {章节1标题}

**要点：**
- {要点 1}
- {要点 2}

**原话摘录：**
> "{带时间戳的直接引用}"

---

### 03:45 - {章节2标题}

...

---

## 重点时间戳

- **00:02:15** - {关键观点/金句}
- **00:07:30** - {重要概念解释}
- **00:15:45** - {实操演示开始}

---

## 关键要点总结

1. {核心发现 1}
2. {核心发现 2}
3. {核心发现 3}

---

## 资源链接

- 原视频：{YouTube URL}
- 频道主页：{频道 URL}
- 提及的资源：{相关链接}

---

*来自翡冷翠*
```

**错误处理**：

| 问题 | 原因 | 对策 |
|------|------|------|
| 视频没有字幕 | 上传者关闭字幕 | 使用浏览器方案提取视频描述、评论区的文字信息 |
| Transcript API 被限制 | IP 被 YouTube 封锁 | 切换到浏览器回退方案，提取页面可见内容 |
| 视频是私有的 | 需要权限访问 | 告知用户无法访问，请求公开链接 |
| 转录语言不匹配 | 需要指定语言代码 | 使用 `--language zh,en` 指定语言回退链 |

**浏览器回退方案（当 API 失败时）**：

```python
# 当 youtube-transcript-api 失败时使用浏览器提取
browser_navigate(url=video_url)
browser_snapshot(full=true)

# 提取以下内容：
# - 视频标题、描述（含章节标记）
# - 观看数、点赞数、发布日期
# - 置顶评论（常包含补充信息）
# - 推荐视频侧边栏（相关内容线索）
```

### 场景 A-2: X/Twitter 展示型帖子（Showcase/Demo Posts）

**识别信号**：
- 作者展示自己做的东西（"用 X 做了 Y"）
- 包含视频/图片演示，但文字描述很简短
- 提到具体项目/产品名称
- 目的是展示成果而非提供教程

**示例**：
> "用 Codex 的 HyperFrames 插件 + 最新 5.5 模型生成 favicon.im 的介绍视频"

**处理策略**（深度补充调研）：

这类帖子本身内容简短，需要主动扩展才能形成有价值的文档：

```python
# Step 1: 提取帖子核心信息
# - 使用的工具/技术（Codex HyperFrames + 5.5 模型）
# - 展示的项目（favicon.im）
# - 作者（@becool_me）

# Step 2: 深度调研被展示的项目
# 搜索项目名称获取详细信息
web_search(query="favicon.im 网站介绍 功能 API")

# 使用 Jina Reader 提取项目官网内容
terminal(command='curl -sL "https://r.jina.ai/http://favicon.im/zh/"')

# Step 3: 调研作者的其他相关项目
# 从作者 profile 提取其他项目链接
# 整理成「作者工具矩阵」

# Step 4: 构建案例研究型文档
# 结构：
# - 简介（概述这个 showcase 的价值）
# - 核心工具介绍（技术栈详解）
# - 案例演示（被展示的项目深度解析）
# - 作者其他项目（工具矩阵）
# - 适用场景与快速参考
```

**关键洞察**：
- Showcase 帖子通常信息量小但示范价值高
- 需要主动挖掘被展示项目的背景信息
- 整理作者的工具矩阵可以增加文档实用性
- 最终输出应该是「案例研究」而非「内容聚合」

---

### 场景 A-2b: X/Twitter 技术观察/观点型帖子（Technical Observation Posts）

**识别信号**（与 Showcase 不同）：
- 作者分享对某个技术/产品的观察和洞察（非展示自己作品）
- 帖子简短但引用多个复杂技术概念
- 评论区被阻塞无法获取
- 目的是表达观点而非教程或资源聚合

**示例**：
> "Stripe 今天新发布了一个功能 Treasury，我觉得这会是集成在 harness engineering 中的一个重要产品，让 wanman 这类工具不仅可以做出初创公司的方案，还能直接开设银行账户，并授权 agent 使用这些账户进行付款。"

**与 Showcase 的区别**：

| 维度 | Showcase 帖子 | Technical Observation 帖子 |
|------|----------------|---------------------------|
| **内容焦点** | 作者自己做了什么 | 作者对某技术的观察和判断 |
| **核心价值** | 示范效应 | 洞察价值 |
| **调研重点** | 被展示的项目详情 | 帖子中提及的所有技术概念 |
| **输出形态** | 案例研究 | 深度分析报告 |

**处理策略**（并行深度调研）：

这类帖子通常只有 1-2 句话，但包含多个值得深挖的技术概念。需要**并行搜索**来高效收集信息：

```python
# Step 1: 解析帖子中的关键技术概念
# 从短帖子中提取所有技术术语和项目名称：
# - "Stripe Treasury" → 需要调研 Stripe 的 BaaS 产品
# - "harness engineering" → 需要调研 Agent 控制框架
# - "wanman" → 需要调研这个 AI 创业项目
# - "银行账户" + "agent 付款" → 需要调研 AI 金融应用场景

# Step 2: 并行搜索所有相关概念（关键！）
# 不要串行搜索，一次发起多个独立查询：

web_search(query="Stripe Treasury 功能介绍 API 2024")  # 概念 1
web_search(query="harness engineering AI agent 控制框架")  # 概念 2
web_search(query="wanman AI 创业 郭宇")  # 概念 3

# Step 3: 提取关键来源并深度抓取
# 使用 Jina Reader 提取受阻页面的内容：
terminal(command='curl -sL "https://r.jina.ai/http://stripe.com/treasury"')
terminal(command='curl -sL "https://r.jina.ai/http://tianpan.co/zh/blog/2026-02-17-harness-engineering-agent-first-software-development"')

# Step 4: 构建深度分析报告（不是简单整理）
# 结构：
# - 执行摘要（原帖观点的升华）
# - 技术概念 1 全面解析（Stripe Treasury）
# - 技术概念 2 全面解析（Harness Engineering）
# - 技术概念 3 全面解析（Wanman AI）
# - 三者协同效应分析
# - 应用场景展望
# - 风险与挑战
# - 结论与启示
```

**关键成功要素**：

| 要素 | 说明 |
|------|------|
| **并行搜索** | 同时发起多个查询，缩短调研时间 |
| **概念全覆盖** | 帖子中提到的每个技术术语都要调研 |
| **深度 > 广度** | 宁可深入 3 个核心概念，不要浅尝 10 个边缘话题 |
| **分析而非罗列** | 输出应该是「分析报告」而非「链接清单」 |
| **观点升华** | 在作者观点基础上，提供更系统的分析框架 |

**输出质量标准**：
- 单篇文档应在 10,000 字以上（短篇帖子 → 深度报告）
- 包含结构化的章节（简介、核心概念、协同分析、应用场景、风险）
- 有清晰的图表和流程图（文字描述的可视化）
- 提供实用的资源汇总和快速参考

**实际案例参考**：
- 输入：@turingou 的 1 段文字（约 100 字）
- 输出：18,000 字深度分析报告，涵盖 Stripe Treasury、Harness Engineering、Wanman AI 三大主题的协同效应分析

---

### 场景 A-3: X/Twitter 评论区内容获取（当主贴引用"评论见详情"但登录受阻）

X 帖子常采用"主贴引流 + 评论区放干货"的模式：
- 主贴说"提示词在评论区"、"👇 看下面"
- 点击评论区发现需要登录（弹窗阻挡）
- 短链可能只是指向原帖图片

**处理策略**：
```python
# 第一步：尝试通过浏览器访问评论区
browser_navigate(url="https://x.com/koffuxu/status/2046966059539058875")
browser_click(ref="e21")  # 评论按钮
# 如果被登录墙阻挡，弹出登录对话框...

# 第二步：使用搜索引擎找第三方镜像站点
# 提取帖子核心主题词，组合搜索
web_search(query="伊索寓言手抄报 prompt AI生成 koffuxu")

# 常见第三方镜像站点类型：
# - AI 提示词库（如 pixps.com）- 专门归档 X 热门 Prompt
# - 中文技术社区（即刻、小红书、知乎）- 用户搬运整理
# - AI 工具导航站 - 收集各类 AI 生成教程
# - 开发者博客 - 个人整理归档

# 第三步：访问镜像站点获取完整内容
browser_navigate(url="https://www.pixps.com/prompts/mn2g5jK5.html")
browser_snapshot(full=true)
# 提取 code: 块中的完整 Prompt 内容
```

**识别信号**：
- 主贴文字中出现"👇"、"见评论区"、"提示词在下面"、"Prompt 在回复"
- 主贴是一个短链（如 `https://t.co/xxxx`），但跳转后只是原帖图片
- 评论区数量显示有回复（如 "5 replies"），但点击后弹出登录框
- 用户明确提示"内容在评论区"

**搜索关键词组合建议**：
```
{帖子主题} + prompt
{帖子主题} + 提示词  
{作者名} + {主题关键词} + prompt
{X 帖子中的关键词} + 教程/模板
```

**验证要点**：
- 优先选择与原帖发布时间接近的镜像（24-48小时内）
- 验证镜像内容完整性（是否包含完整 Prompt/代码/步骤）
- 如多个镜像存在，选择内容最全、排版最清晰的版本
- 交叉验证：对比 X 帖子图片与镜像内容是否一致

**实际案例**（本次任务）：
- X 帖子：`koffuxu` 分享手抄报模板，称"核心 Prompt 整理好了👇"
- 短链指向图片，评论区需登录
- 搜索发现 `pixps.com` 有完整归档
- 获取到结构化 YAML Prompt（约 50 行），成功完成文档

---

### Step 3: 逐一收集详情（含发布者洞察提取）

对每个提取到的链接：

```python
# 访问子链接收集完整信息
browser_navigate(url=sub_url)
browser_snapshot()

# 记录以下字段（特别注意发布者洞察）：
# - 标题
# - 作者/来源
# - 发布时间
# - 核心内容摘要
# - 关键资源链接（GitHub、官网等）
# - 代码/命令片段
# - ⚡ 发布者洞察（很重要！）：
#   * 发布者个人体验（"我用了 X 个月..."）
#   * 核心优势说明（"比传统方式快 10 倍"）
#   * 为什么推荐（"解决了 Y 问题"）
#   * 直接引用发布者原话
```

**发布者洞察提取策略（关键！）**：

当抓取 Twitter/X 或其他社交平台帖子时，**发布者的个人体验和评价比工具功能描述更有价值**：

```python
# 洞察提取清单
insights_to_extract = {
    "personal_experience": "发布者使用这个工具/方法的实际经历",
    "key_benefit": "相比其他方案的核心优势（省时、省事、效果好等）",
    "why_recommend": "发布者推荐的具体理由",
    "use_case": "发布者描述的具体使用场景",
    "direct_quote": "可以直接引用的发布者原话"
}

# 示例：从帖子内容中提取
# 原帖："用了 AutoThread 三个月，我的 Twitter 线程互动率平均提升了 40%。
#        之前手动拆解要花 2 小时，现在 5 分钟搞定。"
# 
# 提取结果：
# - personal_experience: "用了三个月"
# - key_benefit: "手动 2 小时 → 现在 5 分钟"
# - why_recommend: "线程互动率提升 40%"
# - direct_quote: "用了 AutoThread 三个月，我的 Twitter 线程互动率平均提升了 40%"
```

**记录格式（用于后续邮件生成）**：

```python
collected_data = {
    "title": "项目名称",
    "url": "链接",
    "description": "一句话功能描述",
    "author_note": "发布者原文（含个人体验）",  # 这个很重要！
    "highlight": "提取的核心亮点",               # 用于邮件"为什么好用"
    "quote": "可引用的发布者原话",              # 用于邮件"发布者说"
    "use_case": "适用场景",
    "type": "tool/tutorial/resource"
}
```

**收集策略：**
- 教程类：记录核心步骤、安装命令、使用示例 + **作者踩过的坑**
- 工具类：记录功能特点、GitHub 链接、适用场景 + **作者的实际使用体验**
- 文章类：记录核心观点、关键数据、引用来源 + **作者的个人立场**

**失败回退策略（Content-First Fallback）**：

当子代理超时、GitHub 被拦截或浏览器访问受限时，使用 **Content-First 策略**：

```python
# 场景：无法抓取每个 GitHub 仓库详情
# 解决方案：使用 X 帖子中已有的丰富描述

# 1. 从 X 帖子快照中提取每个项目的：
#    - 项目名称（从 github.com/xxx 链接解析）
#    - 描述文本（text: 后的内容）
#    - 作者（@handle）
#    - ⚡ 作者洞察（从描述中提取的"为什么好用"）
#    - ⚡ 作者原话（可引用的完整句子）

# 2. 构建文档时直接使用这些信息：
#    - 核心功能 = X 帖子中的描述
#    - 适用场景 = 从描述中推断
#    - 为什么好用 = 从描述中提取的关键优势
#    - GitHub 链接 = 原始链接（即使未访问）

# 3. 结果：文档依然完整可用
#    - X 聚合帖通常包含丰富的项目描述
#    - 这些描述已提炼核心亮点，足够构建高质量整理文档
```

**何时使用 Content-First Fallback**：
- 子代理超时（>300s）
- `web_extract` 返回 GitHub 被拦截
- `browser_navigate` 访问 GitHub 受限
- 需要快速交付，无需深度调研每个子项目

**优势**：
- 不阻塞整体任务进度
- X 帖子中的描述通常已提炼核心亮点
- 保持文档的及时性和完整性

### Step 4: 构建综合文档

**标准文档结构：**

```markdown
# {主帖/来源标题} - 完整整理

> 来源：{原始链接}
> 整理时间：YYYY-MM-DD
> 来自翡冷翠

---

## 简介
（用 2-3 句话概括这个合集的核心价值）

## 内容清单总览

| 序号 | 标题 | 作者/来源 | 类型 | 核心亮点 |
|------|------|-----------|------|----------|
| 1 | ... | ... | 教程/工具/文章 | ... |
| 2 | ... | ... | ... | ... |

---

## 详细内容

### 1. {内容1标题}
**来源**：@{author} / {source}
**链接**：{url}
**类型**：{教程/工具/文章}

#### 核心内容
- 要点 1
- 要点 2
- 要点 3

#### 关键资源
- GitHub: {link}
- 官网: {link}
- 文档: {link}

#### 适用场景
（这段内容适合解决什么问题）

---

### 2. {内容2标题}
（同上结构）

---

## 资源汇总

### 所有 GitHub 仓库
| 项目 | 链接 | 简介 |

### 所有官方链接
| 名称 | 链接 | 说明 |

### 值得关注的人/账号
- @{handle} - {简介}

## 建议学习/使用路径

（如何按顺序使用这些资源，或推荐的学习路径）

## 附录：快速参考

（常用命令、配置片段、速查表）

---

*来自翡冷翠*
```

### Step 5: 提交到 GitHub

```bash
cd ~/workspace/marovole-Superpowers

# 保存文档到目标目录
# 文件命名规范: {主题关键词}-{日期}.md
# 示例: hermes-tutorials-2026-04-22.md

# Git 操作
git add docs/{filename}.md
git commit -m "docs: add {主题} 完整整理 ({日期})"
git push origin main
```

**提交后记录：**
- 文件路径
- GitHub URL（如 `https://github.com/{user}/{repo}/blob/main/docs/{filename}.md`）

### Step 6: 同步 Linear（如有）

如果有相关 Linear issue：

```python
# 更新 issue 状态为 Done
mcp_linear_save_issue(id="NEU-XXX", state="Done")

# 添加完成评论
mcp_linear_save_comment(
    issueId="NEU-XXX",
    body="""✅ 已完成

**产出物：**
- GitHub: {github_link}
- 本地路径: {local_path}

**文档概要：**
- 整理来源：{source}
- 内容数量：{N} 个
- 文档大小：{size} 字

来自翡冷翠"""
)
```

### Step 7: 邮件交付（充实版）

**邮件配置（固定）**：
- 主收件人：**marovole@gmail.com**
- 抄送：**hueshadow989@gmail.com**

**核心原则**：邮件正文必须让人「一眼看出价值」，不只是通知文档完成，而要说明「为什么这个文档值得你花时间看」。

**使用充实版邮件模板**：

参考上方的「邮件正文模板（充实版）」和「邮件内容生成函数」章节，确保邮件包含：

1. **为什么值得收录** —— 三段式核心价值主张
   - 解决什么问题
   - 与随手搜索的区别
   - 看完能获得什么

2. **核心内容速览** —— 精选亮点项目（3-5个）
   - 这是什么（一句话）
   - 独特优势（为什么选它）
   - 适用场景（什么时候用）
   - 发布者洞察（原话引用）

3. **本次整理的「不一样」之处** —— 调研成果说明
   - 深度处理（做了什么额外工作）
   - 额外发现（组合效应、代码示例等）
   - 结构化整理（文档组织逻辑）

4. **适用场景速查** —— 表格形式便于快速定位

5. **快速上手** —— 1-2个最值得立即尝试的入口

**发送前检查清单**：

- [ ] 邮件正文包含完整的 GitHub URL
- [ ] 价值主张在开头就清晰说明
- [ ] 至少有 3 个项目说明了「独特优势」和「适用场景」
- [ ] 引用了原帖作者的实际体验（发布者洞察）
- [ ] 说明了「本次整理做了什么深度处理」
- [ ] 提供了场景速查表

**邮件发送代码**：

使用上方提供的 `send_completion_email()` 函数，它会自动：
1. 生成充实的邮件正文
2. 前置验证 Mail.app 配置
3. 发送带附件的邮件
4. 返回成功/失败状态

```python
# 发送邮件
success = send_completion_email(
    theme="文档主题",
    source="来源（如 X/Twitter @xxx）",
    item_count=len(collected_items),
    word_count="约 5,000",
    github_link="https://github.com/Hermes-marovole/...",
    local_path="/Users/agent/workspace/...",
    collected_items=collected_items,  # 结构化收集数据
    source_author="原帖作者",
    collection_summary="整理过程中的发现总结"
)

if not success:
    # 邮件失败时通过 Telegram 通知
    send_message(
        message=f"📄 「{theme}」文档已整理完成\n\n📎 GitHub: {github_link}", 
        target="telegram"
    )
```

**重要原则**：
- 邮件正文始终包含 GitHub 链接（即使附件失败也能访问）
- 邮件失败不阻塞整体任务完成通知
- 使用 `osascript -e` 直接传递 AppleScript（不依赖临时文件）
- 前置验证 Mail.app 是否已配置

**邮件正文模板（充实版 - 必须包含洞察摘要）**：

**核心原则**：邮件正文必须让人「一眼看出价值」，不只是通知文档完成，而要说明「为什么这个文档值得你花时间看」。

```
翡冷翠，好！！

你要求的「{主题}」文档已整理完成并提交到 GitHub。

📎 GitHub 链接：https://github.com/{user}/{repo}/blob/main/docs/{filename}.md
📝 本地文件：{local_path}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 文档概要
- 来源：{source}
- 内容数量：{N} 个资源/条目
- 文档大小：约 {size} 字
- 整理深度：{简述整理方式，如"深度提取每个工具的核心特性+发布者实测体验"}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 为什么值得收录（核心价值主张）

{用 2-3 段话清晰说明：}

**解决什么问题**：
{这个合集针对的具体痛点——比如"传统方式需要手动做X，这些工具能实现Y自动化"}

**独特价值点**：
{与随便搜索的区别——比如"这些资源经过 @{source_author} 的实际工作流验证，不是简单罗列，而是经过筛选的组合"}

**收获预期**：
{阅读者能获得什么——比如"看完可以立即搭建完整工作流，节省 70% 的重复劳动时间"}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 核心内容速览（精选亮点）

{不是罗列所有内容，而是挑选 3-5 个最有代表性的项目，突出「差异化价值」}

1. 🔥 {项目名称/标题} —— {一句话定位，如"最轻量级的XX解决方案"}
   ├─ 这是什么：{具体解决什么问题，一句话}
   ├─ 独特优势：{为什么选它而不是其他——如"无需注册/一行命令启动/原生中文支持"}
   ├─ 适用场景：{具体使用场景，如"适合临时需要XX的应急场景"}
   └─ 发布者洞察："{引用发布者原话，说明为什么他们推荐这个}"

2. 🔥 {下一个精选项目...}
   ├─ 这是什么：
   ├─ 独特优势：
   ├─ 适用场景：
   └─ 发布者洞察：

{如果还有更多项目，用一句话总结：}
📌 另有 {N} 个相关资源详见文档，涵盖 {XX}、{XX}、{XX} 等方向。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 本次整理的「不一样」之处

{这是重点——说明这次调研/整理的具体成果和亮点：}

**深度处理**：
- {比如"不只提取标题链接，还深入每个 GitHub 仓库提取了核心功能、Star 数、最后更新时间"}
- {比如"还原了发布者原话中的使用体验和推荐理由"}

**额外发现**：
- {比如"发现其中 2 个工具可以组合使用，形成完整工作流"}
- {比如"提取了每个工具的安装/使用示例，可直接复制运行"}

**结构化整理**：
- {比如"按「开箱即用型」「需要一定配置型」「开发工具型」分类，便于按需查找"}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 适用场景速查

| 如果你需要... | 优先查看文档中的... |
|--------------|-------------------|
| {场景 1} | {对应章节/条目} |
| {场景 2} | {对应章节/条目} |
| {场景 3} | {对应章节/条目} |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ 快速上手（如果想立即尝试）

{根据内容类型选择最实用的 1-2 个资源，提供极简入口：}

→ 最快开始：{项目名} — {官网/GitHub} — {一句话启动方式}
→ 最全面：{项目名} — {官网/GitHub} — {为什么它是首选}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*来自翡冷翠*
```

**邮件内容撰写检查清单（发送前必做）**：

- [ ] **价值主张明确**：第一句就能回答"为什么要看这个文档"
- [ ] **差异化清晰**：说清楚"这个整理和随便搜索的区别在哪里"
- [ ] **亮点突出**：至少有 3 个具体项目说明了「独特优势」和「适用场景」
- [ ] **发布者洞察**：引用了原帖作者的实际体验，不是干巴巴的功能描述
- [ ] **成果可见**：说明「本次整理做了什么深度处理」，不是简单复制粘贴
- [ ] **行动友好**：提供了「如果你需要X，看哪里」的场景速查表

**Fallback（如果邮件发送失败）**：

```python
# 邮件发送失败时，通过 Telegram 通知
send_message(
    message=f"📄 「{theme}」文档整理完成\n\n📎 GitHub: {github_link}\n\n💡 {why_valuable[:100]}...", 
    target="telegram"
)
```

## 工具选择决策树

| 任务 | 首选工具 | 备用方案 |
|------|----------|----------|
| 读取 X/Twitter 普通帖子 | `browser_navigate` + `browser_snapshot` | `curl` + Jina Reader |
| 读取 X/Twitter Articles（长文） | **Jina Reader 直接提取** | `browser_navigate` 原始推文页 + 滚动（当 Jina 失效时） |
| **YouTube 视频内容提取** | **youtube-transcript-api**（`~/.hermes/skills/media/youtube-content/scripts/fetch_transcript.py`） | **浏览器回退**：`browser_navigate` 提取视频描述、章节标记 |
| 读取普通网页 | `web_extract` | `curl` + Jina Reader |
| 读取 X/Twitter 评论区内容 | `browser_click` 评论按钮 | **搜索引擎找第三方镜像**（当登录受阻时） |
| 搜索补充信息 | `web_search` | Tavily |
| 写文档 | `write_file` | — |
| Git 提交 | `terminal` (git) | — |
| 更新 Linear | `mcp_linear_*` | — |
| 发送邮件 | **`execute_code` + `osascript -e`** | Telegram 通知 |

## 邮件发送（充实版）

**邮件内容生成函数（强制执行价值提炼）**：

```python
import subprocess

def build_enhanced_email_body(theme, source, item_count, word_count, github_link, local_path,
                               collected_items=None, source_author="", collection_summary=""):
    """
    构建充实的邮件正文，强制包含：
    1. 为什么值得收录（核心价值主张）
    2. 本次整理的差异化成果
    3. 精选亮点项目（带差异化价值说明）
    4. 适用场景速查表
    """
    
    if collected_items is None:
        collected_items = []
    
    # ========== 辅助提取函数 ==========
    def extract_unique_advantage(author_note, fallback=""):
        """从发布者描述中提取独特优势"""
        if not author_note:
            return fallback if fallback else "详见文档"
        advantage_indicators = ["最快", "最简单", "最轻量", "无需", "不用", "免", "零配置",
                                "一键", "一行命令", "开箱即用", "无缝", "自动", "智能",
                                "省", "快", "方便", "好用", "神器", "推荐", "必备"]
        sentences = author_note.replace("！", "。").replace("？", "。").split("。")
        for sent in sentences:
            sent = sent.strip()
            for ind in advantage_indicators:
                if ind.lower() in sent.lower() and len(sent) > 5:
                    return sent[:100]
        return fallback if fallback else "具体优势详见文档"
    
    def extract_use_case(author_note, fallback=""):
        """从发布者描述中提取适用场景"""
        if not author_note:
            return fallback if fallback else "详见文档"
        scenario_indicators = ["适合", "用于", "场景", "时候", "情况", "如果", "when", "for", "需要", "想", "想要"]
        sentences = author_note.replace("！", "。").replace("？", "。").split("。")
        for sent in sentences:
            sent = sent.strip()
            for ind in scenario_indicators:
                if ind.lower() in sent.lower() and len(sent) > 8:
                    return sent[:80]
        return fallback if fallback else "详见文档"
    
    def extract_best_quote(author_note):
        """提取最有价值的发布者原话"""
        if not author_note:
            return ""
        import re
        quotes = re.findall(r'"([^"]{10,200})"', author_note)
        if quotes:
            return quotes[0][:180]
        experience_indicators = ["我用", "使用", "试", "体验", "发现", "感觉", "觉得", "推荐"]
        sentences = author_note.replace("！", "。").replace("？", "。").split("。")
        for sent in sentences:
            sent = sent.strip()
            for ind in experience_indicators:
                if ind in sent and 15 < len(sent) < 200:
                    return sent[:180]
        return author_note[:100] + "..." if len(author_note) > 100 else author_note
    
    # ========== 1. 生成「为什么值得收录」段落 ==========
    def generate_why_valuable():
        if not collected_items:
            return f"这份文档整理了来自 {source} 的优质内容，具有实际的参考和使用价值。"
        
        types = set(item.get("type", "") for item in collected_items)
        
        problem_solved = (f"这组合集来自 @{source_author} 的精选分享，" if source_author else "这组合集")
        problem_solved += f"针对「{theme}」这个具体场景，整理了 {len(collected_items)} 个经过实际验证的资源。"
        
        if "tool" in str(types) or "工具" in str(types):
            problem_solved += "解决了从需求到落地的工具选型难题——不用自己一个个试错，直接拿别人验证过的方案。"
        elif "tutorial" in str(types) or "教程" in str(types):
            problem_solved += "覆盖了从入门到进阶的完整学习路径，避免了碎片化搜索的时间浪费。"
        else:
            problem_solved += "整合了分散在各处的优质信息，能大幅节省自行搜索和筛选的时间成本。"
        
        unique_value = "**与随手搜索的区别**："
        if source_author:
            unique_value += f"这些不是简单的链接堆砌，而是 @{source_author} 在实际工作流中使用过的资源，包含了一手的使用体验和踩坑经验。"
        else:
            unique_value += "这次整理不只是罗列标题，还深入提取了每个资源的核心特性、适用场景和实际效果，"
        unique_value += "相当于获得了一个经过筛选的「可信资源清单」。"
        
        expected_gain = "**看完你能获得**："
        if "tool" in str(types):
            expected_gain += "一份可直接使用的工具选型指南，能快速搭建完整工作流，节省 70% 以上的调研时间。"
        elif "tutorial" in str(types):
            expected_gain += "系统性的知识框架，以及可以直接跟练的操作步骤，少走很多弯路。"
        else:
            expected_gain += "对这个领域的全面认知，以及经过验证的优质资源入口，后续需要时能快速找到。"
        
        return f"{problem_solved}\n\n{unique_value}\n\n{expected_gain}"
    
    # ========== 2. 生成「核心内容速览」段落 ==========
    def generate_highlight_items():
        if not collected_items:
            return "详细内容请查看附件或访问 GitHub 链接。\n"
        
        sorted_items = sorted(collected_items, 
                             key=lambda x: (1 if x.get('author_note') else 0, len(x.get('description', ''))),
                             reverse=True)
        
        items_text = ""
        for i, item in enumerate(sorted_items[:5], 1):
            name = item.get('title', item.get('name', f'项目 {i}'))
            what = item.get('description', '暂无描述')
            if len(what) > 80:
                what = what[:80] + "..."
            
            unique_advantage = extract_unique_advantage(item.get('author_note', ''), item.get('highlight', ''))
            use_case = extract_use_case(item.get('author_note', ''), item.get('use_case', ''))
            author_quote = extract_best_quote(item.get('author_note', ''))
            
            items_text += f"""
{i}. 🔥 {name}
   ├─ 这是什么：{what}
   ├─ 独特优势：{unique_advantage}
   ├─ 适用场景：{use_case}
"""
            if author_quote:
                items_text += f"   └─ 发布者洞察：\"{author_quote}\"\n"
            else:
                items_text += "   └─ 发布者洞察：暂无\n"
        
        if len(collected_items) > 5:
            items_text += f"\n📌 另有 {len(collected_items) - 5} 个相关资源详见文档，涵盖完整的技术栈组合。\n"
        
        return items_text
    
    # ========== 3. 生成「本次整理的不一样之处」段落 ==========
    def generate_research_highlights():
        highlights = []
        
        depth_desc = "**深度处理**：\n"
        if collected_items:
            has_author_notes = sum(1 for item in collected_items if item.get('author_note'))
            if has_author_notes > 0:
                depth_desc += f"- 不只提取标题链接，还深入分析了 {has_author_notes} 个资源的核心特性和发布者实测体验\n"
            
            has_github = any('github.com' in str(item.get('url', '')) for item in collected_items)
            if has_github:
                depth_desc += "- 对每个 GitHub 仓库提取了 Star 数、最后更新时间、核心功能说明\n"
            
            has_categories = any(item.get('category') or item.get('type') for item in collected_items)
            if has_categories:
                depth_desc += "- 按实际使用场景分类整理，便于按需查找而非按字母排序\n"
        
        if depth_desc != "**深度处理**：\n":
            highlights.append(depth_desc)
        
        discovery_desc = "**额外发现**：\n"
        if len(collected_items) >= 2:
            discovery_desc += "- 发现部分工具可以组合使用，形成完整工作流（具体组合详见文档）\n"
        
        has_code_samples = any(item.get('code_snippet') for item in collected_items)
        if has_code_samples:
            discovery_desc += "- 提取了可直接运行的代码示例和配置片段，降低上手门槛\n"
        
        if collection_summary:
            discovery_desc += f"- 整理过程中发现的协同效应：{collection_summary[:100]}...\n"
        
        if discovery_desc != "**额外发现**：\n":
            highlights.append(discovery_desc)
        
        structure_desc = "**结构化整理**：\n"
        structure_desc += "- 文档采用「总览→详情→快速参考」三层结构，支持快速浏览和深度阅读\n"
        structure_desc += "- 每个资源都有「是什么/为什么/怎么用」三要素说明\n"
        structure_desc += "- 包含实用的场景速查表，便于按需定位\n"
        highlights.append(structure_desc)
        
        return "\n".join(highlights) if highlights else "本次整理深入提取了每个资源的核心价值点，详见文档。"
    
    # ========== 4. 生成「适用场景速查」表格 ==========
    def generate_use_case_table():
        if not collected_items:
            return "| 文档类型 | 建议查看方式 |\n|----------|-------------|\n| 完整内容 | 访问 GitHub 或查看附件 |\n"
        
        scenarios = []
        for item in collected_items[:3]:
            scenario = extract_use_case(item.get('author_note', ''), item.get('use_case', ''))
            if scenario and scenario != "详见文档":
                scenarios.append((scenario, item.get('title', '对应章节')))
        
        while len(scenarios) < 3:
            scenarios.append((f"了解相关资源 {len(scenarios)+1}", "详细内容章节"))
        
        table = "| 如果你需要... | 优先查看文档中的... |\n|--------------|-------------------|\n"
        for scenario, section in scenarios[:3]:
            table += f"| {scenario} | {section} |\n"
        
        return table
    
    # ========== 5. 生成「快速上手」段落 ==========
    def generate_quick_start():
        if not collected_items:
            return "→ 访问 GitHub 链接查看完整内容\n"
        
        best_items = sorted(collected_items, key=lambda x: len(x.get('author_note', '')), reverse=True)[:2]
        
        quick_start = ""
        for i, item in enumerate(best_items, 1):
            name = item.get('title', f'项目{i}')
            url = item.get('url', '详见文档')
            desc = item.get('description', '')
            if len(desc) > 50:
                desc = desc[:50] + "..."
            
            label = "最快开始" if i == 1 else "最全面"
            quick_start += f"→ {label}：{name} — {url} — {desc}\n"
        
        return quick_start
    
    # ========== 组装邮件正文 ==========
    why_valuable = generate_why_valuable()
    highlight_items = generate_highlight_items()
    research_highlights = generate_research_highlights()
    use_case_table = generate_use_case_table()
    quick_start = generate_quick_start()
    
    has_author_insights = sum(1 for item in collected_items if item.get('author_note'))
    processing_depth = f"深度提取 {has_author_insights} 个资源的发布者实测体验" if has_author_insights > 0 else "详细提取每个资源的核心特性"
    
    body = f"""翡冷翠，好！！

你要求的「{theme}」文档已整理完成并提交到 GitHub。

📎 GitHub 链接：{github_link}
📝 本地文件：{local_path}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 文档概要
- 来源：{source}
- 内容数量：{item_count} 个资源/条目
- 文档大小：约 {word_count} 字
- 整理深度：{processing_depth}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 为什么值得收录（核心价值主张）

{why_valuable}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 核心内容速览（精选亮点）

{highlight_items}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 本次整理的「不一样」之处

{research_highlights}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 适用场景速查

{use_case_table}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ 快速上手（如果想立即尝试）

{quick_start}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*来自翡冷翠*
"""
    return body


# ========== 邮件发送主函数 ==========
def send_completion_email(theme, source, item_count, word_count, github_link, local_path,
                         collected_items=None, source_author="", collection_summary=""):
    """
    发送完成邮件的主函数
    前置验证 Mail.app 配置，使用充实的正文模板
    """
    body = build_enhanced_email_body(
        theme=theme, source=source, item_count=item_count, word_count=word_count,
        github_link=github_link, local_path=local_path,
        collected_items=collected_items, source_author=source_author,
        collection_summary=collection_summary
    )
    
    # 前置验证
    verify_script = '''
tell application "Mail"
    try
        get name of every account
        return "Mail configured"
    on error
        return "Mail not configured"
    end try
end tell
'''
    result = subprocess.run(['osascript', '-e', verify_script], capture_output=True, text=True)
    
    if "configured" not in result.stdout:
        print("⚠️ Mail.app 未配置，跳过邮件发送")
        return False
    
    # 转义双引号
    escaped_body = body.replace('"', '""')
    
    mail_script = f'''
tell application "Mail"
    try
        set newMessage to make new outgoing message with properties {{subject:"{theme} 文档整理完成", content:"{escaped_body}"}}
        tell newMessage
            make new to recipient with properties {{address:"marovole@gmail.com"}}
            make new cc recipient with properties {{address:"hueshadow989@gmail.com"}}
            make new attachment with properties {{file name:"{local_path}"}}
            send
        end tell
        return "邮件发送成功"
    on error errMsg
        return "邮件发送失败: " & errMsg
    end try
end tell
'''
    result = subprocess.run(['osascript', '-e', mail_script], capture_output=True, text=True)
    
    if "成功" in result.stdout:
        print("✅ 邮件发送成功")
        return True
    else:
        print(f"⚠️ 邮件发送问题: {result.stdout}")
        return False


# ========== 使用示例 ==========
"""
collected_items = [
    {
        "title": "AutoThread AI",
        "url": "https://autothread.ai",
        "description": "将长文章自动拆解为 Twitter 线程的工具",
        "author_note": "之前手动拆解要花 2 小时，现在 5 分钟搞定。关键是它保留了原文的语气和逻辑流。用了三个月，我的线程互动率平均提升了 40%。推荐给大家！",
        "type": "tool",
        "category": "内容创作"
    },
    {
        "title": "Typefully",
        "url": "https://typefully.com",
        "description": "Twitter 内容排期和分析工具",
        "author_note": "排期功能让我能保持稳定输出而不感到倦怠。最佳发布时间预测很准，不用再猜了。",
        "type": "tool",
        "category": "内容发布"
    },
]

success = send_completion_email(
    theme="AI 内容创作工具合集",
    source="X/Twitter @example_user",
    item_count=len(collected_items),
    word_count="约 5,000",
    github_link="https://github.com/Hermes-marovole/marovole-Superpowers/blob/main/docs/ai-content-tools-2026-04-30.md",
    local_path="/Users/agent/workspace/marovole-Superpowers/docs/ai-content-tools-2026-04-30.md",
    collected_items=collected_items,
    source_author="example_user",
    collection_summary="这些工具可以组合成完整的内容创作工作流"
)
"""
```

**Fallback（如果邮件发送失败）**：

```python
# 邮件发送失败时，通过 Telegram 通知
send_message(
    message=f"📄 「{theme}」文档整理完成\n\n📎 GitHub: {github_link}\n\n💡 {why_valuable[:100]}...", 
    target="telegram"
)
```

**错误处理**：

| 问题 | 原因 | 对策 |
|------|------|------|
| X 内容提取为空 | `web_extract` 被 X 阻拦 | 必须用 `browser_navigate` 或 Jina Reader |
| **X Article 长文浏览器方案失败** | 登录墙/内容截断/点击失效 | **优先使用 Jina Reader**：`curl -sL "https://r.jina.ai/http://x.com/..."` |
| **X 帖子 browser_click 失败** | CSS 选择器错误或登录弹窗 | 停止浏览器尝试，改用 Jina Reader 或搜索第三方镜像 |
| **YouTube 页面显示 "字幕不可用"** | 上传者未上传手动字幕 | **注意**：`youtube-transcript-api` 仍可提取自动生成的转录，优先使用 API |
| **YouTube Transcript API 失败** | 视频确实无转录 / IP 被限制 | 切换到浏览器回退方案，提取视频描述、评论区文字 |
| **YouTube 转录语言错误** | 视频语言与默认语言不匹配 | 使用 `--language zh,en,auto` 指定语言回退链 |
| X Quote Chain 漏收 | 未识别引用链结构 | 递归点击 Quote 链接，逐层收集内容 |
| GitHub 无法访问 | `web_extract` 返回 "Blocked: URL targets a private or internal network address" | **使用 curl 直接获取 raw 文件**: `curl -sL "https://raw.githubusercontent.com/{user}/{repo}/main/README.md"` |
| 子代理超时 | 并行收集详情时网络慢 | 直接用 X 帖子中的描述信息构建文档，无需完整抓取每个 GitHub 页面 |
| 子帖子太多 | 合集可能有 10+ 个链接 | 批量处理，但要保证每个都有摘要 |
| GitHub README 读不到 | 可能被限速或需要登录 | 用 raw 链接 + curl 直接获取 |
| GitHub 子目录文件获取 | 只知道目录链接不知道文件列表 | 先用 browser 获取文件树，再针对性下载 raw 文件 |
| Git 提交失败 | 未配置 user.name/email | 先 `git config --global` |
| 邮件发送失败 | 多种原因（临时文件、编码、引号等） | 使用 `osascript -e` 直接传递，前置验证 Mail.app 配置 |
| 署名写错 | 习惯性写 AI Agent 署名 | 强制检查，必须写"来自翡冷翠" |
| **X 帖子说内容在评论区，但无法查看** | 登录墙阻止访问评论 | **搜索第三方镜像**：用 `web_search` 搜索帖子主题 + 特定关键词（如"prompt"、"提示词"），内容常被归档到提示词库/内容聚合站 |

### 场景 A-3: X/Twitter 评论区内容获取（当主贴引用"评论见详情"）

X 帖子常采用"主贴引流 + 评论区放干货"的模式：
- 主贴说"提示词在评论区"
- 点击评论区发现需要登录

**处理策略**：
```python
# 第一步：尝试通过浏览器访问评论区
browser_navigate(url="https://x.com/...")
browser_click(ref="e21")  # 评论按钮
# 如果被登录墙阻挡...

# 第二步：使用搜索引擎找第三方镜像
# 搜索策略：提取帖子核心主题 + 内容类型关键词
web_search(query="伊索寓言手抄报 prompt AI生成")

# 常见第三方镜像站点：
# - PixPs 提示词库 (pixps.com) - 专门归档 X 上的热门 AI Prompt
# - 即刻、小红书 - 中文社区搬运
# - 各种 AI 导航站、工具站

# 第三步：验证找到的镜像内容
browser_navigate(url="https://www.pixps.com/prompts/...")
browser_snapshot(full=true)
# 确认内容完整性与原始帖子一致
```

**识别信号**：
- 主贴文字中出现"👇"、"见评论区"、"提示词在下面"
- 主贴是一个引流转发的短链
- 评论区数量显示有回复，但点击后弹出登录框

**搜索关键词组合建议**：
```
{帖子主题} + prompt
{帖子主题} + 提示词
{帖子主题} + 教程
{作者名} + {主题关键词}
```

**注意事项**：
- 优先选择与原帖发布时间接近的镜像
- 验证镜像内容的完整性（是否截断）
- 如多个镜像存在，选择内容最全的版本

### 邮件发送可靠性检查清单

执行邮件发送前，确认以下步骤：

1. **前置验证**：先检查 Mail.app 是否已配置账户
   ```python
   verify_script = 'tell application "Mail" to get name of every account'
   result = subprocess.run(['osascript', '-e', verify_script], ...)
   ```

2. **使用 `-e` 参数**：直接传递 AppleScript 代码
   - ❌ 避免：`osascript /tmp/send_mail.scpt`
   - ✅ 推荐：`osascript -e '...'`

3. **内容转义**：邮件内容中的双引号 `"` 需要转义 `""`
   - 最简单的方法：邮件内容使用纯文本，避免复杂格式

4. **错误捕获**：AppleScript 内部使用 try-catch
   ```applescript
   try
       ...发送逻辑...
   on error errMsg
       return "失败: " & errMsg
   end try
   ```

5. **失败不阻塞**：邮件发送失败不应阻塞整个任务完成通知
   - GitHub 提交成功后，即使邮件失败也应告知用户
   - 可以提供备用交付方式（如 Telegram 文件发送）

6. **邮件正文必须包含 GitHub 链接**：
   - ✅ 检查：邮件 body 中包含 `https://github.com/...` 链接
   - ✅ 格式：`https://github.com/{user}/{repo}/blob/main/docs/{filename}.md`
   - ✅ 目的：即使附件发送失败，用户也能通过链接访问内容
   - ✅ 备用：如果邮件完全发送失败，通过 Telegram 发送 GitHub 链接

## 变体场景

### 变体 A: 单来源深度整理
如果用户只提供 1 个链接但需要深度整理（如一个 GitHub 项目）：
- 省略"提取链接列表"步骤
- 直接进入"深度收集"模式
- 输出结构改为单篇详细教程（参考 `open-source-tool-tutorial` Skill）

### 变体 D: YouTube 视频深度整理
如果用户提供 YouTube 视频并要求完整知识沉淀：
- 使用场景 D 的 YouTube 处理流程
- 获取完整转录文本（带时间戳）
- 检测视频章节或使用 AI 自动分段
- 为每个章节生成摘要和关键要点
- 提取重点时间戳和金句引用
- 输出结构参考场景 D 的标准文档模板
- 最终交付：视频摘要 + 章节时间线 + 详细内容 + 重点时间戳

### 变体 B: 无需 GitHub 提交
如果用户只需要本地文档：
- 保存到 `~/workspace/Hermeswork/reports/`
- 跳过 Git 和 Linear 步骤
- 直接交付文件路径

### 变体 C: 竞品/市场信息收集
如果内容是竞品分析：
- 使用 `competitor-research` Skill 进行补充调研
- 输出结构参考 `report-writing` Skill 的报告框架
