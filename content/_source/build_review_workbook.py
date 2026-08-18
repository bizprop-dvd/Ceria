"""Build the bilingual EN/ID review workbook.

Every translatable string in the app — the 365-day guide, the framework grids,
the guidebook, the toolkit, the diary, and the UI chrome that lives inline in
the React components — is emitted side by side with its English source, plus
two empty columns for the reviewer to write in.

Each row carries a stable key (column A) so corrections can be read back in
mechanically. Do not edit or reorder that column.

Usage:  python3 content/_source/build_review_workbook.py
Output: content/_source/out/Ceria_review_EN_ID.xlsx
"""

import json
import pathlib

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = pathlib.Path(".")
OUT = ROOT / "content/_source/out/Ceria_review_EN_ID.xlsx"

FONT = "Arial"
INK = "1F2937"          # ceria dark
BLUE = "2E4FA3"         # ceria blue
PINK = "E91E80"         # ceria pink
CREAM = "FAF6EE"        # ceria cream
CREAM_DEEP = "F2E9D9"
GRAY = "6B7280"
EDIT_FILL = "FFFDF0"    # the two columns the reviewer types into

HEAD = ["Kode / Key", "Bagian / Where", "English", "Bahasa Indonesia (sekarang)",
        "PERBAIKAN / YOUR REVISION", "Catatan / Notes"]


def load(name):
    return json.loads((ROOT / "content" / name).read_text(encoding="utf-8"))


# --------------------------------------------------------------------------
# Row collection. Each collector returns (sheet_title, subtitle, rows) where a
# row is [key, where, en, id].
# --------------------------------------------------------------------------

FIELD_LABEL = {
    "title": "Judul / Title",
    "teaching": "Bacaan / Teaching",
    "inPractice": "Dalam praktik / In practice",
    "practice": "Latihan / Practice",
    "reflection": "Refleksi / Reflection",
    "script": "Kalimat / Script",
}


def daily_rows(d):
    ch_title = {c["number"]: c for c in load("guidebook.json")["chapters"]}
    rows = []
    for day in d["days"]:
        n, c = day["day"], day["chapter"]
        where_base = f"Bab {c} · Hari {n} — {ch_title[c]['title']['id']}"
        for f in ("title", "teaching", "inPractice", "practice", "reflection", "script"):
            rows.append(
                [f"daily:{n}:{f}", f"{where_base}\n{FIELD_LABEL[f]}", day[f]["en"], day[f]["id"]]
            )
    return rows


def framework_rows(d):
    rows = []
    for day in d["days"]:
        fw = day.get("framework")
        if not fw:
            continue
        n = day["day"]
        w = f"Hari {n} — tabel / grid"
        rows.append([f"fw:{n}:title", f"{w}\nJudul tabel", fw["title"]["en"], fw["title"]["id"]])
        rows.append([f"fw:{n}:note", f"{w}\nCatatan tabel", fw["note"]["en"], fw["note"]["id"]])
        for i, e in enumerate(fw["entries"]):
            label = f"{w}\nKartu {i + 1}"
            rows.append([f"fw:{n}:{i}:name", f"{label} — Nama", e["name"]["en"], e["name"]["id"]])
            for j, tag in enumerate(e["tags"]):
                rows.append([f"fw:{n}:{i}:tag:{j}", f"{label} — Label", tag["en"], tag["id"]])
            rows.append([f"fw:{n}:{i}:looksLike", f"{label} — Bentuknya",
                         e["looksLike"]["en"], e["looksLike"]["id"]])
            rows.append([f"fw:{n}:{i}:outcome", f"{label} — Hasilnya",
                         e["outcome"]["en"], e["outcome"]["id"]])
    return rows


def exercise_rows(d):
    rows = []
    for x in d["weeklyExercises"]:
        rows.append([f"weekly:{x['n']}", f"Latihan mingguan {x['n']} (hari {x['range'][0]}–{x['range'][1]})",
                     x["text"]["en"], x["text"]["id"]])
    for x in d["monthlyReviews"]:
        rows.append([f"monthly:{x['n']}", f"Tinjauan bulanan {x['n']} (hari {x['range'][0]}–{x['range'][1]})",
                     x["text"]["en"], x["text"]["id"]])
    return rows


def guidebook_rows(g):
    labels = {"title": "Judul bab", "principle": "Prinsip", "why": "Mengapa",
              "inPractice": "Dalam praktik", "reflection": "Refleksi"}
    rows = []
    for c in g["chapters"]:
        n = c["number"]
        w = f"Bab {n}"
        for k, lab in labels.items():
            if c.get(k):
                rows.append([f"guide:{n}:{k}", f"{w}\n{lab}", c[k]["en"], c[k]["id"]])
        dp = c.get("dailyPractices")
        if dp:
            for i, (en, id_) in enumerate(zip(dp["en"], dp["id"])):
                rows.append([f"guide:{n}:dailyPractices:{i}", f"{w}\nPraktik harian {i + 1}", en, id_])
    return rows


def toolkit_rows(t):
    rows = []
    m = t["meta"]
    rows.append(["tool:meta:transparencyLine", "Toolkit — baris transparansi",
                 m["transparencyLine"]["en"], m["transparencyLine"]["id"]])
    for x in t["tools"]:
        n = x["number"]
        w = f"Alat {n}"
        rows.append([f"tool:{n}:title", f"{w}\nJudul", x["title"]["en"], x["title"]["id"]])
        rows.append([f"tool:{n}:purpose", f"{w}\nTujuan", x["purpose"]["en"], x["purpose"]["id"]])
        rep = x.get("repeat") or {}
        if rep.get("nameLabel"):
            rows.append([f"tool:{n}:repeat:nameLabel", f"{w}\nLabel nama",
                         rep["nameLabel"]["en"], rep["nameLabel"]["id"]])
        guide = x.get("guide")
        if guide:
            for i, (en, id_) in enumerate(zip(guide["en"], guide["id"])):
                rows.append([f"tool:{n}:guide:{i}", f"{w}\nPanduan {i + 1}", en, id_])
        for i, f in enumerate(x.get("fields") or []):
            rows.append([f"tool:{n}:field:{i}", f"{w}\nKolom {i + 1}",
                         f["label"]["en"], f["label"]["id"]])
        for i, f in enumerate(x.get("summaryFields") or []):
            rows.append([f"tool:{n}:summaryField:{i}", f"{w}\nKolom ringkasan {i + 1}",
                         f["label"]["en"], f["label"]["id"]])
    return rows


def diary_rows(dw):
    rows = []
    m = dw["meta"]
    for i, p in enumerate(m["dailyPrompts"]):
        rows.append([f"diary:dailyPrompt:{i}", f"Pertanyaan harian {i + 1}", p["en"], p["id"]])
    for ed in ("combined", "solo"):
        name = "Orang tua" if ed == "combined" else "Orang tua tunggal"
        for i, p in enumerate(m["debrief"][ed]):
            rows.append([f"diary:debrief:{ed}:{i}", f"Tinjauan mingguan — {name} {i + 1}",
                         p["en"], p["id"]])
    for wk in dw["weeks"]:
        n = wk["week"]
        w = f"Minggu {n} (bab {wk['chapter']})"
        for k, lab in (("theme", "Tema"), ("principle", "Prinsip"), ("weekIntent", "Niat minggu ini")):
            rows.append([f"diary:week:{n}:{k}", f"{w}\n{lab}", wk[k]["en"], wk[k]["id"]])
        for ed in ("combined", "solo"):
            name = "Orang tua" if ed == "combined" else "Orang tua tunggal"
            s = wk["sundayReflection"][ed]
            rows.append([f"diary:week:{n}:sunday:{ed}", f"{w}\nRefleksi Minggu — {name}",
                         s["en"], s["id"]])
    return rows


def intro_rows(intro):
    rows = []
    for ed in ("combined", "solo"):
        name = "Orang tua" if ed == "combined" else "Orang tua tunggal"
        rows.append([f"intro:welcome:{ed}", f"Sambutan — {name}",
                     intro["welcome"][ed]["en"], intro["welcome"][ed]["id"]])
        for i, h in enumerate(intro["howToUse"][ed]):
            rows.append([f"intro:howToUse:{ed}:{i}:title", f"Cara memakai — {name} {i + 1}\nJudul",
                         h["title"]["en"], h["title"]["id"]])
            rows.append([f"intro:howToUse:{ed}:{i}:body", f"Cara memakai — {name} {i + 1}\nIsi",
                         h["body"]["en"], h["body"]["id"]])
    s = intro["settingUp"]
    rows.append(["intro:settingUp:intro", "Sebelum memulai — pengantar", s["intro"]["en"], s["intro"]["id"]])
    for ed in ("combined", "solo"):
        name = "Orang tua" if ed == "combined" else "Orang tua tunggal"
        for i, p in enumerate(s[ed]["prompts"]):
            rows.append([f"intro:settingUp:{ed}:{i}", f"Sebelum memulai — {name} {i + 1}",
                         p["en"], p["id"]])
    return rows


def ui_rows(ui):
    """One row per distinct EN/ID pair, naming every place that pair appears.

    Identical pairs are collapsed so the reviewer answers each wording once.
    The row is keyed to the first location, but the others are listed in
    column B — apply_review_workbook.py reports them, and a correction has to
    reach all of them or the same English renders two ways in the app.
    """
    groups = {}
    for r in ui:
        groups.setdefault((r["en"], r["id"]), []).append(r)
    rows = []
    for (en, id_), hits in groups.items():
        first = hits[0]
        where = "\n".join(
            h["file"].replace("src/", "").replace(".tsx", "").replace(".ts", "") for h in hits
        )
        extra = f"  (× {len(hits)})" if len(hits) > 1 else ""
        rows.append(
            [f"ui:{first['file']}:{first['line']}", f"Antarmuka / UI{extra}\n{where}", en, id_]
        )
    return rows


# --------------------------------------------------------------------------
# Writing
# --------------------------------------------------------------------------

thin = Side(style="thin", color="D9D2C4")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)


def write_sheet(wb, title, subtitle, rows):
    ws = wb.create_sheet(title)
    ws.sheet_properties.tabColor = BLUE

    ws["A1"] = subtitle
    ws["A1"].font = Font(name=FONT, size=11, bold=True, color=BLUE)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(HEAD))
    ws.row_dimensions[1].height = 20

    for i, h in enumerate(HEAD, start=1):
        c = ws.cell(row=2, column=i, value=h)
        c.font = Font(name=FONT, size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=BLUE if i < 5 else PINK)
        c.alignment = Alignment(vertical="center", wrap_text=True)
        c.border = BORDER
    ws.row_dimensions[2].height = 30

    for r, row in enumerate(rows, start=3):
        for i, v in enumerate(row, start=1):
            c = ws.cell(row=r, column=i, value=v)
            c.font = Font(name=FONT, size=10, color=GRAY if i <= 2 else INK)
            c.alignment = Alignment(vertical="top", wrap_text=True)
            c.border = BORDER
        for i in (5, 6):
            c = ws.cell(row=r, column=i)
            c.fill = PatternFill("solid", fgColor=EDIT_FILL)
            c.font = Font(name=FONT, size=10, color=PINK)
            c.alignment = Alignment(vertical="top", wrap_text=True)
            c.border = BORDER

    for col, width in zip("ABCDEF", (26, 30, 62, 62, 46, 26)):
        ws.column_dimensions[col].width = width
    ws.freeze_panes = "C3"
    ws.auto_filter.ref = f"A2:{get_column_letter(len(HEAD))}{len(rows) + 2}"
    return len(rows)


def write_readme(wb, sections):
    ws = wb.create_sheet("Baca dulu", 0)
    ws.sheet_properties.tabColor = PINK
    ws.column_dimensions["A"].width = 34
    for col, w in zip("BCDE", (16, 16, 16, 46)):
        ws.column_dimensions[col].width = w

    ws["A1"] = "Ceria — tinjauan Bahasa Indonesia"
    ws["A1"].font = Font(name=FONT, size=16, bold=True, color=BLUE)
    ws["A2"] = "Ceria — Indonesian review pack"
    ws["A2"].font = Font(name=FONT, size=11, italic=True, color=GRAY)

    how = [
        ("Cara memakai berkas ini", "How to use this file", True),
        ("1. Baca kolom C (English) untuk konteks, lalu kolom D (Bahasa Indonesia sekarang).",
         "Read column C for context, then column D for the current Indonesian.", False),
        ("2. Kalau kolom D sudah bagus, biarkan saja. Tidak perlu diapa-apakan.",
         "If column D is already good, leave it. Nothing to do.", False),
        ("3. Kalau perlu diperbaiki, tulis versi barunya di kolom E. Jangan ubah kolom D.",
         "If it needs fixing, write the new version in column E. Do not edit column D.", False),
        ("4. Kolom F untuk catatan bebas — alasan, keraguan, pertanyaan.",
         "Column F is for free notes — reasoning, doubts, questions.", False),
        ("5. Jangan mengubah atau memindahkan kolom A (Kode). Kode itu yang dipakai untuk memasukkan perbaikan kembali ke aplikasi.",
         "Never edit or reorder column A. Those keys are what put your edits back into the app.", False),
        ("", "", False),
        ("Boleh dikerjakan sedikit-sedikit. Tidak harus selesai sekaligus, dan tidak harus urut.",
         "It can be done in pieces. It does not need finishing in one go, or in order.", False),
        ("Mulai dari lembar yang paling terlihat pemakai: Antarmuka, Diari, lalu Panduan.",
         "Start where users look most: Antarmuka (UI), Diari, then Panduan.", False),
    ]
    r = 4
    for id_text, en_text, is_head in how:
        ws.cell(row=r, column=1, value=id_text).font = Font(
            name=FONT, size=12 if is_head else 10, bold=is_head, color=BLUE if is_head else INK)
        ws.cell(row=r, column=1).alignment = Alignment(vertical="top", wrap_text=True)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
        c = ws.cell(row=r, column=5, value=en_text)
        c.font = Font(name=FONT, size=9, italic=True, color=GRAY)
        c.alignment = Alignment(vertical="top", wrap_text=True)
        ws.row_dimensions[r].height = 28 if id_text and not is_head else 20
        r += 1

    r += 1
    ws.cell(row=r, column=1, value="Isi berkas / What is in here").font = Font(
        name=FONT, size=12, bold=True, color=BLUE)
    r += 1
    heads = ["Lembar / Sheet", "Baris / Rows", "Prioritas", "", "Keterangan"]
    for i, h in enumerate(heads, start=1):
        c = ws.cell(row=r, column=i, value=h)
        c.font = Font(name=FONT, size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=BLUE)
        c.alignment = Alignment(vertical="center", wrap_text=True)
        c.border = BORDER
    for name, count, note, priority in sections:
        r += 1
        ws.cell(row=r, column=1, value=name).font = Font(name=FONT, size=10, color=INK)
        ws.cell(row=r, column=2, value=count).font = Font(name=FONT, size=10, color=INK)
        c = ws.cell(row=r, column=3, value=priority)
        c.font = Font(name=FONT, size=10, bold=priority == "1 — mulai di sini", color=PINK)
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=4)
        ws.cell(row=r, column=5, value=note).font = Font(name=FONT, size=9, color=GRAY)
        ws.cell(row=r, column=5).alignment = Alignment(vertical="top", wrap_text=True)
        for i in range(1, 6):
            ws.cell(row=r, column=i).border = BORDER
    r += 1
    ws.cell(row=r, column=1, value="TOTAL").font = Font(name=FONT, size=10, bold=True, color=BLUE)
    ws.cell(row=r, column=2, value=sum(n for _, n, _, _ in sections)).font = Font(
        name=FONT, size=10, bold=True, color=BLUE)
    for i in range(1, 6):
        ws.cell(row=r, column=i).border = BORDER
        ws.cell(row=r, column=i).fill = PatternFill("solid", fgColor=CREAM_DEEP)


def collect():
    """The whole review pack as (sheet, subtitle, rows, note, priority) tuples."""
    d = load("daily.json")
    g = load("guidebook.json")
    t = load("toolkit.json")
    dw = load("diary_weeks.json")
    intro = load("diary_intro.json")
    ui = json.loads((ROOT / "content/_source/ui_strings.json").read_text(encoding="utf-8"))

    P1, P2, P3, DONE = "1 — mulai di sini", "2", "3", "sudah selesai"
    plan = [
        ("Antarmuka", "Antarmuka aplikasi — tombol, judul layar, pesan. Paling sering dilihat pemakai.",
         ui_rows(ui), "Tombol dan label di dalam aplikasi. Pendek-pendek, cepat dikerjakan.", P1),
        ("Diari", "Diari — tema mingguan, prinsip, niat, refleksi hari Minggu.",
         diary_rows(dw), "52 minggu, dua edisi.", P1),
        ("Panduan", "Panduan — 12 bab: judul, prinsip, alasan, praktik.",
         guidebook_rows(g), "Ringkasan tiap bab.", P2),
        ("Alat", "Alat — 12 perangkat kerja: judul, tujuan, label kolom.",
         toolkit_rows(t), "Judul kolom yang diisi orang tua.", P2),
        ("Tabel", "Tabel perbandingan di dalam bacaan harian (13 tabel).",
         framework_rows(d), "Kartu perbandingan, mis. empat gaya pengasuhan.", P2),
        ("Latihan", "Latihan mingguan (52) dan tinjauan bulanan (12).",
         exercise_rows(d), "Diambil apa adanya dari naskah pendiri.", P3),
        ("Harian", "Bacaan harian — 365 hari × 6 bagian. Bagian terbesar.",
         daily_rows(d), "Bagian terbesar. Boleh disaring per bab lewat kolom B.", P3),
        ("Pembuka diari", "Pembuka diari — sudah ditinjau. Ada di sini hanya sebagai rujukan.",
         intro_rows(intro), "Sudah ditinjau. Tidak perlu dikerjakan lagi.", DONE),
    ]

    return plan


def main():
    wb = Workbook()
    wb.remove(wb.active)
    sections = []
    for title, subtitle, rows, note, priority in collect():
        n = write_sheet(wb, title, subtitle, rows)
        sections.append((title, n, note, priority))
    write_readme(wb, sections)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"Wrote {OUT}")
    for name, n, _, _ in sections:
        print(f"  {name:<16} {n:>5} rows")
    print(f"  {'TOTAL':<16} {sum(n for _, n, _, _ in sections):>5} rows")


if __name__ == "__main__":
    main()
