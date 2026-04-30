# OpenRouter Create Agent TUI 完整指南

> 来源：[OpenRouter X 帖子](https://x.com/openrouter/status/2047701992798392484)  
> 官方文档：[Build Your Own Agent TUI](https://openrouter.ai/docs/guides/coding-agents/create-agent-harness-tui)  
> 整理时间：2026-04-25  
> 来自翡冷翠

---

## 简介

**create-agent-tui** 是 OpenRouter 官方推出的 AI 编程助手 Skill，用于快速搭建具备终端界面（TUI）的 AI Agent。它类似于 `create-react-app`，但专为终端 Agent 设计 —— 只需告诉 AI 你想构建什么样的 Agent，它就会生成一个可运行的 TypeScript 项目，包含完整的终端界面、工具系统和配置。

底层基于 [`@openrouter/agent`](https://www.npmjs.com/package/@openrouter/agent) SDK，提供完整的 **Agent Harness**：内循环（模型调用、工具执行、停止条件）由 SDK 处理，外层（配置、工具定义、会话管理、入口点）由生成的项目提供。

---

## 什么时候应该构建自己的 Agent TUI

构建自定义 Agent TUI 在以下场景特别有价值：

| 场景 | 说明 |
|------|------|
| **需要自定义外观** | 想要为项目或团队创建一个独特的终端界面 |
| **需要自定义工具** | Agent 需要访问你的私有 API、数据库或特定领域系统 |
| **需要控制循环逻辑** | 需要自定义停止条件、审批流程、成本限制或模型选择逻辑 |
| **作为产品交付** | Agent 是你应用的一部分，你需要拥有入口点（CLI、API 服务器、嵌入式） |
| **学习目的** | 深入理解 Agent 在工具执行层面的工作原理 |

> 💡 **注意**：如果你已经在使用 Claude Code、Codex CLI 或 Cursor，通常不需要这个 —— 这些已经是生产级的 Agent TUI。这个 Skill 是为那些需要**构建自己的** Agent 的场景准备的。

---

## 快速开始

### 安装 Skill

**Claude Code:**
```bash
/plugin marketplace add OpenRouterTeam/skills
/plugin install openrouter@openrouter
```

**Skills CLI（适用于任何支持的 Agent）:**
```bash
npx skills add OpenRouterTeam/skills
```

### 使用 Skill

安装后，告诉你的 AI 编程助手：

> "build me an agent TUI"  
> "scaffold a coding assistant"

Skill 会自动激活，通过交互式清单引导你选择需要的功能。

### 运行生成的项目

```bash
cd my-agent
export OPENROUTER_API_KEY="your-api-key"
npm start
```

### 启动时自定义

```bash
npm start -- --banner "Acme Bot" --model anthropic/claude-sonnet-4 --input bordered --tool-display emoji
```

---

## 视觉定制选项

每个终端界面元素都可以定制，支持通过 CLI 参数或配置文件覆盖。

### 1. 工具显示样式（Tool Display）

设置 `display.toolDisplay` 或传递 `--tool-display`：

| 样式 | 描述 |
|------|------|
| **`grouped`** (默认) | 粗体动作标签 + 树形分支输出，连续同类调用合并 |
| **`emoji`** | 每次调用带标记，显示工具名、参数和耗时 |
| **`minimal`** | 聚合单行摘要，文本恢复时刷新 |
| **`hidden`** | 完全隐藏工具输出 |
| **Custom** | 描述你想要的效果，Skill 会实现自定义显示 |

### 2. 输入样式（Input Style）

设置 `display.inputStyle` 或传递 `--input`：

| 样式 | 描述 |
|------|------|
| **`block`** (默认) | 全宽背景色输入框 + `›` 提示符 —— 通过 OSC 11 检测终端背景色自适应 |
| **`bordered`** | 水平 `─` 线框 —— 适用于任何终端 |
| **`plain`** | 简单 `>` readline 提示符 —— 无原始模式，无转义序列 |
| **Custom** | 描述你想要的效果，Skill 会实现自定义样式 |

**`block` 样式的特点**：
- 自动检测终端背景色（深色/浅色）
- 深色主题：白色叠加 12% 透明度
- 浅色主题：黑色叠加 4% 透明度
- 完美适配任何配色方案

### 3. 加载动画（Loader）

设置 `display.loader.style` 和 `display.loader.text`：

| 样式 | 描述 |
|------|------|
| **`spinner`** (默认) | 盲文点动画（⠋⠙⠹…）在文本左侧 |
| **`gradient`** | 滚动色彩闪烁覆盖加载文本 |
| **`minimal`** | 尾部点 (`Working···`) |
| **Custom** | 描述你想要的效果，Skill 会实现自定义动画 |

### 4. ASCII Banner

启用 `showBanner` 或传递 `--banner "Your Agent Name"` 在启动时显示自定义 ASCII 艺术 Logo。

- 使用 `█` 字符生成项目名的块状字母艺术
- 彩色显示，适配 60 列终端
- 纯文本回退：边框框内显示 Agent 名和模型

---

## 功能定制清单

Skill 以交互式清单形式呈现可选功能，你可以勾选需要的模块。

### Server Tools（OpenRouter 服务端执行，零客户端代码）

| 工具 | 默认 | 功能 |
|------|------|------|
| Web Search | ✅ on | 实时网页搜索 `openrouter:web_search` |
| Datetime | ✅ on | 当前日期/时间 `openrouter:datetime` |
| Image Generation | ❌ off | 图片生成 `openrouter:image_generation` |

### User-Defined Tools（本地执行，生成到 `src/tools/`）

| 工具 | 默认 | 功能 |
|------|------|------|
| File Read | ✅ on | 读取文件，支持偏移/限制，图片检测 |
| File Write | ✅ on | 创建/覆盖文件，自动创建目录 |
| File Edit | ✅ on | 搜索替换，带 diff 输出 |
| Glob/Find | ✅ on | glob 模式查找文件 |
| Grep/Search | ✅ on | 正则搜索文件内容 |
| Directory List | ✅ on | 列出目录条目 |
| Shell/Bash | ✅ on | 执行命令，带超时 |
| JS REPL | ❌ off | 持久化 Node.js 环境 |
| Sub-agent Spawn | ❌ off | 委派任务给子 Agent |
| Plan/Todo | ❌ off | 多步骤任务进度追踪 |
| Request User Input | ❌ off | 结构化用户提问 |
| Web Fetch | ❌ off | 获取并提取网页文本 |
| View Image | ❌ off | base64 读取本地图片 |
| Custom Tool Template | ✅ on | 领域特定工具的空白骨架 |

### Harness Modules（架构组件）

| 模块 | 默认 | 功能 |
|------|------|------|
| Session Persistence | ✅ on | JSONL 追加式会话日志 |
| ASCII Logo Banner | ❌ off | 启动时自定义 ASCII 艺术横幅 |
| Context Compaction | ❌ off | 上下文过长时总结旧消息 |
| System Prompt Composition | ❌ off | 从静态+动态上下文文件构建指令 |
| Tool Permissions / Approval | ❌ off | 危险工具需用户确认 |
| Structured Event Logging | ❌ off | 发射工具调用/API请求/错误事件 |
| `@`-file References | ❌ off | `@filename` 附加文件到下一次消息 |
| `!` Shell Shortcut | ❌ off | `!command` 运行 shell 并注入输出 |
| Multi-line Input | ❌ off | Shift+Enter 多行输入 |

### Slash Commands（用户 REPL 命令）

| 命令 | 默认 | 功能 |
|------|------|------|
| `/model` | ✅ on | 通过 OpenRouter API 切换模型 |
| `/new` | ✅ on | 开始新对话 |
| `/help` | ✅ on | 列出可用命令 |
| `/compact` | ❌ off | 手动触发上下文压缩 |
| `/session` | ❌ off | 显示会话元数据和 token 使用 |
| `/export` | ❌ off | 保存对话为 Markdown |

---

## `@openrouter/agent` SDK 能力

生成的项目不重新实现 Agent 循环 —— 这一切由 SDK 处理：

| 能力 | 说明 |
|------|------|
| **Model calls** | `client.callModel()` —— 一次调用，OpenRouter 上任何模型 |
| **Tool execution** | 自动执行 —— 用 `tool()` 和 Zod schema 定义工具，SDK 验证输入并调用你的 `execute` 函数 |
| **Multi-turn** | 自动循环 —— SDK 循环（调用模型 → 执行工具 → 调用模型）直到停止条件触发 |
| **Stop conditions** | `stepCountIs(n)`、`maxCost(amount)`、`hasToolCall(name)`、或自定义函数 |
| **Streaming** | `result.getTextStream()` 获取文本增量，`result.getToolCallsStream()` 获取工具调用 |
| **Cost tracking** | `result.getResponse().usage` 包含输入/输出 token 计数 |
| **Shared context** | 通过 `sharedContextSchema` 实现工具间类型安全的共享状态 |

你构建的 TUI 提供循环外围的一切：配置、工具定义、会话持久化、入口点（CLI 或 API 服务器），以及你从清单中选择的任何模块。

---

## 生成的项目结构

默认选项下，生成的 TUI 项目结构如下：

```
my-agent/
├── package.json              # @openrouter/agent, zod, tsx
├── tsconfig.json             # ES2022, Node16, strict
├── .env.example              # OPENROUTER_API_KEY=***
└── src/
    ├── config.ts             # 分层配置（默认值 -> 文件 -> 环境变量）
    ├── agent.ts              # 核心运行器（带重试）
    ├── cli.ts                # 交互式 REPL
    ├── session.ts            # JSONL 对话持久化
    ├── terminal-bg.ts        # 自适应背景检测
    ├── renderer.ts           # 工具显示渲染器
    └── tools/
        ├── index.ts          # 工具注册表 + server tools
        ├── file-read.ts      # 读取文件
        ├── file-write.ts     # 写入文件
        ├── file-edit.ts      # 搜索替换 + diff
        ├── glob.ts           # glob 查找
        ├── grep.ts           # 正则搜索
        ├── list-dir.ts       # 列出目录
        └── shell.ts          # 执行命令
```

---

## 入口点选项

Skill 默认生成 CLI REPL，但你也可以请求：

- **HTTP API Server** —— Express/Hono 服务器 + SSE 流，用于构建 Web 可访问的 Agent
- **Both** —— CLI 用于开发，Server 用于生产

---

## 相关资源

### 官方链接

| 资源 | 链接 |
|------|------|
| X 原帖 | https://x.com/openrouter/status/2047701992798392484 |
| 完整文档 | https://openrouter.ai/docs/guides/coding-agents/create-agent-harness-tui |
| Agent SDK 文档 | https://openrouter.ai/docs/agent-sdk/overview |
| Skill GitHub | https://github.com/OpenRouterTeam/skills/tree/main/skills/create-agent-tui |
| Sample 项目 | https://github.com/OpenRouterTeam/skills/tree/main/skills/create-agent-tui/sample |
| npm 包 | https://www.npmjs.com/package/@openrouter/agent |
| OpenRouter SDK | https://www.npmjs.com/package/@openrouter/sdk |
| Agent SDK 迁移指南 | https://openrouter.ai/docs/sdks/agent-migration |

### 其他 OpenRouter Skills

OpenRouter 还提供了其他有用的 Skills：

| Skill | 用途 |
|-------|------|
| `openrouter-agent-migration` | 从旧版 SDK 迁移到 `@openrouter/agent` |
| `openrouter-images` | 图片生成与处理 |
| `openrouter-models` | 模型查询与选择 |
| `openrouter-oauth` | OAuth 认证流程 |
| `openrouter-typescript-sdk` | TypeScript SDK 使用指南 |

---

## 示例：完整的 Agent TUI 启动

```typescript
// 带工具的多轮 Agent
import { OpenRouter, tool, stepCountIs } from '@openrouter/agent';
import { z } from 'zod';

const openrouter = new OpenRouter();

const searchTool = tool({
  name: 'search',
  description: 'Search the web for information',
  inputSchema: z.object({
    query: z.string(),
  }),
  execute: async ({ query }) => {
    return { results: ['Result 1', 'Result 2'] };
  },
});

const result = openrouter.callModel({
  model: 'anthropic/claude-sonnet-4',
  input: 'Research the latest advances in fusion energy.',
  tools: [searchTool],
  stopWhen: stepCountIs(5),
});

// 流式输出
for await (const delta of result.getTextStream()) {
  process.stdout.write(delta);
}
```

---

## 最佳实践建议

1. **从默认配置开始** —— 先用默认设置生成项目，熟悉后再逐步定制
2. **选择合适的工具** —— 不需要的 Server Tools 可以关闭，避免 API 调用浪费
3. **测试多种视觉风格** —— 用 `--input` 和 `--tool-display` 参数快速试验不同风格
4. **使用 TypeScript 严格模式** —— 生成的项目已配置严格类型检查，充分利用它
5. **参考 Sample 项目** —— `sample/` 目录包含完整工作示例，可作为起点
6. **阅读 Reference 文档** —— Skill 的 `references/` 目录包含详细的实现参考

---

*来自翡冷翠*
