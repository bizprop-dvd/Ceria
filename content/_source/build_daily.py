"""Build content/daily.json — the 365-day companion guide.

Source: the founder's ceria_365_content.json (v3) manuscript.

WHAT IS TAKEN VERBATIM FROM THE MANUSCRIPT
  - the 365 day titles and their chapter assignment / day ranges
  - the 52 weekly exercises and 12 monthly reviews
  - the per-day `reference` (further reading) and `support` (safeguarding line)

WHAT IS NOT TAKEN
  The manuscript's teaching / in_practice / practice / reflection / script
  bodies are template-generated: 362 of 365 days slot the day title verbatim
  into a fixed sentence, and whole chapters share a single reflection question.
  Those fields are left empty here and authored per day in the prose modules
  (content/_source/prose/chNN.py), grounded in the founder's own guidebook
  chapters, toolkit and diary.

Run:  python3 content/_source/build_daily.py
"""

import json
import sys
import os
import glob
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MANUSCRIPT = os.path.join(HERE, "pdf", "ceria_365_content.json")
OUT = os.path.join(ROOT, "content", "daily.json")
PROSE_DIR = os.path.join(HERE, "prose")
# Indonesian corrections coming back from the reviewer's workbook. Applied last
# so they survive a rebuild without anyone hand-editing the prose modules.
OVERRIDES = os.path.join(HERE, "id_overrides.json")

sys.path.insert(0, HERE)
from exercises_id import BY_EN as _EX  # noqa: E402

# Keyed by the English text with whitespace normalised, since the source
# strings are wrapped across lines in both places.
EXERCISES_ID = {" ".join(k.split()): v for k, v in _EX.items()}

# Bilingual safeguarding line. The manuscript ships one English sentence on
# 250/365 days; we keep its meaning and give it an Indonesian counterpart.
SUPPORT = {
    "en": "Consider professional support if this issue is persistent, worsening, "
          "developmentally unusual, or significantly affecting family life.",
    "id": "Pertimbangkan bantuan profesional jika hal ini terus berlanjut, memburuk, "
          "tidak biasa untuk tahap perkembangan anak, atau sangat memengaruhi kehidupan keluarga.",
}


def load_prose():
    """Load per-chapter authored prose: {day_number: {field: {en, id}}}."""
    prose = {}
    for path in sorted(glob.glob(os.path.join(PROSE_DIR, "ch*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(f"prose_{name}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        got = getattr(mod, "DAYS", {})
        overlap = set(got) & set(prose)
        if overlap:
            raise SystemExit(f"{name}: days already defined elsewhere: {sorted(overlap)}")
        prose.update(got)
    return prose


def main():
    src = json.load(open(MANUSCRIPT, encoding="utf-8"))
    prose = load_prose()

    chapters = [
        {
            "number": c["number"],
            "dayStart": c["day_start"],
            "dayEnd": c["day_end"],
            "dayCount": c["day_count"],
        }
        for c in src["chapters"]
    ]

    days = []
    for d in src["days"]:
        p = prose.get(d["day"], {})
        day = {
            "day": d["day"],
            "chapter": d["chapter"],
            # Title comes from the manuscript (EN); Indonesian is authored.
            "title": p.get("title") or {"en": d["title"], "id": ""},
            "teaching": p.get("teaching") or {"en": "", "id": ""},
            "inPractice": p.get("inPractice") or {"en": "", "id": ""},
            "practice": p.get("practice") or {"en": "", "id": ""},
            "reflection": p.get("reflection") or {"en": "", "id": ""},
            "script": p.get("script") or {"en": "", "id": ""},
            "support": SUPPORT,
            "reference": d["reference"],
            # False once every bilingual field on this day is authored.
            "draft": not _complete(p),
        }
        # Optional teaching grid (e.g. the four parenting styles on day 7).
        if p.get("framework"):
            day["framework"] = p["framework"]
        days.append(day)

    weekly = [
        {
            "n": w["n"],
            "range": w["range"],
            "text": prose.get(f"week{w['n']}") or _exercise(_strip_prefix(w["text"])),
        }
        for w in src["weekly_exercises"]
    ]
    monthly = [
        {
            "n": m["n"],
            "range": m["range"],
            "text": prose.get(f"month{m['n']}") or _exercise(_strip_prefix(m["text"])),
        }
        for m in src["monthly_reviews"]
    ]

    authored = sum(1 for d in days if not d["draft"])
    payload = {
        "meta": {
            "product": "daily",
            "version": 1,
            "totalDays": len(days),
            "freeThroughChapter": 4,
            "authoredDays": authored,
            "note": (
                "365-day companion guide. Day titles, references, weekly exercises and "
                "monthly reviews come from the founder's ceria_365_content.json (v3). "
                "The daily prose is authored per day (see content/_source/prose/) because "
                "the manuscript's bodies were template-generated. Days with draft=true are "
                "not yet authored and are hidden in the app."
            ),
        },
        "chapters": chapters,
        "days": days,
        "weeklyExercises": weekly,
        "monthlyReviews": monthly,
    }

    applied = _apply_overrides(payload)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {OUT}")
    print(f"  days: {len(days)}  authored: {authored}  draft: {len(days) - authored}")
    print(f"  weekly: {len(weekly)}  monthly: {len(monthly)}")
    if applied:
        print(f"  reviewed id overrides applied: {applied}")


def _apply_overrides(payload):
    """Overlay reviewed Indonesian from id_overrides.json onto the built data.

    Keys match the review workbook, e.g. 'daily:212:teaching', 'fw:275:2:outcome',
    'weekly:7'. Only the 'id' side is ever replaced.
    """
    if not os.path.exists(OVERRIDES):
        return 0
    with open(OVERRIDES, encoding="utf-8") as f:
        overrides = json.load(f)

    by_day = {d["day"]: d for d in payload["days"]}
    n = 0
    for key, text in overrides.items():
        p = key.split(":")
        try:
            if p[0] == "daily":
                by_day[int(p[1])][p[2]]["id"] = text
            elif p[0] == "fw":
                fw = by_day[int(p[1])]["framework"]
                if p[2] in ("title", "note"):
                    fw[p[2]]["id"] = text
                else:
                    entry = fw["entries"][int(p[2])]
                    if p[3] == "tag":
                        entry["tags"][int(p[4])]["id"] = text
                    else:
                        entry[p[3]]["id"] = text
            elif p[0] in ("weekly", "monthly"):
                bucket = "weeklyExercises" if p[0] == "weekly" else "monthlyReviews"
                item = next(x for x in payload[bucket] if x["n"] == int(p[1]))
                item["text"]["id"] = text
            else:
                continue
        except (KeyError, IndexError, ValueError, StopIteration):
            print(f"  WARNING: override key not found, skipped: {key}")
            continue
        n += 1
    return n


def _complete(p):
    fields = ("title", "teaching", "inPractice", "practice", "reflection", "script")
    return bool(p) and all(
        p.get(f, {}).get("en", "").strip() and p.get(f, {}).get("id", "").strip()
        for f in fields
    )


def _exercise(en):
    """Pair a manuscript exercise with its Indonesian from exercises_id.py.

    The manuscript is English-only. Without this the 52 weekly exercises and 12
    monthly reviews reach the app with an empty 'id' and Indonesian readers get
    a generic placeholder instead of the exercise.
    """
    id_text = EXERCISES_ID.get(" ".join(en.split()), "")
    if not id_text:
        print(f"  WARNING: no Indonesian for exercise: {en[:60]}…")
    return {"en": en, "id": id_text}


def _strip_prefix(text):
    """Drop the redundant 'Week 11: ' / 'Month 6 review: ' prefix; the UI shows it."""
    for sep in (": ",):
        head, _, tail = text.partition(sep)
        if head.lower().startswith(("week", "month")) and tail:
            return tail
    return text


if __name__ == "__main__":
    main()
