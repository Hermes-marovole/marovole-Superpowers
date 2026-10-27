#!/usr/bin/env python3
"""Render HTML cover (`10_package/cover.html`) and chapter figures (`10_package/figures/*.html`) to PNG/JPG using headless Chrome.

Usage:
  python3 render_visuals.py <project_dir> [--cover-size 1600,2400] [--figure-size 1400,980]
"""
import argparse, glob, os, shutil, subprocess, sys


def find_chrome():
    cands = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chrome"),
    ]
    for c in cands:
        if c and os.path.exists(c):
            return c
    return None


def render_html(chrome, html_path, png_path, size="1400,980"):
    abs_html = os.path.abspath(html_path)
    abs_png = os.path.abspath(png_path)
    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        f"--window-size={size}",
        "--hide-scrollbars",
        f"--screenshot={abs_png}",
        f"file://{abs_html}",
    ]
    subprocess.run(cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, check=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    p.add_argument("--cover-size", default="1600,2400")
    p.add_argument("--figure-size", default="1400,980")
    a = p.parse_args()

    chrome = find_chrome()
    if not chrome:
        sys.exit("Google Chrome / Chromium not found; cannot render HTML cover/figures.")

    proj = os.path.abspath(a.project_dir)
    pkg = os.path.join(proj, "10_package")
    os.makedirs(pkg, exist_ok=True)

    cover_html = os.path.join(pkg, "cover.html")
    if os.path.exists(cover_html):
        cover_png = os.path.join(pkg, "cover.png")
        cover_jpg = os.path.join(pkg, "cover.jpg")
        render_html(chrome, cover_html, cover_png, size=a.cover_size)
        if shutil.which("sips"):
            subprocess.run(
                ["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92", cover_png, "--out", cover_jpg],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )
        print("rendered cover:", cover_png, cover_jpg if os.path.exists(cover_jpg) else "")

    fig_dir = os.path.join(pkg, "figures")
    if os.path.isdir(fig_dir):
        htmls = sorted(glob.glob(os.path.join(fig_dir, "*.html")))
        for h in htmls:
            png = os.path.splitext(h)[0] + ".png"
            render_html(chrome, h, png, size=a.figure_size)
            print("rendered figure:", os.path.basename(png))


if __name__ == "__main__":
    main()
