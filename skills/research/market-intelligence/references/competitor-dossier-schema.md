# 竞品失忆侦察兵（Scout Dossier）标准结构与魔鬼代言人压测协议

## 一、失忆侦察兵（Amnesiac Competitor Scout）执行规范

当需要调研 3–5 家标杆竞品时，为防止主 Agent 在单次对话中因上下文过长而偷懒或混淆数据，采用**并行独立侦察（One Scout per Competitor）**模式。

### 1. 每个侦察兵必须采集的 6 大维度

1. **网站架构与获客入口 (`sitemap_and_funnel`)**：
   - 调用 `firecrawl_map` 获取目标域名 URL 列表。
   - 检查是否存在以下高转化增长模块：
     - `/quiz`、`/assessment`、`/test`（互动式症状/需求自测漏斗——健康与订阅制产品的核武器）
     - `/calculator`、`/tools`（免费工具截流 SEO）
     - `/vs/`、`/alternatives`、`/compare`（竞品品牌词劫持页）
     - `/blog`、`/learn`、`/science`、`/research`（循证内容与权威背书中心）
2. **首屏定位与付费墙九维拆解 (`positioning_and_paywall`)**：
   - **逐字摘录（Verbatim）**：Hero 主标题（H1）、副标题、主 CTA 按钮文案。
   - **付费墙与定价（PaywallPro 框架）**：套餐档位、月付/季付/年付价格与锚定方式、是否提供首月低价试用、退款承诺（如 30/60/90-day money-back guarantee）、核心信任背书（医生签名、临床实验数据、第三方检测标）。
3. **搜索与投流情报 (`seo_and_ads`)**：
   - 该竞品在 Google / 百度 / 小红书 / 抖音上占据统治地位的前 5 个痛点关键词。
   - 长期存活（>30 天）的广告或爆款内容钩子（Hook）。
4. **招聘信号逆向 (`hiring_signals`)**：
   - 从 LinkedIn / Boss直聘 / 官网 `/careers` 提取当前开放的核心岗位。
   - 解读信号：招营养师/健康管理师 = 强化人工私域服务；招推荐算法/LLM 工程师 = 投入 AI 个性化；招抖音信息流投手/KOL 媒介 = 押注短视频买量。
5. **用户差评与迁移痛点 (`voc_complaints`)**：
   - 从京东/Amazon/App Store/G2/小红书提取该竞品最集中的 3 条 1-3 星差评原话（附链接）。
6. **对手赢在哪里 (`where_they_win`)**：
   - 诚实写出该竞品最难被击败的 1-2 个优势（品牌心智、供应链成本、独家资质、私域规模）。

### 2. 标准 JSON Dossier 模板（每字段必带 `source_url` 与 `status`）

```json
{
  "competitor_name": "Example Health Inc.",
  "domain": "example.com",
  "fetched_at": "2026-11-05T08:00:00Z",
  "sitemap_signals": {
    "has_quiz_funnel": { "value": true, "url": "https://example.com/quiz", "status": "ok" },
    "has_free_tools": { "value": false, "url": null, "status": "not_found" },
    "top_content_hubs": { "value": ["/science", "/ingredients"], "url": "https://example.com/sitemap.xml", "status": "ok" }
  },
  "positioning": {
    "hero_h1_verbatim": { "value": "Personalized daily nutrition, backed by clinical science.", "source_url": "https://example.com", "status": "ok" },
    "primary_cta_verbatim": { "value": "Take the 3-Minute Quiz", "source_url": "https://example.com", "status": "ok" }
  },
  "pricing_and_paywall": {
    "tiers": { "value": ["Starter $39/mo", "Complete $69/mo (Save 20% quarterly)"], "source_url": "https://example.com/pricing", "status": "ok" },
    "risk_reversal": { "value": "60-day happiness guarantee, cancel anytime", "source_url": "https://example.com/pricing", "status": "ok" }
  },
  "hiring_signals": {
    "open_roles_summary": { "value": "Hiring 4 Lifecycle CRM Managers & 2 Clinical Advisors -> focusing on post-purchase retention", "source_url": "https://example.com/careers", "status": "ok" }
  },
  "voc_top_complaints": [
    {
      "complaint_theme": "Pills cause stomach upset when taken together",
      "verbatim_quote": "I loved the quiz, but taking all 6 capsules in the morning gave me terrible nausea and there was no way to adjust the formula.",
      "source_url": "https://www.trustpilot.com/review/example.com"
    }
  ],
  "where_they_win": "Extremely smooth 12-step onboarding quiz with instant personalized explanation and strong clinical advisory board credibility."
}
```

---

## 二、魔鬼代言人（Devil's Advocate）四维反方压测清单

在将调研数据转化为「我们的产品功能与获客方案」之前，必须强制执行以下反方挑战：

| 压测维度 | 魔鬼代言人质询问题 | 不合格的回答（自嗨） | 合格的回答（有证据支撑） |
| :--- | :--- | :--- | :--- |
| **1. 巨头不作为原因（Why Haven't Giants Done It?）** | “竞品每年花几个亿营销，为什么没做你提议的这个功能？是因为他们傻，还是因为这事算不过账/踩了医疗合规红线？” | “因为传统品牌不懂 AI，我们用大模型就能降维打击。” | “传统品牌在京东/天猫卖标品毛利 75%，但一旦承诺动态调方会触发‘非法行医/疾病诊断’合规风险，且人工营养师随访成本吃掉 30% 毛利。我们必须把边界严格锁在‘营养与生活方式自测及补剂搭配建议’，不碰疾病诊断，并用 AI 替代 80% 常规随访。” |
| **2. 获客成本现实性（CAC Reality Check）** | “招股书显示头部玩家线上获客成本高达 XXX 元/人，首单根本不赚钱。你凭什么能用更低的成本拿到前 100 个客户？” | “我们靠高质量科普内容自然涨粉转化。” | “不投泛流量千川广告；先模仿已被验证高转化的‘3分钟症状与营养缺口自测卡’作为钩子，承接垂直长尾搜索词与高意向问答社区流量。” |
| **3. 切换推力与阻力（JTBD Switching Friction）** | “用户已经在京东自营买惯了 Swisse/汤臣倍健，什么具体痛点会逼她今天换用你的方案？” | “我们的方案更科学、更个性化。” | “差评数据显示 32% 的 40-60 岁女性买了 3 种以上补剂却担心冲突/伤胃/吃错剂量。切入点不是卖新牌子，而是先帮她‘诊断手里正在吃的补剂怎么搭、怎么吃、吃后不适怎么调’。” |
| **4. 孤证与过期数据清查（Evidence Audit）** | “报告里哪条结论只基于单一来源或超过 24 个月的旧数据？” | 隐瞒不报。 | 显式列出证据薄弱项，并给出 24 小时内可执行的最小验证动作。 |
