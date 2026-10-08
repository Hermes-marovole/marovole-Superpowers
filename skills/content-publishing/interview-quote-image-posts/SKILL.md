---
name: interview-quote-image-posts
description: "Use when making 字幕长图 posts from English interviews. Source→render→review→publish→data loop."
version: 2.0.0
author: 智子
license: MIT
metadata:
  hermes:
    tags: [字幕长图, xiaohongshu, douyin, wechat, 图文, interview, yt-dlp]
    related_skills: [native-subtitle-quote-image, cn-social-image-post-publishing, creator-channel-analytics, ego-browser, content-grounding]
---

# 外文访谈 → 中文字幕长图帖（选题 → 出图 → 审核 → 发布 → 看数据）

用户要把英文访谈或演讲（名人、科学家、健康专家）做成「真人画面 + 中文字幕条」的 3:4 长图，发小红书、抖音图文和公众号贴图时用。
渲染交给 `native-subtitle-quote-image` 的脚本字幕模式（`render-script`）。本 skill 管渲染前后的所有环节和本机约定。

## Goal
从一条公开访谈里切出同一主题的 2–3 张字幕长图，组成一篇帖子。中文要逐句对得回英文原文。审核通过后发布，之后回后台看数据，决定下一批做什么。

## Success
- 一篇帖子是 2–3 张同主题的图，不要一张图发一篇。每张图讲一个观点，用 5–7 句连贯原话。
- 每句中文都能对到 `analysis/transcript.txt` 同一时间段的英文。文案里的每个事实都能在原文里找到。
- 每张图的第一帧是讲者正脸特写。没有黑条、没有切脸、字幕完整，并且都打开原图看过。
- Gemini 审核结果为 `OVERALL: PASS`。发布后以后台读到的状态为准，不以脚本的自报为准。
- 发布包齐全：`发布包-<批次>/<NN-讲者-主题>/{01_..jpg,02_..jpg,03_..jpg,小红书.txt,抖音.txt,公众号贴图.txt}`，加上 `review-*.md`。

## Constraints
- 事实红线：中文只翻译或压缩，不加原话里没有的东西。标题不能比图里的内容说得更宽，例如原话没提鸡蛋，标题就不能写鸡蛋。名人故事的标题可以用反差加问号，但答案必须在图里。
- 图上字幕是后期译制的，不是原生字幕。`来源记录.md` 和文案出处行都要写「中文字幕为译制」。
- 每篇正文末尾写出处：`来源：<频道/媒体> <讲者+场合>（YouTube 官方频道），中文字幕为译制。` 健康类再加 `内容为受访者观点，不构成医疗建议。`
- `小红书.txt` 必须有 `媒体：<原频道名>` 这一行。脚本用它填「来源转载」声明，缺这一行会直接报错，不会用默认值。
- 发布、定时发布和删帖都是敏感操作。用户说「审过就发」或「排上」，并且审核是 PASS，才能执行；否则只存草稿。公众号只推草稿，由用户在公众号助手 App 里点发表。
- 新号每平台每天最多 1–3 篇，按 1 篇排。同一时段不要连发，几篇会互相抢流量。
- 系统 python 是 3.9，渲染一律用 `~/.hermes/venvs/nsqi/bin/python`。跑 yt-dlp 前先 `unset PYTHONPATH PYTHONHOME`。

## Procedure
1. **选题池**：用 `yt-dlp --flat-playlist` 搜索候选，按 `references/sourcing-and-rendering.md` 的标准排序，写进 `选题池-<线>-第N批.md`（链接、频道、时长、播放量、可切的故事、标题草稿，可切的故事都标「待字幕核实」）。名人线另看 `references/celebrity-track.md`。
2. **下载**：`scripts/dl.sh <NN-讲者-主题> <YouTube ID>`，会轮换 player_client 并重试。然后用 `scripts/vtt2txt.py` 生成 `analysis/transcript.txt`。写 `来源记录.md`（URL、标题、频道、时长、字幕类型、下载日期、模式=脚本字幕、版权归属）。
3. **选句**：在 transcript 里定位故事段落。字幕定位不到的故事就换一段，不硬写。每张图选 5–7 句连续论证，过渡句可以跳过。第一句写明主语，不要用「他们/它」开头。
4. **写 script.json**：`lines[].t` 取字幕区间的中点，必须严格递增。每行约 ≤17 字，长句拆到同一区间内的两个时间点。用 `sample -t ... --around 0.8` 检查第一帧，必须是特写。
5. **渲染和质检**：跑 `scripts/render_all.sh <目录>`，渲染全部 script.json 并生成 sheet.jpg。逐张打开原图检查。出现黑条说明那个时间点是 B-roll，用 `sample --start A --end B --interval 0.5` 找到讲者帧，把 t 挪过去后加 `--overwrite` 重渲。
6. **写文案**：格式见 `references/platform-publishing.md`。正文用「① ② ③ 依次对应三张图」，标题 ≤20 字。
7. **审核闸门**：packet = 每张图前后各留余量的英文原文 + 图上中文字幕 + 各平台文案。跑 `hermes -z "$(cat review-prompt.md review-packet.md)" --provider antigravity-oauth -m gemini-3.8-flash > review-gemini-N.md`。结果是 FIX 时，先回原文核对再改，因为审稿模型也会误报。改完重审，直到 PASS。prompt 模板在 `templates/review-prompt.md`。
8. **发布**：`scripts/run_mjs.sh <帖子目录> 1 <PUBLISH 0|1> <xhs_fill.mjs|dy_publish.mjs> <SPACE id> [SAVE]`。第一篇先用 PUBLISH=0 跑一遍，截图确认图数、顺序和正文，再正式发。要定时发布，就在平台的定时发布里设时间；没有定时发布时，用 cron 在设定时刻跑上面的命令。公众号贴图用 `md2wechat create_image_post`。
9. **核对**：小红书看 note-manager，抖音看 content/manage，公众号用 draft/batchget，按标题确认帖子在、图数对。删掉失败时留下的本地草稿，然后 `task.finish({keep: []})`。
10. **看数据**：发布后 24h 和 48h 各读一次后台，方法见 `creator-channel-analytics`。和同期笔记比中位数倍数，算赞、藏、评、分享各占观看的比例。结果更新到 `references/celebrity-track.md` 的观察表，下一批选题按它调整。

## Stop
- 素材找不到干净的讲者特写、字幕核实不了、平台要扫码登录，或者审核出现 BLOCK：停下来，把情况交给用户。
- 发布前任一自检不过（声明、出处行、图数、话题）：脚本会打印 `CHECK FAILED` 并且不发。不要绕过检查。

## Verify
交付时说明：各平台的实际状态（后台核对的结果）、审核跑了几轮、改了什么、需要用户手动做的事，以及下一次看数据的时间。
