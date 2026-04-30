# Hermes Agent 生态新进化项目整理

> 来源：https://x.com/gittrend0x/status/2046932331001512385
> 整理时间：2025-04-23
> 来自翡冷翠

---

## 简介

本文档整理了 GitTrend (@GitTrend0x) 在 X 平台分享的 5 个 Hermes Agent 生态新插件/项目。这些新进化体让 Hermes 更像一个个性化 AI 操作系统，覆盖了上下文管理、视觉反馈、记忆增强、Web 界面和搜索增强等多个维度。

---

## 内容清单总览

| 序号 | 项目名称 | 作者/来源 | 类型 | 核心亮点 | Stars |
|------|----------|-----------|------|----------|-------|
| 1 | hermes-lcm | @stephenschoettler | 插件 | 无损上下文管理，DAG 结构 | 265 |
| 2 | hermes-neurovision | @Tranquil-Flow | 插件 | 85 种 ASCII 动态主题，实时可视化 | 26 |
| 3 | supermemory | supermemory.ai | 插件 | 知识图谱原生记忆提供者 | - |
| 4 | hermes-webui | @nesquena | 工具 | 轻量暗色 Web UI | 3.4k |
| 5 | web-search-plus | @robbyczgw | 插件 | 智能多搜索引擎路由 | - |

---

## 详细内容

### 1. hermes-lcm — 无损上下文管理插件

**来源**：@stephenschoettler  
**GitHub**：https://github.com/stephenschoettler/hermes-lcm  
**类型**：上下文引擎插件  
**Stars**：265 ⭐

#### 核心功能

基于 Voltropy PBC 的 [LCM 论文](https://papers.voltropy.com/LCM)（Ehrlich & Blackman, 2026年2月），hermes-lcm 是一个**无损上下文管理插件**，解决了当上下文填满时传统压缩会丢失细节的问题。

**关键特性：**

- **Immutable-first Store** — 每条消息持久化到 SQLite，仅有窄范围的显式 GC tombstones
- **Summary DAG** — 层次化压缩（D0 分钟 → D1 小时 → D2 天）
- **3-Level Escalation** — L1 详细 → L2 摘要 → L3 确定性截断（保证收敛）
- **Agent Tools** — 提供 `lcm_grep`, `lcm_describe`, `lcm_expand`, `lcm_expand_query` 等结构化检索工具
- **Large Tool-Output Handling** — 超大工具结果可选择外部化存储
- **Session Filtering** — 支持 glob 模式排除或只读标记特定会话
- **Profile-scoped** — 每个 Hermes Profile 独立数据库

#### 与内置压缩的区别

| 特性 | 内置压缩 | hermes-lcm |
|------|----------|------------|
| 活跃上下文 | 可能丢失 | 无损 |
| 恢复路径 | 通过 session_search | 插件内直接 drill-down |
| 检索行为 | 隐式不稳定 | DAG 规则显式稳定 |

#### 安装

```bash
git clone https://github.com/stephenschoettler/hermes-lcm \
  ~/.hermes/plugins/hermes-lcm
```

#### 配置

```yaml
plugins:
  enabled:
    - hermes-lcm

context:
  engine: lcm
```

#### 验证

```bash
hermes plugins
# 应显示: ✓ hermes-lcm v0.7.0 (6 tools)
# Context Engine: lcm
```

#### 适用场景

- 长会话需要保留完整历史
- 需要精确回溯之前的对话细节
- 复杂多轮任务需要稳定的上下文引用

---

### 2. hermes-neurovision — 终端神经视觉仪

**来源**：@Tranquil-Flow (@FlowTranquil)  
**GitHub**：https://github.com/Tranquil-Flow/hermes-neurovision  
**类型**：可视化插件  
**Stars**：26 ⭐  
**版本**：v0.2.0

#### 核心功能

一个全屏 ASCII 艺术可视化工具，实时响应 AI Agent 的活动。每次工具调用、内存写入、会话生命周期事件都会驱动视觉效果变化。

**关键特性：**

- **85 种动画主题** — 全屏生成式场域、奇异吸引子、混合节点/场域屏幕、经典节点图
- **7 种数据源** — Sessions、工具调用、内存写入、Cron 任务、轨迹、安全事件
- **实时事件可视化** — Agent 活动直接驱动视觉强度、数据包、脉冲和爆发效果
- **日志叠加层** — 带颜色编码的实时事件流
- **调谐器叠加层** — 实时逐元素控制：滑块调节速度/密度/敏感度，开关控制每个视觉层
- **调试面板** — 显示最近事件和触发时间的实时诊断覆盖层
- **Daemon 模式** — 空闲时画廊屏保，Agent 活动时实时模式
- **Legacy 模式** — 访问重新设计前的原始节点版本主题
- **纯标准库** — 零外部依赖

#### 渲染引擎

**ASCII Field Engine（主引擎）**
- 每帧从数学函数计算每个字符单元
- Agent 事件驱动 `intensity_multiplier`

**Node-Based Engine（传统/混合）**
- 节点图，带边连接
- 事件产生沿边传输的数据包、节点脉冲、粒子爆发

**Hybrid Engine**
- `draw_background()` — 先渲染 ASCII 场域作为背景
- `draw_extras()` — 后渲染前景效果

#### Agent 活动 → 视觉效果映射

| Hermes 动作 | 视觉效果 |
|-------------|----------|
| 会话开始 | **Wake** — 网络亮度激增；场域密度峰值 |
| 工具调用执行 | **Packet** — 沿边传输的字形；场域变亮 |
| 消息加入上下文 | **Pulse** — 从节点扩展的环 |
| 创建内存 | **Spawn node** — 新节点出现 |
| 任务或会话结束 | **Burst** — 粒子爆炸，然后冷却 |
| Token 使用增加 | **Intensity scales** — 场域密度/速度与负载成正比 |
| 错误或安全威胁 | **Flash** — 所有边变色；场域闪光 |
| 10秒内 5+ 工具调用 | **Tool burst** — 快速数据包级联 |
| 同一工具连续使用 3 次 | **Tool chain** — 持续数据包流 |

#### 快速开始

```bash
git clone https://github.com/Tranquil-Flow/hermes-neurovision.git
cd hermes-neurovision
pip install -e .
python3 install_helper.py   # 安装 gateway hook + 自动启动配置
hermes-neurovision
```

#### 使用模式

```bash
hermes-neurovision              # 实时模式（默认）
hermes-neurovision --quiet      # 静默模式
hermes-neurovision --logs       # 带日志叠加
hermes-neurovision --gallery     # 画廊模式浏览主题
hermes-neurovision --daemon      # Daemon 模式
hermes-neurovision --theme storm-core  # 特定主题
```

#### 键盘控制

- `n` / `→` — 下一主题
- `p` / `←` — 上一主题
- `Enter` — 锁定当前主题
- `t` — 打开调谐器叠加层
- `d` — 切换调试面板
- `l` — 切换日志叠加
- `q` — 退出

#### 适用场景

- 想要直观感受 Agent 活动
- 演示/展示时需要视觉反馈
- 调试时想实时观察事件流
- 长时间运行任务时的环境氛围

---

### 3. supermemory — 知识图谱原生记忆提供者

**来源**：supermemory.ai  
**官网**：https://supermemory.ai  
**Hermes 集成**：https://github.com/NousResearch/hermes-agent  
**类型**：记忆提供者插件  
**荣誉**：#1 on LongMemEval, LoCoMo, ConvoMem（三大 AI 记忆基准测试）

#### 核心功能

Supermemory 是 AI 的记忆和上下文层，自动从对话中提取事实、构建用户画像、处理知识更新和矛盾、遗忘过期信息，并在正确的时间提供正确的上下文。

**关键特性：**

| 功能 | 说明 |
|------|------|
| 🧠 Memory | 从对话中提取事实。处理时间变化、矛盾和自动遗忘 |
| 👤 User Profiles | 自动维护的用户上下文 — 稳定事实 + 近期活动 |
| 🔍 Hybrid Search | 单次查询中 RAG + Memory 结合 |
| 🔌 Connectors | Google Drive、Gmail、Notion、OneDrive、GitHub — 实时 webhook 同步 |
| 📄 Multi-modal Extractors | PDF、图片（OCR）、视频（转录）、代码（AST 感知分块）|

#### 使用方法

**方式一：MCP 快速安装**

```bash
npx -y install-mcp@latest https://mcp.supermemory.ai/mcp --client claude --oauth=yes
```

替换 `claude` 为你的客户端：`cursor`, `windsurf`, `vscode` 等。

**方式二：手动配置**

```json
{
  "mcpServers": {
    "supermemory": {
      "url": "https://mcp.supermemory.ai/mcp"
    }
  }
}
```

#### 工具列表

| 工具 | 功能 |
|------|------|
| `memory` | 保存或遗忘信息。AI 自动调用 |
| `recall` | 按查询搜索记忆。返回相关记忆 + 用户画像摘要 |
| `context` | 在会话开始时注入完整画像 |

#### 支持客户端

Claude Desktop · Cursor · Windsurf · VS Code · Claude Code · OpenCode · OpenClaw · **Hermes**

#### 开发者 API 快速开始

```typescript
import Supermemory from "supermemory";

const client = new Supermemory();

// 存储对话
await client.add({
  content: "User loves TypeScript and prefers functional patterns",
  containerTag: "user_123",
});

// 一次调用获取用户画像 + 相关记忆
const { profile, searchResults } = await client.profile({
  containerTag: "user_123",
  q: "What programming style does the user prefer?",
});
```

```python
from supermemory import Supermemory

client = Supermemory()

client.add(
    content="User loves TypeScript and prefers functional patterns",
    container_tag="user_123"
)

result = client.profile(container_tag="user_123", q="programming style")

print(result.profile.static)   # 长期事实
print(result.profile.dynamic)  # 近期上下文
```

#### 适用场景

- 需要 AI 记住跨会话的偏好和历史
- 构建需要用户画像的个性化应用
- 需要连接外部数据源（Drive、Gmail、Notion）
- 希望一站式解决记忆、RAG、用户画像

---

### 4. hermes-webui — 轻量 Web UI

**来源**：@nesquena (Nathan Esquenazi)  
**GitHub**：https://github.com/nesquena/hermes-webui  
**类型**：Web 界面工具  
**Stars**：3.4k ⭐  
**版本**：v0.50.x

#### 核心功能

Hermes WebUI 是在浏览器中完整复刻 Hermes CLI 体验的轻量暗色主题 Web 界面，支持从 Web 或手机使用 Hermes Agent。

**关键特性：**

- **三栏界面** — 会话列表、聊天窗口、文件浏览器
- **实时 Token 使用查看** — 监控上下文使用情况
- **暗色主题** — 护眼的暗色界面设计
- **移动端支持** — 可在手机上使用
- **会话管理** — 创建、重命名、删除会话
- **文件预览** — 内置文件浏览器和预览
- **工作区支持** — 多工作区切换
- **Docker 支持** — 容器化部署

#### 安装（Docker）

```bash
docker run -p 8080:8080 \
  -v ~/.hermes:/home/hermeswebui/.hermes \
  ghcr.io/nesquena/hermes-webui:latest
```

#### 项目活跃度

- 634+ Commits
- 208 Tags（频繁更新）
- 433 Forks
- 活跃维护中（最新提交：11 分钟前）

#### 适用场景

- 不喜欢/不方便使用命令行
- 需要在移动设备上使用 Hermes
- 想要图形化界面管理会话和文件
- 需要实时查看 token 使用情况

---

### 5. web-search-plus — 智能多搜索引擎插件

**来源**：@robbyczgw  
**GitHub**：https://github.com/robbyczgw-cla/web-search-plus  
**ClawHub**：https://clawhub.ai  
**类型**：搜索插件  
**版本**：v2.9.0

#### 核心功能

统一多提供商 Web 搜索，具有**智能自动路由**功能，使用多信号分析自动在 **Serper**、**Tavily**、**Querit**、**Exa**、**Perplexity (Sonar Pro)**、**You.com** 和 **SearXNG** 之间选择。

**智能路由信号：**

- **意图分类**：购物 vs 研究 vs 发现 vs RAG/实时 vs 隐私
- **语言模式**："how much"（价格）vs "how does"（研究）vs "privately"（隐私）
- **实体检测**：产品+品牌组合、URL、域名
- **复杂度分析**：长查询偏向研究提供商
- **置信度评分**：了解路由决策的可靠性

#### 提供商能力矩阵

| 提供商 | 最佳场景 | 示例查询 |
|--------|----------|----------|
| **Serper** (Google) | 产品规格、价格、购物 | "iPhone 16 price" |
| **Tavily** | 研究问题、深度挖掘 | "quantum computing explained" |
| **Querit** | 多语言 AI 搜索、实时答案 | "German AI policy updates" |
| **Exa** | 相似页面查找、公司发现 | "companies like Stripe" |
| **Perplexity** | 直接答案、引用优先 | "Who is the president of Austria?" |
| **You.com** | RAG 应用、实时信息 | "latest AI news" |
| **SearXNG** | 隐私优先、自托管 | "search privately" |

#### 使用示例

```bash
# 自动路由到最佳提供商
python3 scripts/search.py -q "best laptop 2024"

# 显式指定提供商
python3 scripts/search.py -p serper -q "iPhone 16 specs"
python3 scripts/search.py -p tavily -q "quantum computing" --depth advanced
python3 scripts/search.py -p exa -q "AI startups 2024" --category company

# 带缓存统计
python3 scripts/search.py --cache-stats

# 清除缓存
python3 scripts/search.py --clear-cache
```

#### 快速开始

**交互式设置（推荐）**

```bash
python3 scripts/setup.py
```

向导会解释每个提供商，收集 API key，自动创建 `config.json`。

**手动设置**

```bash
export SERPER_API_KEY="***"      # https://serper.dev
export TAVILY_API_KEY="***"      # https://tavily.com
export EXA_API_KEY="***"         # https://exa.ai
export KILOCODE_API_KEY="***"    # Perplexity via kilo.ai
export YOU_API_KEY="***"         # https://api.you.com
export SEARXNG_INSTANCE_URL="..." # 自托管
```

#### 路由示例

```bash
# 路由到 Serper（价格意图）
python3 scripts/search.py -q "how much does iPhone 16 cost"
# → Serper (68% confidence)

# 路由到 Tavily（研究意图）
python3 scripts/search.py -q "how does quantum entanglement work"
# → Tavily (86% HIGH)

# 路由到 Exa（公司发现）
python3 scripts/search.py -q "startups similar to Notion"
# → Exa (76% HIGH)

# 路由到 SearXNG（隐私意图）
python3 scripts/search.py -q "search privately without tracking"
# → SearXNG (74% HIGH)
```

#### 缓存机制

搜索结果自动缓存 1 小时以节省 API 成本：

```bash
# 首次请求：从 API 获取 ($)
python3 scripts/search.py -q "AI startups 2024"

# 重复请求：使用缓存 (FREE!)
python3 scripts/search.py -q "AI startups 2024"
# Output includes: "cached": true

# 绕过缓存
python3 scripts/search.py -q "AI startups 2024" --no-cache
```

#### 适用场景

- 需要根据查询类型自动选择最佳搜索引擎
- 希望节省 API 成本（缓存机制）
- 需要对比多个搜索引擎的结果
- 有隐私需求（SearXNG 支持）

---

## 资源汇总

### 所有 GitHub 仓库

| 项目 | 链接 | Stars | 简介 |
|------|------|-------|------|
| hermes-lcm | https://github.com/stephenschoettler/hermes-lcm | 265 | 无损上下文管理 |
| hermes-neurovision | https://github.com/Tranquil-Flow/hermes-neurovision | 26 | 终端神经视觉仪 |
| hermes-webui | https://github.com/nesquena/hermes-webui | 3.4k | Web UI 界面 |
| web-search-plus | https://github.com/robbyczgw-cla/web-search-plus | - | 智能多搜索引擎 |
| supermemory | https://github.com/supermemoryai/supermemory | - | 知识图谱记忆引擎 |

### 官方链接

| 名称 | 链接 | 说明 |
|------|------|------|
| Hermes Agent 主仓库 | https://github.com/NousResearch/hermes-agent | 主项目 |
| Hermes Atlas | https://hermesatlas.com | 社区项目收录 |
| Supermemory | https://supermemory.ai | 记忆引擎 |
| ClawHub | https://clawhub.ai | OpenClaw 插件市场 |

### 值得关注的人/账号

- @stephenschoettler — hermes-lcm 作者
- @Tranquil-Flow (@FlowTranquil) — hermes-neurovision 作者
- @nesquena — hermes-webui 作者
- @GitTrend0x — GitTrend，GitHub & AI 趋势分享
- @robbyczgw — web-search-plus 作者

---

## 建议学习/使用路径

### 初学者路径

1. **hermes-webui** — 先用 Web 界面熟悉 Hermes
2. **web-search-plus** — 增强搜索能力，覆盖更多场景
3. **supermemory** — 添加记忆能力，跨会话保持上下文

### 进阶路径

1. **hermes-lcm** — 解决长会话上下文压缩问题
2. **hermes-neurovision** — 添加可视化反馈，观察 Agent 活动
3. **组合使用** — lcm + supermemory + webui 构建完整工作流

### 特定场景推荐

| 场景 | 推荐组合 |
|------|----------|
| 长会话研究 | hermes-lcm + supermemory |
| 演示/展示 | hermes-webui + hermes-neurovision |
| 信息检索 | web-search-plus + supermemory |
| 移动办公 | hermes-webui (Docker) |
| 隐私优先 | web-search-plus (SearXNG) |

---

## 附录：快速参考

### hermes-lcm 工具速查

```bash
lcm_grep <query>          # 搜索压缩历史
lcm_describe <id>         # 描述 DAG 节点
lcm_expand <id>           # 展开压缩内容
lcm_expand_query <query>  # 查询并展开
lcm_status                # 查看 LCM 状态
lcm_doctor                # 诊断问题
```

### hermes-neurovision 主题类别

- **Full-screen fields** — 完整场域主题
- **Strange attractors** — 奇异吸引子
- **Hybrid node/field** — 混合节点/场域
- **Classic node graphs** — 经典节点图
- **Legacy themes** — 传统节点版本（20+ 个）

### web-search-plus 环境变量

```bash
SERPER_API_KEY="***"
TAVILY_API_KEY="***"
QUERIT_API_KEY="***"
EXA_API_KEY="***"
KILOCODE_API_KEY="***"
YOU_API_KEY="***"
SEARXNG_INSTANCE_URL="***"
```

---

*来自翡冷翠*
