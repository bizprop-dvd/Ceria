"""Split content/daily.json into an index plus one file per chapter.

The 365-day guide is 957 kB of prose. Bundled whole it made a 1.16 MB
JavaScript file that every parent downloads on install and parses on every
cold start — on the cheap Android phones this app is written for, that is a
second of blank screen before anything appears.

Almost none of it is needed at startup. The screens that open first show
titles, counts, and the rotating line of advice; the full teaching for a day
is only needed once someone taps into that day. So:

  content/daily/index.json   meta, chapters, the weekly and monthly exercises,
                             and a short record per day — number, chapter,
                             title, draft flag, and the reflection and script
                             lines the Today screen rotates through.

  content/daily/ch01.json …  the full text of that chapter's days, loaded when
  content/daily/ch12.json    a reader opens one.

Run after build_daily.py. Both outputs are generated; daily.json stays the
source of truth and is still the file the review pipeline reads.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(ROOT, "content", "daily.json")
OUT_DIR = os.path.join(ROOT, "content", "daily")

# Kept in the index because a screen needs them before any chapter is opened.
SUMMARY_FIELDS = ("day", "chapter", "title", "draft", "reflection", "script")


def main():
    with open(SRC, encoding="utf-8") as f:
        data = json.load(f)

    os.makedirs(OUT_DIR, exist_ok=True)

    index = {
        "meta": data["meta"],
        "chapters": data["chapters"],
        "weeklyExercises": data["weeklyExercises"],
        "monthlyReviews": data["monthlyReviews"],
        "days": [{k: d[k] for k in SUMMARY_FIELDS if k in d} for d in data["days"]],
    }
    _write(os.path.join(OUT_DIR, "index.json"), index)

    by_chapter = {}
    for day in data["days"]:
        by_chapter.setdefault(day["chapter"], []).append(day)

    for number in sorted(by_chapter):
        # Drafts carry no prose, so they only ever need to exist in the index.
        days = [d for d in by_chapter[number] if not d.get("draft")]
        _write(os.path.join(OUT_DIR, f"ch{number:02d}.json"), {"days": days})

    _report(index, by_chapter)


def _write(path, payload):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")


def _report(index, by_chapter):
    size = lambda name: os.path.getsize(os.path.join(OUT_DIR, name)) / 1024
    print(f"Wrote {OUT_DIR}/")
    print(f"  index.json  {size('index.json'):7.0f} kB   {len(index['days'])} days")
    for number in sorted(by_chapter):
        name = f"ch{number:02d}.json"
        authored = sum(1 for d in by_chapter[number] if not d.get("draft"))
        print(f"  {name}   {size(name):7.0f} kB   {authored} days")
    whole = os.path.getsize(SRC) / 1024
    largest = max(size(f"ch{n:02d}.json") for n in by_chapter)
    print(f"  startup was {whole:.0f} kB, is now {size('index.json'):.0f} kB")
    print(f"  largest chapter loaded on demand: {largest:.0f} kB")


if __name__ == "__main__":
    main()
