import json

def f(en, id, t="longtext"):
    return {"type": t, "label": {"en": en, "id": id}}

def guide(en, id):
    return {"en": en, "id": id}

# Faithful phone adaptation of tools 5-12 from Ceria_Family_Toolkit_COMPLETE.pdf
# (print charts/grids become free-text fields; word banks/rules become a guide).
TOOLS = {
    5: {
        "fields": [
            f("The behavior I want to address", "Perilaku yang ingin saya tangani"),
            f("The likely need or feeling underneath it", "Kebutuhan atau perasaan yang mungkin di baliknya"),
            f("The boundary (what I will and won't allow)", "Batasan (apa yang saya izinkan dan tidak)"),
            f("My consistent response — every time", "Respons saya yang konsisten — setiap kali"),
            f("How I will repair if I lose my calm", "Cara saya memperbaiki jika saya hilang kendali"),
        ],
        "guide": guide(
            ["I commit to this plan for one week."],
            ["Saya berkomitmen pada rencana ini selama satu minggu."],
        ),
    },
    6: {
        "guide": guide(
            [
                "A feelings vocabulary to build together, one word at a time:",
                "MAD: frustrated · annoyed · furious · left out · jealous · embarrassed",
                "SAD: lonely · disappointed · hurt · missing · tired · heavy",
                "SCARED: worried · nervous · unsafe · shy · overwhelmed · uncertain",
                "GLAD: proud · calm · loved · excited · playful · grateful",
            ],
            [
                "Kosakata perasaan untuk dibangun bersama, satu kata setiap kali:",
                "MARAH: kesal · jengkel · murka · tersisih · cemburu · malu",
                "SEDIH: kesepian · kecewa · terluka · kangen · lelah · berat hati",
                "TAKUT: khawatir · gugup · tidak aman · malu-malu · kewalahan · ragu",
                "SENANG: bangga · tenang · disayangi · bersemangat · ceria · bersyukur",
            ],
        ),
        "fields": [
            f("Today my child felt… and I named it by saying…",
              "Hari ini anak saya merasa… dan saya menamainya dengan…"),
        ],
    },
    7: {
        "guide": guide(
            ["Common examples: morning rush · bedtime · screens off · homework start · mealtimes"],
            ["Contoh umum: transisi pagi · waktu tidur · mematikan layar · mulai PR · waktu makan"],
        ),
        "fields": [
            f("The friction point I'm choosing", "Titik gesekan yang saya pilih"),
            f("What actually happens (concrete, no judgment)", "Apa yang sebenarnya terjadi (konkret, tanpa menghakimi)"),
            f("My best guess at the root cause", "Dugaan terbaik saya tentang akar masalahnya"),
            f("One simple change I'll test", "Satu perubahan sederhana yang akan saya coba"),
            f("7-day follow-up: did the change help? (note each day)", "Tinjauan 7 hari: apakah perubahan ini membantu? (catat tiap hari)"),
        ],
    },
    8: {
        "guide": guide(
            ["For each incident, note four things:",
             "When · Antecedent (what came before) · Behavior (what happened) · Consequence (what came after)"],
            ["Untuk setiap kejadian, catat empat hal:",
             "Kapan · Pemicu (apa yang mendahului) · Perilaku (apa yang terjadi) · Akibat (apa yang terjadi setelahnya)"],
        ),
        "fields": [
            f("Incident log — track the same behavior across ~6 incidents (When → Antecedent → Behavior → Consequence)",
              "Catatan kejadian — lacak perilaku yang sama dalam ~6 kejadian (Kapan → Pemicu → Perilaku → Akibat)"),
            f("The pattern I notice + one change for next week", "Pola yang saya lihat + satu perubahan minggu depan"),
        ],
    },
    9: {
        "fields": [
            f("Child's name & age", "Nama & usia anak", "text"),
            f("The one responsibility (small, doable, daily)", "Satu tanggung jawab (kecil, bisa dilakukan, harian)"),
            f("7-day check-in with an encouragement note for each day (Mon–Sun)",
              "Catatan 7 hari dengan pesan apresiasi setiap hari (Sen–Min)"),
            f("How did this responsibility change my child this week?",
              "Bagaimana tanggung jawab ini mengubah anak saya minggu ini?"),
        ],
    },
    10: {
        "guide": guide(
            ["Rules: phone away · child chooses the activity · no teaching, no correcting · just be with them."],
            ["Aturan: HP disimpan · anak yang memilih kegiatan · tidak mengajari, tidak menegur · hanya hadir bersama."],
        ),
        "fields": [
            f("7-day log — what we did, child's mood after, my mood after (Mon–Sun)",
              "Catatan 7 hari — yang kami lakukan, suasana hati anak & saya setelahnya (Sen–Min)"),
            f("What kind of moments lit my child up most?",
              "Momen seperti apa yang paling membuat anak saya bersinar?"),
        ],
    },
    11: {
        "guide": guide(
            ["Rate each pressure 1–5, then name one compassionate adjustment for it."],
            ["Beri nilai tiap tekanan 1–5, lalu sebutkan satu penyesuaian yang penuh kasih."],
        ),
        "fields": [
            f("Work / load — pressure (1–5) and one compassionate adjustment", "Pekerjaan / beban kerja — tekanan (1–5) dan satu penyesuaian"),
            f("Marriage / partnership — pressure (1–5) and one adjustment", "Pernikahan / pasangan — tekanan (1–5) dan satu penyesuaian"),
            f("Finances — pressure (1–5) and one adjustment", "Keuangan — tekanan (1–5) dan satu penyesuaian"),
            f("Extended family — pressure (1–5) and one adjustment", "Keluarga besar — tekanan (1–5) dan satu penyesuaian"),
            f("Child's needs / behavior — pressure (1–5) and one adjustment", "Kebutuhan / perilaku anak — tekanan (1–5) dan satu penyesuaian"),
            f("Health / sleep — pressure (1–5) and one adjustment", "Kesehatan / tidur — tekanan (1–5) dan satu penyesuaian"),
            f("My one anchor practice this season", "Satu kebiasaan utama yang akan saya pegang musim ini"),
        ],
    },
    12: {
        "fields": [
            f("Month & Year", "Bulan & Tahun", "text"),
            f("1. What improved this month?", "1. Apa yang membaik bulan ini?"),
            f("2. What kept repeating — what cycle didn't shift?", "2. Apa yang terus berulang — siklus apa yang belum berubah?"),
            f("3. What triggered me most, and what was underneath it?", "3. Apa yang paling memicu saya, dan apa yang ada di baliknya?"),
            f("4. What helped my child most this month?", "4. Apa yang paling membantu anak saya bulan ini?"),
            f("5. One change I'll carry into next month.", "5. Satu perubahan yang akan saya bawa ke bulan depan."),
        ],
        "guide": guide(
            ["Steady, daily love shapes more than any single perfect day."],
            ["Cinta yang stabil setiap hari membentuk lebih banyak hal daripada satu hari yang sempurna."],
        ),
    },
}

t = json.load(open("/home/user/Ceria/content/toolkit.json"))
for tool in t["tools"]:
    n = tool["number"]
    if n in TOOLS:
        spec = TOOLS[n]
        tool.pop("_needsFields", None)
        if "guide" in spec:
            tool["guide"] = spec["guide"]
        tool["fields"] = spec["fields"]

t["meta"]["note"] = ("All 12 tools are complete, adapted for the app from "
                     "Ceria_Family_Toolkit_COMPLETE.pdf. Print charts/grids are rendered as "
                     "free-text fields; reference word banks and rules appear in each tool's guide. "
                     "Tools 1-4 are free; 5-12 unlock with ceria_full_unlock.")

json.dump(t, open("/home/user/Ceria/content/toolkit.json", "w"), ensure_ascii=False, indent=2)
left = [x["number"] for x in t["tools"] if x.get("_needsFields")]
print("tools:", len(t["tools"]), "| _needsFields remaining:", left)
for x in t["tools"]:
    print(f"  tool {x['number']}: {len(x.get('fields',[]))} fields, guide={'yes' if x.get('guide') else 'no'}")
