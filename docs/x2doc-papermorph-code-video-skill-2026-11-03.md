# Papermorph：一本书生成互动网课、纸偶绘本、纪录片与竖屏短视频的 Agent Skill - X2Doc 整理 & 视频落地分析

> 推荐帖来源：https://x.com/DDJCXX/status/2117504549661577290 （@DDJCXX 硅基废话，2026-11-03）
> 原作者展示帖：https://x.com/DontStarve11/status/2113930836445987094 （@DontStarve11 AnotherGameDoge，2026-10-24）
> GitHub 仓库：https://github.com/DozenTwelve/Papermorph （MIT License，1,132 stars，commit `810e9bc`）
> 在线样片书架：https://papermorph.diamonddoge.org/
> 本地浅克隆路径：`/Users/marovole/Workspace/playground/Papermorph`
> 整理时间：2026-11-03
> 来自翡冷翠

---

## TL;DR

- **它是什么**：`DozenTwelve/Papermorph` 是一个面向 Claude Code / OpenCode / Codex 的 MIT 开源 Agent Skill。它以一套纯静态 SVG 舞台引擎（横屏 `1600×900` / 竖屏 `900×1600`）为底座，把一份 PDF、一个故事或一个选题做成**带配音的互动网页书**，并能用 `export.py` 按时间轴逐帧渲染导出为 **1080p MP4 + `.srt` 字幕**。
- **四种出片形态（Tiers）**：① **Lessons**（教材 PDF → 公式/图形随语音逐步推导 + 页内交互测验）；② **Picture books**（故事/童话 → 分层景片 + 纸偶角色 + 对口型 + 幼儿「听音找物」互动游戏）；③ **Documentary**（一本书/一段历史 → 公有领域版画/照片/3D地球+纸质地图 + 旁白纪录片）；④ **Shorts**（`900×1600` 竖屏，1–3 分钟讲透一个观点，亦可从长纪录片一源多剪出 4–6 条竖屏短视频）。
- **核心技术机制**：动画不靠实时录屏，而是**每个元素状态都是节拍时间 `t` 的纯函数**。先在旁白文本里插 `[[mark]]` 锚点，TTS 跑出每个词的精确时间戳 `timings.js`，画面代码用 `m('mark')` 卡词触发动作；竖屏 Shorts 默认提前 `LEAD = 0.22s` 切镜，避免「听见词才切画面」的滞后感。
- **质量与成本实盘（原作者披露）**：真正决定成片质量的不是一轮生成，而是**自动化脚本检查 + 独立强模型 Director 两轮审片（先审接触表、再审导出的 MP4）**。免费链路用 Edge TTS / 本地 Kokoro TTS + Wikimedia 公有领域图 + 程序合成音效，外部 API 成本为 $0；精配版（ElevenLabs v4 配音约 `$0.07/分钟`，两本绘本配音各 `<$0.35`；三集竖屏生图 94 张共 `$0.84`）；但多轮子代理的模型 Token 消耗较高（一章插画物理课约 `$10–18`）。
- **对我们做视频的判断**：**不建议用它替代现有的 `xilo-opus-video` / `huashu-art-motion`，而是精准借它的三块能力**：① **一源多出（长片 → 竖屏 Shorts + 网页互动版）**；② **3D 地球无缝交接纸质地图套件（`globe.js` + `map.js` + `geo.py`）与公有领域史料图自动搜集处理（`commons.py` + `prep.py`）**；③ **2 岁幼儿绘本（`picture-books` 纸偶 + `findWords` 听音点按找物，零挫败感设计）**。中文字幕对词需注意：`eleven.py` 的空格分词对齐暂不支持中日文，中文旁白必须走 `tts.py`（Edge TTS）。

---

## 一、原帖与项目背景还原

### 1.1 两条原帖内容

- **推荐帖（@DDJCXX）**：概括了项目的三类典型输入输出——「教材 PDF → 一章章带配音的互动课，公式和图跟着讲解一步步动」「童话 → 纸偶动画片，有配音、字幕、音效」「一个选题 → 7 分钟纪录片，再剪成 6 条竖屏短视频」，指出每章可导出 1080p 视频与字幕，配音可用免费方案，前置依赖为 `uv`、`ffmpeg` 和 `Playwright`。
- **原作者帖（@DontStarve11）**：展示其物理课章节（*Papermorph, part 2: physics*），强调「场景插画、角色、运镜均未用生图模型，所有动画均由 Opus 5.5 编写运动代码完成（Drop in a PDF, get a web book）」。

### 1.2 定位边界（它和 Claude Motion / Remotion 的区别）

作者在 README FAQ 中明确区分：Claude Motion 做的是单支动画解说短片；Papermorph 做的是**整本书 / 整个系列**——靠 `books/<book>/style.json` 锁定全书的配色语义、字体、配音角色、复用组件库与已批准样板章（`approved`），保证几十个章节或一个系列的短视频保持同一套视觉与叙事标准，同时交付物既是**可离线托管在任意静态站点的互动网页**，又能一键导出为**标准视频平台的 MP4 + SRT**。

---

## 二、技术架构与出片流水线深度拆解

基于本地克隆仓库（commit `810e9bc`）的 `.claude/skills/papermorph/` 源码与 30 个脚本分析，其核心工程设计如下：

### 2.1 四大内容形态（Tiers）与舞台规格

| 形态 (`tier`) | 舞台尺寸 | 核心视觉语法库 | 典型代表作（`site/` 实测） | 适用视频场景 |
|---|---|---|---|---|
| **Lessons** (`1` / `2`) | `1600×900` 横屏 | `engine.js` + `math.js` + `mathjax.js`（数轴、代数磁贴、3D平面、物理受力场景、页内评分题卡） | `linear-algebra` (40章)、`science` (9章) | 硬核知识课、《零基础AI说明书》配套互动课与横屏解说 |
| **Picture books** (`picture`) | `1600×900` 横屏 | `paper.js` + `cast.js`（多层视差纸景、四足/人形纸偶骨骼、音节口型 `mouths.py`、听音找物 `findWords`） | `little-horse`（小马过河）、`little-red-riding-hood`、`joke-collection` | 儿童双语有声互动绘本、故事/段子动画短片 |
| **Documentary** (`documentary`) | `1600×900` 横屏 | `film.js` + `map.js` + `globe.js`（公有领域版画去底染色、手绘描边 `trace.py`、Ken Burns 推镜、名言逐字打字、互动抉择） | `madness`（疯癫与文明 10min）、`pandemic`（7min）、`shooting-an-elephant` | YouTube 深度长视频、历史/商业/科技调查纪录片 |
| **Shorts** (`shorts`) | `900×1600` 竖屏 | `shorts.js` + `icons.js`（1–3秒一镜、`whip` 动态模糊横甩、`swipe` 刷视频上滑、大号浓缩字体 `word`、印章 `stamp`、滚动计数器 `counter`、群像 `swarm`） | `pandemic-shorts` (6集)、`madness-shorts` (4集) | 视频号 / 抖音 / YouTube Shorts / X 竖屏观点切片（1–3分钟） |

### 2.2 声画同步核心：「词级锚点 + 纯函数时钟 + 提前量」

这是该项目最值得做视频借鉴的底层机制：

1. **旁白内嵌触发锚点**：在 `content/<book>/chNN/narration.<lang>.json` 中，把 `[[mark]]` 直接写在要触发画面的那个词前面：
   ```json
   {
     "voice": "en-US-AndrewNeural",
     "rate": "-4%",
     "beats": {
       "hook": "This doctor [[warned]]warned about a new [[virus]]virus. [[police]]The police made him [[sign]]sign a letter calling it [[untrue]]untrue."
     }
   }
   ```
2. **TTS 生成词级时间表**：运行 `tts.py`（免费 Edge TTS 或本地 Kokoro）或 `eleven.py`（付费 ElevenLabs v4），输出每段音频 `.mp3` 及 `timings.js`（记录总时长 `dur`、每个 `[[mark]]` 对应词的起始秒数、按句切分的字幕 `cues`）。缓存按文本与声线 SHA1 索引，**挪动 `[[mark]]` 位置只需毫秒级重算时间表，不重新调 TTS 花钱**。
3. **纯函数画面编排**：画面里所有位移、缩放、改色、绘制路径都是节拍时间 `t` 的纯函数：
   - 普通横屏用 `m('warned', 0.3)` 在说出 `warned` 后 0.3 秒触发；
   - 竖屏 `shorts.js` 专门封装了 `shortsBeat`，**全局将所有 `m(k)` 提前 `LEAD = 0.22s` 触发**——因为转场动画（如 `swipe` 上滑 0.2s、`whip` 横甩 0.26s）需要时间，提前 0.22 秒启动刚好在观众听见那个词的瞬间完成切镜落定。

### 2.3 为竖屏信息流（Shorts）定制的留存与版式硬约束

作者在 `references/films/shorts.md` 中复盘了真实平台投放数据，沉淀出几条硬规则：

- **首秒留存对比实测**：一集以「已经在缓慢推近的画面 + 直接抛出核心观点」开场，**57.8%** 的观众划过首秒留了下来；另一集以「静态文字标题卡 + 铺垫废话」开场，只有 **12.8%** 留下。因此规则锁死：**第 0 帧必须是运动中的画面，第一句台词直接说结论，严禁纯文字开场卡**。
- **平台 UI 安全区（`safe.py` 自动检测）**：在 `900×1600` 舞台上，顶部 `120px`、底部 `300px` 以及右侧 `90px`（`y: 700..1300` 按钮区）会被抖音/视频号/Shorts 的标题、字幕和点赞栏遮挡。**所有屏幕文字强制约束在 `x: 50..810, y: 130..1290` 内**，`word()` 超宽会自动缩字号，`safe.py` 会在每一拍采样抓出越界文字。
- **拒绝「伪动态」死画面（`still.py` 自动检测）**：6 秒内从 `1.0` 推到 `1.08` 的微弱缩放在手机上看着跟死图一样；长镜头推镜必须 `≥ 15%` 或直接切镜。`still.py` 会扫描全片并报出画面无变化的死停区间。

### 2.4 素材与音频工程化脚本链（30 个脚本精选）

| 环节 | 脚本 | 解决什么痛点 |
|---|---|---|
| **公有领域找图** | `commons.py` | 自动搜 Wikimedia Commons，**只下 Public Domain / CC0 文件**，自动把文件名、作者、协议、来源 URL、创作年代写入 `SOURCES.tsv`（作者实测：1 个子代理 13 分钟找齐《疯癫与文明》全部 20 张历史版画并建好台账）。 |
| **图片风格统一** | `prep.py` | 将找来的杂乱图片统一烘焙为三种质感：`print`（带纸张边框与柔影的照片）、`line`（把木刻/版画的白底抽掉，黑线染成全片统一的墨色直接立在底板上）、`full`（竖屏全出血裁切），并自动生成尺寸表 `img/art.js`。 |
| **线条自绘动画** | `trace.py` | 把静态线条画转成有序笔画路径，网页里调 `traced()` 在几秒内自己画出来。 |
| **3D地球+纸质地图** | `geo.py` | 从 Natural Earth 提取国家/省份（如 `--regions CHN`）/城市河流细节，配合 NASA Black Marble 夜景贴图，在同一个 `{ lon, lat, H }` 视角下实现 **3D 地球旋转俯冲无缝交接给 2D 纸质地图**（见 `pandemic-shorts/ch01` 第 2 拍武汉开场）。 |
| **响度与配乐精修** | `level.py` / `music.py` / `sfx.py` | 旁白统一压到 `-14 LUFS`（峰值 `-1.5 dBTP`）；`music.py cut --rests --even` **自动把古典乐/生成配乐里的休止符和弱尾音剪掉**，防止配乐刚好在人声停顿处掉进静音坑，且把尾音精准卡在全片结束帧；`sfx.py` 用 numpy 纯代码合成 20+ 种免版权音效（翻书、盖章 `bang`、转场 `whoosh`、计数 `tick`、雨声等）。 |
| **逐帧确定性导出** | `export.py` | 启动最多 8 个并发无头 Chromium 实例（开启 GPU），按 `f / fps` 逐帧 seek 截图，并用 macOS 原生 `h264_videotoolbox` 硬件编码合成 1080p MP4（BT.709 色彩修正）+ `.srt` 字幕，混入人声、BGM 自动闪避（人声起压到 30%）与音效。 |
| **自动化质检门禁** | `lint.py` / `check.py` / `strip.py` / `perf.py` | `lint.py` 秒级静态检查（全局变量冲突、缺失音频/mark）；`strip.py` 生成带时间刻度与 `@o` 洋葱皮（Onion skin）的分镜接触表；`perf.py` 在 Firefox 实测帧耗时防掉帧。 |

### 2.5 多模型子代理分工与独立导演审片（`team.md` & `review.md`）

为什么它的样片质感远高于普通「一段 Prompt 让 AI 写动画」？

1. **避免长上下文腐烂与高昂重读费**：作者指出，单会话做一集绘本曾因反复重读巨大的接触表图片消耗了 **2,200 万 tokens**。因此拆成「主控 Coordinator（只看摘要和接触表，不读页面源码）+ 按步骤/按场景派发短命 Subagent」。
2. **两轮独立 Director 审片（最关键的质量杠杆）**：
   - **Round 1（接触表审片）**：派一个全新的强模型子代理，只给分镜接触表（`strip.py`）和参考样片，不给代码，专门挑「画面画的跟嘴里说的不是一回事」（例如《疯癫与文明》首轮抓出 10 个必改缺陷，一半是旁白在讲 A 人物、画面却停在 B 人物身上）。
   - **Round 2（导出 MP4 实片审片）**：导出 MP4 后，每 0.5 秒抽帧拼成接触表 + 单独放大首帧 + 用 Whisper 反跑音轨时间戳，交给另一个全新 Director 审查（《大流行》6 条竖屏在工人自检全过后，仍靠这一轮每集抓出 1–3 个声画矛盾硬伤）。

---

## 三、结合我们视频矩阵的适配度与对比分析

我们已经有一套成熟的短视频与代码动画管线（`xilo-opus-video`、`huashu-art-motion`、`dashi-animationstyle`、`grounded-explainer-script-pipeline` 以及 3D 拆解号管线）。把 Papermorph 放进我们的坐标系里对比：

### 3.1 Papermorph vs 我们现有代码视频工具链

| 维度 | 我们现有管线 (`xilo` + `huashu` + `dashi`) | `Papermorph` | 结论：谁更强 / 怎么配合 |
|---|---|---|---|
| **单条短视频出片速度** | 快（单 HTML 渲染契约 + 现成 35 种艺术画风 / 7 种口播画风） | 较重（需建 `books/`、`content/`、`site/` 三层目录与完整 kit） | 日更口播/单点科普继续用 `xilo` / `dashi`，不要每条小片都套 Papermorph 全家桶 |
| **声画卡点的精确度** | 多靠按句估算时长或手动对齐秒数 | **极强**：剧本内嵌 `[[mark]]` → TTS 导出词级秒数 → `m('mark')` + `0.22s` 提前量 | **核心借鉴点**：把 `tts.py` 的 `[[mark]]` 词级时间戳机制引入我们的代码视频管线 |
| **一源多出（长转短+网页）** | 单向出 MP4 为主 | **原生支持**：同一套素材与 `SOURCES.tsv`，既出 10 分钟横屏纪录片，又切 6 条竖屏 Shorts，还自带可交互静态网站 | 极适合 **YouTube 长视频 → 视频号/抖音/X 竖屏切片** 的主线矩阵 |
| **地理与历史/论文史料图** | 需手动找图或生图 | 自带 `commons.py`（自动搜公有领域图+建来源台账）、`prep.py`（版画去底染色）、`geo.py`（3D地球无缝切纸质地图） | 做宏观科技史、商业调查、医学史选题时的**神器** |
| **中文支持度** | 原生中文口播与字幕优化 | 引擎 UI 支持中文；但 **`eleven.py` 词对齐按空格分词，不支持中文**；默认字体（Oswald / EB Garamond）仅含拉丁字符 | 中文必须用 `tts.py`（Edge TTS 支中文字符边界）并在 `fonts.css` 显式加中文字体（如思源宋/黑） |

### 3.2 落到我们四条具体内容线的可行性评估

#### 场景 A：个人号主线（YouTube 深度长视频 + 视频号/抖音/X 竖屏切片，AI/科技/财富）—— ⭐⭐⭐⭐⭐ 极高匹配
- **怎么用**：当你做一期 7–10 分钟的 YouTube 深度选题（如某个 AI 巨头演进史、某个财富/商业机制拆解），直接用 `documentary` + `shorts` 双形态模式。
- **合规加分项**：它的 `SOURCES.tsv` + `srcTag()` 机制（画面左上角自动打灰色半透明来源角标，开发预览时隐藏，导出竖屏 MP4 时可一键开启或用 `--no-tags` 关闭）与我们的**硬性事实核查红线（片内每个数字/引语须有原文依据）**以及**个人号不带 AI 字样角标（用 `--no-tags` 导出，把声明放发布 metadata）**完全契合。

#### 场景 B：个人号《零基础AI说明书》系列 / FDE 内部培训材料 —— ⭐⭐⭐⭐ 高匹配
- **怎么用**：`Lessons` 形态可以把一份枯燥的 AI 教程 PDF 或 SOP 变成「左边动画一步步演示 Prompt/工作流变化，右边弹出小测验，底部带语音讲解」的静态网页（直接挂 Cloudflare Pages 分享给社群或公司非技术同事），同时用 `export.py` 导出成配套视频。

#### 场景 C：家里 2 岁宝宝的定制有声互动绘本（自用 + 宝爸育儿副线素材）—— ⭐⭐⭐⭐⭐ 意外之喜
- **怎么用**：仓库里的 `site/little-horse/`（小马过河）和 `site/little-red-riding-hood/` 专门针对**还不识字的低龄幼儿**设计了 `findWords`（听音找物）机制：
  - 动画播到河边自动停住，背景音乐降音量，纸偶小马眨着眼保持呼吸，语音问：「你能找到小鸟吗？摸摸它！」
  - 触控热区强制 `≥ 120×120px`（适配幼儿手指）；**点错了永远不判错**——点到牛，牛会跳一下并读出「牛（ox）」，然后温和地重问一遍「小鸟在哪儿？」；连续点错两次目标会抖动提示，三次会绕星星，20 秒没点会自动帮宝宝指出并继续播放，**零挫败感**。
  - 你可以随时把宝宝喜欢的故事或日常经历做成专属 iPad 网页绘本，还能一键导出无互动的纯动画 MP4 给宝宝看。

#### 场景 D：本机环境就绪度（已实测验证）
- 我已在你的 MBP 上核验过所有前置依赖：
  - `uv`（`0.11.21`）、`ffmpeg` / `ffprobe`（`9.0.2`，支持 `h264_videotoolbox` Apple Silicon 硬件加速编码）、`playwright` **均已安装就绪**。
  - 仓库已浅克隆至 `/Users/marovole/Workspace/playground/Papermorph`，并对其中的 `site/pandemic-shorts/ch01` 实跑了 `lint.py` 静态检查（`0 errors`）。
  - 随时执行 `python3 /Users/marovole/Workspace/playground/Papermorph/.claude/skills/papermorph/scripts/serve.py 8765 /Users/marovole/Workspace/playground/Papermorph/site` 即可在本地 `http://localhost:8765/` 体验全部 14 本成品书与短视频样片。

---

## 四、风险、局限与避坑指南（实事求是评估）

1. **Token 消耗与制作周期不低，绝非「一键秒出片」**：
   - 原作者坦承：一章带插画的物理课模型调用费约 **$10–18**（使用 Opus 5.5 / GPT-6.1-Sol / Sonnet 5.5 组合）；单会话如果不拆子代理甚至跑出过 2,200 万 tokens。
   - 原因在于它要跑「剧本 → 分镜布局静帧 → 写运动代码 → 跑无头浏览器抽帧拼接触表 → 强模型看图审片 → 返工重渲」的多轮闭环。如果只是做一条简单的 30 秒日更口播，用它会**杀鸡用牛刀**。
2. **中文本地化的三个必改项**（直接用原版模板做中文片会踩坑）：
   - **配音脚本**：`eleven.py` 依赖 `faster-whisper` 按空格切词对齐 `[[mark]]`，原文档明确标注**暂不支持中日文**；做中文视频必须用 `tts.py`（Edge TTS，如 `zh-CN-YunxiNeural` / `zh-CN-XiaoxiaoNeural`，原生支持中文字符级 `WordBoundary`）。
   - **语速与时长估算**：原版 Shorts 按英文 `2.6 词/秒` 算时长；中文口播需按 **`3.8–4.5 字/秒`** 重新核算每拍时长。
   - **字体配置**：`shorts.js` 和 `film.js` 默认锁死拉丁字体 `Oswald` 和 `EB Garamond`，且 `startShorts()` 会等待这两个字体加载。做中文片必须在 `lib/fonts.css` 和 `SANS` / `SERIF` 常量里加入中文字体回退（如 `"PingFang SC", "Noto Sans CJK SC"` 和 `"Songti SC", "Noto Serif CJK SC"`——原仓库 `pandemic-shorts/ch01` 画中文「训诫书」时就是这么处理的）。
3. **国内平台发布尺寸微调**：
   - Papermorph 的竖屏舞台是标准 `9:16`（`900×1600`，导出 `1080×1920`）。而我们的抖音/视频号主力规格有时候用 `2:3`（`1080×1620`，≤130s），如果发 `9:16` 没问题，如果要严卡 `2:3` 则需改 `engine.js` 的 `PORTRAIT` 宽高常量或导出后裁切上下黑边（由于安全区已经把文字锁在 `y: 130..1290`，上下各裁 150px 刚好不伤任何字幕！）。
4. **导出画面默认带角标**：
   - `export.py` 在导出竖屏视频时，默认会自动加上 `?tags` 参数，在画面左上角打出 `AI ILLUSTRATION` 或图片来源角标。根据我们「画面禁 AI 字样，声明放发布 metadata」的规则，**导出时务必加上 `--no-tags` 参数**。

---

## 五、如果要试：低成本验证方案（Next Actions）

不建议一上来就改写我们现有的视频 Skill，按最低成本分三步验证：

- [ ] **Step 1（5 分钟本地看样片）**：在本地启动预览服务，重点看三个标杆：`http://localhost:8765/pandemic-shorts/ch01/`（竖屏信息流叙事+地球切地图）、`http://localhost:8765/madness/ch01/`（横屏版画纪录片）、`http://localhost:8765/little-horse/ch01/`（低幼听音找物绘本）。
- [ ] **Step 2（单条竖屏 Pilot 实测）**：挑一个你近期准备发的个人号「AI + 财富/科技」选题（≤ 90 秒，约 6–8 个 beats），直接复用 `/Users/marovole/Workspace/playground/Papermorph` 仓库环境，用 `new_book.py shorts <slug> --lang zh --maps` 建一个测试目录，跑通 **Edge 中文配音 (`tts.py`) + `[[mark]]` 词级卡点 + `export.py --no-tags` 导出 1080×1920 MP4**，实测单条耗时与成片观感。
- [ ] **Step 3（能力择优吸收）**：如果 Step 2 效果满意，无需全盘照搬它的重型目录结构，只需把它的 **`tts.py`（`[[mark]]` 词级时间戳生成）**、**`shorts.js`（`LEAD = 0.22s` 提前量与竖屏安全区组件）** 以及 **`geo.py` + `map.js`（地球/地图套件）** 抽出来，合入我们现有的代码出片流水线。

---

*来自翡冷翠*
