# 阶段 9：drafting 逐章写作

目标：按简报写出每章初稿，并让每章通过 lint。

## 派发

有子代理就每章派一个写作子代理，最多 4 个并行；按章号顺序派发，第 1 章先单独写完并通过 lint，用它校准文风后再并行写其余章节。没有子代理就按章号顺序自己写，每章开始前只读下面列出的文件。

写作子代理的交接说明（把 `<>` 换成实际值，原样发出）：

```
你在为医生 <姓名> 写书《<书名>》的第 <NN> 章。只写这一章。
项目目录：<项目目录>；skill 目录：<SKILL_DIR>
先读这些文件：
- <项目目录>/05_architecture/briefs/ch<NN>.md（本章简报，必须逐项落实）
- <项目目录>/02_voice/voice_profile.md
- <SKILL_DIR>/references/chapter-template.md
- <SKILL_DIR>/references/voice-style.md
- <SKILL_DIR>/references/compliance-cn.md
- 简报里列出的模式卡片（在 <SKILL_DIR>/references/patterns/ 里按卡片名搜索）
- 证据库和素材库里简报列出的条目（用 grep 按编号查，不要通读）
- 上一章简报的"结尾"一节和下一章简报的"冷开场"一节（用来写衔接）
写到 <项目目录>/07_drafts/ch<NN>.md，格式：
- 开头 YAML：chapter、part、type、title、budget（取自简报）
- 正文小标题用 ##，不写章标题
- 引用研究处标 [E编号]；使用素材库病例的段落前一行写 <!-- src: C编号 -->；情景示例在首次出现时写明"（情景示例）"或说明为复合案例
- 素材里没有的事实、医生经历和原话，写成【待核实：说明】
- 需要配图的地方写【插图：画什么、要说明什么】，组装时会汇总成插图需求清单
- lint 的文风指标（WARN）是体检，不是考试：不要为了凑指标把小标题改成粗体、硬塞"我"或拆散段落；确实因内容需要而越界的，在回复里说明理由
章节较长时分 2–3 次写入（按节拍顺序追加），不要一次性生成整章。
写完运行：python3 <SKILL_DIR>/scripts/lint_chapter.py <项目目录>/07_drafts/ch<NN>.md
有 FAIL 就改，直到退出码为 0（最多 5 轮）。WARN 尽量消除。
注意：disease、tactic、plan 章的行动清单必须出现在全章最后 30% 以内，并且写明就医红线。
最后回复：lint 最后一次的完整输出、【待核实】条目数、你偏离简报的地方及原因。
```

## 总控要做的

1. 收到每章结果后，看 lint 输出；退出码不是 0 的章，用 resume 让同一个子代理继续修改。
2. 在 `state.json` 的 `chapters.NN.status` 写 `drafted`，并记录待核实数。
3. 全部写完后运行 `python3 SKILL_DIR/scripts/book_stats.py <项目目录>`，超出预算 ±15% 的章节让对应子代理增删。

## 完成标准

每章 lint 退出码为 0，状态都是 `drafted`。把 `stages.drafting` 改为 `done`。
