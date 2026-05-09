# Ladder + Polymarket 开源工具矩阵：从付费墙破解到 AI 交易代理的完整替代方案

> 来源：X/Twitter @oragnes（比特币橙子Trader）
> 整理时间：2026-05-09
> 来自翡冷翠

---

## 执行摘要

@oragnes 在 X 上分享了两组极具实用价值的开源工具合集：

- **第一组（单帖）**：Ladder —— 一个基于 Go 的自托管 HTTP 代理，伪装 Google 爬虫请求头绕过付费墙，让你免费阅读部分付费内容。它是 12ft.io 的完全自主可控替代品。

- **第二组（聚合帖）**：围绕 Polymarket 等预测市场生态构建的 7 个开源工具，覆盖图表、宏观数据、回测、策略执行、模拟交易、Token 节省、AI Agent 闭环，全部为 100% 免费方案，可替代总价值超过 $2,330/月 的商业工具链。

这两组合集的核心洞察是：**商业工具的护城河正在被开源社区快速瓦解**。从付费墙绕过，到金融数据获取，再到 AI Agent 交易闭环，开源方案不仅免费，而且在可控性、透明度和组合灵活性上往往更胜一筹。

---

## 内容清单总览

| 序号 | 工具名称 | 替代目标 | 核心定位 | 技术栈 | 开源协议 |
|------|---------|---------|---------|--------|---------|
| 1 | **Ladder** | 12ft.io | 付费墙绕过自托管代理 | Go | 未注明 |
| 2 | **lightweight-charts** | TradingView Pro ($30/月) | 45KB 轻量金融图表库 | TypeScript | Apache-2.0 |
| 3 | **fredapi** | 彭博终端 ($2,000/月) | 美联储宏观经济数据 API | Python | BSD |
| 4 | **prediction-market-backtesting** | 回测平台 ($100/月) | Polymarket/Kalshi 回测框架 | Python + Rust | Mixed |
| 5 | **polybot** | 策略执行系统 | Polymarket 交易基础设施 | Java 21 | 未注明 |
| 6 | **polymarket-paper-trader** | 模拟交易工具 | AI Agent 真实订单簿模拟 | Python | MIT |
| 7 | **rtk** | Claude Code Token 消耗 | Token 压缩代理 | Rust | MIT |
| 8 | **goose** | Claude Code ($200/月) | 通用 AI Agent 闭环 | Rust | Apache-2.0 |

---

## 详细内容

### 1. Ladder —— 自托管付费墙绕过代理

**来源**：@oragnes / X
**GitHub**：https://github.com/everywall/ladder
**类型**：开发者工具 / 代理服务器
**替代目标**：12ft.io（第三方付费墙绕过服务）

#### 核心原理

付费墙为了让 Google 索引文章，必须允许 Google 爬虫（Googlebot）读取全文。Ladder 就伪装成 Google 爬虫的请求头（User-Agent、X-Forwarded-For 等），骗过付费墙，让你直接看到完整内容。这是出版商自己为 SEO 留下的结构性漏洞。

#### 关键特性

- **付费墙绕过**：伪装主流搜索引擎爬虫请求头，获取被付费墙拦截的完整内容
- **CORS 移除**：移除/修改响应中的 CORS 头、Content-Security-Policy 等限制，可直接用于自己的 App 或脚本
- **自定义注入**：支持注入自定义 HTML、CSS、JavaScript 代码到目标页面
- **规则集系统**：基于域名的规则集（ruleset），不同网站不同处理方式，规则集可共享（Exposed Ruleset）
- **多平台部署**：
  - Docker 容器（amd64, arm64）
  - 二进制文件（Linux / macOS / Windows）
  - Helm Chart（Kubernetes）
- **基本认证**：支持 Basic Auth，防止代理被滥用
- **API 接口**：支持程序化访问和 RAW HTML 获取
- **访问日志**：完整记录请求链路

#### 快速上手

```bash
# Docker 一键部署（2 分钟搞定，$5 VPS 即可）
docker run -p 8080:8080 -d \
  --env RULESET=https://raw.githubusercontent.com/everywall/ladder-rules/main/ruleset.yaml \
  --name ladder ghcr.io/everywall/ladder:latest

# 本地二进制运行
./ladder -r https://raw.githubusercontent.com/everywall/ladder-rules/main/ruleset.yaml
# 默认访问 http://localhost:8080
```

#### 架构流程

```
Client → Ladder（应用 RequestModifications）→ Website → Ladder（应用 ResultModifications）→ Client
```

#### 注意事项

- 部分网站使用高级反爬机制（指纹识别、行为分析、速率限制），Ladder 无法绕过这些防护
- 作者明确声明：仅用于合法测试、研究和质量保证目的，使用时需遵守目标网站的服务条款和适用法规
- 公开部署务必启用 Basic Auth，防止被他人滥用
- 可配合 FlareSolverr 等独立工具处理需要 JavaScript 渲染的页面

---

### 2. lightweight-charts —— 45KB 金融图表库

**来源**：TradingView 官方 / X @oragnes 推荐
**GitHub**：https://github.com/tradingview/lightweight-charts
**官网**：https://www.tradingview.com/lightweight-charts/
**类型**：前端图表库
**替代目标**：TradingView Pro（$30/月）

#### 核心定位

TradingView 官方出品的开源金融图表库，体积仅约 45KB，是目前最小且最快的 HTML5 金融图表方案之一。它用接近静态图片的体积，提供了完整的交互式图表能力。

#### 关键特性

- **极致轻量**：约 45KB，几乎不影响页面加载速度
- **高性能**：针对金融数据场景深度优化，大数据量下依然流畅
- **丰富图表类型**：K 线、折线、面积、柱状图、基准线等
- **插件扩展**：支持自定义插件开发，官方提供丰富的交互式插件示例
- **多种接入方式**：npm、CDN、pkg.pr.new 最新构建

#### 快速上手

```bash
npm install lightweight-charts
```

```js
import { createChart, LineSeries } from 'lightweight-charts';

const chart = createChart(document.body, { width: 400, height: 300 });
const lineSeries = chart.addSeries(LineSeries);
lineSeries.setData([
    { time: '2019-04-11', value: 80.01 },
    { time: '2019-04-12', value: 96.63 },
    // ...
]);
```

#### CDN 使用

```html
<script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
<script>
const chart = LightweightCharts.createChart(document.body, { width: 400, height: 300 });
</script>
```

#### 为什么选它

如果你需要在网页上展示金融数据图表，又不希望引入数百 KB 的图表库拖慢页面加载速度，lightweight-charts 是最佳选择。它来自 TradingView 官方团队，API 设计成熟，社区生态活跃，且有丰富的插件扩展能力。

---

### 3. fredapi —— 美联储经济数据 Python 接口

**来源**：@oragnes / X
**GitHub**：https://github.com/mortada/fredapi
**PyPI**：https://pypi.org/project/fredapi/
**类型**：金融数据 API 封装
**替代目标**：彭博终端（$2,000/月）

#### 核心定位

fredapi 是 FRED（Federal Reserve Economic Data，美联储经济数据）Web 服务的 Python 封装，让你免费获取美联储圣路易斯分行发布的全部宏观经济数据集。配合 Claude 等 LLM，可以直接通过 API 做宏观经济分析。

#### 关键特性

- **完整 FRED 数据访问**：GDP、CPI、失业率、利率、SP500 等 80,000+ 经济指标
- **ALFRED 历史修订数据**：支持获取数据修订历史，回答"当时已知什么数据"
- **Pandas 原生集成**：返回数据为 pandas Series 或 DataFrame，无缝衔接数据分析工作流
- **免费 API Key**：在 FRED 官网免费申请

#### 快速上手

```bash
pip install fredapi
```

```python
from fredapi import Fred
fred = Fred(api_key='your_free_api_key')

# 获取标普 500 数据
data = fred.get_series('SP500')

# 获取 GDP 首次发布数据（忽略修订）
first_release = fred.get_series_first_release('GDP')

# 获取最新发布数据
latest = fred.get_series_latest_release('GDP')
```

#### 与 Claude 配合使用

```python
# 将 FRED 数据直接送入 Claude 做宏观分析
data = fred.get_series('GDP')
analysis_prompt = f"""
以下是美国的季度 GDP 数据（单位：十亿美元）：
{data.tail(20).to_string()}

请分析：
1. 近 5 个季度的增长趋势
2. 是否存在增长放缓的信号
3. 与历史同期相比处于什么水平
"""
# 将 analysis_prompt 发送给 Claude API
```

#### 为什么选它

彭博终端的核心价值之一是历史宏观经济数据库。fredapi + FRED 免费 API 覆盖了 80,000+ 美国及全球经济指标，对于大部分非机构级宏观分析已经足够。配合 LLM 的解读能力，可以构建零成本的自动化宏观研究流水线。

---

### 4. prediction-market-backtesting —— 预测市场回测框架

**来源**：@oragnes / X
**GitHub**：https://github.com/evan-kolberg/prediction-market-backtesting
**类型**：量化回测框架
**替代目标**：商业回测平台（$100/月）

#### 核心定位

基于 NautilusTrader 的强力分支，专门为 Polymarket 和 Kalshi 等预测市场定制了交易所适配器。提供完整的回测、策略开发和执行建模能力。

#### 关键特性

- **NautilusTrader 内核**：继承专业级量化交易框架的成熟架构
- **预测市场专属适配**：Polymarket + Kalshi 双市场支持
- **丰富图表输出**：
  - 权益曲线（总权益 + 单市场权益）
  - 逐笔盈亏 / 周期性盈亏柱状图
  - 市场配置占比
  - YES 价格（带买卖填充标记）
  - 回撤曲线
  - Sharpe 比率（带上下阴影）
  - 现金 / 权益曲线
  - 月度收益矩阵
  - 累积 Brier 优势
- **执行建模**：费用模型、滑点、被动订单队列位置、延迟模拟
- **多市场策略配置**：支持同时回测多个关联市场
- **数据源灵活**：支持原生供应商、PMXT 镜像、本地 Parquet 文件

#### 技术栈

- Python 3.12+ + Rust 1.93.1
- NautilusTrader 1.224.0
- Ruff（代码风格）+ uv（包管理）

#### 快速上手

```bash
git clone https://github.com/evan-kolberg/prediction-market-backtesting.git
cd prediction-market-backtesting

# 安装依赖
uv sync

# 运行回测
python -m backtests.runner your_strategy_config.yaml
```

#### 为什么选它

预测市场的回测与股票/期货有本质不同：二元结果、流动性差异、费用结构独特。这个框架针对预测市场做了专门的执行建模（费用、滑点、延迟），而不是简单套用传统回测工具。它的图表输出质量也远超大部分开源方案。

---

### 5. polybot —— Polymarket 交易基础设施

**来源**：@oragnes / X
**GitHub**：https://github.com/ent0n29/polybot
**类型**：交易系统 / 策略执行基础设施
**替代目标**：商业策略执行系统

#### 核心定位

开源的 Polymarket 交易基础设施和策略逆向工程工具包，覆盖从数据接入、策略执行到量化分析的完整链路。它是 AWARE 基金（Trader Intelligence、PSI 指数、基金镜像）的执行层和数据层基础。

#### 系统架构

Polybot 是一个多服务微服务系统：

- **执行服务**：支持模拟交易（Paper）和实盘（Live）双模式
- **策略运行时**：策略引擎和市场做市模块
- **数据接入**：市场/用户交易数据接入 ClickHouse
- **量化分析**：完整的分析流水线，支持策略复制评分
- **监控栈**：Grafana + Prometheus + Alertmanager

#### 技术栈

- Java 21（Amazon Corretto 推荐）+ Maven 3.8+
- ClickHouse（列式数据库）+ Redpanda（事件流）
- Kafka（消息总线）
- Docker Compose 一键部署

#### 快速上手

```bash
git clone https://github.com/ent0n29/polybot.git
cd polybot

# 配置环境
cp .env.example .env
set -a; source .env; set +a

# 一键启动全部服务
./start-all-services.sh

# 验证健康状态
curl http://localhost:8080/actuator/health
curl http://localhost:8123 --data "SELECT 1"
```

#### 研究工具包

`research/` 目录包含：
- 市场快照工具
- 深度分析脚本
- 策略复制度量（Replication Metrics）

#### 为什么选它

如果你需要从 0 搭建一个预测市场交易系统，polybot 提供了完整的生产级架构参考。Kafka + ClickHouse + Grafana 的组合是业界验证过的高吞吐数据流水线方案，而其策略逆向工程能力（通过公开交易数据推断其他交易者的策略逻辑）在预测市场这个信息透明的领域尤其有价值。

---

### 6. polymarket-paper-trader —— AI Agent 模拟交易

**来源**：@oragnes / X
**GitHub**：https://github.com/agent-next/polymarket-paper-trader
**PyPI**：https://pypi.org/project/polymarket-paper-trader/
**类型**：模拟交易 / AI Agent 工具
**替代目标**：商业模拟交易平台

#### 核心定位

**让 AI Agent 成为 Polymarket 交易者。** 给 Claude 等 AI Agent 提供 $10,000 虚拟资金，在真实 Polymarket 订单簿上交易，跟踪盈亏，还能在公共排行榜上竞争。零风险，真实价格。

#### 关键特性

- **真实订单簿执行**：订单按实际 Polymarket 的 ask/bid 簿逐层执行，消耗每个价格水平的流动性，与真实交易完全一致
- **精确费用模型**：使用 Polymarket 真实公式 `bps/10000 × min(price, 1-price) × shares`
- **滑点追踪**：每笔交易记录相对于中点的滑点（basis points）
- **限价订单状态机**：支持 GTC（Good-Til-Cancelled）和 GTD（Good-Til-Date）完整生命周期
- **策略回测**：支持基于历史价格快照回放策略
- **多结果市场**：不仅支持 YES/NO 二元市场，还支持任意数量结果的市场
- **公共排行榜**：AI Agent 之间可以竞争交易业绩

#### 快速上手（60 秒演示）

```bash
# 安装
pip install polymarket-paper-trader
# 或 ClawHub（OpenClaw Agent）
npx clawhub install polymarket-paper-trader

# 初始化 $10k 虚拟账户
pm-trader init --balance 10000

# 搜索市场
pm-trader markets search "bitcoin"

# 交易
pm-trader buy will-bitcoin-hit-100k yes 500

# 查看组合和盈亏
pm-trader portfolio
pm-trader stats --card    # 生成可分享的统计卡片
```

#### 为什么不是玩具

开发者明确指出：其他工具要么用随机数模拟价格，要么用简单公式。而 polymarket-paper-trader 模拟的是**真实的交易所机制**：层级订单簿、精确费用、滑点追踪。你的模拟盈亏与真实盈亏的差距仅在买卖价差范围内。

#### 为什么选它

这是目前唯一一个专门为 AI Agent 设计的预测市场模拟交易工具。它不只是让人类练习交易，而是让 AI Agent 在零风险环境下学习市场机制、测试策略、积累交易经验。对于构建自主交易 Agent 的研究者来说，这是理想的沙盒环境。

---

### 7. rtk —— Token 压缩代理

**来源**：@oragnes / X
**GitHub**：https://github.com/rtk-ai/rtk
**官网**：https://www.rtk-ai.app
**类型**：CLI 代理 / 开发效率工具
**替代目标**：Claude Code 高昂的 Token 消耗

#### 核心定位

**Rust 编写的高性能 CLI 代理，在命令输出到达 LLM 上下文之前进行过滤和压缩。** 兼容多种 AI 工具（Claude Code、Codex 等），单二进制文件，支持 100+ 常用命令。

#### Token 节省实测（30 分钟 Claude Code 会话）

| 操作 | 频率 | 标准 Token | rtk 后 | 节省 |
|------|------|-----------|--------|------|
| `ls` / `tree` | 10x | 2,000 | 400 | **-80%** |
| `cat` / `read` | 20x | 40,000 | 12,000 | **-70%** |
| `grep` / `rg` | 8x | 16,000 | 3,200 | **-80%** |
| `git status` | 10x | 3,000 | 600 | **-80%** |
| `git diff` | 5x | 10,000 | 2,500 | **-75%** |
| `git log` | 5x | 2,500 | 500 | **-80%** |
| `git add/commit/push` | 8x | 1,600 | 120 | **-92%** |
| `cargo test` / `npm test` | 5x | 25,000 | 2,500 | **-90%** |
| `ruff check` | 3x | 3,000 | 600 | **-80%** |
| `pytest` | 4x | 8,000 | 800 | **-90%** |
| **总计** | | **~118,000** | **~23,900** | **-80%** |

> 基于中等规模 TypeScript/Rust 项目估算，实际节省因项目规模而异。

#### 核心原理

rtk 在 LLM 读取命令输出前进行拦截，通过智能过滤（去除冗余、压缩重复模式、提取关键信息）减少进入上下文的 Token 数量。开销 <10ms，几乎感知不到延迟。

#### 安装方式

```bash
# Homebrew（推荐）
brew install rtk

# 快速安装（Linux/macOS）
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh

# Cargo
cargo install --git https://github.com/rtk-ai/rtk
```

#### 为什么选它

如果你每天使用 Claude Code 或类似 AI 编程助手，Token 消耗是持续的成本。rtk 通过压缩命令输出减少 60-90% 的 Token 使用，对于高频使用场景，一个月可以节省数百美元。而且它是一个透明代理，不需要改变你的工作流。

---

### 8. goose —— 通用 AI Agent 闭环

**来源**：@oragnes / X
**GitHub**：https://github.com/aaif-goose/goose（原 block/goose）
**官网**：https://goose-docs.ai
**类型**：通用 AI Agent
**替代目标**：Claude Code（$200/月）

#### 核心定位

**Block（Jack Dorsey 公司）出品的通用 AI Agent，现已移交 Linux Foundation 下的 Agentic AI Foundation (AAIF)。** 支持 15+ LLM 提供商，70+ MCP 扩展，提供完整的 AI Agent 闭环：桌面应用 + CLI + API。

#### 关键特性

- **多平台**：macOS、Linux、Windows 原生桌面应用
- **多提供商**：Anthropic、OpenAI、Google、Ollama、OpenRouter、Azure、Bedrock 等 15+
- **MCP 生态**：通过 Model Context Protocol 连接 70+ 扩展
- **ACP 支持**：通过 Agent Context Protocol 直接使用 Claude、ChatGPT、Gemini 的订阅
- **Rust 构建**：高性能、可移植
- **自定义发行版**：支持构建预配置提供商和扩展的品牌化发行版

#### 快速上手

```bash
# 安装 CLI
curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash

# 桌面应用下载
# https://goose-docs.ai/docs/getting-started/installation
```

#### 项目演进

- 最初由 Block 开发（原仓库 block/goose）
- 2026 年移交至 Linux Foundation 的 Agentic AI Foundation (AAIF)
- 社区快速增长：Discord、YouTube、LinkedIn、X 多渠道活跃

#### 为什么选它

如果你不想被锁定在单一 LLM 提供商，goose 是理想的通用 Agent 平台。它支持任意 LLM，通过 MCP 标准连接工具生态，而且作为 Linux Foundation 项目，具有长期的开源治理保障。35K Stars 证明了社区的认可。

---

## 发布者洞察（@oragnes 的推荐理由）

从 @oragnes 的帖子中可以直接提取以下关键洞察：

### 关于 Ladder

> "有人做了一个免费自托管工具，能瞬间阅读部分付费墙文章！"
> "核心原理：付费墙为了让 Google 索引文章，必须允许 Google 爬虫读取全文。Ladder 就伪装成 Google 爬虫的请求头，骗过付费墙，让你直接看到完整内容——这是出版商自己留下的漏洞。"

**洞察**：这不是一个"破解"工具，而是一个利用出版商自身 SEO 需求的合法技术手段。出版商为了搜索引擎排名主动向爬虫开放内容，Ladder 只是让你也能以"爬虫身份"访问。

### 关于开源替代方案合集

> "省钱贴（点赞&收藏）💸 围绕 Polymarket 构建的交易工具，我都在 GitHub 上找到了 100% 免费的开源替代方案。"

**洞察**：这个合集不是简单的"省钱"，而是构建了一个完整的**预测市场交易工具链**。从数据获取（fredapi）、图表展示（lightweight-charts）、策略回测（prediction-market-backtesting）、策略执行（polybot）、模拟训练（polymarket-paper-trader），到效率工具（rtk）和 Agent 平台（goose），覆盖了交易闭环的每个环节。

---

## 综合对比

| 维度 | 商业方案 | 开源替代方案 | 差异点 |
|------|---------|-------------|--------|
| **付费墙绕过** | 12ft.io（第三方服务，不稳定） | Ladder（自托管，完全可控） | 自主可控 + 可扩展规则集 |
| **图表** | TradingView Pro（$30/月） | lightweight-charts（免费，45KB） | 更轻量，官方出品，可嵌入任何页面 |
| **宏观数据** | 彭博终端（$2,000/月） | fredapi + FRED（免费） | 覆盖 80,000+ 指标，适合非机构级分析 |
| **回测** | 商业平台（$100/月） | prediction-market-backtesting（免费） | 专为预测市场设计，执行建模更精确 |
| **策略执行** | 商业系统（定制昂贵） | polybot（免费，开源） | 完整微服务架构，可自主扩展 |
| **模拟交易** | 有限功能的模拟器 | polymarket-paper-trader（免费） | 真实订单簿模拟，专为 AI Agent 设计 |
| **Token 优化** | 无 | rtk（免费，-80% Token） | 被动代理，不改变工作流 |
| **AI Agent 平台** | Claude Code（$200/月） | goose（免费，35K Stars） | 任意 LLM，70+ MCP 扩展 |

**月度成本对比**：商业工具链约 $2,330+/月 → 开源方案 $0（仅需 VPS 和 API 费用）

---

## 组合使用建议

### 场景 A：构建完整的预测市场交易流水线

```
fredapi（宏观数据）
  ↓
lightweight-charts（数据可视化）
  ↓
prediction-market-backtesting（策略验证）
  ↓
polymarket-paper-trader（模拟交易训练）
  ↓
polybot（实盘执行）
```

### 场景 B：AI Agent 驱动的自动化研究

```
Ladder（获取付费研究内容）
  ↓
fredapi（获取宏观经济数据）
  ↓
Claude / goose（AI 分析 Agent）
  ↓
rtk（压缩 Token 消耗，降低成本）
```

### 场景 C：个人量化研究工作站

```
Docker Compose 部署：
- Ladder（端口 8080）
- polybot 基础设施（Kafka + ClickHouse + Grafana）
- prediction-market-backtesting（本地回测）
```

---

## 资源汇总

### GitHub 仓库列表

| 项目 | 链接 | Stars | 语言 | 说明 |
|------|------|-------|------|------|
| Ladder | https://github.com/everywall/ladder | - | Go | 付费墙绕过代理 |
| lightweight-charts | https://github.com/tradingview/lightweight-charts | - | TypeScript | 45KB 金融图表 |
| fredapi | https://github.com/mortada/fredapi | - | Python | 美联储数据 API |
| prediction-market-backtesting | https://github.com/evan-kolberg/prediction-market-backtesting | - | Python/Rust | 预测市场回测 |
| polybot | https://github.com/ent0n29/polybot | - | Java | Polymarket 交易基础设施 |
| polymarket-paper-trader | https://github.com/agent-next/polymarket-paper-trader | - | Python | AI Agent 模拟交易 |
| rtk | https://github.com/rtk-ai/rtk | - | Rust | Token 压缩代理 |
| goose | https://github.com/aaif-goose/goose | 35K+ | Rust | 通用 AI Agent |

### 官方链接

| 名称 | 链接 | 说明 |
|------|------|------|
| Ladder Docker | https://github.com/everywall/ladder/pkgs/container/ladder | 官方容器镜像 |
| Ladder Ruleset | https://github.com/everywall/ladder-rules | 社区规则集 |
| TradingView Charts | https://www.tradingview.com/lightweight-charts/ | 官网与文档 |
| FRED API | https://api.stlouisfed.org/docs/fred/ | 美联储数据 API 文档 |
| goose 文档 | https://goose-docs.ai | 官方文档与教程 |
| rtk 官网 | https://www.rtk-ai.app | 产品官网与安装指南 |

### 值得关注的人/账号

- **@oragnes**（比特币橙子Trader）—— 持续分享加密货币和预测市场领域的开源工具与交易洞察
- **@agent-next** —— 自主进化 Agent 研究实验室，polymarket-paper-trader 的开发者
- **Block / AAIF** —— goose 的原始开发团队和现在的 Linux Foundation 维护方

---

## 建议学习/使用路径

### 第一步：立即尝试（5 分钟）

1. **Ladder**：`docker run -p 8080:8080 ghcr.io/everywall/ladder:latest`，输入一个付费文章链接测试
2. **fredapi**：`pip install fredapi`，申请免费 API Key，获取第一个经济指标
3. **lightweight-charts**：`npm install lightweight-charts`，复制官方示例运行

### 第二步：构建交易能力（1-2 天）

1. **polymarket-paper-trader**：给 AI Agent $10k 虚拟金，让它在真实订单簿上交易
2. **prediction-market-backtesting**：用历史数据验证你的策略逻辑
3. **polybot**：了解完整的交易基础设施架构

### 第三步：优化效率（持续）

1. **rtk**：接入 Claude Code，观察 Token 消耗下降
2. **goose**：如果需要跨 LLM 的通用 Agent 能力，替换 Claude Code

---

## 延伸思考

### 1. 付费墙与 SEO 的根本矛盾

Ladder 的核心原理揭示了一个有趣的结构性矛盾：出版商为了搜索引擎排名必须向爬虫开放内容，但付费墙又试图限制普通用户访问。这个矛盾本质上不可调和——只要出版商还想从 Google 获取流量，就必须保留这个"后门"。Ladder 只是把这个后门平等地向所有用户开放。

### 2. 预测市场的工具民主化

Polymarket 等预测市场的核心魅力在于信息透明度（所有交易公开可见），但这同时也意味着需要专业工具才能从海量信息中提取价值。polybot 的"策略逆向工程"能力就是一个典型例子：通过分析公开交易数据，推断其他交易者的策略逻辑。这在传统金融市场几乎不可能，但在预测市场是可行的。

### 3. AI Agent 交易的经济学

polymarket-paper-trader 让 AI Agent 在零风险环境下积累交易经验，这实际上是在创造一种"AI 交易能力的复利效应"：Agent 可以通过大量模拟交易学习市场模式，然后将经验迁移到实盘。如果模拟交易的数量足够大，这种学习方式可能超越人类交易者的经验积累速度。

### 4. Token 经济学的新维度

rtk 代表的不仅是技术优化，而是 AI 时代的新型"资源管理"问题。当 AI Agent 成为主要的工作方式时，Token 消耗就像云计算资源一样需要优化。Rust 编写的代理压缩层可能成为 AI 基础设施的标准组件。

### 5. 开源替代方案的成熟度拐点

这 8 个工具共同说明了一个趋势：开源软件在特定垂直领域的替代能力正在跨越"可用"到"好用"的拐点。它们不再是粗糙的玩具，而是具有生产级能力的系统，且往往在架构设计（微服务、MCP、规则集）上比商业方案更开放、更灵活。

---

## 风险与注意事项

| 工具 | 潜在风险 | 建议 |
|------|---------|------|
| Ladder | 可能违反目标网站 ToS；公开部署未加 Basic Auth 会被滥用 | 仅用于个人研究；务必启用认证；遵守当地法律 |
| 预测市场工具 | Polymarket 在某些司法管辖区受限；交易有风险 | 了解当地法规；先用 paper-trader 充分测试 |
| fredapi | 依赖 FRED API 的可用性 | 数据可用于学术/研究目的，注意引用规范 |
| rtk | 压缩可能丢失部分上下文信息 | 在关键场景验证输出完整性 |

---

## 附录：快速参考

### Ladder Docker 一键部署

```bash
docker run -p 8080:8080 -d \
  --env RULESET=https://raw.githubusercontent.com/everywall/ladder-rules/main/ruleset.yaml \
  --name ladder ghcr.io/everywall/ladder:latest
```

### fredapi 免费 API Key 申请

访问 https://fred.stlouisfed.org/docs/api/api_key.html，注册后即可获得免费 Key。

### lightweight-charts 最小示例

```html
<script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
<div id="chart"></div>
<script>
const chart = LightweightCharts.createChart(document.getElementById('chart'), { width: 600, height: 300 });
const line = chart.addSeries(LightweightCharts.LineSeries);
line.setData([
    { time: '2024-01-01', value: 100 },
    { time: '2024-01-02', value: 105 },
    { time: '2024-01-03', value: 103 },
]);
</script>
```

### polymarket-paper-trader 60 秒启动

```bash
pip install polymarket-paper-trader
pm-trader init --balance 10000
pm-trader markets search "bitcoin"
pm-trader buy will-bitcoin-hit-100k yes 100
pm-trader stats --card
```

---

*来自翡冷翠*
