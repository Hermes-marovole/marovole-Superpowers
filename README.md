# Superpowers

> 本项目是不断探索前沿 AI 应用和个人能力进化的长期项目。
> 一个持续学习、研究和内化前沿 AI 能力的个人知识工程。

## 项目主旨

从 X、Reddit、Newsletter 以及各类开源社区中捕获高信号内容，将其转化为可复用的企业级技能（Skills）。目标不是收藏，而是**内化**——让每一项经过验证的 AI 应用方法论，都成为团队肌肉记忆的一部分。

## 工作流

```
捕获 (Source) → 研究 (Research) → 实验 (Experiment) → 固化 (Skill)
      ↑                                                            ↓
      └────────────── 持续迭代反馈 ◄──────────────────────────────┘
```

## 原则

- **信号 > 噪音**：只收集经过验证或高潜力的 AI 应用
- **文档即代码**：所有研究过程与结论必须可复现、可版本化
- **Skill 优先**：最终产出是可被团队直接调用的能力，而非静态笔记

---

## Skills 分类索引

本仓库包含 **120+ 个 Hermes Skills**，按功能领域组织：

### 🤖 Agent 核心
| Skill | 描述 |
|-------|-------|
| [agent-configuration](autonomous-ai-agents/agent-configuration/) | Hermes Agent 配置、扩展与错误排除 |
| [agent-workflow-system](autonomous-ai-agents/agent-workflow-system/) | 翡冷翠的 Hermes 工作系统总控 |
| [agent-health-check](devops/agent-health-check/) | 审计 Hermes 配置栈健康度 |
| [agent-deployment](devops/agent-deployment/) | Hermes 部署指南 |
| [agent-self-evolution](autonomous-ai-agents/agent-self-evolution/) | Agent 自我进化系统 |
| [agent-handoff-document](productivity/agent-handoff-document/) | 创建 Agent 交接/入职文档 |

### 🎭 Agent 协作与编排
| Skill | 描述 |
|-------|-------|
| [subagent-driven-development](autonomous-ai-agents/subagent-driven-development/) | 通过子代理执行计划 |
| [neumina-agent-architecture](autonomous-ai-agents/neumina-agent-architecture/) | Neumina 6 智能体产品架构 |
| [claude-code](autonomous-ai-agents/claude-code/) | 委派编码任务给 Claude Code |
| [codex](autonomous-ai-agents/codex/) | 委派编码任务给 OpenAI Codex |
| [opencode](autonomous-ai-agents/opencode/) | 委派给 OpenCode CLI |

### 📜 任务管理
| Skill | 描述 |
|-------|-------|
| [kanban-orchestrator](task-management/kanban-orchestrator/) | Kanban 看板任务分解与协调 |
| [kanban-worker](task-management/kanban-worker/) | Kanban 工作者执行流程 |
| [night-research-cron](task-management/night-research-cron/) | 夜间自动研究任务 |
| [content-absorption-framework](task-management/content-absorption-framework/) | 内容吸收框架 |
| [plan](software-development/plan/) | 创建 Markdown 执行计划 |

### ✍️ 内容整理与发布
| Skill | 描述 |
|-------|-------|
| [link2doc](productivity/link2doc/) | 从链接整理文档并提交到 GitHub |
| [content-absorption-framework](task-management/content-absorption-framework/) | 系统化吸收外部知识仓库 |
| [md2wechat](content-publishing/md2wechat/) | Markdown 转公众号排版 |
| [markdown-to-social-cards](creative/markdown-to-social-cards/) | Markdown 转社交媒体卡片 |
| [url-to-markdown](productivity/url-to-markdown/) | URL 或文件转 Markdown |

### 📄 文档处理
| Skill | 描述 |
|-------|-------|
| [nano-pdf](document-processing/nano-pdf/) | 通过 NL 提示编辑 PDF |
| [ocr-and-documents](document-processing/ocr-and-documents/) | 从 PDF/扫描件提取文字 |
| [pdf-generation-fallbacks](document-processing/pdf-generation-fallbacks/) | Markdown 转 PDF 可靠方案 |
| [powerpoint](document-processing/powerpoint/) | 创建/编辑 PPT |

### 🌐 网页自动化
| Skill | 描述 |
|-------|-------|
| [web-crawler](web-automation/web-crawler/) | 抓取网页数据 |
| [browser-bookmark-management](web-automation/browser-bookmark-management/) | 浏览器书签管理 |
| [cloudflare-web-crawler](productivity/cloudflare-web-crawler/) | Cloudflare 浏览器渲染 API 爬取 |
| [dokobot](external-tools/dokobot/) | 使用真实浏览器读取任何网页 |

### 💼 工作空间整合
| Skill | 描述 |
|-------|-------|
| [linear](workspace-integration/linear/) | Linear 项目管理 |
| [notion](workspace-integration/notion/) | Notion API 操作 |
| [airtable](workspace-integration/airtable/) | Airtable REST API |
| [google-workspace](workspace-integration/google-workspace/) | Gmail/日历/文档/表格 |
| [obsidian](note-taking/obsidian/) | Obsidian 知识库操作 |

### 🎨 创意内容生成
| Skill | 描述 |
|-------|-------|
| [image-generation](creative/image-generation/) | AI 图像生成 |
| [gpt-image-2-workflow](creative/gpt-image-2-workflow/) | GPT-image-2 批量出图工作流 |
| [markdown-to-social-cards](creative/markdown-to-social-cards/) | 文章转社交卡片 |
| [long-form-translation](creative/long-form-translation/) | 英文长文翻译为中文 |
| [video-content-automation](media/video-content-automation/) | 视频内容自动化 |

### 🤖 外部工具集成
| Skill | 描述 |
|-------|-------|
| [dokobot](external-tools/dokobot/) | 真实浏览器页面提取 |
| [kami-design-system](external-tools/kami-design-system/) | AI 文档设计系统 |
| [yuanbao](external-tools/yuanbao/) | 元宝群组操作 |

### 🧠 模型推理
| Skill | 描述 |
|-------|-------|
| [inference-sh-cli](inference/inference-sh-cli/) | inference.sh 150+ AI 应用 |
| [minimax-api](inference/minimax-api/) | MiniMax API 完整指南 |

### 📊 研究与分析
| Skill | 描述 |
|-------|-------|
| [ai-model-comparison](research/ai-model-comparison/) | AI 模型对比分析 |
| [horizontal-vertical-analysis](research/horizontal-vertical-analysis/) | 横纵分析法 |
| [duckduckgo-search](research/duckduckgo-search/) | 免费网页搜索 |
| [arxiv](research/arxiv/) | arXiv 论文搜索 |
| [llm-wiki](research/llm-wiki/) | Karpathy 风格 LLM Wiki |

### 💻 软件开发
| Skill | 描述 |
|-------|-------|
| [github-pr-workflow](github/github-pr-workflow/) | GitHub PR 完整生命周期 |
| [github-code-review](github/github-code-review/) | 代码审查指南 |
| [test-driven-development](software-development/test-driven-development/) | TDD 流程 |
| [code-review](software-development/code-review/) | 代码审查最佳实践 |
| [gpt-5.5-prompt-strategy](software-development/gpt-5.5-prompt-strategy/) | Skill 提示词写作标准 |

### ☁️ DevOps 与部署
| Skill | 描述 |
|-------|-------|
| [cloudflare-deployment](devops/cloudflare-deployment/) | Cloudflare Pages/Workers 部署 |
| [agent-monitoring-dashboard](devops/agent-monitoring-dashboard/) | Agent 实时监控 Dashboard |
| [agent-security-boundaries](devops/agent-security-boundaries/) | Agent 安全边界 |
| [geo-optimization](devops/geo-optimization/) | 生成式引擎优化 |

### 🤓 MLOps
| Skill | 描述 |
|-------|-------|
| [unsloth](mlops/training/unsloth/) | 高速 LoRA/量化微调 |
| [axolotl](mlops/training/axolotl/) | YAML LLM 微调 |
| [vllm](mlops/inference/serving-llms-vllm/) | 高吞吐量 LLM 服务 |
| [llama-cpp](mlops/inference/llama-cpp/) | 本地 GGUF 推理 |
| [dspy](mlops/research/dspy/) | 声明式 LM 程序优化 |

### ✉️ 邮件
| Skill | 描述 |
|-------|-------|
| [clawemail](email/clawemail/) | 专属邮箱工作流 |
| [himalaya](email/himalaya/) | 终端 IMAP/SMTP 邮件 |

### 📱 社交媒体
| Skill | 描述 |
|-------|-------|
| [xitter](social-media/xitter/) | X/Twitter 交互客户端 |
| [xurl](social-media/xurl/) | X/Twitter xurl CLI |
| [x-brand-strategy-planning](social-media/x-brand-strategy-planning/) | X 个人品牌策略 |

### 🎹 娱乐
| Skill | 描述 |
|-------|-------|
| [minecraft-modpack-server](gaming/minecraft-modpack-server/) | Minecraft 模组服务器 |
| [spotify](media/spotify/) | 播放/搜索/队列管理 |

---

## 分类架构图

```
superpowers/
├─── autonomous-ai-agents/          # Agent 核心与委派
│   ├─── agent-configuration          # Hermes 配置
│   ├─── agent-workflow-system        # 工作流系统
│   ├─── agent-self-evolution         # 自我进化
│   ├─── subagent-driven-development  # 子代理协作
│   └─── codex/claude-code/opencode   # AI 编码委派
├─── devops/                       # 部署与监控
│   ├─── agent-health-check           # 健康审计
│   ├─── agent-deployment             # 部署指南
│   ├─── cloudflare-deployment        # CF 部署
│   └─── agent-monitoring-dashboard   # 实时监控
├─── task-management/              # 任务管理
│   ├─── kanban-orchestrator          # 看板协调
│   ├─── kanban-worker                # 任务执行
│   └─── night-research-cron          # 定时研究
├─── content-publishing/           # 内容发布
│   └─── md2wechat                    # 公众号发布
├─── document-processing/          # 文档处理
│   ├─── nano-pdf, ocr-and-documents
│   └─── pdf-generation-fallbacks, powerpoint
├─── workspace-integration/        # 工具整合
│   ├─── linear, notion
│   └─── airtable, google-workspace
├─── web-automation/               # 网页自动化
│   ├─── web-crawler
│   └─── browser-bookmark-management
├─── creative/                     # 创意生成
│   ├─── image-generation, gpt-image-2-workflow
│   └─── markdown-to-social-cards, video-content-automation
├─── research/                     # 研究分析
│   ├─── ai-model-comparison, horizontal-vertical-analysis
│   └─── duckduckgo-search, arxiv, llm-wiki
├─── mlops/                        # 机器学习
│   ├─── training/                  # 微调
│   ├─── inference/                 # 推理
│   └─── cloud/                     # 云服务器
├─── github/                       # GitHub 工作流
├─── software-development/         # 软件开发
├─── external-tools/               # 外部工具
│   ├─── dokobot, kami-design-system, yuanbao
├─── inference/                    # 模型推理
│   └─── inference-sh-cli, minimax-api
└─── productivity/               # 生产力（精简后）
    └─── link2doc, maps, marketing-growth-skills
```

---

## 开始使用

### 安装单个 Skill

```bash
hermes skill view <skill-name>
# 查看 skill 详情后，根据指引安装
```

### 常见工作流示例

**内容整理流**：
```
web-crawler → link2doc → md2wechat
         → night-research-cron (自动化)
```

**研究分析流**：
```
duckduckgo-search → url-to-markdown → content-absorption-framework
               → ai-model-comparison (模型选择)
```

**代码开发流**：
```
plan → codex/claude-code → code-review → github-pr-workflow
```

---

## 贡献与更新

本仓库持续迭代中。发现新的 AI 工具或改进建议？

1. 提交 Issue 描述需求
2. 使用 `link2doc` 整理相关资源
3. 创建 PR 添加新 Skill

---

*来自翡冷翠* | 持续更新于 2026-05-01
