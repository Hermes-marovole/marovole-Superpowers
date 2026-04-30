# Beads - AI Agent 记忆系统升级方案

> 来源：[向阳乔木 @vista8](https://x.com/vista8/status/2049651974317191464)
> 整理时间：2026-04-30
> 来自翡冷翠

---

## 简介

Beads 是一个为 AI 编程 Agent 设计的分布式图状任务追踪系统，GitHub 已获得 **22.6k+ Stars**。它用结构化的数据库替代了传统的 Markdown 任务清单，解决了 AI Agent 在处理长任务时的「失忆」问题。

**核心洞察**：当任务一多、上下文窗口一满，Markdown 作为纯文本记忆的方式会导致信息丢失。Beads 的思路是——好好做「任务管理」。

---

## 为什么需要 Beads

### 传统 Markdown 的局限

现在的 AI Agent 普遍依赖 Markdown 做任务记忆，但 Markdown 存在结构性缺陷：

| 问题 | 影响 |
|------|------|
| **纯文本无结构** | 无法表达任务间的依赖关系 |
| **无状态追踪** | 任务完成状态容易被覆盖或丢失 |
| **无版本控制** | 多 Agent 协作时产生冲突 |
| **上下文溢出** | 任务堆积后，重要信息被截断 |

### Beads 的解决方案

**用数据库思维做任务管理**：

底层采用 **Dolt** —— 一个「像 Git 一样」的 SQL 数据库，支持：
- ✅ 分支管理
- ✅ 合并操作
- ✅ 版本回溯
- ✅ 单元格级别的 merge

---

## 核心技术架构

### Dolt 数据库优势

| 特性 | 说明 |
|------|------|
| **哈希 ID** | 任务 ID 如 `bd-a1b2`，避免多 Agent 并发写入冲突 |
| **版本回溯** | 任务历史完整保留，不会凭空消失 |
| **远程同步** | 支持团队协作和多机器使用 |
| **脱离 Git** | Beads 可完全独立运行，不依赖 Git |

### 上下文压缩设计

**语义记忆衰减（Semantic Memory Decay）**：
- 自动将已关闭任务压缩为摘要
- 节省上下文窗口空间
- 保留关键信息，去除冗余细节

---

## 核心功能特性

### 🛠 主要能力

- **Dolt-Powered**: 版本控制的 SQL 数据库，支持 cell-level merge
- **Agent 优化**: JSON 输出、依赖追踪、自动就绪任务检测
- **零冲突**: 基于哈希的 ID 系统，多 Agent/多分支工作流无碰撞
- **任务压缩**: 语义记忆衰减，智能总结旧任务
- **消息线程**: 支持消息类型的 issue 和线程回复
- **图链接**: `relates_to`、`duplicates`、`supersedes`、`replies_to` 构建知识图谱

### 📖 常用命令

| 命令 | 功能 |
|------|------|
| `bd ready` | 列出无阻塞的任务 |
| `bd create "Title" -p 0` | 创建 P0 优先级任务 |
| `bd update <id> --claim` | 原子化认领任务 |
| `bd dep add <child> <parent>` | 建立任务依赖关系 |
| `bd show <id>` | 查看任务详情和审计日志 |

### 🔗 层级工作流

支持分层任务 ID 管理史诗级项目：

```
bd-a3f8      → Epic（史诗）
bd-a3f8.1    → Task（任务）
bd-a3f8.1.1  → Sub-task（子任务）
```

### 🕵️ 隐身模式

```bash
bd init --stealth
```

- 在本地使用 Beads 而不提交到主仓库
- 适合个人在共享项目上的私密使用
- 完全 Git-Free 运行

---

## 适用场景

### 官方定位

项目官方说明主要面向 **AI 编程 Agent** 使用。

### 实际适用范围

任何需要在 **多个 AI 会话之间保持任务连续性** 的场景：

| 场景 | 价值 |
|------|------|
| **长项目开发** | 跨会话保持任务上下文，无需重复交代背景 |
| **多 Agent 协作** | 避免任务冲突，自动合并并行工作 |
| **复杂任务拆解** | 可视化依赖关系，追踪任务进度 |
| **团队项目同步** | 远程数据库同步，多人共享任务状态 |

---

## 安装与使用

### ⚡ 快速安装

```bash
# 一键安装（推荐）
curl -fsSL https://raw.githubusercontent.com/gastownhall/beads/main/scripts/install.sh | bash

# macOS / Linux 用户
brew install beads

# Node.js 用户
npm install -g @beads/bd
```

### 初始化项目

```bash
# 进入你的项目目录
cd your-project

# 初始化 Beads
bd init

# 告诉你的 Agent 使用 Beads
echo "Use 'bd' for task tracking" >> AGENTS.md
```

**注意**：Beads 是系统级 CLI 工具，只需安装一次，到处可用。不需要将 beads 仓库克隆到你的项目中。

### 存储模式

| 模式 | 命令 | 适用场景 |
|------|------|----------|
| **Embedded**（默认） | `bd init` | 单用户，推荐大多数人使用 |
| **Server** | `bd init --server` | 多并发写入，团队协作 |

---

## 资源汇总

### 官方链接

| 资源 | 链接 | 说明 |
|------|------|------|
| GitHub 仓库 | https://github.com/steveyegge/beads | 主仓库（22.6k+ Stars） |
| 官方文档 | https://gastownhall.github.io/beads/ | 完整文档站点 |
| PyPI 包 | https://pypi.org/project/beads-mcp/ | Python MCP 集成 |
| npm 包 | https://www.npmjs.com/package/@beads/bd | Node.js 版本 |

### 相关工具

- **Dolt**: https://github.com/dolthub/dolt — Beads 底层数据库
- **Steve Yegge**: 项目作者，知名技术博主

### 社区资源

- [VirtusLab 深度分析](https://virtuslab.com/blog/ai/beads-give-ai-memory/)
- [Hacker News 讨论](https://news.ycombinator.com/item?id=46075616)

---

## 快速参考

### 典型工作流

```bash
# 1. 初始化
bd init

# 2. 创建史诗任务
bd create "重构用户系统" -p 0

# 3. 创建子任务并建立依赖
bd create "设计新的数据库 schema" -p 1
bd dep add bd-xxxxx bd-yyyyy

# 4. 查看就绪任务
bd ready --json

# 5. 认领并完成任务
bd update bd-xxxxx --claim
bd close bd-xxxxx "已完成 schema 设计"
```

### 环境变量配置

| 变量 | 用途 |
|------|------|
| `BEADS_DIR` | 自定义 `.beads/` 目录位置 |
| `BEADS_DOLT_SERVER_HOST` | Dolt 服务器地址 |
| `BEADS_DOLT_SERVER_PORT` | Dolt 服务器端口 |

---

## 核心洞察

> "Beads 不是给人类用的待办清单，而是为机器设计的分布式、Git 支持的任务数据库（issue tracker）。"

**关键启示**：

1. **Markdown 已经不够用** —— 当 AI Agent 开始处理复杂项目时，我们需要结构化的数据存储
2. **Git 是更好的数据库** —— 对于异步工作的团队和 Agent，Git 的分支/合并模型比传统 SQL 更适合协作
3. **哈希 ID 解决并发冲突** —— 类似于 Git commit hash，随机生成的任务 ID 天然避免写入冲突
4. **语义压缩节省上下文** —— 自动总结旧任务，让 Agent 专注于当前工作

---

*来自翡冷翠*
