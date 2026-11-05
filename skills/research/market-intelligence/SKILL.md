---
name: market-intelligence
description: "Use when doing market/competitor/10-K/GTM intel."
version: 2.0.0
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

## Success Criteria (全维度大样本默认门禁 — 每次调研必须一次到位，不许等用户追问才补抓)

- **大样本一手数据硬门槛（默认 ≥300–1,000 条原始记录落盘）**：每次调研必须在 `~/.hermes/cache/scratch/<topic>_research/` 下落盘保存原始 JSON/MD 抓取数据包，严禁只搜 5 条网页摘要就写报告。
- **八维全覆盖（缺一不可）**：
  1. **自家产品契约审计**：先读本地代码仓/线上文案，列出「教科书视角 vs 用户任务视角」病灶对照表；
  2. **6 大平台实时搜索动作 (`intent`)**：跑满 3–5 个核心词根（200+ 条下拉联想词）；
  3. **电商交易与买家评论 (`ecommerce` + `opencli`)**：同人群下对比 5 种交付形态（纯视频/静态表/图书 vs 1v1 服务 vs 高毛利实物）的真实售价、付款人数与 80+ 条买家评论原话；
  4. **1688 源头供应链 BOM 底价 (`opencli 1688`)**：抓取 30–60 家 OEM/ODM 代工厂批发价与回头率，核算终端溢价倍数；
  5. **闲鱼（Goofish）二手弃坑率与灰产代充监测**：通过 `opencli xianyu` 或 `site:goofish.com` / `site:smzdm.com` 抓取二手抛售价格、弃坑理由与会员代充价梯；
  6. **国内外行业招聘 JD 逆向 (`hiring`)**：从智联招聘/猎聘/BOSS直聘及海外 Greenhouse/Lever/Primary VC 抓取真实 JD 原文，拆出竞品私域 SOP、单教练管理人数上限（Caseload）与单客人工计件成本（如 $5/user/mo）；
  7. **四大标杆招股书/财报 + 社媒高赞评论 + PubMed 临床文献 (`queries` + `pubmed`)**：抓取 200+ 条 B站/小红书/知乎/Reddit 高赞用户原话，以及 20–50 篇 PubMed/Europe PMC 最新临床医学文献（带 PMID/DOI）；
  8. **TAM/SAM/SOM 双向三角校验 (`size`) + 1,000 人池单位经济模型 + Grounding 引用台账 (`sources.py verify`)**。
- 每一条市场规模、毛利率、CAC、LTV、留存率、价格、招聘 KPI 与用户原话，均附有本次实际抓取的 URL 与逐字引语（通过 `sources.py verify` 输出 `citations OK`）。
- 最终输出包含：**浅色简洁一页到底的独立 HTML 报告** + **Markdown 存档** + **本地原始 JSON 样本库路径说明**。

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
4. **招聘信号逆向产品路线图与人效底牌 (`market_intel_tool.py hiring`)**：
   - 运行 `python3 $MI_TOOL hiring "<角色/赛道词>" -c "<竞品名>"` 生成国内外招聘平台穿透检索式，并用 `web_extract` 抓取智联招聘（`zhaopin.com/jobdetail/...`）、猎聘、BOSS直聘、Greenhouse（`job-boards.greenhouse.io/<company>`）、Lever、Ashby、Primary VC Job Board 上的 JD 全文。
   - **必拆三大机密指标**：
     1. **私域 SOP 与转化闭环路径**：从国内「私域营养师 / 训练营班主任 / 用户增长运营」JD 的岗位职责中，直接提取对手的完整转化链路（如“视频号公域引流 → 企微标签分层管理 → 降糖/减脂训练营 → 服务包复购裂变”）；
     2. **一线顾问人效上限（Active Caseload）与单客人工成本**：从海外/国内教练 JD 中提取单人同时管理客户数（如 Noom Mindset Coach JD 明确写明 `Active Caseload: Up to 500 users`，响应 SLA `<1 hour`，计件薪酬 `$5 per user per month`）及国内顾问底薪+提成比例（如兴趣岛开一单 1880 元提成 94 元 = 5% 提成率），直接用于测算我们自己的单位经济模型（Unit Economics）；
     3. **高薪研发与高管岗位暴露的未来半年战略**：如年薪 $230K–$325K 招聘 `Clinical AI Director` 与 `Growth & Supplement Commerce Director`，直接证明对手正把重兵压在 Agentic AI 赋能顾问与补剂电商闭环。
5. **诚实记录“对手赢在哪里（Where They Win）”**：
   - 每份竞品档案必须写明对手最强的壁垒，禁止单方面贬低竞品。

---

### Step 4: 用户行为、搜索动作、付费意愿与供应链底牌挖掘 (User Behavior, WTP & Commercial Push)

产品功能（Feature）与市场机会点不由脑暴决定，由**真实用户的搜索动作、掏钱信号、使用断崖与供应链真实毛利**共同决定（详见 `references/user-behavior-and-willingness-to-pay.md`）：

1. **实时搜索动作与购买意图雷达 (`market_intel_tool.py intent`)**：
   - 运行 `python3 $MI_TOOL intent "<核心词/品类词>"`，一键并发拉取 **Google / 百度 / 必应 / YouTube / 淘宝天猫 / Amazon** 6 大平台的实时搜索下拉框联想词（Autocomplete），并自动裂变为「痛点与副作用」「购买与选型意图」「用法与依从性行为」三维矩阵。
   - **洞察逻辑**：搜索框下拉词是全网几十万用户用手指投票出来的最高频真实动作（如搜`甘氨酸镁`直接蹦出`甘氨酸镁副作用睡不着`、`甘氨酸镁一般吃几天停`、`甘氨酸镁怎么吃不伤胃`），直接对应产品最该做的核心功能与获客选题。
2. **八大电商全链路与带货底牌交叉检验 (`market_intel_tool.py ecommerce <词>` + `opencli`)**：
   - 运行 `python3 $MI_TOOL ecommerce "<品类或品牌词>"` 生成 **货架电商 + 兴趣直播电商 + 源头供应链** 8 大阵地采集指令：
   - **货架电商（京东/淘宝/Amazon）**：用 `opencli jd search/item/reviews`、`opencli taobao search/detail/reviews`、`opencli amazon bestsellers/movers-shakers` 提取主力价格带（日均花费锚点）、自营 vs 旗舰店销量结构及 **30–90 天追评原话**。
   - **兴趣与直播带货电商（抖音精选联盟/蝉妈妈/考古加 + 小红书买手种草 + 视频号微信小店）**：
     - 抖音：用 `opencli douyin search/detail/user-videos` 拆解爆款带货视频的前 3 秒黄金钩子与完整口播文案，并配合 `search.py` 检索蝉妈妈/考古加/精选联盟公开数据（看达人带货佣金率 20%–50%、直播间 GMV 构成）；
     - 小红书：用 `opencli xiaohongshu search/note/comments` 筛选「收藏/点赞比 > 0.8」的高转化种草笔记，并统计楼中楼评论区“求链接/怎么买/多少钱”的真实买单密度；
     - 微信视频号（40–60 岁高客单价营养品第一阵地）：借公众号后台 `mp.weixin.qq.com` 的 `/cgi-bin/videosnap` 接口免扫码拉取竞品视频号全量爆款，或用 `opencli weixin search` 追踪爆款动态。
   - **供应链真实 BOM 底价与拼多多白牌底线（1688 + 拼多多）**：用 `opencli 1688 search/item` 查源头代工厂 OEM/ODM 阶梯批发价与起订量（MOQ），结合拼多多百亿补贴价格底线，算出品牌真实毛利倍数（终端价 ÷ 1688 代工价）。
   - **后端弃坑与会员灰产检验（闲鱼 Goofish 照妖镜）**：
     - 首选 `opencli xianyu search "<竞品名> 闲置 未拆封" -f json`；若遇 Chrome 扩展 `attach_failed` / `detached_mid_command`，**严禁跳过闲鱼维度**，立即切换 `search.py --engine serper` 跑 `site:goofish.com "<品类/品牌>"` 与 `site:smzdm.com "闲鱼" "<品牌>" ("闲置" OR "未拆封" OR "代充")` + `web_extract` 抓取闲鱼商品详情页（`goofish.com/item?id=...` 会同时返回主商品与同页 20+ 款同类闲置推荐列表！）。
     - **两大必查指标**：① **硬件/补剂闲置抛售率与弃坑理由**（如营养秤/体脂秤因“称重算热量太麻烦、没电懒得换”被半价甩卖 → 证明必须用 AI 拍照 3 秒识餐替代手动称重）；② **虚拟会员/课程代充灰产地板价**（如 Keep 官方月卡 ¥19 在闲鱼被代充杀到 ¥9.3/月、年卡 ¥90，以及免密自动扣费引发的 12345 投诉潮 → 证明纯虚拟课毫无价格护城河，必须绑定 1v1 档案 + 顾问伴学 + 实物营养包）。
   - **临床医学与分子机制循证 (`market_intel_tool.py pubmed`)**：
     - 针对健康/营养/医疗/抗衰赛道，运行 `python3 $MI_TOOL pubmed "<英文临床检索式>" -n 8`（底层调用稳定的 Europe PMC REST API `ebi.ac.uk/europepmc/webservices/rest/search`，彻底规避 NCBI E-utilities 间歇性 HTTP 500 故障），批量拉取最新临床研究与 RCT 的 PMID、DOI、年份与摘要，从分子机制（如下丘脑食欲神经肽、皮质醇内脏脂肪轴、围绝经期骨量流失率）解释用户痛点。
3. **两类必抓用户原话（Verbatim Quotes）**：
   - **手工替代方案与挫败点（Workaround & Friction）**：用户在小红书（`opencli xiaohongshu search/comments`）、Reddit（`opencli reddit search/read`）、知乎（`opencli zhihu search`）上晒出的 Excel 表、分装药盒照片或“这几种能不能一起吃”的求助帖 → 直接转化为 AI 产品的自动化功能切口（Feature Wedge）。
   - **迁移触发词（Switching Language）**：专门检索 `"换到了"`、`"弃坑"`、`"switched from"`、`"instead of"`，用 `dbs-jtbd` 拆解推力（旧方案痛点）、拉力（新方案承诺）、焦虑（切换顾虑）与习惯（惰性阻力）。
4. **先审自家产品契约，再做人群合成**：在跑任何外部调研之前，先读自己产品里已写死的文案与字段（课程 JSON 的 `suitableFor` 与课节标题、落地页 Hero、onboarding 题面、SKU 卖点），产出一张「文案病灶对照表」——教科书视角（「升糖与 GI、GL」）要改写为用户当天正在经历的身体场景（「同样是吃饱，为什么有的主食养气色，有的专门长小肚子？」）。人群画像的目的是修正产品，不是产出一份漂亮 PDF；顺序反过来会得到一份跟现有产品对不上的画像。
5. **画像、付费意愿与闭环可行性**：从 autocomplete 里带年龄性别的长尾词直接切出 ICP、从恐惧词提取必须先拆掉的反对意见、从「吃什么补什么」类词证明实物/订阅联动意图；再用四象标杆（上市龙头财报 / 国内百亿同类 / 全球龙头 / 被战投的相邻巨头）+ 四阶漏斗 + 按 1,000 人测算的单位经济表论证闭环节。完整表格结构与质询清单见 `references/persona-and-business-closed-loop.md`。

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
   - **交付顺序固定**：写完带 `[1][2]` 标记的草稿 → 跑 `sources.py render --replace-in <草稿.md>` 生成标准 `Sources:` 块 → 再跑 `sources.py verify <草稿.md>`，看到 `citations OK` 才算交付。手写 `## Sources` 小标题加项目符号列表**不会被识别**，`verify` 会直接报 `draft cites sources but has no Sources: block`；不要为绕开它去改标记，重跑 render 即可。
   - **中文引语要摘整句，不要摘短语**：`sources.py quote` 按空白分词判断长度，`线上会员及付费内容73.0%的毛利率` 这类短中文串会被判 `quote too short`；直接复制原文中一个完整小句或并列结构（含逗号、两个以上分句）即可通过，不要为了凑词去改写原文。
2. **视觉与文档交付标准**：
   - 生成一份 Markdown 完整存档 + 一份**浅色简洁、一页到底的独立 HTML 调研报告**（白底/浅灰卡片、清晰数据表格、高对比度结论框、可点击原文引用链接，拒绝深色复杂仪表盘）。

---

## Constraints & Pitfalls

- **严禁把招股书/财报的“行业总盘子”当成“可获得市场”**：招股书里的沙利文报告往往为了帮企业讲故事而把 TAM 划得极大；必须对照财报正文里前五大厂商真实营收之和来交叉核验。
- **财务分母铁律**：转述财报百分比（如“线上渠道占 70%”、“复购率 60%”）时，必须写清分母口径（是占自营收入还是总 GMV？是 90 天复购还是年复购？）。
- **调研词根必须先跑工具再下结论**：写“用户在搜 X”之前必须已实际执行 `market_intel_tool.py intent`（或等价的 autocomplete 直连），并逐字摘录下拉词；凭直觉列举搜索词等于编造一手数据，直接违反 Grounding 红线。
- **把 `opencli` 命令写进文档前先跑 `opencli <site> --help`**：适配器签名是**位置参数**（`opencli jd search "词" -f json`、`opencli taobao detail <id>`），不是 `--keyword` / `--url` / `--query` 这类旗标；按记忆或旧文档写旗标，命令当场报参数错误，而同事拿到 handoff 后会在自己的环境里重复踩一次。同一站点不同子命令的入参形态也不一致（`search <query>` vs `detail <id>` vs `bestsellers <url|node>`），逐个核对。
- **技能改动必须同批同步到全部投递目标**：本机 `~/.hermes/skills/`、同事环境 `~/.config/alma/skills/`、`marovole-Superpowers` 仓库的 `skills/research/<name>/` 与 `docs/handoff-*.md`。handoff 文档里内嵌了 `market_intel_tool.py` 的**字面副本**，只改技能里的脚本而不改 handoff，等于给同事发一份带旧代码的安装包；脚本新增子命令时，handoff 的 argparse 段、Step 说明与验收脚本三处要一起改。
- **中文 seed 不要只跑 Google**：Google 的中文电商/消费类长尾覆盖明显弱于百度、淘宝，单平台取词会系统性漏掉“哪个牌子/多少钱/怎么吃”这类付费与依从性意图；六个平台（Google/百度/必应/淘宝/Amazon/YouTube）至少跑中文三源 + 英文两源。
- **做人群与闭环调研时，别先写行业总盘子**：先读自家产品契约拿病灶，再跑搜索动作拿 ICP，最后才用四象标杆与单位经济表论证闭环。开篇就上「XX 行业 3000 亿」的写法，读者拿不到任何可执行结论，也不符合本技能要防的表演式调研。
- **别把「内容/课程本身就是产品」当成结论**：高价内容类业务单靠卖课/卖会员普遍被免费内容击穿（分部收入下滑、单用户 ARPU 低个位数），必须把内容定位成前端信任钩子，利润落在实物/耗材/订阅与复评调方上。写闭环时若利润仍只来自课程收入，方案要重做。
  **可执行的证明方法（比访谈硬）**：在同一平台、同一人群词下横向搜五种交付形态——纯录播课 / 静态食谱资料 / 同名图书 / 1v1 定制计划+实时看餐答疑 / 功效型实物（补剂或低 GI 主食替换），记录「单价 × 真实付款人数」。量级落差通常跨 4 个数量级（个位数付款 → 数百单 → 千至十万级），这条曲线就是「内容不是产品」的判决书。表格模板与三条配套铁律见 `references/user-behavior-and-willingness-to-pay.md` 第五节。
- **用户说「更深、更广、要我们自己抓的数据」时，先交数据实证，不交落地方案**：这类追加指令的真实含义是「你上一轮引的是一手平台之外的二手文章，我要平台原始数据」。正确响应是回淘宝/1688/Amazon/B站/Reddit 抓交易笔数、评价原话与代工报价，产出一份纯实证报告（谁在付钱、付多少、原话怎么说、毛利几倍），把方案留到对方明确要求后再给。把「调研」和「方案」分成两次交付，是这一轮指令的验收条件。
- **「原文引用」不等于「一手抓取」**：引用第三方专栏、媒体测评、营养师文章只是二手证据，哪怕引语逐字准确也不能单独支撑人群画像。人群画像、付费意愿、痛点排序这三类结论必须落在自己抓的平台原始记录上（付款人数、买家评价原文、代工厂报价、高赞评论区原话）；二手文章只能用来解释一手数据背后的机制（如「肌肉每十年流失 3–8%」这类生理学解释），不能用来定义人群。
- **版本命名规范**：报告文件升级直接升版本号（如 `v1.0` → `v1.1`），严禁使用「终版」「无xx终版」字样。

## References

- `references/prospectus-earnings-playbook.md` — 招股书（S-1/港股/A股）与财报（10-K/电话会）5 大章节检索式、单位经济模型（CAC/LTV/毛利）反推公式与财务避坑指南。
- `references/user-behavior-and-willingness-to-pay.md` — 用户搜索动作（6 大平台 autocomplete 实测端点与词根裂变模板）、付费意愿（同人群×五形态付费极性对照法、京东/淘宝/闲鱼弃坑率/1688 源头底价）、使用断崖、`opencli` 181 站点命令映射与各站 JSON 字段速查、四象限机会公式。
- `references/persona-and-business-closed-loop.md` — 人群画像与商业闭环手册：先审自家文案的病灶对照表、从 autocomplete 长尾反推 ICP（年龄性别限定词/恐惧词/「吃什么补什么」词）、三级画像与 JTBD 陈述结构、四象标杆选择表、四阶漏斗与 1,000 人单位经济测算。
- `references/competitor-dossier-schema.md` — 失忆侦察兵（Scout）标准 JSON Dossier 结构、网站目录树信号表与魔鬼代言人质询清单。
- `scripts/market_intel_tool.py` — 实时用户搜索意图与电商下拉词采集器 (`intent`) + 八大电商/直播带货/1688 底价采集矩阵生成器 (`ecommerce`) + 招股书/财报/差评检索式生成器 (`queries`) + TAM/SAM/SOM 双向三角校验 CLI (`size`)。
