# Open Slide - 为 AI Agent 打造的幻灯片框架

> 来源：[Yiwei Ho @1weiho](https://x.com/1weiho/status/2050602481953181968)  
> GitHub: [1weiho/open-slide](https://github.com/1weiho/open-slide)  
> 官网: [open-slide.dev](https://open-slide.dev/)  
> 整理时间：2026-05-03  
> 来自翡冷翠

---

## 简介

**Open Slide** 是一个专为 AI Agent 设计的幻灯片框架。它让开发者能够用自然语言描述演示文稿，由编码 Agent（如 Claude Code、Codex、Cursor）生成 React 代码，最终输出精美的幻灯片。

**核心理念**：幻灯片是可视化代码，而 Agent 擅长写代码。Open Slide 填补了"帮我做一套关于 X 的幻灯片"与"可展示的成品"之间的空白——全程无需离开聊天窗口。

---

## 快速开始

```bash
# 初始化项目
npx @open-slide/cli init my-slide

# 进入项目目录
cd my-slide

# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev
```

---

## 核心特性

### 🤖 Agent 原生创作

与任何编码 Agent（Claude Code、Codex、Cursor 等）无缝协作。脚手架预置了 Agent Skills：

| Skill | 功能 |
|-------|------|
| `/create-slide` | 端到端起草幻灯片。询问 4 个范围问题（主题与风格、页数、文字密度、动态 vs 静态），选择 ID，规划结构，编写页面 |
| `/slide-authoring` | 技术参考文档，涵盖 1920×1080 画布、字体比例、配色和布局规则。Agent 编写前先读取 |

**从一句话提示到精美幻灯片，零样板代码。**

### 🎯 浏览器内检查器

在开发服务器中点击任意元素并添加评论——*"把这个变红"*、*"改成'Open Slide Rocks'"*、*"缩小标题"*。评论会以 `@slide-comment` 标记形式保存在源码中。运行 `/apply-comments`，Agent 会应用所有待处理的编辑并清除标记。

**工作流程**：展示 → 点击评论 → `/apply-comments` → 重复。

### 🖼️ 资源管理器 + SVGL Logo 搜索

通过内置的资源面板管理每套幻灯片的图片、视频和字体。通过集成的 [svgl](https://svgl.app/) 目录搜索并拖入任意品牌 Logo——无需再四处寻找 SVG。

### 🎬 专业演讲模式

全屏播放配合键盘导航，外加**演讲者模式**——当前/下一张预览、演讲者备注和计时器。为舞台而生，不只是浏览器标签页。

### 📦 导出为静态 HTML 与 PDF

一条命令将幻灯片导出为自包含的静态 HTML 站点或打印就绪的 PDF。无需服务器即可分享。

### 📁 幻灯片管理器

用自定义表情符号将幻灯片组织到文件夹中，拖拽重新排序。当你制作了超过三套幻灯片并需要查找时非常有用。

### 🚀 部署友好

输出纯静态构建——一键部署到 Vercel、Cloudflare Pages、Zeabur、Netlify 或任何静态托管服务。无服务器、无运行时、无锁定。

---

## 技术规格

- **画布尺寸**：固定 1920 × 1080
- **页面类型**：任意 React 组件（不是受限的 DSL）
- **技术栈**：React + TypeScript + Vite
- **依赖**：`@open-slide/core`（运行时、Vite 插件、CLI）
- **配置**：`open-slide.config.ts`（TypeScript 类型化配置）

---

## 项目结构

```
my-slide/
├── slides/
│   └── getting-started/          # 幻灯片目录（可编辑或删除）
│       └── index.tsx              # 默认导出 Page 组件数组
├── package.json                   # 依赖 @open-slide/core
├── open-slide.config.ts          # 可选类型化配置（slidesDir, port）
├── .claude/skills/               # Claude Code Skills
├── .agents/skills/              # 其他 Agent Skills
└── CLAUDE.md                    # Agent 幻灯片编写指南
```

**注意**：工作区中看不到 Vite、React 或 tsconfig 文件——它们隐藏在 `@open-slide/core` 内部，你永远不需要触碰它们。

---

## 可用命令

### @open-slide/cli（脚手架）

| 命令 | 说明 |
|------|------|
| `open-slide init [dir]` | 在 `dir` 目录（默认为当前目录）中搭建新工作区 |
| `open-slide init --force` | 在非空目录中搭建 |
| `open-slide init --name <name>` | 覆盖生成的 package.json 名称 |

### @open-slide/core（工作区内）

| 命令 | 说明 |
|------|------|
| `open-slide dev` | 启动开发服务器 |
| `open-slide build` | 构建生产版本 |
| `open-slide preview` | 预览生产构建 |

---

## 代码仓库布局

此仓库使用 pnpm + Turbo 管理的 monorepo 结构：

| 路径 | 说明 |
|------|------|
| `packages/core` | `@open-slide/core` —— 运行时（首页、幻灯片查看器、演讲模式、检查器）、Vite 插件、`open-slide` CLI |
| `packages/cli` | `@open-slide/cli` —— `npx @open-slide/cli init` 脚手架。生成最小工作区，Vite/React/tsconfig 隐藏在 core 内部 |
| `apps/demo` | 示例工作区，通过 `workspace:*` 消费 `@open-slide/core`。用于框架本地开发 |

---

## 相关资源

### 官方链接
| 名称 | 链接 | 说明 |
|------|------|------|
| GitHub 仓库 | https://github.com/1weiho/open-slide | 源码与文档 |
| 官方网站 | https://open-slide.dev/ | 项目官网 |
| npm 包 | https://www.npmjs.com/package/@open-slide/cli | CLI 脚手架包 |
| CLAUDE.md | https://github.com/1weiho/open-slide/blob/main/CLAUDE.md | Agent 编写规则 |

### 集成服务
- **SVGL** (https://svgl.app/) - Logo SVG 搜索目录

---

## 值得关注

- **@1weiho (Yiwei Ho)** - 项目作者，专注于 AI 工具与开发者体验设计

---

## 许可协议

MIT License

---

*来自翡冷翠*
