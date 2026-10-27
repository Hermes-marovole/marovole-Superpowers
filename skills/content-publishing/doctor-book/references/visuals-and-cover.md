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
2. **画布尺寸与防裁切铁律（极重要）**：
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
5. **EPUB 阅读器防跨栏裁切 CSS**：
   `export.py` 生成的 `_epub.css` 已内置 `figure { break-inside: avoid; -webkit-column-break-inside: avoid; }` 与 `figure img { max-height: 76vh; width: auto; object-fit: contain; }`，保证在 macOS/iOS Apple「图书（Books）」双栏翻页模式下整图与图注完整同屏显示。
