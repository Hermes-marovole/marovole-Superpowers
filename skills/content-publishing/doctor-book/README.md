# doctor-book (`Neuma-Inc/doctor-book-skill`)

全自动为中国临床医生撰写 **8–12 万字叙事框架型大众健康科普书** 的 Agent Skill（兼容 Hermes Agent / Factory Droid / Claude Code）。

从公开/私域素材入库、医生文风克隆、核心概念与分型框架搭建、循证医学证据核验、八拍章节简报、逐章写作与合规 Lint、三幕一致性审稿，到 **16 开出版级 Word（`.docx`）精排**、**印刷级封面（`1600×2400`）与全彩章节信息图（`1400×980`）自动渲染**、**Apple Books 防裁切/防跨页 EPUB（`.epub`）导出** 及 **出版社标准投稿包（`.zip`）** 的 13 阶段全闭环流水线。

---

## 目录结构

| 路径 | 说明 |
|---|---|
| `SKILL.md` | 技能主入口与 13 阶段状态机总控规范 |
| `stages/01-intake.md` – `13-assembly.md` | 13 个阶段的逐步执行手册、子代理 Prompt 与完成门禁 |
| `references/architecture.md` | 三幕结构（15% / 35% / 50%）、六种章型、概念复现与首尾闭环 |
| `references/chapter-template.md` | 八拍章节主模板（冷开场→命题转向→背景→机制→证据→案例回收→行动→交接） |
| `references/compliance-cn.md` | 国内医疗科普出版合规红线（禁绝逆转/根治/停药承诺、相对风险配绝对风险、恐惧词 400 字内给行动出口、CGM 适应证边界等） |
| `references/voice-style.md` | 医生口吻量化指标与去 AI 腔规则 |
| `references/visuals-and-cover.md` | 图书封面（1600×2400）与章节信息图（1400×980）HTML/SVG 渲染、防折行/防裁切及 EPUB/Word 表格防跨页规范 |
| `references/patterns/` | 8 类写作模式卡片库（开篇、解释、病例、证据、说服、章尾工具、标题、前言结语） |
| `references/atlas/` | 标杆医学科普书拆解（《超越百岁 Outlive》《好能量 Good Energy》《营养圣经》） |
| `scripts/init_project.py` | 初始化新书工程目录与 `state.json` |
| `scripts/lint_chapter.py` | 单章硬门禁检查（合规红线、真实病例溯源、相对风险换算、药物剂量防护、文风指标） |
| `scripts/book_check.py` / `book_stats.py` | 全书结构、三幕比例、免责声明、概念跨章复现与字数预算校验 |
| `scripts/render_visuals.py` | 调用 Headless Chrome 将 `cover.html` 与 `figures/*.html` 批量渲染为高清封面与章节配图 |
| `scripts/assemble.py` | 组装 `book.md`（自动将 `[E0xx]` 单/多文献引文转为上标 `^[1,2]^`、自动注入章节信息图、自动降级前言/附录内部小标题防碎片切页） |
| `scripts/export.py` | 导出 16 开出版级 `book.docx`、带封面与防跨栏裁切/表格防跨页的 `book.epub`（内置 `audit_epub()` 门禁）及 `投稿包.zip` |
| `scripts/audit_book.py` | 全书端到端 Debug 与质量审计门禁（扫描 `book.md`、封面/插图尺寸与防折行、EPUB 严格 XML 解析、残页/空白页、`[E0xx]` 泄露、表格行列几何与空单元格、Word 16 开 DOM） |
| `scripts/selftest.py` | `lint_chapter.py` 的 12 项回归自测套件 |

---

## 快速安装

```bash
git clone https://github.com/Neuma-Inc/doctor-book-skill.git
ln -s "$PWD/doctor-book-skill" ~/.hermes/skills/doctor-book
ln -s "$PWD/doctor-book-skill" ~/.factory/skills/doctor-book
```

**运行环境依赖**：
- `python3`（建议安装 `python-docx` 以启用 16 开出版级三线表、斑马纹、金句框与书眉页码精排）
- `pandoc`（`brew install pandoc`）
- `Google Chrome`（用于 `render_visuals.py` 渲染封面与章节信息图）

## 自检

```bash
python3 scripts/selftest.py
```
