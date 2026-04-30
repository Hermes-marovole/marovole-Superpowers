# OpenClaw 浏览器自动化完全指南

> 来源：https://x.com/shangdu2005/status/2048959974857228555
> 整理时间：2026-04-29
> 来自翡冷翠

---

## 简介

OpenClaw 是一个自托管的多通道 AI Agent 网关，让你在本地机器上运行 AI 助手，直接操作浏览器、自动化任务、管理多种通信渠道。本指南整理自 X 用户 [@shangdu2005](https://x.com/shangdu2005) 的分享，详细介绍如何通过 OpenClaw 让你的 Claude Code 具备操作任意网站的能力。

**核心价值**：
- 零 LLM 成本 —— 复用已登录的 Chrome，不额外消耗 API 调用
- 无需模拟/反爬 —— 直接控制真实浏览器环境
- 支持任意网站 —— 小红书、B站、知乎、Twitter 等均可操作

---

## 原帖内容

**@shangdu2005（领哥LingGe）在 X 上分享**：

> 装一个 skill！你的 Claude Code 就能操作小红书、B站、知乎、Twitter 任意网站。
>
> Agent 自动 navigate → click → type → extract
> 把你的浏览器变成 AI 操作后端。
>
> 不用模拟，不用反爬。直接复用你已登录的 Chrome。
> 零 LLM 成本，一万次执行不花一分钱。

此贴同时引用了 OpenClaw 2026.4.25 的 TTS（语音合成）全面升级公告，显示该项目正在积极迭代。

---

## OpenClaw 是什么

OpenClaw 是一个**自托管的 AI Agent 网关**，核心特点：

| 特性 | 说明 |
|------|------|
| **多通道支持** | Telegram、WhatsApp、Discord、Slack、iMessage 等 15+ 通信渠道 |
| **浏览器自动化** | Chrome MCP 集成、多 profile 控制、现有会话接管 |
| **多 Agent 路由** | 支持配置多个 Agent，各自隔离工作区和会话 |
| **ACP 外部运行时** | 可调用 Codex、Claude Code、Gemini CLI 等 14+ 种 Agent |
| **插件系统** | 能力模型、上下文引擎插件、SDK、Hook API |
| **自动化** | Cron 任务、Webhook、后台任务、定时指令 |

### 核心架构组件

```
┌─────────────────────────────────────────────────────────────┐
│                     OpenClaw Gateway                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Channels   │  │    Agent     │  │   Browser    │      │
│  │  (Telegram   │  │   Runtime    │  │  (Chrome     │      │
│  │   WhatsApp   │  │              │  │   MCP)       │      │
│  │   Discord...)│  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Memory     │  │   Plugin     │  │   Cron/Web   │      │
│  │  (Vector     │  │   System     │  │   Hooks      │      │
│  │   Search)    │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

---

## 浏览器自动化能力详解

### 核心功能

OpenClaw 提供强大的浏览器自动化工具集，支持：

| 能力 | 命令示例 | 用途 |
|------|----------|------|
| **页面导航** | `browser_navigate` | 访问指定 URL |
| **元素点击** | `browser_click` | 模拟用户点击 |
| **文本输入** | `browser_type` | 在表单中输入内容 |
| **内容提取** | `browser_snapshot` | 获取页面完整快照 |
| **滚动页面** | `browser_scroll` | 加载更多内容 |
| **键盘操作** | `browser_press` | 发送 Enter、Tab 等按键 |

### 两种浏览器控制方式

#### 方式一：OpenClaw 内置浏览器（Chrome Relay）

```bash
# 多 profile 浏览器控制
openclaw browser --profile work  # 工作 profile
openclaw browser --profile personal  # 个人 profile
```

**特点**：
- 支持多 profile 隔离
- 可与现有 Chrome 会话共存
- 支持快照/引用系统（snapshots/refs）

#### 方式二：Claude Code Chrome 扩展（替代方案）

```bash
# 检查 Chrome 扩展是否激活
pgrep -f "claude --chrome-native-host"

# 使用 Claude Code 执行浏览器任务
claude --dangerously-skip-permissions --chrome -p "Go to example.com and read the headline"
```

**特点**：
- 直接使用 Claude Code 的 Chrome MCP 集成
- 无需额外安装 OpenClaw browser 模块
- 适合已有 Claude Code 环境的用户

---

## 核心资源汇总

### 官方资源

| 资源 | 链接 | 说明 |
|------|------|------|
| **OpenClaw 主仓库** | https://github.com/openclaw/openclaw | 官方开源项目 |
| **官方文档** | https://docs.openclaw.ai/ | 完整文档中心 |
| **ClawHub 技能注册表** | https://clawhub.ai/ | 社区技能市场 |
| **技能仓库** | https://github.com/openclaw/skills | 官方技能集合 |

### 社区资源

| 资源 | 链接 | 说明 |
|------|------|------|
| **Awesome OpenClaw Skills** | https://github.com/VoltAgent/awesome-openclaw-skills | 5200+ 社区技能整理（47k+ stars） |
| **OpenClaw-Skill** | https://github.com/win4r/OpenClaw-Skill | 完整的 Agent Skill 参考（6000+ 行文档） |
| **ClawSkills.sh** | https://clawskills.sh/ | 技能浏览器和分类目录 |

### 关键技能推荐

从 5200+ 社区技能中筛选出的浏览器/自动化相关技能：

| 技能 | 类别 | 功能 |
|------|------|------|
| `claude-chrome` | 浏览器自动化 | Claude Code Chrome 扩展集成 |
| `browser` | 浏览器控制 | OpenClaw 内置浏览器工具 |
| `chrome-mcp` | MCP 集成 | Chrome MCP 服务器连接 |
| `multi-profile` | 配置管理 | 多浏览器 profile 管理 |
| `web-fetch` | 数据抓取 | 轻量级网页内容提取 |

---

## 快速开始指南

### 安装 OpenClaw

```bash
# 通过 npm 安装
npm install -g openclaw

# 或者使用 Docker
docker pull openclaw/openclaw:latest
```

### 基础配置

```bash
# 初始化配置
openclaw onboard

# 查看状态
openclaw status
openclaw doctor  # 诊断问题

# 配置模型
openclaw models set claude-sonnet-4
```

### 启动 Gateway

```bash
# 安装为系统服务
openclaw gateway install

# 启动/停止/重启
openclaw gateway start
openclaw gateway stop
openclaw gateway restart

# 查看状态
openclaw gateway status
```

### 添加通信渠道（可选）

```bash
# 添加 Telegram 机器人
openclaw channels add telegram

# 添加其他渠道
openclaw channels add discord
openclaw channels add slack

# 查看已配置渠道
openclaw channels list
openclaw channels status --probe  # 健康检查
```

---

## 浏览器自动化实战示例

### 示例 1：访问网页并提取内容

```python
# 导航到目标网站
browser_navigate(url="https://www.example.com")

# 获取页面快照
snapshot = browser_snapshot(full=true)

# 提取特定元素（通过 ref ID）
browser_click(ref="e5")  # 点击 ref=e5 的元素

# 在输入框中输入内容
browser_type(ref="e10", text="搜索关键词")
browser_press(key="Enter")  # 按回车搜索
```

### 示例 2：处理登录墙网站

对于需要登录的网站（如 X/Twitter）：

```python
# 使用已登录的 Chrome profile
# 在 openclaw.json 中配置:
# "browser": {
#   "profile": "user",
#   "chromePath": "/Applications/Google Chrome.app"
# }

# 直接访问需要登录的页面
browser_navigate(url="https://x.com/shangdu2005/status/...")

# 由于复用已登录的 Chrome，无需再次登录
snapshot = browser_snapshot(full=true)
```

### 示例 3：滚动加载更多内容

```python
# 初始快照
snapshot = browser_snapshot()

# 如果内容被截断，向下滚动
browser_scroll(direction="down")

# 获取完整内容
snapshot = browser_snapshot(full=true)
```

---

## 性能基准参考

使用 Claude Code Chrome 扩展时的典型性能：

| 任务类型 | 示例 | 耗时 | 建议超时设置 |
|----------|------|------|--------------|
| **简单** | 读取 Google 页面按钮文字 | 13s | 30s (30000ms) |
| **中等** | Wikipedia 搜索 + 导航 + 总结 | 76s | 2min (120000ms) |
| **复杂** | 多页面导航 + 外部链接 | 90s+ | 3min (180000ms) |

**注意**：OpenClaw Gateway 有 10 秒的硬编码连接超时，但命令会在后台继续运行，完成后通过系统消息返回结果。

---

## 安全提示

> ⚠️ **Skills in this list are curated, not audited.**

使用任何 Agent Skill 前请注意：

1. **审查源代码** — 技能可能包含 prompt 注入、工具投毒或隐藏恶意载荷
2. **使用安全扫描工具** — 如 [Snyk Agent Scan](https://github.com/snyk/agent-scan)
3. **检查 VirusTotal 报告** — ClawHub 上的技能页面会显示安全扫描结果
4. **权限控制** — 使用 `--dangerously-skip-permissions` 时需谨慎

---

## 故障排除

### 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| EADDRINUSE 错误 | 端口冲突 | `openclaw gateway --force` 或更换端口 |
| Gateway 无响应 | 服务未启动 | `openclaw gateway start` |
| 浏览器连接失败 | Chrome 未运行 | 先启动 Chrome |
| 权限被拒绝 | 缺少执行权限 | `chmod +x` 或检查系统权限 |

### 诊断命令

```bash
# 全面诊断
openclaw doctor

# 查看日志
openclaw gateway logs

# 渠道健康检查
openclaw channels status --probe

# 配置检查
openclaw config get
```

---

## 相关项目生态

### 模型提供商支持（25+）

OpenClaw 原生支持主流 LLM 提供商：
- **Anthropic** — Claude 系列
- **OpenAI** — GPT-5.4 / GPT-5.4 Pro（支持 WebSocket 低延迟传输）
- **Google** — Gemini 系列
- **Ollama** — 本地模型
- 以及 20+ 其他提供商

### 部署选项

- **Docker** — `docker pull openclaw/openclaw`
- **Podman** — 兼容容器运行时
- **Nix** — 函数式包管理
- **Ansible** — 自动化部署
- **VPS/云服务器** — 任何主流云平台

---

## 学习路径建议

### 初学者
1. 安装 OpenClaw — `npm install -g openclaw`
2. 完成 onboarding — `openclaw onboard`
3. 尝试基础浏览器操作 — 访问简单网页
4. 安装第一个 skill — `clawhub install browser`

### 进阶用户
1. 配置多 profile 浏览器隔离
2. 设置 ACP Agent（Codex/Claude Code）集成
3. 探索 Cron 自动化任务
4. 参与社区技能贡献

### 开发者
1. 开发自定义 Skill
2. 使用 Plugin SDK 扩展功能
3. 贡献到官方技能仓库
4. 参与开源项目开发

---

## 参考链接汇总

### 必看资源
- [OpenClaw 官方仓库](https://github.com/openclaw/openclaw)
- [官方文档](https://docs.openclaw.ai/)
- [Awesome OpenClaw Skills](https://github.com/VoltAgent/awesome-openclaw-skills) — 5200+ 技能整理

### 社区资源
- [ClawSkills.sh](https://clawskills.sh/) — 技能浏览器
- [VoltAgent Discord](https://s.voltagent.dev/discord) — 社区讨论
- [OpenClaw-Skill 详细参考](https://github.com/win4r/OpenClaw-Skill) — 6000+ 行文档

### 相关生态
- [Claude Code](https://github.com/anthropics/claude-code) — Anthropic 官方 CLI
- [Codex CLI](https://github.com/openai/codex) — OpenAI 编码 Agent
- [VoltAgent](https://github.com/VoltAgent/voltagent) — Agent 框架

---

## 快速参考卡片

```bash
# === 安装与配置 ===
npm install -g openclaw          # 安装
openclaw onboard                 # 初始化配置
openclaw status                  # 查看状态
openclaw doctor                  # 诊断问题

# === Gateway 管理 ===
openclaw gateway install         # 安装为服务
openclaw gateway start           # 启动
openclaw gateway stop            # 停止
openclaw gateway restart         # 重启

# === 模型配置 ===
openclaw models set <model>      # 设置默认模型
openclaw models status --probe   # 检查认证状态

# === 渠道管理 ===
openclaw channels add            # 添加渠道向导
openclaw channels list           # 列出已配置
openclaw channels status --probe # 健康检查

# === 浏览器操作 ===
browser_navigate(url="...")      # 导航
browser_click(ref="e5")          # 点击
browser_type(ref="e5", text="...") # 输入
browser_scroll(direction="down") # 滚动
browser_snapshot(full=true)      # 获取快照

# === 安全 ===
openclaw security audit          # 安全审计
openclaw security audit --fix    # 自动修复
```

---

*来自翡冷翠*
