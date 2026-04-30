# macOS 微信双开完整教程

> 来源：[yichen-skills/mac-wechat-dual-open](https://github.com/mcncarl/yichen-skills/tree/main/mac-wechat-dual-open)
> 整理时间：2026-04-28
> 来自翡冷翠

---

## 简介

本教程介绍如何在 macOS 上创建第二个微信应用实例，实现同时登录两个微信账号。该方法**无需第三方注入工具**，通过修改应用 bundle identifier 和重新签名实现，相对安全可靠。

---

## 核心原理

macOS 通过 **bundle identifier** 来区分应用。通过以下步骤，系统将副本视为独立应用：

1. 复制 `/Applications/WeChat.app` 到 `~/Applications/WeChat-2.app`
2. 修改副本的 `CFBundleIdentifier`（例如改为 `com.tencent.xin2`）
3. 使用 `codesign` 进行本地临时签名
4. 直接启动副本的可执行文件

---

## 前提条件

- macOS 12+，已安装微信于 `/Applications/WeChat.app`
- Python 3.10+
- Pillow 库（用于图标变色）：`pip3 install Pillow`
- Xcode Command Line Tools：`xcode-select --install`

---

## 快速使用（推荐脚本方式）

### 1. 检查当前状态

```bash
python3 wechat_dual_open.py status
```

输出示例：
```
source: /Applications/WeChat.app exists=True version=3.8.0 bundle=com.tencent.xin
target: ~/Applications/WeChat-2.app exists=False
```

### 2. 创建第二个微信

```bash
python3 wechat_dual_open.py create
```

此命令会：
- 复制应用到 `~/Applications/WeChat-2.app`
- 修改 bundle ID 为 `com.tencent.xin2`
- 设置中文语言偏好
- 移除 `CFBundleIconName` 避免缓存问题
- 重新签名并注册到 Launch Services

### 3. 设置语言（解决英文界面问题）

```bash
python3 wechat_dual_open.py set-language --languages zh-Hans en
```

### 4. 更换图标颜色（便于区分）

将微信绿色图标变为蓝色：

```bash
python3 wechat_dual_open.py recolor-icon --blue "#1296db"
```

### 5. 启动第二个微信

```bash
python3 wechat_dual_open.py launch
```

### 6. 修复问题

微信更新后，原应用升级可能导致副本失效，运行修复：

```bash
python3 wechat_dual_open.py repair
```

---

## 手动操作方式（理解原理）

如果不想使用脚本，可手动执行以下命令：

```bash
# 1. 复制应用
cp -R /Applications/WeChat.app ~/Applications/WeChat-2.app

# 2. 修改 bundle identifier
/usr/libexec/PlistBuddy -c "Set :CFBundleIdentifier com.tencent.xin2" \
  ~/Applications/WeChat-2.app/Contents/Info.plist

# 3. 重新签名
codesign --force --deep --sign - ~/Applications/WeChat-2.app

# 4. 设置中文语言
defaults write com.tencent.xin2 AppleLanguages -array zh-Hans en

# 5. 启动第二个实例
nohup ~/Applications/WeChat-2.app/Contents/MacOS/WeChat >/dev/null 2>&1 &
```

---

## 可靠性评估

**评分：6.5～7 / 10**

| 优点 | 缺点 |
|------|------|
| 无代码注入，无第三方工具 | **微信更新后需重新创建** |
| 易于检查和撤销 | 推送通知可能不稳定 |
| 在多个 macOS/微信版本上可用 | 登录状态和钥匙串按 bundle ID 隔离 |
| | 临时签名可能被微信更严格检查 |

### 风险提示

1. **更新即失效**：每次更新原微信后，需重新运行 `create` 或 `repair`
2. **推送通知**：APNs 与原应用身份绑定，副本可能收不到推送
3. **避免降级**：教程中要求固定微信版本的做法不安全，建议保持更新
4. **拒绝第三方注入工具**：相比本方案，注入工具风险更高

---

## 常见问题排查

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 第二个微信打开是英文界面 | 新 bundle ID 没有语言偏好 | 运行 `set-language` 后重启 |
| "已损坏/无法打开" | Gatekeeper 阻止未签名应用 | 系统设置 → 隐私与安全性 → 仍要打开 |
| "应用程序版本过低" | 账号先登录了错误实例 | 退出两个微信 → 先登录原微信 → 再启动副本 |
| Dock 仍显示绿色图标 | 图标缓存未刷新 | 退出微信副本重新启动 |
| 微信更新后副本消失 | 原微信更新，副本过时 | 重新运行 `create` 或 `repair` |

---

## 安全须知

- **永远不要修改 `/Applications/WeChat.app`** —— 所有修改仅作用于副本
- 删除现有副本前请用户确认，优先使用 `repair` 而非删除重建
- 必须先执行 `codesign` 再添加 Finder 自定义图标，否则会报错 "resource fork not allowed"

---

## 图标变色技术细节

微信图标存储在多处，脚本会处理所有位置：

| 位置 | 作用 |
|------|------|
| `Contents/Resources/AppIcon.icns` | 主应用图标 |
| `Contents/MacOS/WeChatAppEx.app/Contents/Resources/app.icns` | 嵌入式运行时图标 |
| `Contents/Resources/Assets.car` | 资源目录（通过移除 `CFBundleIconName` 处理）|
| `Icon\r` + Finder 自定义图标属性 | Finder "应用程序" 视图 |

变色算法使用 HSV/HSL 色相旋转，将绿色区域映射到目标蓝色。

---

## 完整 Python 脚本

```python
#!/usr/bin/env python3
"""Create and maintain a second macOS WeChat app."""

from __future__ import annotations

import argparse
import colorsys
import os
import plistlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


DEFAULT_SOURCE = Path("/Applications/WeChat.app")
DEFAULT_TARGET = Path("~/Applications/WeChat-2.app").expanduser()
DEFAULT_BUNDLE_ID = "com.tencent.xin2"
DEFAULT_LANGUAGES = ["zh-Hans", "en"]


def run(args: list[str], *, check: bool = True, capture: bool = False) -> subprocess.CompletedProcess:
    kwargs = {
        "check": check,
        "text": True,
    }
    if capture:
        kwargs.update({"stdout": subprocess.PIPE, "stderr": subprocess.STDOUT})
    return subprocess.run(args, **kwargs)


def require_tool(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise SystemExit(f"Missing required macOS tool: {name}")
    return path


def plist_path(app: Path) -> Path:
    return app / "Contents" / "Info.plist"


def read_plist(path: Path) -> dict:
    with path.open("rb") as f:
        return plistlib.load(f)


def write_plist(path: Path, data: dict) -> None:
    with path.open("wb") as f:
        plistlib.dump(data, f, sort_keys=False)


def app_version(app: Path) -> str:
    try:
        info = read_plist(plist_path(app))
        return info.get("CFBundleShortVersionString") or info.get("CFBundleVersion") or "unknown"
    except Exception:
        return "unknown"


def bundle_id(app: Path) -> str:
    try:
        return read_plist(plist_path(app)).get("CFBundleIdentifier", "unknown")
    except Exception:
        return "unknown"


def embedded_app(target: Path) -> Path:
    return target / "Contents" / "MacOS" / "WeChatAppEx.app"


def outer_icon(target: Path) -> Path:
    return target / "Contents" / "Resources" / "AppIcon.icns"


def inner_icon(target: Path) -> Path:
    return embedded_app(target) / "Contents" / "Resources" / "app.icns"


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def copy_app(source: Path, target: Path) -> None:
    if not source.exists():
        raise SystemExit(f"Source app not found: {source}")
    if target.exists():
        raise SystemExit(f"Target already exists: {target}. Use repair, or delete/recreate only after user confirmation.")
    ensure_parent(target)
    shutil.copytree(source, target, symlinks=True)


def set_bundle_id(app: Path, new_id: str) -> None:
    info_path = plist_path(app)
    info = read_plist(info_path)
    info["CFBundleIdentifier"] = new_id
    write_plist(info_path, info)


def remove_icon_name(app: Path) -> None:
    for info_path in [plist_path(app), plist_path(embedded_app(app))]:
        if info_path.exists():
            info = read_plist(info_path)
            if "CFBundleIconName" in info:
                del info["CFBundleIconName"]
                write_plist(info_path, info)


def clear_finder_custom_icon(app: Path) -> None:
    """Remove Finder custom icon detritus before code signing."""
    icon_file = app / "Icon\r"
    if icon_file.exists():
        icon_file.unlink()
    for path in [app, icon_file]:
        for attr in ["com.apple.FinderInfo", "com.apple.ResourceFork"]:
            run(["xattr", "-d", attr, str(path)], check=False, capture=True)


def codesign(app: Path) -> None:
    require_tool("codesign")
    clear_finder_custom_icon(app)
    result = run(["codesign", "--force", "--deep", "--sign", "-", str(app)], check=False, capture=True)
    if result.returncode != 0:
        raise SystemExit(result.stdout)


def register_and_refresh(app: Path) -> None:
    """Re-register the app with Launch Services and flush icon caches."""
    lsregister = Path("/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister")
    if lsregister.exists():
        run([str(lsregister), "-f", str(app)], check=False)
        ex = embedded_app(app)
        if ex.exists():
            run([str(lsregister), "-f", str(ex)], check=False)
    run(["qlmanage", "-r", "cache"], check=False, capture=True)
    run(["killall", "iconservicesagent"], check=False, capture=True)


def set_language(bundle: str, languages: list[str]) -> None:
    run(["defaults", "write", bundle, "AppleLanguages", "-array", *languages])


def launch(app: Path) -> None:
    exe = app / "Contents" / "MacOS" / "WeChat"
    if not exe.exists():
        raise SystemExit(f"WeChat executable not found: {exe}")
    subprocess.Popen([str(exe)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)


def status(source: Path, target: Path) -> None:
    print(f"source: {source} exists={source.exists()} version={app_version(source)} bundle={bundle_id(source)}")
    print(f"target: {target} exists={target.exists()} version={app_version(target)} bundle={bundle_id(target)}")
    if target.exists():
        for p in [outer_icon(target), inner_icon(target)]:
            print(f"icon: {p} exists={p.exists()} size={p.stat().st_size if p.exists() else 'n/a'}")
    ps = run(["ps", "-axo", "pid,command"], check=False, capture=True).stdout or ""
    for needle in [str(source), str(target)]:
        rows = [line.strip() for line in ps.splitlines() if needle in line and "Contents/MacOS/WeChat" in line]
        print(f"running for {needle}: {len(rows)}")
        for row in rows[:5]:
            print(f"  {row}")


def create(source: Path, target: Path, new_bundle_id: str, languages: list[str]) -> None:
    copy_app(source, target)
    set_bundle_id(target, new_bundle_id)
    set_language(new_bundle_id, languages)
    remove_icon_name(target)
    codesign(target)
    register_and_refresh(target)
    print(f"created: {target}")


def repair(target: Path, new_bundle_id: str, languages: list[str]) -> None:
    if not target.exists():
        raise SystemExit(f"Target app not found: {target}")
    set_bundle_id(target, new_bundle_id)
    set_language(new_bundle_id, languages)
    remove_icon_name(target)
    codesign(target)
    register_and_refresh(target)
    print(f"repaired: {target}")


def import_pillow():
    try:
        from PIL import Image
    except Exception as exc:
        raise SystemExit(
            f"Pillow is required for icon recoloring.\n"
            f"Install it with: pip3 install Pillow\n"
            f"Original error: {exc}"
        ) from exc
    return Image


def extract_largest_png(icns: Path, work: Path) -> Path:
    require_tool("iconutil")
    iconset = work / "source.iconset"
    run(["iconutil", "-c", "iconset", str(icns), "-o", str(iconset)])
    candidates = sorted(iconset.glob("*.png"), key=lambda p: p.stat().st_size, reverse=True)
    if not candidates:
        raise SystemExit(f"No PNG renditions extracted from {icns}")
    return candidates[0]


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("Use a 6-digit hex color such as #1296db")
    try:
        return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use a 6-digit hex color such as #1296db") from exc


def recolor_green_to_blue(src_png: Path, out_png: Path, target_rgb: tuple[int, int, int]) -> None:
    Image = import_pillow()
    img = Image.open(src_png).convert("RGBA")
    target_h = colorsys.rgb_to_hls(*(c / 255 for c in target_rgb))[0]
    pix = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pix[x, y]
            if a == 0:
                continue
            h, light, sat = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
            hue = h * 360
            is_green = 70 <= hue <= 175 and sat > 0.18 and g > r * 1.04 and g > b * 1.04
            is_greenish_light = g > 135 and g > r + 14 and g > b + 10 and sat > 0.10
            if is_green or is_greenish_light:
                new_sat = min(1.0, max(sat * 1.03, 0.34 if light < 0.82 else sat))
                new_light = min(0.92, light + (0.25 < light < 0.72) and 0.035 or 0.0)
                nr, ng, nb = colorsys.hls_to_rgb(target_h, new_light, new_sat)
                pix[x, y] = (round(nr * 255), round(ng * 255), round(nb * 255), a)
    img.save(out_png)


def build_icns(preview_png: Path, out_icns: Path) -> None:
    Image = import_pillow()
    require_tool("iconutil")
    img = Image.open(preview_png).convert("RGBA")
    iconset = out_icns.parent / "AppIcon.iconset"
    if iconset.exists():
        shutil.rmtree(iconset)
    iconset.mkdir()
    for size in [16, 32, 128, 256, 512]:
        img.resize((size, size), Image.Resampling.LANCZOS).save(iconset / f"icon_{size}x{size}.png")
        img.resize((size * 2, size * 2), Image.Resampling.LANCZOS).save(iconset / f"icon_{size}x{size}@2x.png")
    run(["iconutil", "-c", "icns", str(iconset), "-o", str(out_icns)])


def set_finder_custom_icon(app: Path, preview_png: Path, work: Path) -> None:
    """Set a Finder custom icon using Carbon-era tools if available."""
    for tool in ["sips", "DeRez", "Rez", "SetFile"]:
        if not shutil.which(tool):
            print(f"  note: skipping Finder custom icon ({tool} not found); icns replacement is sufficient")
            return
    custom_png = work / "custom-icon-source.png"
    rsrc = work / "custom-icon.rsrc"
    shutil.copy2(preview_png, custom_png)
    run(["sips", "-i", str(custom_png)], capture=True)
    with rsrc.open("w") as f:
        subprocess.run(["DeRez", "-only", "icns", str(custom_png)], check=True, text=True, stdout=f)
    icon_file = app / "Icon\r"
    if icon_file.exists():
        icon_file.unlink()
    run(["Rez", "-append", str(rsrc), "-o", str(icon_file)])
    run(["SetFile", "-a", "C", str(app)])
    run(["SetFile", "-a", "V", str(icon_file)])


def recolor_icon(source: Path, target: Path, blue: tuple[int, int, int], no_finder_custom_icon: bool) -> None:
    if not target.exists():
        raise SystemExit(f"Target app not found: {target}")
    source_icns = outer_icon(source)
    if not source_icns.exists():
        raise SystemExit(f"Source icon not found: {source_icns}")
    with tempfile.TemporaryDirectory(prefix="wechat-blue-icon-") as td:
        work = Path(td)
        src_png = extract_largest_png(source_icns, work)
        preview = work / "wechat-original-blue-preview.png"
        new_icns = work / "AppIcon.icns"
        recolor_green_to_blue(src_png, preview, blue)
        build_icns(preview, new_icns)
        for dest in [outer_icon(target), inner_icon(target)]:
            if dest.parent.exists():
                shutil.copy2(new_icns, dest)
                print(f"replaced icon: {dest}")
        remove_icon_name(target)
        codesign(target)
        if not no_finder_custom_icon:
            set_finder_custom_icon(target, preview, work)
        register_and_refresh(target)
        print(f"recolor complete; preview saved to {preview}")


def main():
    p = argparse.ArgumentParser(description="Create and maintain a second macOS WeChat app")
    p.add_argument("--source-app", type=Path, default=DEFAULT_SOURCE, help="Path to original WeChat.app")
    p.add_argument("--target-app", type=Path, default=DEFAULT_TARGET, help="Path to second WeChat app")
    p.add_argument("--bundle-id", default=DEFAULT_BUNDLE_ID, help="Bundle identifier for the copy")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="Check current state")
    sub.add_parser("create", help="Create the second WeChat app")
    sub.add_parser("repair", help="Repair bundle id, signing, language, and caches")
    sub.add_parser("launch", help="Launch the second WeChat instance")
    p_setlang = sub.add_parser("set-language", help="Set language preferences")
    p_setlang.add_argument("--languages", nargs="+", default=DEFAULT_LANGUAGES, help="Language codes")
    p_recolor = sub.add_parser("recolor-icon", help="Recolor icon from green to blue")
    p_recolor.add_argument("--blue", type=hex_to_rgb, default=(18, 150, 219), help="Target blue hex color (default: #1296db)")
    p_recolor.add_argument("--no-finder-custom-icon", action="store_true", help="Skip Finder custom icon step")
    args = p.parse_args()

    if args.cmd == "status":
        status(args.source_app, args.target_app)
    elif args.cmd == "create":
        create(args.source_app, args.target_app, args.bundle_id, DEFAULT_LANGUAGES)
    elif args.cmd == "repair":
        repair(args.target_app, args.bundle_id, DEFAULT_LANGUAGES)
    elif args.cmd == "launch":
        launch(args.target_app)
    elif args.cmd == "set-language":
        set_language(args.bundle_id, args.languages)
    elif args.cmd == "recolor-icon":
        recolor_icon(args.source_app, args.target_app, args.blue, args.no_finder_custom_icon)


if __name__ == "__main__":
    main()
```

---

## 参考与致谢

- 原始教程作者：[@koffuxu](https://x.com/koffuxu/status/2043110831584690427) (2026-04, 博客文章: "Mac 微信双开最完美方案")
- 验证确认：[@MinLiBuilds](https://x.com/MinLiBuilds/status/2043121624971678083) (2026-04)
- 图标变色使用 Pillow 的 HSV/HSL 色相旋转
- Finder 自定义图标使用经典 Carbon 资源工具 (`DeRez`/`Rez`)

---

*来自翡冷翠*
