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
- 自动字幕没有标点，还有识别错误（人名、术语）。写进审核 packet 时注明这一点，免得审稿模型把识别错误当成翻译错误。
