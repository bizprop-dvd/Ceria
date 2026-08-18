"""Take the generator's mark off the chapter illustrations that carry one.

The first twelve masters arrived with a small "AI生成" stamped in the bottom-left
corner. Later replacements arrived clean. The masters are never edited either
way — this decides, per picture, whether there is a mark to take off on the way
to the copies the app ships.

HOW THE MARK WAS RECOVERED

It was the same stamp in the same place on all twelve of the originals, laid
over twelve different background colours:

    seen = background * (1 - alpha) + white * alpha

Eleven of those had a flat wash under the mark, so the background there was
known — it is the colour of the surrounding border. Each gave an independent
reading of alpha per pixel; averaging them cancelled the JPEG noise. The result
is saved in watermark-alpha.png and reused, so replacing masters can never
shrink the pool it was solved from. solve_alpha() regenerates it if the twelve
originals are ever needed again.

WHY IT IS UNDONE RATHER THAN PAINTED OVER

Undoing the composite restores whatever was underneath. That matters where the
mark lay across the edge of a wooden floor: painting or blurring would have left
a smudge there. What the maths cannot undo is the JPEG ringing baked in around
the strokes when the masters were encoded, so a gentle median, applied only
where the mark actually was, settles that.

TELLING MARKED FROM UNMARKED

A picture with no mark must be left alone: undoing a composite that was never
applied would brighten those pixels and leave a ghost of the glyphs. Since the
mark's exact shape is known, the test is a correlation — how much the picture's
own high-pass residual in that corner looks like the mark. A stamped picture
scores above 0.88 even over a busy wooden floor; a clean one scores within 0.07
of zero. Nothing lands in between.
"""

import os

import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA_FILE = os.path.join(HERE, "watermark-alpha.png")

# A window around the mark, with room to spare on every side.
WINDOW = (0, 935, 170, 1018)
# Pictures whose wash under the mark is flat — the ones alpha can be solved
# from. Only used by solve_alpha(); chapter 10's original had a floor there.
FLAT_CHAPTERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
WHITE = 255.0
# Below this the mark is thinner than the JPEG noise; leave those pixels alone.
MIN_ALPHA = 0.01
# Never divide by less than this — a fully opaque pixel carries no information
# about what was under it.
MAX_ALPHA = 0.97
# How much a picture's corner has to look like the mark before it is treated as
# stamped. Measured: marked 0.88-1.00, clean -0.04 to +0.07.
MARK_CORRELATION = 0.5


def load_alpha():
    """The mark's coverage map, as recovered from the original twelve."""
    if not os.path.exists(ALPHA_FILE):
        return None
    a = np.asarray(Image.open(ALPHA_FILE)).astype(float) / 65535.0
    return np.minimum(np.clip(a, 0, 1), MAX_ALPHA)


def carries_mark(im, alpha):
    """Does this picture actually have the mark stamped on it?

    Correlates the corner's high-pass residual against the known shape. Returns
    the correlation, which is near 1 when stamped and near 0 when not.
    """
    crop = im.crop(WINDOW).convert("RGB")
    background = crop.filter(ImageFilter.MedianFilter(size=11))
    residual = (
        np.asarray(crop).astype(float) - np.asarray(background).astype(float)
    ).mean(axis=2)

    inked = alpha > 0.05
    if not inked.any():
        return 0.0
    x = alpha[inked] - alpha[inked].mean()
    y = residual[inked] - residual[inked].mean()
    denominator = np.sqrt((x * x).sum() * (y * y).sum())
    return 0.0 if denominator == 0 else float((x * y).sum() / denominator)


def remove(im, alpha):
    """Return a copy of `im` with the mark undone."""
    a = _window(im)
    a3 = alpha[..., None]
    bare = np.clip((a - WHITE * a3) / (1 - a3), 0, 255)

    # Only where the mark was, and feathered out at its edge.
    weight = np.clip(alpha * 3.0, 0, 1)[..., None]
    settled = np.asarray(
        Image.fromarray(bare.astype("uint8")).filter(ImageFilter.MedianFilter(size=5))
    ).astype(float)
    patched = bare * (1 - weight) + settled * weight

    out = im.copy()
    out.paste(Image.fromarray(patched.astype("uint8")), (WINDOW[0], WINDOW[1]))
    return out


def residual(im, alpha):
    """How far the mended area strays from the wash around it, in levels 0-255.

    Only meaningful for a picture with a flat background under the mark. Around
    3 is the JPEG noise floor of these files; much above that means the removal
    left something behind.
    """
    a = _window(im)
    bg = _wash(a)
    mended = _window(remove(im, alpha))
    return float(np.abs(mended - bg).max())


def solve_alpha(masters):
    """Recover the mark's coverage from pictures with a known background.

    `masters` maps chapter number to a full-size PIL image. Returns a 2-D array
    the size of WINDOW, or None if too few flat pictures were supplied. Only
    needed to regenerate watermark-alpha.png.
    """
    readings = []
    for n in FLAT_CHAPTERS:
        im = masters.get(n)
        if im is None:
            continue
        a = _window(im)
        bg = _wash(a)
        readings.append(((a - bg) / (WHITE - bg)).mean(axis=2))
    if len(readings) < 4:
        return None

    alpha = np.clip(np.mean(readings, axis=0), 0, 1)
    alpha[alpha < MIN_ALPHA] = 0.0
    return np.minimum(alpha, MAX_ALPHA)


def _window(im):
    return np.asarray(im.crop(WINDOW).convert("RGB")).astype(float)


def _wash(a):
    """The background colour, read from the window's border where the mark never reaches."""
    border = np.concatenate([
        a[:8].reshape(-1, 3),
        a[-8:].reshape(-1, 3),
        a[:, :8].reshape(-1, 3),
        a[:, -20:].reshape(-1, 3),
    ])
    return np.median(border, axis=0)
