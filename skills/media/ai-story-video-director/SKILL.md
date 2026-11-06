---
name: ai-story-video-director
description: Use when directing FL2V story/animation videos with AI.
version: 1.0.0
author: 智子
license: MIT
metadata:
  source: https://x.com/eianlu/status/2118317430665613741
  hermes:
    tags: [video, seedance, minimax-h3, keyframes, storyboard, blind-qa, ffmpeg]
    related_skills: [minimax-h3-colab, video-common, stickman-omni-flash-pipeline, nutrition-short-video]
---

# AI 叙事/动画短片总导演工作流（首尾帧防漂移 + 零上下文盲审 + 代码后期）

提炼自 `@EianLu`《Claude code/Codex+Seedance AI视频：从一个想法到成片的全流程》（2026-11-05），结合本机免费生图工具（Dogbooks `gpt-image-2` / Codex）与视频生成后端（Colab G4 `MiniMax-H3` / 火山方舟 `Seedance` / Google `Flow`）。

## When to Use
- 用户要制作**多镜头叙事短片、动画故事片、或基于首尾帧（FL2V）驱动的生成式 AI 视频**。
- 在跑 `minimax-h3-colab`、`nutrition-short-video`（3D 医学 Hybrid）、`exercise-follow-along-video` 或 `stickman-omni-flash-pipeline` 时，需要**压低抽卡率、消除首尾帧背景漂移、或做提交渲染前的守门员盲审**。
- （注：纯数据/概念讲解的确定性代码动画仍走 `science-video-daily` / `dashi-animationstyle` / `xilo-opus-video`，无需走图生视频抽卡。）

## Goal
以主 Agent 为唯一总导演，通过「文字阶段拦截逻辑错 → 静态首尾帧阶段拦截构图/漂移错 → 零上下文子 Agent 盲审放行后才调用高成本视频生成 → 瑕疵优先用代码修而非重抽」，用最低的算力/API 成本和极低的抽卡率交付成片。

## Success Criteria
- **故事与分镜**：符合现实物理逻辑，一句话能说清主旨；全片平视正面 ≤ 2 次，人物头/眼落在横向 **38% 或 62%** 黄金位；分场色表经灰度图（黑白）检验前景与背景明暗分离。
- **首尾帧零漂移**：首尾帧尺寸严格一致；背景与不动道具经 `scripts/precheck_keyframes.py diff` 叠片检查无错位、无缩放漂移；局部改图经 `patch` 贴回原图确保背景像素差为 0。
- **守门员盲审通过**：每个镜头送视频渲染前，由无历史上下文的盲审子 Agent 核对【七段式提示词 + 首帧 + 尾帧 + 设定图】并签出“通过”。
- **成片交付**：经代码完成转场、色彩空间转换（Seedance 按 `BT.601` 解码、`BT.709` 交付）、720p→1080p `lanczos` 超分及首帧色彩拉回；成片盲审无穿帮硬伤。

## Constraints（总导演铁律）
1. **成本漏斗铁律**：文字改几个字 ¥0 → 生图重画 ¥0（Dogbooks `gpt-image-2` 免费 / 订阅额度）→ 视频按秒烧钱/烧 CCU（Seedance 2.5 约 ¥1.5/s、2.0 mini 约 ¥0.5/s、Colab G4 8.71 CCU/h）。**文字能发现的错绝不留到图上，图上能发现的错绝不留到视频上。**
2. **两道人工确认闸门**：用户未确认故事与分镜前，不画任何正式图；用户未确认画风样帧与设定图前，不画正式镜头首尾帧。
3. **避开 AI 视频 9 大死穴**：写分镜时直接避开「人物交叉、手拿小东西、画面带文字、镜子和倒影、左右不对称复杂特征、一镜内换光、一人连做三个动作、俯拍看不到脸、配角太多」。首选**片段式结构**（镜头间不接戏最稳）。
4. **多人反应必有先后**：每个转折按「问题 → 主角解决 → 旁人反应」三段写；严禁多人同一秒做同一动作（首帧不能摆同一姿势，提示词必须写明“A 先……过 1 秒 B 才……”）。
5. **首尾帧防漂移三件套**：
   - **倒序作画**：先画元素最全的**尾帧**，再在尾帧基础上改出**首帧**，锁死机位与透视。
   - **推镜靠代码裁切**：慢推镜头直接用代码裁切放大首帧作为尾帧，禁止让 AI 重画推近后的尾帧。
   - **局部改图强制贴回（Patch-back）**：生图模型局部编辑仍会重算全图导致背景微变（引发视频墙壁变色/杯子变大）。只改局部时，必须用 `scripts/precheck_keyframes.py patch` 把修改框羽化贴回原图。
6. **七段式提示词与正面锁死**：
   - 固定写满 7 段：`【画风】【镜头】【构图与配色】【人物】【逐秒】【声音】【约束】`。
   - **首尾静止锚点**：`0–0.2 秒：画面完全静止，与首帧一致`；`最后 0.3 秒：所有人完全停住，与尾帧一致`。
   - **禁否定句与拟人词**：写“壶嘴不出水”必出水，一律改为正面存在描述；写“卡通云”必长五官，改为物理纹理描述；方向一律写“朝画面左/右边走”。完整 20 条对照表见 `references/prompts-and-pitfalls.md`。
7. **废片先代码抢救，不盲目重拍**：
   - 开头/结尾几帧崩坏或首帧过锐（Seedance 2.5）→ FFmpeg 掐头去尾或取好帧定格延展；
   - 视频越往后越暗冷（Seedance 2.0 mini）→ 按该段首帧做色彩匹配拉回；
   - 推镜幅度不够 → 代码补数字推镜；
   - 必须重拍时，**先改首尾帧或提示词再拍**，且旧文件绝不删除覆盖（存新版本号留作混剪备选）。

## Workflow & Tooling

### Step 1：故事与零上下文盲审
- 按 `references/prompts-and-pitfalls.md` 中的 **Prompt 2** 展开逐镜头故事。
- 用 `delegate_task` 新开一个**零上下文盲审子 Agent**（只传故事文件，不传聊天记录），发送 **Prompt 3**：要求它先写出“看懂的故事是什么”，再逐镜挑逻辑和 AI 难拍项。

### Step 2：分镜表 + 38%/62% 黄金位色块与黑白对比预检
- 按 **Prompt 4** 写分镜表（全片平视正面 ≤ 2 次，每镜明确什么在动，全身/半身/特写交替）。
- 运行预检脚本生成 1920×1080 黄金比例色块草图与黑白灰度图，检查主体与背景明暗反差（`luma diff >= 35`）：
  ```bash
  /opt/homebrew/bin/python3 ~/.hermes/skills/media/ai-story-video-director/scripts/precheck_keyframes.py sketch \
    --spec '{"bg":"#0B132B","blocks":[{"label":"主角(38%)","color":"#F59E0B","rect":[0.32,0.25,0.14,0.55]}]}' \
    --out-prefix ./qa/shot01_sketch
  ```

### Step 3：设定图与首尾帧制作 + 叠片 Diff 检查
- 画师首选本机免费 Dogbooks `gpt-image-2`（`generate-and-share.py` + `/v1/images/edits`）；若用 Codex CLI 则调 `codex exec --skip-git-repo-check -s read-only -i ref.png - < prompt.txt`。
- 先画角色设定图（正/侧/表情，写死固定特征如“左手臂纹身”）→ 再画每镜**尾帧** → 从尾帧改出**首帧**。
- 局部改图贴回原图（防背景漂移）：
  ```bash
  /opt/homebrew/bin/python3 ~/.hermes/skills/media/ai-story-video-director/scripts/precheck_keyframes.py patch \
    --orig shot01_tail.png --edited shot01_head_raw.png --box 420,180,500,600 --feather 6 --out shot01_head.png
  ```
- 首尾帧叠片像素差异预检（揪出尺寸不一致或背景错位）：
  ```bash
  /opt/homebrew/bin/python3 ~/.hermes/skills/media/ai-story-video-director/scripts/precheck_keyframes.py diff \
    --first shot01_head.png --last shot01_tail.png --out ./qa/shot01_diff_overlay.png
  ```
- 按 **Prompt 5** 放大检查 8 项细节（首帧道具必须在场、多人不同姿、风向统一、缩到手机看远景）。

### Step 4：七段式视频提示词 + 守门员盲审（签“通过”才渲染）
- 按 **Prompt 6** 和 **20 大翻车对照表** 编写每镜视频提示词。
- 用 `delegate_task` 启动**守门员盲审子 Agent**（**Prompt 7**），传入提示词、首尾帧、设定图、分镜表，逐项核对通过后才提交 Colab G4 `MiniMax-H3` 或火山方舟 `Seedance`（720p 生成）。

### Step 5：代码后期与成片盲审
- 按 **Prompt 8** 用 FFmpeg/Python 完成转场、BT.601→BT.709 色彩空间标注、`lanczos` 1080p 超分与原曲拍点对齐。
- 启动**成片盲审子 Agent**（**Prompt 9**）：切点前后各抽 3 帧，先复述看懂的故事，再列穿帮硬伤，明确声明无法检查的项（动态手感、声音）。

## Stop Rules
- 预算或算力触线（Colab CCU 不足或 API 返回欠费）立即停机（`./h3.sh down`），把已有片段粗剪交付。
- 盲审子 Agent 判“不通过”时，严禁强行提交视频渲染。

## Verification
- 运行 `scripts/precheck_keyframes.py` 确认 `status: PASS`。
- `ffprobe` 核验成片分辨率、帧率、色彩空间（`bt709`）与时长。

## References & Scripts
- `references/prompts-and-pitfalls.md` — 完整 10 段导演/盲审/四线程 Prompt 模板 + 20 大翻车修辞对照表。
- `scripts/precheck_keyframes.py` — 38%/62% 黄金分割色块/灰度对比草图生成、首尾帧叠片 Diff 检测、局部重绘无损贴回工具。
