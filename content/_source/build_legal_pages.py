"""Turn the two legal documents into pages a web team can publish.

docs/legal/*.md are the source. Each holds the English and the Indonesian text
of one document, separated by a `---\\n---` rule. This emits one self-contained
HTML file per document with both languages on the page, English first, and a
short jump link between them.

Deliberately plain: no fonts to load, no scripts, no external requests. It is
readable as-is, and a web team that wants it inside their own site template can
lift the contents of <main> and drop the CSS.

Run:  python3 content/_source/build_legal_pages.py
Out:  content/_source/out/privacy.html
      content/_source/out/terms.html
"""

import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(HERE, "out")

# "**Publisher:** …", "**Terakhir diperbarui:** …" and the like.
META_LINE = re.compile(r"^\*\*[^*]+:\*\*")

PAGES = [
    {
        "src": os.path.join(ROOT, "docs", "legal", "privacy-policy.md"),
        "out": "privacy.html",
        "title": "Kebijakan Privasi — Ceria",
        "url": "https://www.yayasanceria.org/privacy",
        "jump": ("Baca dalam Bahasa Indonesia", "Read in English"),
    },
    {
        "src": os.path.join(ROOT, "docs", "legal", "eula.md"),
        "out": "terms.html",
        "title": "Ketentuan Penggunaan — Ceria",
        "url": "https://www.yayasanceria.org/terms",
        "jump": ("Baca dalam Bahasa Indonesia", "Read in English"),
    },
]

CSS = """
:root { color-scheme: light dark; }
* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 2.5rem 1.25rem 5rem;
  background: #FAF6EE;
  color: #1F2937;
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
main { max-width: 40rem; margin: 0 auto; }
h1 {
  font-size: 1.55rem; line-height: 1.25; margin: 0 0 .35rem;
  color: #2E4FA3; font-weight: 700;
}
h2 { font-size: 1.1rem; margin: 2.25rem 0 .5rem; color: #2E4FA3; }
p, li { margin: 0 0 .85rem; }
ul { padding-left: 1.15rem; }
li { margin-bottom: .4rem; }
a { color: #2E4FA3; }
code {
  background: #F2E9D9; padding: .1em .35em; border-radius: .25rem;
  font-size: .9em; word-break: break-all;
}
strong { font-weight: 600; }
hr { border: 0; border-top: 1px solid #E5DED0; margin: 3.5rem 0 2.5rem; }
.meta { color: #6B7280; font-size: .9rem; margin-bottom: .25rem; }
.jump { margin: 1.5rem 0 0; font-size: .95rem; }
blockquote { display: none; }
@media (prefers-color-scheme: dark) {
  body { background: #16161a; color: #e6e4df; }
  h1, h2, a { color: #9db2ee; }
  code { background: #2a2a30; }
  hr { border-top-color: #33333a; }
  .meta { color: #a3a19c; }
}
"""


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for page in PAGES:
        with open(page["src"], encoding="utf-8") as f:
            text = f.read()

        halves = re.split(r"\n---\n---\n", text)
        if len(halves) != 2:
            raise SystemExit(
                f"{page['src']}: expected one '---/---' rule between the English "
                f"and Indonesian halves, found {len(halves) - 1}"
            )

        en = render(halves[0], anchor="en")
        idn = render(halves[1], anchor="id")
        jump_id, jump_en = page["jump"]

        doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page['title'])}</title>
<link rel="canonical" href="{page['url']}">
<meta name="robots" content="index, follow">
<style>{CSS}</style>
</head>
<body>
<main>
{en}
<p class="jump"><a href="#id">{html.escape(jump_id)} &darr;</a></p>
<hr>
{idn}
<p class="jump"><a href="#en">{html.escape(jump_en)} &uarr;</a></p>
</main>
</body>
</html>
"""
        path = os.path.join(OUT_DIR, page["out"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(doc)
        print(f"  {page['out']:14} {len(doc) / 1024:5.0f} kB   -> {page['url']}")

    print(f"Wrote {OUT_DIR}/")


def render(markdown, anchor):
    """The small subset of Markdown these two documents actually use."""
    out = []
    lines = markdown.strip().split("\n")
    para, bullets, first_heading = [], [], True

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def flush_bullets():
        if bullets:
            items = "".join(f"<li>{inline(b)}</li>" for b in bullets)
            out.append(f"<ul>{items}</ul>")
            bullets.clear()

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # The editorial notes to ourselves are not for the public page.
        if line.startswith(">"):
            flush_para(); flush_bullets()
            i += 1
            continue
        if line.strip() == "---":
            flush_para(); flush_bullets()
            i += 1
            continue

        if line.startswith("## "):
            flush_para(); flush_bullets()
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            flush_para(); flush_bullets()
            tag = f' id="{anchor}"' if first_heading else ""
            first_heading = False
            out.append(f"<h1{tag}>{inline(line[2:])}</h1>")
        elif line.startswith("- "):
            flush_para()
            item = line[2:]
            # continuation lines of the same bullet
            while i + 1 < len(lines) and lines[i + 1].startswith("  ") and lines[i + 1].strip():
                i += 1
                item += " " + lines[i].strip()
            bullets.append(item)
        elif META_LINE.match(line):
            # "**Publisher:** …" and its siblings sit on their own lines under
            # the title. Markdown would run them into one paragraph; on the page
            # they read as a list of facts, so each keeps its own line.
            flush_para(); flush_bullets()
            out.append(f'<p class="meta">{inline(line.strip())}</p>')
        elif not line.strip():
            flush_para(); flush_bullets()
        else:
            flush_bullets()
            para.append(line.strip())
        i += 1

    flush_para(); flush_bullets()

    return "\n".join(out)


def inline(text):
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # Bare URLs, which is the only link form these documents use.
    text = re.sub(r"(?<![\"'>=])(https?://[^\s<),]+)", r'<a href="\1">\1</a>', text)
    return text


if __name__ == "__main__":
    main()
