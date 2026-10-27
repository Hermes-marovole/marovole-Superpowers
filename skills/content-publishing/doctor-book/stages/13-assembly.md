# 阶段 13：assembly 组装与导出

## 步骤

1. 先跑 `python3 SKILL_DIR/scripts/book_check.py <项目目录>`，有 FAIL 就回到对应阶段处理。只交样章（不是全书）时加 `--sample`，它会跳过章数、三幕比例和概念复现。
2. 确认封面与章节信息图已渲染就绪：若 `10_package/cover.html` 或 `10_package/figures/*.html` 有更新，运行 `python3 SKILL_DIR/scripts/render_visuals.py <项目目录>` 生成最新 PNG/JPG。
3. `python3 SKILL_DIR/scripts/assemble.py <项目目录>`：生成 `10_package/book.md`（自动将正文、前言、结语、附录中的 `[E0xx]` 转为上标 `^[1]^` 并汇总文末参考文献，自动补齐“第 X 章”编号，并按 `10_package/figures/manifest.json` 或 `figures/chNN.png` 约定把章节信息图内嵌进对应章节）、`verify_list.md`、`lint_report.md`。退出码不为 0 说明有章节 lint 失败，回到对应章节修改。
4. `python3 SKILL_DIR/scripts/export.py <项目目录>`：生成出版级排版的 `book.docx`（16 开 170×240mm 版心、五号宋体首行缩进 2 字符、仅在卷与章分页、全书三线表+斑马纹+跨页表头重复+中短表格 `≤9` 行 `keep_with_next` 整表锁页、加粗结论卡片框、书眉与页码）、带内嵌封面与防跨栏裁切配图的 `book.epub`（自动将“第 X 部分”卷标题合并为章首 `.part-banner` 横幅、将前言/结语/附录内部小节降为 `H3` 防碎片切页、对全部 `table/thead/tr/th/td` 施加 `break-inside: avoid; -webkit-column-break-inside: avoid;` 整表防跨页保护，并自动运行 `audit_epub()` 校验全书 0 空白碎片页、0 `[E0xx]` 引用残留、100% 表格防跨页保护），以及 `投稿包/` 和 `投稿包.zip`。导出到用户下载目录时统一用版本号命名（如 `《书名》_作者_v1.0.epub`，每次修改直接升版本号 `v1.1`、`v1.2`，不加“终版/完整版”等文字后缀）。
5. 抽查 `book.docx` 与 `book.epub`：用 `pandoc book.docx -t plain | head -200` 看目录和第一章是否正常，确认参考文献编号在正文里显示为上标 `[1]` 的形式、无残留 `[E0xx]`，并用 `unzip -l book.epub | grep media/` 确认封面与全部章节插图已打包进 EPUB。
6. 写 `10_package/delivery_report.md`：
   - 书名、副标题、章数、总字数、插图与表格数
   - 素材等级和它对质量的影响
   - 所有交付文件路径（含 `.docx`、`.epub`、封面、`投稿包.zip`）
   - `【待核实】` 条目总数和最重要的 10 条
   - 证据库条目数和"未联网核验"条目数
   - 审稿未完全通过的章节和剩余问题
   - 需要医生本人做的事：审读待核实清单、补充真实病例和经历、确认人设和书名、出版社医学审读
7. 把 `stages.assembly` 改为 `done`，按 SKILL.md 的"交付"一节向用户汇报。

## 完成标准

三个脚本（`render_visuals.py`、`assemble.py`、`export.py`）都成功；`book.docx`、`book.epub`（含封面与章节配图）和 `投稿包.zip` 存在且能打开；交付报告已写。
