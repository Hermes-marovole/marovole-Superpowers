# ChatGPT 5.5 Pro 在两小时内产出博士论文级数学成果：菲尔兹奖得主 Timothy Gowers 的亲身测试

**来源**：Timothy Gowers (@wtgowers) 博客文章及 X Thread  
**发布时间**：2026-05-08  
**原始链接**：https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/  
**X Thread**：https://x.com/wtgowers/status/2052830948685676605  

---

## 执行摘要

菲尔兹奖得主、剑桥大学教授 Timothy Gowers 近期获得了 ChatGPT 5.5 Pro 的内测权限。他将 Melvyn Nathanson 提出的加法组合学开放问题交给该模型处理，结果令人震惊：ChatGPT 5.5 Pro 在大约两小时内独立产出了 Gowers 评估为"博士论文中完全合理的章节级别"的研究成果。Gowers 强调，他自己的数学输入为零，仅提供了诸如"你能探索一下那个想法吗？"或"请把论证写成 LaTeX 预印本格式"这类不含任何数学内容的提示。

---

## 核心亮点

### 1. 博士论文级成果，零人类数学输入

Gowers 明确写道："模型证明了一个结果，按我的评估完全可以作为博士论文中一个合理的章节。它在总共约两小时内完成了这个工作，而我的提示中没有任何数学内容。"

他进一步描述自己只说了类似这样的话：
- "是的，如果你能探索那个想法并看看能不能行得通，那就太好了。"
- "你能把那个论证改写成标准数学预印本风格的 LaTeX 文件吗？"

### 2. 从指数界到多项式界的三级跃迁

测试围绕 Nathanson 论文《Diversity, Equity and Inclusion for Problems in Additive Number Theory》中关于 sumset sizes 上界的问题展开：

**第一问（17分钟）**：ChatGPT 思考 17 分 5 秒后，给出了从 Nathanson 的指数界到二次上界的构造——这是理论最优的。Gowers 随后让它改写成 LaTeX 预印本格式，耗时 2 分 23 秒。

**第二问（轻松完成）**：对受限 sumset（restricted sumset）的类似问题，ChatGPT 也毫无困难地解决了。

**第三问（最 impressive，总计约1小时）**：针对 MIT 学生 Isaac Rajagopal 证明的指数依赖上界，Gowers 要求 ChatGPT 尝试收紧。模型经历了以下阶段：
- 16 分 41 秒：将上界从指数级改进到 k^(1/2+ε) 的次指数级
- Gowers 要求写成预印本，耗时 47 分 39 秒
- Rajagopal 审阅后认为看起来正确
- Gowers"贪心"地要求尝试多项式界
- 13 分 33 秒：ChatGPT 表示乐观，但有几个技术命题需要检查
- 9 分 12 秒：检查完成
- 31 分 40 秒：预印本完成
- Rajagopal 最终评估：**"几乎肯定正确"**，且在想法层面是真正原创的

Rajagopal 的原话："这是我花一两周思考后会非常自豪能想出的想法，而 ChatGPT 不到一小时就找到并证明了——使用的方法与我自己的证明类似。"

### 3. 核心数学创意：k-dissociated sets 的原创构造

ChatGPT 的突破性贡献在于独立构思了一种使用 **k-dissociated sets**（k-不相关集）的新构造方法，将上界从指数级降到了多项式级。Rajagopal 在技术附录中详细解释了这一点，认为其在数学思想层面具有真正的原创性。

---

## 发布者洞察（Gowers 的核心观点）

### AI 数学正以惊人速度逼近人类研究能力

Gowers 在 X Thread 中写道：

> "如果 AI 数学继续以当前速度发展——这正是我所预期的——那么我们很快将面临一场危机，数学系对他们的学生负有照护责任，应该紧急为此做准备。"

他进一步指出：

> "以你的名字永远与某个定理或定义相关联的那种激动人心的时代，可能已接近尾声。"

### 对 PhD 教育的冲击

Gowers 观察到，以前数学家会给初入研究领域的博士生布置一些"看起来相对温和的"开放问题，让他们获得首次解决正式开放问题的巨大鼓励。但如果 LLM 已经到了能解"温和问题"的程度，这个策略就不再可行了。问题的门槛被提高了：现在不仅需要一个开放问题，还需要它**足够难，难到 LLM 也解不了**。

### AI 产出成果的归属与存档问题

Gowers 提出了一个重要问题：这类 AI 产出的数学结果应该放在哪里？
- 如果由人类数学家产出，这个结果绝对是可发表的
- 但把它放进期刊似乎毫无意义——既然可以免费获取，没有人需要"署名功劳"
- arXiv 有政策反对接受 AI 写作内容
- 他建议也许需要一个新的仓库，由人类数学家审核认证 AI 产出的结果，或者最好由证明辅助工具（proof assistant）形式化验证

---

## 技术背景

### 问题领域：加法组合学（Additive Combinatorics）

Nathanson 的论文研究的是 sumset sizes 的问题。给定一个整数集合 A，其 h-重和集 hA 定义为 h 个 A 中元素之和的集合。核心问题是：给定 |A| = k，hA 可能的取值集合是什么？以及，要达到某个特定 |hA|，A 的直径（即元素的最大值）需要多大？

### ChatGPT 的方法论

- 对 h=2 的情况：利用 Sidon 集（和集最大化的集合）与等差数列的组合构造
- 对一般 h 的情况：在 Rajagopal 的指数界基础上，引入 k-dissociated sets 实现多项式界
- 使用生成函数作为簿记工具跟踪各组件集合的和集大小

---

## 社区反响

该帖子引发了数学界和 AI 研究社区的广泛讨论：

- **Sebastien Bubeck**（微软研究院）："非常重要。'如果 AI 数学继续以当前速度发展，我们很快将面临危机。'"
- **Matt Clifford**：引用 Gowers 的话讽刺"随机鹦鹉"论调——"模型证明了一个可以作为博士论文章节的结果"
- **Paul Graham**："我记得你在 2025 年愚人节说 AI 解决了一个开放问题，当时我想这可能不久就会成真。"
- **Michael Nielsen**："非常有趣的 thread（尤其是详细的博客文章）关于 LLM 与数学。"
- **Michael Bronstein**："我以为'随机鹦鹉'的棺材几年前就已经钉上了最后一根钉子。"
- **Danielle Fong**："除了需要数学家来获得结果，还需要数学家来理解它，以及一个来过滤垃圾。就像互联网上的其他东西一样。"

---

## 延伸思考

### 1. AI 数学能力的"阶梯式"进步

Gowers 回顾了 LLM 在数学领域的能力演进：
- 最初：LLM 只是发现文献中已有答案，或从已知结果 trivial 推导
- 后来：LLM 能解决一些人类因注意力分散而遗漏的"容易论证"
- 现在：LLM 能独立产生博士论文级别的原创数学思想

他承认，很多优秀的人类数学本质上也是"组合现有知识和证明技巧"，LLM 在这方面可能正在逼近甚至超越人类。

### 2. 研究数学中的"平等主义"终结

评论者 domotorp（Olof Sisask）指出："直到此刻，与大多数其他科学不同，在研究级别的数学中，拥有昂贵资源几乎没有任何优势。这已经一去不复返了。我不知道未来会怎样，但在这一刻，研究数学中的平等主义时代——在共产主义意义上——令人遗憾地结束了。"

### 3. 方法论启示：AI 辅助研究的"乒乓球模式"

一位评论者提到使用不同 AI 进行"pingpong 模式"：让 AI 1 写证明→让 AI 2 仔细检查错误和漏洞→反馈给 AI 1 修复。Gowers 的经历与此类似，只是他的"反馈"完全是非数学性的引导。

---

## 完整资源

- **Gowers 博客原文**：https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/
- **X Thread**：https://x.com/wtgowers/status/2052830948685676605
- **Isaac Rajagopal 的原始论文**（MIT，关于 sumset sizes）：https://arxiv.org/abs/2603.15556
- **Nathanson 的问题论文**：《Diversity, Equity and Inclusion for Problems in Additive Number Theory》
- **ChatGPT 产出的预印本（第一问）**：[Google Drive 链接](https://drive.google.com/file/d/11r-ggU__GMmHIrgEHQVULUIR1VxKSwmi/view?usp=drive_link)
- **ChatGPT 产出的预印本（第三问）**：[Google Drive 链接](https://drive.google.com/file/d/1IkJBcWYz_3J_QGsESBmMa-jrEHAJDcJB/view?usp=sharing)

---

来自翡冷翠
