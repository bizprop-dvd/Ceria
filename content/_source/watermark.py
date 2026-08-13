"""Take the generator's mark off the chapter illustrations.

The twelve masters arrived with a small "AI生成" stamped in the bottom-left
corner. The masters keep it — they are the delivered files and are never
edited. This removes it on the way to the copies the app ships.

HOW

The mark is the same stamp in the same place on all twelve, laid over twelve
different background colours. That is enough to recover it exactly rather than
guess at it:

    seen = background * (1 - alpha) + white * alpha

Eleven of the twelve have a flat wash under the mark, so the background there
is known — it is the colour of the surrounding border. Each of those eleven
gives an independent reading of alpha per pixel; averaging them cancels the
JPEG noise. Undoing the composite then restores whatever was underneath.

That matters for chapter ten, where the mark lies across the edge of a wooden
floor. Painting or blurring the mark out would have left a smudge there. Undoing
the composite brings the grain back.

What the maths cannot undo is the JPEG ringing that was baked in around the
strokes when the masters were encoded. A gentle median, applied only where the
mark actually was, settles that.
"""

import numpy as np
from PIL import Image, ImageFilter

# A window around the mark, with room to spare on every side.
WINDOW = (0, 935, 170, 1018)
# Pictures with a flat wash under the mark — the ones alpha is solved from.
# Chapter 10 is excluded: it has a floor there, so its background is not known.
FLAT_CHAPTERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
WHITE = 255.0
# Below this the mark is thinner than the JPEG noise; leave those pixels alone.
MIN_ALPHA = 0.01
# Never divide by less than this — a fully opaque pixel carries no information
# about what was under it.
MAX_ALPHA = 0.97


def solve_alpha(masters):
    """Recover the mark's coverage from pictures with a known background.

    `masters` maps chapter number to a full-size PIL image. Returns a 2-D array
    the size of WINDOW, or None if too few flat pictures were supplied.
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
