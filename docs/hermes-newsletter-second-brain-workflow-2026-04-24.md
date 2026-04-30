# Hermes Agent 工作流：用顶级 AI Newsletter 构建第二大脑 - 完整整理

> 来源：https://x.com/lxfater/status/2047150392274993624?s=46  
> 作者：铁锤人 @lxfater  
> 整理时间：2026-04-24  
> 来自翡冷翠

---

## 简介

这篇文章介绍了一套面向 AI 学习与内容输出的 Hermes Agent 工作流：先用高质量海外 AI Newsletter 替换低信号信息源，再把 Newsletter 接入 Agent 专属邮箱，让 Hermes 每天筛选、摘要、推荐值得深读的内容，最后把精读文章编译进 LLM Wiki / Obsidian 第二大脑，并反向驱动 X 文章、信息图、公众号内容等输出。

核心不是“收藏更多信息”，而是把信息处理链路自动化：

```text
高质量 Newsletter → Agent 邮箱 → mail-cli / ClawEmail → 每日摘要 → 文章筛选 → LLM Wiki 编译 → Obsidian 知识图谱 → 内容输出
```

---

## 内容清单总览

| 序号 | 内容 | 类型 | 核心亮点 |
|------|------|------|----------|
| 1 | 顶级 AI Newsletter 信息源清单 | 信息源 | 从 50+ 来源筛选出 10 个高信号海外 Newsletter |
| 2 | ClawEmail / mail-cli Agent 邮箱配置 | 工具链 | 给 Hermes 配置可读、可搜、可回复的邮箱输入管道 |
| 3 | Newsletter 专属子邮箱 | 信息隔离 | 把 Newsletter 与客服、个人邮件等场景隔离 |
| 4 | Daily Report Skill | 自动摘要 | 每日把 Newsletter 摘要与推荐推送给用户 |
| 5 | LLM Wiki / Obsidian 第二大脑 | 知识编译 | 用 Agent 把文章拆成概念、实体、主张与双向链接 |
| 6 | 基于 Wiki 的输出系统 | 内容生产 | 用知识图谱支撑信息图、X 文章、公众号草稿 |
| 7 | 关联文章：Obsidian + Claude Code 第二大脑 | 深度教程 | 介绍 Karpathy LLM Knowledge Base 方法落地 |
| 8 | 关联文章：md2wechat 公众号排版 Skill | 发布流程 | Markdown 自动排版并推送到微信公众号草稿 |

---

## 一、为什么要换信息源

文章的起点是一个常见问题：每天都在刷 AI 信息，但关上手机后什么都没进脑子。不是学习不努力，而是信息源与处理方式从一开始就错了。

作者认为，AI 赛道变化太快，真正有信号的源头大多来自海外 Newsletter、开发者社区、研究者博客，而国内公众号往往经过多层转述与洗稿，看到时已经是二手信息。

关键判断：

- 信息源质量决定学习质量，垃圾进垃圾出。
- 与其刷大量碎片推文，不如稳定接入高质量 Newsletter。
- 信息源进入 Agent 后，才能形成自动化筛选、摘要、精读、沉淀、输出的闭环。

---

## 二、高质量 AI Newsletter 清单

作者从 50+ 信息源中筛选出 10 个值得订阅的 AI Newsletter：

| Newsletter | 链接 | 频率/定位 | 核心价值 |
|------------|------|-----------|----------|
| The Rundown AI | https://therundown.ai | 每日 AI 产业动态 | 通俗易懂、密度高，适合快速了解产业变化 |
| TLDR AI | https://tldr.tech | 5 分钟科技简报 | AI + 编程 + 产品精华浓缩 |
| The Neuron | https://www.theneurondaily.com | AI 日报 | 面向非技术读者，3 分钟读完 |
| Ben's Bites | https://www.bensbites.com | AI 工具日报 | Ben Tossell 维护，适合追踪工具圈动态 |
| Latent Space | https://www.latent.space | 开发者 Newsletter | swyx 主理，偏工程视角、未公开项目与 AI infra |
| Smol AI News | https://smol.ai/news | 社区情报 | Discord、Reddit 等 AI 社区一线信息 |
| Interconnects | https://www.interconnects.ai | 深度专栏 | Nathan Lambert 关于 RLHF、模型训练、开源模型的分析 |
| One Useful Thing | https://www.oneusefulthing.org | AI 实用洞察 | Ethan Mollick 的学术与工作场景洞察 |
| AI Breakfast | https://aibreakfast.beehiiv.com | 每周 AI 新闻早餐 | 系统回顾与深度讨论 |
| Every | https://every.to | 商业/科技分析 | 科技与商业下一步，偏战略与专家观点 |

建议订阅策略：

1. 先订阅 3 个日报源：The Rundown AI、TLDR AI、The Neuron。
2. 再订阅 2 个深度源：Latent Space、Interconnects。
3. 最后补充商业与内容视角：Every、One Useful Thing、AI Breakfast。
4. 不要一开始订阅太多，否则 Agent 摘要有用，但人类复盘压力会变大。

---

## 三、第一步：给 Hermes 配置 Agent 邮箱

文章推荐使用网易新出的 Agent 专属邮箱产品 ClawEmail：

- 官网：https://claw.163.com/?channel=lxfater
- 内测邀请码：CLAW3C02D3891B6C

ClawEmail 的价值在于，它不是传统人类邮箱，而是面向 Agent 的邮箱：

- Agent 可以读邮件
- Agent 可以搜索关键词
- Agent 可以拉取正文
- Agent 可以处理确认邮件
- Agent 可以回复部分人机检查邮件

文章中给出的基础 mail-cli 配置流程：

```bash
# 1. 全局安装 mail-cli
npm install -g @clawemail/mail-cli

# 2. 把 API Key 写进系统钥匙串
mail-cli auth apikey set ck_live_xxxxxxxxxxxxxxxx

# 3. 登录主邮箱
mail-cli auth login --user yourname@claw.163.com

# 4. 测试连接
mail-cli auth test
```

文章也建议让 Hermes 阅读官方 CLI 文档并制作一个专门操纵 ClawEmail 的 Skill：

```text
https://claw.163.com/projects/doc/ 阅读这个CLI文档，然后制作一个Skill来专门来操纵这CLI。
```

### 本机执行记录

本次已按用户提供的配置链接执行安装：

```bash
npx "@clawemail/claw-setup@latest" --auth-url "t1/uTPWhZ4Faeg8eGC3PAQkVfVTVu4"
```

首次执行失败，原因是全局 npm 安装目录 `/usr/local/lib/node_modules` 无权限。已改用用户级 npm prefix：

```bash
mkdir -p "$HOME/.npm-global"
npm config set prefix "$HOME/.npm-global"
export PATH="$HOME/.npm-global/bin:$PATH"
```

随后安装 OpenClaw 并重新运行配置：

```bash
npm install -g openclaw --force
npx "@clawemail/claw-setup@latest" --auth-url "t1/uTPWhZ4Faeg8eGC3PAQkVfVTVu4"
```

配置结果：

- mail-cli 已安装
- OpenClaw Email 插件已安装到 `/Users/marovole/.openclaw/extensions/email`
- 账号信息获取成功
- API Key 已设置
- 已添加 Email Channel 账号：`hermes4.04@claw.163.com`
- 已生成并绑定机器人
- OpenClaw Gateway 已重启
- `mail-cli auth test` 验证通过

当前 mail-cli 状态：

```text
profile: 04
user: hermes4.04@claw.163.com
config: /Users/marovole/.config/mail-cli/config.json
transport: ajax
```

注意：后续终端使用 mail-cli 时，需要确保 PATH 包含：

```bash
export PATH="$HOME/.npm-global/bin:$PATH"
```

---

## 四、第二步：构建 Newsletter 专属子邮箱

文章建议不要把 Newsletter、客服、个人邮件混在一个邮箱里。更好的方法是为 Newsletter 创建专属子邮箱：

```bash
mail-cli clawemail create \
  --prefix newsletter \
  --type sub \
  --display-name "Newsletter Bot"
```

然后在 Dashboard 中配置通讯规则：

1. Dashboard → Agent 邮箱管理 → 选中 newsletter 子邮箱 → 通讯规则
2. 开启“开放外部通信”
3. 收信范围选择“所有人”

原因：Newsletter 发件域名非常分散，如果用白名单维护成本会很高。

订阅方式：

```text
yourname.newsletter@claw.163.com
```

以后遇到 Newsletter 订阅框，就直接填写这个子邮箱。确认邮件到达后，让 Hermes 从邮件正文中提取确认链接，必要时打开浏览器完成确认；若需要回复邮件进行人机检查，也可以让 Agent 辅助回复。

---

## 五、第三步：Daily Report Skill 初筛 Newsletter

文章提到 ClawEmail 官方提供了一个 Daily Report 能力，可以每天早上发送一封日报到 Gmail，内容包括：

- 当天所有 Newsletter 的摘要
- 重点内容推荐
- 值得深读的文章

安装命令：

```bash
npx skills add https://claw.163.com/gitea-web/s/daily-report.git
```

这一步的关键不是“让 AI 帮你读完省时间”，而是让 AI 帮你完成第一层筛选：

```text
今天几十封 Newsletter → 摘要 → 选出最值得深读的一篇
```

这会把人类的注意力从“扫所有信息”变成“判断最值得投入的主题”。

---

## 六、第四步：用 LLM Wiki 消化知识

文章的核心在这里：把 Daily Report 中筛出来的高价值文章编译进 LLM Wiki。

作者对 LLM Wiki 的类比：

> 它像个实习生。每天你扔一篇文章给它，它把里面的概念、实体、主张、开放问题一个个拆出来，每个做一张索引卡片贴在墙上，再用线把新卡片和已有相关卡片连起来。久了，这堵墙就是一张活的知识图。

操作方式：

```text
让 Hermes 找出邮箱里你感兴趣的文章，然后告诉它：
“这篇编译到我的 Wiki。”
```

Agent 会产出一组互相链接的 Markdown 文件，通常包括：

- 文章摘要
- 关键概念页
- 人物页
- 工具页
- 方法页
- 主张与反驳
- 开放问题
- 与旧知识的双向链接
- index.md 索引更新
- log.md 操作记录

打开 Obsidian 图谱后，可以看到知识点之间的连接。新文章不再是孤立收藏，而是会刷新旧概念、补充旧论据、建立新旧知识之间的连接。

文章给出的关键认知收益：

- 别人每天刷 100 条推文，一天就忘。
- 你一天精读一篇，但每篇都会关联已有知识。
- 读 1 篇，等于刷新 10 篇。
- 知识图谱每天厚一点，长期形成复利。

---

## 七、关联文章一：Obsidian + Claude Code 第二大脑

关联链接：
https://x.com/lxfater/status/2042848343949480173

标题：
《Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）》

这篇文章进一步解释了 Karpathy 的 LLM Knowledge Base 方法。

### 核心问题

传统第二大脑容易死掉，因为维护成本太高：

- 标签过时没人改
- 断链没人修
- 新笔记扔进去后无人整理
- 结构几个月后变成垃圾堆
- 最后只能重建，然后再次烂尾

### Karpathy 方法的三层结构

文章总结 Karpathy 的方法为三层：

```text
raw/   → 原始素材
wiki/  → AI 整理后的知识页面
规则文件 → 告诉 AI 如何维护这套系统
```

常见操作只有三种：

1. 录入：把文章、网页、思考、对话等原始素材放入 raw/，让 Agent 编译到 wiki/。
2. 查询：让 Agent 先读 index.md，再按需读具体页面。
3. 修复：定期检查孤儿页面、概念重复、矛盾说法、过时信息。

### 推荐目录

```text
vault/
  raw/        # 原始素材
  wiki/       # 编译后的知识页面
  index.md   # 所有知识页面索引
  log.md     # 操作历史
  rules.md   # Wiki 维护规则
```

### 健康检查

可以在 Claude Code / Hermes 中定期执行：

```text
帮我检查一下 Wiki 的健康状况。
```

Agent 应检查：

- 哪些页面之间说法有矛盾
- 哪些页面没有任何链接指向它（孤儿页面）
- 哪些概念被反复提到但还没有自己的页面
- 哪些信息已经过时，被新素材推翻

更进一步，可以把这一步写成每周自动任务，让 Wiki 每周自动体检与修复。

### AI 如何使用 Wiki

把 `wiki/index.md` 地址写进 Agent 配置文件，例如 Claude Code 的 `CLAUDE.md` 或 Hermes 的相关 Skill / Memory / Project Context：

```text
需要了解我的长期知识库时，先读取这个目录下的 wiki/index.md，再按索引读取相关页面。
```

这样 AI 不需要每次从零了解你，也不需要把所有笔记塞进上下文。它会先读 index，再按需展开，节省 token，同时输出更贴近你的知识体系。

---

## 八、关联文章二：md2wechat 公众号排版 Skill

关联链接：
https://x.com/lxfater/status/2037047059384328315

标题：
《这个开源 Skill，自动排版，发送到公众号草稿，不花一分钱》

这篇文章补齐了“输出到公众号”的最后一步。

### 解决的问题

很多人写完文章后不愿意发公众号，因为排版麻烦。最后内容只发在 X 上，被别人搬运到公众号或其他平台。

md2wechat Skill 的目标：

- Markdown 自动排版
- 图片上传与地址替换
- 推送到微信公众号草稿
- 降低从 X / Markdown 到公众号发布的摩擦

### 安装命令

文章给出的安装提示词：

```markdown
请帮我安装 md2wechat 并验证可用。按这个顺序执行：
1. 运行：curl -fsSL https://github.com/geekjourneyx/md2wechat-skill/releases/download/v2.0.4/install.sh | bash
2. 运行：npx skills add https://github.com/geekjourneyx/md2wechat-skill --skill md2wechat
3. 运行：export PATH="$HOME/.local/bin:$PATH"
4. 运行：md2wechat version --json
5. 运行：md2wechat config init
6. 运行：md2wechat capabilities --json
如果某一步失败，请直接告诉我失败原因和下一步修复命令，不要省略命令。
```

### 配置变量

如果要自动推送到微信公众号草稿，需要：

- WECHAT_APPID
- WECHAT_SECRET

配置后，可让 Agent 执行：

```text
使用 AI 模式 html，上传图片后，更新图片地址，发布到草稿。
```

这一步与前面的 LLM Wiki 结合后，形成完整输出链路：

```text
Newsletter → Wiki → 文章草稿 → md2wechat → 公众号草稿
```

---

## 九、完整 Hermes 工作流复盘

### 1. 输入层：高质量信息源

订阅高信号海外 AI Newsletter，避免低质量二手信息污染输入。

```text
The Rundown AI / TLDR AI / The Neuron / Latent Space / Interconnects / Every ...
```

### 2. 管道层：Agent 邮箱

用 ClawEmail + mail-cli 给 Hermes 一个可以读取、搜索、确认订阅、回复邮件的输入管道。

```text
Newsletter → hermes4.04@claw.163.com / newsletter 子邮箱 → mail-cli → Hermes
```

### 3. 初筛层：Daily Report

每天自动摘要所有 Newsletter，并选出最值得深读的文章。

```bash
npx skills add https://claw.163.com/gitea-web/s/daily-report.git
```

### 4. 消化层：LLM Wiki

把深读文章编译成知识图谱，而不是简单收藏。

```text
文章 → 概念 / 实体 / 主张 / 工具 / 方法 / 开放问题 → Markdown 双链
```

### 5. 复利层：Obsidian 图谱 + 每周修复

用 Obsidian 可视化图谱，用 Agent 定期检查并修复 Wiki 健康度。

```text
孤儿页面 / 过时概念 / 矛盾主张 / 未建页概念 → 周期性修复
```

### 6. 输出层：X / 信息图 / 公众号

基于 Wiki index 与相关页面，生成：

- X 长帖
- 信息图
- 公众号文章
- 研究报告
- 产品洞察
- Skill / SOP

---

## 十、对 Neuma / Neumina / Hermes 的落地建议

### A. 为 Hermes 新增 ClawEmail Skill

虽然当前已安装 mail-cli，但最好沉淀为 Hermes Skill，触发场景包括：

- “查一下 Agent 邮箱”
- “帮我看今天 Newsletter”
- “找一下确认邮件”
- “回复这封邮件”
- “把这篇邮件编译进 Obsidian Wiki”

Skill 应覆盖：

```bash
export PATH="$HOME/.npm-global/bin:$PATH"
mail-cli auth test
mail-cli clawemail list
mail-cli folder list
mail-cli mail list
mail-cli read <message-id>
mail-cli compose ...
```

### B. 创建 Newsletter 子邮箱

当前已配置 `hermes4.04@claw.163.com`，建议后续创建专门的 newsletter 子邮箱，避免与其他 Agent 邮件任务混杂。

建议命名：

```text
hermes4.newsletter@claw.163.com
```

### C. 把 Newsletter Daily Report 接入 Hermes cron

每天早上自动：

1. 读取过去 24 小时 Newsletter。
2. 生成摘要。
3. 选出 1-3 篇最值得深读文章。
4. 输出到 Obsidian Daily Note。
5. 如果主题与 Neumina / AI Agent / Biohacking 强相关，则创建 Linear 研究任务。

### D. 把 LLM Wiki 接入 Obsidian Vault

用户 Obsidian Vault 路径：

```text
/Users/marovole/Library/CloudStorage/Dropbox/Obsidian Vault
```

建议在其中建立：

```text
AI Wiki/
  raw/
  wiki/
  index.md
  log.md
  rules.md
```

Hermes 后续处理 Newsletter 时，默认把高价值文章编译进这里。

### E. 与 Neuma-Superpower 的关系

Neuma-Superpower 更适合作为“已研究并整理成文档/Skill 的成果库”；Obsidian Wiki 更适合作为“持续增厚的知识网络”。

建议分工：

```text
ClawEmail / Newsletter → Obsidian AI Wiki → 成熟主题 → Neuma-Superpower docs/ 或 skills/
```

---

## 资源汇总

### 原文与关联文章

| 名称 | 链接 | 说明 |
|------|------|------|
| Hermes Agent 工作流：用顶级 AI Newsletter 构建第二大脑 | https://x.com/lxfater/status/2047150392274993624?s=46 | 主文 |
| Obsidian + Claude Code 第二大脑教程 | https://x.com/lxfater/status/2042848343949480173 | LLM Wiki / Karpathy 方法详解 |
| md2wechat 公众号排版 Skill | https://x.com/lxfater/status/2037047059384328315 | Markdown 到公众号草稿发布 |

### 工具链接

| 工具 | 链接 | 说明 |
|------|------|------|
| ClawEmail | https://claw.163.com/?channel=lxfater | Agent 专属邮箱 |
| ClawEmail CLI 文档 | https://claw.163.com/projects/doc/ | mail-cli 官方文档 |
| Daily Report Skill | https://claw.163.com/gitea-web/s/daily-report.git | Newsletter 日报 Skill |
| md2wechat Skill | https://github.com/geekjourneyx/md2wechat-skill | 公众号排版与草稿发布 |
| Obsidian | https://obsidian.md | Markdown 知识库 |
| Claude Code | https://claude.ai/code | Anthropic 编程 Agent |

### Newsletter 链接

| Newsletter | 链接 |
|------------|------|
| The Rundown AI | https://therundown.ai |
| TLDR AI | https://tldr.tech |
| The Neuron | https://www.theneurondaily.com |
| Ben's Bites | https://www.bensbites.com |
| Latent Space | https://www.latent.space |
| Smol AI News | https://smol.ai/news |
| Interconnects | https://www.interconnects.ai |
| One Useful Thing | https://www.oneusefulthing.org |
| AI Breakfast | https://aibreakfast.beehiiv.com |
| Every | https://every.to |

---

## 快速执行清单

### 已完成

- [x] 安装 @clawemail/mail-cli
- [x] 安装 openclaw
- [x] 执行用户提供的 ClawEmail 配置链接
- [x] 添加并绑定 `hermes4.04@claw.163.com`
- [x] `mail-cli auth test` 验证通过
- [x] 将 npm 用户级 prefix 配置为 `~/.npm-global`

### 建议下一步

- [ ] 创建 newsletter 专属子邮箱
- [ ] 开通子邮箱外部收信规则
- [ ] 订阅核心 5-10 个 AI Newsletter
- [ ] 安装 Daily Report Skill
- [ ] 创建 ClawEmail Hermes Skill
- [ ] 在 Obsidian Vault 中建立 AI Wiki 目录
- [ ] 配置每日 Newsletter digest cron
- [ ] 配置每周 Wiki 健康检查 cron

---

## 一句话总结

这套工作流的真正价值，不是让 Agent 替你“读更多信息”，而是让 Agent 把高质量信息变成可检索、可链接、可复利、可输出的个人知识网络。

```text
少刷一点，多编译一点；少收藏一点，多连接一点；少问 AI 从零想，多让 AI 读取你的长期知识库。
```

---

*来自翡冷翠*
