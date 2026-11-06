#!/opt/homebrew/bin/python3
"""
Pre-render Visual Gatekeeper for Keyframe Video Generation (Seedance / MiniMax H3 / Flow)
1. sketch: Generate 1920x1080 color-block composition sketch with 38%/62% golden lines + grayscale luminance check.
2. diff: Overlay first & last keyframes to detect background drift, size mismatch (e.g. 13% cup scale drift), or crop misalignment.
3. patch: Paste a locally edited region back onto the original image with feathering so untouched background pixels have zero drift.
"""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps, ImageStat


def cmd_sketch(args):
    W, H = args.width, args.height
    spec = json.loads(Path(args.spec).read_text(encoding="utf-8")) if Path(args.spec).exists() else json.loads(args.spec)
    bg_hex = spec.get("bg", "#1a2436")
    blocks = spec.get("blocks", [])

    img = Image.new("RGB", (W, H), bg_hex)
    draw = ImageDraw.Draw(img)

    for b in blocks:
        xr, yr, wr, hr = b["rect"]
        x0, y0 = int(xr * W), int(yr * H)
        x1, y1 = int((xr + wr) * W), int((yr + hr) * H)
        draw.rectangle([x0, y0, x1, y1], fill=b.get("color", "#e0a96d"), outline="#ffffff", width=2)
        if b.get("label"):
            draw.text((x0 + 12, y0 + 12), b["label"], fill="#ffffff")

    for ratio in (0.38, 0.62):
        gx = int(W * ratio)
        gy = int(H * ratio)
        draw.line([(gx, 0), (gx, H)], fill="#00ffcc", width=2)
        draw.line([(0, gy), (W, gy)], fill="#00ffcc", width=1)

    out_color = Path(args.out_prefix + "_color.png")
    out_gray = Path(args.out_prefix + "_gray.png")
    img.save(out_color)

    gray = ImageOps.grayscale(img)
    gray.save(out_gray)

    bg_luma = ImageOps.grayscale(Image.new("RGB", (10, 10), bg_hex)).getpixel((0, 0))
    warnings = []
    for b in blocks:
        fg_luma = ImageOps.grayscale(Image.new("RGB", (10, 10), b.get("color", "#e0a96d"))).getpixel((0, 0))
        diff = abs(int(fg_luma) - int(bg_luma))
        if diff < 35:
            warnings.append(f"LOW_LUMA_CONTRAST: '{b.get('label', 'block')}' luma diff={diff} (<35) against bg")

    print(json.dumps({
        "status": "WARN" if warnings else "PASS",
        "color_sketch": str(out_color),
        "gray_sketch": str(out_gray),
        "bg_luma": bg_luma,
        "warnings": warnings
    }, ensure_ascii=False))


def cmd_diff(args):
    im1 = Image.open(args.first).convert("RGB")
    im2 = Image.open(args.last).convert("RGB")

    size_mismatch = im1.size != im2.size
    if size_mismatch:
        im2_resized = im2.resize(im1.size, Image.Resampling.LANCZOS)
    else:
        im2_resized = im2

    diff = ImageChops.difference(im1, im2_resized)
    gray_diff = ImageOps.grayscale(diff)
    stat = ImageStat.Stat(gray_diff)
    mean_diff = round(stat.mean[0], 2)

    hist = gray_diff.histogram()
    changed_px = sum(hist[26:])
    total_px = im1.size[0] * im1.size[1]
    changed_ratio = round(changed_px / total_px, 4)

    blend = Image.blend(im1, im2_resized, alpha=0.5)
    red_mask = gray_diff.point(lambda p: 255 if p > 25 else 0)
    red_layer = Image.new("RGB", im1.size, (255, 40, 40))
    overlay = Image.composite(red_layer, blend, red_mask)

    out_path = Path(args.out)
    overlay.save(out_path)

    print(json.dumps({
        "status": "FAIL_SIZE" if size_mismatch else ("WARN_HIGH_DRIFT" if changed_ratio > 0.45 else "PASS"),
        "first_size": list(im1.size),
        "last_size": list(im2.size),
        "size_mismatch": size_mismatch,
        "mean_luma_diff": mean_diff,
        "changed_pixel_ratio": changed_ratio,
        "diff_overlay": str(out_path)
    }, ensure_ascii=False))


def cmd_patch(args):
    orig = Image.open(args.orig).convert("RGB")
    edited = Image.open(args.edited).convert("RGB")
    if orig.size != edited.size:
        edited = edited.resize(orig.size, Image.Resampling.LANCZOS)

    x, y, w, h = [int(v) for v in args.box.split(",")]
    mask = Image.new("L", orig.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle([x, y, x + w, y + h], fill=255)
    if args.feather > 0:
        mask = mask.filter(ImageFilter.GaussianBlur(args.feather))

    result = Image.composite(edited, orig, mask)
    out_path = Path(args.out)
    result.save(out_path)
    print(json.dumps({
        "status": "PASS",
        "patched_file": str(out_path),
        "box": [x, y, w, h],
        "feather": args.feather
    }, ensure_ascii=False))


def main():
    p = argparse.ArgumentParser(description="Precheck keyframes & color sketches before video generation.")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_sketch = sub.add_parser("sketch", help="Generate 38pct/62pct color & grayscale composition sketch")
    p_sketch.add_argument("--spec", required=True, help="JSON string or file with {bg, blocks:[{label,color,rect:[x,y,w,h]}]}")
    p_sketch.add_argument("--out-prefix", required=True, help="Output file prefix")
    p_sketch.add_argument("--width", type=int, default=1920)
    p_sketch.add_argument("--height", type=int, default=1080)
    p_sketch.set_defaults(func=cmd_sketch)

    p_diff = sub.add_parser("diff", help="Overlay first and last frames to catch background/scale drift")
    p_diff.add_argument("--first", required=True)
    p_diff.add_argument("--last", required=True)
    p_diff.add_argument("--out", required=True)
    p_diff.set_defaults(func=cmd_diff)

    p_patch = sub.add_parser("patch", help="Paste edited region back onto original image with zero background drift")
    p_patch.add_argument("--orig", required=True)
    p_patch.add_argument("--edited", required=True)
    p_patch.add_argument("--box", required=True, help="x,y,w,h in pixels")
    p_patch.add_argument("--feather", type=int, default=6)
    p_patch.add_argument("--out", required=True)
    p_patch.set_defaults(func=cmd_patch)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
