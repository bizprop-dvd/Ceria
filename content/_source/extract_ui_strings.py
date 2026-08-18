"""Extract the bilingual UI strings that live inline in the React components.

Most translatable text lives in content/*.json, but the app chrome (buttons,
headings, empty states) is written inline as `lang === 'en' ? '…' : '…'`.
Those pairs still need review, so this pulls them out into a flat list.

Usage:  python3 content/_source/extract_ui_strings.py
Output: content/_source/ui_strings.json
"""

import json
import pathlib
import re

SRC = pathlib.Path("src")
OUT = pathlib.Path("content/_source/ui_strings.json")

# `lang === 'en' ? <a> : <b>` where each side is a single- or double-quoted
# string or a backtick template. Spans newlines, since the ternary is often
# wrapped by the formatter.
QUOTED = r"""(?:'(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*"|`(?:[^`\\]|\\.)*`)"""
PAIR = re.compile(
    r"lang\s*===\s*'en'\s*\?\s*(" + QUOTED + r")\s*:\s*(" + QUOTED + r")",
    re.DOTALL,
)
# Bilingual object literals, e.g. `{ en: 'Today', id: 'Hari Ini' }` — used for
# tab labels, mood words and role names.
OBJ = re.compile(r"\ben:\s*(" + QUOTED + r")\s*,\s*id:\s*(" + QUOTED + r")")


def unquote(s: str) -> str:
    body = s[1:-1]
    return body.replace("\\'", "'").replace('\\"', '"').replace("\\`", "`")


def main() -> None:
    rows = []
    for path in sorted(SRC.rglob("*.tsx")) + sorted(SRC.rglob("*.ts")):
        text = path.read_text(encoding="utf-8")
        for m in sorted(
            [*PAIR.finditer(text), *OBJ.finditer(text)], key=lambda x: x.start()
        ):
            en, id_ = unquote(m.group(1)), unquote(m.group(2))
            # Skip pairs that only forward a variable, e.g. `m.en : m.id`.
            if not en.strip() or not id_.strip():
                continue
            rows.append(
                {
                    "file": str(path),
                    "line": text[: m.start()].count("\n") + 1,
                    "en": en,
                    "id": id_,
                }
            )

    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")
    print(f"  ui strings: {len(rows)}")
    files = sorted({r['file'] for r in rows})
    print(f"  files: {len(files)}")


if __name__ == "__main__":
    main()
