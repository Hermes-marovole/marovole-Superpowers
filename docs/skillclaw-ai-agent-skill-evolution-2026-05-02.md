# SkillClaw - AI 智能体技能自动进化与沉淀系统

> 来源：[GitHubDaily @GitHub_Daily](https://x.com/github_daily/status/2050206139598721028)  
> 项目地址：[github.com/AMAP-ML/SkillClaw](https://github.com/AMAP-ML/SkillClaw)  
> 整理时间：2026-05-02  
> 来自翡冷翠

---

## 执行摘要

**SkillClaw** 是一个让 AI 智能体技能自动进化、沉淀并支持跨设备/跨智能体共享的开源框架。它能够在后台静默地从每次用户与智能体的交互中提炼可复用的技能，自动完成去重、优化和归档，无需用户额外操作。

| 项目信息 | 详情 |
|---------|------|
| **核心功能** | AI 智能体技能的自动进化、去重、优化与跨实例共享 |
| **兼容性** | Hermes、OpenClaw、Codex、Claude Code、QwenPaw、IronClaw、PicoClaw、ZeroClaw 等 |
| **技术栈** | Python 3.10+、OpenAI-compatible API / AWS Bedrock |
| **许可协议** | MIT |
| **论文** | [arXiv:2604.08377](https://arxiv.org/abs/2604.08377) |

---

## 核心亮点

### 1. 零感知技能进化
用户只需像往常一样与智能体对话，SkillClaw 在后台自动完成：
- 从会话中提炼可复用技能
- 技能去重与合并
- 质量自动优化
- 归档整理

### 2. 跨智能体技能共享
- **多 Agent 统一技能库**：多个不同用途的 Agent 共享同一技能库，前端 Agent 学会的 React 模式可自动提升后端 Agent 的 API 设计能力
- **多设备无缝同步**：家庭/学校/工作环境的 Agent 实例共享技能，换设备无需重新开始

### 3. 集体进化机制
团队场景下的核心优势：
- 用户 A 踩过的坑 → 提炼成技能 → 用户 B/C/D 直接受益
- N 个用户的经验汇入同一进化循环
- 真正实现"一次犯错，全员避雷"

---

## 系统架构

### 双组件设计

```
┌─────────────────┐     ┌─────────────────┐
│   Client Proxy  │────▶│  Evolve Server  │
│  (本地 API 代理)  │     │  (技能进化服务)  │
└─────────────────┘     └─────────────────┘
         │                        │
         ▼                        ▼
┌─────────────────────────────────────────┐
│         Shared Storage Layer            │
│    (Alibaba OSS / S3 / Local FS)        │
└─────────────────────────────────────────┘
```

**1. Client Proxy（客户端代理）**
- 拦截 Agent 的 API 请求 (`/v1/chat/completions`, `/v1/messages`)
- 记录会话数据并管理本地技能库
- 单用户即可开始使用

**2. Evolve Server（进化服务器）**
- 从共享存储读取会话数据
- 执行技能进化/创建
- 支持两种引擎：
  - `workflow`：固定 3 阶段 LLM 流水线（Summarize → Aggregate → Execute）
  - `agent`：OpenClaw 驱动的 Agent 工作区直接编辑

---

## 部署模式

### 模式 A：单用户本地使用
适合个人开发者，一台机器上运行完整闭环：

```bash
# 1. 安装
git clone https://github.com/AMAP-ML/SkillClaw.git && cd SkillClaw
bash scripts/install_skillclaw.sh
source .venv/bin/activate

# 2. 配置向导
skillclaw setup
# - 选择 CLI agent（可选 hermes/codex/claude/none）
# - 设置本地技能目录（默认 ~/.skillclaw/skills）
# - 启用本地共享存储（如需进化服务器）

# 3. 启动服务
skillclaw start --daemon
skillclaw status
```

### 模式 B：加入现有共享组
适合团队协作，仅需安装客户端：

```bash
skillclaw config sharing.enabled true
skillclaw config sharing.backend oss
skillclaw config sharing.endpoint https://oss-cn-hangzhou.aliyuncs.com
skillclaw config sharing.bucket my-skillclaw-bucket
skillclaw config sharing.access_key_id "$OSS_ACCESS_KEY_ID"
skillclaw config sharing.secret_access_key "$OSS_ACCESS_KEY_SECRET"
skillclaw config sharing.group_id my-group
skillclaw config sharing.user_alias alice
skillclaw config sharing.auto_pull_on_start true

skillclaw start --daemon
skillclaw skills pull
```

### 模式 C：运行进化服务器（团队管理员）

```bash
git clone https://github.com/AMAP-ML/SkillClaw.git && cd SkillClaw
bash scripts/install_skillclaw_server.sh
source .venv-server/bin/activate

# 启动 workflow 引擎
skillclaw-evolve-server --port 8787 --interval 300 \
  --storage-backend oss \
  --oss-endpoint "$EVOLVE_STORAGE_ENDPOINT" \
  --oss-bucket "$EVOLVE_STORAGE_BUCKET" \
  --group-id my-group

# 或使用 validated 模式（需客户端验证）
EVOLVE_PUBLISH_MODE=validated \
EVOLVE_VALIDATION_REQUIRED_RESULTS=1 \
EVOLVE_VALIDATION_REQUIRED_APPROVALS=1 \
skillclaw-evolve-server ...
```

---

## 与主流 Agent 框架集成

### Hermes 集成
```bash
skillclaw setup  # 选择 hermes
skillclaw start --daemon

# 验证
hermes chat -Q -m skillclaw-model -q "Reply with exactly HERMES_SKILLCLAW_OK"
```
- 自动配置 `~/.hermes/config.yaml` 指向本地代理
- 技能库存储于 `~/.hermes/skills`
- 提供 `skillclaw doctor hermes` 诊断命令

### Codex / Claude Code 集成
```bash
skillclaw setup  # 选择 codex 或 claude
# 自动配置代理和默认技能目录
```

---

## 技能管理命令

| 命令 | 功能 |
|------|------|
| `skillclaw skills pull` | 下载共享技能 |
| `skillclaw skills push` | 上传本地技能 |
| `skillclaw skills sync` | 双向同步 |
| `skillclaw skills list-remote` | 浏览共享技能 |
| `skillclaw skills list` | 查看本地技能 |

---

## 可视化仪表盘（新增功能）

2026/04/22 新增双语仪表盘功能，支持：
- 本地/共享技能对比检查
- 候选验证任务状态
- 已发布技能版本历史
- 会话追踪

```bash
skillclaw dashboard sync
skillclaw dashboard serve --host 127.0.0.1 --port 3791
# 访问 http://127.0.0.1:3791
```

---

## 最新动态

| 日期 | 更新内容 |
|------|----------|
| 2026/04/22 | 新增双语仪表盘 (`skillclaw dashboard`) |
| 2026/04/20 | 新增 Codex / Claude Code 集成 |
| 2026/04/17 | 新增 QwenPaw 集成、完整 Hermes 集成 |
| 2026/04/14 | 微信讨论组上线 |
| 2026/04/11 | 入选 Hugging Face Daily Papers #2 |
| 2026/04/10 | 正式开源 |

---

## 引用信息

```bibtex
@article{ma2026skillclaw,
  title={SkillClaw: Let Skills Evolve Collectively with Agentic Evolver},
  author={Ma, Ziyu and Yang, Shidong and Ji, Yuxiang and Wang, Xucong and Wang, Yong and Hu, Yiming and Huang, Tongwen and Chu, Xiangxiang},
  journal={arXiv preprint arXiv:2604.08377},
  year={2026}
}
```

---

## 相关资源

| 资源 | 链接 |
|------|------|
| **GitHub 仓库** | https://github.com/AMAP-ML/SkillClaw |
| **论文 (arXiv)** | https://arxiv.org/abs/2604.08377 |
| **论文 (PDF)** | https://arxiv.org/pdf/2604.08377 |
| **Hugging Face** | https://huggingface.co/papers/2604.08377 |
| **中文文档** | [README_ZH.md](https://github.com/AMAP-ML/SkillClaw/blob/main/assets/README_ZH.md) |
| **技术基础** | [MetaClaw](https://github.com/aiming-lab/MetaClaw)、[WildClawBench](https://github.com/InternLM/WildClawBench)、[OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) |

---

*来自翡冷翠*
