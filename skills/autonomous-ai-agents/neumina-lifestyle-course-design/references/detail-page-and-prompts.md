# Detail Page TOC + Co-create Prompts

## Standard detail-page directory

```text
主标题 + 副标题
开场 · 你还没病，但哪儿哪儿不对劲
为什么这个人群尤其要管
机制 · 到底怎么来的（短）
课程是什么 · 不极端的 14 天
分两步走（W1/W2）
你会得到什么
多久见效 · 说实话的时间线
适合谁 / 不适合谁
每天怎么打卡
加分项
FAQ
结尾 CTA（从 Day 0 记下/拍下第一笔）
```

## Honest timeline template

- **1–3 天**：最先感到的变化  
- **3–7 天**：体感改善  
- **1–2 周**：更可见的变化  
- **更深改善**：更久且因人而异  
- **收束**：别跟别人比，跟自己的 Day 0 / 昨天比  

## FAQ defaults (adapt per theme)

- 要极端戒断/饿肚子吗？→ 教换掉与重排，不卖剥夺  
- 一定要补剂吗？→ 主线是行为；补剂可选，缺啥查啥  
- 多久有效？→ 用 honest timeline，拒绝速效神话  
- 现实约束（外卖/出差/带娃）？→ 降级版也算赢 + 情绪解锁  

## CTA pattern

```text
从第 0 天开始：把你平常的一天{证据}记下来。
那是你的起点。14 天后，你会看见{隐喻}变化了多少。
{主题动词}，从看清自己开始。今天就记下第一笔。
```

## Co-create system prompt (paste-ready)

```text
你是 Neumina 课程设计师。请按「11 层课程骨架」输出一门 14 天生活方式课。
人群：40–60 岁中国女性（不对外包装更年期）。主题：{THEME}。
必须包含：一句话定位、核心公式、三增三减、绿红名单、Day0 基线、
W1 清空 6 天 + Day7 评估、W2 养成 6 天 + Day14 结业、
每日四件套、6 维评分、体感5项、加分3项、补剂三梯队、
详情页文案目录、合规边界。
语气：温暖、可执行、不诊断、不速效承诺。每天只做一件事。
输出两份 Markdown：课程设计文档 + 小程序详情页文案。
示范标注为「较严格版本」，并写出现实降级鼓励。
```

## Extraction prompt (from legacy docs)

```text
阅读以下课程设计/详情页/会议记录。抽取可复用的课程操作系统：
11 层骨架、每日四件套、评分维、周评估字段、产品补丁、反模式。
不要复述某一门课的菜谱细节；输出通用框架 + 主题迁移映射表。
```

## Product config hints (for SPA / miniprogram)

Reuse chrome across themes via config, not forks:

| Anti-inflam component | Generic key | Cortisol example |
|----------------------|-------------|------------------|
| 餐盘公式 | `formula` | 日节奏盘 |
| 三增三减 | `rules6` | same shape |
| 6-dim meal score | `scoreDims[]` | stress-day dims |
| meal photo | `checkinEvidence` | multi-type evidence |
| 加分锦囊 | `dailyBonus` | reuse component |
| 结业 3 件事 | `graduationKeeps` | reuse |
| 灵芝 AI | `aiRail` | swap knowledge pack |

State key: bump `course_state_vN` when score schema changes.
