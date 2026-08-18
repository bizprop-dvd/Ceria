# Chapter 5 — Discipline (days 122-151)
#
# Grounded in the founder's guidebook chapter 5 ("Discipline is teaching, not
# punishing. Calm, consistent, connected.") and toolkit tool 5 (Calm Discipline
# Plan).
#
# Through-line: consistency, not intensity, is what changes behaviour.
# This is the first paid chapter — day 122 opens it deliberately.

def d(title, teaching, inPractice, practice, reflection, script, framework=None):
    f = lambda p: {"en": p[0], "id": p[1]}
    out = {
        "title": f(title), "teaching": f(teaching), "inPractice": f(inPractice),
        "practice": f(practice), "reflection": f(reflection), "script": f(script),
    }
    if framework:
        out["framework"] = framework
    return out


def fw(title, note, entries):
    f = lambda p: {"en": p[0], "id": p[1]}
    return {
        "title": f(title), "note": f(note),
        "entries": [
            {"name": f(n), "tags": [f(t) for t in tags], "looksLike": f(l), "outcome": f(o)}
            for (n, tags, l, o) in entries
        ],
    }


DAYS = {
    122: d(
        ("What discipline really means",
         "Apa arti disiplin sebenarnya"),
        ("The word discipline comes from the same root as disciple — it means to teach. "
         "Somewhere along the way it came to mean punish, and that shift causes an "
         "enormous amount of unnecessary difficulty in families.\n\n"
         "If discipline is teaching, then the question in every hard moment changes. Not "
         "\"what punishment fits this?\" but \"what does my child need to learn here, and "
         "what is the most likely way to teach it?\"\n\n"
         "That question usually produces a calmer, smaller, more effective response than "
         "the punishment question does.",
         "Kata disiplin berakar sama dengan kata murid — artinya mengajar. Entah sejak "
         "kapan ia berubah makna menjadi menghukum, dan pergeseran itu menimbulkan sangat "
         "banyak kesulitan yang tak perlu dalam keluarga.\n\n"
         "Jika disiplin adalah mengajar, maka pertanyaan di setiap momen sulit pun berubah. "
         "Bukan \"hukuman apa yang pantas untuk ini?\" melainkan \"apa yang perlu anak saya "
         "pelajari di sini, dan cara apa yang paling mungkin mengajarkannya?\"\n\n"
         "Pertanyaan itu biasanya menghasilkan respons yang lebih tenang, lebih kecil, dan "
         "lebih efektif daripada pertanyaan tentang hukuman."),
        ("The same incident, two questions. \"What's the consequence?\" leads to a "
         "negotiation about fairness. \"What does he need to learn?\" leads to teaching, "
         "which is what you actually wanted.",
         "Kejadian yang sama, dua pertanyaan. \"Apa konsekuensinya?\" berujung pada "
         "tawar-menawar soal keadilan. \"Apa yang perlu dia pelajari?\" berujung pada "
         "pengajaran — yang sebenarnya Anda inginkan."),
        ("Ask \"what needs to be learned here?\" before deciding your response today.",
         "Tanyakan \"apa yang perlu dipelajari di sini?\" sebelum memutuskan respons Anda hari ini."),
        ("Am I trying to teach my child, or to make them pay?",
         "Apakah saya sedang berusaha mengajar anak, atau membuatnya membayar?"),
        ("\"My job here is to teach you, not to make you suffer.\"",
         "\"Tugas Mama/Papa di sini mengajarimu, bukan membuatmu menderita.\""),
    ),
    123: d(
        ("Teaching vs punishing",
         "Mengajar vs menghukum"),
        ("Punishment aims to make the child feel bad enough to stop. Teaching aims to make "
         "the child capable enough to choose differently. They can look similar from the "
         "outside and they produce very different children.\n\n"
         "Punishment has a real short-term effect, which is why it persists. Its costs are "
         "delayed: it teaches concealment, damages the relationship you need for "
         "influence, and never actually supplies the missing skill.",
         "Hukuman bertujuan membuat anak merasa cukup buruk sehingga berhenti. Pengajaran "
         "bertujuan membuat anak cukup mampu untuk memilih berbeda. Keduanya bisa tampak "
         "mirip dari luar dan menghasilkan anak yang sangat berbeda.\n\n"
         "Hukuman punya efek jangka pendek yang nyata, dan karena itulah ia bertahan. "
         "Biayanya tertunda: ia mengajarkan menyembunyikan, merusak hubungan yang Anda "
         "butuhkan untuk berpengaruh, dan tak pernah benar-benar menyediakan keterampilan "
         "yang hilang."),
        ("If a child cannot yet calm down when angry, no punishment will install that "
         "skill. Only practice, modelling and repetition will.",
         "Jika anak belum bisa menenangkan diri saat marah, tak ada hukuman yang akan "
         "memasang keterampilan itu. Hanya latihan, keteladanan, dan pengulangan yang bisa."),
        ("Identify the missing skill behind one behaviour today, and teach that instead.",
         "Kenali keterampilan yang hilang di balik satu perilaku hari ini, dan ajarkan itu."),
        ("Does my response supply the skill my child was missing?",
         "Apakah respons saya menyediakan keterampilan yang belum anak miliki?"),
        ("\"Let's practise what to do instead.\"",
         "\"Ayo latih apa yang bisa dilakukan sebagai gantinya.\""),
        framework=fw(
            ("Punishment or teaching?", "Hukuman atau pengajaran?"),
            ("Both stop the behaviour today. Only one changes what your child can do tomorrow.",
             "Keduanya menghentikan perilaku hari ini. Hanya satu yang mengubah kemampuan anak besok."),
            [
                (("Punishment", "Hukuman"),
                 [("Fast", "Cepat"), ("Costs are delayed", "Biayanya tertunda")],
                 ("Aimed at making the child feel bad enough to stop. Usually imposed from "
                  "outside and unrelated to the act.",
                  "Bertujuan membuat anak merasa cukup buruk agar berhenti. Biasanya "
                  "ditimpakan dari luar dan tak berhubungan dengan perbuatannya."),
                 ("Stops behaviour while you are watching. Teaches concealment, and never "
                  "supplies the missing skill.",
                  "Menghentikan perilaku selama Anda mengawasi. Mengajarkan menyembunyikan, "
                  "dan tak pernah menyediakan keterampilan yang kurang.")),
                (("Teaching", "Pengajaran"),
                 [("Slower", "Lebih lambat"), ("Compounds", "Berbuah menumpuk")],
                 ("Aimed at making the child capable of choosing differently. Connected to "
                  "the act, and usually involves practice or repair.",
                  "Bertujuan membuat anak mampu memilih berbeda. Terhubung dengan "
                  "perbuatannya, dan biasanya melibatkan latihan atau perbaikan."),
                 ("Slower today, and it is the only version that works when you are not in "
                  "the room.",
                  "Lebih lambat hari ini, dan satu-satunya versi yang berhasil saat Anda "
                  "tidak ada di ruangan.")),
            ],
        ),
    ),
    124: d(
        ("Natural consequences",
         "Konsekuensi alami"),
        ("A natural consequence is what happens on its own when you do not intervene: "
         "forgotten coat means cold, forgotten homework means facing the teacher, refusing "
         "dinner means hungry later.\n\n"
         "They teach powerfully because reality is not arguing with the child — it simply "
         "is. Your job is to stay warm and resist the urge to add a lecture on top, which "
         "converts the lesson into a fight about you.",
         "Konsekuensi alami adalah apa yang terjadi dengan sendirinya bila Anda tidak turun "
         "tangan: jaket tertinggal berarti kedinginan, PR terlupa berarti berhadapan dengan "
         "guru, menolak makan malam berarti lapar nanti.\n\n"
         "Ia mengajarkan dengan kuat karena kenyataan tidak sedang berdebat dengan anak — ia "
         "hanya ada. Tugas Anda adalah tetap hangat dan menahan dorongan menambahkan ceramah "
         "di atasnya, yang justru mengubah pelajarannya menjadi pertengkaran tentang Anda."),
        ("\"I told you so\" undoes a natural consequence entirely. Sympathy — \"that's "
         "cold, isn't it\" — leaves the lesson standing.",
         "\"Kan Mama sudah bilang\" membatalkan konsekuensi alami sepenuhnya. Simpati — "
         "\"dingin ya\" — membiarkan pelajarannya tetap berdiri."),
        ("Let one safe natural consequence happen today, and add sympathy instead of a lecture.",
         "Biarkan satu konsekuensi alami yang aman terjadi hari ini, dan tambahkan simpati, "
         "bukan ceramah."),
        ("Where am I protecting my child from a lesson reality would teach better?",
         "Di mana saya melindungi anak dari pelajaran yang justru lebih baik diajarkan kenyataan?"),
        ("\"That's uncomfortable. I'm sorry.\"",
         "\"Itu memang tidak enak. Turut prihatin, ya.\""),
    ),
    125: d(
        ("Logical consequences",
         "Konsekuensi logis"),
        ("When there is no safe natural consequence, a logical one is the next best thing. "
         "It is connected to the behaviour, proportionate, and known in advance where "
         "possible.\n\n"
         "Draw on a whiteboard, clean the whiteboard. Throw the toy, the toy rests for the "
         "afternoon. The link is what does the teaching — an unrelated punishment teaches "
         "only that you are powerful.",
         "Bila tidak ada konsekuensi alami yang aman, konsekuensi logis adalah pilihan "
         "terbaik berikutnya. Ia terhubung dengan perilakunya, sebanding, dan sebisa mungkin "
         "sudah diketahui sejak awal.\n\n"
         "Menggambar di papan, bersihkan papannya. Melempar mainan, mainannya istirahat "
         "sore itu. Keterhubungan itulah yang mengajarkan — hukuman yang tak berhubungan "
         "hanya mengajarkan bahwa Anda berkuasa."),
        ("Taking away a tablet because a child was rude at dinner teaches nothing about "
         "dinner. It teaches that you take things when annoyed.",
         "Menyita tablet karena anak tidak sopan saat makan malam tidak mengajarkan apa pun "
         "tentang makan malam. Ia mengajarkan bahwa Anda menyita sesuatu saat jengkel."),
        ("Make one consequence today genuinely connected to what happened.",
         "Buat satu konsekuensi hari ini yang sungguh terhubung dengan apa yang terjadi."),
        ("Are my consequences connected to the behaviour, or just convenient?",
         "Apakah konsekuensi saya terhubung dengan perilakunya, atau sekadar praktis?"),
        ("\"You spilled it, so you help clean it. That's all.\"",
         "\"Kamu yang menumpahkan, jadi kamu bantu bersihkan. Itu saja.\""),
    ),
    126: d(
        ("When consequences are not helpful",
         "Kapan konsekuensi tidak membantu"),
        ("Consequences are the wrong tool when the behaviour was caused by a missing skill, "
         "an unmet need, or overwhelm. You cannot consequence a child into a capacity they "
         "do not yet have.\n\n"
         "If the same consequence has been applied many times and the behaviour has not "
         "changed, that is definitive evidence it is not the right tool — not evidence "
         "that it needs to be bigger.",
         "Konsekuensi adalah alat yang salah ketika perilakunya disebabkan oleh keterampilan "
         "yang belum ada, kebutuhan yang tak terpenuhi, atau kewalahan. Anda tak bisa "
         "meng-konsekuensi anak sampai memiliki kemampuan yang belum dia punya.\n\n"
         "Jika konsekuensi yang sama sudah diterapkan berkali-kali dan perilakunya tidak "
         "berubah, itu bukti telak bahwa alatnya keliru — bukan bukti bahwa ia perlu diperbesar."),
        ("Escalating a consequence that has already failed five times is the clearest sign "
         "that the problem was never about motivation.",
         "Memperbesar konsekuensi yang sudah gagal lima kali adalah tanda paling jelas bahwa "
         "masalahnya memang tak pernah soal motivasi."),
        ("Find one consequence you keep repeating without effect, and stop using it.",
         "Temukan satu konsekuensi yang terus Anda ulang tanpa hasil, dan berhentilah memakainya."),
        ("What have I been escalating that has never once worked?",
         "Apa yang terus saya perbesar padahal tak pernah sekali pun berhasil?"),
        ("\"This isn't working. Let's try something different.\"",
         "\"Cara ini tidak berhasil. Ayo coba yang lain.\""),
    ),
    127: d(
        ("Why threats fail",
         "Mengapa ancaman gagal"),
        ("A threat is a consequence you have not decided to carry out. Children work this "
         "out quickly, and once they have, threats become background noise.\n\n"
         "The damage is bigger than the moment: every unenforced threat teaches that your "
         "words do not predict your actions, which undermines every future limit you set.",
         "Ancaman adalah konsekuensi yang belum Anda putuskan untuk dijalankan. Anak cepat "
         "memahaminya, dan begitu paham, ancaman menjadi suara latar belaka.\n\n"
         "Kerusakannya lebih besar dari momen itu: setiap ancaman yang tak ditegakkan "
         "mengajarkan bahwa kata-kata Anda tidak meramalkan tindakan Anda, dan itu "
         "melemahkan setiap batas yang Anda tetapkan kelak."),
        ("\"If you do that again we're going home\" — said four times without going home — "
         "has taught the child precisely how much your sentences are worth.",
         "\"Kalau kamu ulangi lagi kita pulang\" — diucapkan empat kali tanpa pulang — telah "
         "mengajarkan anak persis seberapa berharga kalimat Anda."),
        ("Say only what you are willing to carry out today. Say less, mean all of it.",
         "Katakan hanya apa yang siap Anda jalankan hari ini. Bicara lebih sedikit, dan "
         "sungguh-sungguhi semuanya."),
        ("How many of my warnings do I actually follow through on?",
         "Berapa banyak peringatan saya yang benar-benar saya tegakkan?"),
        ("\"I only say things I'm going to do.\"",
         "\"Mama/Papa hanya mengatakan hal yang akan dilakukan.\""),
    ),
    128: d(
        ("Why spanking is risky and ineffective long-term",
         "Mengapa memukul berisiko dan tidak efektif jangka panjang"),
        ("This is worth stating plainly, because it is common and because the evidence is "
         "unusually consistent. Physical punishment produces short-term compliance and, "
         "over time, is associated with more aggression, more mental health difficulty, "
         "and a weaker parent-child relationship — not less misbehaviour.\n\n"
         "It also teaches, unavoidably, that hurting someone is an acceptable way for a "
         "bigger person to solve a problem with a smaller one. That is the lesson most "
         "reliably absorbed.",
         "Ini layak dinyatakan terus terang, karena ia lazim dan karena buktinya sangat "
         "konsisten. Hukuman fisik menghasilkan kepatuhan jangka pendek dan, seiring waktu, "
         "dikaitkan dengan lebih banyak agresi, lebih banyak kesulitan kesehatan mental, dan "
         "hubungan orang tua-anak yang lebih lemah — bukan berkurangnya kenakalan.\n\n"
         "Ia juga mengajarkan, tak terhindarkan, bahwa menyakiti seseorang adalah cara yang "
         "bisa diterima bagi orang yang lebih besar untuk menyelesaikan masalah dengan yang "
         "lebih kecil. Itulah pelajaran yang paling pasti terserap."),
        ("Many parents who smack were smacked themselves and turned out fine. That is "
         "survivorship, not evidence — and it is worth asking what it cost that nobody measured.",
         "Banyak orang tua yang memukul dulu juga dipukul dan tumbuh baik-baik saja. Itu "
         "bias penyintas, bukan bukti — dan layak ditanyakan apa harganya yang tak pernah diukur."),
        ("If this is part of your home, choose one replacement response and prepare it "
         "today, before you need it.",
         "Jika ini bagian dari rumah Anda, pilih satu respons pengganti dan siapkan hari ini, "
         "sebelum Anda membutuhkannya."),
        ("What was I taught about this as a child, and do I still agree with it?",
         "Apa yang diajarkan kepada saya soal ini sewaktu kecil, dan apakah saya masih menyetujuinya?"),
        ("\"I'm putting my hands down. I need a minute.\"",
         "\"Mama/Papa turunkan tangan. Mama/Papa perlu sebentar.\""),
    ),
    129: d(
        ("Redirection for young children",
         "Mengalihkan untuk anak kecil"),
        ("For children under about four, redirection is usually more effective than any "
         "explanation. Their attention is highly moveable and their reasoning is not yet "
         "the lever you want to pull.\n\n"
         "Redirection is not avoidance. It is choosing the tool that fits the age — and it "
         "prevents dozens of conflicts that would otherwise have to be resolved.",
         "Untuk anak di bawah sekitar empat tahun, mengalihkan biasanya lebih efektif "
         "daripada penjelasan apa pun. Perhatian mereka sangat mudah dipindah dan penalaran "
         "mereka belum menjadi tuas yang ingin Anda tarik.\n\n"
         "Mengalihkan bukan menghindar. Itu memilih alat yang sesuai usia — dan mencegah "
         "puluhan konflik yang jika tidak, harus diselesaikan."),
        ("Removing the fragile object and handing over a different one ends the situation "
         "in three seconds and costs the child nothing.",
         "Menyingkirkan benda yang mudah pecah dan memberikan benda lain mengakhiri "
         "situasinya dalam tiga detik dan tak merugikan anak sama sekali."),
        ("Redirect rather than explain once today with your youngest child.",
         "Alihkan alih-alih menjelaskan sekali hari ini pada anak terkecil Anda."),
        ("Am I reasoning with a child too young to be reasoned with?",
         "Apakah saya menalar dengan anak yang terlalu kecil untuk diajak menalar?"),
        ("\"Not that one — here, this one.\"",
         "\"Bukan yang itu — ini, yang ini.\""),
    ),
    130: d(
        ("Setting limits kindly",
         "Menetapkan batas dengan lembut"),
        ("A limit and a kindness are not in competition, though at 7pm it can feel that "
         "way. The most effective limits are stated warmly, briefly, and without "
         "justification piled on top.\n\n"
         "Kindness in the delivery does not weaken the limit. It removes the fight about "
         "your tone, so that only the limit itself remains — which is exactly what you wanted.",
         "Batas dan kelembutan tidak saling bersaing, meski pukul tujuh malam bisa terasa "
         "begitu. Batas yang paling efektif dinyatakan dengan hangat, singkat, dan tanpa "
         "tumpukan pembenaran.\n\n"
         "Kelembutan dalam penyampaian tidak melemahkan batasnya. Ia menghapus pertengkaran "
         "tentang nada Anda, sehingga yang tersisa hanya batasnya sendiri — persis yang Anda inginkan."),
        ("\"I know. It's hard. And it's still bedtime.\" Three short sentences: empathy, "
         "acknowledgement, limit. Nothing else needed.",
         "\"Mama tahu. Memang berat. Dan tetap waktunya tidur.\" Tiga kalimat pendek: empati, "
         "pengakuan, batas. Tak perlu yang lain."),
        ("State one limit today in three sentences or fewer, warmly.",
         "Nyatakan satu batas hari ini dalam tiga kalimat atau kurang, dengan hangat."),
        ("Can I hold a limit without hardening my voice?",
         "Bisakah saya memegang batas tanpa mengeraskan suara?"),
        ("\"I know. And it's still no.\"",
         "\"Mama/Papa tahu. Dan jawabannya tetap tidak.\""),
    ),
    131: d(
        ("Following through calmly",
         "Menegakkan dengan tenang"),
        ("Following through is where most discipline plans fail — not in the deciding but "
         "in the doing, usually because the parent is tired and the resistance is loud.\n\n"
         "Calm follow-through is more powerful than angry follow-through, because it "
         "signals that the limit does not depend on your emotional state. The child learns "
         "the rule is simply true, rather than true when you are cross.",
         "Menegakkan adalah tempat sebagian besar rencana disiplin gagal — bukan pada "
         "memutuskan, melainkan pada melaksanakan, biasanya karena orang tua lelah dan "
         "perlawanannya nyaring.\n\n"
         "Menegakkan dengan tenang lebih kuat daripada dengan marah, karena ia menandakan "
         "batas itu tidak bergantung pada kondisi emosi Anda. Anak belajar bahwa aturannya "
         "memang berlaku, bukan berlaku saat Anda sedang jengkel."),
        ("Doing exactly what you said, quietly and without a speech, is the single most "
         "convincing thing a parent can do.",
         "Melakukan persis apa yang Anda katakan, dengan tenang dan tanpa pidato, adalah hal "
         "paling meyakinkan yang bisa dilakukan orang tua."),
        ("Follow through on one thing today without raising your voice at all.",
         "Tegakkan satu hal hari ini tanpa meninggikan suara sama sekali."),
        ("Do my limits hold when I am tired, or only when I have energy to enforce them?",
         "Apakah batas saya bertahan saat saya lelah, atau hanya saat saya punya tenaga untuk menegakkannya?"),
        ("\"I said what would happen, so this is what happens.\"",
         "\"Mama/Papa sudah bilang apa yang akan terjadi, jadi ini yang terjadi.\""),
    ),
    132: d(
        ("The importance of predictability",
         "Pentingnya bisa ditebak"),
        ("Children test limits far harder when they cannot predict them. Inconsistency does "
         "not read as flexibility — it reads as a machine that sometimes pays out, which is "
         "precisely the pattern that produces the most persistent pushing.\n\n"
         "A predictable no is easier for a child to accept than a no that worked yesterday "
         "and might not today.",
         "Anak menguji batas jauh lebih keras ketika mereka tak bisa menebaknya. "
         "Ketidakkonsistenan tidak terbaca sebagai keluwesan — ia terbaca sebagai mesin yang "
         "kadang mengeluarkan hadiah, dan pola itulah yang paling menghasilkan dorongan "
         "yang paling gigih.\n\n"
         "Tidak yang bisa ditebak lebih mudah diterima anak daripada tidak yang kemarin "
         "mempan dan hari ini mungkin tidak."),
        ("The rule that holds nine times out of ten produces more testing than the rule "
         "that holds every time, because the tenth time is worth trying for.",
         "Aturan yang bertahan sembilan dari sepuluh kali menghasilkan lebih banyak "
         "pengujian daripada aturan yang bertahan setiap kali, karena yang kesepuluh layak dicoba."),
        ("Pick your least consistent rule and hold it exactly today.",
         "Pilih aturan Anda yang paling tidak konsisten dan tegakkan persis hari ini."),
        ("Which of my rules does my child expect to be able to move?",
         "Aturan saya yang mana yang anak harapkan masih bisa digeser?"),
        ("\"This one is always the same.\"",
         "\"Yang ini selalu sama.\""),
    ),
    133: d(
        ("Household rules that are few and clear",
         "Aturan rumah yang sedikit dan jelas"),
        ("A long list of rules cannot be held consistently, so it degrades into "
         "arbitrary enforcement — which is worse than fewer rules kept properly.\n\n"
         "Most families run well on three to five core rules covering safety, respect and "
         "responsibility. Everything else can be a preference, and preferences do not need "
         "to be defended like laws.",
         "Daftar aturan yang panjang tak bisa ditegakkan secara konsisten, sehingga merosot "
         "menjadi penegakan yang sembarang — yang lebih buruk daripada aturan lebih sedikit "
         "yang dijaga dengan baik.\n\n"
         "Kebanyakan keluarga berjalan baik dengan tiga sampai lima aturan inti yang "
         "mencakup keselamatan, rasa hormat, dan tanggung jawab. Selebihnya bisa jadi "
         "preferensi, dan preferensi tak perlu dibela seperti undang-undang."),
        ("Ask your child to list the family rules. If they cannot, there are too many — or "
         "they were never actually stated.",
         "Minta anak menyebutkan aturan keluarga. Jika dia tidak bisa, aturannya terlalu "
         "banyak — atau memang tak pernah benar-benar dinyatakan."),
        ("Write down your family's three to five real rules today.",
         "Tuliskan tiga sampai lima aturan nyata keluarga Anda hari ini."),
        ("Could my child list our rules if I asked?",
         "Bisakah anak saya menyebutkan aturan kami jika saya tanya?"),
        ("\"We have three rules in this house.\"",
         "\"Di rumah ini ada tiga aturan.\""),
    ),
    134: d(
        ("Routines as preventive discipline",
         "Rutinitas sebagai disiplin pencegahan"),
        ("The best discipline is the conflict that never happens. Routines do this quietly, "
         "by removing the negotiation from the parts of the day that reliably go wrong.\n\n"
         "A family that argues nightly about bedtime usually does not have a bedtime "
         "problem. It has a bedtime that gets renegotiated every night.",
         "Disiplin terbaik adalah konflik yang tak pernah terjadi. Rutinitas melakukan ini "
         "dengan tenang, dengan menghapus tawar-menawar dari bagian hari yang selalu berantakan.\n\n"
         "Keluarga yang bertengkar tiap malam soal jam tidur biasanya tidak punya masalah "
         "jam tidur. Mereka punya jam tidur yang dinegosiasi ulang setiap malam."),
        ("Fixing the routine usually removes more difficult behaviour than any consequence "
         "aimed at the behaviour itself.",
         "Membenahi rutinitas biasanya menghapus lebih banyak perilaku sulit daripada "
         "konsekuensi apa pun yang diarahkan pada perilakunya sendiri."),
        ("Turn your worst daily conflict into a fixed sequence today.",
         "Ubah konflik harian terburuk Anda menjadi urutan yang tetap hari ini."),
        ("Which of my discipline problems is actually a routine problem?",
         "Masalah disiplin saya yang mana yang sebenarnya masalah rutinitas?"),
        ("\"Same order every night. That's just how it goes.\"",
         "\"Urutannya sama setiap malam. Memang begitu.\""),
    ),
    135: d(
        ("Using choices wisely",
         "Menggunakan pilihan dengan bijak"),
        ("Choices work because they return a small amount of control without moving the "
         "limit. They fail when they are fake, when there are too many, or when the child "
         "is too flooded to choose at all.\n\n"
         "Two options, both acceptable to you, offered before the resistance peaks. That "
         "is the whole technique.",
         "Pilihan berhasil karena ia mengembalikan sedikit kendali tanpa menggeser batasnya. "
         "Ia gagal ketika pilihannya palsu, ketika terlalu banyak, atau ketika anak terlalu "
         "kewalahan untuk memilih apa pun.\n\n"
         "Dua opsi, keduanya bisa Anda terima, ditawarkan sebelum perlawanan memuncak. Itu "
         "seluruh tekniknya."),
        ("\"Pyjamas first or teeth first?\" keeps bedtime intact. \"Do you want to go to bed?\" "
         "hands over a decision that was never actually available.",
         "\"Piyama dulu atau gosok gigi dulu?\" menjaga waktu tidur tetap utuh. \"Mau tidur "
         "sekarang?\" menyerahkan keputusan yang sebenarnya tak pernah tersedia."),
        ("Offer one genuine two-option choice today, before the resistance starts.",
         "Tawarkan satu pilihan dua opsi yang sungguhan hari ini, sebelum perlawanan dimulai."),
        ("Are the choices I offer real ones?",
         "Apakah pilihan yang saya tawarkan itu pilihan yang sungguhan?"),
        ("\"This way or that way — you pick.\"",
         "\"Cara ini atau cara itu — kamu pilih.\""),
    ),
    136: d(
        ("Avoiding too many warnings",
         "Menghindari terlalu banyak peringatan"),
        ("Every extra warning teaches a child exactly how many they get before anything "
         "happens. If the count is five, they will reliably use four.\n\n"
         "One clear warning, then action. This feels harsher and is actually kinder, "
         "because the child stops having to guess where the real line is.",
         "Setiap peringatan tambahan mengajarkan anak persis berapa banyak peringatan yang "
         "dia dapat sebelum sesuatu terjadi. Jika hitungannya lima, dia pasti memakai empat.\n\n"
         "Satu peringatan yang jelas, lalu tindakan. Ini terasa lebih keras dan sebenarnya "
         "lebih baik hati, karena anak berhenti harus menebak di mana garis sungguhannya."),
        ("Counting to three works only if something reliably happens at three. Otherwise "
         "you have taught a child to start moving at two and a half, forever.",
         "Menghitung sampai tiga hanya berhasil jika sesuatu benar-benar terjadi di hitungan "
         "tiga. Jika tidak, Anda mengajarkan anak baru bergerak di dua setengah, selamanya."),
        ("Give exactly one warning today, then act without a second one.",
         "Beri tepat satu peringatan hari ini, lalu bertindak tanpa peringatan kedua."),
        ("How many warnings does my child know they get?",
         "Berapa peringatan yang anak saya tahu akan dia dapat?"),
        ("\"That's your one warning.\"",
         "\"Itu peringatan satu-satunya.\""),
    ),
    137: d(
        ("When to ignore minor behavior",
         "Kapan mengabaikan perilaku kecil"),
        ("Not everything needs a response. Attention is fuel, and some minor behaviours "
         "burn out on their own if they are not fed — muttering, mild silliness, small "
         "provocations aimed at getting a reaction.\n\n"
         "Ignoring is a deliberate strategy, not neglect. It applies to behaviour that is "
         "annoying, not to behaviour that is unsafe or unkind.",
         "Tidak semua hal butuh tanggapan. Perhatian adalah bahan bakar, dan sebagian "
         "perilaku kecil padam sendiri bila tidak diberi makan — menggerutu, konyol ringan, "
         "provokasi kecil yang mengincar reaksi.\n\n"
         "Mengabaikan adalah strategi yang disengaja, bukan penelantaran. Ia berlaku untuk "
         "perilaku yang menjengkelkan, bukan untuk yang tidak aman atau tidak baik."),
        ("The muttered complaint as a child walks off to do what you asked is usually best "
         "left entirely alone. They complied; the commentary is not the point.",
         "Gerutuan yang diucapkan sambil anak berjalan melakukan yang Anda minta biasanya "
         "paling baik dibiarkan sepenuhnya. Dia menurut; komentarnya bukan intinya."),
        ("Deliberately let one minor irritating behaviour pass today without comment.",
         "Dengan sengaja biarkan satu perilaku kecil yang menjengkelkan lewat hari ini tanpa komentar."),
        ("What am I responding to that would fade if I said nothing?",
         "Apa yang saya tanggapi, yang sebenarnya akan memudar jika saya diam saja?"),
        ("\"Not everything needs me.\"",
         "\"Tidak semuanya butuh saya tanggapi.\""),
    ),
    138: d(
        ("Selective attention",
         "Perhatian yang selektif"),
        ("Behaviour grows in the direction of attention. Most parents, exhausted, give the "
         "most attention to what is going wrong — which quietly teaches that trouble is "
         "the reliable route to connection.\n\n"
         "Deliberately attending to what is going right rebalances this, and it costs "
         "nothing except noticing.",
         "Perilaku bertumbuh ke arah perhatian. Kebanyakan orang tua, karena lelah, memberi "
         "perhatian terbanyak pada apa yang salah — yang diam-diam mengajarkan bahwa keributan "
         "adalah jalan andal menuju kedekatan.\n\n"
         "Dengan sengaja memperhatikan apa yang berjalan benar menyeimbangkan kembali hal ini, "
         "dan tidak memerlukan apa pun selain kesadaran."),
        ("Two children in a room: one playing quietly, one making trouble. Almost every "
         "parent speaks to the second. The first has just learned something.",
         "Dua anak dalam satu ruangan: satu bermain tenang, satu membuat keributan. Hampir "
         "setiap orang tua menyapa yang kedua. Yang pertama baru saja belajar sesuatu."),
        ("Speak to the child who is doing fine today, before you speak to the one who isn't.",
         "Sapa anak yang sedang baik-baik saja hari ini, sebelum menyapa yang sedang bermasalah."),
        ("Which of my children gets my attention only when something is wrong?",
         "Anak saya yang mana yang hanya mendapat perhatian saat ada yang bermasalah?"),
        ("\"I noticed you sorting that out by yourself.\"",
         "\"Mama/Papa lihat kamu membereskannya sendiri.\""),
    ),
    139: d(
        ("Catching good behavior",
         "Menangkap perilaku baik"),
        ("Catching a child being good is the cheapest and most underused discipline tool "
         "there is. It requires no confrontation, builds the relationship, and "
         "strengthens exactly the behaviour you want more of.\n\n"
         "It must be specific to work. \"Good boy\" is noise. \"You waited while I finished "
         "the call — that was patient\" tells a child precisely what to repeat.",
         "Menangkap anak sedang berbuat baik adalah alat disiplin termurah dan paling kurang "
         "dipakai. Ia tak butuh konfrontasi, membangun hubungan, dan menguatkan persis "
         "perilaku yang Anda ingin lebih banyak.\n\n"
         "Ia harus spesifik agar berhasil. \"Anak pintar\" hanyalah bunyi. \"Kamu menunggu "
         "sampai Mama selesai menelepon — itu sabar\" memberi tahu anak persis apa yang harus diulang."),
        ("Aim for noticing something good more often than correcting something bad. Most "
         "households run the other way around without meaning to.",
         "Targetkan menyadari hal baik lebih sering daripada menegur hal buruk. Kebanyakan "
         "rumah berjalan sebaliknya tanpa bermaksud demikian."),
        ("Catch and name three specific good things today.",
         "Tangkap dan sebutkan tiga hal baik yang spesifik hari ini."),
        ("What is my ratio of noticing good to correcting bad?",
         "Berapa perbandingan saya antara menyadari yang baik dan menegur yang buruk?"),
        ("\"I saw that. That was thoughtful.\"",
         "\"Mama/Papa lihat tadi. Itu penuh perhatian.\""),
    ),
    140: d(
        ("Effective praise",
         "Pujian yang efektif"),
        ("Effective praise is specific, honest and about something the child actually did. "
         "Vague or inflated praise is quickly detected and quietly discounted.\n\n"
         "Describing rather than evaluating usually works best: say what you saw, and let "
         "the child draw the conclusion about themselves. That conclusion is more durable "
         "than one you hand them.",
         "Pujian yang efektif itu spesifik, jujur, dan tentang sesuatu yang benar-benar anak "
         "lakukan. Pujian yang kabur atau dilebih-lebihkan cepat terdeteksi dan diam-diam "
         "diabaikan.\n\n"
         "Menggambarkan alih-alih menilai biasanya paling berhasil: katakan apa yang Anda "
         "lihat, dan biarkan anak menarik kesimpulan tentang dirinya. Kesimpulan itu lebih "
         "tahan lama daripada yang Anda sodorkan."),
        ("\"You put all the blocks back without being asked\" lands better than \"you're so "
         "good\", because it is checkable and it is true.",
         "\"Kamu mengembalikan semua baloknya tanpa diminta\" lebih mengena daripada \"kamu "
         "anak baik\", karena bisa diperiksa dan memang benar."),
        ("Describe rather than evaluate in every piece of praise today.",
         "Gambarkan alih-alih menilai dalam setiap pujian hari ini."),
        ("Does my praise tell my child what I actually saw?",
         "Apakah pujian saya memberi tahu anak apa yang sungguh saya lihat?"),
        ("\"You did that whole thing on your own.\"",
         "\"Kamu mengerjakan semuanya sendiri.\""),
    ),
    141: d(
        ("Effort praise vs trait praise",
         "Memuji usaha vs memuji sifat"),
        ("Trait praise — clever, talented, gifted — makes ability feel fixed, so difficulty "
         "becomes threatening evidence. Children praised this way often avoid hard tasks to "
         "protect the label.\n\n"
         "Effort and strategy praise makes difficulty normal and improvable. Over years, "
         "this difference shows up as willingness to attempt hard things, which matters "
         "more than most ability differences.",
         "Memuji sifat — pintar, berbakat, jenius — membuat kemampuan terasa tetap, sehingga "
         "kesulitan menjadi bukti yang mengancam. Anak yang dipuji begini sering menghindari "
         "tugas sulit demi melindungi labelnya.\n\n"
         "Memuji usaha dan strategi membuat kesulitan terasa wajar dan bisa diperbaiki. "
         "Setelah bertahun-tahun, perbedaan ini muncul sebagai kesediaan mencoba hal sulit — "
         "yang lebih penting daripada kebanyakan perbedaan bakat."),
        ("\"You found a different way when the first one didn't work\" praises the thing "
         "you actually want repeated.",
         "\"Kamu mencari cara lain waktu cara pertama tidak berhasil\" memuji hal yang "
         "memang ingin Anda lihat berulang."),
        ("Praise a strategy today, not a trait.",
         "Puji sebuah strategi hari ini, bukan sifat."),
        ("Do I praise who my child is, or what my child did?",
         "Apakah saya memuji siapa anak saya, atau apa yang anak saya lakukan?"),
        ("\"You kept trying different ways. That's the skill.\"",
         "\"Kamu terus mencoba berbagai cara. Itu keterampilannya.\""),
    ),
    142: d(
        ("Rewards: when they help and when they harm",
         "Imbalan: kapan membantu dan kapan merugikan"),
        ("Rewards are useful for genuinely dull, necessary tasks that nobody would choose — "
         "and risky for anything you want a child to value for itself.\n\n"
         "Attach a reward to reading and you often get a child who reads until the reward "
         "stops. The reward becomes the reason, and the original interest quietly leaves.",
         "Imbalan berguna untuk tugas wajib yang memang membosankan dan tak akan dipilih "
         "siapa pun — dan berisiko untuk apa pun yang Anda ingin anak hargai karena hal itu sendiri.\n\n"
         "Lekatkan imbalan pada membaca, dan Anda sering mendapat anak yang membaca sampai "
         "imbalannya berhenti. Imbalan menjadi alasannya, dan minat aslinya diam-diam pergi."),
        ("Use rewards to get a habit started, then fade them out deliberately once the "
         "routine holds on its own.",
         "Pakai imbalan untuk memulai kebiasaan, lalu kurangi dengan sengaja begitu "
         "rutinitasnya bertahan sendiri."),
        ("Check one reward you use: is it on a chore, or on something you want loved?",
         "Periksa satu imbalan yang Anda pakai: apakah untuk tugas rumah, atau untuk sesuatu "
         "yang Anda ingin dicintai?"),
        ("What am I paying for that I would rather my child valued on its own?",
         "Apa yang saya bayar, yang sebenarnya saya ingin anak hargai dengan sendirinya?"),
        ("\"Let's see if we still do it without the chart.\"",
         "\"Coba kita lihat apakah masih jalan tanpa tabelnya.\""),
    ),
    143: d(
        ("Time-in vs time-out",
         "Time-in vs time-out"),
        ("Time-out isolates a child at the moment they are least able to regulate alone. "
         "For some children it works as a neutral pause; for many it registers as "
         "rejection, and the rejection is what they remember.\n\n"
         "Time-in keeps the child near you while they settle. It holds the limit without "
         "withdrawing the relationship — which matters, because the relationship is what "
         "you are relying on to teach.",
         "Time-out mengisolasi anak tepat saat dia paling tidak mampu menenangkan diri "
         "sendirian. Bagi sebagian anak ia berfungsi sebagai jeda netral; bagi banyak anak ia "
         "terasa sebagai penolakan, dan penolakan itulah yang mereka ingat.\n\n"
         "Time-in menjaga anak tetap dekat Anda selagi dia mereda. Ia memegang batas tanpa "
         "menarik hubungannya — dan itu penting, karena hubungan itulah yang Anda andalkan untuk mengajar."),
        ("\"Come and sit with me until you're calm\" holds the same limit as \"go to your "
         "room\" without teaching that big feelings get you sent away.",
         "\"Sini duduk sama Mama sampai tenang\" memegang batas yang sama dengan \"masuk "
         "kamar\" tanpa mengajarkan bahwa perasaan besar membuatmu diusir."),
        ("Try a time-in today where you would normally have used a time-out.",
         "Coba time-in hari ini di tempat Anda biasanya memakai time-out."),
        ("Does my child calm down better alone, or near me?",
         "Apakah anak saya lebih tenang sendirian, atau di dekat saya?"),
        ("\"Sit with me until this passes.\"",
         "\"Duduk sama Mama/Papa sampai ini reda.\""),
    ),
    144: d(
        ("Cooling off without rejection",
         "Menenangkan diri tanpa penolakan"),
        ("Both of you sometimes need to cool down, and that is legitimate. The difference "
         "between a helpful separation and a harmful one is entirely in how it is framed.\n\n"
         "\"I need a minute and I'm coming back\" is regulation. Silent withdrawal, or "
         "sending a child away in anger, reads to a child as: you are too much for me.",
         "Kadang kalian berdua butuh menenangkan diri, dan itu sah. Beda antara perpisahan "
         "yang membantu dan yang merugikan sepenuhnya terletak pada cara membingkainya.\n\n"
         "\"Mama perlu sebentar dan akan kembali\" adalah pengaturan diri. Menarik diri dalam "
         "diam, atau mengusir anak dalam kemarahan, terbaca oleh anak sebagai: kamu terlalu "
         "berat bagi saya."),
        ("The returning is the important half. A break that is announced and honoured "
         "teaches a skill; a break that just happens teaches abandonment.",
         "Kembalinya adalah separuh yang penting. Jeda yang diumumkan dan ditepati "
         "mengajarkan keterampilan; jeda yang terjadi begitu saja mengajarkan ditinggalkan."),
        ("If you need to step away today, name it and return exactly as promised.",
         "Jika Anda perlu menjauh hari ini, sebutkan dan kembalilah persis seperti dijanjikan."),
        ("When I withdraw, what does my child conclude?",
         "Saat saya menarik diri, apa kesimpulan anak saya?"),
        ("\"I'm not leaving you. I'm getting calm so I can help.\"",
         "\"Mama/Papa tidak meninggalkanmu. Mama/Papa menenangkan diri supaya bisa membantu.\""),
    ),
    145: d(
        ("Discipline in public places",
         "Disiplin di tempat umum"),
        ("Public discipline is hard because of the audience, not the child. Imagined "
         "judgement pushes parents into responses far harsher than they would choose at "
         "home, and children feel the inconsistency immediately.\n\n"
         "Decide in advance that you will parent identically in public. It removes most of "
         "the pressure and, incidentally, tends to impress the onlookers you were worried "
         "about.",
         "Disiplin di tempat umum sulit karena penontonnya, bukan karena anaknya. Bayangan "
         "penilaian orang mendorong orang tua ke respons yang jauh lebih keras daripada yang "
         "akan mereka pilih di rumah, dan anak langsung merasakan ketidakkonsistenannya.\n\n"
         "Putuskan sejak awal bahwa Anda akan mengasuh dengan cara yang sama di tempat umum. "
         "Itu menghapus sebagian besar tekanannya dan, kebetulan, cenderung mengesankan "
         "orang-orang yang tadinya Anda khawatirkan."),
        ("Stepping outside with a child mid-meltdown is not defeat. It is choosing to "
         "parent rather than perform.",
         "Keluar sebentar bersama anak yang sedang meltdown bukan kekalahan. Itu memilih "
         "mengasuh, bukan menampilkan diri."),
        ("Handle one public moment today exactly as you would at home.",
         "Tangani satu momen di tempat umum hari ini persis seperti di rumah."),
        ("Whose opinion am I managing in that moment?",
         "Pendapat siapa yang saya kelola di momen itu?"),
        ("\"Let's step outside for a minute.\"",
         "\"Ayo keluar sebentar.\""),
    ),
    146: d(
        ("Bedtime battles",
         "Pertempuran waktu tidur"),
        ("Bedtime conflict is almost always structural rather than moral. It concentrates "
         "everything difficult: a tired child, a tired parent, a transition away from "
         "something pleasant, and a separation.\n\n"
         "Fix the structure — same order, same time, same words, ending in the same place "
         "— and most of the battle disappears without any discipline at all.",
         "Konflik waktu tidur hampir selalu bersifat struktural, bukan moral. Ia memusatkan "
         "semua yang sulit: anak yang lelah, orang tua yang lelah, perpindahan dari sesuatu "
         "yang menyenangkan, dan perpisahan.\n\n"
         "Benahi strukturnya — urutan sama, waktu sama, kata-kata sama, berakhir di tempat "
         "yang sama — dan sebagian besar pertempurannya hilang tanpa disiplin apa pun."),
        ("Four fixed steps in the same order every night outperform any consequence "
         "invented at 8.40pm.",
         "Empat langkah tetap dengan urutan sama setiap malam lebih unggul daripada "
         "konsekuensi apa pun yang diciptakan pukul 20.40."),
        ("Write your bedtime sequence down tonight and follow it exactly.",
         "Tuliskan urutan waktu tidur Anda malam ini dan ikuti persis."),
        ("Is our bedtime a routine, or a negotiation that starts fresh each night?",
         "Apakah waktu tidur kami sebuah rutinitas, atau negosiasi yang dimulai dari nol setiap malam?"),
        ("\"Same four things, same order. Then lights out.\"",
         "\"Empat hal yang sama, urutan yang sama. Lalu lampu mati.\""),
    ),
    147: d(
        ("Mealtime struggles",
         "Perjuangan waktu makan"),
        ("Food is one of the few areas where a child has genuine physical autonomy, which "
         "is why it becomes a battleground. Pressure reliably backfires: forced eating "
         "increases refusal and can build a lasting difficulty with food.\n\n"
         "The useful division is old and holds up well — the parent decides what is offered "
         "and when; the child decides whether and how much.",
         "Makanan adalah salah satu dari sedikit wilayah di mana anak punya otonomi fisik "
         "yang sungguhan, dan karena itulah ia menjadi medan pertempuran. Tekanan selalu "
         "berbalik: memaksa makan meningkatkan penolakan dan bisa membangun kesulitan yang "
         "bertahan lama dengan makanan.\n\n"
         "Pembagian yang berguna itu sudah lama dan masih kuat — orang tua menentukan apa "
         "yang disajikan dan kapan; anak menentukan apakah dan seberapa banyak."),
        ("Removing pressure from the table usually reduces refusal within a couple of "
         "weeks. Adding pressure has never reliably reduced anything.",
         "Menghapus tekanan dari meja makan biasanya mengurangi penolakan dalam beberapa "
         "minggu. Menambah tekanan tak pernah terbukti mengurangi apa pun."),
        ("Serve without commenting on how much is eaten today. Not once.",
         "Sajikan tanpa berkomentar tentang seberapa banyak yang dimakan hari ini. Sama sekali tidak."),
        ("How much of our mealtime talk is about how much is being eaten?",
         "Berapa banyak obrolan waktu makan kami yang tentang seberapa banyak yang dimakan?"),
        ("\"It's there if you want it.\"",
         "\"Ada di situ kalau kamu mau.\""),
    ),
    148: d(
        ("Screen-time boundary conflicts",
         "Konflik batas waktu layar"),
        ("Screens are engineered to be hard to stop, so this is not a character weakness in "
         "your child. Ending a screen session is a transition away from something designed "
         "to prevent exactly that.\n\n"
         "Boundaries set in advance, tied to a visible end point, work far better than "
         "boundaries announced mid-session. \"After this episode\" beats \"turn it off now\" "
         "almost every time.",
         "Layar dirancang agar sulit dihentikan, jadi ini bukan kelemahan karakter anak Anda. "
         "Mengakhiri sesi layar adalah perpindahan dari sesuatu yang justru dirancang untuk "
         "mencegah hal itu.\n\n"
         "Batas yang ditetapkan sejak awal, terikat pada titik akhir yang terlihat, jauh "
         "lebih berhasil daripada batas yang diumumkan di tengah sesi. \"Setelah episode ini\" "
         "hampir selalu mengalahkan \"matikan sekarang\"."),
        ("Agreeing the end before it starts turns you from the person who takes it away "
         "into the person who is keeping an agreement.",
         "Menyepakati akhirnya sebelum dimulai mengubah Anda dari orang yang merebutnya "
         "menjadi orang yang menepati kesepakatan."),
        ("Agree the end point before the next screen session starts today.",
         "Sepakati titik akhirnya sebelum sesi layar berikutnya dimulai hari ini."),
        ("Do we agree screen limits before or during?",
         "Apakah kami menyepakati batas layar sebelum atau saat sedang berlangsung?"),
        ("\"Two episodes, then we stop. Agreed?\"",
         "\"Dua episode, lalu berhenti. Sepakat?\""),
    ),
    149: d(
        ("Homework resistance",
         "Perlawanan terhadap PR"),
        ("Homework resistance is usually about difficulty, shame or fatigue rather than "
         "laziness. A child who expects to fail avoids starting, and avoidance looks "
         "identical to defiance from the outside.\n\n"
         "Reducing the size of the first step is the most effective intervention. Most "
         "resistance is at the beginning, not the middle.",
         "Perlawanan terhadap PR biasanya soal kesulitan, rasa malu, atau kelelahan — bukan "
         "kemalasan. Anak yang memperkirakan dirinya gagal menghindari memulai, dan "
         "penghindaran tampak persis seperti pembangkangan dari luar.\n\n"
         "Memperkecil ukuran langkah pertama adalah intervensi paling efektif. Sebagian "
         "besar perlawanan ada di awal, bukan di tengah."),
        ("\"Just do the first question and then we'll see\" gets more homework finished "
         "than any argument about responsibility.",
         "\"Kerjakan soal pertama saja dulu, nanti kita lihat\" menyelesaikan lebih banyak PR "
         "daripada perdebatan apa pun tentang tanggung jawab."),
        ("Shrink the first step of one difficult task today until it is almost too small.",
         "Perkecil langkah pertama satu tugas sulit hari ini sampai hampir terlalu kecil."),
        ("Is my child avoiding the work, or avoiding feeling stupid?",
         "Apakah anak menghindari pekerjaannya, atau menghindari perasaan bodoh?"),
        ("\"Just the first line. That's all for now.\"",
         "\"Baris pertama saja. Itu dulu.\""),
    ),
    150: d(
        ("Repeated disobedience",
         "Ketidakpatuhan yang berulang"),
        ("When the same behaviour keeps returning despite consistent responses, the "
         "response is not the problem — the diagnosis is. Something underneath has not been "
         "identified.\n\n"
         "Go back to chapter 2: is it a missing skill, an unmet need, a predictable trigger, "
         "or a system problem? Repeated failure of a good strategy is information, and it "
         "is asking you to look somewhere else.",
         "Ketika perilaku yang sama terus kembali meski respons Anda konsisten, yang jadi "
         "masalah bukan responsnya — melainkan diagnosisnya. Ada sesuatu di bawahnya yang "
         "belum teridentifikasi.\n\n"
         "Kembalilah ke bab 2: apakah ini keterampilan yang belum ada, kebutuhan yang tak "
         "terpenuhi, pemicu yang bisa diperkirakan, atau masalah sistem? Kegagalan berulang "
         "sebuah strategi yang baik adalah informasi, dan ia meminta Anda melihat ke tempat lain."),
        ("Five failed attempts with the same approach is not a reason for a sixth. It is a "
         "reason to change the question.",
         "Lima percobaan gagal dengan pendekatan yang sama bukan alasan untuk yang keenam. "
         "Itu alasan untuk mengganti pertanyaannya."),
        ("Take your most persistent behaviour and re-diagnose it from scratch today.",
         "Ambil perilaku Anda yang paling membandel dan diagnosis ulang dari awal hari ini."),
        ("What have I never checked underneath this behaviour?",
         "Apa yang belum pernah saya periksa di balik perilaku ini?"),
        ("\"I've been solving the wrong problem.\"",
         "\"Selama ini saya menyelesaikan masalah yang salah.\""),
    ),
    151: d(
        ("Weekly reflection",
         "Refleksi mingguan"),
        ("This chapter has one sentence at its centre: consistency, not intensity, is what "
         "changes behaviour. The fifth calm repetition does more than the first loud one.\n\n"
         "Look back over the month and check the pattern rather than the incidents. Most "
         "parents find their discipline is either consistent but harsh, or warm but "
         "unpredictable. The work is holding both at once — which is the same warmth and "
         "structure pairing from chapter 1, arriving again in a harder setting.",
         "Bab ini punya satu kalimat di pusatnya: konsistensi, bukan intensitas, yang "
         "mengubah perilaku. Pengulangan kelima yang tenang lebih berhasil daripada yang "
         "pertama yang keras.\n\n"
         "Tengok kembali sebulan ini dan periksa polanya, bukan kejadiannya. Kebanyakan "
         "orang tua menemukan disiplin mereka entah konsisten tapi keras, atau hangat tapi "
         "tak bisa ditebak. Pekerjaannya adalah memegang keduanya sekaligus — pasangan "
         "kehangatan dan struktur yang sama dari bab 1, datang lagi dalam keadaan yang lebih sulit."),
        ("Consistent but harsh, or warm but unpredictable — almost every parent leans one "
         "way. Knowing which is yours tells you exactly what to practise.",
         "Konsisten tapi keras, atau hangat tapi tak bisa ditebak — hampir setiap orang tua "
         "condong ke salah satunya. Mengetahui yang mana milik Anda memberi tahu persis apa "
         "yang perlu dilatih."),
        ("Name which way you lean, and choose the one dial to turn this month.",
         "Sebutkan Anda condong ke mana, dan pilih satu tombol untuk diputar bulan ini."),
        ("Am I consistent but harsh, or warm but unpredictable?",
         "Apakah saya konsisten tapi keras, atau hangat tapi tak bisa ditebak?"),
        ("\"Calm and the same, every time. That's the whole method.\"",
         "\"Tenang dan sama, setiap kali. Itu seluruh metodenya.\""),
    ),
}
