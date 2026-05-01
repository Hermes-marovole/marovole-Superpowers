# Open Design - 完整系统指南

> 来源：[nexu-io/open-design](https://github.com/nexu-io/open-design)  
> 星标：9k+ stars | Fork 997  
> 许可证：Apache-2.0  
> 整理时间：2026-05-01  
> 来自翠冷翠

---

## 简介

**Open Design (ODS)** 是 Anthropic Claude Design 的开源替代方案，定位为"会编码的设计工具，会设计的 CLI“。

项目核心理念是 **Local-first（本地优先）** —— 让 AI 助手真正"撸起袖子干实事"，而不仅仅是聊天。它将对话内容固化为可复用的设计系统和技能，支持多种编码 Agent CLI 协同工作。

### 为什么存在

Anthropic 于 2026-04-17 发布的 Claude Design （基于 Opus 4.7）展示了当 LLM 从写作转向设计交付时的可能性，但它是闭源、付费、云端限制、锁定到 Anthropic 模型和技能的。

**Open Design 作为开源替代品：**
- 无锁定 —— 支持 10+ 种主流编码 Agent CLI
- 本地优先 —— `pnpm tools-dev` 启动本地守护进程 + Web 层
- 可部署到 Vercel —— Web 层支持静态导出
- BYOK（Bring Your Own Keys）—— 每个层都支持使用自己的 API 密键

### 核心特性一览

| 特性 | 描述 |
|------|------|
| **支持 11 种编码 Agent CLI** | Claude Code · Codex CLI · Cursor Agent · Gemini CLI · OpenCode · Qwen · GitHub Copilot CLI · Hermes · Kimi CLI · Pi · Kiro —— 自动检测 PATH，一键切换 |
| **31 项内置技能** | 覆盖设计、营销、产品、工程、财务、人事、销售、个人等场景 |
| **72 个品牌级设计系统** | Linear、Stripe、Vercel、Airbnb、Tesla、Notion、Apple、Anthropic、Figma 等 |
| **5 种确定性视觉方向** | Editorial Monocle · Modern Minimal · Warm Soft · Tech Utility · Brutalist Experimental |
| **多形态支持** | Desktop App、CLI、VS Code 扩展 |
| **设备框架** | iPhone 15 Pro、Pixel、iPad Pro、MacBook、Browser Chrome 像素级精度 |

---

## 六大核心理念

### 1. 不发布 Agent，只发布设计工具

> We don't ship an agent. Yours is good enough.

守护进程在启动时自动扫描 PATH 检测已安装的 CLI（`claude`、`codex`、`cursor-agent`、`gemini`、`opencode`、`qwen`、`copilot`、`hermes`、`kimi`、`pi`、`kiro-cli`）。用户可以在模型选择器中自由切换。没有 CLI？`POST /api/proxy/stream` 提供 OpenAI 兼容的 BYOK 代理回退方案。

### 2. 技能即文件，技能即插件

> Skills are files, and skills are plugins.

遵循 Claude Code 的 SKILL.md 规约，每个技能是一个文件夹：`SKILL.md` + `assets/` + `references/` 。将文件夹放入 `skills/`，重启守护进程，技能即出现在选择器中。

### 3. 设计系统是可移植的 Markdown

> Design Systems are portable Markdown, not theme JSON.

基于 VoltAgent/awesome-design-md 的 9 部分 DESIGN.md 模式：颜色、排版、间距、布局、组件、动效、语调、品牌、反模式。切换设计系统 → 下一次渲染自动应用新的设计令牌。

### 4. 交互式问卷表单解决 80% 的需求不明确问题

> The interactive question form answers 80% of asks.

OD 的提示词栈强制规定：每个新设计需求必须从 `<question-form id="discovery">` 开始，而不是代码。锁定表面类型、受众、语调、品牌背景、规模、约束 —— 30 秒的单选约等于节省30分钟的重定向。

### 5. 守护进程让 Agent 感觉就在你的笔记本上

> The daemon makes the agent feel like it's on your laptop, because it is.

守护进程以项目的交付文件夹为工作目录 `cwd: .od/projects/<id>/`启动 CLI。Agent 拥有真实的 Read、Write、Bash、WebFetch 工具，可以读取模板、检索 CSS、写入 brand-spec.md、生成图片、产出 `.pptx`/`.zip`/`.pdf` 文件。

### 6. 提示词栈本身就是产品

> The prompt stack is the product.

发送时的提示词叠加如下：

```
DISCOVERY 指令（Turn-1 表单、Turn-2 品牌分支、TodoWrite、五维度评价）
  + 身份宪章（OFFICIAL_DESIGNER_PROMPT、反 AI 垃圾清单、初级通道）
  + 活动 DESIGN.md（72 系统可用）
  + 活动 SKILL.md（31 技能可用）
  + 项目元数据（类型、保真度、演讲笔记、动效、灵感 ID）
  + 技能侧文件（预飞行自检：读取 assets/template.html + references/*.md）
  + 演示框架指令（deck 模式无 skill 种子时）
```

每一层都可编辑。查看 `apps/web/src/prompts/system.ts` 和 `apps/web/src/prompts/discovery.ts` 了解实际契约。

---

## 技能（Skills）详解

共 **31 项内置技能**，分为两大顶层模式：

### 模式对比

| 模式 | 技能数量 | 主要用途 |
|------|---------|---------|
| **prototype** | 27 | 单页 HTML 交付物（网页原型、移动端 App、邮件、海报等） |
| **deck** | 4 | 水平滑动演示文稿（PPT 风格） |

### 设计与营销表面（prototype 模式）

| 技能 | 平台 | 场景 | 交付物 |
|------|------|------|---------|
| `web-prototype` | desktop | design | 单页 HTML 原型 —— 营销页/首页/文档/SaaS 页面（prototype 模式默认） |
| `saas-landing` | desktop | marketing | Hero / 功能特点 / 定价 / CTA 营销布局 |
| `dashboard` | desktop | operation | 管理后台/分析面板，含侧边栏 + 密集数据布局 |
| `pricing-page` | desktop | sale | 独立定价页 + 对比表 |
| `docs-page` | desktop | engineering | 三栏文档布局 |
| `blog-post` | desktop | marketing | 编辑式长文章 |
| `mobile-app` | mobile | design | iPhone 15 Pro / Pixel 框架的 App 屏幕 |
| `mobile-onboarding` | mobile | design | 多屏移动端引导流程（闪屏 · 价值主张 · 登录） |
| `gamified-app` | mobile | personal | 三帧游戏化移动应用原型 |
| `email-marketing` | desktop | marketing | 品牌产品发布 HTML 邮件（表格回退兼容） |
| `social-carousel` | desktop | marketing | 3 卡 1080×1080 社交媒体轮播图 |
| `magazine-poster` | desktop | marketing | 单页杂志风格海报 |
| `motion-frames` | desktop | marketing | 带循环 CSS 动画的运动设计英雄区 |
| `sprite-animation` | desktop | marketing | 像素/复古 8-bit 动画解释幻灯片 |
| `dating-web` | desktop | personal | 消费者约会仪表盘模拟 |
| `digital-eguide` | desktop | marketing | 双页数字电子指南（封面 + 课程） |
| `wireframe-sketch` | desktop | design | 手绘风格构思草图 —— 用于"展示可视化方案的早期阶段" |

### 演示表面（deck 模式）

| 技能 | 默认用途 | 交付物 |
|------|----------|---------|
| `guizang-ppt` | deck 模式默认 | 杂志风格 Web PPT —— 来自 op7418/guizang-ppt-skill，完整保留原有 LICENSE |
| `simple-deck` | — | 最小水平滑动演示稿 |
| `replit-deck` | — | Replit 风格产品导览演示稿 |
| `weekly-update` | — | 团队周报节奏的滑动演示稿（进度 · 阻碍 · 下一步） |

### 办公与运营表面（prototype 模式）

| 技能 | 场景 | 交付物 |
|------|------|---------|
| `pm-spec` | product | PM 规范文档（含目录 + 决策日志） |
| `team-okrs` | product | OKR 评分表 |
| `meeting-notes` | operation | 会议决策记录 |
| `kanban-board` | operation | 看板快照 |
| `eng-runbook` | engineering | 故障处理手册 |
| `finance-report` | finance | 执行财务摘要 |
| `invoice` | finance | 单页发票 |
| `hr-onboarding` | hr | 角色入职计划 |

### 设计质量保障技能

| 技能 | 用途 |
|------|------|
| `critique` | 五维度专家设计评审 —— 哲学/视觉层级/细节/功能/创新，输出雷达图和 Keep/Fix/Quick-wins 行动清单 |
| `tweaks` | AI 生成的调整面板 —— 模型提出值得调整的参数 |

### 技能工作流示例：web-prototype

**触发关键词**：prototype, mockup, landing, single page, marketing page, homepage

**工作步骤：**
1. **Step 0**: 预读 `assets/template.html` 和 `references/layouts.md`
2. **Step 1**: 复制种子模板为 `index.html`，替换设计系统颜色变量
3. **Step 2**: 规划版块列表（营销页/定价/文档等节奏）
4. **Step 3**: 从 `layouts.md` 复制并填充版块
5. **Step 4**: 自检清单
6. **Step 5**: 输出 `<artifact>` 包裹的 HTML

**核心规则：**
- 单一强调色，每屏最多使用2次
- 显示字体用衬线体，正文用无衬线体
- 使用 `.ph-img` 图片占位符，不用外部 CDN
- 移动端响应式已通过种子模板的 920px 媒体查询实现
- 每个 `<section>` 需加 `data-od-id` 属性

### 技能工作流示例：guizang-ppt

**触发关键词**：ppt, deck, slides, presentation, magazine, 杂志, 杂志风 PPT

**视觉基调：**
- 电子杂志 + 电子墨水混血风格
- WebGL 流体/等高线/色散背景（hero 页）
- 衬线标题 + 非衬线正文 + 等宽元数据
- Lucide 线性图标（无 emoji）
- 水平左右翻页（键盘 ← →、滚轮、触屏滑动、底部圆点、ESC 索引）

**五套预设主题：**

| # | 主题 | 适合 |
|---|------|------|
| 1 | 墨水经典 | 通用 / 商业发布 / 不知道选哪个时的默认 |
| 2 | 靛蓝瓷 | 科技 / 研究 / 数据 / 技术发布会 |
| 3 | 森林墨 | 自然 / 可持续 / 文化 / 非虚构 |
| 4 | 牛皮纸 | 怀旧 / 人文 / 文学 / 独立杂志 |
| 5 | 沙丘 | 艺术 / 设计 / 创意 / 画廊 |

---

## 设计系统（Design Systems）详解

共 **72 套品牌级设计系统**，包括：

### 知名产品系统示例

| 品牌 | 风格特点 |
|------|----------|
| **Linear** | 极简冷静的工具类产品风格 |
| **Stripe** | 专业金融/支付平台的可靠感 |
| **Vercel** | 技术/开发者工具的现代感 |
| **Airbnb** | 温暖人性化的消费平台 |
| **Notion** | 简洁多功能的知识工具 |
| **Apple** | 极致简约的硬件品牌语言 |
| **Figma** | 设计工具的协作和创意感 |
| **Tesla** | 未来感科技品牌语言 |
| **Supabase** | 开发者友好的数据库工具 |
| **Anthropic** | 人工智能公司的端正感 |
| **Cursor** | AI 编码工具的现代感 |
| **Xiaohongshu (小红书)** | 中国本土社交电商风格 |

### 全部设计系统列表

```
airbnb, airtable, apple, binance, bmw, bugatti, cal, claude, clay, clickhouse,
cohere, coinbase, composio, cursor, default, elevenlabs, expo, ferrari, figma,
framer, hashicorp, ibm, intercom, kraken, lamborghini, linear-app, lovable,
mastercard, meta, minimax, mintlify, miro, mistral-ai, mongodb, nike, notion,
nvidia, ollama, opencode-ai, pinterest, playstation, posthog, raycast, renault,
replicate, resend, revolut, runwayml, sanity, sentry, shopify, spacex, spotify,
starbucks, stripe, supabase, superhuman, tesla, theverge, together-ai, uber,
vercel, vodafone, voltagent, warm-editorial, warp, webflow, wired, wise,
x-ai, xiaohongshu, zapier
```

*来源：通过 `scripts/sync-design-systems.ts` 从 VoltAgent/awesome-design-md 导入*

---

## 架构概览

```
┌─────────────────── browser (Next.js 16) ───────────────────┐
│  chat · file workspace · iframe preview · settings · imports     │
└─────────├──────────────────────────┤├─────────┘
           │ /api/* (rewritten in dev)          │
           ▼                                    ▼
 ┌───────────────────────────────────────┘   /api/proxy/stream (SSE)
 │  Local daemon (Express + SQLite) │   ──→ any OpenAI-compat
 │                                  │       endpoint (BYOK)
 │  /api/agents          /api/skills│       w/ SSRF blocking
 │  /api/design-systems  /api/projects/…
 │  /api/chat (SSE)      /api/proxy/stream (SSE)
 │  /api/templates       /api/import/claude-design
 │  /api/artifacts/save  /api/artifacts/lint
 │  /api/upload          /api/projects/:id/files…
 │  /artifacts (static)  /frames (static)
 │
 │  optional: sidecar IPC at /tmp/open-design/ipc/<ns>/<app>.sock
 │  (STATUS · EVAL · SCREENSHOT · CONSOLE · CLICK · SHUTDOWN)
 └────────┴────────────────────────────────┘
              │ spawn(cli, […], { cwd: .od/projects/<id> })
              ▼
 ┌───────────────────────────────────────────────────────┐
 │  claude · codex · gemini · opencode · cursor-agent · qwen        │
 │  copilot · hermes (ACP) · kimi (ACP) · pi (RPC) · kiro (ACP)      │
 │  reads SKILL.md + DESIGN.md, writes artifacts to disk            │
 └───────────────────────────────────────────────────────┘
```

### 层级技术栈

| 层级 | 技术栈 |
|------|--------|
| 前端 | Next.js 16 App Router + React 18 + TypeScript，可部署到 Vercel |
| 守护进程 | Node 24 · Express · SSE 流式传输 · better-sqlite3 |
| 数据表 | projects · conversations · messages · tabs · templates |
| Agent 传输 | child_process.spawn，按 CLI 类型使用不同流式格式 |
| BYOK 代理 | POST /api/proxy/stream → OpenAI-compatible /v1/chat/completions，SSE 透传 |
| 存储 | 普通文件在 .od/projects/<id>/ + SQLite 在 .od/app.sqlite |
| 预览 | srcdoc iframe + 按技能的 <artifact> 解析器 |
| 导出 | HTML (内联资源) · PDF (浏览器打印) · PPTX (技能驱动) · ZIP (归档) · Markdown |
| 生命周期 | `pnpm tools-dev start | stop | run | status | logs | inspect | check` |

### 支持的编码 Agent CLI

| Agent | 二进制 | 流格式 | 参数形态 |
|-------|--------|--------|----------|
| Claude Code | `claude` | claude-stream-json | `-p <prompt> --output-format stream-json` |
| Codex CLI | `codex` | json-event-stream | `exec --json --skip-git-repo-check --full-auto` |
| Gemini CLI | `gemini` | json-event-stream | `--output-format stream-json --skip-trust --yolo` |
| OpenCode | `opencode` | json-event-stream | `run --format json --dangerously-skip-permissions` |
| Cursor Agent | `cursor-agent` | json-event-stream | `--print --output-format stream-json` |
| Qwen Code | `qwen` | plain | `--yolo` |
| GitHub Copilot CLI | `copilot` | copilot-stream-json | `-p <prompt> --allow-all-tools --output-format json` |
| Hermes | `hermes` | acp-json-rpc | `acp --accept-hooks` |
| Kimi CLI | `kimi` | acp-json-rpc | `acp` |
| Kiro CLI | `kiro-cli` | acp-json-rpc | `acp` |
| Pi | `pi` | pi-rpc | `--mode rpc --no-session` |
| BYOK | n/a | SSE pass-through | POST /api/proxy/stream |

---

## 快速开始

### 安装依赖

- Node ~24
- pnpm 10.33.x

```bash
# 安装 Node 24（如果没有）
nvm install 24 && nvm use 24
# 或
fnm install 24 && fnm use 24
```

### 项目初始化

```bash
git clone https://github.com/nexu-io/open-design.git
cd open-design
corepack enable
corepack pnpm --version   # 应输出 10.33.2
pnpm install
pnpm tools-dev run web
# 打开输出的 Web URL
```

### 首次启动

1. 自动检测 PATH 上的 CLI 并选择一个
2. 加载 31 技能 + 72 设计系统
3. 弹出欢迎对话框，可粘贴 Anthropic key（仅用于 BYOK 回退路径）
4. 自动创建 `./.od/` —— 本地运行文件夹

### 运行时目录结构

```
.od/
├── app.sqlite                 ← 项目 · 对话 · 消息 · 打开的文件标签
├── artifacts/                 ← 一次性"保存到磁盘"渲染（带时间戳）
└── projects/<id>/             ← 按项目工作目录，也是 Agent 的 cwd
```

---

## 资源来源与血统

| 项目 | 本项目中的角色 |
|------|------------|
| Claude Design | 本项目是其开源替代品 |
| huashu-design (华书设计) | 设计哲学核心、初级设计师工作流、反 AI 垃圾清单、五维度自我评价 |
| guizang-ppt-skill (归藏 PPT 技能) | deck 模式默认技能，杂志风格 PPT |
| open-codesign (开放共创) | 第一个开源 Claude-Design 替代品，UX 模式来源 |
| multica-ai/multica | 守护进程 + 适配器架构 |
| awesome-design-md | 9 部分 DESIGN.md 模式和 69 产品系统 |

---

## 与竞品的对比

| 维度 | Claude Design (Anthropic) | Open CoDesign | Open Design |
|------|---------------------------|---------------|-------------|
| 许可证 | Closed | MIT | Apache-2.0 |
| 形态 | Web (claude.ai) | Desktop (Electron) | Web app + 本地守护进程 |
| 可部署到 Vercel | ❌ | ❌ | ✅ |
| Agent 运行时 | 内置 (Opus 4.7) | 内置 (pi-ai) | 委托给用户现有 CLI |
| 技能 | 专有 | 12 个自定义 TS 模块 | 31 个文件技能，可投放 |
| 设计系统 | 专有 | DESIGN.md (v0.2 路线图) | 72 个 DESIGN.md |
| 提供商灵活性 | 仅 Anthropic | 7+ 通过 pi-ai | 10 CLI 适配器 + BYOK 代理 |
| 初始问卷表单 | ❌ | ❌ | ✅ 强制规则，第一轮 |
| 视觉方向选择器 | ❌ | ❌ | ✅ 5 个确定性方向 |
| 实时待办进度 | ❌ | ✅ | ✅ |
| Claude Design ZIP 导入 | n/a | ❌ | ✅ 保持编辑连续性 |
| 5 维度自我评价 | ❌ | ❌ | ✅ 预发射门户 |
| 交付物 lint | ❌ | ❌ | ✅ POST /api/artifacts/lint |
| 导出格式 | 有限 | HTML/PDF/PPTX/ZIP/Markdown | 同左 |

---

## 路线图（Roadmap）

### 已完成
- [x] 守护进程 + Agent 检测（10 CLI 适配器）+ 技能注册表 + 设计系统目录
- [x] Web 应用 + 对话 + 问卷表单 + 5 方向选择器 + 待办进度 + 沙盒预览
- [x] 31 技能 + 72 设计系统 + 5 视觉方向 + 5 设备框架
- [x] SQLite 持久化（项目、对话、消息、标签、模板）
- [x] BYOK 代理（/api/proxy/stream）带 SSRF 防护
- [x] Claude Design ZIP 导入（/api/import/claude-design）
- [x] Sidecar 协议 + Electron 桌面自动化
- [x] 交付物 lint API + 5 维度自我评价门户

### 进行中 / 计划中
- [ ] 评论模式手术编辑（点击元素 → 指令 → 补丁）
- [ ] AI 生成的调整面板 UX（tweaks 技能已发布，面板本身待实现）
- [ ] Vercel + 隧道部署指南（拓扑 B）
- [ ] 技能市场（`od skills install <github-repo>`）
- [ ] 打包 Electron 构建

---

## 快速参考卡

```
┌─────────────────────────────────────────────────────┐
│  Open Design - 快速参考                          │
├─────────────────────────────────────────────────────┤
│                                                          │
│  安装                                                    │
│  ───────────────────────────────────────────────────────  │
│  git clone https://github.com/nexu-io/open-design.git     │
│  cd open-design && corepack enable                         │
│  pnpm install && pnpm tools-dev run web                    │
│                                                          │
│  快捷命令                                               │
│  ───────────────────────────────────────────────────────  │
│  pnpm tools-dev start      # 启动守护进程 + Web           │
│  pnpm tools-dev stop       # 停止所有服务               │
│  pnpm tools-dev status     # 查看状态                     │
│  pnpm tools-dev logs       # 查看日志                     │
│  pnpm tools-dev inspect    # 调试模式                     │
│  pnpm tools-dev check      # 健康检查                   │
│                                                          │
│  技能选择器                                             │
│  ───────────────────────────────────────────────────────  │
│  prototype 模式: web-prototype, saas-landing, mobile-app   │
│  deck 模式: guizang-ppt, simple-deck, weekly-update      │
│  质量保障: critique, tweaks                              │
│                                                          │
└─────────────────────────────────────────────────────┘
```

---

*来自翠冷翠*
