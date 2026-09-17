"""Generate Capacitor source assets from content/logo.jpg.

Outputs into assets/ (consumed by `npx @capacitor/assets generate`):
  icon-foreground.png / icon-background.png  -> adaptive icon (star mark)
  icon.png                                   -> single-image icon fallback
  splash.png / splash-dark.png               -> launch screens (full logo)

Re-run after changing the logo:  python3 assets/_generate_assets.py
"""
from PIL import Image, ImageDraw
import os

HERE = os.path.dirname(__file__)
LOGO = os.path.join(HERE, "..", "content", "logo.jpg")

CREAM = (250, 246, 238)      # --ceria-cream
DARK = (31, 41, 55)          # --ceria-dark

def load_rgba_transparent(path, thr=238):
    """Load image, make near-white background transparent."""
    im = Image.open(path).convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if r >= thr and g >= thr and b >= thr:
                px[x, y] = (r, g, b, 0)
    return im

def bbox_in_region(im, y0frac, y1frac):
    """Bounding box of opaque pixels within a vertical band."""
    w, h = im.size
    region = im.crop((0, int(h * y0frac), w, int(h * y1frac)))
    bb = region.getbbox()
    if not bb:
        return None
    return (bb[0], bb[1] + int(h * y0frac), bb[2], bb[3] + int(h * y0frac))

def paste_centered(canvas, img, target_frac):
    """Scale img to target_frac of canvas width, paste centered."""
    cw, ch = canvas.size
    scale = (cw * target_frac) / img.width
    nw, nh = int(img.width * scale), int(img.height * scale)
    img = img.resize((nw, nh), Image.LANCZOS)
    canvas.alpha_composite(img, ((cw - nw) // 2, (ch - nh) // 2))
    return canvas

def rounded_card(size, radius, color):
    card = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius=radius, fill=color + (255,))
    return card

logo = load_rgba_transparent(LOGO)
full = logo.crop(logo.getbbox())                         # whole logo, trimmed
star_bb = bbox_in_region(logo, 0.0, 0.68)                # star mark only (no wordmark)
star = logo.crop(star_bb)

def out(name):
    return os.path.join(HERE, name)

# --- Adaptive icon (Android) + single icon ---
# Foreground: star centered in the adaptive "safe zone" (~62% of the icon).
fg = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
paste_centered(fg, star, 0.62)
fg.save(out("icon-foreground.png"))

bg = Image.new("RGBA", (1024, 1024), CREAM + (255,))
bg.save(out("icon-background.png"))

# Single-image icon fallback (iOS uses this): star on cream, a touch larger.
icon = Image.new("RGBA", (1024, 1024), CREAM + (255,))
paste_centered(icon, star, 0.72)
icon.save(out("icon.png"))

# --- Splash screens ---
splash = Image.new("RGBA", (2732, 2732), CREAM + (255,))
paste_centered(splash, full, 0.34)
splash.save(out("splash.png"))

splash_dark = Image.new("RGBA", (2732, 2732), DARK + (255,))
card = rounded_card((1280, 1280), 260, CREAM)
paste_centered(card, full, 0.74)
splash_dark.alpha_composite(card, ((2732 - 1280) // 2, (2732 - 1280) // 2))
splash_dark.save(out("splash-dark.png"))

# Also refresh the web favicon/logo copy in public/
full_web = Image.new("RGBA", (512, 512), CREAM + (255,))
paste_centered(full_web, star, 0.8)
full_web.convert("RGB").save(os.path.join(HERE, "..", "public", "icon-512.png"))

print("Generated:", ", ".join(sorted(f for f in os.listdir(HERE) if f.endswith(".png"))))
