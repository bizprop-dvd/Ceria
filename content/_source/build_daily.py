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
import os
import glob
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MANUSCRIPT = os.path.join(HERE, "pdf", "ceria_365_content.json")
OUT = os.path.join(ROOT, "content", "daily.json")
PROSE_DIR = os.path.join(HERE, "prose")

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
            "text": prose.get(f"week{w['n']}") or {"en": _strip_prefix(w["text"]), "id": ""},
        }
        for w in src["weekly_exercises"]
    ]
    monthly = [
        {
            "n": m["n"],
            "range": m["range"],
            "text": prose.get(f"month{m['n']}") or {"en": _strip_prefix(m["text"]), "id": ""},
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

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {OUT}")
    print(f"  days: {len(days)}  authored: {authored}  draft: {len(days) - authored}")
    print(f"  weekly: {len(weekly)}  monthly: {len(monthly)}")


def _complete(p):
    fields = ("title", "teaching", "inPractice", "practice", "reflection", "script")
    return bool(p) and all(
        p.get(f, {}).get("en", "").strip() and p.get(f, {}).get("id", "").strip()
        for f in fields
    )


def _strip_prefix(text):
    """Drop the redundant 'Week 11: ' / 'Month 6 review: ' prefix; the UI shows it."""
    for sep in (": ",):
        head, _, tail = text.partition(sep)
        if head.lower().startswith(("week", "month")) and tail:
            return tail
    return text


if __name__ == "__main__":
    main()
