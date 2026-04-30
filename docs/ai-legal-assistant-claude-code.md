# AI Legal Assistant for Claude Code - 完整指南

> 来源：[@Honcia13](https://x.com/Honcia13/status/2048983294398652585)  
> GitHub：[zubair-trabzada/ai-legal-claude](https://github.com/zubair-trabzada/ai-legal-claude)  
> 整理时间：2026-04-29  
> 来自翡冷翠

---

## 简介

**AI Legal Assistant** 是一个专为 Claude Code 设计的 AI 法律助手，能够在 60 秒内完成合同审查分析。通过 5 个并行工作的 AI Agent，它可以自动识别合同风险、生成法律文档、提供谈判建议，并输出专业的 PDF 报告。

这套工具直接把合同审查拉进了 AI 时代——不再需要花费数千美元请律师逐条审阅，一份合同的安全评分、风险分级、条款解读、义务时间线，全部一键生成。

---

## 为什么这很重要

| 指标 | 数值 |
|------|------|
| 平均律师审查费用 | $300–$500/小时 |
| 基础合同审查成本 | $1,500–$3,000 |
| 不阅读合同的自由职业者比例 | 82% |
| 一个糟糕条款的潜在损失 | $10,000+ |
| 没有法务审查的小企业比例 | 67% |
| 使用本工具审查时间 | 60 秒内 |

---

## 核心功能一览

### 合同分析功能

| 功能 | 说明 |
|------|------|
| 📊 **合同安全评分** | 0-100 分量化评估，附带等级评定 |
| 🚨 **风险仪表盘** | 高危/中危/低危条款分级展示 |
| 📝 **大白话解读** | 将法律术语翻译成普通人能懂的解释 |
| 🔍 **缺失保护识别** | 找出合同里应该存在但缺失的保护条款 |
| 📅 **义务时间线** | 梳理所有截止日期和对应后果，一目了然 |
| ⚖️ **合规问题标记** | 自动标记 GDPR、CCPA 等监管合规问题 |
| 🎯 **谈判优先级** | 按重要性排序的修改建议 |

### 文档生成功能

支持一键生成以下法律文档：
- NDA（保密协议）- 双向/单向/员工/供应商版本
- 服务条款（Terms of Service）
- 隐私政策（Privacy Policy）
- 商业合作协议
- 自由职业者合同

---

## 快速开始

### 一键安装

```bash
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/ai-legal-claude/main/install.sh | bash
```

一条命令即可完成：14 个技能 + 5 个 Agent + PDF 生成脚本的完整安装。

### 环境要求

- **Claude Code**（需配置 Anthropic API key）
- **Python 3.8+**（仅 PDF 生成功能需要）
- **reportlab** — `pip3 install reportlab`（PDF 生成依赖）

---

## 14 个核心命令详解

### 合同分析类

| 命令 | 功能描述 |
|------|----------|
| `/legal review <文件>` | **旗舰功能** — 完整合同审查，5 个 Agent 并行工作。输出合同安全评分、逐条分析、优先建议 |
| `/legal risks <文件>` | 深度风险分析，每条条款 severity 评分，估算财务风险敞口 |
| `/legal compare <文件1> <文件2>` | 并排对比两份合同，标记增删改和危险变更 |
| `/legal plain <文件>` | 将每条款翻译成大白话 |
| `/legal negotiate <文件>` | 为每条不利条款生成具体的反提案和替换语言 |
| `/legal missing <文件>` | 找出"应该存在但缺失"的保护条款 |

### 文档生成类

| 命令 | 功能描述 |
|------|----------|
| `/legal nda <描述>` | 生成定制 NDA — 双向/单向/员工/供应商 |
| `/legal terms <网址>` | 根据网站实际功能生成服务条款，GDPR/CCPA 合规 |
| `/legal privacy <网址>` | 扫描网站数据收集情况，生成隐私政策 |
| `/legal agreement <类型>` | 生成商业协议 — 自由职业者合同、合作、SOW、MSA 等 |
| `/legal freelancer <文件>` | 从自由职业者角度专项审查，标记常见承包商陷阱 |

### 合规与报告类

| 命令 | 功能描述 |
|------|----------|
| `/legal compliance <网址>` | 合规缺口分析 — GDPR、CCPA、ADA、PCI-DSS、CAN-SPAM、SOC 2 |
| `/legal report-pdf` | 专业 PDF 报告，含评分仪表盘、风险图表、优先级行动清单 |

---

## 旗舰功能：/legal review 深度解析

最强大的命令，运行后获得完整分析报告：

### 输出内容

1. **合同安全评分** (0-100) + 字母等级
2. **风险仪表盘** — 高/中/低风险条款数量统计
3. **逐条分析** — 每条款评分、大白话解释、具体修复建议
4. **缺失保护** — 应该存在但缺失的条款清单
5. **义务时间线** — 每个截止日期和后果的映射
6. **合规标记** — 监管问题识别
7. **谈判优先级** — 按重要性排序的修改建议
8. **后续行动** — 可执行的行动清单

### 5 个并行 Agent 工作机制

```
/legal review my-contract.pdf
```

执行后，5 个 AI Agent 并行启动：

| Agent | 角色 | 权重 |
|-------|------|------|
| Clause Analyst | 识别并分类每条款 | 20% |
| Risk Assessor | 条款风险评分 | 25% |
| Compliance Checker | 标记监管问题 | 20% |
| Terms Mapper | 映射义务、截止日期、触发条件 | 15% |
| Recommendations Engine | 生成具体修复建议 | 20% |

结果汇总为统一报告，输出单一合同安全评分。

---

## 适用场景

### 自由职业者与代理机构
- 签约前审查客户合同
- 为新客户生成 NDA
- 创建带保护条款的工作说明书（SOW）
- 将合同审查作为付费服务提供（$500-$1,500/次）

### 小型企业
- 审查供应商和供应合同
- 生成隐私政策和服务条款
- 网站合规性审计
- 真正理解自己在签什么

### AI 自动化服务商
- 将合同审查加入服务套餐
- 为客户生成专业 PDF 报告
- 提供月度法律文件管理托管服务
- 与 AI 营销套件、AI 销售团队配合使用

---

## 项目结构

```
ai-legal-claude/
├── legal/
│   └── SKILL.md                    # 主编排器（命令路由）
├── skills/
│   ├── legal-review/SKILL.md       # 完整审查（5 Agent）
│   ├── legal-risks/SKILL.md        # 深度风险分析
│   ├── legal-compare/SKILL.md      # 合同对比
│   ├── legal-plain/SKILL.md        # 大白话翻译
│   ├── legal-negotiate/SKILL.md    # 反提案生成
│   ├── legal-missing/SKILL.md      # 缺失保护查找
│   ├── legal-nda/SKILL.md          # NDA 生成
│   ├── legal-terms/SKILL.md        # 服务条款生成
│   ├── legal-privacy/SKILL.md      # 隐私政策生成
│   ├── legal-agreement/SKILL.md    # 商业协议生成
│   ├── legal-compliance/SKILL.md     # 合规缺口分析
│   ├── legal-freelancer/SKILL.md   # 自由职业者专项审查
│   └── legal-report-pdf/SKILL.md   # PDF 报告生成
├── agents/
│   ├── legal-clauses.md             # 条款分析 Agent
│   ├── legal-risks.md               # 风险评估 Agent
│   ├── legal-compliance.md          # 合规检查 Agent
│   ├── legal-terms.md               # 条款与义务 Agent
│   └── legal-recommendations.md     # 建议 Agent
├── scripts/
│   └── generate_legal_pdf.py        # PDF 生成（ReportLab）
├── templates/
│   └── contract-review-template.md  # 报告模板
├── install.sh                       # 一行命令安装
├── uninstall.sh                     # 干净卸载
└── README.md
```

---

## 卸载方法

```bash
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/ai-legal-claude/main/uninstall.sh | bash
```

或在本地运行：

```bash
./uninstall.sh
```

---

## 系列项目

此工具属于 **Claude Code 技能系列**：
- [AI Marketing Suite](https://github.com/zubair-trabzada/ai-marketing-claude)
- [AI Sales Team](https://github.com/zubair-trabzada/ai-sales-team-claude)
- **AI Legal Assistant**（本项目）

---

## ⚠️ 免责声明

本工具仅供教育和信息参考使用。**不构成法律建议**，**不能替代执业律师的咨询**。在签署任何合同前，请务必让合格的律师进行审查。

---

## 快速参考：常用命令速查表

| 需求 | 命令 |
|------|------|
| 全面审查合同 | `/legal review <文件>` |
| 只看风险点 | `/legal risks <文件>` |
| 对比两个版本 | `/legal compare <旧> <新>` |
| 读懂条款 | `/legal plain <文件>` |
| 生成 NDA | `/legal nda "描述项目"` |
| 生成隐私政策 | `/legal privacy https://yoursite.com` |
| 检查网站合规 | `/legal compliance https://yoursite.com` |
| 输出 PDF 报告 | `/legal report-pdf` |

---

*来自翡冷翠*
