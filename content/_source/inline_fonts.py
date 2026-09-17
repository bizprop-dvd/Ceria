"""Fetch Lora and Inter and emit them as a self-contained @font-face stylesheet.

The published page runs under a CSP that blocks every external host, so the
app's <link> to Google Fonts cannot load there. Without this the headings fall
back to Georgia and the body to a system sans — a visible change from the app
the founder is actually reviewing.

Only the latin subset is taken; the app's text is English and Indonesian, both
of which it covers.

Usage:  python3 content/_source/inline_fonts.py
Output: content/_source/out/fonts.css
"""

import base64
import pathlib
import re
import subprocess

CSS_URL = (
    "https://fonts.googleapis.com/css2"
    "?family=Lora:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap"
)
# woff2 is only served to a browser-like client; the default curl UA gets ttf.
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)
OUT = pathlib.Path("content/_source/out/fonts.css")


def fetch(url, binary=False):
    r = subprocess.run(
        ["curl", "-sS", "-A", UA, "--max-time", "30", url],
        capture_output=True,
        check=True,
    )
    return r.stdout if binary else r.stdout.decode("utf-8")


def main():
    css = fetch(CSS_URL)
    blocks = re.findall(r"/\*\s*([a-z-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
    latin = [b for subset, b in blocks if subset == "latin"]
    if not latin:
        raise SystemExit("no latin subset found — did the CSS format change?")

    out, total = [], 0
    for block in latin:
        url = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
        data = fetch(url, binary=True)
        total += len(data)
        uri = "data:font/woff2;base64," + base64.b64encode(data).decode("ascii")
        block = re.sub(r"url\(https://[^)]+\.woff2\)", f"url({uri})", block)
        # unicode-range is pointless once there is a single embedded subset
        block = re.sub(r"\s*unicode-range:[^;]+;", "", block)
        out.append(block)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(out), encoding="utf-8")
    fams = sorted({re.search(r"font-family:\s*'([^']+)'", b).group(1) for b in latin})
    print(f"Wrote {OUT}")
    print(f"  faces: {len(latin)}  families: {', '.join(fams)}")
    print(f"  woff2 payload: {total / 1024:.0f} kB  ->  css {OUT.stat().st_size / 1024:.0f} kB")


if __name__ == "__main__":
    main()
