# 选素材与渲染细节

## 搜索与排序
```bash
yt-dlp --flat-playlist --playlist-end 8 --print "%(id)s | %(channel)s | %(duration_string)s | %(view_count)s | %(title)s" "ytsearch8:<人物/主题> interview"
yt-dlp --skip-download --print "%(upload_date)s %(height)sp subs=%(subtitles.en.0.ext)s" URL   # 有无人工英文字幕
```
- 首选单人特写、干净背景、B-roll 少的视频，例如 Big Think 完整访谈、大学演讲、达沃斯对谈。双人播客也可以用，主画面挑正脸。
- 动画类或代码画面类视频做不了主画面，因为这个格式要靠人脸撑起来。
- 只要 Creative Commons 视频时，在搜索 URL 后加 `&sp=EgIwAQ%253D%253D`（素材通常偏少）。
- 机房出口 IP 会随机触发 bot 验证。换 player_client 加重试就能过。要用 `--cookies-from-browser` 必须先问用户，因为这会读取浏览器凭证。

## 目录
`~/HermesWork/字幕长图/NN-讲者-主题/{source/video.mp4, source/*.vtt, analysis/transcript.txt, NN_标题.script.json, output-v1/*.jpg, 来源记录.md}`

## 渲染
```bash
~/.hermes/venvs/nsqi/bin/python ~/.hermes/skills/media/native-subtitle-quote-image/scripts/native_subtitle_stitch.py \
  render-script source/video.mp4 --script X.script.json --out output-v1/X.jpg --aspect 3:4 --width 1440 [--overwrite]
```
- 7 句字幕时主画面约占 55%，5 句约占 70%。
- 取帧有约 0.5s 偏差。挪时间点时挪到讲者那段的中间，不要贴着边缘。
- 先用 `sample --start A --end B --interval 3` 扫全片拼总览图，标出特写段，再选哪几段当每张图的首句；B-roll 多的杂志短片尤其要先扫。
- 首句开口时镜头已切走（背影/B-roll）时，可把首句 t 提前到同一特写镜头里、上一句字幕结束后的空档帧（讲者没在说别的话），并在来源记录写明该例外；不要把 t 放进别的台词区间。特写里讲者低头/闭眼时按 0.3s 步长细扫挑睁眼帧。
- 主画面糊（讲者转头的运动模糊）时，在该句区间内按 0.4s 步长细扫，挑连续 2 帧以上都清晰的那段中点；单帧清晰的点会因 0.5s 偏差落到糊帧上。
- 首句开口处不是特写、但相邻下一条字幕区间是特写时，可把相邻两条原文合成一句中文、t 放在特写那条区间里（来源记录写「合并 A–B 两条」）。
- 渲染后字幕条字号明显变小 = 该行太长被自动缩字号；压到约 15 字以内重渲，不要接受一张图里字号不一。
- 人工字幕（`subtitles` 里有 en、vtt 很小且带标点）优先于自动字幕，审核误报少。查法：`--print "%(subtitles.en.0.ext|none)s"`，非 none 即有人工字幕。多条视频连续拉字幕会被 429，逐条拉、间隔几秒。
- 批量拉字幕报 `The page needs to be reloaded` 或 429 时，加 `--extractor-args "youtube:player_client=tv_simply"`，每条间隔约 6s；仍拿不到的先标「待核」，不要硬重试。
- 不允许嵌入的视频（web_embedded 报 Video unavailable）：dl.sh 轮换全失败时，隔几分钟用**不带 extractor-args** 的默认调用重试常能过（10-08 马斯克 60 Minutes 即如此）。同一时段连续下第二条容易连续报 reload。android_vr 只给 360p，不能用。
- 限流死循环兜底：ego-lite 装 Stream Recorder 插件（用户 10-08 装），对官方播放器 1080p 画面录制：`ego-cli nodejs` 只吃 stdin（`cat x.mjs | ego-browser nodejs`），页面跳到段起点，`video.captureStream()` + MediaRecorder（vp9,opus 12Mbps）录 dur 秒自动下载 webm；ffmpeg 转 h264 mp4 后照常 render-script（nsqi 读不了无 duration 的原生 webm）。录前先跳广告、setPlaybackQualityRange('hd1080')，段头留 1s 缓冲，段尾超时长会让字幕条渲染失败——把最后一行 t 压到时长-0.5s。模板：`~/HermesWork/字幕长图/scripts/rec_yt.mjs`（cfg 在 scratch/rec_cfg.json）。
- 自动字幕没有标点，还有识别错误（人名、术语）。写进审核 packet 时注明这一点，免得审稿模型把识别错误当成翻译错误。
- 新上传视频常暂无字幕：用本机 whisper.cpp 转写（Metal，约 20× 实时，4.4h 音频约 17 分钟）：`ffmpeg -i X -vn -ac 1 -ar 16000 a.wav && whisper-cli -m ~/models/whisper/ggml-large-v3-turbo.bin -f a.wav -l en -t 8 -ovtt -of analysis/whisper`（中文用 `-l zh --prompt "简体中文…人名"`）。模型用户要求保留，勿删。
