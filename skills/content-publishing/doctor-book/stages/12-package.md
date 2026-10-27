# 阶段 12：package 选题策划书、营销文案、图书封面与章节信息图

目标：写出版社投稿用的选题策划书与营销文案，选定样章，并基于已通过医学科学性审计的定稿文字制作印刷级图书封面与 8–12 幅全彩章节信息图。

**前置检查（硬门槛）**：进入本阶段绘制封面和章节信息图之前，必须确认阶段 10 的 `08_reviews/scientific_audit.md` 与阶段 11 的后置附录科学性核查已全部完成且 `06_evidence/evidence_bank.md` 已修正——**严禁在未完成科学性审计的情况下提前画图**（避免图内切点、HR、百分比或机制词错误导致整批图片返工）。

先读：`references/proposal-template.md`、`references/visuals-and-cover.md`、`03_positioning/positioning.md`、`04_market/competitors.md`、`05_architecture/outline.md`、`01_materials/material_bank.md` 中的 B 条目。

## 步骤

1. 按模板写 `10_package/proposal.md`，所有栏目都要填写。图表数量按书稿实际情况写：表格数按正文统计，插图数按实际制作的章节信息图数量填写。作者平台数据、门诊量、获奖等必须来自 B 条目，否则写 `【待核实】`。
2. 选样章：第 1 章，加上第三部分里最具代表性、lint 指标最好的一章。写入 `state.json` 的 `sample_chapters`，例如 `["01", "09"]`。
3. 写 `10_package/marketing.md`：封底文案（200 字以内）、腰封文案（30 字以内，3 个备选）、内容简介（300 字）、一句话推荐语、推荐人邀请名单（只写类型，例如"同领域三甲医院主任医师"，不编造人名）。
4. 对 `proposal.md` 和 `marketing.md` 做合规自查：按 `references/compliance-cn.md` 的红线逐条检查，营销文案最容易越线。
5. **制作图书封面与章节信息图（必做，严格遵循 `references/visuals-and-cover.md`）**：
   - 编写 `10_package/cover.html`（`1600×2400` 暖米白纸感 + 四色功能色板 + 中央核心框架图 + 底部深海蓝腰封；注意中心徽章避让卡片文字 `padding ≥110px`，腰封右侧方法口诀加 `white-space: nowrap` 保持严格水平一线）。
   - 在 `10_package/figures/` 下为 8–12 个核心章节编写信息图 HTML（`fig01.html`…，`1400×980` 画布；中间容器用 `flex: 1` 自适应高度严禁写死超限高度防底部裁切；所有右上角胶囊标签加 `white-space: nowrap; flex-shrink: 0;` 且文字 ≤8 字防折行），并生成 `10_package/figures/manifest.json` 映射各章图号与图注。
   - 运行 `python3 SKILL_DIR/scripts/render_visuals.py <项目目录>`，用 Headless Chrome 一次性渲染出 `10_package/cover.png`、`cover.jpg` 与 `10_package/figures/*.png`。

## 完成标准

`proposal.md` 所有栏目已填，`sample_chapters` 已写入，`marketing.md` 已写并通过合规自查，`cover.jpg` 与 `figures/*.png`（及 `manifest.json`）已渲染生成且无文字折行或底部裁切。把 `stages.package` 改为 `done`。
