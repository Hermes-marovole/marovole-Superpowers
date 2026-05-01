# Hermes Agent 资源合集 - 从入门到进阶完整指南

> 来源：
> - [爱丽丝呀！ - Hermes Agent 自我进化资源合集](https://x.com/BTCqzy1/status/2046437276235022371)
> - [Dr. Moyu 摸鱼局长 - 10篇保姆级教程合集](https://x.com/Jason23818126/status/2046426659264540866)
> 整理时间：2026-05-01
> 来自翡冷翠

---

## 简介

这是目前 X 上关于 **Hermes Agent** 最全面的两份资源合集整理。

- **合集A（爱丽丝呀！）**：聚焦 Hermes Agent 的持久记忆、自动提炼技能、跨会话成长等自我进化能力，帮你把 Hermes 打造成长期运行的生产力引擎
- **合集B（摸鱼局长）**：覆盖 Windows 本地部署、云服务器方案、多智能体团队构建、免费模型配置、中高阶玩法等 10 篇保姆级教程

两份合集结合使用，能帮你从快速上手到长期自我进化，一路走通。

---

## 内容清单总览

### 合集A：进阶资源（11个生态项目）

| 序号 | 标题 | 类型 | 核心亮点 |
|------|------|------|----------|
| 1 | Hermes Agent 官方文档 | 文档 | 最全面的安装到架构解析 |
| 2 | Hermes Agent 主引擎 | 仓库 | Nous Research 官方核心代码 |
| 3 | Hermes-Wiki | 仓库 | 基于源码自动生成的 Agent 自解释文档 |
| 4 | Hermes Atlas | 仓库 | 社区维护的 80+ 工具与技能全景图 |
| 5 | Hermes Control Interface | 仓库 | 自托管仪表盘，统一调度多 Agent |
| 6 | Hermes Skill Factory | 仓库 | 通过任务复盘自动生成新技能 |
| 7 | Maestro | 仓库 | 基于 Beads 架构的指挥官框架 |
| 8 | Hermes Agent Camel | 仓库 | 内置信任边界与安全协议 |
| 9 | Hermes HUD | 仓库 | Textual TUI 监控终端 |
| 10 | Hermes Alpha | 仓库 | 一键云端部署模板 |
| 11 | Awesome Hermes Agent | 仓库 | 社区精选插件与教程列表 |

### 合集B：入门教程（10篇保姆级指南）

| 序号 | 标题 | 作者 | 核心内容 |
|------|------|------|----------|
| 1 | Hermes Agent 安装教程 | @eternityspring | 一行命令安装流程 |
| 2 | Windows 本地部署保姆教程 | @xinchne_eth | WSL2 部署方法 |
| 3 | 云服务器部署方案 | @congge918 | 10分钟云端部署 |
| 4 | 上手后建议先尝试的十件事 | @LufzzLiz | SOUL.md、记忆系统配置 |
| 5 | Ollama 原生集成教程 | @Lonely__MH | 本地离线运行 |
| 6 | 接入即梦 CLI 教程 | @MrLarus | 自由生图、生视频 |
| 7 | 构建多智能体团队 | @NeoAIForecast | Profile 多角色协作 |
| 8 | NVIDIA 免费 Minimax 配置 | @PierceZhang34 | 10步接入免费大模型 |
| 9 | 中级到高级进阶指南 | @BTCqzy1 | 记忆管理优化 |
| 10 | Hermes 全部高阶工具配置 | @ResearchWang | SOUL.md、技能管理清单 |

---

## 合集A详细内容：进阶生态项目

### 1. Hermes Agent 官方文档
**来源**：Nous Research 官方  
**链接**：https://hermes-agent.nousresearch.com/docs/  
**类型**：官方文档

#### 核心内容
- 从安装到基础使用的完整指南
- 高级架构解析与源码解读
- API 参考与配置说明

#### 适用场景
适合初次接触的用户，快速了解 Hermes Agent 的设计哲学与核心功能。

---

### 2. Hermes Agent 主引擎
**来源**：Nous Research 官方  
**链接**：https://github.com/NousResearch/hermes-agent  
**类型**：核心仓库

#### 核心内容
- Nous Research 官方核心仓库
- Hermes Agent 完整源码
- 社区贡献指南

---

### 3. Hermes-Wiki
**来源**：社区贡献 (@cclank)  
**链接**：https://github.com/cclank/Hermes-Wiki  
**类型**：文档仓库

#### 核心内容
- 基于源码自动生成的 Wiki
- Agent 自解释实现
- 文档同步机制

#### 核心优势
自动从源码提取注释与结构，保持文档与代码同步更新，减少文档过时问题。

---

### 4. Hermes Atlas（生态地图）
**来源**：社区维护 (@ksimback)  
**链接**：https://github.com/ksimback/hermes-atlas  
**类型**：生态导航

#### 核心内容
- 社区维护的 80+ 工具与技能全景图
- 支持 RAG 查询的智能检索
- 分类整理：开发工具、生产力、创意、DevOps 等

#### 适用场景
快速发现适合特定任务的 Hermes Skills，避免重复造轮子。

---

### 5. Hermes Control Interface
**来源**：社区贡献 (@xaspx)  
**链接**：https://github.com/xaspx/hermes-control  
**类型**：管理仪表盘

#### 核心内容
- 自托管 Web 仪表盘
- 统一调度多个 Agent 实例
- 长程任务管理与监控
- 记忆系统可视化

#### 核心优势
将分散的 Agent 会话整合到统一界面，便于管理长期运行的任务与跨会话记忆。

---

### 6. Hermes Skill Factory
**来源**：社区贡献 (@Romanescu11)  
**链接**：https://github.com/Romanescu11/hermes-skill-factory  
**类型**：技能生成工具

#### 核心内容
- 通过任务复盘自动生成新技能
- 将成功的工作流自动提炼为可复用 Skill
- 一键安装到本地 Hermes

#### 核心优势（作者洞察）
"武器自造" —— 每次完成复杂任务后，系统自动分析步骤并生成 Skill 文件，实现知识沉淀。

---

### 7. Maestro（指挥官框架）
**来源**：社区贡献 (@ReinaMacCredy)  
**链接**：https://github.com/ReinaMacCredy/Maestro  
**类型**：多 Agent 协作框架

#### 核心内容
- 基于 Beads 架构的指挥官框架
- 跨 Agent 协作与任务编排
- 结构化记忆管理

#### 适用场景
构建复杂多 Agent 系统，如研究团队、内容工厂等需要协调多个角色的场景。

---

### 8. Hermes Agent Camel
**来源**：社区贡献 (@nativ3ai)  
**链接**：https://github.com/nativ3ai/hermes-camel  
**类型**：安全增强版

#### 核心内容
- 内置信任边界与安全协议
- 适合生产环境的防护机制
- 权限管理与审计日志

#### 适用场景
企业部署或处理敏感数据时，需要额外安全层级的生产环境。

---

### 9. Hermes HUD
**来源**：社区贡献 (@joeynyc)  
**链接**：https://github.com/joeynyc/hermes-hud  
**类型**：TUI 监控工具

#### 核心内容
- 基于 Textual 的终端 UI
- 实时可视化 Agent 意识流
- 内存状态监控
- 工具调用追踪

#### 适用场景
喜欢终端操作的用户，实时监控 Agent 思考过程与资源消耗。

---

### 10. Hermes Alpha
**来源**：社区贡献 (@kaminocorp)  
**链接**：https://github.com/kaminocorp/hermes-alpha  
**类型**：部署模板

#### 核心内容
- 一键部署模板
- 简化云端环境配置
- 快速原型开发脚手架

#### 适用场景
想要快速在云服务器（AWS/GCP/Azure）上部署 Hermes 的用户。

---

### 11. Awesome Hermes Agent
**来源**：社区维护 (@0xNyk)  
**链接**：https://github.com/0xNyk/awesome-hermes  
**类型**：精选列表

#### 核心内容
- 社区驱动的精选插件列表
- 优质提示词集合
- 教程与案例汇总

---

## 合集B详细内容：入门教程

### 1. Hermes Agent 安装教程
**作者**：@eternityspring  
**链接**：https://x.com/eternityspring/status/2041735065865220416  
**类型**：安装指南

#### 核心内容
- 一行命令安装流程
- 常见配置参数说明
- 多平台支持（macOS/Linux/Windows WSL）

#### 适用人群
初次接触 Hermes 的小白用户，看完就能独立完成安装。

---

### 2. Windows 本地部署保姆教程
**作者**：@xinchne_eth  
**链接**：https://x.com/xinchne_eth/status/2046075258277613938  
**类型**：Windows 部署指南

#### 核心内容
- 针对 Windows 环境的详细说明
- WSL2 部署方法步骤
- Windows 特有注意事项

#### 适用人群
Windows 用户，之前找不到详细 Windows 教程的用户。

---

### 3. 云服务器部署方案保姆级教程
**作者**：@congge918  
**链接**：https://x.com/congge918/status/2043172874404725124  
**类型**：云端部署指南

#### 核心内容
- 以腾讯云为例的完整流程
- 购买服务器后运行安装脚本
- 部署完成后云端长期运行配置

#### 核心亮点
10分钟搞定云端部署，适合需要 24/7 运行的场景。

---

### 4. 上手 Hermes Agent 后建议先尝试的十件事情
**作者**：@LufzzLiz  
**链接**：https://x.com/LufzzLiz/status/2042237123865297267  
**类型**：快速上手清单

#### 核心内容
安装 Hermes 后可立即尝试的功能：
1. 配置 SOUL.md 个性化角色
2. 启用记忆系统
3. 设置浏览器工具
4. 配置 MCP 服务器
5. 探索内置 Skills
6. 配置模型提供商
7. 设置计划任务 (cron)
8. 配置通知渠道
9. 尝试浏览器自动化
10. 设置文档索引

---

### 5. 一行命令跑起 Hermes Agent：Ollama 原生集成
**作者**：@Lonely__MH  
**链接**：https://x.com/Lonely__MH/status/2045425574618034324  
**类型**：本地模型集成

#### 核心内容
- Ollama 本地模型集成命令
- 离线环境运行配置
- 本地大模型推荐

#### 适用场景
希望完全离线运行、保护隐私或不希望产生 API 费用的用户。

---

### 6. 新手教程：Hermes 接入即梦 CLI
**作者**：@MrLarus  
**链接**：https://x.com/MrLarus/status/2042895934460211442  
**类型**：工具集成教程

#### 核心内容
- 接入即梦 (Dreamina) CLI 的具体步骤
- 自动提交提示词并轮询生成结果
- 批量处理图片和视频任务

#### 适用场景
需要 Hermes Agent 自动完成 AI 生图、生视频工作流的用户。

---

### 7. 如何在 Hermes 中构建多智能体团队
**作者**：@NeoAIForecast  
**链接**：https://x.com/NeoAIForecast/status/2043455838459920718  
**类型**：多 Agent 配置指南

#### 核心内容
- 使用 Profile 功能创建多个角色 Agent
- 每个角色拥有独立记忆和技能
- 主 Agent 协调任务分配的团队协作模式

#### 核心亮点
一个人就是一支团队：研究员、写手、设计师角色分工协作。

---

### 8. 只需 10 步 HERMES 配上 NVIDIA 免费 Minimax-m2.7 大模型
**作者**：@PierceZhang34  
**链接**：https://x.com/PierceZhang34/status/2045521315646599471  
**类型**：免费模型配置

#### 核心内容
- 注册 NVIDIA NIM 平台
- 生成 API Key
- 配置 Hermes 调用 Minimax-m2.7

#### 核心亮点
免费使用 Minimax-m2.7（性能接近 GPT-4），零成本体验高质量模型。

---

### 9. Hermes Agent 从中级到高级进阶指南
**作者**：@BTCqzy1（爱丽丝呀）  
**链接**：https://x.com/BTCqzy1/status/2044259795499450414  
**类型**：进阶指南

#### 核心内容
- 记忆管理深度优化
- 多 Agent 协作进阶配置
- 生产部署后台运行方式

#### 适用人群
已完成基础配置，希望进一步提升 Hermes 生产力的用户。

---

### 10. 一文理清！Hermes 全部高阶工具配置
**作者**：@ResearchWang  
**链接**：https://x.com/ResearchWang/status/2045812932538438001  
**类型**：配置清单

#### 核心内容
- SOUL.md 文件完整配置
- 技能管理系统详解
- 平台接入（Linear/GitHub/Notion 等）
- 逐项检查清单

#### 适用场景
作为 Hermes 高阶配置的「查漏清单」，确保所有功能都正确启用。

---

## 资源汇总

### GitHub 仓库汇总

| 项目名称 | 链接 | 简介 |
|----------|------|------|
| Hermes Agent | https://github.com/NousResearch/hermes-agent | 官方核心仓库 |
| Hermes-Wiki | https://github.com/cclank/Hermes-Wiki | 自动生成的文档 Wiki |
| Hermes Atlas | https://github.com/ksimback/hermes-atlas | 80+ 工具生态地图 |
| Hermes Control | https://github.com/xaspx/hermes-control | 自托管管理仪表盘 |
| Hermes Skill Factory | https://github.com/Romanescu11/hermes-skill-factory | 自动技能生成 |
| Maestro | https://github.com/ReinaMacCredy/Maestro | 多 Agent 指挥官框架 |
| Hermes Camel | https://github.com/nativ3ai/hermes-camel | 安全增强版 |
| Hermes HUD | https://github.com/joeynyc/hermes-hud | TUI 监控终端 |
| Hermes Alpha | https://github.com/kaminocorp/hermes-alpha | 云端部署模板 |
| Awesome Hermes | https://github.com/0xNyk/awesome-hermes | 社区精选列表 |

### 值得关注的人/账号

| 账号 | 简介 |
|------|------|
| @BTCqzy1（爱丽丝呀！） | 交易员/技术派投研，分享 Hermes 进阶玩法 |
| @Jason23818126（摸鱼局长） | AI/Web3/美股超级个体实践者，保姆级教程 |
| @eternityspring | 一行命令安装教程作者 |
| @ResearchWang | 高阶配置清单作者 |

---

## 建议学习/使用路径

### 路径A：从零开始（新用户）
1. 先看 **合集B 教程1**（@eternityspring 安装教程）完成安装
2. 按 **合集B 教程4**（十件事情清单）配置基础功能
3. 参考 **合集B 教程10** 完成高阶配置
4. 探索 **合集A** 的生态项目扩展能力

### 路径B：进阶进化（已有基础）
1. 部署 **Hermes Skill Factory** 实现技能自造
2. 配置 **Maestro** 构建多 Agent 团队
3. 搭建 **Hermes Control** 统一管理所有实例
4. 关注 @BTCqzy1 获取最新进阶玩法

### 路径C：生产部署（团队/企业）
1. 使用 **Hermes Camel** 确保安全边界
2. 部署 **Hermes Alpha** 到云端
3. 配置 **Hermes HUD** 监控运行状态
4. 结合 **Hermes Atlas** 管理技能库

---

## 附录：快速参考

### 常用命令
```bash
# 一行命令安装 Hermes Agent
pip install hermes-agent

# 启动 Hermes
hermes

# 配置 MCP 服务器
hermes mcp add <server-name>

# 安装技能
hermes skill install <skill-name>
```

### 配置文件位置
- SOUL.md：`~/.config/hermes/SOUL.md`
- 配置文件：`~/.config/hermes/config.yaml`
- Skills 目录：`~/.hermes/skills/`

### 免费模型推荐
- **NVIDIA Minimax-m2.7**：需 NIM 平台 API Key
- **Ollama 本地模型**：完全离线，推荐 llama3/phi4

---

*来自翡冷翠*
