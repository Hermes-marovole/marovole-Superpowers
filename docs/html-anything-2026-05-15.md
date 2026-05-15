# html-anything：让 Agent 将任意数据转为世界级设计 HTML

> 来源：[@tuturetom](https://x.com/tuturetom) (Tom Huang, Co-founder & CEO @nexudotio) · GitHub: [nexu-io/html-anything](https://github.com/nexu-io/html-anything) · 整理日期：2026-05-15

---

## 执行摘要

Tom Huang（@tuturetom，Nexu 联合创始人）正式开源了 **html-anything**——一个专注于 Agent 时代的 HTML 编辑器。历时 3 天、1.5 万行代码，支持 75 套 Skill 模板、9 种导出格式，兼容 Claude Code、Codex、OpenClaw、Hermes 等 8 种主流代码 Agent CLI。

核心主张：**Markdown 是草稿，HTML 才是给人类看的最终形态**。在 Agent 时代，用户不再手工编辑文档，输出格式应该直接是读者想要的 HTML。

---

## 核心亮点

### 1. 8 种代码 Agent CLI 自动检测

启动时自动扫描 `PATH`（包括 GUI 启动 Node 常遗漏的目录如 `~/.local/bin`、`/opt/homebrew/bin` 等），识别并复用你已登录的会话：

| Agent | 检测命令 | 调用方式 |
|---|---|---|
| Claude Code | `claude` | `claude -p --output-format stream-json` |
| OpenAI Codex | `codex` | `codex exec --json --sandbox workspace-write` |
| Cursor Agent | `cursor-agent` | `cursor-agent --print --output-format stream-json` |
| Gemini CLI | `gemini` | `gemini --output-format stream-json --yolo` |
| GitHub Copilot CLI | `copilot` | `copilot --allow-all-tools --output-format json` |
| OpenCode | `opencode-cli` / `opencode` | `opencode run --format json` |
| Qwen Coder | `qwen` | `qwen --yolo` |
| Aider | `aider` | `aider --no-pretty --no-stream --yes-always` |

**零 API Key 成本**——复用你已有的订阅（Claude / Cursor / Codex / Gemini 等），边际成本为 $0。

### 2. 75 套 Skill 模板 × 9 种交付面

按 `mode`（原型/演示/帧/社交/办公/文档）× `scenario`（设计/营销/工程/产品/财务/HR/运营/个人）组织：

- **原型**（20+）：SaaS 落地页、定价页、Dashboard、文档站、博客、移动端原型、游戏化应用、约会匹配面板等
- **演示**（20）：瑞士国际风格、归藏墨韵编辑风、Open Slide 画布、小红书 pastel、Hermes Cyber、Replit 风等
- **视频帧/VFX/设备 mockup**（12）：流体英雄背景、NYT 数据图表、便利贴流程图、故障艺术标题、电影光晕、macOS 通知、品牌 Logo 收尾、文字光标 VFX、3D 设备框等
- **社交卡片**（8）：X/Twitter 引用卡、Spotify Wrapped 风、Reddit 串、小红书图文卡、Twitter 摘录卡、3 图轮播等
- **办公/文档**（14）：PM 需求文档、团队 OKR、会议记录、周报、看板、工程运维手册、财务报告、发票、HR 入职计划、数据报告、实时 Dashboard 等

### 3. 一键导出到主流平台

| 平台 | 技术方案 | 粘贴效果 |
|---|---|---|
| 微信公众号 | `juice` 内联 CSS + `data-tool` 标记 | 零二次排版 |
| 知乎 | 同上 + `<mjx-container>` → `data-eeimg` | 公式自动渲染 |
| X / 微博 / 小红书 | `modern-screenshot` 渲染 2× PNG → `ClipboardItem` | 直接拖入编辑器 |
| 下载 `.html` | 单文件内联资源 | 任意浏览器打开 |
| 下载 `.png` | 高 DPI 截图 | 任意平台分享 |

### 4. SSE 流式渲染

`POST /api/convert` 通过 SSE 流式返回。Agent 的标准输出按 JSON 行解析为文本增量 → 客户端实时追加到 iframe `srcdoc`。你可以**像看 Agent 在终端打字一样看 HTML 被逐行渲染出来**，随时中断并重提示，不浪费完整生成。

### 5. 沙箱隔离预览

`<iframe sandbox="allow-scripts allow-same-origin">`。第三方脚本（Tailwind CDN、Google Fonts、自定义动画）正常运行，但 Cookie 和 localStorage 与宿主页面隔离。

---

## 发布者洞察（来自 @tuturetom）

- **动机**：Anthropic Claude Code 团队宣布内部文档不再用 Markdown，改 ship HTML。他们的逻辑是——Markdown 适合写的人，HTML 适合看的人；Markdown 截图到推文里很丑，HTML 本身就是设计好的图像；Markdown 需要为微信/知乎/Newsletter 重排，HTML 一键转换。
- **立场**："我们不 ship 一个 Agent，你的 Agent 已经足够好。" 只做 Agent 编排层 + 设计系统 + Skill 协议，让用户的本地 Agent 直接产出 ship-ready 的 HTML。
- **速度**：3 天、1.5 万行代码、75 套 Skills、9 种导出格式——来自 Open Design 原班人马（40k★、200+ 贡献者）。

---

## 技术栈速览

| 层级 | 技术 |
|---|---|
| 前端 | Next.js 16 App Router + Turbopack · React 19 · Tailwind v4 · zustand |
| 服务端 | `GET /api/agents`（检测）· `POST /api/convert`（SSE 流式 spawn） |
| Agent 传输 | `child_process.spawn` · 每 CLI 一个 stdin/stdout 适配器 |
| 浏览器处理 | `juice`（CSS 内联）· `modern-screenshot`（PNG 导出）· `xlsx`/`papaparse`（表格解析）· `marked` + `highlight.js`（Markdown 兼容）· `dompurify`（XSS 防御） |
| 预览沙箱 | `iframe[sandbox]` + `srcdoc` |
| 部署 | 本地 `pnpm dev` · Vercel 一键部署（Web 层，Agent 始终本地） |

---

## 快速启动

```bash
git clone https://github.com/nexu-io/html-anything
cd html-anything
pnpm install
pnpm dev
# → http://localhost:3000
```

打开浏览器 → 顶部栏自动检测你已登录的代码 Agent CLI → 选择模板 → 粘贴内容 → ⌘+Enter。

---

## 六大设计支柱

1. **不造 Agent，复用你的**：检测 PATH 上 8 种 CLI，复用现有登录会话，零额外 API Key。
2. **Skills 是文件夹，不是插件**：遵循 Claude Code `SKILL.md` 约定（`SKILL.md` + `assets/` + `references/` + `example.html`），复制一个邻接模板、修改 frontmatter、重启 `pnpm dev` 即可在 picker 中显示。
3. **硬约束防 freestyle**：每模板硬性规定——CJK 优先字体栈（Noto Sans/Serif SC）、8px 基准网格、圆角·柔和阴影·无纯黑纯白、对比度 ≥ 4.5、必须使用真实数据（禁用 lorem ipsum）。
4. **流式渲染 = 看 AI 画画**：SSE 实时追加 iframe，随时中断。
5. **一键导出 = 零二次排版**：微信/X/知乎/HTML/PNG 全覆盖。
6. **沙箱 iframe = 安全隔离**：用户生成的 HTML 在独立 origin 运行。

---

## 生态谱系

| 上游项目 | 在本仓库中的角色 |
|---|---|
| `nexu-io/open-design`（40k★） | Agent 检测层、`DESIGN.md` 设计系统 schema、`SKILL.md` 协议 |
| `multica-ai/multica` | Daemon 架构：一个特权进程 spawn CLI，JSON-line 作为 wire protocol |
| `alchaincyf/huashu-design` | 反 AI-slop 纪律——Junior-Designer 模式、5 步品牌资产协议、硬约束 |
| `mdnice/markdown-nice` | `juice` 内联 CSS → 微信/知乎零重排粘贴 |
| `gcui-art/markdown-to-image` | iframe → 高 DPI PNG 导出路径 |
| `op7418/guizang-ppt-skill` | 归藏墨韵编辑演示风（保留原 LICENSE 和作者） |
| `tw93/kami` | 暖色羊皮纸编辑文档风 |
| `1weiho/open-slide` | 1920×1080 Agent 原生画布 |
| `heygen-com/hyperframes` + `remotion-dev/remotion` | 视频帧脚本规范 + 渲染器 |

---

## Roadmap 状态

| 功能 | 状态 |
|---|---|
| Agent 检测（8 CLI） | ✅ 稳定 |
| Skill 注册 + Picker（75 Skills） | ✅ 稳定 |
| SSE 流式渲染 | ✅ 稳定 |
| 沙箱 iframe 预览 | ✅ 稳定 |
| 一键导出（微信/X/知乎/HTML/PNG） | ✅ 稳定 |
| CSV/Excel/JSON/SQL 格式自动检测 | ✅ 稳定 |
| 多模板对比（生成 4 选 1） | 🛠 进行中 |
| Hyperframes → `.mp4` 一键交接 | 🛠 进行中 |
| 浏览器插件（选中任意页面 → 转换） | ⏳ 计划中 |
| 历史 / 版本对比 / IndexedDB 归档 | ⏳ 计划中 |
| Skill 市场（`install <github-repo>`） | ⏳ 计划中 |

---

## 为什么值得关注

对中文 AI Agent 生态而言，html-anything 的价值不仅在于"把 Markdown 变成好看的 HTML"，而在于它提出了一个 Agent 时代内容交付的新范式：

- **Agent 写完即交付**：不再是 Markdown 草稿 → 设计师排版 → 运营发布的传统流程，而是 Agent 直接产出 ship-ready 的 HTML。
- **本地优先 + 零边际成本**：复用已有的 CLI 登录态，无需额外 API Key，对个人开发者和团队极其友好。
- **中文内容场景全覆盖**：微信、知乎、小红书、Twitter 的一键导出，解决了中文创作者跨平台分发的最大痛点。
- **开放 Skill 体系**：75 套模板 + 易于扩展的 `SKILL.md` 协议，意味着社区可以持续贡献设计系统，形成正向飞轮。

---

## 属性声明

来自翡冷翠
