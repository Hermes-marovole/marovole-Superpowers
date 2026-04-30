# 基于 YC RFS 的 AI 行业域名投资策略

> 来源：[BECOOL @becool_me](https://x.com/becool_me/status/2049496332050526690)  
> 引用：[Y Combinator @ycombinator](https://x.com/ycombinator/status/2048834285197812146)  
> 整理时间：2026-04-30  
> 来自翡冷翠

---

## 执行摘要

本文档记录了一种创新的 AI 时代域名投资策略：利用 Claude AI 基于 Y Combinator 最新发布的 Requests for Startups (RFS) 生成海量行业域名候选，通过 query.domains API 批量筛选可注册域名，最终完成精选投资。原作者花费 $90 成功注册 11 个高价值域名，将域名投资转化为一种数据驱动的"AI 增强投机"。

**核心洞察**:
- 利用 AI 生成域名的创意来源（YC RFS 代表未来 3-5 年的创业热点）
- 自动化批量检查域名可用性
- AI 辅助排序和决策
- 低成本高潜力的另类投资方式

---

## 方法论详解

### 第一步：识别权威趋势源

**Y Combinator Requests for Startups (RFS)** 是 YC 每半年发布一次的创业方向指南，代表硅谷顶级加速器对未来创业趋势的判断。Summer 2026 RFS 的核心理念：

> "AI has stopped being a feature and started being the foundation."
> — Y Combinator

这意味着 AI 正在从"附加功能"转变为"基础设施"，基于这一判断的所有创业方向都可能产生大量相关域名需求。

### 第二步：AI 生成域名候选

使用 Claude 针对每个行业生成 **200 个推荐域名**。提示词思路：

```
基于以下行业描述，生成 200 个创意域名建议：
- 行业名称：[如 "AI-Native Service Companies"]
- 核心概念：[一句话概括]
- 关键词：[行业关键词列表]
- 域名偏好：.com / .ai / .io / 创意新 TLD
- 命名风格：简洁、易记、品牌化、可发音
```

### 第三步：批量可用性检查

使用 **query.domains** 的 API 进行批量 WHOIS 查询，筛选出可注册域名。

**query.domains 工具特点**：
- 基于 WHOIS 查询的即时批量域名可用性检查
- 支持 SSE (Server-Sent Events) 快速返回结果
- 免费额度充足，适合大规模筛选
- 支持多域名并行查询

**API 调用示例**：
```bash
curl "https://query.domains/api/check?domains=example1.com,example2.ai,example3.io"
```

### 第四步：AI 辅助排序推荐

将可注册域名列表再次交给 Claude，进行推荐排序：

**排序维度**：
1. **品牌潜力** - 是否易于品牌化
2. **行业匹配度** - 与目标行业的关联强度
3. **发音友好性** - 是否容易发音和记忆
4. **长度简洁性** - 越短越好
5. **扩展性** - 是否可扩展到相邻领域

### 第五步：注册执行

根据 AI 推荐，选择性注册最具潜力的域名。原作者策略：
- 总预算：$90
- 注册数量：11 个域名
- 均价：约 $8/域名
- 投资逻辑：分散投资，覆盖多个 RFS 领域

---

## YC Summer 2026 RFS 完整解读

以下 15 个创业方向是本次域名策略的核心依据：

### 1. AI for Low-Pesticide Agriculture（低农药农业 AI）
**作者**: Garry Tan

现代农业依赖化学农药，但成本上升、效果下降、健康风险增加。AI 现在可以：
- 实时识别单个杂草和害虫
- 精准机器人处理（只处理受感染植株而非整片农田）
- 生物解决方案（微生物、肽、RNA 技术）

**域名生成关键词**: agri-ai, precision-farm, bio-pesticide, smart-crop, agro-robot

---

### 2. AI-Native Service Companies（AI 原生服务公司）
**作者**: Gustaf Alströmer

从 SaaS 到 AI Copilot 再到 AI 原生服务公司——直接"做工作"而不是"卖工具"。重点领域：
- 保险经纪
- 会计、税务、审计
- 合规
- 医疗管理

**域名生成关键词**: ai-service, auto-compliance, ai-broker, smart-tax, agent-firm

---

### 3. AI Personalized Medicine（AI 个性化医疗）
**作者**: Ankit Gupta

两大科学革命交汇：
1. 个性化诊断成本暴跌（基因组测序超越摩尔定律速度降价）
2. 个性化治疗成本暴跌（mRNA 等基因疗法）

智能体可以分析个性化健康数据，提供精准建议。

**域名生成关键词**: ai-medicine, personal-health, genome-ai, precision-cure, bio-agent

---

### 4. Company Brain（公司大脑）
**作者**: Tom Blomfield

每家公司的关键知识分散在各处：员工脑海、旧邮件、Slack、工单系统。构建一个集中式的"公司大脑"，将碎片化知识结构化，转化为 AI 可执行的技能文件。

这不是企业搜索或文档聊天机器人，而是公司运作方式的活地图。

**域名生成关键词**: company-brain, org-memory, ai-knowledge, corp-mind, work-map

---

### 5. Counter-Swarm Defense（反蜂群防御）
**作者**: Tyler Bosmeny

伊朗无人机群摧毁 AWS 数据中心——未来战争不是单无人机，而是低成本、自主、抗干扰的蜂群。

防御方案：
- 高容量拦截器（一次击落 50 架而非 1 架）
- 传感器融合软件
- 非动能防御（气溶胶、缠绕物）
- 攻击自主性协议

**域名生成关键词**: swarm-defense, anti-drone, aerial-guard, swarm-shield, counter-uas

---

### 6. Dynamic Software Interfaces（动态软件界面）
**作者**: Ankit Gupta

AI 让用户成为自己的"前置部署工程师"。用户可以深度定制软件界面——我的邮件客户端可能像任务列表，学生的可能像日历。

软件公司将交付可共享的原语，用户通过 AI 代理进行激进定制。

**域名生成关键词**: dynamic-ui, adaptive-interface, custom-software, ai-frontend, mod-app

---

### 7. Electronics in Space（太空电子）
**作者**: Philip Johnston

可重复使用火箭大幅降低太空运输成本。需要大量新的太空计算能力，特别是推理芯片。

**域名生成关键词**: space-chip, orbital-compute, cosmic-silicon, sat-ai, astro-inference

---

### 8. Hardware Supply Chain（硬件供应链）
**作者**: Nicolas Dessaigne

深圳硬件团队一天就能从设计到新零件，美国需要数周。需要：
- 加速零件生产
- 快速硬件迭代
- 设计-制造-物流整合

**域名生成关键词**: hardware-chain, maker-supply, proto-fast, fab-speed, hw-logistics

---

### 9. Industrial Capabilities in Space（太空工业能力）
**作者**: Adi Oltean

在月球和太空发展工业能力，特别是：
- 通过电解提取硅、铝、铁、钛等原材料
- 从熔融月壤 3D 打印复杂结构（无支撑更高效）

**域名生成关键词**: space-industry, lunar-fab, moon-mine, astro-material, regolith-tech

---

### 10. Inference Chips for Agent Workflows（Agent 工作流推理芯片）
**作者**: Diana Hu

传统 GPU 在 Agent 工作流中利用率仅 30-40%，因为工作流是循环的：工具调用、分支、回溯、跨步骤保持上下文。

专用芯片需要：
- 快速上下文切换
- 原生推测解码
- 为 KV Cache 优化的内存

NVIDIA 以 $200 亿收购 Groq 正是因为预见到这一点。

**域名生成关键词**: agent-chip, inference-silicon, ai-accelerator, workflow-gpu, llm-hardware

---

### 11. SaaS Challengers（SaaS 挑战者）
**作者**: Jared Friedman

AI 编码让软件生产成本降低 10-100 倍，传统 SaaS 护城河（数百万行代码、数十年积累）正在消失。

攻击策略：
- 十分之一价格克隆现有产品
- 从头开始 AI 原生设计
- 将 10 个点解决方案打包成套件
- 开源替代 $50K/席的产品

**域名生成关键词**: saas-challenge, ai-native-saas, legacy-killer, cloud-disrupt, next-saas

---

### 12. Software for Agents（Agent 软件）
**作者**: Aaron Epstein

下一个万亿互联网用户将是 AI Agent。但现有软件为人类点击按钮设计，Agent 需要：
- API、MCP、CLI 等机器可读接口
- 完整文档
- 无需人类介入即可自动发现和使用

**域名生成关键词**: agent-software, mcp-tools, api-for-agents, bot-infrastructure, agent-stack

---

### 13. Startups That Want to Sell to Huge Companies（面向大企业的初创公司）
**作者**: Harshita Arora & Brad Flora

AI 改变了与大企业交易的三个障碍：
1. 接触决策者：大企业 CEO 主动寻找 AI 解决方案
2. 产品深度：2-3 人团队可在数月内交付大企业可用的产品
3. 风险回报：大企业领导理解必须适应 AI

YC 公司现在可在成立第一年就与财富 10 强签署数百万美元合同。

**域名生成关键词**: enterprise-ai, b2b-agent, corp-automation, fortune-tech, bigco-ai

---

### 14. Supply Chain 2.0 for Semiconductors（半导体供应链 2.0）
**作者**: Diana Hu

一块先进 AI 芯片需要 1,400 个工艺步骤，跨越十几国，耗时 5 个月。目前用 Excel、SAP 和电话管理。

需求：
- 实时分配跟踪
- 多层级风险监控
- 出口合规

**域名生成关键词**: chip-supply, semi-chain, wafer-track, fab-logistics, silicon-flow

---

### 15. The AI Operating System for Companies（企业 AI 操作系统）
**作者**: Diana Hu

最佳 AI 原生公司让整个公司可查询：每个会议被记录、每个工单被跟踪、每次客户互动被捕获，全部对智能层可读。

将公司从"开环"转变为"闭环"系统：监控、比较、调整。将公司自身的产物转化为自我改进循环。

**域名生成关键词**: ai-os, corp-operating, company-ai, org-system, enterprise-loop

---

## 工具与资源

### query.domains
- **网址**: https://query.domains
- **功能**: 基于 WHOIS 的批量域名可用性检查
- **定价**: 免费额度充足，付费方案透明
- **API 文档**: https://query.domains/zh-hans/playground

### Y Combinator RFS
- **网址**: https://www.ycombinator.com/rfs
- **更新频率**: 每半年一次（与批次同步）
- **历史版本**: Summer 2026, Spring 2026, Fall 2025, Summer 2025, Spring 2025, Winter 2025, Summer 2024...

### 作者背景
**BECOOL** (@becool_me) 已开发的工具型产品：
- small.im - 小图工具
- favicon.im - Favicon 生成
- datetime.app - 日期时间工具
- ip.network - IP 查询
- temp.now - 临时工具
- base64.sh - Base64 编码解码

---

## 投资策略启示

### 为什么这个策略有效？

1. **趋势前置**: YC RFS 代表未来 3-5 年的创业热点
2. **需求验证**: 每个 RFS 领域都将产生大量创业公司，需要品牌域名
3. **规模化**: AI 生成 + API 检查可以批量处理海量候选
4. **低成本试错**: $8-15/域名的小额投资，分散风险
5. **退出路径**: 可向对应领域的创业公司出售域名

### 风险与注意事项

- 域名投资并非稳赚不赔
- 需要持有周期（可能数年）
- 部分新 TLD 续费昂贵
- 商标注册冲突风险
- 投机性质，请量力而行

---

## 快速参考：域名生成提示词模板

```
你是域名命名专家。请基于以下信息生成 200 个域名建议：

行业名称: [从上方 15 个选择]
行业核心概念: [一句话描述]
目标用户: [初创公司/开发者/企业]

要求：
1. 主要推荐 .com、.ai、.io、.app、.co
2. 长度优先 5-10 个字符
3. 易发音、易记忆、可品牌化
4. 避免连字符和数字
5. 考虑动词+名词、形容词+名词、合成词、新造词等策略

输出格式：
- 一级推荐（10个）：最优质的域名
- 二级推荐（40个）：高质量备选
- 三级推荐（150个）：其他创意

请为每个推荐简要说明命名逻辑。
```

---

## 相关链接汇总

| 名称 | 链接 | 说明 |
|------|------|------|
| 原帖 | https://x.com/becool_me/status/2049496332050526690 | BECOOL 分享域名投资策略 |
| YC RFS 原帖 | https://x.com/ycombinator/status/2048834285197812146 | YC Summer 2026 RFS 发布 |
| YC RFS 页面 | https://www.ycombinator.com/rfs | 完整 Requests for Startups |
| query.domains | https://query.domains | 批量域名可用性检查工具 |
| query.domains API | https://query.domains/zh-hans/playground | API 文档与测试 |
| 作者项目-small.im | https://small.im | 小图工具 |
| 作者项目-favicon.im | https://favicon.im | Favicon 生成器 |
| 作者项目-datetime.app | https://datetime.app | 日期时间工具 |
| 作者项目-ip.network | https://ip.network | IP 查询工具 |

---

*来自翡冷翠*
