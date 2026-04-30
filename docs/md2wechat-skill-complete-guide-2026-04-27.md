# md2wechat-skill - 公众号创作全流程 CLI 完整整理

> 来源：https://github.com/geekjourneyx/md2wechat-skill
> 作者：极客杰尼 (@geekjourneyx / @seekjourney)
> 整理时间：2026-04-27
> 来自翡冷翠

---

## 简介

**md2wechat** 是一个专为 AI 时代设计的公众号创作工作台 CLI 工具，由独立开发者极客杰尼开发。它不是一个简单的格式转换器，而是一个覆盖「写作 → 去 AI 痕 → 排版 → AI 配图 → 上传 → 推送草稿」全流程的 Agent-native 工具。支持 Claude Code / Codex / OpenClaw 等 Coding Agent 原生集成。

GitHub Stars: 1.6k+ · 语言: Go · License: MIT

---

## 核心定位

| | 其他工具 | md2wechat |
|---|---|---|
| **输出一致性** | LLM 每次不同 | API 模式确定性输出，同样 Markdown 永远相同 |
| **排版系统** | 靠 prompt 碰运气 | 43 个结构化排版模块（`:::block` 语法），API 专属 |
| **主题数量** | 无 / 寥寥几个 | 40+ 专业主题，微信渲染精调 |
| **全流程** | 只做格式转换 | 写作 → 去 AI 痕 → 排版 → AI 配图 → 上传 → 推送草稿 |
| **Agent 集成** | 无结构约定 | JSON envelope、capabilities 端点、discovery 命令 |

---

## 安装方式

### macOS（推荐）
```bash
brew install geekjourneyx/tap/md2wechat
```

### npm 全局安装
```bash
npm install -g @geekjourneyx/md2wechat
```

### Go 安装
```bash
go install github.com/geekjourneyx/md2wechat-skill/cmd/md2wechat@v2.1.0
```

### 安装脚本
```bash
curl -fsSL https://github.com/geekjourneyx/md2wechat-skill/releases/download/v2.1.0/install.sh | bash
```

### Agent Skill 安装
```bash
npx skills add https://github.com/geekjourneyx/md2wechat-skill --skill md2wechat
```

---

## 命令速览

| 命令 | 说明 |
|------|------|
| `inspect` | 解析文章元数据与发布 readiness，推荐 `convert` 前先跑 |
| `preview` | 生成本地预览 HTML，不触发任何上传或草稿副作用 |
| `convert` | Markdown → 微信格式 HTML，可选 `--draft` 直接推送草稿 |
| `write` | 风格写作，从一个想法生成完整文章 + 封面提示词 |
| `humanize` | AI 去痕，让 AI 生成的文章听起来像真人写的 |
| `generate_cover` | AI 生成封面图，内置专业 preset |
| `generate_infographic` | AI 生成信息图，内置 10+ 风格 preset |
| `upload_image` | 上传图片到微信永久素材库 |

---

## 两种工作模式

### AI 模式（免费）
- 不需要 API Key
- 生成排版 prompt，由外部 LLM 继续处理 HTML
- 3 个基础主题：autumn-warm / spring-fresh / ocean-calm
- 适合实验、偶发写作

### API 模式（专业）
- 需要 API Key（扫码联系作者申请）
- 秒级响应，直接返回最终 HTML
- 40+ 专业主题（Minimal / Focus / Elegant / Bold 四大系列）
- 43 个高级排版模块（`:::block` 语法）
- 确定性输出，同样 Markdown 每次结果完全一致
- 适合品牌内容、团队协作、自动化发布

---

## 高级排版模块（API 专属核心能力）

基于 `:::block` 语法的结构化排版组件系统。不是 prompt，是一套确定性的内容设计语言。

### 示例语法
```markdown
:::block hero
eyebrow: 深度观察
title: AI 时代的公众号写作
subtitle: 为什么你需要重新定义「好内容」
:::

:::block callout type=tip
高级排版模块仅在 API 模式下生效。
:::

:::block timeline
- 2024：GPT-4 发布，内容生产门槛归零
- 2025：AI 写作工具爆发，同质化严重
- 2026：高质量、有视角的内容成为稀缺品
:::
```

### 6 大类模块

| 类别 | 目的 | 代表模块 |
|------|------|---------|
| **opening 开场类** | attention — 让读者知道值不值得读 | hero, cards, verdict, stats |
| **infographic 信息图类** | readability — 让手机窄屏阅读不累 | toc, steps, part, timeline |
| **judgment 判断类** | memorability — 让读者记住判断/品牌 | verdict, manifesto, quote |
| **evidence 证据类** | credibility — 让判断有据可查 | case, data, comparison, ref |
| **conversion 行动类** | conversion — 收藏/关注/咨询/购买 | cta, faq, checklist, offer |
| **brand 品牌类** | identity — 统一品牌感知 | author-card, brand-story, newsletter |

### 发现与验证命令
```bash
md2wechat layout list --json              # 全部 43 个模块
md2wechat layout list --serves attention  # 按用途筛选
md2wechat layout show hero --json         # 模块完整规格
md2wechat layout validate --file article.md  # 验证用法
```

---

## Agent 发现命令

```bash
md2wechat capabilities --json              # 当前实例能力总览
md2wechat themes list --json               # 所有可用主题
md2wechat prompts list --kind image --json # 图片 prompt catalog
md2wechat providers list --json            # 图片生成 provider
md2wechat layout list --json               # 高级排版模块列表
```

所有命令加 `--json` 后 stdout 只输出 JSON envelope，适合脚本和 Agent 直接消费。

---

## 全流程示例

```bash
# 1. 从一个想法生成初稿 + 封面提示词
md2wechat write --style dan-koe
# 2. AI 去痕
md2wechat humanize article.md
# 3. AI 生成封面图
md2wechat generate_cover --article article.md
# 4. 预览排版效果
md2wechat convert article.md --preview
# 5. 转换并推送草稿箱
md2wechat convert article.md --draft --cover cover.jpg
```

在 Claude Code 中一句话搞定：
```
"用 Dan Koe 风格写一篇关于 AI 时代独立开发者的文章，生成封面，推送到微信草稿箱"
```

---

## 图片生成支持

| 服务 | 推荐 | 说明 |
|------|------|------|
| Volcengine Ark | ⭐ 主推荐 | 豆包 Seedream 系列，高质量，国内直连 |
| ModelScope | 次推荐 | 有免费额度，国内访问稳定 |
| OpenRouter | 通用 | 多模型聚合，支持 Gemini / Flux |
| OpenAI | 通用 | 官方 DALL-E |
| Google Gemini | 通用 | 官方 Gemini 图片生成 |

---

## Agent 集成平台

| 平台 | skill 路径 | 安装文档 |
|------|------------|---------|
| Claude Code / Codex / OpenCode | `skills/md2wechat/` | `npx skills add ...` |
| Obsidian（Claudian 插件） | `~/.claude/skills/` | docs/OBSIDIAN.md |
| OpenClaw | `platforms/openclaw/md2wechat/` | docs/OPENCLAW.md |

---

## 项目结构

```
.
├── cmd/md2wechat/           # Cobra 命令入口
│   ├── main.go
│   └── ...                  # 各子命令实现
├── internal/
│   ├── publish/             # 发布主编排 + AssetPipeline
│   ├── inspect/             # metadata 解析 + readiness 计算
│   ├── preview/             # 只读预览 HTML 渲染
│   ├── draft/               # 草稿平台适配
│   └── wechat/              # 微信 API 适配
├── skills/md2wechat/        # Coding Agent skill 包
├── platforms/openclaw/      # OpenClaw 专用 skill 包
├── docs/                    # 完整文档目录（19 个文档）
├── examples/                # 示例文章
└── assets/                  # 图标、GIF 演示、二维码
```

---

## 文档清单

| 文档 | 说明 |
|------|------|
| QUICKSTART.md | 详细图文教程，新手优先 |
| USAGE.md | 所有命令和选项完整说明 |
| LAYOUT.md | 高级排版模块保姆级教程（43 个模块） |
| DISCOVERY.md | discovery 命令与 Prompt Catalog |
| INSTALL.md | 多平台安装指南 |
| CONFIG.md | 配置文件与环境变量 |
| IMAGE_PROVISIONERS.md | AI 图片生成服务配置 |
| WECHAT-CREDENTIALS.md | 微信凭证与 IP 白名单 |
| ARCHITECTURE.md | 项目架构说明 |
| FAQ.md | 20+ 常见问题解答 |
| TROUBLESHOOTING.md | 故障排查 |
| OPENCLAW.md | OpenClaw 平台安装 |
| OBSIDIAN.md | Claudian 插件集成 |
| SKILL-RULE.md | Skill 开发规则 |
| DESIGN.md | 设计文档 |
| HUMANIZE.md | AI 去痕机制 |
| WRITING_FAQ.md | 写作 FAQ |
| SMOKE.md | 冒烟测试 |

---

## 关键链接

| 名称 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/geekjourneyx/md2wechat-skill |
| 作者主页 | https://jieni.ai |
| 作者 X/Twitter | https://x.com/seekjourney |
| Theme Gallery | https://md2wechat.app/theme-gallery |
| ClawHub | https://clawhub.ai/geekjourneyx/md2wechat |
| 作者公众号 | 微信搜「极客杰尼」 |

---

## 分析：是否吸收到 Hermes 技能体系

### 与现有技能对比

Hermes 已有 `wechat-formatter`（productivity/wechat-formatter），但比较后发现：

| 维度 | wechat-formatter（现有） | md2wechat（新） |
|------|------------------------|-----------------|
| 定位 | CSS 排版规范 + 手动粘贴 HTML | 全流程 CLI，端到端自动化 |
| 输出 | 生成 HTML 让人粘贴 | 直接推送到微信草稿箱 |
| 排版模块 | 基础 CSS 样式 | 43 个结构化 `:::block` 组件 |
| 主题 | 一套品牌规范 | 40+ 专业主题 |
| AI 去痕 | 无 | 有 `humanize` 命令 |
| 封面生成 | 无 | 有 `generate_cover` 命令 |
| Agent-native | 无 | JSON envelope + capabilities 发现 |
| 微信对接 | 无 | 直接通过 API 上传草稿 |
| 确定性输出 | 依赖 LLM | API 模式确定性 |

### 结论：值得吸收

md2wechat 不是 wechat-formatter 的替代品，而是**升级版**。它在 wechat-formatter 的基础上增加了：
1. 端到端自动化（Markdown → 草稿箱）
2. 专业排版引擎（43 个 `:::block` 组件）
3. Agent-native 集成（JSON envelope / discovery）
4. AI 去痕 + 封面生成

**建议吸收方式**：不替换现有 wechat-formatter，而是创建一个新的专用 skill（推荐 `productivity/md2wechat`），因为：
- wechat-formatter 适合快速排版（Lightweight）
- md2wechat 适合完整公众号工作流（Full workflow）
- 两者可以互补使用

### 注意事项
- **API Key 依赖**：完整功能需要微信 AppID/Secret + API Key（付费），AI 模式有限但免费
- **Go 依赖**：CLI 需要 Go 环境或 Homebrew 安装
- **国内网络**：微信 API 需要国内网络访问

---

*来自翡冷翠*
