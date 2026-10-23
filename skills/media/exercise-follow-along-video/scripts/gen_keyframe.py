#!/usr/bin/env python3
"""用 gpt-image-2（Dogbooks sub2api）出一张姿势关键帧，并裁成 H3 用的 1344x768（16:9）或 768x1344（9:16）。

  export DOGBOOKS_API_KEY=...   # 只从环境变量读，不要写进脚本或仓库
  python3 gen_keyframe.py --out kf/K_side_sit.png --prompt-file prompts/side_sit.txt [--ref kf/K_side_stand.png] [--ratio 16:9]

--ref 给了就走 /v1/images/edits（同一人物/服装/场景改姿势），不给走 /v1/images/generations。
原图存在 <out>.raw.png，裁切后的存在 --out。
"""
import argparse, base64, os, sys
from pathlib import Path
import requests
from PIL import Image

BASE = os.environ.get('DOGBOOKS_BASE', 'https://sub2api.dogbooks.co')


def crop(src, dst, tw, th):
    im = Image.open(src).convert('RGB')
    s = max(tw / im.width, th / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.Resampling.LANCZOS)
    l, t = (im.width - tw) // 2, (im.height - th) // 2
    im.crop((l, t, l + tw, t + th)).save(dst)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--prompt-file', required=True)
    ap.add_argument('--ref')
    ap.add_argument('--ratio', default='16:9', choices=['16:9', '9:16'])
    a = ap.parse_args()
    key = os.environ.get('DOGBOOKS_API_KEY')
    if not key:
        sys.exit('DOGBOOKS_API_KEY 未设置')
    prompt = Path(a.prompt_file).read_text(encoding='utf-8').strip()
    size = '1792x1024' if a.ratio == '16:9' else '1024x1792'
    hdr = {'Authorization': f'Bearer {key}'}
    if a.ref:
        with open(a.ref, 'rb') as f:
            r = requests.post(f'{BASE}/v1/images/edits', headers=hdr, timeout=300,
                              data={'model': 'gpt-image-2', 'prompt': prompt, 'size': size, 'n': 1},
                              files={'image': (Path(a.ref).name, f, 'image/png')})
    else:
        r = requests.post(f'{BASE}/v1/images/generations', headers=hdr, timeout=300,
                          json={'model': 'gpt-image-2', 'prompt': prompt, 'size': size, 'quality': 'high', 'n': 1})
    r.raise_for_status()
    d = r.json()['data'][0]
    img = base64.b64decode(d['b64_json']) if d.get('b64_json') else requests.get(d['url'], timeout=120).content
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    raw = out.with_suffix('.raw.png'); raw.write_bytes(img)
    tw, th = (1344, 768) if a.ratio == '16:9' else (768, 1344)
    crop(raw, out, tw, th)
    print('saved', out)


if __name__ == '__main__':
    main()
