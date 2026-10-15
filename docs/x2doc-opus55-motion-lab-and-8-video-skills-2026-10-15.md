# Opus 5.5 Motion Lab + 8 个 Claude 做视频的 skill - X2Doc 整理

> 来源 1：https://x.com/flxrnc/status/2105311836190978392 （@flxrnc，X Article《Opus 5.5 Motion Lab: Make Claude Animate Like a Studio》，2026-09-30）
> 来源 2：https://x.com/Cryptoxorz/status/2110044544494600619 （@Cryptoxorz，8 个 skill 合集，2026-10-13）
> 来源 3：https://github.com/Vincentwei1021/video-shotcraft
> 整理时间：2026-10-15
> 来自翡冷翠

---

## TL;DR

- Motion Lab 的核心观点：形容词是模型默认审美住的地方，每换成一个数字就收回一个决定。同模型同题材，27 词 prompt 出来是"深蓝太空+光环+bloom+粒子"，448 词带数字 prompt 才可交付。
- "一条 prompt 出片"大多是假象：作者三个作品分别用了 10 / 15 / 4 条创意追问，每支约 2 小时 + 声音 45–90 分钟；业内爆款也是"5 分钟口述 + 12 小时自主"或"3 条 prompt"。
- 可直接复用的资产：八行 brief 模板（GOAL/OUTPUT/TIME/LOOK/MOTION/SHOTS/BANNED/QA）、渲染契约、缓动/弹簧/错峰/节拍数字表、"感觉→数字"翻译表、带帧号的修改指令、声音测量验收法（模型听不见，靠解码音轨测）。
- 8 个 skill 里，对我们视频矩阵最有用的是 huashu-art-motion（解说动画语法 + 出片门禁）和 dashi-animationstyle（中文口播→7 种画风，能直接进剪映）；shotcraft 专做产品宣传片，适合灵知产品/出海工具站的推广片。
- 我们的主力渲染器 xilo-opus-video 已经覆盖 render(t)、弹簧、自检打分；这次补的是"导演数字"和"声音测量"两块空白。

## 原文核心内容（Motion Lab）

### 三个实验
| 作品 | prompt 词数 | 创意追问 | 帧数 | 用时 |
|---|---|---|---|---|
| 开场：液态铬字 | 416 | 10 | 360 | ~2h + 声音 45min |
| 实验 1 模糊版（耳机） | 27 | 0（故意） | 360 | ~30min |
| 实验 1 导演版（耳机） | 448 | 15（4 轮） | 360 | ~90min + 声音 90min |
| 实验 2 3D 吉祥物五原则 | 399 | 4 | 480 | ~2h + 声音 70min，71 项数值审计全过 |

模糊 vs 导演的差别：
- "高级" → 材质：陶瓷粗糙度 0.38、清漆 0.35，铬 0.05，Claude 橙只用在一处
- "酷" → 主/补/轮廓三盏光写色值和强度，零 glow
- "现代" → fov 30、机位永不停、一次 easeOutExpo 推近
- "动画" → 120BPM、3 帧预备、弹簧阻尼 0.6，跟随件 0.5
- 默认项点名禁用：bloom、光球、霓虹、粒子、转盘、深色底、文字

### 工作原理
Opus 输出的是画像素的代码。一个 HTML 页面 + 无头浏览器逐帧冻结截图 + ffmpeg。三个好处：逐帧可复现（每个像素是 t 的纯函数）、改一个数重渲即可、模型能看接触表检查自己的作品。

渲染契约（贴在任何动效 prompt 下）：单 HTML、只用点名并锁版本的库、除字体和这些库外无网络请求、每帧是 t 的纯函数、JS 驱动则暴露 window.renderAt(t)、不用 Date.now/setTimeout/未设种子 Math.random、循环只渲 0..N-1。

### 数字表（摘要，全文见 skill 参考文件）
- 缓动：ease-out-expo (0.16,1,0.3,1) 揭示；ease-out-quint 高级入场；ease-in-out-quart 位移/镜头；ease-in-expo 快退；ease-out-back 回弹 pop。退场比入场短 40–50%。
- 弹簧阻尼比：1.0 不弹 / 0.7–0.85 高级 / 0.4–0.6 活泼 / <0.3 卡通；位置尺寸可弹，透明度颜色不弹。
- 层级：一镜一主角，次要 50–70% 行程、晚 100–200ms，环境 <5%。
- 节拍：每拍单独 n×60/BPM 取整，别累加。卡拍切，按小节换版式。
- 字停留 ≥ 0.3s/词 + 0.5s；对比度 ≥4.5:1；闪烁 ≤3 次/秒；手机上关键姿态再夸张 10–30%。

### 修改回路
渲静帧 → 看 → 写带帧号意见 → 只重渲改动部分，2–4 轮正常。每轮只贴 1–2 条。?t=2.5 冻结任意帧；每 12 帧一张接触表；洋葱皮看间距；位置曲线图看线性/死停；修不掉就渲 N-1/N+1 并排找差异。修好的问题写进契约。

### 声音
模型听不见，所以全靠测：音效峰值在画面后 1 帧；hit 比铺底高 3–6 dB；首版 80% 能量在 60Hz 以下（手机听不见）要上移；手机频段 200Hz–6kHz 单独测响度；AAC 会把真峰值从 -1.3 抬到 -0.4 dBTP，所以 WAV 限到 -2.2 dBTP；循环片 AAC 有 16ms 填充，首尾加 2ms 淡变。

### 引擎选择
10 秒内一个点子→纯 HTML；系列/模板/数据驱动→Remotion（>3 人公司需授权）；习惯网页+GSAP→HyperFrames（Apache 2.0）；3D→Three.js；产品内交互动效→Motion/GSAP。

## 关键信息与资源（8 个 skill）

| # | 名称 | 链接 | Stars（10-15） | 定位 | 对我们 |
|---|---|---|---|---|---|
| 1 | xilo-opus-video | https://github.com/Kianzzz/xilo-opus-video | 134 | 通用：三方案+预览→成片 | 已在用（主力渲染器），本地与上游同步 |
| 2 | lemo-opuscar | https://github.com/lemomo-ai/lemo-opuscar | 2.4k | 43 种影片风格图册，每种配代码样片 | 风格参考库，按需查 |
| 3 | mg-styles-15 | https://github.com/Vincentwei1021/mg-styles-15 | 884 | 15 种 MG 风格，各 10s，带完整 prompt+源码+rubric | 风格 prompt 参考（含 9:16 综艺花字） |
| 4 | dashi-animationstyle | https://github.com/chuspeeism/dashi-animationstyle | 71 | 15–60s 中文口播→7 套画风动画，带字幕，可进剪映 | 高，贴合口播短视频 |
| 5 | huashu-art-motion | https://github.com/alchaincyf/huashu-art-motion | 4.0k | 35 种艺术风格 + 9 种解说动画语法 + 出片门禁 | 高，解说语法和门禁可直接借 |
| 6 | wtt-code-animation-studio | https://github.com/WaterDJiang/Wattter_openSkills/tree/main/wattter_skills/wtt-code-animation-studio | — | 想法→剧本→分镜→源码→带声成片 | 与 xilo 重叠大，仅参考素材锁定流程 |
| 7 | video-shotcraft | https://github.com/Vincentwei1021/video-shotcraft | 12k | 产品宣传片：152 张镜头卡、Remotion、2.5D 运镜、149 个免费 SFX、剪映导出 | 中，产品推广片专用 |
| 8 | archival-doc | 原帖未给链接 | — | 找公有领域/CC 历史影像剪纪录片 | 未核实，未找到仓库 |

## 我的吸收判断

- Tier 1（已吸收）：Motion Lab 的 brief 模板、数字表、修改回路、声音测量法 → 写进 `video-common/references/motion-direction.md`，所有代码出片线共用。
- Tier 2（建议装来直接用，不改规则）：huashu-art-motion（解说语法 + `film_gate.py`/`storyboard_lint.py` 门禁，能补我们门禁漏查的"空画面/每镜同一推镜/蓝紫底"）；dashi-animationstyle（口播→画风，含丰富度检查和卡点检查图）。
- Tier 3（按场景用）：video-shotcraft（灵知产品或出海工具站要宣传片时；SFX 库免费商用可单独取用；Remotion 公司授权要注意）；lemo-opuscar / mg-styles-15 当风格 prompt 图册。
- Tier 4：wtt-code-animation-studio（与 xilo 重叠）。
- 对自媒体的价值：Motion Lab 本身就是一个"带收据的实测"选题范式——晒 prompt + 每条追问 + 用时，正对"AI 前沿实测"主轴。
- 风险：Opus 5.5 相关数据为原作者自述；几个仓库的 star 数为 2026-10-15 GitHub API 实测；Remotion 公司使用需授权。

## 可执行下一步

- [ ] 下一支片 brief 用八行模板写，混音按 -2.2 dBTP 限 WAV 后再查解码 MP4
- [ ] 决定是否安装 huashu-art-motion、dashi-animationstyle 到 ~/.agents/skills
- [ ] 选一个题材试 dashi 手绘笔记风格出一条 30 秒口播片
- [ ] "带收据"实测选题：同题材模糊 prompt vs 导演 prompt 对比，做成公众号/视频

---

*来自翡冷翠*
