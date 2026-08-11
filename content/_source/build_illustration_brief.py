"""Build the chapter illustration brief as a shareable page.

Pulls the twelve chapter titles, principles and hues straight from the source
of truth so the brief cannot drift from the app an illustrator is drawing for.

Usage:  python3 content/_source/build_illustration_brief.py
Output: content/_source/out/illustration-brief.html
"""

import json
import pathlib
import re

ROOT = pathlib.Path(".")
OUT = ROOT / "content/_source/out/illustration-brief.html"
FONTS = ROOT / "content/_source/out/fonts.css"

# What each chapter should show. Grounded in that chapter's own teaching, and
# chosen to be drawable — a scene, not a concept.
SUBJECTS = {
    1: ("A parent and child walking somewhere ordinary, the child half a step ahead "
        "and the parent letting them lead.",
        "Formation, not control. The parent is present and unhurried, not steering."),
    2: ("The same child at three ages in one frame — a toddler, a school-age child, a "
        "teenager — in the same posture, growing across the picture.",
        "Behaviour that looks like a character flaw is usually just an age."),
    3: ("A parent alone for a moment: sitting on the edge of a bed or a step, one hand "
        "resting on their chest, taking a breath. The household soft and out of focus behind.",
        "The only chapter where the parent is by themselves. Give them that space."),
    4: ("Two figures brought to the same height, one leaning in to listen. Show speech as "
        "a soft shape passing between them, never as written words.",
        "Empathy first, then redirection — so listening is the action in the frame."),
    5: ("A parent holding a limit: an open, steady hand and a warm stance, with a child "
        "mid-protest. Neither face angry.",
        "Firm and kind at the same moment. This is the hardest one to get right and the "
        "most important — do not let it read as scolding."),
    6: ("A child beside a small storm — a dark soft shape near them — and a parent sitting "
        "down next to it rather than reaching in to take it away.",
        "Name it to tame it. The feeling is allowed to be there."),
    7: ("A morning hallway that works: shoes in a row, a bag on its hook, a simple picture "
        "schedule on the wall. People small or absent.",
        "The only one that is mostly a place rather than people. Calm structure."),
    8: ("A child in a difficult moment, drawn with curiosity rather than judgement, and the "
        "parent looking past the behaviour to what sits behind it.",
        "Behaviour has a function. Warm, puzzled, not exasperated."),
    9: ("A child alone and absorbed in an ordinary job — carrying a plate to the sink, "
        "feeding an animal, watering something.",
        "Character is built by small repeated responsibility. No adult praising in frame."),
    10: ("A parent and child sitting close on a step or a floor, doing nothing in particular. "
         "Shoulders touching.",
         "The relationship is the curriculum. Stillness, not activity."),
    11: ("A family indoors with weather visible through the window — grey outside, warm "
         "inside.",
         "Pressure from outside the family. The room is safe; the weather is not the family's fault."),
    12: ("A year seen as a path of small marks or steps, with a parent pausing to look back "
         "along it.",
         "Reflection and small repeated adjustments. Quiet, not triumphant."),
}


def load(name):
    return json.loads((ROOT / "content" / name).read_text(encoding="utf-8"))


def themes():
    src = (ROOT / "src/lib/chapterTheme.ts").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(
        r"(\d+):\s*\{\s*base:\s*'(#\w+)',\s*tint:\s*'(#\w+)',\s*ring:\s*'(#\w+)'", src
    ):
        out[int(m.group(1))] = {"base": m.group(2), "tint": m.group(3), "ring": m.group(4)}
    return out


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    g = load("guidebook.json")
    d = load("daily.json")
    th = themes()
    ranges = {c["number"]: (c["dayStart"], c["dayEnd"]) for c in d["chapters"]}
    fonts = FONTS.read_text(encoding="utf-8") if FONTS.exists() else ""

    cards = []
    for c in g["chapters"]:
        n = c["number"]
        t = th[n]
        subject, note = SUBJECTS[n]
        a, b = ranges[n]
        cards.append(f"""
      <article class="ch" style="--base:{t['base']};--tint:{t['tint']}">
        <header>
          <span class="num">{n:02d}</span>
          <div>
            <h3>{esc(c['title']['en'])}</h3>
            <p class="id-title">{esc(c['title']['id'])}</p>
          </div>
        </header>
        <p class="principle">{esc(c['principle']['en'])}</p>
        <p class="subject"><strong>Draw:</strong> {esc(subject)}</p>
        <p class="note">{esc(note)}</p>
        <div class="swatches">
          <span class="sw" style="background:{t['base']}">{t['base']}</span>
          <span class="sw light" style="background:{t['tint']}">{t['tint']} — background</span>
        </div>
        <p class="meta">Days {a}–{b} &middot; file <code>ch{n:02d}.png</code></p>
      </article>""")

    html = f"""<title>Ceria — chapter illustration brief</title>
<style>
{fonts}
:root {{
  --cream:#FAF6EE; --cream-deep:#F2E9D9; --ink:#1F2937; --muted:#6B7280;
  --blue:#2E4FA3; --pink:#E91E80; --card:#FFFFFF; --rule:#E7DECD;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --cream:#15171C; --cream-deep:#1D2027; --ink:#ECE7DD; --muted:#9AA1AC;
    --blue:#8FA6E0; --pink:#F072AE; --card:#1B1E25; --rule:#2C313A;
  }}
}}
:root[data-theme="dark"] {{
  --cream:#15171C; --cream-deep:#1D2027; --ink:#ECE7DD; --muted:#9AA1AC;
  --blue:#8FA6E0; --pink:#F072AE; --card:#1B1E25; --rule:#2C313A;
}}
:root[data-theme="light"] {{
  --cream:#FAF6EE; --cream-deep:#F2E9D9; --ink:#1F2937; --muted:#6B7280;
  --blue:#2E4FA3; --pink:#E91E80; --card:#FFFFFF; --rule:#E7DECD;
}}
* {{ box-sizing:border-box; }}
body {{
  margin:0; background:var(--cream); color:var(--ink);
  font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:16px; line-height:1.65; -webkit-font-smoothing:antialiased;
}}
.wrap {{ max-width:60rem; margin:0 auto; padding:3rem 1.25rem 5rem; }}
h1,h2,h3 {{ font-family:Lora,Georgia,serif; font-weight:600; text-wrap:balance; margin:0; }}
h1 {{ font-size:clamp(1.9rem,4vw,2.6rem); color:var(--blue); line-height:1.2; }}
.lede {{ font-size:1.05rem; color:var(--muted); max-width:44rem; margin:.75rem 0 0; }}
h2 {{ font-size:1.3rem; color:var(--blue); margin:3rem 0 .75rem; }}
p {{ margin:.6rem 0; }}
.eyebrow {{
  font-size:.72rem; letter-spacing:.12em; text-transform:uppercase;
  color:var(--pink); font-weight:600; margin:0 0 .4rem;
}}
.panel {{
  background:var(--card); border:1px solid var(--rule); border-radius:14px;
  padding:1.25rem 1.4rem; margin:1rem 0;
}}
ul {{ margin:.5rem 0; padding-left:1.15rem; }}
li {{ margin:.35rem 0; }}
.two {{ display:grid; gap:1rem; grid-template-columns:repeat(auto-fit,minmax(17rem,1fr)); }}
.yes li::marker {{ color:#0E7C74; }}
.no li::marker {{ color:#A85440; }}
.grid {{ display:grid; gap:1rem; grid-template-columns:repeat(auto-fit,minmax(20rem,1fr)); margin-top:1rem; }}
.ch {{
  background:var(--card); border:1px solid var(--rule); border-radius:14px;
  padding:1.1rem 1.2rem 1rem; border-top:5px solid var(--base);
}}
.ch header {{ display:flex; gap:.8rem; align-items:baseline; }}
.num {{
  font-family:Lora,Georgia,serif; font-size:1.5rem; font-weight:600;
  color:var(--base); font-variant-numeric:tabular-nums; line-height:1;
}}
.ch h3 {{ font-size:1.05rem; line-height:1.3; }}
.id-title {{ margin:.1rem 0 0; font-size:.85rem; color:var(--muted); font-style:italic; }}
.principle {{
  margin:.7rem 0 .8rem; padding-left:.7rem; border-left:3px solid var(--base);
  font-size:.92rem; color:var(--ink);
}}
.subject {{ font-size:.95rem; }}
.subject strong {{ color:var(--base); }}
.note {{ font-size:.86rem; color:var(--muted); }}
.swatches {{ display:flex; flex-wrap:wrap; gap:.4rem; margin:.8rem 0 .5rem; }}
.sw {{
  font-size:.7rem; padding:.25rem .5rem; border-radius:6px; color:#fff;
  font-variant-numeric:tabular-nums;
}}
.sw.light {{ color:#1F2937; border:1px solid var(--rule); }}
.meta {{ font-size:.78rem; color:var(--muted); margin:.4rem 0 0; }}
code {{
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:.85em;
  background:var(--cream-deep); padding:.1rem .35rem; border-radius:4px;
}}
.id-block {{ background:var(--cream-deep); border-radius:14px; padding:1.25rem 1.4rem; }}
.id-block h2 {{ margin-top:0; }}
footer {{ margin-top:3rem; padding-top:1.25rem; border-top:1px solid var(--rule); color:var(--muted); font-size:.85rem; }}
</style>

<div class="wrap">
  <p class="eyebrow">Ceria &middot; Yayasan Sukacita Keluarga Indonesia</p>
  <h1>Chapter illustrations — brief</h1>
  <p class="lede">
    Twelve illustrations, one for each chapter of a 365-day parenting guide for
    Indonesian families. They open each chapter inside a phone app. They are the
    only pictures in it, so they carry the whole feeling of the thing.
  </p>

  <h2>What we need</h2>
  <div class="panel">
    <ul>
      <li><strong>Twelve images</strong>, named <code>ch01.png</code> through <code>ch12.png</code>.</li>
      <li><strong>1800 &times; 1200 px</strong> (3:2 landscape), PNG.</li>
      <li><strong>Keep the subject in the middle 80%.</strong> The edges may be cropped on
        narrow phones, so nothing important should sit near them.</li>
      <li><strong>No text anywhere in the artwork.</strong> The app is in Indonesian and
        English and adds its own words.</li>
      <li><strong>Fill the background</strong> with the pale colour given for that chapter.
        Not white, not transparent.</li>
    </ul>
  </div>

  <h2>How they should feel</h2>
  <div class="two">
    <div class="panel yes">
      <p class="eyebrow">Yes</p>
      <ul>
        <li>Indonesian families — faces, clothing, hair, homes. Surabaya, not a stock library.</li>
        <li>Vary who is in them: two parents, one parent, a grandparent, an older sibling.
          Some mothers in hijab, some not.</li>
        <li>Quiet and ordinary. Kitchens, doorways, floors, the edge of a bed.</li>
        <li>Soft hand-drawn shapes with a light grain or texture.</li>
        <li>Four or five colours per picture, taken from that chapter's own hue.</li>
      </ul>
    </div>
    <div class="panel no">
      <p class="eyebrow">No</p>
      <ul>
        <li>No perfect, glossy, advertising families.</li>
        <li>No shouting, crying-as-comedy, or a child made to look naughty.</li>
        <li>No flat geometric blob-people — that style is everywhere and dates fast.</li>
        <li>No heavy black outlines, no harsh shadows.</li>
        <li>No hands cupping seedlings, no lightbulbs, no jigsaw pieces.</li>
      </ul>
    </div>
  </div>

  <div class="panel">
    <p class="eyebrow">The one rule that matters most</p>
    <p style="margin:0">
      A parent opening chapter 5 has probably just shouted at their child and feels
      terrible. Every picture has to be kind to that person. Warm, never clever at a
      parent's expense, and never showing a family doing better than the reader's.
    </p>
  </div>

  <h2>The twelve</h2>
  <p class="lede" style="margin-bottom:0">
    Each chapter has its own colour, already used throughout the app. Use it as the
    picture's lead colour and its pale version as the background.
  </p>
  <div class="grid">{''.join(cards)}
  </div>

  <div class="id-block" style="margin-top:3rem">
    <h2>Ringkasan dalam Bahasa Indonesia</h2>
    <ul>
      <li><strong>Dua belas gambar</strong>, satu untuk setiap bab. Nama berkas
        <code>ch01.png</code> sampai <code>ch12.png</code>.</li>
      <li><strong>Ukuran 1800 &times; 1200 piksel</strong> (3:2, mendatar), format PNG.</li>
      <li><strong>Jangan menaruh bagian penting di tepi gambar</strong> — tepinya bisa
        terpotong di layar ponsel yang sempit.</li>
      <li><strong>Tanpa tulisan di dalam gambar.</strong> Aplikasinya dwibahasa dan
        menambahkan teksnya sendiri.</li>
      <li><strong>Latar diisi warna muda</strong> sesuai bab, bukan putih.</li>
      <li><strong>Keluarga Indonesia</strong> — wajah, pakaian, rumah. Ada yang berhijab,
        ada yang tidak. Ada keluarga lengkap, orang tua tunggal, kakek-nenek.</li>
      <li><strong>Suasana tenang dan sehari-hari.</strong> Dapur, ambang pintu, tepi
        tempat tidur. Bukan keluarga iklan yang serba sempurna.</li>
      <li><strong>Hindari</strong> gambar anak yang tampak nakal, orang tua yang membentak,
        garis hitam tebal, dan gaya blob geometris yang sedang umum.</li>
      <li>Yang paling penting: orang tua yang membuka bab ini mungkin baru saja membentak
        anaknya dan merasa bersalah. Setiap gambar harus ramah kepada orang itu.</li>
    </ul>
  </div>

  <footer>
    Colours and chapter text in this brief are generated directly from the app, so they
    match what ships. Questions: yayasanceria.id@gmail.com
  </footer>
</div>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT}  ({OUT.stat().st_size / 1024:.0f} kB)")
    print(f"  chapters: {len(g['chapters'])}  fonts embedded: {bool(fonts)}")


if __name__ == "__main__":
    main()
