# 用户行为、搜索动作、付费意愿与 OpenCLI 181 站点映射手册

## 一、核心认知：如何不靠问卷，直接抓取真实的「用户行为与付费意愿」？

传统的问卷调查充满了“口头说想买、掏钱时跑路”的伪需求。真正指导产品迭代与寻找市场机会点的一手数据，来自用户在互联网上留下的 **4 类不可伪造的行为痕迹**：

| 维度 | 用户真实动作 | 最强一手数据源 | 如何反哺产品与商业决策 |
| :--- | :--- | :--- | :--- |
| **1. 搜索动作 (Search Action)** | 用户在搜索框敲下前几个字时的自动联想词（Autocomplete） | 百度 / Google / 必应 / 淘宝天猫 / Amazon / YouTube 实时下拉词（`market_intel_tool.py intent`） | **直接决定内容选题与产品功能名**。例如搜`甘氨酸镁`时下拉词出现`甘氨酸镁副作用睡不着`、`甘氨酸镁一般吃几天停`、`甘氨酸镁怎么吃不伤胃`——说明“吃后反而失眠/伤胃/停药周期”是最高频的真实焦虑，产品必须内置【服用反应复评与周期提醒】。 |
| **2. 付费意愿 (Willingness to Pay)** | 用户在掏钱买单前的比价、求推荐、买二手、找平替与复购行为 | 京东/淘宝评价与销量结构、Amazon Best Sellers & Movers、闲鱼二手转让率、Reddit/小红书求购帖 | **检验真伪需求与定价锚点**。<br>• **闲鱼检验法**：如果某保健品/硬件在闲鱼上大量出现“全新未拆封/吃了一两次转”（`opencli xianyu search`），说明该品类**冲动购买强但依从性极差（假复购）**；<br>• **价格带分层**：看京东/Amazon 销量前 10 的单月日均花费（如 3元/天 vs 15元/天），锁定主力人群的心理账户上限。 |
| **3. 使用行为与断崖 (Usage & Adherence)** | 用户买回去之后怎么用、卡在哪一步、为什么放弃、自己搭了什么土办法（Workaround） | 京东/淘宝「追评」（买后 30-90 天）、小红书/Reddit 打卡帖与退坑帖、App Store 1-3 星长评论 | **定义产品迭代方向（Feature Wedge）**。<br>• 当大量用户用 Excel / 备忘录 / 药盒分装并拍照发小红书求助“这 5 种补剂能不能一起吃”时，说明现有的**手工替代方案（Workaround）极度痛苦**，这就是 AI 切入的最佳产品形态。 |
| **4. 商业推动力 (Commercial Push)** | 资本、供应链、渠道和头部玩家正在把钱砸向哪里 | 1688 工厂拿货价与起订量、东方财富/雪球机构研报与股东动向、BOSS直聘高薪抢人方向、抖音/小红书爆款商业笔记 | **判断入场时机与商业杠杆**。<br>• 用 `1688 search/item` 查出某核心配方的工厂代工底价（如出厂价 18 元，终端卖 298 元，毛利 >90%），立即看穿该赛道的商业推动力是**高毛利驱动的渠道/达人分销**还是**技术壁垒**。 |

---

## 二、本机 `opencli` 181 站点在「宽度×深度」调研中的黄金命令表

本机已安装的 `opencli` 拥有 **181 个网站、1289 个现成命令**。在做市场调研时，严禁放着现成结构化接口不用去写脆弱的 HTML 爬虫。以下按调研场景归类最核心的命令：

### 1. 货架电商、供应链底价与付费意愿检验（JD / Taobao / 1688 / Amazon / Xianyu / Pinduoduo）

```bash
# ① 京东：查竞品真实价格、规格参数与真实买家差评/30-90天追评
opencli jd search "甘氨酸镁" -f json
opencli jd item <sku_id_or_url> -f json
opencli jd reviews <sku_id_or_url> -f json

# ② 淘宝/天猫：查实时购买下拉词、商品列表与买家评价
python3 ~/.hermes/skills/research/market-intelligence/scripts/market_intel_tool.py intent "甘氨酸镁"
opencli taobao search "更年期 营养包" -f json
opencli taobao detail <item_id_or_url> -f json
opencli taobao reviews <item_id_or_url> -f json

# ③ 1688 供应链底牌：查同款配方/硬件的源头工厂批发价、阶梯报价（MOQ）与成交量（测算竞品真实 BOM 成本！）
opencli 1688 search "甘氨酸镁 贴牌 代工" -f json
opencli 1688 item <offer_id_or_url> -f json
opencli 1688 store <store_url> -f json

# ④ 闲鱼弃坑率检测：查某网红产品有多少人在“吃不习惯/闲置转让”（检验真实留存 vs 营销泡沫）
opencli xianyu search "Swisse 闲置 未拆封" -f json
opencli xianyu item <item_id> -f json

# ⑤ 拼多多百亿补贴与白牌底价：摸清全网比价底线与白牌销量天花板
python3 ~/.hermes/skills/research/web-search/scripts/search.py search 'site:yangkeduo.com OR "拼多多" "甘氨酸镁" ("百亿补贴" OR "已拼" OR "评价")' --engine serper -n 8

# ⑥ Amazon 全球消费趋势：查畅销榜（Best Sellers）、飙升榜（Movers & Shakers）、新品榜（New Releases）与评论汇总
opencli amazon bestsellers "<category_url_or_node>" -f json
opencli amazon movers-shakers "<category_url_or_node>" -f json
opencli amazon new-releases "<category_url_or_node>" -f json
opencli amazon search "magnesium glycinate" -f json
opencli amazon product <ASIN> -f json
opencli amazon discussion <ASIN> -f json
```

### 2. 兴趣与直播带货电商（抖音精选联盟/蝉妈妈/考古加 + 小红书买手种草 + 微信视频号小店）

```bash
# ① 抖音电商 & 蝉妈妈/考古加/精选联盟：查爆款带货视频、达人佣金率（20%-50%）、GMV 量级与直播切片话术
opencli douyin search "甘氨酸镁 睡眠" -f json
opencli douyin hashtag search --keyword "女性营养" -f json
opencli douyin detail <抖音短链或视频ID> -f json
opencli douyin user-videos <带货达人_sec_uid> -f json
python3 ~/.hermes/skills/research/web-search/scripts/search.py search '"甘氨酸镁" OR "Swisse" ("蝉妈妈" OR "考古加" OR "精选联盟" OR "佣金" OR "带货" OR "GMV")' --engine serper -n 8

# ② 小红书买手电商与种草转化：看「收藏/点赞比 > 0.8」的爆款笔记，并抓取楼中楼评论区“求链接/怎么买/哪个牌子/吃了啥反应”的买单信号
opencli xiaohongshu search "甘氨酸镁 测评 避雷" -f json
opencli xiaohongshu note <note_id> -f json
opencli xiaohongshu comments <note_id> -f json

# ③ 微信视频号小店（40-60岁中老年高客单价营养品/滋补品第一带货阵地）：
# 路径 A：通过已登录公众号后台 mp.weixin.qq.com 的 /cgi-bin/videosnap 接口免扫码拉取竞品视频号全量爆款列表（见 web-crawler 技能）
# 路径 B：搜狗微信与全网检索视频号带货爆款
opencli weixin search "视频号 营养 爆款" -f json
python3 ~/.hermes/skills/research/web-search/scripts/search.py search '"视频号" ("微信小店" OR "带货" OR "中老年") "营养"' --engine serper -n 8

# ④ 知乎 & B站 & Reddit & YouTube：深度长文测评、弹幕痛点与海外真实用户 Stack 讨论
opencli zhihu search "定制维生素 智商税" -f json
opencli bilibili search "补剂 搭配" -f json
opencli reddit search "menopause supplement stack" -f json
opencli reddit read <reddit_thread_url> -f json
opencli youtube search "perimenopause supplements review" -f json
```

### 3. 公司商业推动力、资本动向与招聘信号（东方财富 / 雪球 / BOSS直聘 / LinkedIn / PubMed）

```bash
# ① 东方财富 & 雪球：查上市公司最新公告、机构调研纪要、高管增减持、股民/行业老兵深度拆解
opencli eastmoney announcement --keyword "汤臣倍健" -f json
opencli xueqiu search --keyword "健合集团 Swisse 财报" -f json
opencli xueqiu comments --symbol "<股票代码>" -f json

# ② BOSS直聘 & LinkedIn：查竞品正在高薪招什么岗位（逆向工程对手未来半年的商业发力点）
opencli boss detail --url "<job_url>" -f json
opencli linkedin search --query "<company_name>" -f json

# ③ PubMed 临床循证：查某成分/方案的最新临床试验与荟萃分析（支撑灵知 AI 的循证壁垒）
opencli pubmed search --query "magnesium glycinate insomnia clinical trial" -f json
```

---

## 三、零成本 Autocomplete 端点清单（本机实测可用，无需 API Key、无需登录）

搜索下拉词是免费且最难被公关污染的行为数据。以下端点直接 `curl` 即可，`market_intel_tool.py intent` 已把 6 个平台并发封装好；只有在脚本报错或需要单点补采时才手写请求。

| 平台 | 端点 | 取词位置 | 备注 |
| :--- | :--- | :--- | :--- |
| Google | `https://suggestqueries.google.com/complete/search?client=firefox&hl=zh-CN&q=<kw>` | `json[1]` | 加 `&ds=yt` 即 YouTube 搜索下拉词；`hl` 切换中英文语料 |
| 百度 | `https://www.baidu.com/sugrec?prod=pc&wd=<kw>` | `json["g"][*]["q"]` | 中文长尾最丰富，痛点位/疑问句式主要靠它 |
| 必应 | `https://api.bing.com/osjson.aspx?query=<kw>` | `json[1]` | 中文语料质量高，常补充 Google 漏掉的“XX和苏糖酸镁的区别”类对比词 |
| 淘宝/天猫 | `https://suggest.taobao.com/sug?code=utf-8&q=<kw>` | `json["result"][*][0]` | **用 `suggest.taobao.com`**；`dropdown.taobao.com/sug` 是废弃路径，返回 404 |
| Amazon US | `https://completion.amazon.com/api/2017/suggestions?limit=10&prefix=<kw>&alias=aps&mid=ATVPDKIKX0DER` | `json["suggestions"][*]["value"]` | 只吃英文 seed；中文 seed 会退化，海外品类务必用英文词根再跑一次 |

使用要点：
- **必须先跑工具再写结论**：不要凭对用户搜索习惯的想象编造长尾词，`intent` 的输出才是可引用的一手动作数据，写报告时应逐字摘录下拉词。
- **中英文各跑一遍**：CJK seed 走百度/淘宝，英文 seed 走 Google/Amazon，两边词根差异本身就是「国内 vs 海外需求差」的证据。
- **词尾裂变模板固定三类**（脚本已内置）：痛点/副作用（`副作用`、`没用`、`智商税`、`side effects`、`not working`）、购买与选型意图（`哪个牌子`、`多少钱`、`平替`、`best … for`、`worth it`、`alternative`）、用法与依从性（`怎么吃`、`什么时候`、`吃几天停`、`how to take`、`dosage`、`vs`）。三类对应「产品该做什么 / 定价锚在哪 / 留存断在哪」，不要只做 base 词。
- **App Store 评论别走旧 RSS**：`itunes.apple.com/rss/customerreviews/...` 目前普遍返回空 feed（0 entry），白跑。应用类差评改走 `opencli` 的 app 商店适配器或第三方评论聚合站，别在这个端点上反复试。

---

## 四、从「用户动作 + 商业推动」推导产品迭代方向的决策矩阵

当收集完上述宽度与深度数据后，按以下 **四象限机会点公式** 输出产品迭代建议：

1. **高搜索增长 + 高供应链毛利（1688 成本极低、终端售价高）+ 高京东/小红书差评率**
   → **一级战略机会点（立即立项/迭代）**：说明市场已被巨头教育成熟、用户愿意掏高价，但现有方案体验极烂（如吃了伤胃、不知道怎么搭、没人管售后体感）。
2. **高淘宝/京东搜索下拉词 + 低内容覆盖度（搜索结果全是软文广告，无客观工具/测评）**
   → **一级获客钩子（Free Tool / Quiz Wedge）**：立刻把该搜索词做成免费的「AI 交互式自测卡 / 搭配冲突检查器 / 剂量计算器」，用极低 CAC 截流高意向用户。
3. **高前端销量 + 高闲鱼转让率 / 高“坚持不下来”差评**
   → **核心留存迭代方向（Retention Feature）**：不要去卷前端卖货话术，重点迭代产品的「最小依从性闭环」（如分阶段小剂量适应、第 3/7/14 天体感复评、不适反应一键调方）。
4. **巨头财报销售费用率 >50% + 风险因素提示“获客成本持续上升”**
   → **商业模式避坑指令**：严禁跟风买量投流，必须用「高留存订阅/复购服务 + 老客转介绍（Referral）+ 私域陪伴」重构单位经济模型（Unit Economics）。
