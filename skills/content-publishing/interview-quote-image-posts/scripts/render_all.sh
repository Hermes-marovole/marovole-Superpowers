#!/bin/bash
# usage: render_all.sh DIR [OUT=output-v1] — 渲染 DIR 下所有 *.script.json 并生成 sheet.jpg
unset PYTHONPATH PYTHONHOME
P=~/.hermes/venvs/nsqi/bin/python
S=~/.hermes/skills/media/native-subtitle-quote-image/scripts/native_subtitle_stitch.py
cd ~/HermesWork/字幕长图/"$1"; OUT=${2:-output-v1}; mkdir -p "$OUT"
for f in *.script.json; do n=${f%.script.json}
  $P $S render-script source/video.mp4 --script "$f" --out "$OUT/$n.jpg" --aspect 3:4 --width 1440 --overwrite 2>&1 | tail -1
done
$P - "$OUT" <<'EOF'
import sys,glob
from PIL import Image
o=sys.argv[1];fs=sorted(glob.glob(o+'/0*.jpg'));ims=[Image.open(f).resize((720,960)) for f in fs]
c=Image.new('RGB',(720*len(ims),960));[c.paste(im,(i*720,0)) for i,im in enumerate(ims)];c.save(o+'/sheet.jpg',quality=85)
EOF
echo sheet: $PWD/$OUT/sheet.jpg
