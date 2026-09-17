import re, json

txt = open("toolkit_complete.txt").read()
pages = re.split(r'\n===== PAGE (\d+) =====\n', txt)
P = {pages[i]: pages[i + 1] for i in range(1, len(pages), 2)}

def clean(s):
    s = s.replace('\x7f', ' ')
    s = re.sub(r'[ \t]*\n[ \t]*', ' ', s)   # join wrapped lines
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def bullets(block):
    parts = [clean(b) for b in block.split('\x7f')]
    return [b for b in parts if b]

# marker sets for EN and ID pages
EN = dict(why="Why this matters", practice="In practice", daily="Daily practices",
          tool="Tool to use:", refl="Reflection:", ref="Reference:", head="CHAPTER")
ID = dict(why="Mengapa ini penting", practice="Dalam praktik", daily="Praktik harian",
          tool="Alat yang digunakan:", refl="Refleksi:", ref=None, head="BAB")

def cut(body, start_marker, end_marker):
    a = body.index(start_marker) + len(start_marker)
    b = body.index(end_marker, a) if end_marker else len(body)
    return body[a:b]

def parse_page(page_text, M):
    # start at the big "CHAPTER 0N" / "BAB 0N" heading
    hi = page_text.index('\n' + M['head'] + ' ')
    body = page_text[hi:]
    # first line is "CHAPTER 0N", then title line1, title line2
    lines = body.split('\n')
    # lines[0] == '', lines[1] == 'CHAPTER 0N'
    idx = 1
    title_primary = lines[idx + 1].strip()
    title_secondary = lines[idx + 2].strip()
    # principle: from after title_secondary up to the 'why' marker
    rest = '\n'.join(lines[idx + 3:])
    principle = clean(rest[:rest.index(M['why'])])
    why = clean(cut(rest, M['why'], M['practice']))
    inpractice = clean(cut(rest, M['practice'], M['daily']))
    daily_block = cut(rest, M['daily'], M['tool'])
    daily = bullets(daily_block)
    tool_line = clean(cut(rest, M['tool'], M['refl']))
    refl_end = M['ref'] if (M['ref'] and M['ref'] in rest) else None
    reflection = clean(cut(rest, M['refl'], refl_end))
    reference = clean(rest[rest.index(M['ref']) + len(M['ref']):]) if M['ref'] and M['ref'] in rest else None
    return dict(title_primary=title_primary, title_secondary=title_secondary,
                principle=principle, why=why, inPractice=inpractice, daily=daily,
                tool_line=tool_line, reflection=reflection, reference=reference)

def build_chapter(n):
    en_page = str(8 + (n - 1) * 2)   # ch1->8, ch5->16
    id_page = str(9 + (n - 1) * 2)
    en = parse_page(P[en_page], EN)
    idp = parse_page(P[id_page], ID)
    ch = {
        "number": n,
        "locked": n > 4,
        "title": {"en": en["title_primary"], "id": idp["title_primary"]},
        "principle": {"en": en["principle"], "id": idp["principle"]},
        "why": {"en": en["why"], "id": idp["why"]},
        "inPractice": {"en": en["inPractice"], "id": idp["inPractice"]},
        "dailyPractices": {"en": en["daily"], "id": idp["daily"]},
        "reflection": {"en": en["reflection"], "id": idp["reflection"]},
        "toolRef": n,
    }
    if en["reference"]:
        ch["reference"] = en["reference"]
    return ch

chapters = [build_chapter(n) for n in range(1, 13)]
json.dump(chapters, open("parsed_guidebook.json", "w"), ensure_ascii=False, indent=2)
print("Parsed", len(chapters), "chapters")
