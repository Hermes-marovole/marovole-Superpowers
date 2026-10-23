#!/usr/bin/env python3
"""把两条 H3 动作片段（去程 ext + 回程 ret）拼成一条带 UI 的跟练成片。

时间轴（对齐实拍样例 131.9s）：
  0-3s   片头：模糊背景 + 居中动作名 + 处方
  3-63s  第 1 组：10 次 × 6s（ext 3s + ret 3s），左上标题/处方，右上 60→1 秒倒计时
  63-71s 组间休息：模糊背景 + 「休息时间」+ 8 秒倒计时
  71-131s 第 2 组：同第 1 组；单侧动作传 --ext2/--ret2 换另一侧
  131-132s 收尾：「完成跟练」

用法：
  python3 build_follow_along.py --id 28 --name 坐姿腿屈伸 --rx 每组10次×2组 \
      --ext clips/28_ext.mp4 --ret clips/28_ret.mp4 --bg kf/K_side_sit.png \
      [--ext2 clips/28_ext_R.mp4 --ret2 clips/28_ret_R.mp4] \
      [--audio cues/28_cues.m4a] --out out/
不传 --audio 时输出静音成片并告警：不要把别的动作的口令音轨套到这条上。
"""
import argparse, shutil, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1920, 1080
INTRO, SET, REST, OUTRO, REPS, REP_HALF = 3, 60, 8, 1, 10, 3.0
TOTAL = INTRO + SET + REST + SET + OUTRO  # 132

FONT_BOLD = '~/Library/Fonts/SourceHanSansCN-Bold.otf'
FONT_MED = '~/Library/Fonts/SourceHanSansCN-Medium.otf'
FONT_NUM = '/System/Library/Fonts/Supplemental/DIN Alternate Bold.ttf'
INK, SUB, WHITE = (40, 42, 45, 255), (95, 100, 105, 255), (255, 255, 255, 255)


def font(p, size):
    return ImageFont.truetype(str(Path(p).expanduser()), size)


def ff(*args):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *map(str, args)], check=True)


def duration(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                        '-of', 'csv=p=0', str(p)], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def to_half_rep(src, dst):
    """H3 5s 片段 → 3.0s、1920x1080、30fps、无声。"""
    k = REP_HALF / duration(src)
    ff('-i', src, '-vf', f'scale={W}:{H}:flags=lanczos,setpts={k:.6f}*PTS,fps=30,format=yuv420p',
       '-c:v', 'libx264', '-crf', 16, '-preset', 'fast', '-t', REP_HALF, '-an', dst)


def concat(listfile, items, dst):
    listfile.write_text(''.join(f"file '{p}'\n" for p in items), encoding='utf-8')
    ff('-f', 'concat', '-safe', 0, '-i', listfile, '-c', 'copy', dst)


def still(img, dur, dst):
    ff('-loop', 1, '-i', img, '-vf', f'scale={W}:{H}:flags=lanczos,fps=30,format=yuv420p',
       '-c:v', 'libx264', '-crf', 16, '-preset', 'fast', '-t', dur, '-an', dst)


def blurred_bg(kf, dst):
    im = Image.open(kf).convert('RGB').resize((W, H), Image.Resampling.LANCZOS)
    veil = Image.new('RGB', (W, H), (235, 235, 232))
    Image.blend(im.filter(ImageFilter.GaussianBlur(28)), veil, 0.38).save(dst, quality=95)


def overlay_frames(d, title, rx):
    f_ti, f_si = font(FONT_BOLD, 72), font(FONT_MED, 34)
    f_tt, f_st = font(FONT_BOLD, 60), font(FONT_MED, 32)
    f_num, f_rt, f_rn = font(FONT_NUM, 155), font(FONT_BOLD, 68), font(FONT_NUM, 110)

    def cx(dr, text, f, y, c):
        b = dr.textbbox((0, 0), text, font=f)
        dr.text(((W - (b[2] - b[0])) // 2, y), text, font=f, fill=c)

    def head(dr):
        dr.text((85, 95), title, font=f_tt, fill=INK)
        dr.text((88, 175), rx, font=f_st, fill=SUB)

    def count(dr, n):
        s = f'{n:02d}'
        b = dr.textbbox((0, 0), s, font=f_num)
        dr.text((1810 - (b[2] - b[0]), 75), s, font=f_num, fill=WHITE)

    s1, r0, s2, o0 = INTRO, INTRO + SET, INTRO + SET + REST, INTRO + SET + REST + SET
    for s in range(TOTAL):
        im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        dr = ImageDraw.Draw(im)
        if s < s1:
            cx(dr, title, f_ti, 430, INK); cx(dr, f'{rx} · 准备开始', f_si, 540, SUB)
        elif s < r0:
            head(dr); count(dr, SET - (s - s1))
        elif s < s2:
            head(dr); cx(dr, '休息时间', f_rt, 390, INK); cx(dr, f'{REST - (s - r0):02d}', f_rn, 490, (60, 62, 65, 255))
        elif s < o0:
            head(dr); count(dr, SET - (s - s2))
        else:
            cx(dr, '完成跟练', f_ti, 430, INK); cx(dr, '太棒了，完成今日训练！', f_si, 540, SUB)
        im.save(d / f'frame_{s:04d}.png')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--id', type=int, required=True)
    ap.add_argument('--name', required=True)
    ap.add_argument('--rx', required=True, help='处方副标题，如 每组10次×2组')
    ap.add_argument('--ext', required=True); ap.add_argument('--ret', required=True)
    ap.add_argument('--ext2'); ap.add_argument('--ret2')
    ap.add_argument('--bg', required=True, help='该动作的起始关键帧，用作片头/休息的模糊底')
    ap.add_argument('--audio', help='本动作专属的口令/BGM 音轨（≥132s）')
    ap.add_argument('--out', required=True)
    ap.add_argument('--work')
    a = ap.parse_args()

    out_dir = Path(a.out); out_dir.mkdir(parents=True, exist_ok=True)
    work = Path(a.work or out_dir / '_work') / f'm{a.id:02d}'; work.mkdir(parents=True, exist_ok=True)
    title = f'{a.name}跟练'
    out = out_dir / f'{a.id:02d}_{a.name}_跟练完整版.mp4'

    def rep(ext, ret, tag):
        e, r, rp = work / f'{tag}_ext.mp4', work / f'{tag}_ret.mp4', work / f'{tag}_rep.mp4'
        to_half_rep(ext, e); to_half_rep(ret, r)
        concat(work / f'{tag}.txt', [e, r], rp)
        return rp

    rep1 = rep(a.ext, a.ret, 'set1')
    rep2 = rep(a.ext2, a.ret2, 'set2') if a.ext2 and a.ret2 else rep1

    bg = work / 'bg.png'; blurred_bg(a.bg, bg)
    intro, rest, outro = work / 'intro.mp4', work / 'rest.mp4', work / 'outro.mp4'
    still(bg, INTRO, intro); still(bg, REST, rest); still(bg, OUTRO, outro)

    base = work / 'base.mp4'
    concat(work / 'full.txt', [intro, *[rep1] * REPS, rest, *[rep2] * REPS, outro], base)

    ov = work / 'ov'; ov.mkdir(exist_ok=True)
    overlay_frames(ov, title, a.rx)

    cmd = ['-i', base, '-framerate', 1, '-i', ov / 'frame_%04d.png']
    if a.audio:
        cmd += ['-i', a.audio, '-filter_complex', '[0:v][1:v]overlay=0:0:format=auto[v]',
                '-map', '[v]', '-map', '2:a', '-c:a', 'aac', '-b:a', '192k']
    else:
        print('WARN: 没有 --audio，输出静音成片', file=sys.stderr)
        cmd += ['-filter_complex', '[0:v][1:v]overlay=0:0:format=auto[v]', '-map', '[v]']
    cmd += ['-c:v', 'libx264', '-crf', 17, '-preset', 'veryfast', '-pix_fmt', 'yuv420p',
            '-t', TOTAL - 0.1, '-movflags', '+faststart', out]
    ff(*cmd)
    shutil.rmtree(ov, ignore_errors=True)
    print('BUILT', out)


if __name__ == '__main__':
    main()
