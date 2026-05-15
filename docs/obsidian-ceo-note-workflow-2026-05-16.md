# Obsidian CEO 的笔记工作流深度解析：拥抱混乱与懒惰的知识复利系统

> 来源：X/Twitter @AYi_AInotes（大厂组织发展专家 × 心理学硕士 × AI 重度实践者）  
> 原始出处：Steph Ango（Obsidian CEO，GitHub: kepano）— https://stephango.com/vault  
> GitHub 模板仓库：kepano/kepano-obsidian（⭐ 3.2k，Fork 243）  
> 整理时间：2026-05-16  
> 来自翡冷翠

---

## 执行摘要

Obsidian CEO Steph Ango（GitHub 用户名 kepano）公开了他个人使用 Obsidian 的完整工作流。这套系统与大多数人使用 Obsidian 的方式截然相反——**几乎不用文件夹，也很少手动加标签**，核心只有三样东西：**模板、属性、内部链接**。其底层哲学是：好的笔记系统应该拥抱混乱和懒惰，先快速记录想法，结构会在后续的连接中自然涌现。几年后，你的 Vault 不会变成一堆死文件，而会变成一个活的「外部大脑」。

---

## 一、反直觉的真相：文件夹越多，笔记系统越没用

AYi 在帖子中一针见血地指出：

> "大多数人拿到 Obsidian 第一件事就是建一堆复杂的文件夹，然后花几个小时整理分类，最后越用越乱，干脆放弃。喵的我就是这样做的。"

Steph Ango 本人的做法完全相反：

- **不用文件夹做组织**：因为笔记往往属于多个类别，强行归入单一文件夹本身就是错误的
- **不用文件浏览器导航**：几乎不用左侧的文件树
- **根目录优先**：绝大多数笔记直接放在 Vault 的根目录下

**核心洞察**：当你把精力花在「决定这个笔记应该放在哪个文件夹」时，就已经产生了认知摩擦。高摩擦的系统最终一定会被废弃，只有低摩擦的系统才能产生知识复利。

---

## 二、三大核心支柱

Steph Ango 的工作流只依赖三个东西，其他一切（复杂插件、精美主题、多层文件夹）都是可选甚至是有害的。

### 支柱一：模板（Templates）

> "几乎每一个笔记都从模板开始。模板自动填充所有需要的元数据。"

**模板设计理念**：
- **每个类别一个模板**：会议、书籍、人物、地点、电影……都有专属模板
- **模板自动填充属性**：日期、人物、主题、地点、评分等
- **模板可组合**：例如 `Person` 和 `Author` 是两个不同模板，可以叠加到同一个笔记
- **懒加载信息**：模板让你「懒惰地」添加以后能找到笔记所需的信息

**Meeting 模板示例**：
```yaml
---
categories:
  - "[[Meetings]]"
type: []
date: 2026-05-16
org:
loc:
people: []
topics: []
---
```

**Book 模板示例**：
```yaml
---
categories:
  - "[[Books]]"
author: []
cover:
genre: []
pages:
isbn:
isbn13:
year:
rating:
topics: []
created: 2026-05-16
last:
via: ""
tags:
  - to-read
---
```

**People 模板示例**（包含动态引用）：
```yaml
---
categories:
  - "[[People]]"
birthday:
org: []
created: 2026-05-16
---
## Meetings

![[Meetings.base#Person]]
```

### 支柱二：属性（Properties）

> "这些属性不是静态的标签，是可以计算、可以过滤、可以生成任意视图的数据库。"

**属性的革命性**：
- 传统标签 = 静态分类 → 一旦贴上就无法改变
- Obsidian 属性 = 动态数据 → 可以作为 Bases（数据库视图）进行查询、排序、过滤

**Steph Ango 使用的核心属性类型**（从 `.obsidian/types.json` 提取）：

| 属性类型 | 用途 | 示例 |
|---------|------|------|
| `date` | 日期字段 | created, start, end, published, birthday |
| `number` | 数值字段 | rating, pages, year, price, runtime, season |
| `multitext` | 多值文本 | categories, tags, author, director, genre, people, topics |
| `text` | 单值文本 | model, system, source, status, role, address |

**跨类别共享属性**：
Steph Ango 刻意让属性名称在不同类别间复用。例如 `genre` 同时用于书籍、电影、电视节目，这样可以在一个视图中看到所有「科幻」类的内容，无论它是书、电影还是剧。

**属性命名规则**：
- 使用短名称（`start` 而非 `start-date`）→ 打字更快
- 默认使用 `list` 类型 → 即使现在只有一个值，未来也可以扩展
- 保持一致的命名风格 → 减少每次新建笔记时的决策摩擦

### 支柱三：内部链接（Internal Links）

> "我大量使用内部链接。我总是链接第一次提到的东西。"

**链接策略**：
- **首次提及必链接**：任何概念、人物、地点第一次出现时都要链接
- **允许未解析链接**：链接指向的笔记还不存在也没关系——这些「面包屑」是未来连接的伏笔
- **日记作为连接流**：日记条目往往是一连串事件的流水账，每个事件链接到对应的参考笔记

**日记条目示例**：
```markdown
I went to see the movie [[Perfect Days]] with [[Aisha]] at [[Vidiots]] and had Filipino food at [[Little Ongpin]]. I loved this quote from Perfect Days: [[Next time is next time, now is now]]. It reminds me of the essay ...
```

---

## 三、文件夹策略：极简到只有六个

Steph Ango 的 Vault 中绝大多数笔记都在**根目录**。他明确使用的文件夹只有以下六个：

| 文件夹 | 用途 | 位置策略 |
|--------|------|---------|
| **References** | 存放外部世界的事物：书籍、电影、地点、人物、播客 | 笔记在子文件夹，以标题命名（如 `Book title.md`） |
| **Clippings** | 保存他人写的内容：文章、论文、剪贴 | 直接从 Web Clipper 导入 |
| **Attachments** | 图片、音频、视频、PDF | 隐藏文件夹，不出现在导航中 |
| **Daily** | 每日笔记（`YYYY-MM-DD.md`） | 隐藏文件夹，不写内容，仅作为链接锚点 |
| **Templates** | 所有模板文件 | 隐藏文件夹 |
| **Categories** | 类别总览页面 | 在下载版中便于展示；个人使用时可放根目录 |

**两个核心原则**：
1. **根目录 = 我写的**：如果笔记在根目录，说明是我写的，或与我直接相关
2. **References = 外部世界**：书籍、电影等外部事物的笔记放在 References

---

## 四、分类系统：用属性替代文件夹

传统做法：
```
📁 Meetings/
  ├── 2026-01-15-project-a.md
  ├── 2026-02-03-project-b.md
📁 Books/
  ├── book-a.md
  ├── book-b.md
```

Steph Ango 的做法：
```
📁 (根目录)
  ├── 2026-01-15 Project A Meeting.md  ← categories: [[Meetings]]
  ├── 2026-02-03 Project B Meeting.md  ← categories: [[Meetings]]
  ├── Book A.md                        ← categories: [[Books]]
  ├── Book B.md                        ← categories: [[Books]]
```

**优势对比**：

| 维度 | 文件夹分类 | 属性分类 |
|------|-----------|---------|
| 一个笔记多个类别 | ❌ 不可能 | ✅ 天然支持 |
| 动态视图 | ❌ 静态结构 | ✅ Bases 自动聚合 |
| 排序方式 | ❌ 按文件名 | ✅ 按日期、评分、人物任意排序 |
| 添加笔记的摩擦 | ⚠️ 需要选择文件夹 | ✅ 直接放根目录，属性由模板自动填充 |
| 查找方式 | ⚠️ 浏览文件夹树 | ✅ Quick Switcher (Cmd/Ctrl+O) |

---

## 五、评分系统：1-7 分量化一切

Steph Ango 使用 1-7 分的整数评分系统来量化体验质量：

| 分数 | 含义 | 标准 |
|------|------|------|
| **7** | Perfect | 必须尝试，改变人生，值得特意去寻找 |
| **6** | Excellent | 值得重复体验 |
| **5** | Good | 不需要特意找，但体验愉快 |
| **4** | Passable | 凑合能用，应急可用 |
| **3** | Bad | 能避则避 |
| **2** | Atrocious | 主动避免，令人反感 |
| **1** | Evil | 负面地改变人生 |

**为什么用 7 分而非 5 分或 10 分？**
- 比 5 分制更精细（尤其是在高分段，需要区分「优秀」和「完美」）
- 比 10 分制更简洁（10 分太细，每次打分都要纠结）
- 7 是心理学上最舒适的选择粒度

---

## 六、分形日记与回顾节奏

Steph Ango 设计了一套分层的回顾系统，让知识在时间维度上自然涌现：

### 日常记录：Unique Note
- **快捷键触发**：Obsidian 的「Unique Note」热键
- **自动命名**：`YYYY-MM-DD HHmm 标题.md`
- **碎片化输入**：随时记录想法，不需要考虑结构

### 每几天：碎片汇编
- 回顾最近的日记碎片
- 把相关的零散想法汇编成更连贯的总结

### 每月：模式反思
- 使用「Monthly Note」模板
- 反思高层次的模式和「想法聚合」

### 每年：深度审视
- 使用 [40 个问题](https://stephango.com/40-questions) 模板
- 审视一整年的思考脉络

### 随机回顾：Random Revisit
- 每隔几个月使用「Random Note」热键随机穿梭
- 查看旧想法，发现缺失的链接，获取灵感
- **重要原则**：这个过程不自动化，不交给 AI。Steph Ango 明确说："Don't delegate understanding."

---

## 七、发布者洞察

### AYi 的个人共鸣
> "大多数人拿到 Obsidian 第一件事就是建一堆复杂的文件夹，然后花几个小时整理分类，最后越用越乱，干脆放弃。**喵的我就是这样做的。**"

AYi 的这句自嘲揭示了一个普遍现象：**完美主义是笔记系统的最大敌人**。我们以为复杂的分类体系会让知识更有序，实际上它制造了大量的前置决策成本，最终导致系统被废弃。

### Steph Ango 的设计哲学
> "好的笔记系统应该拥抱混乱和懒惰。你不应该为了整理而整理，应该先把想法快速记下来，结构会在后续的连接中自然涌现。"

这句话是整套系统的灵魂：**先记录，后组织；先连接，后分类**。传统的笔记系统要求你在记录之前就决定分类，而 Steph Ango 的方法让你先自由地写，然后通过链接和属性让结构自然浮现。

### 核心洞察：低摩擦 = 知识复利
> "很多人花了几百个小时折腾各种插件和主题，却从来没有真正建立起一个能长期坚持的笔记习惯。因为高摩擦的系统最终一定会被废弃，只有低摩擦的系统才能产生知识复利。"

这不仅是笔记系统的规律，也是所有工具使用的规律。**能坚持的系统比完美的系统更重要。**

---

## 八、为什么这套系统有效

### 1. 文件 over App（File over App）
Obsidian Vault 本质上就是一个文件夹里的 Markdown 文件。这意味着：
- 你的数据不依赖任何软件
- 格式开放、易于检索和读取
- 即使 Obsidian 消失，你的笔记依然可用

### 2. 涌现结构（Emergent Structure）
复杂系统理论告诉我们：**自下而上的涌现结构往往比自上而下的设计更健壮**。Steph Ango 的系统不预设分类体系，而是让链接和属性在使用过程中自然形成网络。

### 3. 一致的文风（Consistent Style）
Steph Ango 给自己设定了严格的文风规则：
- 类别和标签永远用复数（`#books` 而非 `#book`）
- 日期统一用 `YYYY-MM-DD`
- 避免非标准 Markdown
- 保持单一每周待办清单

> "Having a consistent style collapses hundreds of future decisions into one, and gives me focus."

### 4. 可操作的元数据（Actionable Metadata）
属性不是装饰性的标签，而是可计算的数据库字段。配合 Obsidian Bases 功能，可以：
- 一键查看所有和某人相关的会议
- 查看所有评分 7 分以上的书籍
- 查看在某个城市发生的所有事件

---

## 九、如何快速上手

### 第一步：下载模板仓库
```bash
# 方式一：直接下载 ZIP
curl -L -o vault.zip https://github.com/kepano/kepano-obsidian/archive/refs/heads/main.zip

# 方式二：Git 克隆
git clone https://github.com/kepano/kepano-obsidian.git
```

解压后，在 Obsidian 中「Open folder as vault」即可。

### 第二步：理解文件夹结构
```
Vault/
├── (根目录)        ← 你的日记、随笔、Evergreen 笔记
├── References/     ← 外部事物（书、电影、人、地点）
├── Clippings/      ← 他人写的内容
├── Attachments/    ← 图片、PDF（隐藏）
├── Daily/          ← 每日笔记（隐藏）
├── Templates/      ← 模板文件（隐藏）
└── Categories/     ← 类别总览页面
```

### 第三步：掌握核心热键
| 热键 | 功能 | 用途 |
|------|------|------|
| **Unique Note** | 创建时间戳笔记 | 随时记录想法 |
| **Random Note** | 随机打开笔记 | 回顾旧想法 |
| **Quick Switcher** (Cmd/Ctrl+O) | 快速搜索切换 | 替代文件浏览器 |
| **插入模板** | 从模板新建笔记 | 标准化元数据 |

### 第四步：建立你的第一条笔记
不要从整理旧笔记开始。从**今天的一个想法**开始，用模板创建，填上属性，加上内部链接。

---

## 十、模板类型全览

kepano/kepano-obsidian 仓库包含 50+ 个模板，覆盖生活的方方面面：

| 类别 | 模板示例 |
|------|---------|
| **媒体消费** | Book, Movie, Show, Podcast, Album, Video Game, Board Game |
| **人物关系** | People, Contact, Author, Actor, Director, Musician |
| **工作场景** | Meeting, Project, Job Interview, Conference, Email |
| **生活记录** | Place, Restaurant, Food, Coffee, Recipe, Trip |
| **知识管理** | Evergreen, Clipping, Post, Quote, Journal |
| **财务投资** | Product, Stock Trade, Real Estate |
| **时间管理** | Daily Note, Monthly Note, Event, Meditation |

---

## 十一、资源汇总

### 核心来源
| 资源 | 链接 | 说明 |
|------|------|------|
| Steph Ango 个人工作流 | https://stephango.com/vault | 最权威的一手资料 |
| GitHub 模板仓库 | https://github.com/kepano/kepano-obsidian | ⭐ 3.2k，可直接下载使用 |
| Minimal 主题 | https://stephango.com/minimal | Steph Ango 设计的 Obsidian 主题 |
| Flexoki 配色 | https://stephango.com/flexoki | 为网站和笔记设计的配色方案 |
| Web Clipper 模板 | https://github.com/kepano/clipper-templates | 网页剪贴模板 |
| 40 Questions 模板 | https://stephango.com/40-questions | 年度反思问题 |
| File over App | https://stephango.com/file-over-app | 数字文件哲学 |
| Evergreen Notes | https://stephango.com/evergreen-notes | 常青笔记方法论 |

### 相关工具
| 工具 | 说明 |
|------|------|
| Obsidian Sync | 跨设备同步 |
| Obsidian Web Clipper | 网页剪贴 |
| Obsidian Bases | 属性数据库视图 |
| Obsidian Maps | 地图视图（用于地点模板）|
| Obsidian Git | 将笔记推送到 GitHub |
| Jekyll | 静态网站生成器（用于发布笔记）|
| Quartz / Astro / Eleventy / Hugo | 替代 Jekyll 的发布方案 |

### 第三方解读
| 文章 | 链接 |
|------|------|
| How the CEO of Obsidian Takes his Notes | https://algieg.prose.sh/How_the_CEO_of_Obsidian_Takes_ |
| How I Use Obsidian (2025) | https://jeredsutton.com/post/how-i-use-obsidian-2025/ |
| Obsidian Forum 讨论 | https://forum.obsidian.md/t/questions-about-steph-angos-vault-system/111565 |
| YouTube 解读视频 | https://www.youtube.com/watch?v=Dq3R3uS0sQ4 |

---

## 十二、常见问题

**Q1: 我完全不用文件夹吗？**
> 不是。Steph Ango 用 6 个文件夹，但大部分笔记在根目录。关键是「尽量少用」，避免分类成为记录的前置障碍。

**Q2: 如果笔记很多，根目录不会很乱吗？**
> 不会。因为你不用文件浏览器导航。通过 Quick Switcher、内部链接、Bases 视图来查找，根本看不到根目录的「混乱」。

**Q3: 这套系统适合初学者吗？**
> 适合。实际上这套系统比复杂的文件夹体系更适合初学者，因为它减少了学习成本和决策摩擦。

**Q4: 我需要用所有模板吗？**
> 不需要。从 2-3 个你最常用的模板开始（比如 Meeting + Book + Daily Note），逐步扩展。

**Q5: 属性比标签好在哪里？**
> 属性是结构化数据（日期、数值、多选文本），可以被 Bases 查询和排序。标签是静态字符串，只能做简单的包含匹配。

---

## 十三、核心金句汇总

> "你在 Obsidian 里建的文件夹越多，你的笔记系统就越没用。" — AYi

> "好的笔记系统应该拥抱混乱和懒惰。" — Steph Ango

> "你不应该为了整理而整理，应该先把想法快速记下来，结构会在后续的连接中自然涌现。" — Steph Ango

> "高摩擦的系统最终一定会被废弃，只有低摩擦的系统才能产生知识复利。" — AYi

> "几年后你的 Vault 不会变成一堆死文件，它会变成一个活的外部大脑。" — AYi

> "Don't delegate understanding." — Steph Ango

> "Having a consistent style collapses hundreds of future decisions into one, and gives me focus." — Steph Ango

---

*来自翡冷翠*
