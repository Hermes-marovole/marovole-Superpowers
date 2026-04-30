# Hermes Agent 生态项目完整整理

> 来源：https://x.com/GitTrend0x/status/2047616606826893413  
> 整理时间：2026-04-26  
> 核实结果：**主帖 5 个项目全部真实** ✅  
> 来自翡冷翠

---

## 📌 帖子结构说明

这是一个**引用推文（Quote Tweet）**，包含两层内容：

| 层级 | 日期 | 内容 | 状态 |
|------|------|------|------|
| **主帖** | Apr 24 | 5 个最新进化体 | ✅ 全部真实 |
| **引用推文** | Apr 23 | 5 个"全新进化体" | ❌ 全部 404 |

**我之前只检查了引用的推文，忽略了主帖的真实项目，抱歉！**

---

## ✅ 主帖项目（全部真实）

### 1️⃣ super-hermes
- **GitHub**: https://github.com/Cranot/super-hermes
- **Stars**: 67 | Forks: 4
- **描述**: Meta-reasoning 插件：Agent 执行前先自我优化 prompt
- **宣传语**: "自己给自己写作业"
- **状态**: ✅ 真实存在，活跃维护

### 2️⃣ hermes-life-os ⭐ 推荐
- **GitHub**: https://github.com/Lethe044/hermes-life-os
- **Stars**: 55 | Forks: 6
- **作者**: @Lethe044
- **描述**: 生活 OS：自动追踪日常习惯、学习用户模式。私人生活管家
- **核心功能**:
  - 🧠 长期记忆 - 记录情绪、饮食、睡眠、压力、专注度
  - 🔍 模式检测 - 自动发现生活数据关联（睡眠差→情绪差）
  - ⏰ Cron 自动化 - 早间简报/午间检查/晚间反思/周一周报
  - 📊 全维度追踪 - 营养、睡眠、水分、健身、心理健康
- **演示模式**: onboard/morning/checkin/evening/weekly/nutrition/sleep/fitness/mental/focus/health/dream/chat
- **状态**: ✅ 真实存在，功能完整

### 3️⃣ hermes-dojo
- **GitHub**: https://github.com/Yonkoo11/hermes-dojo
- **Stars**: 35 | Forks: 3
- **描述**: 技能道场：实时监控 + 自动迭代弱技能。Hermes 自己练级进行时
- **核心流程**: `measure → identify weakness → evolve → measure again → report`
- **功能**:
  - Performance Monitor - 读取 session logs，识别失败模式
  - Weakness Analyzer - 分类根因并排序改进机会
  - Auto-Fixer - 自动修复或创建新技能
  - Reports - 生成 CLI/Telegram 报告
- **状态**: ✅ 真实存在

### 4️⃣ hermes-web-search-plus
- **GitHub**: https://github.com/robbyczgw-cla/hermes-web-search-plus
- **Stars**: 86 | Forks: 5
- **描述**: 多提供商搜索插件：Serper/Tavily/Exa/Querit/Perplexity 自动路由
- **特性**:
  - 智能自动路由到最优搜索引擎
  - 支持深度研究、时间和域名过滤
  - 查询路由解释
- **状态**: ✅ 真实存在，功能完整

### 5️⃣ hermes-memory-plugin
- **GitHub**: https://github.com/Ladybug-Memory/hermes-memory-plugin
- **Stars**: 9 | Forks: 0
- **描述**: Ladybug 本地内存插件：纯本地图数据库，无云无 API。隐私党狂喜
- **技术**:
  - 基于 LadybugMemory（列式嵌入式图数据库 .lbdb）
  - BM25 关键词搜索
  - 重要性加权回忆
  - 命名图边关系
  - 可选 GLiNER2 实体提取
- **特点**: 完全本地，无外部服务依赖
- **状态**: ✅ 真实存在

---

## ❌ 引用推文项目（全部 404）

| 项目 | 声称链接 | 核实结果 |
|------|---------|---------|
| Lyra | github.com/lyra-ai/hermes | ❌ 404 |
| Nexus | github.com/nexusforge/her | ❌ 404 |
| Pulse | github.com/pulsecheck/her | ❌ 404 |
| Vanguard | github.com/vanguard-ai/he | ❌ 404 |
| Lumina | github.com/lumina-hermes/ | ❌ 404 |

**注意**: 短链接声称重定向到带 `hermes-` 前缀的完整仓库名（如 hermes-lyra），但这些也是 404。

---

## 📊 项目总览

| 项目 | 作者 | Stars | 类型 | 核心亮点 |
|------|------|-------|------|----------|
| super-hermes | Cranot | 67 | Meta-reasoning | 自我优化 prompt |
| hermes-life-os | Lethe044 | 55 | 生活 OS | 长期记忆 + 模式检测 |
| hermes-dojo | Yonkoo11 | 35 | 技能进化 | 自动修复弱技能 |
| hermes-web-search-plus | robbyczgw-cla | 86 | 搜索插件 | 多引擎自动路由 |
| hermes-memory-plugin | Ladybug-Memory | 9 | 本地内存 | 无云隐私优先 |

**生态 Stars 总计**: 252+ ⭐

---

## 🎯 使用建议

1. **hermes-life-os** - 最适合个人生活管理，功能最完整
2. **hermes-web-search-plus** - 搜索增强必备，86 stars 证明社区认可
3. **hermes-dojo** - 想让 Agent 自我进化就用这个
4. **hermes-memory-plugin** - 隐私优先用户的本地内存方案
5. **super-hermes** - 提升 Agent reasoning 能力

---

## ⚠️ 关于引用推文的风险提示

引用推文（Apr 23）中的 5 个项目全部为虚假链接：
- 显示文本与实际链接目标不一致
- 所有短链接目标也是 404
- 可能是早期未发布的项目或钓鱼内容

**建议**: 谨慎对待 GitTrend 账号中引用推文的内容，以主帖内容为准。

---

## 🔗 相关资源

- **NousResearch Hermes Agent**: https://github.com/NousResearch/hermes-agent
- **Hermes Atlas（生态地图）**: https://github.com/ksimback/hermes-ecosystem
- **awesome-hermes-agent**: https://github.com/0xNyk/awesome-hermes-agent

---

*来自翡冷翠*  
*核实日期：2026-04-26*
