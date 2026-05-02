# Superpowers

> 个人知识工程与精选 Skills 仓库：从 X、Reddit、Newsletter、GitHub 和开源社区捕获高信号内容，沉淀为可复用的方法、文档与少量经过验证的 Hermes Skills。

本仓库不是 `~/.hermes/skills` 的完整镜像。完整 live skill registry 以本机 Hermes 环境为准：

```bash
/Users/marovole/.hermes/skills
```

本仓库的定位是：

1. 保存高信号 AI / Product / Biohacking / Agent 工作流文档
2. 存放少量已经推广为公共资产的精选 skills
3. 记录 Superpowers 技能体系的分类、审计、重构和吸收过程
4. 作为个人能力复利系统的 GitHub 版本化出口

---

## 项目主旨

从外部信号中提炼可执行能力。目标不是收藏链接，而是完成这条链路：

```text
捕获 Source → 研究 Research → 实验 Experiment → 固化 Skill/Workflow → 复用 Reuse
```

原则：

- 信号 > 噪音：只收集经过验证或高潜力的 AI 应用
- 文档即代码：所有研究过程与结论必须可复现、可版本化
- Skill 优先：有复用价值的流程最终沉淀为 Hermes skill 或工作流文档
- 精选入库：repo/skills 只放 promoted skills，不追求镜像全部本地 skills

---

## 当前仓库结构

```text
marovole-Superpowers/
├── README.md
├── docs/                 # 主体：研究、教程、工具评估、工作流文档
├── research/             # 研究报告与专题分析
└── skills/               # 精选 promoted Hermes skills，不是完整 registry
```

当前 promoted skills：

| Skill | 路径 | 用途 |
|---|---|---|
| dokobot | [skills/dokobot/](skills/dokobot/) | 用真实 Chrome 浏览器读取 JS-heavy / login-walled 页面 |
| link2doc | [skills/research/link2doc/](skills/research/link2doc/) | 从链接/来源整理文档并提交到 GitHub 的内容策展流程 |

完整 live registry 请查看本机：

```bash
find /Users/marovole/.hermes/skills -name SKILL.md
```

---

## 关键文档入口

### Skills 体系与 Hermes Agent OS

| 文档 | 说明 |
|---|---|
| [Superpowers Skills Health Map](docs/superpowers-skills-health-map-2026-05-02.md) | 当前 repo 与本地 Hermes skills 的健康检查、差异和后续建议 |
| [Hermes Skills Phase 3 Local Refactor](docs/hermes-skills-phase3-local-refactor-2026-05-02.md) | 本地 `~/.hermes/skills` 中 creative 与 software-development 拥挤分类拆分记录 |
| [Superpowers Skills 分类分析](docs/superpowers-skills-classification-analysis-2026-05-01.md) | 2026-05-01 skills 分类重构分析 |
| [Skills 重构完成报告](docs/REFACTORING_SUMMARY_2026-05-01.md) | `~/.hermes/skills` 分类优化总结 |
| [Hermes Skill Factory 分析](docs/hermes-skill-factory-analysis-2026-05-01.md) | 自动从工作流生成 skill 的机制研究 |
| [Hermes Agent 资源合集](docs/hermes-agent-resource-compilation-2026-05-01.md) | Hermes 生态资源整理 |
| [Hermes 多 Agent 设置教程](docs/hermes-multi-agent-setup-tutorial.md) | 多 Agent 协作配置 |

### Prompt / Agent / Workflow

| 文档 | 说明 |
|---|---|
| [GPT-5.5 Prompting Guide](docs/gpt-5.5-prompting-guide-2026-04-30.md) | 新一代模型 outcome-first prompt 标准来源 |
| [SkillClaw Agent Skill Evolution](docs/skillclaw-ai-agent-skill-evolution-2026-05-02.md) | Agent 技能进化机制 |
| [Waza Skills System Tutorial](docs/waza-skills-system-tutorial-2026-04-30.md) | Waza 技能体系教程 |
| [Claude Code Burn Token Workflow](docs/claude-code-burn-token-workflow-2025-04-30.md) | 夜间消耗 idle quota 的自主研究工作流 |
| [OpenClaw Browser Automation Guide](docs/openclaw-browser-automation-guide.md) | 浏览器自动化工具研究 |

### 内容与发布工具

| 文档 | 说明 |
|---|---|
| [md2wechat Skill Complete Guide](docs/md2wechat-skill-complete-guide-2026-04-27.md) | Markdown 到公众号排版发布 |
| [Markdown to Image Cards](docs/md-poster-markdown-to-image-cards-2026-04-29.md) | Markdown 转社交媒体卡片 |
| [HyperFrames AI Video Guide](docs/hyperframes-ai-video-guide.md) | AI 视频内容工具 |
| [AI Content Tools: HyperFrames + ChatPDF](docs/ai-content-tools-hyperframes-chatpdf-2026-05-02.md) | 内容工具指南 |

### GPT-image / Creative

| 文档 | 说明 |
|---|---|
| [Awesome GPT-image-2 Curation](docs/awesome-gpt-image-2-curation.md) | GPT-image-2 案例与提示词策展 |
| [GPT Image 2 Prompts Collection](docs/gpt-image-2-prompts-collection-2026-04-24.md) | GPT-image-2 提示词合集 |
| [Concept Poster Prompt Framework](docs/concept-poster-prompt-framework-2026-04-27.md) | 概念海报 prompt 框架 |
| [ChatGPT JSON Style Guide](docs/chatgpt-json-style-guide.md) | JSON 风格协议 |

---

## 工作流

### 内容策展

```text
source link/thread → link2doc → docs/*.md → review → git commit/push
```

默认输出位置：`docs/`

### Skill 吸收

```text
docs candidate → 判断是否可执行/可复用 → 对比现有 ~/.hermes/skills → create/patch skill → 必要时 promoted 到 repo/skills
```

注意：

- 纯信息清单不一定转 skill
- 已有 skill 覆盖时优先 patch，不重复创建
- 新 skill 应遵循 GPT-5.5 Prompt Strategy：Goal → Success Criteria → Constraints → Stop Rules → Verify

### 仓库维护

```bash
git pull --ff-only
# 新增或更新 docs/ 与 promoted skills
git status --short
git add <files>
git commit -m "docs: ..." 或 "skills: ..."
git push
```

---

## 与本地 Hermes Skills 的关系

本机 Hermes 使用的完整技能库位于：

```bash
/Users/marovole/.hermes/skills
```

Superpowers 仓库只保存：

- 重要研究和教程文档
- 值得公开/迁移/复用的 promoted skills
- skills 分类、审计和重构报告
- 外部工具/方法论的吸收记录

这意味着 README 不再列出 120+ live skills 的完整索引，避免 GitHub 仓库结构与本地 Hermes 运行时状态发生误导性不一致。

---

## 更新原则

1. 新内容优先进入 `docs/`
2. 只有经过验证、可复用、适合共享的能力才进入 `skills/`
3. 每次 skills 结构变动后更新健康检查或相关说明
4. 署名保持个人身份：来自翡冷翠

---

*来自翡冷翠* | 持续更新于 2026-05-02
