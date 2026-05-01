# Superpowers Skills 分类分析与优化建议

> 分析时间：2026-05-01  
> 分析对象：marovole-Superpowers 仓库 (120+ skills)  
> 参考标准：Hermes Atlas (已下架，仅基于历史数据) + Skill Factory 分类  
> 来自翡冷翠

---

## 当前分类现状

### 现有分类结构

```
Superpowers/
├─── autonomous-ai-agents/        # 9 skills
├─── creative/                   # 25 skills (最大类)
├─── data-science/               # 1 skill
├─── devops/                     # 11 skills
├─── dokobot/                    # 1 skill
├─── email/                      # 3 skills
├─── gaming/                     # 2 skills
├─── github/                     # 6 skills
├─── inference-sh/               # 1 skill
├─── kami-design-system/         # 1 skill
├─── leisure/                    # 1 skill
├─── mcp/                        # 2 skills
├─── media/                      # 6 skills
├─── minimax-api/                # 1 skill
├─── mlops/                      # 39 skills (最大类，含子分类)
├─── monthly-dev-report/         # 1 skill
├─── note-taking/                # 2 skills
├─── productivity/               # 20 skills (重点需优化)
├─── red-teaming/                # 1 skill
├─── research/                   # 14 skills
├─── smart-home/                 # 1 skill
├─── social-media/               # 3 skills
├─── software-development/       # 16 skills
└─── yuanbao/                    # 1 skill

总计: 40+ 分类，120+ skills
```

---

## 发现的问题

### 问题 1：productivity 太膨胀

`productivity/` 包含 20 个技能，但跨度过大：
- 内容整理 (link2doc, url-to-markdown)
- 文档处理 (nano-pdf, ocr)
- 发布工具 (md2wechat, web-crawler)
- 生产力工具 (airtable, notion, google-workspace)
- 任务管理 (kanban-orchestrator, night-research-cron)
- 知识管理 (content-absorption-framework)

### 问题 2：重叠分类

- `kanban-orchestrator` 同时在 `devops/` 和 `productivity/`
- `url-to-markdown` 同时在 `productivity/` 和 `research/`

### 问题3：naming 不一致

- 以 `hermes-` 前缀命名的 skills 与实际功能不匹配：
  - `hermes-health-check` → 应为 `agent-health-check`
  - `hermes-deployment` → 应为 `agent-deployment`

### 问题4：单一技能独立分类

多个分类只有 1 个 skill，过度拆分：
- `dokobot/`, `inference-sh/`, `kami-design-system/`, `minimax-api/`, `monthly-dev-report/`, `yuanbao/`

---

## 优化方案

### 方案 A：基于功能领域的分类重构

```
superpowers/
├─── agent-core/               # Agent 核心能力
│   ├─── hermes-agent (重命名: agent-config)
│   ├─── hermes-health-check (重命名: agent-health-check)
│   ├─── hermes-operating-system (重命名: agent-workflow-system)
│   ├─── agent-monitoring-dashboard
│   ├─── agent-security-boundaries
│   ├─── agent-self-evolution
│   └─── agent-handoff-document
├─── agent-orchestration/        # 多 Agent 协作
│   ├─── subagent-driven-development
│   ├─── neumina-agent-architecture
│   ├─── cmux-multi-agent-terminal
│   ├─── claude-code
│   ├─── codex
│   ├─── opencode
│   └─── ai-coding-agent-model-config
├─── agent-skills/             # Skill 开发与管理
│   ├─── hermes-agent-skill-authoring
│   ├─── gpt-5.5-prompt-strategy
│   ├─── writing-plans
│   └─── nuwa-cognitive-distillation
├─── content-creation/         # 内容生成
│   ├─── creative/ → 所有图片/视频/音乐技能
│   └─── media/ → youtube-content, video-content-automation
├─── content-curation/         # 内容整理
│   ├─── link2doc
│   ├─── url-to-markdown
│   ├─── content-absorption-framework
│   ├─── night-research-cron
│   └─── blogwatcher
├─── content-publishing/        # 内容发布
│   ├─── md2wechat
│   ├─── markdown-to-social-cards
│   └─── social-media/
├─── data-ml/                  # 数据与 ML
│   ├─── data-science/
│   ├─── mlops/
│   └─── minimax-api (合并到 inference/)
├─── dev-deployment/            # 开发部署
│   ├─── devops/ (删除 kanban-orchestrator)
│   ├─── github/
│   ├─── software-development/
│   └─── cloudflare-deployment
├─── inference/                 # 模型推理
│   ├─── inference-sh-cli
│   └─── minimax-api (合并至此)
├─── knowledge-management/      # 知识管理
│   ├─── note-taking/
│   ├─── research/
│   └─── llm-wiki
├─── productivity-tools/        # 生产力工具
│   ├─── airtable
│   ├─── notion
│   ├─── google-workspace
│   ├─── linear
│   └─── maps
├─── task-management/          # 任务管理
│   ├─── kanban-orchestrator
│   ├─── kanban-worker
│   ├─── monthly-dev-report
│   └─── plan
├─── document-processing/       # 文档处理
│   ├─── nano-pdf
│   ├─── ocr-and-documents
│   ├─── pdf-generation-fallbacks
│   ├─── powerpoint
│   └─── web-crawler
├─── external-tools/            # 外部工具
│   ├─── dokobot (合并)
│   ├─── mcp/
│   ├─── kami-design-system (合并)
│   ├─── yuanbao (合并)
│   ├─── smart-home/
│   └─── gaming/
└─── security-research/         # 安全与研究
    ├─── red-teaming/
    └─── domain-intel
```

### 方案 B：渐进式优化（推荐）

不重构代码，仅优化组织：

#### Step 1: 合并单一技能分类

```bash
# 目标：将以下单一 skill 分类合并

# 方案 A：合并到 mcp/
mcp/
  ├─── mcporter
  ├─── native-mcp
  └─── external-tools/          # 从这里移动
      ├─── dokobot
      ├─── kami-design-system
      └─── yuanbao

# 方案 B：合并到 inference/
inference/
  ├─── inference-sh-cli
  ├─── minimax-api               # 从单独分类移入
  └─── external-inference/        # 其他模型接入
```

#### Step 2: 重命名 hermes-* skills

```bash
# 旧名称 → 新名称
hermes-agent              →  agent-configuration
hermes-operating-system   →  agent-workflow-system
hermes-health-check       →  agent-health-check
hermes-deployment         →  agent-deployment
debugging-hermes-tui-commands →  debugging-tui-commands
```

#### Step 3: 解决重叠分类

```bash
# 移除重叠的 symlink
# 保留 canonical 位置，删除副本

# kanban-orchestrator
# 保留在 productivity/
# 从 devops/ 移除

# url-to-markdown
# 保留在 productivity/ (link2doc 依赖它)
# 从 research/ 移除
```

#### Step 4: productivity 内部重组

```
productivity/
├─── task-management/           # 移入：kanban-*
├─── content-curation/          # 移入：link2doc, url-to-markdown, content-absorption
├─── research-automation/       # 移入：night-research-cron, blogwatcher
├─── workspace-integration/     # 保留：notion, airtable, google-workspace, linear
├─── document-processing/       # 移入：nano-pdf, ocr, pdf-generation, powerpoint
└─── web-automation/            # 移入：web-crawler
```

---

## 对比分析：与行业标准

### Hermes Atlas 的分类思路（参考）

```
Hermes Atlas (历史分类)
├─── software-development/      # 代码、Git、测试、调试
├─── devops/                   # 部署、CI/CD、监控
├─── data-science/             # 分析、可视化、ML
├─── mlops/                    # 训练、部署、监控
├─── productivity/             # 文档、协作、自动化
├─── creative/                 # 设计、内容、多媒体
├─── research/                 # 搜索、论文、数据收集
├─── communication/            # 邮件、消息、通知
└─── integration/              # API、MCP、工具链接
```

### 与我的实际分类对比

| Atlas 分类 | 我的对应分类 | 差异 |
|-----------|-------------|------|
| software-development | software-development/ | 匹配 |
| devops | devops/ | 匹配 |
| data-science | data-science/ | 匹配 |
| mlops | mlops/ | 匹配 |
| productivity | productivity/ | 我的更膨胀 |
| creative | creative/ | 我的更细化 |
| research | research/ | 匹配 |
| communication | email/, social-media/ | 我拆分了 |
| integration | mcp/ | 我更聚焦 |

### 我的优势

1. **更细的子分类**：如 mlops/cloud, mlops/training 等
2. **Agent 专用分类**：autonomous-ai-agents/ 是 Atlas 没有的
3. **工作流优化**：link2doc 是行业领先的模式

### 需改进的地方

1. **productivity 膨胀**：需要拆分
2. **缺少 integration 分类**：MCP 工具集中但不够
3. **重叠问题**：需要 canonical path

---

## 具体行动建议

### 第一阶段（立即执行）

1. **重命名 hermes-* skills**
   ```bash
   # 编辑 SKILL.md 前置数据
   # 修改 name 字段
   # 更新所有引用的地方
   ```

2. **移除重叠分类**
   ```bash
   # 从 devops/ 删除 kanban-orchestrator
   # 从 research/ 删除 url-to-markdown
   # 确保 canonical path 唯一
   ```

3. **合并单一技能分类**
   ```bash
   # 创建 external-tools/ 分类
   # 移入 dokobot, kami-design-system, yuanbao
   # 合并 inference-sh/ 和 minimax-api 到 inference/
   ```

### 第二阶段（规划中）

1. **productivity 内部重组**
   - 需要讨论：如何拆分最合理
   - 方案：按功能领域 vs 按工作流阶段

2. **创建 integration 分类**
   - 整合 mcp/ 和其他工具链接 skill
   - 如 future的 Skill Factory 插件系统

3. **文档化分类策略**
   - 在 README 中明确分类说明
   - 提供分类体系图

---

## 附录：技能命名规范

### 建议的 naming convention

```
# 格式：{domain}-{action}-{target}

# 好例子
agent-health-check       # agent 领域，health check 动作
content-url-to-markdown  # content 领域，url 转 markdown 动作
code-review-pr           # code 领域，review PR 动作
mlops-gguf-quantization  # mlops 领域，gguf 量化动作

# 差例子
hermes-agent            # 前缀无意义
awesome-tools           # 太泛泛
setup                   # 太模糊
```

### category 标签规范

```yaml
# 前置数据中的 category 字段
name: skill-name
category: | # 从以下选择
  - agent-core          # Agent 核心
  - agent-orchestration # 多Agent协作
  - agent-skills        # Skill开发
  - content-creation    # 内容生成
  - content-curation    # 内容整理
  - content-publishing  # 内容发布
  - data-ml            # 数据与ML
  - dev-deployment     # 开发部署
  - inference          # 模型推理
  - knowledge-management # 知识管理
  - productivity-tools  # 生产力工具
  - task-management    # 任务管理
  - document-processing # 文档处理
  - external-tools     # 外部工具
  - security-research  # 安全研究
```

---

## 结论

当前 Superpowers 仓库的分类体系已经相对完善，但存在以下改进空间：

1. **立即执行**：重命名 hermes-* 和移除重叠分类
2. **短期规划**：合并单一技能分类，减少分类数量
3. **中期优化**：refactor productivity/ 内部结构
4. **长期规划**：考虑基于 Skill Factory 的自动分类

---

*来自翡冷翠*
