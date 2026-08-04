"""Build a small top-up workbook: only what the reviewer has not seen.

After a review round, some Indonesian changes anyway — new content gets
authored, or a correction reaches a string the reviewer never had in front of
them. Resending the full 3,096-row pack to catch a few dozen lines wastes
everyone's time and loses the reviewer's sense of progress.

This diffs the current content against a returned workbook and emits only the
rows whose Indonesian is now different from what that reviewer saw. Same
columns, same keys, so apply_review_workbook.py reads it back unchanged.

Usage:
    python3 content/_source/build_topup_workbook.py path/to/returned.xlsx
Output:
    content/_source/out/Ceria_review_topup.xlsx
"""

import pathlib
import sys

from openpyxl import Workbook, load_workbook

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_review_workbook as base  # noqa: E402

OUT = pathlib.Path("content/_source/out/Ceria_review_topup.xlsx")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    returned = load_workbook(sys.argv[1])

    # What the reviewer had in front of them: key -> the Indonesian they saw,
    # superseded by their own revision where they wrote one.
    seen = {}
    for ws in returned.worksheets:
        if ws.title == "Baca dulu":
            continue
        for key, _where, _en, id_, revision, *_ in ws.iter_rows(min_row=3, max_col=6, values_only=True):
            if not key:
                continue
            seen[key] = (str(revision).strip() if revision and str(revision).strip() else id_)

    # Every wording they signed off on, wherever it appeared. A string that moved
    # to a different key is still reviewed text and must not be sent back.
    approved = {v for v in seen.values() if v}

    rows = []
    for _title, _subtitle, sheet_rows, _note, _priority in base.collect():
        for row in sheet_rows:
            key, where, en, id_ = row
            if seen.get(key) == id_ or id_ in approved:
                continue
            rows.append([key, where, en, id_])

    if not rows:
        print("Nothing new — the reviewer has seen every current string.")
        return

    wb = Workbook()
    wb.remove(wb.active)
    base.write_sheet(
        wb,
        "Tambahan",
        "Hanya bagian yang belum ditinjau. Cara mengisinya sama: perbaikan di kolom E.",
        rows,
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"Wrote {OUT}")
    print(f"  rows needing review: {len(rows)}")


if __name__ == "__main__":
    main()
