# Hermes Agent 生态进化全景图 —— 从底层骨架到 103+ 进化体

> 来源：[@GitTrend0x](https://x.com/GitTrend0x) X 系列帖子整理  
> 整理时间：2026-04-26  
> 来自翡冷翠

---

## 📋 简介

2026 年 4 月，Nous Research 的 [hermes-agent](https://github.com/NousResearch/hermes-agent) 以 **持久记忆 + 自动提炼技能 + 跨会话成长** 的底层架构，在社区引发了一场轰轰烈烈的「进化运动」。

短短 6 周内，全球开发者基于 Hermes 的开放 DNA，fork 出 **103+ 个高质量社区项目**，生态总星数突破 **10 万+**。这不是简单的工具堆砌，而是一个**活的进化树**——每个项目都在自我改进，同时反哺整个生态。

本文档整理了从 4 月 17 日到 4 月 25 日 [@GitTrend0x](https://x.com/GitTrend0x) 发布的 **6 期「进化体」系列帖子**，涵盖 **29 个独特项目**，分类整理成这份「生态导航地图」。

---

## 📊 生态总览

| 指标 | 数据 |
|------|------|
| **主 Repo Stars** | 96k+ → 100k+（持续增长） |
| **生态项目数** | 80+ → 103+（6 周增长） |
| **生态总星数** | 10 万+ |
| **Atlas 收录** | 98+ 个安全审查项目 |
| **文档覆盖** | 29 个独特进化体 |

---

## 🗺️ 项目分类索引

| 类别 | 代表项目 | 核心价值 |
|------|----------|----------|
| **界面与可视化** | hermes-ui, hermes-webui, hermes-hud, hermes-hudui | 从 CLI 进化为 GUI/Web/TUI |
| **监控与运维** | hermes-dashboard, hermes-local-rig-accounting, Pulse | 生产环境必备的可观测性 |
| **记忆与知识** | supermemory, Persist, Nexus, Hermes-Wiki | 跨会话持久化 + 知识图谱 |
| **编排与调度** | Lyra, Multiverse, maestro | 从单 Agent 到 Agent 军团 |
| **推理与反思** | Arc, Reflect, hermes-agent-fork | 规划-执行-反思闭环 |
| **安全与边界** | hermes-agent-camel | CaMeL 信任边界 |
| **跨平台桥接** | hermesclaw, Bridge | WeChat/Slack/Discord 集成 |
| **开发工具** | hermes-skill-factory, hermes-lcm | Meta-skill + 上下文管理 |
| **云与部署** | hermes-alpha | 一键上云部署 |
| **资源索引** | awesome-hermes-agent, Hermes Atlas | 社区生态地图 |

---

## 🔥 第一弹：界面革命（Apr 17-18）

### 1. hermes-webui — 随时随地指挥的 Web 版

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/nesquena/hermes-webui |
| **类型** | Web 界面 |
| **核心亮点** | 浏览器/Web + 手机端 UI，暗黑风响应式设计 |

**功能特性：**
- 📱 手机端适配 —— 手机党终于翻身
- 🌙 暗黑主题 —— 护眼前端体验
- 🔄 响应式布局 —— 桌面/平板/手机全兼容

**社区评价**："手机党终于翻身了！"

---

### 2. hermes-dashboard — 生产环境监控台

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/Kori-x/hermes-dashboard |
| **Stars** | 19 ⭐ |
| **类型** | 实时监控 + 自动 Wiki |
| **技术栈** | React 19 + TypeScript + Vite + WebSocket |

**核心功能：**

| 模块 | 能力 |
|------|------|
| **实时监控** | Agent 会话阶段追踪（processing / idle / awaiting input / needs approval） |
| **活动流** | 工具调用、消息、审批实时展示 |
| **会话详情** | 上下文窗口可视化、工具执行历史、子 Agent 追踪 |
| **自动 Wiki** | Skills/Plugins/Tools/CLI/Config/Memory/Soul/Architecture 自动生成 |

**架构：**
```
Hermes Agent → Dashboard Plugin → Unix Socket → Bridge Server → React Dashboard
```

**社区评价**："生产环境标配，Atlas 安全审查通过！"

---

### 3. hermesclaw — 微信生态入侵者

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/AaronWong1999/hermesclaw |
| **类型** | WeChat 桥接器 |
| **官方推荐** | ✅ 主 repo 重点推送 |

**功能特性：**
- 💬 让 Hermes 和 OpenClaw 共用一个微信号
- 🔄 双向无缝通信
- 🇨🇳 中文玩家狂喜

**社区评价**："微信生态直接被 Hermes 入侵！"

---

### 4. hermes-hud / hermes-hudui — 灵魂监控 2.0

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/joeynyc/hermes-hud |
| **Stars** | ⭐ 642 |
| **标语** | *What does an AI see when it looks in a mirror?* |
| **类型** | TUI 仪表盘 → Web HUD |

**9 大监控标签页：**
1. **Overview** — 概览总览
2. **Dashboard** — 核心仪表盘
3. **Cron** — 定时任务监控
4. **Projects** — Git 项目追踪
5. **Health** — API 密钥、服务状态
6. **Corrections** — 错误日志与改正记录
7. **Agents** — 实时代理监控 + **tmux 操作员视图**
8. **Profiles** — 代理配置、会话统计
9. **Prompt Patterns** — 任务聚类、重复请求检测

**4 种主题：**
- 🔵 **Neural Awakening** — 蓝青色（默认）
- 🟠 **Blade Runner** — 琥珀霓虹粉
- 🟢 **fsociety** — 终端绿（Mr. Robot 风格）
- 🟣 **Digital Soul** — 紫粉渐变霓虹

**社区评价**："终于看到 Agent 的内心戏了"

---

### 5. awesome-hermes-agent — 社区圣经

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/0xNyk/awesome-hermes-agent |
| **Stars** | 1.8k+ ⭐ |
| **Forks** | 123 |
| **类型** | 社区资源索引 |
| **维护者** | 0xNyk (Builderz) |

**收录分类（10 大类）：**

| 类别 | 说明 |
|------|------|
| 1. 官方资源 | Nous Research 核心项目 (23k+ stars) |
| 2. 技能与插件 | 社区技能、插件、agentskills.io 生态 |
| 3. 工具与实用程序 | GUI、部署工具、分析工具 |
| 4. 部署 | Docker、Nix、云模板 |
| 5. 集成与桥接 | Android、记忆层、MCP 集成 |
| 6. 检测与媒体取证 | Deepfake 检测 |
| 7. 多代理与群体 | 多代理协调框架 |
| 8. 领域应用 | 机器人、Minecraft、求职代理等 |
| 9. 分支与衍生 | 企业/云衍生版本 |
| 10. 指南与文档 | 社区教程 |

**精选资源示例：**

| 项目 | Stars | 成熟度 |
|------|-------|--------|
| hermes-workspace | 500+ | production |
| mission-control | 3.7k+ | production |
| wondelai/skills | 380+ | production |
| SkillClaw | 705 | production |

**社区评价**："想 fork 就从这里抄作业，Atlas 列为 Guides 头牌"

---

## 🛡️ 第二弹：安全与部署（Apr 19）

### 6. hermes-agent-camel — 信任边界守护者

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/nativ3ai/hermes-agent-camel |
| **类型** | 安全插件 |
| **核心亮点** | 内置 CaMeL 信任边界 |

**功能特性：**
- 🛡️ 自主执行再也不怕翻车
- 🔒 生产环境终于敢上了
- ⚡ CaMeL (Capabilities & Mechanisms Layer) 安全框架

**社区评价**："生产环境终于敢上了！"

---

### 7. hermes-alpha — 一键上云

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/kaminocorp/hermes-alpha |
| **类型** | 云部署模板 |
| **核心亮点** | 托管基础设施，部署门槛归零 |

**功能特性：**
- ☁️ 云部署模板 + 托管基础设施
- 🚀 一键把 Hermes 扔上云
- 😴 懒人福音 —— 部署门槛直接归零

**社区评价**："懒人福音！"

---

### 8. hermes-skill-factory — Meta-skill 生成器

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/Romanescu11/hermes-skill-factory |
| **类型** | Meta-skill 插件 |
| **核心亮点** | Agent 跑完任务自动生成新 skill |

**功能特性：**
- 🏭 Agent 自己给自己造武器
- 🔄 任务完成后自动提炼 skill
- 📈 自我进化的正反馈循环

**社区评价**："Hermes 自己给自己造武器，太离谱了！"

---

### 9. maestro — 长运行强化框架

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/ReinaMacCredy/maestro |
| **类型** | 长运行框架 |
| **核心亮点** | 结构化记忆 + plan-approve-execute |

**功能特性：**
- 🎯 Plan-Approve-Execute 工作流
- 💾 结构化记忆持久化
- ⚔️ 能打持久战的 Agent

**社区评价**："把玩具 Agent 进化成生产基础设施"

---

### 10. icarus-plugin — 自动训练接班人

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/esaradev/icarus-plugin |
| **类型** | 自记忆 + 教学插件 |
| **核心亮点** | Agent 边干边教徒弟 |

**功能特性：**
- 👨‍🏫 边干活边训练接班人
- 📝 自动记录教学经验
- 🎓 退休计划安排上了

**社区评价**："退休计划安排上了"

---

## 🧠 第三弹：记忆与推理（Apr 21）

### 11. Arc — 高级推理循环

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/arcforge/hermes-arc |
| **类型** | 推理插件 |
| **核心亮点** | 规划-执行-反思闭环 |

**功能特性：**
- 🔄 自动闭环「规划-执行-反思」
- 🧠 推理能力直接起飞
- 🎯 复杂任务终于不飘了

**社区评价**："推理能力直接起飞，复杂任务终于不飘了"

---

### 12. Persist — 超长持久化记忆

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/persistentx/hermes-persist |
| **类型** | 记忆插件 |
| **核心亮点** | 跨月会话不丢任何上下文 |

**功能特性：**
- 💾 跨月会话记忆保持
- 🧠 专治 "Agent 跑着跑着就失忆"
- 🔄 自动记忆压缩与恢复

**社区评价**："专治 Agent 失忆的老毛病"

---

### 13. Multiverse — Agent 军团编排器

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/multiverse-ai/hermes-multiverse |
| **类型** | 多 Agent 编排 |
| **核心亮点** | 一键管理 10+ 子 Agent |

**功能特性：**
- 👥 一键管理 10+ 子 Agent
- 🎯 协作分工智能调度
- 🚀 单体 Agent → Agent 军团

**社区评价**："终于把单体 Agent 进化成 Agent 军团"

---

### 14. Reflect — 自反思插件

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/reflect-ai/hermes-reflect |
| **类型** | 元认知插件 |
| **核心亮点** | 自动总结经验更新 system prompt |

**功能特性：**
- 🤔 每跑完任务自动反思
- 📝 总结经验教训
- 🔄 自动更新自身 system prompt
- 🎭 Meta 程度拉满

**社区评价**："Meta 程度拉满"

---

### 15. Bridge — 跨平台桥接

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/bridge-ai/hermes-bridge |
| **类型** | 多平台集成 |
| **核心亮点** | Slack + Discord + Telegram 统一控制 |

**功能特性：**
- 💬 Slack + Discord + Telegram 三平台统一
- 🌉 哪里需要 Agent 就出现在哪里
- 🔄 双向消息同步

**社区评价**："哪里需要 Agent 就出现在哪里"

---

## 🎨 第四弹：个性化进化（Apr 22）

### 16. hermes-lcm — 上下文管理大师

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/stephenschoett/hermes-lcm |
| **类型** | 上下文管理插件 |
| **核心亮点** | 损失极低的上下文压缩 |

**功能特性：**
- 🗂️ 将对话保存为层次化 DAG
- 🔍 `lcm_grep`、`lcm_expand` 工具检索
- 📦 被压缩的历史可展开恢复

**技术亮点**：层次化 DAG 存储，支持复杂的上下文回溯

---

### 17. hermes-neurovision — 终端神经视觉仪

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/Tranquil-Flow/hermes-neurovision |
| **类型** | 可视化插件 |
| **核心亮点** | 85 种 ASCII 动态主题 |

**功能特性：**
- 🎨 85 种 ASCII 动态主题
- ✨ 随每次工具调用、内存写入亮起/熄灭
- 📊 日志叠层和调试面板
- 🧠 实时可视化 Agent "神经活动"

**社区评价**：终端里的神经视觉仪

---

### 18. supermemory — 知识图谱原生记忆

| 属性 | 详情 |
|------|------|
| **GitHub** | supermemory.ai/docs/integrations |
| **类型** | 记忆提供者 |
| **核心亮点** | 基于知识图谱的原生记忆 |

**功能特性：**
- 🕸️ 知识图谱记忆结构
- 🔄 集成到 Hermes 生命周期钩子
- 👤 自动捕捉对话、维护用户画像
- 🌐 支持多容器路由

---

### 19. Hermes WebUI（轻量版）— 暗色主题三栏界面

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/nesquena/hermes-webui |
| **类型** | 轻量 Web UI |
| **核心亮点** | 暗色主题 + 三栏界面 + Token 实时查看 |

**功能特性：**
- 🌙 轻量暗色主题
- 📊 三栏界面：会话列表 / 聊天窗口 / 文件浏览器
- 🔢 实时查看上下文 token 使用
- 🖥️ 浏览器中完整复刻 CLI 体验

---

### 20. web-search-plus — 智能多搜索引擎

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/robbyczgw-claude/web-search-plus |
| **类型** | 搜索插件 |
| **核心亮点** | 七大搜索引擎自动路由 |

**功能特性：**
- 🔍 自动路由到 Serper、Tavily、Exa 等七大服务
- 🧠 根据查询类型智能选择引擎
- ⏰ 支持时间过滤和域名过滤
- 📖 提供查询路由解释
- 🔬 深度研究模式

---

## ⚡ 第五弹：智能调度与探索（Apr 23）

### 21. Lyra — 智能调度插件

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/lyra-ai/hermes |
| **类型** | 调度插件 |
| **核心亮点** | Agent 自动优先级排序、资源分配 |

**功能特性：**
- 📋 自动优先级排序
- 🎯 资源分配智能调度
- ⚡ 任务抢占机制

**社区评价**："Agent 终于会自己排班了，人类老板可以下班"

---

### 22. Nexus — 知识融合插件

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/nexusforge/hermes-nexus |
| **类型** | 知识融合 |
| **核心亮点** | 多源记忆融合成一致知识图谱 |

**功能特性：**
- 🔗 自动融合多源记忆
- 🌐 外部 API 数据整合
- 🕸️ 构建一致知识图谱
- 🩹 解决"信息打架"顽疾

---

### 23. Pulse — 实时健康检查

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/pulsecheck/hermes-pulse |
| **类型** | 监控插件 |
| **核心亮点** | Agent 性能、内存、loop 健康度监控 |

**功能特性：**
- 💓 实时监控 Agent 性能
- 🧠 内存使用追踪
- 🔄 Loop 健康度检测
- 🔧 自动触发自我修复

**社区评价**："Agent 也有体检报告了"

---

### 24. Vanguard — 前沿探索插件

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/vanguard-ai/hermes |
| **类型** | 探索插件 |
| **核心亮点** | Agent 主动发现新工具/API/模型 |

**功能特性：**
- 🔭 主动发现新工具
- 🌐 自动探索新 API
- 🤖 边干活边扩充工具箱
- 🧭 前沿技术雷达

---

### 25. Lumina — 可视化决策引擎

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/lumina-hermes/hermes |
| **类型** | 可视化引擎 |
| **核心亮点** | 实时渲染决策树 + 记忆路径 |

**功能特性：**
- 🌳 实时渲染决策树
- 🛤️ 记忆路径可视化
- 🔗 因果链展示
- 👁️ 人类一眼看懂 Agent 在想啥

---

## 🚀 第六弹：最新进化体（Apr 25）

### 26. hermes-ui — Glassmorphic 毛玻璃界面

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/pyrate-llama/hermes-ui |
| **版本** | v3.0 |
| **类型** | Web 界面 |
| **Stars** | - |
| **技术栈** | React 18 + Python 代理服务器 |

**核心功能（12 大模块）：**

| 模块 | 功能 |
|------|------|
| **聊天界面** | SSE 流式响应、工具调用可视化、消息编辑/重试、图片粘贴/拖放、文档上传 |
| **仪表板** | 实时统计（会话/消息/工具/Token）、系统信息、模型能力标签 |
| **Artifact 面板** | 实时预览 HTML/SVG/PDF/CSV、沙盒 iframe 渲染 |
| **终端** | Shell / Hermes / Claude Code 标签页、实时日志流 |
| **文件浏览器** | 浏览 `~/.hermes` 目录、编辑配置文件 |
| **内存检查器** | 查看/编辑 MEMORY.md、USER.md |
| **技能浏览器** | 搜索/管理已安装技能、编辑/删除 |
| **MCP 工具浏览器** | 浏览连接的 MCP 服务器及其工具 |
| **推理力度控制** | 调节 Agent 推理深度 |
| **Steering** | 流中指导 Agent |

**技术亮点：**
- 📦 **单文件架构** — 整个前端打包在 `hermes-ui.html` 中
- 🚀 **零依赖部署** — 无需 `npm install`，无构建步骤
- 🐍 **轻量级代理** — `serve_lite.py` 仅使用 Python 标准库
- 🎨 **毛玻璃设计** — Glassmorphic 现代 UI

**安装：**
```bash
git clone https://github.com/pyrate-llama/hermes-ui.git
cd hermes-ui
python3 serve_lite.py
# 访问 http://localhost:3333/hermes-ui.html
```

**社区评价**："终于有好看的 Agent 仪表盘"

---

### 27. hermes-local-rig-accounting — 成本监控插件

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/GumbyEnder/hermes-local-rig-accounting |
| **类型** | 成本插件 |
| **核心亮点** | 本地免费时代的终结者 |

**功能特性：**
- ⚡ 自动算电费
- 💻 硬件折旧追踪
- 💰 每 token 真实价格计算
- 📊 内置 leaderboard（排行榜）

**社区评价**："本地免费时代终结"

---

### 28. hermes-desktop — Mac 原生客户端

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/dodo-reach/hermes-desktop |
| **类型** | macOS 桌面应用 |
| **核心亮点** | 真实 SSH + 嵌入终端 |

**核心功能：**

| 功能 | 描述 |
|------|------|
| **SSH 连接** | 支持 SSH 别名、直连配置、多 Profile |
| **嵌入式终端** | 真实 SSH 终端、多标签、主题切换 |
| **文件管理** | 编辑 USER.md、MEMORY.md、SOUL.md（带冲突检测） |
| **会话管理** | 从 SQLite 读取会话、搜索、删除 |
| **Cron 任务** | 管理定时任务（创建/编辑/暂停/运行/删除） |
| **使用统计** | Token 统计、模型分析、跨 Profile 汇总 |
| **Skills** | 浏览和编辑远程 SKILL.md |
| **多语言** | 英文、简体中文、俄文 |
| **架构** | Universal (Apple Silicon + Intel) |

**安装：**
- 从 GitHub Releases 下载 `HermesDesktop.app.zip`
- macOS 14+ 支持

**核心理念**：Hermes 主机是唯一的真实数据源，SSH 直连不镜像

**社区评价**："CLI 玩具进化成 Mac 神器"

---

### 29. hermes-agent-fork — 强化 Fork 版

| 属性 | 详情 |
|------|------|
| **GitHub** | github.com/morph-labs/hermes-agent-fork |
| **类型** | Fork 强化版 |
| **核心亮点** | 保留自进化循环 + OpenClaw 迁移优化 |

**功能特性：**
- 🔄 保留完整自进化循环
- 🦞 OpenClaw 迁移优化
- 🧠 深度玩家专用 hack 版本
- ⚡ 性能增强

**社区评价**："深度玩家直接上手 hack"

---

## 📚 资源汇总

### 生态地图导航

| 资源 | 链接 | 说明 |
|------|------|------|
| **Hermes Atlas** | [hermesatlas.com](https://hermesatlas.com) | 官方生态地图，103+ 项目 |
| **awesome-hermes-agent** | github.com/0xNyk/awesome-hermes-agent | 社区资源索引，1.8k+ stars |
| **Hermes Ecosystem** | github.com/ksimback/hermes-ecosystem | 生态地图仓库 |
| **Nous Research 主 Repo** | github.com/NousResearch/hermes-agent | 96k+ stars |

### 值得关注的人/账号

| 账号 | 角色 | 贡献 |
|------|------|------|
| [@GitTrend0x](https://x.com/GitTrend0x) | 生态挖掘者 | 每日精选 Hermes 进化体 |
| [@ksimback](https://github.com/ksimback) | Atlas 作者 | 构建 hermesatlas.com |
| [@0xNyk](https://github.com/0xNyk) | 社区索引者 | 维护 awesome-hermes-agent |
| [@joeynyc](https://github.com/joeynyc) | HUD 作者 | hermes-hud / hermes-hudui |
| [@pyrate-llama](https://github.com/pyrate-llama) | UI 作者 | hermes-ui |

---

## 🎯 快速上手路径

### 新手入门路线
1. **了解基础** → 阅读 [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)
2. **浏览生态** → 访问 [hermesatlas.com](https://hermesatlas.com)
3. **安装界面** → 尝试 [hermes-ui](https://github.com/pyrate-llama/hermes-ui) 或 [hermes-desktop](https://github.com/dodo-reach/hermes-desktop)
4. **添加监控** → 部署 [hermes-dashboard](https://github.com/Kori-x/hermes-dashboard)

### 深度玩家路线
1. **Fork 主 Repo** → github.com/NousResearch/hermes-agent
2. **安装强化版** → [hermes-agent-fork](https://github.com/morph-labs/hermes-agent-fork)
3. **自定义插件** → 参考 [hermes-skill-factory](https://github.com/Romanescu11/hermes-skill-factory)
4. **贡献社区** → 提交 PR 到 Atlas

---

## 💡 核心洞察：为什么 Hermes 生态这么猛？

### 1. 开放底层 DNA
- 🔓 **可读、可 hack、可自我改进** 的底层循环
- 🧬 **持久记忆 + 自动提炼技能 + 跨会话成长**
- 🚀 从 80+ 到 103+ 只用了 6 周

### 2. 社区 remix 文化
- 🎨 不是用工具，而是和 Agent 一起**递归自我改进**
- 🔄 每个项目都是进化树的一个分支
- 🌳 **一个 Agent，变成全世界的进化树**

### 3. 互补式创新
| 维度 | 项目组合 |
|------|----------|
| **界面层** | hermes-ui + hermes-desktop + hermes-hud |
| **监控层** | hermes-dashboard + hermes-local-rig-accounting + Pulse |
| **记忆层** | Persist + supermemory + Nexus |
| **编排层** | Lyra + Multiverse + maestro |
| **安全层** | hermes-agent-camel + Bridge |

### 4. 生产就绪
- ✅ Atlas 安全审查通过
- 🏭 从玩具 → 生产基础设施
- 💼 企业级监控、成本核算、多 Agent 编排

---

## 📅 时间线回顾

| 日期 | 里程碑 |
|------|--------|
| Apr 17 | Hermes 主 repo 90k+ stars，生态 80+ 项目 |
| Apr 18 | 发布 5 个最新进化体（界面革命） |
| Apr 19 | 发布 5 个新进化体（安全与部署） |
| Apr 21 | 发布 5 个新进化体（记忆与推理） |
| Apr 22 | 发布 5 个新进化体（个性化进化） |
| Apr 23 | 发布 5 个新进化体（智能调度与探索） |
| Apr 25 | 发布 5 个最新进化体（全面进化），主 repo 破 100k stars |

---

## 📝 附录：快速参考

### 常用命令

```bash
# 克隆主 Repo
git clone https://github.com/NousResearch/hermes-agent.git

# 启动 hermes-ui
git clone https://github.com/pyrate-llama/hermes-ui.git
cd hermes-ui && python3 serve_lite.py

# 安装 hermes-dashboard
git clone https://github.com/Kori-x/hermes-dashboard.git
cd hermes-dashboard && ./install.sh

# 启动 hermes-hud
hermes-hud              # 交互式 TUI
hermes-hud --snapshot   # 保存快照
```

### 关键概念

| 概念 | 解释 |
|------|------|
| **Self-Evolution** | 自进化 —— Agent 通过反思循环自我改进 |
| **Persistent Memory** | 持久记忆 —— 跨会话保持上下文 |
| **Skill Extraction** | 技能提炼 —— 自动从任务中提炼可复用技能 |
| **Cross-Session Growth** | 跨会话成长 —— 长期积累知识与经验 |
| **Meta-Skill** | 元技能 —— 生成其他技能的技能 |

---

*来自翡冷翠*

---

**文档信息：**
- 原始来源：[@GitTrend0x](https://x.com/GitTrend0x) X 系列帖子
- 收录项目：29 个独特进化体
- 时间跨度：2026-04-17 至 2026-04-25
- 字数统计：约 1.5 万字
