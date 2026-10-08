#!/bin/bash
# usage: dl.sh DIR ID   — 依次尝试多个 player_client（嵌入被禁的视频 web_embedded 会报 unavailable）
cd ~/HermesWork/字幕长图
unset PYTHONPATH PYTHONHOME   # 后台进程会继承 Hermes venv 的路径，导致 py3.9 的 yt-dlp 导入 3.14 的 urllib3 崩溃
D="$1"; ID="$2"
mkdir -p "$D/source" "$D/analysis"
for round in 1 2 3; do
  for C in web_embedded tv_simply mweb default ios; do
    yt-dlp --extractor-args "youtube:player_client=$C" --no-progress \
      -f "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[height<=1080]/b" --merge-output-format mp4 \
      --write-subs --write-auto-subs --sub-langs "en,en-orig,en-US" --sub-format vtt \
      -o "$D/source/video.%(ext)s" --no-overwrites \
      -- "$ID" >> "$D/source/dl.log" 2>&1
    if [ -f "$D/source/video.mp4" ]; then echo "OK client=$C" >> "$D/source/dl.log"; break 2; fi
  done
  sleep 15
done
ls -la "$D/source"; tail -3 "$D/source/dl.log"
