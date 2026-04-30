# 90天成为高薪AI工程师：10个必精通的GitHub仓库

> 来源：[千寻 @Crypto_QianXun](https://x.com/crypto_qianxun/status/2049295115441905775)  
> 整理时间：2026-04-30  
> 来自翡冷翠

---

## 简介

本文档整理了 X 用户[@Crypto_QianXun](https://x.com/Crypto_QianXun)分享的 10 个核心 GitHub 仓库，专为希望在 90 天内掌握高薪 AI 工程师技能的学习者设计。这些仓库覆盖了从基础框架到生产级系统的完整技术栈，涵盖 RAG、智能体、多模态应用、向量数据库等当前最热门的 AI 工程领域。

---

## 内容清单总览

| 序号 | 仓库名称 | 核心领域 | 适用场景 | Stars |
|------|----------|----------|----------|-------|
| 1 | awesome-llm-apps | 生产级AI应用 | RAG、智能体、多模态 | 106k+ |
| 2 | LangChain | AI基础框架 | 通用AI应用开发 | 135k+ |
| 3 | LangGraph | 智能体编排 | 复杂工作流设计 | 30.8k+ |
| 4 | CrewAI | 多智能体协调 | 企业级AI团队 | - |
| 5 | Ollama | 本地LLM运行 | 模型学习与测试 | - |
| 6 | awesome-mcp-servers | MCP协议 | AI工具集成 | - |
| 7 | Qdrant | 向量数据库 | 语义搜索/RAG | - |
| 8 | AI-Agents-for-Beginners | 微软课程 | 智能体入门学习 | - |
| 9 | system-design-primer | 系统设计 | 工程架构面试 | - |
| 10 | awesome-claude-code | Claude Code | AI辅助编程 | - |

---

## 详细内容

### 1. awesome-llm-apps
**来源：** [shubhamai/awesome-llm-apps](https://github.com/shubhamai/awesome-llm-apps)

#### 核心定位
生产级AI应用开发完整指南，涵盖 RAG（检索增强生成）、智能体、多模态应用等核心技术方向。

#### 核心内容
- **RAG 应用**：完整的检索增强生成实现方案
- **AI 智能体**：构建自主决策的智能体系统
- **多模态应用**：文本、图像、音频等多模态处理
- **生产级代码**：附带完整可运行的代码示例

#### 适用人群
- 希望系统学习AI应用开发的工程师
- 需要生产级RAG系统实现的开发者
- 对多模态AI应用感兴趣的技术人员

---

### 2. LangChain
**来源：** [langchain-ai/langchain](https://github.com/langchain-ai/langchain)

#### 核心定位
AI智能体工程平台，是目前应用最广泛的AI应用开发基础框架。

#### 核心特性
- **生产环境验证**：被 Klarna、Replit、Elastic 等知名企业以及 2026 年大多数 AI 创业公司采用
- **模块化设计**：灵活的链式组件架构
- **丰富集成**：支持几乎所有主流 LLM 和工具
- **生态系统**：拥有庞大的社区和插件生态

#### 适用场景
- 构建基于LLM的应用程序
- 快速原型开发和生产部署
- 需要与多种AI服务集成的项目

---

### 3. LangGraph
**来源：** [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)

#### 核心定位
驱动生产级智能体的编排层，用于构建具有状态管理和循环能力的复杂AI系统。

#### 核心特性
- **图结构**：将智能体工作流建模为有向图
- **状态管理**：支持复杂的状态流转和持久化
- **循环支持**：允许智能体进行多轮交互和迭代
- **生产就绪**：专为生产环境设计的高可靠性框架

#### 行业地位
资深AI工程师岗位描述中的必备技能，掌握 LangGraph 是进入高级AI工程岗位的敲门砖。

---

### 4. CrewAI
**来源：** [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)

#### 核心定位
多智能体协调框架，专为复杂任务的多智能体协作设计。

#### 核心特性
- **角色定义**：可为不同智能体分配特定角色和职责
- **任务委派**：智能体之间的任务自动分配和协调
- **企业级**：财富500强团队首选的多智能体框架
- **工作流设计**：可视化工作流设计工具

#### 适用场景
- 需要多个AI智能体协同完成的复杂项目
- 企业级自动化工作流
- 模拟团队协作的AI系统

---

### 5. Ollama
**来源：** [ollama/ollama](https://github.com/ollama/ollama)

#### 核心定位
在本地机器上运行任何开源LLM的最简单方式。

#### 核心价值
- **本地运行**：无需云服务，完全本地部署
- **快速上手**：一键运行主流开源模型
- **学习利器**：理解LLM工作原理的最佳实践工具
- **隐私保护**：数据完全本地处理

#### 适用人群
- 希望深入理解LLM内部机制的开发者
- 对数据隐私有高要求的用户
- 需要在离线环境使用AI的开发者

---

### 6. awesome-mcp-servers
**来源：** [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)

#### 核心定位
MCP（Model Context Protocol）服务器资源合集，2026年主流AI实验室采用的标准协议。

#### 核心价值
- **标准掌握**：MCP是AI工具集成的新标准
- **先发优势**：掌握MCP让你在竞争中领先99%的工程师
- **生态整合**：连接各种AI工具和服务的标准化接口
- **未来趋势**：被主流AI实验室广泛采用

#### 学习建议
尽早掌握MCP协议，这将成为AI工程师的基础技能要求。

---

### 7. Qdrant
**来源：** [qdrant/qdrant](https://github.com/qdrant/qdrant)

#### 核心定位
大规模生产级RAG使用的向量数据库。

#### 核心特性
- **向量存储**：高效的嵌入向量存储和检索
- **语义搜索**：基于语义的相似性搜索
- **生产级性能**：为大规模生产环境优化
- **AI岗位必需**：嵌入和语义搜索已成为AI工程师的核心技能

#### 技术要点
- 掌握向量数据库是构建RAG系统的关键
- Qdrant是当前生产环境最受欢迎的向量数据库之一

---

### 8. AI-Agents-for-Beginners
**来源：** [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)

#### 核心定位
微软官方免费课程，12节课教你从零构建AI智能体。

#### 课程内容
- **12节课程**：系统化的智能体开发教程
- **真实代码**：每一课都配有可运行的代码
- **实战练习**：基于真实场景的编程练习
- **面试准备**：课程内容紧贴AI工程师面试要求

#### 学习价值
- 微软官方出品，内容权威可靠
- 从入门到实战，循序渐进
- 适合作为AI智能体领域的入门首选

---

### 9. system-design-primer
**来源：** [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

#### 核心定位
生产级AI工程的核心是系统设计，FAANG工程师面试准备的经典仓库。

#### 核心价值
- **系统设计基础**：构建可扩展系统的核心知识
- **面试准备**：FAANG等大厂技术面试的标准参考资料
- **工程思维**：培养架构师级别的系统设计思维
- **生产实践**：从理论到生产环境的最佳实践

#### 与AI工程的关系
生产级AI系统本质上是复杂的分布式系统，掌握系统设计是成为高级AI工程师的必经之路。

---

### 10. awesome-claude-code
**来源：** [anthropics/awesome-claude-code](https://github.com/anthropics/awesome-claude-code)

#### 核心定位
Claude Code使用指南，AI辅助编程工具的资源合集。

#### 行业地位
- **大厂内部使用**：被FAANG、OpenAI、Anthropic以及大多数YC创业公司内部采用
- **AI编程趋势**：代表AI辅助编程的最新发展方向
- **效率工具**：显著提升代码开发效率

#### 学习建议
了解并掌握AI辅助编程工具，这是未来软件工程师的标配技能。

---

## 资源汇总

### 所有GitHub仓库链接

| 仓库 | 链接 | 核心功能 |
|------|------|----------|
| awesome-llm-apps | https://github.com/shubhamai/awesome-llm-apps | 生产级AI应用示例 |
| LangChain | https://github.com/langchain-ai/langchain | AI应用框架 |
| LangGraph | https://github.com/langchain-ai/langgraph | 智能体编排 |
| CrewAI | https://github.com/crewAIInc/crewAI | 多智能体协调 |
| Ollama | https://github.com/ollama/ollama | 本地LLM运行 |
| awesome-mcp-servers | https://github.com/appcypher/awesome-mcp-servers | MCP协议资源 |
| Qdrant | https://github.com/qdrant/qdrant | 向量数据库 |
| AI-Agents-for-Beginners | https://github.com/microsoft/ai-agents-for-beginners | 微软智能体课程 |
| system-design-primer | https://github.com/donnemartin/system-design-primer | 系统设计指南 |
| awesome-claude-code | https://github.com/anthropics/awesome-claude-code | Claude Code资源 |

### 值得关注的人/账号

- **@Crypto_QianXun** - 千寻，币圈工具分享/项目研究/赛道分析

---

## 学习路径建议

### 第1-30天：基础构建
1. 完成 [AI-Agents-for-Beginners](https://github.com/microsoft/ai-agents-for-beginners) 微软课程
2. 学习 [Ollama](https://github.com/ollama/ollama) 本地运行LLM，理解模型基础
3. 掌握 [LangChain](https://github.com/langchain-ai/langchain) 基础框架

### 第31-60天：进阶应用
4. 深入学习 [LangGraph](https://github.com/langchain-ai/langgraph) 智能体编排
5. 研究 [CrewAI](https://github.com/crewAIInc/crewAI) 多智能体系统
6. 实践 [awesome-llm-apps](https://github.com/shubhamai/awesome-llm-apps) 中的生产级案例

### 第61-90天：系统能力
7. 掌握 [Qdrant](https://github.com/qdrant/qdrant) 向量数据库，构建RAG系统
8. 学习 [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) MCP协议
9. 研读 [system-design-primer](https://github.com/donnemartin/system-design-primer) 系统设计
10. 实践 [awesome-claude-code](https://github.com/anthropics/awesome-claude-code) AI辅助编程

---

## 附录：快速参考

### 技术栈分类

| 层级 | 技术 | 对应仓库 |
|------|------|----------|
| 基础框架 | AI应用框架 | LangChain |
| 编排层 | 智能体工作流 | LangGraph |
| 多智能体 | 团队协作AI | CrewAI |
| 数据层 | 向量数据库 | Qdrant |
| 协议层 | 工具集成标准 | awesome-mcp-servers |
| 系统层 | 架构设计 | system-design-primer |
| 工具层 | AI辅助编程 | awesome-claude-code |
| 学习层 | 入门教程 | AI-Agents-for-Beginners |
| 实践层 | 生产案例 | awesome-llm-apps |
| 本地层 | 模型运行 | Ollama |

---

*来自翡冷翠*
