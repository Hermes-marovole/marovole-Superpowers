# Datawhale Happy-LLM - 从零开始构建大模型

> 来源：https://x.com/IndieDevHailey/status/2048293804705529906  
> GitHub：https://github.com/datawhalechina/happy-llm  
> 在线阅读：https://datawhalechina.github.io/happy-llm/  
> 整理时间：2026-04-26  
> 来自翡冷翠

---

## 简介

**Happy-LLM** 是 Datawhale 社区出品的开源系统性 LLM 学习教程，GitHub 已获 **29k+ Stars**，持续霸榜 Trending。这是一份真正「从零开始」的手把手教程——不是拼凑知识点，而是带你从 NLP 基础一路走到亲手训练出一个完整的 LLaMA2 风格大模型。

适合人群：
- 想深入理解 LLM 原理的开发者
- 不满足于只会调用 API、想自己动手的人
- 想做 AI 应用 / Agent 的工程师

---

## 项目核心亮点

| 维度 | 特点 |
|------|------|
| **体系完整** | NLP → Transformer → 预训练 → LLM 一条线讲通，非拼凑式知识 |
| **边学边做** | 按 LLaMA 2 思路，从 Tokenizer 到预训练到微调（LoRA / QLoRA），完整跑通 |
| **工程导向** | 不止讲模型，RAG / Agent / 模型评测全覆盖，贴近真实项目落地 |

---

## 内容导航（7章完整路径）

| 章节 | 关键内容 | 状态 |
|------|----------|------|
| **前言** | 项目缘起、背景及读者建议 | ✅ |
| **第一章：NLP 基础概念** | 什么是 NLP、发展历程、任务分类、文本表示演进（One-hot → Word2Vec → Transformer） | ✅ |
| **第二章：Transformer 架构** | 注意力机制详解、Encoder-Decoder 结构、**手把手代码搭建 Transformer** | ✅ |
| **第三章：预训练语言模型** | Encoder-only（BERT）、Encoder-Decoder（T5）、Decoder-Only（GPT）三种架构对比 | ✅ |
| **第四章：大语言模型** | LLM 定义、训练策略（预训练+微调）、涌现能力分析、上下文学习 | ✅ |
| **第五章：动手搭建大模型** | **实现 LLaMA2 架构**、训练自己的 Tokenizer、预训练 215M 参数小型 LLM | ✅ |
| **第六章：大模型训练实践** | 预训练流程、有监督微调（SFT）、**LoRA / QLoRA 高效微调**实战 | 🚧 |
| **第七章：大模型应用** | **模型评测（Benchmark）**、**RAG 检索增强生成**、**Agent 智能体**简单实现 | ✅ |

> ✅ = 已完成 ｜ 🚧 = 更新中

---

## 学完你能做什么？

- ✅ 看懂 Transformer 架构和注意力机制原理
- ✅ 训练一个 215M 参数的小模型（Base + SFT 两个版本已开源）
- ✅ 会调参、会排查训练问题
- ✅ 动手做出一个 AI 小应用（RAG / Agent）

---

## 实战产出物

### 开源模型（ModelScope）

| 模型 | 参数量 | 下载地址 |
|------|--------|----------|
| Happy-LLM-Chapter5-Base-215M | 215M | [🤖 ModelScope](https://www.modelscope.cn/models/kmno4zx/happy-llm-215M-base) |
| Happy-LLM-Chapter5-SFT-215M | 215M | [🤖 ModelScope](https://www.modelscope.cn/models/kmno4zx/happy-llm-215M-sft) |

> 创空间在线体验：[🤖 点击试用](https://www.modelscope.cn/studios/kmno4zx/happy_llm_215M_sft)

### PDF 离线版

- GitHub Releases：https://github.com/datawhalechina/happy-llm/releases
- 国内下载：https://www.datawhale.cn/learn/summary/179

*注：PDF 已添加 Datawhale 水印防营销号倒卖，不影响阅读*

### PPT 课件

- 配套讲义 PPT：https://github.com/HZAI-ZJNU/happy-llm-ppt

---

## 建议学习路径

### 路径 A：完整通关（推荐）
```
第1章 → 第2章 → 第3章 → 第4章 → 第5章 → 第6章 → 第7章
(NLP基础 → Transformer → 预训练模型 → LLM原理 → 动手实现 → 训练微调 → 应用实战)
```

### 路径 B：急用先行
- **只想用 LLM**：第4章（LLM基础）→ 第7章（RAG/Agent应用）
- **想做微调**：第5章（模型结构）→ 第6章（LoRA/QLoRA微调）
- **想懂原理**：第2章（Transformer精读）→ 第3章（模型架构对比）

---

## 资源汇总

### 官方链接
| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/datawhalechina/happy-llm |
| 在线阅读（Docsify） | https://datawhalechina.github.io/happy-llm/ |
| SwanLab 训练看板 | https://swanlab.cn/@kmno4/Happy-LLM/overview |
| Trendshift 榜单 | https://trendshift.io/repositories/14175 |

### 前置知识要求
- Python 编程基础
- 深度学习基础（PyTorch 了解更佳）
- 了解 NLP 基本概念（非必须，第1章会覆盖）

### 相关项目
- [self-llm](https://github.com/datawhalechina/self-llm) - Datawhale 开源大模型食用指南（调用/部署篇）

---

## 核心贡献者

- **宋志学** ([KMnO4-zx](https://github.com/KMnO4-zx)) - 项目负责人（Datawhale / 中国矿业大学北京）
- **邹雨衡** ([logan-zou](https://github.com/logan-zou)) - 项目负责人（Datawhale / 对外经济贸易大学）
- **朱信忠** ([xinzhongzhu.github.io](https://xinzhongzhu.github.io/)) - 指导专家（Datawhale首席科学家 / 浙江师范大学杭州人工智能研究院教授）

### 社区共建
- 已有多位社区贡献者的 Extra Chapter 文章
- 欢迎提交 Issue / PR 参与共建

---

## 快速参考

### 本地启动文档站点
```bash
git clone https://github.com/datawhalechina/happy-llm.git
cd happy-llm
# 使用 docsify 本地预览
npm i docsify-cli -g
docsify serve docs
```

### 第五章核心依赖
```bash
torch>=2.0.0
transformers>=4.30.0
datasets
sentencepiece
accelerate
peft  # 用于 LoRA 微调
```

---

*来自翡冷翠*
