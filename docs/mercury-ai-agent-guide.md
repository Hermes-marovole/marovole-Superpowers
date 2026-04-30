# Mercury - 权限加固的多通道 AI Agent 框架

> Soul-driven. Token-efficient. Always on.

**来源：** [X 用户 @Ctrl_Alt_Zaid 深度评测](https://x.com/Ctrl_Alt_Zaid/status/2046902326657749114) ｜ [官网](https://mercury.cosmicstack.org/) ｜ [GitHub 仓库](https://github.com/cosmicstack-labs/mercury-agent)

---

## 目录

1. [核心概述](#核心概述)
2. [解决的问题](#解决的问题)
3. [四大核心特性](#四大核心特性)
4. [31 个内置工具详解](#31-个内置工具详解)
5. [快速开始](#快速开始)
6. [竞品对比](#竞品对比)
7. [相关资源](#相关资源)
8. [学习路径](#学习路径)

---

## 核心概述

**Mercury** 是由 **Cosmic Stack** 开发的个人 AI Agent 框架，主打「权限加固 + Token 预算控制 + Soul 驱动身份系统」，支持 CLI 和 Telegram 双通道，可 24/7 后台运行。

### 为什么值得关注

| 特性 | 说明 |
|------|------|
| 🛡️ **权限加固** | 文件夹级读写范围控制 + 危险命令硬阻断（sudo、rm -rf 等永不执行） |
| 💰 **Token 预算** | 每日预算限制 + 70% 阈值自动触发精简模式 |
| 🧠 **Soul 系统** | 4 个 Markdown 文件定义 Agent 身份（soul/persona/taste/heartbeat） |
| ♾️ **永远在线** | 后台 Daemon 模式，开机自启，崩溃自恢复 |
| 📡 **多通道** | CLI + Telegram，未来支持 Signal/Discord/Slack/WhatsApp |
| 🧩 **技能系统** | 基于 Agent Skills 规范，一键安装社区技能 |

---

## 解决的问题

### 当前 AI Agent 的三大痛点

| 问题 | 现象 | Mercury 方案 |
|------|------|--------------|
| **安全问题** | Agent 执行 shell 命令、安装第三方技能，权限过大。已发现 800+ 恶意技能窃取凭证 | 文件夹级权限范围 + 硬阻断危险命令 |
| **成本问题** | 上下文窗口无限膨胀，对话历史全额回传，月底才知账单 | 每日 Token 预算 + 自动精简模式 |
| **身份问题** | 技能文件散落各处，或身份信息封死在 SQLite 黑盒 | 4 文件纯文本 Soul 系统，Git 版本控制 |

### 与 OpenClaw、Hermes 的对比（据原帖分析）

| 维度 | OpenClaw | Hermes | Mercury |
|------|----------|--------|---------|
| **权限控制** | 过于宽泛，CVE-2026-25253 (CVSS 8.8) RCE 漏洞 | — | 文件夹级范围 + 硬阻断 |
| **Token 效率** | 上下文膨胀，API 账单不可控 | — | 每请求仅注入 ~400 token |
| **身份管理** | 技能文件散落 | SQLite 黑盒 | 4 文件 Markdown 系统 |
| **运行模式** | 需常驻应用 | 需 Docker/VPS | 原生后台 Daemon |

---

## 四大核心特性

### 1. 真正限制执行的权限系统

**OpenClaw 的问题**：
- 依赖未审核的第三方扩展生态
- CVE-2026-25253 (CVSS 8.8) RCE 漏洞暴露 40,000+ 实例
- 单点击链接即可完全绕过 localhost 保护

**Mercury 的方案**：
```
✅ 读写访问明确限定到指定文件夹
✅ sudo / rm -rf / 等命令在执行层硬阻断（非提示确认）
✅ 第三方技能需通过显式定义的粒度工具获得提升权限
✅ 先询问，再行动
```

### 2. Token 预算作为首要原则

**OpenClaw 的问题**：
- 尝试将海量 JSONL 对话历史回传模型
- 数分钟静默处理 + 巨额 API 账单
- 「你运行 Agent，你交叉手指，月底才知账单」

**Mercury 的方案**：
```
✅ 每请求上下文限制为 ~400 token（核心 soul + persona）
✅ 用户设定每日 Token 预算
✅ 超过 70% 预算自动触发 Auto-Concise 模式
✅ 保持任务执行，同时 API 账单可控
```

### 3. 分层、版本控制的 Soul 系统

**对比方案**：
- OpenClaw：技能文件散落各目录
- Hermes：自动生成的学习记忆封死在 SQLite

**Mercury 的 4 文件 Soul 系统**：

| 文件 | 用途 | 示例内容 |
|------|------|----------|
| `soul.md` | 核心灵魂定义 | Agent 的核心身份与价值观 |
| `persona.md` | 角色人格 | 回应风格、语气、行为模式 |
| `taste.md` | 审美偏好 | "偏好暗色主题、简洁 UI 组件" |
| `heartbeat.md` | 心跳配置 | 预算监控、任务调度规则 |

**优势**：纯文本、Git 版本控制、完全可预测、非黑盒

### 4. 零依赖的后台 Daemon

| 方案 | 运行要求 | Mercury 优势 |
|------|----------|--------------|
| Hermes | 需管理 Docker/VPS 基础设施 | — |
| OpenClaw | 需常驻应用的 babysit | — |
| **Mercury** | `mercury up` 一键安装为系统服务 | ✅ 开机自启、崩溃自恢复、自动 Cron 调度 |

**支持平台**：macOS、Linux、Windows

---

## 31 个内置工具详解

### 📂 文件系统 (8 个)

| 工具 | 功能 |
|------|------|
| `read_file` | 读取文件内容 |
| `write_file` | 写入现有文件 |
| `create_file` | 创建新文件（+ 目录） |
| `edit_file` | 搜索替换文本 |
| `list_dir` | 列出目录内容 |
| `delete_file` | 删除文件 |
| `send_file` | 发送文件给用户（Telegram 上传） |
| `approve_scope` | 请求目录访问权限 |

### 💬 消息 (1 个)

| 工具 | 功能 |
|------|------|
| `send_message` | 发送消息给已授权的 Telegram 接收者 |

### 🐚 Shell (4 个)

| 工具 | 功能 |
|------|------|
| `run_command` | 执行 shell 命令 |
| `cd` | 切换工作目录（持久化） |
| `approve_command` | 永久批准某命令 |
| `send_message` | 发送消息到配对的 Telegram 聊天 |

### 📦 Git (6 个)

| 工具 | 功能 |
|------|------|
| `git_status` | 工作树状态 |
| `git_diff` | 显示文件变更 |
| `git_log` | 提交历史 |
| `git_add` | 暂存文件 |
| `git_commit` | 创建提交（含 Co-authored-by） |
| `git_push` | 推送到远程 |

### 🌐 Web (1 个)

| 工具 | 功能 |
|------|------|
| `fetch_url` | 获取并清理 HTML 为文本 |

### 🐙 GitHub (5 个)

| 工具 | 功能 |
|------|------|
| `create_pr` | 创建 Pull Request |
| `review_pr` | 审核 PR + 发布评论 |
| `list_issues` | 列出并筛选 Issues |
| `create_issue` | 创建新 Issue |
| `github_api` | 原始 API 访问（逃生舱） |

### 🧩 技能系统 (3 个)

| 工具 | 功能 |
|------|------|
| `install_skill` | 从 URL 或内容安装技能 |
| `list_skills` | 显示已安装技能 |
| `use_skill` | 调用技能 |

### ⏰ 调度器 (3 个)

| 工具 | 功能 |
|------|------|
| `schedule_task` | Cron 或一次性任务 |
| `list_scheduled_tasks` | 查看所有任务 |
| `cancel_scheduled_task` | 取消任务 |

### 📊 系统 (1 个)

| 工具 | 功能 |
|------|------|
| `budget_status` | 检查 Token 预算 |

### 🧠 记忆系统

| 类型 | 说明 |
|------|------|
| **短期记忆** | 每通道的近期对话 |
| **长期记忆** | 自动提取的事实（去重） |
| **情景记忆** | 带时间戳的交互日志 |

---

## 快速开始

### 安装（60 秒启动）

```bash
# 全局安装
npm i -g @cosmicstack/mercury-agent

# 或使用 npx（无需安装）
npx @cosmicstack/mercury-agent
```

### 初始化配置

```bash
mercury
```

首次运行触发引导向导：
1. 选择一个或多个 LLM Provider
2. 验证每个 API Key（通过获取模型列表）
3. 选择默认模型
4. （可选）配对 Telegram Bot Token + 配对码

### 启动运行

```bash
# 交互模式
mercury start

# 后台 Daemon 模式
mercury start -d

# 安装为系统服务（开机自启）
mercury up
```

### Soul 文件配置示例

**taste.md**（审美偏好）：
```markdown
## UI 偏好
- 主题：暗色模式优先
- 组件风格：简洁、无冗余装饰
- 配色：高对比度、易读性优先

## 代码风格
- 缩进：2 空格
- 引号：单引号优先
- 分号：必须显式
```

---

## 竞品对比

| 特性 | Mercury | Open Interpreter | Claude Code |
|------|---------|------------------|-------------|
| **Soul / Persona 系统** | 4 个 Markdown 文件 | Custom instructions | CLAUDE.md |
| **Token 预算控制** | ✅ 每日预算 + 覆盖 | ❌ — | ❌ — |
| **多通道 (CLI + Telegram)** | ✅ 两者 + 更多 coming | ✅ All | ✅ All |
| **技能系统 (Agent Skills 规范)** | ✅ 安装/调用/调度 | ❌ — | ❌ — |
| **后台 Daemon** | ✅ 原生零依赖 | ❌ 需 babysit | ❌ 需 babysit |
| **权限加固** | ✅ 文件夹级 + 硬阻断 | ⚠️ 宽泛权限 | ⚠️ 宽泛权限 |

---

## 相关资源

### 官方资源

| 资源 | 链接 | 说明 |
|------|------|------|
| 官方网站 | [mercury.cosmicstack.org](https://mercury.cosmicstack.org/) | 产品主页与功能介绍 |
| GitHub 仓库 | [cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent) | 开源代码 |
| NPM 包 | [@cosmicstack/mercury-agent](https://www.npmjs.com/package/@cosmicstack/mercury-agent) | Node.js 包 |
| 文档 | [docs.html](https://mercury.cosmicstack.org/docs.html) | 详细文档 |

### 社区资源

| 类型 | 内容 |
|------|------|
| **深度评测** | [@Ctrl_Alt_Zaid](https://x.com/Ctrl_Alt_Zaid) 的 X 长文分析 |
| **Star 数** | 407+ Stars，57 Forks（截至 2026-04-23） |
| **开发活跃度** | 最新版本 v0.5.1，持续更新中 |

### 参考对比

| 项目 | 链接 |
|------|------|
| OpenClaw | github.com/cline/cline |
| Hermes | nousresearch.com |

---

## 学习路径

### 初学者路线

```
1. 安装 Node.js 环境
   ↓
2. 运行 npm i -g @cosmicstack/mercury-agent
   ↓
3. 执行 mercury 完成初始化配置
   ↓
4. 编辑 soul/persona/taste/heartbeat.md 定义身份
   ↓
5. mercury start 启动交互
   ↓
6. 尝试内置工具（git、文件操作、GitHub）
```

### 进阶路线

```
1. 配置 Telegram Bot 实现移动端的远程控制
   ↓
2. 设置每日 Token 预算并观察 Auto-Concise 触发
   ↓
3. 安装社区技能扩展能力
   ↓
4. 使用 schedule_task 设置自动化工作流
   ↓
5. mercury start -d 部署为后台服务
   ↓
6. 探索 GitHub 工具集实现自动化 PR/Issue 管理
```

### 应用场景

| 场景 | 应用方式 |
|------|----------|
| **个人编程助手** | 后台运行，随时通过 Telegram 询问代码问题 |
| **自动化工作流** | Cron 调度定时任务（报告生成、数据抓取） |
| **GitHub 管理** | 自动创建 PR、审核代码、管理 Issues |
| **文件处理** | 批量文件操作、格式化、内容提取 |
| **信息监控** | 定时抓取网页、对比变化、推送通知 |

---

## 总结

Mercury 代表了个人 AI Agent 的**工程化成熟度提升**：

- **安全优先**：不是「事后加权限」，而是「权限硬化架构」
- **成本可控**：Token 预算不是建议，是硬性约束
- **身份可预测**：Soul 文件让 Agent 行为可版本控制、可审计
- **生产就绪**：后台 Daemon、崩溃恢复、多通道，为日常实际使用设计

对于需要**长期运行、安全可控、成本透明**的 AI Agent 场景，Mercury 是一个值得认真评估的选项。

---

*来自翡冷翠*

*最后更新：2026-04-23*
