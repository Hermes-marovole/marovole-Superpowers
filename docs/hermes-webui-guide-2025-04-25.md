# Hermes WebUI 完全指南 —— 让 Hermes Agent 更好用的网页控制台

> 来源：[X @0xmulight](https://x.com/0xmulight/status/2047913598635421839)  
> 仓库：[nesquena/hermes-webui](https://github.com/nesquena/hermes-webui)  
> 整理时间：2025-04-25  
> 来自翡冷翠

---

## 简介

**Hermes WebUI** 是一个专为 [Hermes Agent](https://hermes-agent.nousresearch.com/) 打造的轻量级网页控制台。它让你告别黑色终端，在浏览器或手机上就能与 AI 助理对话。项目目前在 GitHub 已获得 **4k+ Stars**，是 Hermes 生态中最受欢迎的 Web 界面。

**核心价值**：
- 无需复杂编译环境，一键启动
- 手机浏览器深度优化，随时随地查进度、发任务
- 与 Hermes CLI 1:1 功能对等，所有终端操作都能在网页完成
- 直接复用现有 Hermes 配置，无需重复设置

---

## 核心亮点

### 1. 真正的全平台适配

界面针对手机浏览器做了深度优化：
- 出门在外用手机就能查进度或发新任务
- 多端对话数据完全同步
- 响应式布局：汉堡菜单侧边栏、触摸友好的控件

### 2. 后台动作的视觉化

AI 每次调用工具或派发子任务都会生成一张**独立卡片**：
- 清楚看到每一步的思考过程
- 哪里出错直接点开查看
- 支持展开/折叠所有工具卡片

### 3. 现有配置的无缝迁移

直接读取你之前配好的 API 和模型信息：
- 终端里设置好的英伟达 API 或本地模型，在这里直接可用
- 自动发现 Hermes Agent 目录、Python 环境、工作区
- 省去重复配置的麻烦

### 4. 自带文件浏览器

界面右侧直接预览工作区文件：
- AI 修改的代码或写的报告，直接在网页上点开确认
- 支持代码高亮、Markdown 渲染、图片预览
- 文件树导航、面包屑路径、Git 分支状态显示

---

## 快速开始

### 方法一：一键启动脚本（推荐）

```bash
# 克隆仓库
git clone https://github.com/nesquena/hermes-webui.git hermes-webui
cd hermes-webui

# 运行启动脚本
./start.sh
```

启动脚本会自动：
1. 检测 Hermes Agent，如缺失则尝试自动安装
2. 找到或创建带 WebUI 依赖的 Python 环境
3. 启动 Web 服务器并等待健康检查
4. 自动打开浏览器
5. 进入首次使用的引导向导

### 方法二：Docker 部署

```bash
# 拉取预构建镜像
docker pull ghcr.io/nesquena/hermes-webui:latest

# 运行容器
docker run -d \
  -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` \
  -v ~/.hermes:/home/hermeswebui/.hermes \
  -e HERMES_WEBUI_STATE_DIR=/home/hermeswebui/.hermes/webui-mvp \
  -v ~/workspace:/workspace \
  -p 8787:8787 \
  ghcr.io/nesquena/hermes-webui:latest
```

或使用 Docker Compose（推荐）：
```bash
docker compose up -d
```

### 方法三：手动启动

```bash
cd /path/to/hermes-agent
HERMES_WEBUI_PORT=8787 venv/bin/python /path/to/hermes-webui/server.py
```

访问：`http://localhost:8787`

---

## 远程访问方案

### 方案 A：SSH 隧道

如果你运行在远程服务器/VPS：

```bash
ssh -N -L 8787:127.0.0.1:8787 user@your.server.com
```

然后在本地浏览器打开 `http://localhost:8787`

### 方案 B：Tailscale（零配置 VPN）

1. 在服务器和手机上都安装 [Tailscale](https://tailscale.com/)
2. 启动 WebUI 监听所有接口并启用密码保护：
   ```bash
   HERMES_WEBUI_HOST=0.0.0.0 HERMES_WEBUI_PASSWORD=你的密码 ./start.sh
   ```
3. 在手机浏览器访问 `http://<服务器TailscaleIP>:8787`

**优势**：
- 无需端口转发或公网暴露
- 端到端 WireGuard 加密
- 可添加到手机主屏幕，获得类 App 体验

---

## 功能详解

### 三栏布局

| 面板 | 功能 |
|------|------|
| **左侧边栏** | 会话列表、搜索、项目分组、标签筛选 |
| **中间聊天区** | 对话、流式响应、工具卡片、子任务委派 |
| **右侧文件区** | 工作区文件浏览、预览、编辑 |

### 聊天功能

- **流式响应**：SSE 实时推送， tokens 逐字显示
- **多模型支持**：OpenAI、Anthropic、Google、DeepSeek、OpenRouter 等
- **消息队列**：可在处理中发送新消息，自动排队
- **历史编辑**：点击任意用户消息可编辑并重新生成
- **工具调用卡片**：每个工具调用独立显示，含参数和结果
- **Mermaid 图表**：直接在对话中渲染流程图、时序图
- **语音输入**：麦克风按钮，支持实时语音转文字

### 会话管理

- 创建、重命名、复制、删除、搜索会话
- 固定/收藏会话置顶显示
- 归档会话（隐藏但不删除）
- 项目分组 + 标签系统
- CLI 会话桥接：终端会话同步显示在侧边栏
- 导出为 Markdown / JSON，或从 JSON 导入

### 工作区文件浏览器

- 目录树展开/折叠
- 面包屑导航
- 代码、Markdown、图片内联预览
- 编辑、创建、删除、重命名文件
- Git 分支名称和未提交文件数显示
- 二进制文件下载

### 面板系统

- **Tasks**：Cron 任务管理，查看、创建、编辑、运行定时任务
- **Skills**：技能库浏览、搜索、创建、编辑
- **Memory**：MEMORY.md 和 USER.md 内联编辑
- **Profiles**：多配置文件切换、创建、克隆
- **Todos**：当前会话任务列表
- **Spaces**：工作区切换管理

### 主题与个性化

7 种内置主题：
- Dark（默认）
- Light
- Slate
- Solarized Dark
- Monokai
- Nord
- OLED（纯黑背景，适合 OLED 屏幕）

支持自定义主题，通过 CSS 变量定义。

---

## 高级配置

### 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `HERMES_WEBUI_AGENT_DIR` | 自动发现 | Hermes Agent 路径 |
| `HERMES_WEBUI_PYTHON` | 自动发现 | Python 可执行文件 |
| `HERMES_WEBUI_HOST` | `127.0.0.1` | 绑定地址 |
| `HERMES_WEBUI_PORT` | `8787` | 端口 |
| `HERMES_WEBUI_STATE_DIR` | `~/.hermes/webui-mvp` | 状态存储目录 |
| `HERMES_WEBUI_DEFAULT_WORKSPACE` | `~/workspace` | 默认工作区 |
| `HERMES_WEBUI_DEFAULT_MODEL` | `openai/gpt-5.4-mini` | 默认模型 |
| `HERMES_WEBUI_PASSWORD` | （未设置） | 启用密码认证 |
| `HERMES_HOME` | `~/.hermes` | Hermes 基础目录 |

### 多容器部署

**Agent + WebUI 双容器**：
```bash
docker compose -f docker-compose.two-container.yml up -d
```

**Agent + Dashboard + WebUI 三容器**：
```bash
docker compose -f docker-compose.three-container.yml up -d
```

共享 `hermes-home` 卷，确保配置、会话、技能、记忆在所有服务间一致。

---

## 与竞品对比

| 特性 | OpenClaw | Claude Code | Codex CLI | Hermes WebUI |
|------|----------|-------------|-----------|--------------|
| 持久记忆 | ✅ | 部分 | 部分 | ✅ |
| 自托管定时任务 | ✅ | ❌ | ❌ | ✅ |
| 消息应用接入 | ✅ (15+) | 部分 | ❌ | ✅ (10+) |
| Web UI (自托管) | Dashboard 仅 | ❌ | ❌ | ✅ |
| 自改进技能 | 部分 | ❌ | ❌ | ✅ |
| Python/ML 生态 | ❌ (Node.js) | ❌ | ❌ | ✅ |
| 多供应商支持 | ✅ | ❌ (仅 Claude) | ✅ | ✅ |
| 开源 | ✅ (MIT) | ❌ | ✅ | ✅ |

**最接近的竞品是 OpenClaw**，两者都是自托管、开源、带记忆和定时任务的 Agent。关键差异：
- Hermes 自动编写和保存技能（OpenClaw 依赖社区市场）
- Hermes 在 Python 生态中原生运行
- Hermes 更稳定，OpenClaw 有文档化的发布回归问题

---

## 常见问题

### Q: 原生 Windows 支持吗？
A: 启动脚本暂不支持原生 Windows。请使用 Linux、macOS 或 WSL2。

### Q: 忘记设置密码，如何启用认证？
A: 启动时设置环境变量：`HERMES_WEBUI_PASSWORD=你的密码 ./start.sh`

### Q: 移动端如何使用？
A: WebUI 完全响应式，手机浏览器访问即可。建议配合 Tailscale 使用。

### Q: 与 Hermes CLI 的数据同步吗？
A: 完全同步。CLI 会话会自动出现在 WebUI 侧边栏，带金色 "cli" 标记。

### Q: 支持哪些模型？
A: 任何 Hermes API 支持的提供商：OpenAI、Anthropic、Google、DeepSeek、Nous Portal、OpenRouter、MiniMax、Z.AI 等。

---

## 相关资源

- **GitHub 仓库**：https://github.com/nesquena/hermes-webui
- **Hermes Agent 官网**：https://hermes-agent.nousresearch.com/
- **Docker 镜像**：`ghcr.io/nesquena/hermes-webui:latest`
- **文档**：
  - `HERMES.md` — 为何选择 Hermes，详细竞品对比
  - `ROADMAP.md` — 功能路线图
  - `ARCHITECTURE.md` — 系统设计
  - `TESTING.md` — 测试指南
  - `CHANGELOG.md` — 更新日志
  - `THEMES.md` — 主题系统文档

---

## 适用场景

| 场景 | 使用建议 |
|------|----------|
| 日常对话 | 手机浏览器 + Tailscale，随时访问 |
| 代码开发 | 桌面浏览器，配合文件浏览器查看修改 |
| 任务调度 | Tasks 面板管理 Cron 作业 |
| 技能开发 | Skills 面板创建、编辑、测试 |
| 多项目管理 | 工作区切换 + 项目分组 |
| 团队协作 | 共享 Hermes 实例 + 密码保护 |

---

## 快速参考

```bash
# 启动 WebUI
./start.sh

# 指定端口
./start.sh 9000

# Docker 启动
docker compose up -d

# SSH 隧道访问远程实例
ssh -N -L 8787:127.0.0.1:8787 user@server

# 检查健康状态
curl http://127.0.0.1:8787/health

# 运行测试
pytest tests/ -v --timeout=60
```

---

*来自翡冷翠*
