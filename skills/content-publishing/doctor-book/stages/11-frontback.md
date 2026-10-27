# 阶段 11：frontback 前言、结语、附录

目标：写前言、结语、附录工具和术语表。

先读：`references/patterns/preface-epilogue.md`、`references/patterns/endings-tools.md`、`references/compliance-cn.md`、`03_positioning/positioning.md`、`05_architecture/outline.md`。

所有文件写在 `09_backmatter/`，开头都带 YAML（`chapter: 0`、`type`、`title`、`budget`），正文第一行用 `# 标题`。

## 文件

1. `preface.md` 前言（type: essay，3–5%）：作者故事钩子（S 条目；没有就用履历事实 + `【待核实】`）→ 读者痛点 → 命题转向 → 框架预告（一张概念关系图的文字描述）→ 承诺 → 怎么读这本书 → 免责说明（本书不能代替面诊；用药调整必须遵医嘱；有红线症状立即就医）。
2. `afterword.md` 结语（type: essay，2–4%）：回收全书开场的人物或故事，只换解释、不换信息 → 为什么值得这样做（意义层）→ 一个最小的第一步。
3. `appendix_1_selftest.md` 自测问卷与饮食摸底（type: plan）：按 `patterns/endings-tools.md` 的问卷模板，题目、计分、分档解释、对应章节、就医阈值齐全；对于营养/代谢类书籍，强烈推荐结合**“5 分钟近 3 个月饮食习惯半定量频率自查卡”**（按“每天几次 / 每周几次 × 单次估算量”快速摸底主食碳水与肉蛋奶优质蛋白的结构性缺口）。
4. `appendix_2_plan.md` 行动计划（type: plan）：4 周或 12 周分阶段计划，每周目标、具体动作、记录方式、复评点。
5. `appendix_3_redflags.md` 就医红线速查（type: plan）：出现哪些情况必须马上去医院、挂哪个科。
6. `appendix_4_indicators.md` 指标速查（type: plan，适用时）：指标、参考范围、指南推荐目标、复查频率、对应章节，全部带 [E编号]。
7. `glossary.md` 术语表（type: plan）：全书所有命名概念和医学术语，每条一句话解释 + 首次出现章节。
8. `acknowledgements.md` 致谢：只写占位 `【待核实：请医生补充致谢对象】`。

## 步骤

1. 逐个写完后对每个文件跑 `lint_chapter.py`，退出码必须为 0。
2. **前言、结语与附录的医学科学性核查（必做！在进入阶段 12 画图与阶段 13 排版之前完成）**：
   对照 `references/scientific-audit.md` 的六大高危区，专门检查 `09_backmatter/*.md`：
   - **结语（`afterword.md`）**：开场回收人物的复查指标判读是否完全符合诊断切点与缓解线（如 `2hPG 8.1 mmol/L` 仍属 IGT，绝不能写“已退出糖前切点”或算错达标项数）；
   - **自测表与行动计划（`appendix_1` / `appendix_2`）**：分龄切点（如 AWGS 2025 五次起坐 50–64 岁 `≥10.0s` vs ≥65 岁 `≥12.0s`、DXA vs BIA 切点）、测试主食生熟重与碳水克数（`50g 总碳水 ≈ 65g 生米 ≈ 170–200g 熟饭`）、红黄绿灯阈值是否与正文完全一致；表格严格控制在 `≤9 行`、`≤5 列`、`0 空白单元格`、`0 <br>`；
   - **就医红线与用药安全（`appendix_3`）**：保钾药/CKD（防高钾）与胰岛素/磺脲类（防低血糖）是否分开、是否注明**阿卡波糖服药者低血糖急救必须直接用葡萄糖片/葡萄糖水**、是否避免将慢性肝病/肝硬化误列为高蛋白禁忌；
   - **核心指标速查表（`appendix_4`）**：**HOMA-IR 等公式必须加粗标注单位（空腹胰岛素单位必须为 `μIU/mL`，若化验单为 `pmol/L` 必须先除以 `6.0` 换算）**。
3. 运行 `book_stats.py`，全书合计必须在 8–12 万字之间；超出就删减第二部分最长的章节，不足就补充第三部分的方法细节。

## 完成标准

8 个文件齐全，lint 全部通过，前言/结语/附录全部通过 `references/scientific-audit.md` 科学性核查（0 公式单位缺失、0 切点错判），`book_stats.py` 和 `book_check.py` 退出码都为 0。把 `stages.frontback` 改为 `done`。
