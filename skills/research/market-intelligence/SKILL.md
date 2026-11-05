---
name: market-intelligence
description: "Use when doing market/competitor/10-K/GTM intel."
version: 1.1.0
author: 智子 (Hermes Agent)
license: MIT
metadata:
  hermes:
    tags: [market-research, competitive-intelligence, prospectus, earnings-report, sec-edgar, hkex, voc, gtm, tam-sam-som]
    category: research
    related_skills: [content-grounding, grounded-citations, web-search, web-crawler, startup-pressure-test, dbs-benchmark, dbs-jtbd]
---

# Market, Financial & GTM Intelligence (市场、招股书财报与获客一手情报)

## When to Use

当用户需要进行以下任一深度的商业与产品研究时调用本技能：
- **市场与赛道调研**：测算真实市场规模（TAM/SAM/SOM）、拆解产业链毛利与分润结构、寻找未被满足的细分切口（Wedge）。
- **行业巨头招股书与财报解剖**：从美股（S-1/10-K/20-F）、港股（港交所披露易招股书/沙利文灼识行业概览/年报）、A股（招股说明书/审核问询函回复）提取真实毛利率、销售费用率、获客成本（CAC）、留存复购率（Cohort）与风险因素。
- **竞品全景与获客漏斗拆解**：扫描竞品网站目录树（Sitemap）、拆解测评问卷（Quiz）与付费墙（Paywall）、逆向分析其 SEO/投流钩子与招聘 JD 暴露的产品路线图。
- **用户差评与迁移痛点挖掘（VOC）**：抓取京东、Amazon、小红书、Reddit、App Store、G2 的 1-3 星差评与切换原话，指导产品功能优先级。

## Goal

为产品方向定义、核心功能切入点（Feature Wedge）和获客增长（GTM）提供**100% 源自一手抓取数据**的决策依据。彻底杜绝拿二手自媒体软文或拍脑袋宏观大数交差的「表演式调研（Research Theater）」。

核心融合 6 大情报工程模块：
1. **行业巨头招股书（S-1 / 港交所 H 股 / A 股）与财报（10-K / 20-F / 年报 / 电话会）深度解剖**
2. **TAM / SAM / SOM 双向三角定量校验（Top-Down × Bottom-Up Triangulation）**
3. **并发失忆侦察兵（Amnesiac Competitor Scouts）：网站拓扑、付费墙漏斗、SEO 与招聘信号逆向**
4. **一手用户差评与迁移原话挖掘（1-3 Star Review & Switching VOC Mining）**
5. **魔鬼代言人反方压测（Devil's Advocate Challenge）**
6. **Grounding 原文引用台账 + 浅色简洁一页到底 HTML 交付**

## Success Criteria

- 每一条市场规模、毛利率、CAC、LTV、留存率、价格与竞品结论，均附有本次实际抓取的 URL 与逐字原文引语（通过 `grounded-citations` / `content-grounding` 校验）。
- 招股书与财报分析必须拆出**单位经济模型（Unit Economics）**、**销售费用构成**与**管理层承认的硬伤（Risk Factors）**，并转化为对我们产品与获客的具体指导。
- 市场规模必须通过 `scripts/market_intel_tool.py size` 完成 Top-Down 与 Bottom-Up 双向三角校验（偏差 >3x 自动标红预警）。
- 最终输出包含：**一页到底浅色简洁 HTML 报告** + **结构化竞品 Dossier JSON** + **反方压测结论**。

## Tools & Scripts

```bash
# 1. 多引擎搜索与网页提取路由器（支持 auto/exa/tavily/serper/brave/firecrawl/ddgs）
SEARCH_PY=~/.hermes/skills/research/web-search/scripts/search.py

# 2. 招股书/财报检索与 TAM-SAM-SOM 双向三角校验工具（本技能内置）
MI_TOOL=~/.hermes/skills/research/market-intelligence/scripts/market_intel_tool.py

# 3. 事实核查与引用台账（Perplexity 风格编号引用）
SOURCES_PY=~/.hermes/skills/research/grounded-citations/scripts/sources.py
```

---

## Procedure (六步标准作业程序)

### Step 1: 行业巨头招股书与财报解剖 (Prospectus & Earnings Teardown)

**核心认知**：自媒体文章全是公关噪音，只有经过审计师和律所签字负法律责任的**招股书（Prospectus / S-1 / F-1）**和**年度财报（10-K / 20-F / 年报）**才是免费的百万美金级一手数据库。

使用 `python3 $MI_TOOL queries --company "<公司/赛道>" --market us|hk|cn` 生成精准检索式，并通过 `search.py --engine serper` 或 `firecrawl` 抓取原文，重点解剖以下 **5 个黄金章节**：

| 必拆章节 | 英文/港美股定位词 | 中文/港A股定位词 | 提取什么一手数据 | 对我们的指导意义 |
| :--- | :--- | :--- | :--- | :--- |
| **1. 行业概览（白嫖顶级付费研报）** | `Industry Overview` / `Market Opportunity` | `行业概览`（弗若斯特沙利文 / 灼识咨询 / 艾瑞 / 欧睿） | 细分赛道真实盘子、CAGR、渗透率、产业链上下游分润比例、前五大玩家市占率（CR5）。 | **定方向**：看清钱在产业链哪一层被赚走了（生产 vs 渠道 vs 品牌 vs 订阅服务）。 |
| **2. 业务与产品矩阵（解剖现金牛）** | `Business` / `Our Products` / `Cohort` | `业务` / `主要产品及服务` / `客户留存` | 各产品线/SKU 营收占比、复购率（Retention / Net Dollar Retention）、平均客单价（ARPU/AOV）、生命周期（LTV）。 | **定功能**：巨头靠哪个单品引流（Loss Leader），靠哪个高毛利服务/复购赚钱？ |
| **3. 财务与销售费用拆解（透视获客 ROI）** | `MD&A` / `Selling and Marketing Expenses` | `财务信息` / `销售及营销开支明细` | 毛利率（Gross Margin）、销售费用率（S&M % of Revenue）、**获客费用的具体去向**（投流买量 vs 达人佣金 vs 线下渠道 vs 研发人员薪酬）、回本周期（Payback Period）。 | **定获客**：如果巨头买量费用率高达 50%-60% 导致微利，我们绝不能正面硬刚付费投流，必须走内容/SEO/私域/钩子工具差异化获客。 |
| **4. 风险因素（管理层被迫说真话的地方）** | `Item 1A. Risk Factors` | `风险因素` | 客户流失原因、单一渠道/平台依赖度、退货/投诉率、合规监管红线（如保健品宣传边界、FDA/NMPA/广告法风险）、技术迭代威胁。 | **找切口（Wedge）**：巨头因为船大掉不了头或害怕合规而不敢碰、但用户极度渴望的痛点，就是我们的破局点。 |
| **5. 财报电话会 Q&A（华尔街逼问的最新趋势）** | `Earnings Call Transcript` / `Q&A` | `业绩电话会实录` / `投资者关系问答` | 分析师尖锐追问的增长放缓原因、最新一个季度什么新功能/新渠道转化率最高、管理层未来 12 个月砍掉了什么业务、重注什么方向。 | **抢时效**：比静态行业报告领先 6-12 个月感知一线冷暖。 |

> **参考手册**：详细财务指标反推公式（如从销售费用与新增付费用户反推真实 CAC）见 `references/prospectus-earnings-playbook.md`。

---

### Step 2: 市场规模双向三角校验 (TAM / SAM / SOM Triangulation)

严禁只报一个“XX 行业万亿市场”的 Top-Down 大数。必须运行 `market_intel_tool.py size` 同时计算两条路径：
1. **Top-Down（自上而下）**：招股书/智库总盘子（TAM） × 产品可服务范围比例（SAM %） × 1-3 年现实市占率（SOM %）。
2. **Bottom-Up（自下而上）**：可触达目标人群/企业基数 × 付费转化率 × 年均客单价（ACV / ARPU）。
3. **三角校验铁律**：若 `Top-Down SOM` 与 `Bottom-Up SOM` 相差超过 **3 倍**，脚本将触发 `TRIANGULATION_FAILED` 警告，必须重新核查客单价或真实受众基数，绝不取平均数掩盖分歧。

---

### Step 3: 并发失忆侦察兵 — 竞品拓扑与漏斗逆向 (Parallel Competitor Scouts)

锁定 3–5 家高利润/高增长标杆竞品（先用 `dbs-benchmark` 五重过滤排除噪音）。用 `delegate_task` 为每家竞品派生一个独立的子 Agent（或分批脚本），互不串味，严格按 `references/competitor-dossier-schema.md` 抓取以下 5 维一手信号：

1. **全站目录树扫描 (`firecrawl_map`)**：
   - 先看 URL 结构再看文案：是否有 `/quiz/`（测评漏斗）、`/tools/` 或 `/calculator/`（免费工具 SEO 获客）、`/vs/` 或 `/alternatives/`（竞品词截流）、`/enterprise`（向 B 端转型）？
2. **Onboarding → Paywall 付费墙九维拆解**：
   - 首屏 5 秒价值主张（逐字摘录 Hero Tagline & CTA）、启动到付费墙经过几个问题节点、订阅周期比例（月/季/年）、价格锚定与风险消除话术（退款承诺/专家背书）。
3. **SEO 与付费买量获客情报**：
   - 谁在核心痛点词排前 3？哪些长青广告素材在 Meta Ad Library / Google Ads Transparency Center / 抖音小红书连续投放超 30 天（存活期 >30 天 = ROI 跑通）？
4. **招聘信号逆向产品路线图 (Hiring Signals)**：
   - 抓取竞品 LinkedIn / Boss直聘 / 官网 `/careers` 在招岗位：招什么算法/合规/私域运营？JD 里要求什么工具栈与 KPI？直接暴露其未来半年的研发与获客重心。
5. **诚实记录“对手赢在哪里（Where They Win）”**：
   - 每份竞品档案必须写明对手最强的壁垒，禁止单方面贬低竞品。

---

### Step 4: 用户行为、搜索动作、付费意愿与供应链底牌挖掘 (User Behavior, WTP & Commercial Push)

产品功能（Feature）与市场机会点不由脑暴决定，由**真实用户的搜索动作、掏钱信号、使用断崖与供应链真实毛利**共同决定（详见 `references/user-behavior-and-willingness-to-pay.md`）：

1. **实时搜索动作与购买意图雷达 (`market_intel_tool.py intent`)**：
   - 运行 `python3 $MI_TOOL intent "<核心词/品类词>"`，一键并发拉取 **Google / 百度 / 必应 / YouTube / 淘宝天猫 / Amazon** 6 大平台的实时搜索下拉框联想词（Autocomplete），并自动裂变为「痛点与副作用」「购买与选型意图」「用法与依从性行为」三维矩阵。
   - **洞察逻辑**：搜索框下拉词是全网几十万用户用手指投票出来的最高频真实动作（如搜`甘氨酸镁`直接蹦出`甘氨酸镁副作用睡不着`、`甘氨酸镁一般吃几天停`、`甘氨酸镁怎么吃不伤胃`），直接对应产品最该做的核心功能与获客选题。
2. **付费意愿与弃坑率交叉检验 (`opencli` 电商与二手链路)**：
   - **前端买单信号**：用 `opencli jd search/item/reviews`、`opencli taobao search/reviews`、`opencli amazon bestsellers/movers-shakers` 提取主力价格带（日均花费锚点）与高转化卖点。
   - **后端弃坑检验（闲鱼测试法）**：用 `opencli xianyu search --keyword "<竞品名> 闲置"` 检查二手转让率與转让理由（如“买了吃不惯”、“颗粒太大咽不下”），识别“前端靠营销冲动消费、后端依从性崩盘”的假复购品类。
   - **供应链真实 BOM 底价（1688 透视法）**：用 `opencli 1688 search/item` 查源头代工厂同款配方的批发拿货价与起订量（MOQ），对比终端售价算出行业真实毛利空间，看穿商业推动力到底是“高毛利驱动的达人分销”还是“研发壁垒”。
3. **两类必抓用户原话（Verbatim Quotes）**：
   - **手工替代方案与挫败点（Workaround & Friction）**：用户在小红书（`opencli xiaohongshu search/comments`）、Reddit（`opencli reddit search/read`）、知乎（`opencli zhihu search`）上晒出的 Excel 表、分装药盒照片或“这几种能不能一起吃”的求助帖 → 直接转化为 AI 产品的自动化功能切口（Feature Wedge）。
   - **迁移触发词（Switching Language）**：专门检索 `"换到了"`、`"弃坑"`、`"switched from"`、`"instead of"`，用 `dbs-jtbd` 拆解推力（旧方案痛点）、拉力（新方案承诺）、焦虑（切换顾虑）与习惯（惰性阻力）。

---

### Step 5: 魔鬼代言人反方压测 (Devil's Advocate War Room)

在汇总出初步的「产品功能建议」与「获客策略」后，强制切换到**反方审视角色（Devil's Advocate）**进行自检辩论，回答 4 个尖锐问题：
1. **巨头为什么不做？** 既然这个需求这么痛，为什么财大气粗的行业巨头没做？（是因为毛利太薄、获客 CAC 算不过账、还是有医疗/广告合规红线？）
2. **证据链是否牢固？** 哪条建议背后只有 1 个孤证或过期数据？如果这条假设是错的，我们的方案会怎么死？
3. **前 100 个客户到底从哪来？** 拒绝“做 SEO / 发小红书”这种宽泛废话，必须指明具体哪个搜索词簇、哪类爆款选题模板、哪个测评钩子能低成本跑通冷启动。
4. **最小验证动作（24h Validation）**：未来 24–48 小时内，不写重代码就能验证核心假设的一个具体动作是什么？

---

### Step 6: Grounding 核查与浅色一页式 HTML 交付

1. **原文引用台账校验**：
   - 所有引用的招股书数据、研报数字、竞品价格、用户原话，必须登记进 `sources.py` 台账（`add <url> --title "..." --quote "..."`），并在正文中标注 `[1][2]`。
   - 查不到或被拦截的数据一律如实标注 `not_found` 或 `[未核实推断]`，严禁编造数字或篡改分母（注意核对财报科目分母，如部门收入 vs 集团总收入）。
2. **视觉与文档交付标准**：
   - 生成一份 Markdown 完整存档 + 一份**浅色简洁、一页到底的独立 HTML 调研报告**（白底/浅灰卡片、清晰数据表格、高对比度结论框、可点击原文引用链接，拒绝深色复杂仪表盘）。

---

## Constraints & Pitfalls

- **严禁把招股书/财报的“行业总盘子”当成“可获得市场”**：招股书里的沙利文报告往往为了帮企业讲故事而把 TAM 划得极大；必须对照财报正文里前五大厂商真实营收之和来交叉核验。
- **财务分母铁律**：转述财报百分比（如“线上渠道占 70%”、“复购率 60%”）时，必须写清分母口径（是占自营收入还是总 GMV？是 90 天复购还是年复购？）。
- **调研词根必须先跑工具再下结论**：写“用户在搜 X”之前必须已实际执行 `market_intel_tool.py intent`（或等价的 autocomplete 直连），并逐字摘录下拉词；凭直觉列举搜索词等于编造一手数据，直接违反 Grounding 红线。
- **中文 seed 不要只跑 Google**：Google 的中文电商/消费类长尾覆盖明显弱于百度、淘宝，单平台取词会系统性漏掉“哪个牌子/多少钱/怎么吃”这类付费与依从性意图；六个平台（Google/百度/必应/淘宝/Amazon/YouTube）至少跑中文三源 + 英文两源。
- **版本命名规范**：报告文件升级直接升版本号（如 `v1.0` → `v1.1`），严禁使用「终版」「无xx终版」字样。

## References

- `references/prospectus-earnings-playbook.md` — 招股书（S-1/港股/A股）与财报（10-K/电话会）5 大章节检索式、单位经济模型（CAC/LTV/毛利）反推公式与财务避坑指南。
- `references/user-behavior-and-willingness-to-pay.md` — 用户搜索动作（6 大平台 autocomplete 实测端点与词根裂变模板）、付费意愿（京东/淘宝/闲鱼弃坑率/1688 源头底价）、使用断崖、`opencli` 181 站点命令映射与四象限机会公式。
- `references/competitor-dossier-schema.md` — 失忆侦察兵（Scout）标准 JSON Dossier 结构、网站目录树信号表与魔鬼代言人质询清单。
- `scripts/market_intel_tool.py` — 实时用户搜索意图与电商下拉词采集器 (`intent`) + 招股书/财报/差评检索式生成器 (`queries`) + TAM/SAM/SOM 双向三角校验 CLI (`size`)。
