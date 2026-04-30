# Hermes WebUI：浏览器中的 Hermes Agent 完整界面

> 来源：https://x.com/laogui/status/2046980600830308691
> 整理时间：2026-04-23
> 来自翡冷翠

---

## 简介

**Hermes WebUI** 是目前最好用的 Hermes Agent Web 界面，由 @nesquena 开发。它将会话管理、工作区文件浏览、自动化任务、长期记忆、多 Profiles 等常用能力全部搬进了浏览器。

**核心亮点**：
- 与 TUI 和 Telegram 会话无缝续聊
- 可随时切换工作目录和 Profiles
- 纯 UI 层，对接现有 Hermes 服务，数据保留在原机器
- 无构建步骤、无框架、无打包器 —— 仅用 Python 和原生 JS

---

## 核心功能一览

| 功能 | 说明 |
|------|------|
| **会话管理** | 在浏览器中管理所有 Hermes 会话 |
| **工作区文件浏览** | 右侧边栏直接浏览工作区文件 |
| **自动化任务** | 支持 cron 任务和自动化工作流 |
| **长期记忆** | Hermes 的记忆系统完整可用 |
| **多 Profiles 切换** | 按需切换不同 AI 员工配置 |
| **三栏布局** | 左侧会话导航、中间聊天、右侧文件浏览 |
| **Composer Footer** | 底部固定区域控制模型、profile、工作区 |
| **Token 用量环** | 圆形上下文环显示 token 使用量 |
| **Hermes 控制中心** | 侧边栏底部的启动器访问所有设置 |

---

## 界面布局详解

```
┌─────────────────────────────────────────────────────────────┐
│  左侧边栏        │     中间聊天区      │     右侧边栏       │
│  ─────────────  │  ────────────────  │  ───────────────  │
│                │                     │                    │
│  会话列表      │    消息气泡         │   工作区文件浏览   │
│  导航菜单      │                     │   文件操作         │
│                │                     │                    │
│  ─────────────  │  ────────────────  │  ───────────────  │
│  Hermes        │  Composer Footer   │                    │
│  Control       │  [模型][Profile]    │                    │
│  Center        │  [工作区][Token环]  │                    │
│                │                     │                    │
└─────────────────────────────────────────────────────────────┘
```

**Composer Footer**（始终可见）：
- 模型选择
- Profile 切换
- 工作目录控制
- Token 用量环（圆形上下文指示器）

---

## 部署方式

### 方式一：本机部署（最简单）

如果 Hermes 安装在本机，一条命令即可启动 WebUI：

```bash
# 进入 hermes-webui 目录
python server.py

# 或
cd hermes-webui
./start.sh
```

然后浏览器打开：`http://localhost:8787`

---

### 方式二：远程服务器 + SSH 隧道

如果 Hermes 安装在远程服务器：

**步骤 1**：在远程服务器上启动 WebUI
```bash
# SSH 登录远程服务器
ssh user@your.server.com

# 启动 WebUI
python server.py
```

**步骤 2**：在本地建立 SSH 隧道
```bash
ssh -N -L 8787:127.0.0.1:8787 user@your.server.com
```

**步骤 3**：浏览器访问
```
http://localhost:8787
```

> `-N` 表示不执行远程命令（仅做端口转发）
> `-L` 将本地 8787 端口映射到远程的 8787 端口

---

## macOS 专属：Swift 原生客户端

macOS 用户可以配合 **3MB 的 Swift 原生客户端** 使用，体验更佳：

**项目地址**：https://github.com/hermes-webui/hermes-native

```bash
# 克隆 Swift 客户端
git clone https://github.com/hermes-webui/hermes-native.git
cd hermes-native

# 构建并运行（需要 Xcode）
```

**特点**：
- 仅 3MB 大小
- Swift 原生性能
- 与 WebUI 无缝配合

---

## Profiles 管理策略

**老鬼的使用建议**：

> 建几个 Profiles 当成不同的 AI 员工，按需切换，避免所有记忆和 skills 都堆在一个 Profile 里，把上下文搞得一团糟。

**示例 Profile 划分**：

| Profile 名称 | 用途 | 挂载 Skills |
|-------------|------|------------|
| `coder` | 代码开发 | coding, git, github |
| `writer` | 内容创作 | writing, research |
| `pm` | 项目管理 | planning, linear |
| `ops` | 运维部署 | docker, k8s, aws |

**切换方式**：
- 在 Composer Footer 中直接选择 Profile
- 每个 Profile 拥有独立的记忆和上下文

---

## 技术架构

**设计哲学**：
- **无构建步骤**：直接运行，无需 npm/webpack
- **无框架**：原生 JavaScript，无 React/Vue
- **无打包器**：没有复杂的构建流程
- **仅用**：Python（后端）+ Vanilla JS（前端）

**技术栈**：
- 后端：Python Flask/FastAPI
- 前端：原生 JavaScript + CSS
- 通信：WebSocket（实时消息）+ REST API
- 数据：对接现有 Hermes Agent，不迁移数据

---

## 资源汇总

### 项目链接

| 资源 | 链接 | 说明 |
|------|------|------|
| **主项目** | https://github.com/nesquena/hermes-webui | WebUI 核心项目 |
| **Swift 客户端** | https://github.com/hermes-webui/hermes-native | macOS 原生客户端 (3MB) |
| **Hermes 官网** | https://hermes-agent.nousresearch.com/ | 官方文档 |

### 社区资源

- **作者 X**：@nesquena
- **推荐人 X**：@laogui（老鬼）
- **GitHub Stars**：3.3k+
- **Forks**：427+

---

## 快速启动清单

```bash
# 1. 克隆项目
git clone https://github.com/nesquena/hermes-webui.git
cd hermes-webui

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境（可选）
cp .env.example .env
# 编辑 .env 设置端口等

# 4. 启动服务
python server.py

# 5. 浏览器打开
open http://localhost:8787
```

---

## 适用场景

| 场景 | 为什么选 WebUI |
|------|---------------|
| 不方便用 TUI | 浏览器随时随地访问 |
| 需要文件浏览 | 右侧栏直接查看工作区 |
| 多设备切换 | 手机、平板、电脑统一界面 |
| 团队协作 | 共享 Web 界面，多人查看 |
| 远程服务器 | SSH 隧道即可安全访问 |

---

## 延伸阅读

- [Hermes Agent 官方文档](https://hermes-agent.nousresearch.com/)
- 项目内的 `ARCHITECTURE.md` 了解技术细节
- `THEMES.md` 自定义主题
- `ROADMAP.md` 查看开发路线图

---

*来自翡冷翠*
