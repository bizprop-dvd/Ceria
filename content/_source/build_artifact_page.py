"""Turn the self-contained preview into a publishable page body.

The Artifact host wraps whatever it is given in its own <!doctype>/<html>/
<head>/<body>, so a complete HTML document cannot be handed to it directly.
This lifts the <style>, <title> and <script> out of the built preview and
emits just the fragment that belongs inside a body.

Run `npm run build:preview` first.

Usage:  python3 content/_source/build_artifact_page.py
Output: content/_source/out/ceria-app.html
"""

import pathlib
import re

SRC = pathlib.Path("preview-dist/index.html")
OUT = pathlib.Path("content/_source/out/ceria-app.html")

# The published page is served under a strict CSP that blocks every external
# host, so the Google Fonts <link> would fail anyway. Dropping it avoids a
# console error; the stylesheet already falls back to Georgia and a system sans.
FONT_LINK = re.compile(r'<link[^>]+fonts\.(googleapis|gstatic)\.com[^>]*>', re.I)


def main():
    if not SRC.exists():
        raise SystemExit("preview-dist/index.html missing — run `npm run build:preview` first")
    html = SRC.read_text(encoding="utf-8")

    head = re.search(r"<head[^>]*>(.*?)</head>", html, re.S).group(1)
    body = re.search(r"<body[^>]*>(.*?)</body>", html, re.S).group(1)

    head = FONT_LINK.sub("", head)
    keep = "".join(
        m.group(0)
        for m in re.finditer(r"<style[^>]*>.*?</style>|<script[^>]*>.*?</script>", head, re.S)
    )

    # Lora and Inter as data URIs, since the CSP blocks the Google Fonts host.
    # Without them the app renders in Georgia and a system sans, which is not
    # what the founder is reviewing. Must precede the app's own stylesheet.
    fonts = pathlib.Path("content/_source/out/fonts.css")
    if not fonts.exists():
        raise SystemExit("run `python3 content/_source/inline_fonts.py` first")
    keep = f"<style>{fonts.read_text(encoding='utf-8')}</style>" + keep

    title = "<title>Ceria — pratinjau aplikasi</title>"
    # The app fills the viewport; the host page must not add its own scrollbar.
    frame = (
        "<style>html,body{margin:0;padding:0;height:100%;overflow:hidden;}"
        "#root{height:100dvh;}</style>"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(title + keep + frame + body, encoding="utf-8")
    print(f"Wrote {OUT}  ({OUT.stat().st_size / 1024:.0f} kB)")


if __name__ == "__main__":
    main()
