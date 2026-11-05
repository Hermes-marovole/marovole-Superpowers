# ChrisHKAI-Video：贴一条 X 链接，生成创作者 3D 搪胶公仔自我介绍短片 - X2Doc 整理与引擎适配评估

> 来源：https://x.com/chrishkai/status/2118250441519624278
> X Article ID：`2118243955150348288`
> 开源仓库：https://github.com/ChrisHKAI/ChrisHKAI-Video （浅克隆实测 commit：`15b66ee613e621f82ba781d27547a67e76c55f50`）
> 作者：Chris (@ChrisHKAI)
> 发布时间：2026-11-05 (UTC)
> 整理时间：2026-11-06
> 来自翡冷翠

---

## TL;DR

- **纯代码 + Blender Cycles 3D 个人介绍片引擎**：`ChrisHKAI-Video`（核心 Skill 为 `creator-toy-intro`）接收一条创作者 X 主页链接，零图生视频 API、零素材库，全靠代码将创作者头像鼓起成 3D 搪胶公仔（Vinyl Toy），把代表作帖子立成 3D 墙面、让真实数据从页面原位升起，并用 Python 合成配乐（内置 `lemo-opuscar` MIT 采样器），最终通过 Blender Cycles 渲染出默认 30 秒的 3D 短片。
- **两道本地 Web Studio 交互式审批门（Human-in-the-Loop）**：
  1. **故事页（Story Page）**：在动 3D 之前，先调研创作者最自豪的证据与数字，给出 A/B/C 三条故事主线（含开场方案、分镜草图与结尾道具）供用户挑选。
  2. **分镜页（Storyboard Page）**：用 EEVEE 渲染带配乐的 1/3 分辨率粗剪动画（Animatic）+ 16 张半分辨率真 3D 预览帧，支持**直接在画面坐标上点击留言（写入 `comments.jsonl`）**，通过全部自动化门禁且用户签字（OK）后才启动耗时 1–1.5 小时的 Cycles 正式渲染。
- **硬核工程化自检门禁（Before-Blender Gates）**：内置 `check`、`pace`、`clearance`、`palette`、`ledger`、`compare` 六大脚本——在正式渲染前自动拦截：**前 3 秒无重拍钩子、超过 2 小节（4 秒）无新事件、公仔小于画面高度 8%、文字停留不够阅读时长（中文 4.5 字/秒 + 1.5s）、公仔与文字色差低于 3:1、3D 穿模（`clearance.mjs` 逐帧碰撞检测）、以及与历史成片雷同（`ledger.py` 要求 6 个维度中至少 4 项不同）**。
- **本机环境实测（M2 Max 64GB）**：仓库浅克隆至 `/Users/marovole/Workspace/playground/ChrisHKAI-Video`（commit `15b66ee`），运行 `doctor.mjs` 实测：**Node v22.22.3、Blender 5.2.1、FFmpeg 9.0.2、Chrome、Apple M2 Max (38-core Metal GPU)、134 款中文字体全部就绪**（仅需 `doctor.mjs --install` 自动配置约 150MB 独立 Python venv）；离线测试集 **36/36 Node 故事方向测试 + 6/6 Blender 公仔部件碰撞测试 + 11/11 GPU 设备选择测试 + 7/7 Codex 安装测试全部 `0 errors` 通过**。
- **对我们现有产线的取舍结论（借件不换栈）**：它专注于「创作者/产品里程碑 3D 搪胶公仔宣传片（单条耗时数小时 + 高額 Opus 5.5 Token + 1.5h Cycles 渲染）」，**不能也不应替代**我们现有的日更科普/知识短视频管线（`xilo-opus-video` / `huashu-art-motion` / `papermorph-book-film`）；但极其适合用来为**个人号（`@marovole`）或开源仓库破万 Star 节点制作置顶个人介绍片**，且其 **6 项渲染前自动化门禁**可直接抽取出片管线复用。

---

## 一、原帖核心内容

### 1. 初衷与两大原则
很多人会做个人网站介绍自己，但很少有人做个人介绍视频。作者 Chris（@ChrisHKAI）在 Claude Opus 5.5 发布后为“蜗牛King”制作了一条 3D 搪胶公仔个人短片，反响极好，遂历时两周将其提炼为开源 Claude Code / Codex Skill：`ChrisHKAI-Video`。

- **原则一：片子是创作者自己的，不是套模板的**
  - 头像、帖子、数字全部取自创作者真实主页（数字注明抓取来源与日期，绝不硬编转折），舞台强调色直接从创作者头像与封面图中提取。
- **原则二：每一步都停在看得见的东西上，点头才往下走**
  - 故事页 → 公仔转身图 → 分镜页（带粗剪视频与自检报告） → 正式渲染，任何一步未确认绝不空跑几个小时的 Cycles 渲染。

### 2. 从安装到成片的 5 步工作流

#### 第 0 步：安装与环境自检（`doctor.mjs`）
支持作为 Claude Code Plugin 安装，也支持通过 `scripts/install-codex.py` 安装到 Codex：
```bash
# Claude Code 插件安装
claude plugin marketplace add https://github.com/ChrisHKAI/ChrisHKAI-Video.git
claude plugin install chrishkai-video@chrishkai-video

# 或本地克隆后安装
git clone --depth 1 https://github.com/ChrisHKAI/ChrisHKAI-Video.git
```
首次运行自动检查 `Blender 5.2+`、`Node 22+`、`Python 3.9+`、`ffmpeg` 与 `headless Chrome`。

#### 第 1 步：贴链接建工作区
直接输入 `帮我做一条自我介绍片：https://x.com/yourhandle` 或运行 `/chrishkai-video:creator-toy-intro`。
开局只问画幅：**16:9（X 电脑版主页，推荐）** 或 **9:16（X / 抖音 / 小红书 / 视频号 / IG 手机版主页）**，并在当前目录创建 `<handle>-intro/` 独立工作区。

#### 第 2 步：调研并生成本地「故事页（Story Page）」
- Claude 抓取创作者代表作、高赞帖与里程碑数字（若装了 Grok Build 会询问是否用 Grok 搜 X，未装则直接用无头浏览器抓取，不啰嗦）。
- 启动本地 Web 服务展示**故事页**（或导出长图 `materials.png`），包含三部分：
  1. **① 主线（A / B / C 三条完整叙事方案，带「推荐」标记）**：每张卡片写明“核心人物是谁”、“一句话主旨”、“第一帧画面与大字”、“每段素材对应的代码动画草图（Sketch）”以及“还缺哪些证据”。
  2. **② 开场（三选一，带预览图）**：如主页浮空头像撕下鼓成公仔、主页平躺立起等。
  3. **③ 收尾（三选一或自定义）**：公仔骑在专属道具上（如蜗牛、金色 GitHub Star、雕塑底座），撕纸条打出 Slogan。
- 用户只需回复一句：`【主线 A、开场 2、收尾 1】`，或直接在本地网页卡片上打字留言。

#### 第 3 步：生成 3D 搪胶公仔（`lookdev`）
- 严格按照原图身体结构建模（人、动物、物品均可，“柠檬就是柠檬，绝不会硬长出手脚”）。
- 内置三套建模方案：**零件表（Parts Kit）**、**宠物套件（Pet Kit）**、**SDF 雕塑套件（Sculpt Kit，`sdf.py`）**。
- 自动跑 `toyparts.py` 检查部件是否悬空、内陷或重叠，并在深色舞台上渲染一张多角度转身图（Turnaround）供用户确认。

#### 第 4 步：签分镜——本地「分镜页（Storyboard Studio）」与自检门禁
正式渲染前的最后一道闸门。本地网页从上到下展示：
- **故事表**：每段秒数、发生什么、观众收获什么、使用哪份真实素材。
- **节拍格（Beat Grid）**：每格一拍，粗线为小节首拍，红线为重拍（Downbeat）。
- **16 格真 3D 预览画面**：50% 分辨率、低采样真实渲染图（非手绘草图）。
- **粗剪动画（Animatic）**：EEVEE 渲染的全片草稿 + Python 自动谱写的配乐（页面明确标注地板光斑是 EEVEE 草稿伪影，Cycles 成片不会有）。
- **画面定点批注**：点击任意预览格或暂停的粗剪画面，直接在坐标位置写修改意见（存入 `build/comments.jsonl`），改哪格只重渲哪几格。
- **6 种声音试听**：`bed`（默认，音效+轻和弦）、`song`（合成曲）、`band`（真实乐器采样）、`strings`（真实弦乐+钢琴，需约 1.4GB 采样库）、`fx`（纯音效）、`own`（创作者自备歌曲卡点）。
- **「我自己检查咗」（Claude 自动预检清单）**：
  - 节奏无冷场（头 3 秒有重拍钩子，每两小节 4 秒内必有新事件）；
  - 阅读时长充足（5 段文字均停够阅读时间）；
  - 不穿模（`clearance.mjs` 逐帧检查公仔不穿墙、字条不穿公仔）；
  - 色彩对比度告警（例如截图实测抓出：`8 件字用 #F2C14E，同公仔自己嘅颜色 #F6C814 太近：企埋一齐会溶做一旧，换一只颜色`）；
  - 防模板雷同（`ledger.py` 比对历史成片：开场、结构、招牌动作、配色、声音、结尾 6 项中至少 4 项不同，例如截图显示 `同之前 3 条片都够唔同（最似 蜗牛King：5 样唔同）`）。
- **「开工前要你拍板」5 项确认**：故事与画面、数字升起方式、结尾口号、招牌动作、出街平台与画幅。用户回复 `OK` 后才启动 Cycles。

#### 第 5 步：样本试渲与 Cycles 正式渲染
- 先用最终画质试渲最难的几秒（`run.mjs sample`），确认动态与音乐卡点无误后再全片渲染。
- Apple Silicon (M4 Pro / M5) 下 Cycles 后台渲染约需 **1–1.5 小时**，单条片占用约 **10 GB** 磁盘空间。
- 完成后自动输出：**成片 MP4（峰值锁在 -1 dBTP 内、-13 LUFS）**、**纯音效版（Effects-only cut）**、**各平台安全区裁剪封面（`out/covers/`）**、**最后一轮独立盲审报告（`qa.txt`）** 与 **开源采样署名文件（`credits.txt`）**。

---

## 二、仓库实测与外部引擎适配评估（External Engine Fit）

按照 `x2doc` 外部引擎评估规范，已在本地只读浅克隆并执行工具链与测试集验证。

### 1. 本机实测结果（Commit `15b66ee613e6`）

- **克隆路径**：`/Users/marovole/Workspace/playground/ChrisHKAI-Video`
- **`doctor.mjs` 硬件与依赖扫描输出**：
  - `computer`: `darwin arm64` ✓
  - `Node.js 22+`: `v22.22.3` ✓
  - `Blender 5.2+`: `5.2.1 (/Applications/Blender.app/Contents/MacOS/Blender)` ✓
  - `GPU for Cycles`: `Apple M2 Max (GPU - 38 cores) (Metal)` ✓
  - `ffmpeg + ffprobe`: `9.0.2` ✓
  - `headless Chrome`: `/Applications/Google Chrome.app` ✓
  - `faces with Chinese`: 检测到本机 **53 个字体家族共 134 款中文字体** ✓
  - `free space`: `1417 GB free`（单条片需约 10 GB）✓
  - `Python modules`: 仅需在首次制片时运行 `node skills/creator-toy-intro/engine/scripts/doctor.mjs --install` 在该 Skill 私有 venv 中安装约 150MB 依赖（`numpy, scipy, pillow, fonttools, contourpy, scikit-image`），不污染全局环境。
- **门禁与单测实跑（全部 `0 errors`）**：
  - `node --test tests/story-directions.test.mjs`：**36 / 36 passed**（覆盖证据溯源、引号原文逐字核对、赞助置顶帖过滤、三语故事页转义、盲审门禁失效重算）。
  - `python3 tests/toy-parts.test.py`：**6 / 6 passed**（测试 Blender 内眼球悬空 4mm 报警、内部隐藏球体报警、异色重叠报警）。
  - `python3 tests/render-device.test.py`：**11 / 11 passed**（OptiX > CUDA > HIP > oneAPI > Metal 优先级）。
  - `python3 tests/install-codex.test.py`：**7 / 7 passed**。

---

### 2. 形态映射表（能做哪类片 → 对应我们哪条线）

| 形态 | 画布与规格 | 视觉语法 | 官方样片 | 我们的用途 |
|---|---|---|---|---|
| **X 桌面端创作者介绍片** (`x-desktop`) | `1920×1080` (16:9), 30fps, 默认 30s | 暗色 3D 舞台 + 网页浮空立起 + 头像撕纸鼓成 3D 搪胶公仔 + 高赞帖立墙 + 数字跳表 + 结尾骑道具撕纸 Slogan | 蜗牛King (`@isnail`, 30s)、铁柱AGI (`@cgnot996`, 42s)、Lemomo (`@lemomo_ai`, 32s)、Kin (`@KinGao476942`, 30s) | **个人号 (`@marovole` / YouTube 频道片头 / GitHub 个人主页)** 的置顶自我介绍片；或 `marovole-Superpowers` 等开源项目里程碑纪念片 |
| **移动端平台主页介绍片** (`x-mobile`, `douyin-mobile`, `xhs-mobile`, `channels-mobile`, `ig-mobile`) | `1080×1920` (9:16), 30fps, 默认 30s | 对应 App 原生主页 UI 布局（含抖音/小红书/视频号点赞与收藏格）+ 3D 公仔破屏而出 | 仓库 `themes/` 已内置 6 套平台布局，分阶段开放发布预设 | **视频号 / 抖音 / 小红书** 账号置顶“新粉 30 秒认识我”名片视频 |
| **品牌 / 产品片尾标识** (Outro / Bumper) | `1920×1080` 或 `1080×1920`, ~15–23s | 独立雕塑公仔 + 品牌 Slogan 撕纸定格 | Chris HKAI 片尾标识 (23s) | 长视频（YouTube AI 实测 / 拆解片）固定品牌片尾 |

---

### 3. 与我们现有视频栈的取舍对比表

| 维度 | 我们现有主力栈 (`xilo-opus-video` / `huashu-art-motion` / `papermorph` / `blender-3d-scene-video`) | `ChrisHKAI-Video` (`creator-toy-intro`) | 结论：谁强 · 怎么配合 |
|---|---|---|---|
| **定位与题材** | 通用科普、知识解说、书稿拆解、商业调查、Vibe 知识大赏（高频量产） | **专精单一题材**：创作者/产品主页 3D 搪胶公仔自我介绍片 | **严禁拿它替代日常日更管线**；仅在制作“账号置顶名片 / 里程碑宣传片”时专案调用 |
| **单条出片速度** | Web Canvas / SVG / 轻量代码渲染：几分钟到半小时出片，适合日更 3 条 | 重度精品慢工：多轮交互审批 + Blender Cycles 渲染 **1.5–3 小时/条** | 日更继续用现有轻量栈；季度级置顶名片用 `ChrisHKAI-Video` |
| **3D 材质与灯光工艺** | `blender-3d-scene-video` 偏通用几何/拆解场景 | 专精 **PBR Neutral 搪胶（Vinyl Toy）材质、SDF 雕塑、撕纸贴图与暗色舞台布光（`look.py`）** | **它强**：其 `look.py` 舞台灯光参数与 `toyblend.py` 搪胶材质可直接借入我们的 `blender-3d-scene-video` |
| **渲染前自动化质检（QA Gates）** | 依赖 `video-common` 事实台账与人工/子代理抽帧审片 | **极强**：渲染前纯数学/几何静态检查（`pace.py` 节奏与字速、`clearance.mjs` 3D 穿模、`colors.py` 3:1 色差 + 手机尺寸 OCR 回读、`ledger.py` 防同质化） | **最值得借鉴的部分**：把它的 6 项静态检查思想移植到我们现有的代码视频管线 |
| **人机协作审片体验** | 生成图片接触表（Contact Sheet）或直接导出 MP4 在对话里反馈 | 本地起 `studio` Web 服务，浏览器里看 EEVEE 粗剪 + **直接点画面坐标写批注（`comments.jsonl`）**，按帧增量重渲 | 做复杂长片或高优精品片时，可复用其 `studio` + `comments.jsonl` 定点批注模式 |

---

### 4. 中文与多平台落地注意点

1. **画幅差异**：该引擎竖屏原生为 `9:16 (1080×1920)`，而我们抖音/视频号日常科普标准为 `2:3 (1080×1620)`。若用它做视频号/抖音置顶名片，可直接使用其 `channels-mobile` / `douyin-mobile` 的 9:16 主题（因其自带 `safezone` 平台控件遮挡检查器，已避开顶部 120px、底部与右侧按钮区）。
2. **中文字体与 OCR 回读**：引擎不捆绑字体，而是调用 `fonts.py` 扫描本机支持目标繁/简汉字的字体并生成 `typesheet`，再用 macOS Vision (`read-text.swift`) 在手机缩略图尺寸下做 OCR 回读校验，确保笔画不糊成一团。本机已检出 134 款中文字体，开箱即用。
3. **事实核查红线天然对齐**：该 Skill 强制要求 `facts.json` 中每个数字注明抓取位置与日期，且對置顶推广帖（Paid Partnership）自动过滤不入片，并用单元测试强制校验 `「」` 内的引语必须与抓取原文逐字一致——这与我们的 `content-grounding` 硬性红线完全同构。

---

### 5. 三栏成本核算（作者披露 + 本机实测）

| 成本维度 | 费用 / 消耗明细 | 说明 |
|---|---|---|
| **1. 外部付费 API（生图 / 视频 / TTS）** | **$0** | 零图生视频 API、零生图 API、零付费 TTS（画面 100% Blender 渲染，音乐由本地 Python + 开源采样库合成；Grok Search 为可选项，不装则直接走本地无头 Chrome 免费抓取） |
| **2. 本地算力与存储** | **免费（耗时 1.5–2 小时 + ~10 GB 磁盘/片）** | 本机 M2 Max (38 核 Metal GPU) 跑 EEVEE 粗剪约数分钟，Cycles 正式渲染（48 samples, 1080p, 30fps, 30s = 900 帧）约需 **1–1.5 小时**；若启用 `strings`/`band` 真实乐器需一次性下载约 **1.4 GB** MIT 采样包 |
| **3. LLM Token 消耗（真正大头）** | **高（作者明确提示“很耗 token”，强依赖 Claude Opus 5.5 high/xhigh）** | 单片需经历：多源网页调研 → 3 套故事方向与代码草图生成 → 3D 公仔部件/SDF 建模调试 → 专属分镜动画与配乐代码编写 → 多帧视觉对比（`compare.jpg`）与独立子代理盲审（`review.md`）。按 Opus 5.5 high 估算，完整跑通一条定制片约消耗数百万至千万级输入缓存 Token |

---

## 三、最值得我们直接借用的 5 个工程机制

哪怕不跑它的 Blender 搪胶公仔全流程，以下 5 个机制在代码设计上非常精妙，可直接吸收进我们的视频管线：

1. **零渲染成本的 `pace.py` 节奏与阅读速度静态检查**：
   - 在还没有渲染任何一帧画面前，直接读取动画时间轴 JSON（`build/anim.json` 与 `build/reads.json`），硬编码拦截：
     - **前 3 秒无重拍视觉钩子（No hit in first 3s）**；
     - **超过 2 小节（4 秒）无新视觉事件（死画面）**；
     - **主角占比过小（小于画面高度 8%）或出画**；
     - **字幕闪太快读不完**：按 **中文 4.5 字/秒、英文 3 词/秒 + 1.5 秒缓冲** 计算最低停留时长。
2. **手机缩略图尺寸 + 辉光（Bloom）模拟下的 macOS 原生 OCR 可读性检查（`reading.py` + `read-text.swift`）**：
   - 很多大字在 1080p 下看很清楚，但加了后期辉光并缩到手机屏幕大小后笔画粘连或与公仔撞色。它把预览帧缩到手机尺寸并调用 macOS 原生 Vision 框架做 OCR 识别，认不出字或对比度 `< 3:1`（如黄字 `#F2C14E` 撞上黄柠檬公仔 `#F6C814`）直接报错拦截。
3. **跨历史成片的防同质化账本（`ledger.py`）**：
   - 把每条已交付成片的 6 个结构特征（开场方式、段落结构、招牌动作、主色调、配乐风格、结尾道具）记入 `~/.chrishkai-video/ledger.json`。新片开拍前自动比对，**必须与所有历史成片在 6 项中有至少 4 项不同**，从机制上杜绝“套模板批量生产一模一样的片子”。
4. **与黄金标杆帧的并排像素级量化比对（`compare` + `quality.md`）**：
   - 将已获批的 3 条标杆成片（蜗牛King、Kin、铁柱AGI）的 5 个关键时刻（开场、公仔登场、数据证明、高潮、尾卡）存在 `references/look/`，并测出黄金区间（暗部舞台亮度 `48–76`、对比度 `33–88`、色彩丰富度 `27–48`、主角高度占比 `45%–70%`、数字大字占比 `15%–25%`）。新片自动拼成 `build/compare.jpg` 逐行对比，超标自动打印帧号。
5. **两阶段分层渲染 + 定点坐标批注（`EEVEE 33% Animatic` → `Web Studio Click-to-Comment` → `Cycles 100% 增量重渲`）**：
   - 彻底解决 Blender 渲染慢与反复返工的矛盾：先用几分钟的 EEVEE 粗剪 + 16 张半尺寸静帧让用户在网页上点选坐标批注，改定后再跑 `run.mjs sample`（只用最终画质渲最难的几秒），最后才全量跑 Cycles。

---

## 四、关键信息与资源

| Type | Name | Link | Why it matters |
|---|---|---|---|
| X Article | ChrisHKAI-Video 上线：贴一条 X 链接，做出主角是他自己的 3D 搪胶公仔短片 | https://x.com/chrishkai/status/2118250441519624278 | 原帖全文，详解 5 步交互式制片流程与故事页/分镜页设计 |
| GitHub Repo | `ChrisHKAI/ChrisHKAI-Video` | https://github.com/ChrisHKAI/ChrisHKAI-Video | MIT 开源仓库（本地已浅克隆至 `~/Workspace/playground/ChrisHKAI-Video`，commit `15b66ee`） |
| Showcase Releases | 5 条已交付成片合集（GitHub Releases） | https://github.com/ChrisHKAI/ChrisHKAI-Video/releases/tag/films | 含铁柱AGI (0:42)、蜗牛King (0:30)、Kin (0:30)、Lemomo (0:32) 及片尾标识真片 |
| Audio Dependency | `lemomo-ai/lemo-opuscar` | https://github.com/lemomo-ai/lemo-opuscar | 仓库 `engine/vendor/lemo/` 内置的 MIT 真实乐器采样器与音效合成模块 |
| Related X Posts | 作者历史方法论文章（18天开通收益 / 演讲力 / 涨粉复盘） | https://x.com/ChrisHKAI/status/2117612889205072073 | 原帖末尾附带的创作者个人增长复盘链接 |

---

## 五、三步低成本验证与可执行下一步

> **总体策略**：不改动我们现有的日常短视频 Skill；先将该仓库作为独立沙盒工具保留在 `~/Workspace/playground/ChrisHKAI-Video`，按以下三步验证并抽取其质检机制：

- [ ] **Step 1（3 分钟看样片与本地架构）**：已浅克隆至 `/Users/marovole/Workspace/playground/ChrisHKAI-Video` 并通过全部 60 项离线单测；可随时打开 https://github.com/ChrisHKAI/ChrisHKAI-Video/releases/tag/films 观看 4 条 30s 标杆成片。
- [ ] **Step 2（单条 Pilot 实测——做一条自己的置顶介绍片）**：若后续想为个人 X 账号或 GitHub `marovole-Superpowers` 做一条 30 秒 3D 置顶介绍片，先执行一次 `node /Users/marovole/Workspace/playground/ChrisHKAI-Video/skills/creator-toy-intro/engine/scripts/doctor.mjs --install` 装齐私有 venv，然后只跑到 **Step 4 分镜页 + EEVEE 粗剪动画**（耗时约 15–20 分钟，不跑 1.5 小时的 Cycles），验证故事页与分镜页体验。
- [ ] **Step 3（抽 3 个质检机制合入现有管线）**：将 `pace.py`（中文 4.5 字/秒 + 1.5s 阅读时长与前 3s 钩子检查）、`colors.py` + `reading.py`（3:1 对比度与缩略图 OCR 回读）、以及 `quality.md`（与已获批标杆帧自动并排生成 `compare.jpg`）抽取为 `video-common` 的通用导出前自检脚本。

---

*来自翡冷翠*
