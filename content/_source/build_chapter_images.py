"""Prepare the twelve chapter illustrations for the app.

Masters live in assets/chapters/chNN.jpg at the size they were delivered. They
are never edited in place — this reads them and writes what the app ships:

  public/chapters/chNN.jpg    1200 x 800

They go in public/ rather than through the bundler on purpose. Capacitor loads
them from the app's own files, one at a time, as a reader moves through the
book — nothing about them belongs in the JavaScript a parent parses at startup.

It also checks each picture's background against its chapter's colour in
src/lib/chapterTheme.ts. The illustration sits directly on the app's cream with
its own wash showing, so a picture whose background has drifted away from its
chapter would read as a mistake. A warning here means either the artwork or the
theme needs a look.

Run:  python3 content/_source/build_chapter_images.py
"""

import os
import re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC_DIR = os.path.join(ROOT, "assets", "chapters")
OUT_DIR = os.path.join(ROOT, "public", "chapters")
THEME_TS = os.path.join(ROOT, "src", "lib", "chapterTheme.ts")

# The app frame is 448 px wide at most, so 1200 covers it on a 2.5x screen with
# room to spare. Beyond that is bytes a parent pays for and cannot see.
SIZE = (1200, 800)
QUALITY = 82
# How far a picture's background may sit from its chapter tint, per channel,
# before it is worth a second look. Around 12 is still invisible on screen.
TINT_TOLERANCE = 12


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theme = _theme_tints()
    total = 0
    warnings = []

    for n in range(1, 13):
        src = os.path.join(SRC_DIR, f"ch{n:02d}.jpg")
        if not os.path.exists(src):
            warnings.append(f"ch{n:02d}: no master in assets/chapters/")
            continue

        im = Image.open(src).convert("RGB")
        if abs(im.width / im.height - 1.5) > 0.01:
            warnings.append(f"ch{n:02d}: {im.width}x{im.height} is not 3:2, it will be squashed")

        out = os.path.join(OUT_DIR, f"ch{n:02d}.jpg")
        im.resize(SIZE, Image.LANCZOS).save(
            out, "JPEG", quality=QUALITY, optimize=True, progressive=True
        )
        size = os.path.getsize(out)
        total += size

        found = _corner_colour(im)
        want = theme.get(n)
        drift = max(abs(a - b) for a, b in zip(_rgb(found), _rgb(want))) if want else 0
        flag = "  <- drifted from the chapter colour" if drift > TINT_TOLERANCE else ""
        if flag:
            warnings.append(f"ch{n:02d}: background {found}, chapter tint {want}")
        print(f"  ch{n:02d}  {size / 1024:6.0f} kB   background {found}{flag}")

    print(f"Wrote {OUT_DIR}/  —  {total / 1024:.0f} kB shipped in the app")
    for w in warnings:
        print(f"  WARNING: {w}")


def _corner_colour(im):
    """The picture's own background, read from the four corners.

    Every illustration sits on a flat wash. Sampling a small block in each
    corner and taking the median channel avoids being thrown off by anything
    that reaches into one corner — the tree in chapter 1, the sofa in ten.
    """
    w, h = im.size
    box = max(8, w // 60)
    corners = [
        im.crop((0, 0, box, box)),
        im.crop((w - box, 0, w, box)),
        im.crop((0, h - box, box, h)),
        im.crop((w - box, h - box, w, h)),
    ]
    samples = [c.resize((1, 1), Image.LANCZOS).getpixel((0, 0)) for c in corners]
    median = tuple(sorted(s[i] for s in samples)[len(samples) // 2] for i in range(3))
    return "#%02X%02X%02X" % median


def _theme_tints():
    """The per-chapter tint hexes, read straight out of chapterTheme.ts."""
    with open(THEME_TS, encoding="utf-8") as f:
        source = f.read()
    pattern = r"(\d+):\s*\{[^}]*tint:\s*'(#[0-9A-Fa-f]{6})'"
    return {int(n): hexcode for n, hexcode in re.findall(pattern, source)}


def _rgb(hexcode):
    h = hexcode.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


if __name__ == "__main__":
    main()
