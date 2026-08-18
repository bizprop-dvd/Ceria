"""Prepare the twelve chapter illustrations for the app.

Masters live in assets/chapters/chNN.jpg or .png at the size and in the format
they were delivered. They are never edited in place — this reads them and writes
what the app ships:

  src/assets/chapters/chNN.jpg    1200 x 800

Vite emits them as twelve separate files and gives the app their URLs, so they
are fetched one at a time as a reader moves through the book. None of the image
data lands in the JavaScript a parent parses at startup. Keeping them here
rather than in public/ also means the shareable single-file preview can inline
them, instead of showing twelve broken pictures to a reviewer.

On the way through it takes the generator's "AI生成" corner mark off the masters
that carry one — see watermark.py, which undoes the mark rather than painting
over it, and leaves the pictures that arrived clean alone.

It also checks each picture's background against its chapter's colour in
src/lib/chapterTheme.ts. The illustration sits directly on the app's cream with
its own wash showing, so a picture whose background has drifted away from its
chapter would read as a mistake. A warning here means either the artwork or the
theme needs a look.

Run:  python3 content/_source/build_chapter_images.py
"""

import os
import re
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import watermark  # noqa: E402

SRC_DIR = os.path.join(ROOT, "assets", "chapters")
OUT_DIR = os.path.join(ROOT, "src", "assets", "chapters")
THEME_TS = os.path.join(ROOT, "src", "lib", "chapterTheme.ts")

# The app frame is 448 px wide at most, so 1200 covers it on a 2.5x screen with
# room to spare. Beyond that is bytes a parent pays for and cannot see.
SIZE = (1200, 800)
QUALITY = 82
# How far a picture's background may sit from its chapter tint, per channel,
# before it is worth a second look. Around 12 is still invisible on screen.
TINT_TOLERANCE = 12
# How much unevenness the mended corner may carry. About 3 is the JPEG noise
# floor of these masters; above 6 the mark has left a visible shadow.
RESIDUAL_LIMIT = 6.0
# How far the four corners may disagree before the picture counts as full-bleed
# — a scene that runs to the edges rather than sitting on a flat wash.
FULL_BLEED_SPREAD = 25


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    theme = _theme_tints()
    total = 0
    warnings = []

    masters = {}
    for n in range(1, 13):
        for ext in ("jpg", "png"):
            src = os.path.join(SRC_DIR, f"ch{n:02d}.{ext}")
            if os.path.exists(src):
                masters[n] = Image.open(src).convert("RGB")
                break
        else:
            warnings.append(f"ch{n:02d}: no master in assets/chapters/")

    alpha = watermark.load_alpha()
    if alpha is None:
        warnings.append("watermark-alpha.png missing — any corner mark stays in the pictures")

    marked = 0
    for n, master in masters.items():
        if abs(master.width / master.height - 1.5) > 0.01:
            warnings.append(
                f"ch{n:02d}: {master.width}x{master.height} is not 3:2, it will be squashed"
            )

        # Only the masters that actually carry the mark are mended. Undoing a
        # composite that was never applied would leave a ghost of the glyphs.
        im = master
        stamped = 0.0 if alpha is None else watermark.carries_mark(master, alpha)
        if stamped > watermark.MARK_CORRELATION:
            marked += 1
            im = watermark.remove(master, alpha)
            if n in watermark.FLAT_CHAPTERS:
                left = watermark.residual(master, alpha)
                if left > RESIDUAL_LIMIT:
                    warnings.append(f"ch{n:02d}: corner still uneven after removal ({left:.1f})")

        out = os.path.join(OUT_DIR, f"ch{n:02d}.jpg")
        im.resize(SIZE, Image.LANCZOS).save(
            out, "JPEG", quality=QUALITY, optimize=True, progressive=True
        )
        size = os.path.getsize(out)
        total += size

        found, spread = _corner_colour(im)
        want = theme.get(n)
        mark = "  mark removed" if stamped > watermark.MARK_CORRELATION else ""

        if spread > FULL_BLEED_SPREAD:
            # The scene runs to the edges, so there is no wash to compare. Not a
            # fault: it just sits in its rounded card as a picture, not a tint.
            note = "  full-bleed, no wash"
        else:
            drift = max(abs(a - b) for a, b in zip(_rgb(found), _rgb(want))) if want else 0
            note = "  <- drifted from the chapter colour" if drift > TINT_TOLERANCE else ""
            if note:
                warnings.append(f"ch{n:02d}: wash {found}, chapter tint {want}")
        print(f"  ch{n:02d}  {size / 1024:6.0f} kB   background {found}{mark}{note}")

    print(f"Wrote {OUT_DIR}/  —  {total / 1024:.0f} kB shipped in the app")
    print(f"  corner mark found on {marked} of {len(masters)} masters")
    for w in warnings:
        print(f"  WARNING: {w}")


def _corner_colour(im):
    """The picture's own background, and how much the four corners disagree.

    Sampling a small block in each corner and taking the median channel avoids
    being thrown off by anything that reaches into one corner. The spread says
    whether there is a flat wash at all: a picture whose scene runs to the edges
    has corners that do not agree, and nothing to compare with a chapter tint.
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
    spread = max(max(s[i] for s in samples) - min(s[i] for s in samples) for i in range(3))
    return "#%02X%02X%02X" % median, spread


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
