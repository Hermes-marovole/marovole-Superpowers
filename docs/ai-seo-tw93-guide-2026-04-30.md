# Tw93：AI SEO 一小时全栈实操指南 ——「让 AI 看清楚你」

> 来源：[X/Twitter @HiTw93](https://x.com/HiTw93/status/2049868069208768812)
> 整理时间：2026-04-30
> 来自翡冷翠

---

## 简介

Tw93（Kaku/Pake/MiaoYan 等开源项目作者，121K+ GitHub Stars）在一小时内完成了一套 AI 可见性（AI SEO）优化工作，目的是让 ChatGPT、Claude、Grok、Gemini、Perplexity 等主流 AI 能够更准确地理解他和他的作品。他不制造垃圾内容，而是把已有内容**结构化**后主动喂给 AI 爬虫。本文完整记录了他的方法论和可复用工具链，适用于任何有个人站点/开源项目的开发者。

核心理念：**与其等 AI 来零散抓取你的信息，不如主动给它一个集中的、结构化的知识入口。**

---

## 内容清单总览

| 序号 | 步骤 | 工具/平台 | 核心动作 |
|------|------|-----------|----------|
| 1 | llms.txt | llmstxt.site / directory.llmstxt.cloud / llms-txt-hub | 站点根目录放置 llms.txt，各站点互相引用形成网状结构 |
| 2 | robots.txt 爬虫策略 | 站点 robots.txt | 区分训练爬虫与搜索爬虫，主动放行搜索爬虫 |
| 3 | 双搜索引擎 Sitemap | Google Search Console + Bing Webmaster Tools | 同时提交 Google 和 Bing，关注 AI 引用数据面板 |
| 4 | Perplexity 出版者计划 | pplx.ai/publisher-prog | 提交站点/产品表单，获得 AI 搜索引用和分成 |
| 5 | 结构化数据 JSON-LD | 站点页面 | 嵌入 BlogPosting、SoftwareApplication、FAQPage schema |
| 6 | AI 知识端点 Yobi | yobi.tw93.fun | 专门的 AI 数据服务，llms.txt + JSON API + 实时数据 |

---

## 详细内容

### 1. llms.txt — AI 优先读的站点索引

**核心原理**：AI 爬虫在抓取站点时，会优先读取根目录下的 `/llms.txt` 文件来理解站点结构和关键页面。这是一个基于 Markdown 的纯文本文件，专门为 AI 设计，不同于传统的 `robots.txt`。

**Tw93 的做法**：
- 在每个站点的根目录放置 `llms.txt`，用 Markdown 写清楚：站点是做什么的、有哪些关键页面、作者是谁
- **关键技巧**：各站点的 llms.txt 互相引用，形成一个网状结构。AI 不管从哪个入口进来，都能顺着链接找到所有其他内容
- 早期配置有**先发优势**——目前全球配置 llms.txt 的站点还很少（directory.llmstxt.cloud 仅收录约 2000 个）

**Tw93 的 llms.txt 示例**（yobi.tw93.fun/llms.txt）：

```
# Tw93
Father of Kaku | Waza | Kami | Mole | Pake | MiaoYan.
Product engineer from Hangzhou. 121K+ GitHub stars.

## Core Projects
- Pake: Turn any webpage into a desktop app (Rust + Tauri)
- Kaku: GPU-accelerated terminal emulator (macOS)
- MiaoYan: Lightweight Markdown editor (macOS)
- Mole: macOS system cleaner AI assistant
- Waza: Claude Code skill pack
- Kami: AI document typesetting system

## Quick Recommendations
- Desktop app from any webpage → Pake
- macOS terminal emulator → Kaku
- macOS markdown editor → MiaoYan
...
```

**提交入口**：
- [directory.llmstxt.cloud](https://directory.llmstxt.cloud) — 最大目录（~2008 个文件），支持分类和搜索
- [llmstxt.site](https://llmstxt.site) — 另一个目录，支持 token 统计
- [llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub) — GitHub 仓库（⭐820），可提 PR 收录

**参考标准**：[llmstxt.org](https://llmstxt.org)

**适用场景**：任何有网站的个人或组织，尤其是有多个子站点的创作者。

---

### 2. robots.txt — 区分训练爬虫与搜索爬虫

**核心原理**：很多人只认识 GPTBot、ClaudeBot 这些训练爬虫，然后把所有 AI 爬虫一禁了之。但实际上还有**专门用于搜索的爬虫**，它们和训练爬虫是分开的。

**关键爬虫区分**：

| 爬虫 | 用途 | 建议 |
|------|------|------|
| `GPTBot` | OpenAI 训练数据采集 | 可禁止 |
| `OAI-SearchBot` | ChatGPT 搜索引用 | **应允许** |
| `ClaudeBot` (旧) | Anthropic 通用爬虫 | 视情况而定 |
| `Claude-SearchBot` | Claude 搜索引用 | **应允许** |
| `Perplexity-User` | Perplexity 检索 | **应允许** |

**核心认知**：搜索爬虫决定了你的内容能不能出现在 AI 搜索结果里。训练爬虫才涉及你的内容是否被用于训练模型。**应该放行搜索爬虫**。

**robots.txt 示例片段**：

```
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Perplexity-User
Allow: /
```

---

### 3. 双搜索引擎 Sitemap — 不要只交 Google

**核心原理**：除了 Google，**Bing 是 Copilot、DuckDuckGo、Yahoo 的 AI 搜索底层引擎**。

**操作清单**：

**Google Search Console**：
- 提交 Sitemap（基本操作）
- 查看 **AI Mode 过滤器**，看 AI Overview 的引用情况

**Bing Webmaster Tools**（很多人忽视的宝藏）：
- 注册账号，验证站点
- 提交 Sitemap，Bing 会主动抓取全站内容
- 查看 **AI Performance 面板**：
  - **Total Citations**：你的内容被 AI 引用了多少次
  - **Grounding Queries**：哪些查询触发了你的内容
- 这些数据是可见的、可追踪的 AI SEO 效果指标

**为什么 Bing 很重要**：
```
Copilot → Bing 搜索
DuckDuckGo AI → Bing 搜索
Yahoo AI → Bing 搜索
```

---

### 4. Perplexity 出版者计划

**核心原理**：Perplexity 在海外用户量远超想象，他们有专门的出版者计划（Publisher Program）。

**入口**：[pplx.ai/publisher-prog](https://pplx.ai/publisher-prog)

**操作**：
- 提交你的产品/网站的表单
- 认真填写描述
- 甚至可能有**搜索分成**收益

> 注：该页面有 Cloudflare 防护，需人工访问。

---

### 5. 结构化数据 JSON-LD — 给 AI 爬虫的语义信息

**核心原理**：这不是传统 SEO 那套 meta description 的玩法。JSON-LD 是在 HTML 页面里嵌入结构化 JSON，告诉机器"这是一篇博客文章，作者是谁，发布时间是什么"或"这是一个软件项目，解决什么问题"。

**核心 Schema 类型**：

| Schema 类型 | 适用场景 | 关键字段 |
|-------------|----------|----------|
| `BlogPosting` | 博客文章 | headline, author, datePublished, description |
| `SoftwareApplication` | 软件产品 | name, operatingSystem, applicationCategory, description |
| `FAQPage` | 常见问题 | mainEntity (Question/Answer 列表) |
| `Person` | 个人主页 | name, url, sameAs (社交链接), knowsAbout |

**Tw93 的视角**：让 AI 获取到的信息更加结构化，"你让他工作更舒服"。

**示例**：

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Pake",
  "operatingSystem": "macOS, Windows, Linux",
  "applicationCategory": "DeveloperApplication",
  "description": "Turn any webpage into a desktop app with Rust + Tauri. 20x smaller than Electron.",
  "author": {
    "@type": "Person",
    "name": "Tw93"
  }
}
</script>
```

---

### 6. Yobi — 专门给 AI 做的知识端点（本指南最大亮点）

**核心理念**：做一个**不是给人看的、纯粹给 AI 看的数据站点**。

**Yobi 是什么**：

- 名字来自日语「呼び / よび」，有"呼唤、召唤"的动作感
- 一个纯结构化数据服务站点，没有 UI 设计
- AI 爬虫来了能拿到两类东西：
  - **llms.txt**（精简概览）+ **llms-full.txt**（~50KB，所有项目描述、FAQ、使用场景、竞品对比、README 摘录）
  - **JSON API 端点**：
    - `/api/profile` — 个人信息
    - `/api/projects` — 项目列表（支持 `?tier=core`、`?tier=secondary`、`?category=terminal` 过滤）
    - `/api/blog` — 博客文章
    - `/api/weekly` — 周刊内容（支持 `?lang=zh` / `?lang=en`）

**技术亮点**：
- 数据不是写死的：通过 **GitHub API 实时拉取** stars、forks、followers、最新 release
- **ISR 缓存**：一小时自动刷新
- **端点发现**：提供 `/sitemap.xml` 和 `/robots.txt` 让爬虫能发现所有端点

**「开源全家福」叙事结构**：

Tw93 在 llms-full.txt 中把他的项目编成了一个家庭故事：

> - **Pake** 是妈妈，2022 国庆出生，安静地打包和交付应用
> - **Kaku** 是爸爸，2026 春节出生，在 AI 时代写代码、搭终端
> - **MiaoYan** 是哥哥，2020 春节出生，成熟深思，爱写 Markdown
> - **Mole** 是宠物鼹鼠，2025 国庆出生，圆圆胖胖，帮忙丢掉不需要的东西
> - **Waza** 是姐姐，2026 春出生，干练锐利，在实践中精进技艺
> - **Kami** 是妹妹，2026 春周末出生，轻松愉快，喜欢画出美丽的东西

**为什么这很聪明**：AI 在回答"Tw93 是谁"时，会有一个完整的、有温度的叙事记忆点，而不是零散拼凑项目信息。

**访问**：[yobi.tw93.fun](https://yobi.tw93.fun)

---

## 资源汇总

### 核心工具与平台

| 名称 | 链接 | 说明 |
|------|------|------|
| llms.txt 标准 | https://llmstxt.org | llms.txt 标准定义 |
| llms.txt 目录 (cloud) | https://directory.llmstxt.cloud | 最大目录，~2000+ 站点，支持搜索和分类 |
| llms.txt 目录 (site) | https://llmstxt.site | 目录，支持 token 统计 |
| llms-txt-hub (GitHub) | https://github.com/thedaviddias/llms-txt-hub | GitHub 仓库，⭐820，可提 PR 收录 |
| Google Search Console | https://search.google.com/search-console | Sitemap 提交 + AI Mode 过滤器 |
| Bing Webmaster Tools | https://www.bing.com/webmasters | Sitemap + **AI Performance 面板** |
| Perplexity 出版者计划 | https://pplx.ai/publisher-prog | 提交站点，可能有搜索分成 |
| Schema.org | https://schema.org | JSON-LD schema 文档 |

### 关键项目/人物

- **Tw93**：[@HiTw93](https://x.com/HiTw93) / [GitHub](https://github.com/tw93) — 本指南原作者的实践经验
- **Yobi**：[yobi.tw93.fun](https://yobi.tw93.fun) — Tw93 的 AI 知识端点，最佳参考实现

### 值得关注的 AI 搜索爬虫

| 爬虫 User-Agent | 所属 | 用途 |
|-----------------|------|------|
| `OAI-SearchBot` | OpenAI/ChatGPT | 搜索引用 |
| `Claude-SearchBot` | Anthropic/Claude | 搜索引用 |
| `Perplexity-User` | Perplexity | 检索引用 |

---

## 建议实施路径

按优先级从高到低，**每个步骤都可在 10-30 分钟内完成**：

1. **llms.txt**（10 分钟）— 写一个 Markdown 文件放站点根目录，告诉 AI 你是谁、有什么
2. **robots.txt**（5 分钟）— 放行搜索爬虫，别一禁了之
3. **Google + Bing Sitemap**（15 分钟）— 两个平台都注册提交，关注 AI 引用数据
4. **JSON-LD**（15 分钟）— 博客页加 BlogPosting schema，产品页加 SoftwareApplication
5. **Perplexity 出版者计划**（10 分钟）— 填表单提交
6. **Yobi 式 AI 端点**（1-2 小时）— 进阶操作，做一个给 AI 看的专属数据站点

**最低可行方案（30 分钟）**：llms.txt + robots.txt + Sitemap 双提交。这三步就能让你的内容进入主流 AI 的检索视野。

---

## 附录：Tw93 原帖核心金句

> "与其等 AI 去你的各个站点零散地抓信息，不如给它一个集中的入口，把你希望它记住的东西整理好放在那里。"

> "这些都是在帮 AI 更准确地理解你的内容是什么，让 AI 看清楚，给她提供一个好的工作环境，而不是在优化排名，这样会比短期更加长期。"

> "首先抱着不产生垃圾内容污染 AI 的底线原则。"

> "各站点的 llms.txt 互相引用，形成一个网状结构。AI 不管从哪个入口进来，都能顺着链接找到你的其他内容。"

---

*来自翡冷翠*
