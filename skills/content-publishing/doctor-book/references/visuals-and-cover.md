# 封面与章节信息图制作规范（Visuals & Cover Design）

本指南用于阶段 12（`stages/12-package.md`）与阶段 13（`stages/13-assembly.md`）：通过编写结构化 HTML/CSS/SVG 并调用 `scripts/render_visuals.py`（Headless Chrome）生成**印刷级图书封面**（`1600×2400`）与**全彩章节机制/实操信息图**（`1400×980`），再由 `assemble.py` 与 `export.py` 自动内嵌至 `.docx` 与 `.epub`。

---

## 一、统一视觉配色体系（中信/湛庐大众医学书风格）

- **纸感暖白底色**：`#FAF8F3` ～ `#F4F1EA`（拒绝刺眼纯白背景与廉价高饱和渐变）
- **四色功能色板**：
  - 主色（深海学术蓝）：`#16324F` / `#13293D`（主标题、腰封底色、第一分类色）
  - 辅色一（临床松石绿）：`#215E59` / `#2A6F68`（安全缓解区、第二分类色）
  - 辅色二（暖阳赤陶橙）：`#C87D55` / `#B86B43`（强调线条、步骤编号、第三分类色）
  - 辅色三（沉稳岩灰蓝）：`#3B4D5E` / `#475569`（第四分类色、图注说明）
  - 警示红（红线/错误路径）：`#991B1B`（背景 `#FEF2F2`）
- **字体栈**：
  - 大标题/机制名：`font-family: "Songti SC", "STSong", "Noto Serif CJK SC", serif; font-weight: 900;`
  - 正文/标签/数据说明：`font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;`

---

## 二、封面设计规范（`10_package/cover.html` → `cover.png` & `cover.jpg`）

1. **尺寸**：固定 `1600px × 2400px`（`2:3` 标准图书封面比例）。
2. **四段式版面结构**：
   - **顶部导语区**：丛书定位标签（如“中国临床营养精准干预实践读本”）+ 英文副标 Kicker + **特大号宋刻主书名（180–210px）** + 左侧竖线强调的副标题。
   - **中央核心概念视觉区**：将全书总框架（如四型四宫格、三支柱、五步法）可视化为带 SVG 几何底纹的卡片矩阵；**若中心放置圆形靶标徽章，直径须 ≤200px，且左右相邻卡片必须留出 `≥110px` 的避让内边距（padding-left / padding-right），严禁遮挡卡片标题或右上角胶囊**。
   - **底部深色腰封区（Obi Band）**：深海蓝底色（`#13293D`）配顶部 `8px` 赤陶橙分割线；左侧放作者姓名（`white-space: nowrap`）与三甲医院/学术头衔；右侧放核心方法胶囊框。
   - **防折行硬性铁律**：腰封右侧的方法口诀（如 `测 · 配 · 练 · 评`）必须使用 `display: flex; align-items: center; white-space: nowrap;` 并将每个字包裹在独立 `<span>` 中，确保严格处在一条水平线上，绝不允许竖排掉字。

---

## 三、章节信息图设计规范（`10_package/figures/figNN.html` → `figNN.png`）

1. **数量与分布**：全书至少为 8–12 个核心章节各配 1 幅信息图（涵盖：疾病自然史/分岔口、化验单解读标尺、全书分型总图、各分型核心病理机制对比、餐盘比例与进食顺序、运动剂量与时间窗、地域/人群特色方案、90 天行动路线图）。
- **防溢出铁律**：`.top-bar` 必须使用上下两行堆叠（`display: flex; flex-direction: column; align-items: flex-start; gap: 5px;`），严禁把长标题（`.fig-title`）与长副标题（`.fig-sub`）并排放在同一水平行（1400px 宽度放不下两个长句，会导致右侧副标题超出画布被截断）；所有 Grid 容器的子卡片必须加 `min-width: 0;`。
   - 画布固定为 **`1400px × 980px`**，外层 `.canvas` 使用 `display: flex; flex-direction: column; justify-content: space-between; padding: 36px 48px;`。
   - **严禁给中间内容区（`.main` / `.quad` / `.grid3`）写死会撑破画布的固定像素高度**！中间区域一律使用 `flex: 1; align-items: stretch;`，内部卡片自适应分配高度，确保最底部的“▶ 头号动作”与 `.footer-bar` 100% 完整落在画布内，绝不被截断。
3. **防 UI 折行铁律**：
   - 所有卡片右上角的胶囊标签（`.qpill`、`.cam-tag`、`.s-days`、`.cb-step`、`.fc-tag`）和卡片主标题必须加上 **`white-space: nowrap; flex-shrink: 0;`**。
   - 胶囊标签文字控制在 **8 个汉字以内**（例如写 `50岁+ · 外瘦肌空`，不写过长句子），防止挤压左侧主标题导致胶囊变成丑陋的两行。
4. **注册清单（`10_package/figures/manifest.json`）**：
   ```json
   {
     "01": {"file": "figures/fig01.png", "caption": "图 1-1  ……"},
     "02": {"file": "figures/fig02.png", "caption": "图 2-1  ……"}
   }
   ```
   `assemble.py` 会自动读取 `manifest.json`（或按 `figures/chNN.png` 约定）将配图插入对应章节第一小节末尾。
5. **EPUB 阅读器防跨栏裁切、表格防跨页与防空白页铁律**：
   - **图片与表格整块同页（不跨栏/不跨页）**：`export.py` 生成的 `_epub.css` 已对 `figure, table, tr, th, td` 全部设置 `page-break-inside: avoid; break-inside: avoid; -webkit-column-break-inside: avoid;`，并对 `thead` 和 `h3` 设置 `break-after: avoid;`（配合紧凑字号 `0.84em`、单元格 `padding: 5px 7px` 与偶行斑马纹 `#f8fafc`），保证在 macOS/iOS Apple「图书（Books）」双栏翻页模式下整幅信息图与整张表格完整落在同一页内，绝不出现“右页底留一行表头、左页顶甩三行内容”的割裂现象；Word 导出器同样对 `≤9` 行的表格自动开启行间 `keep_with_next + keep_together` 整表锁页，并在阶段 09 写作规范中要求正文单表控制在 4–8 行。
   - **严禁在 `_epub.css` 的 `h1` 或 `h2` 上设置 `page-break-before: always`**（因为 `pandoc --split-level=2` 已按章节切分 `.xhtml`，再加 CSS 分页会产生整页空白）。
   - **卷扉页合并（`.part-banner`）**：`export.py` 的 `to_epub()` 会自动把 `# 第一部分 ...` 等卷标题合并为紧随其后章节顶部的 `.part-banner` 导读横幅卡片，防止产生只有十几个字的独立卷扉空白页。
   - **严禁未闭合 `<br>` 与空白格打卡表**：`assemble.py` 会自动将残留的 `<br>` 清洗为中文分号 `；`；所有表格严格限制在 `≤9` 行、`≤5` 列且 **0 空白单元格**（打卡模板用 `餐前 ____ ｜ 2h ____` 内联横线代替多列空单元格）；`export.py` 的 `audit_epub()` 会在导出后用 `xml.etree.ElementTree` 逐一解析全部 `.xhtml` 文件，并校验所有表格行数、列数与空单元格，任何一项违规直接阻断导出。
6. **交付物版本命名规范**：
   - 交付给用户的电子书与文档统一使用语义化版本号命名（如 `《书名》_作者_v1.0.epub`、每次迭代直接升版本号 `v1.1`、`v1.2`、`v1.3`……），**严禁使用“正式封面版 / 无空白页终版 / 精排完整版”等累赘后缀**（既保持命名干净，又能避开 Apple 图书对同文件名的缓存）。
