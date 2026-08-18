# Chapter 1 — Parenting Mindset (days 1-31)
#
# Authored to replace the manuscript's template-generated bodies. Grounded in
# the founder's guidebook chapter 1 ("Effective parenting is formation, not
# control"), toolkit tool 1 (Long-Game Vision Worksheet), and diary weeks 1-4.
#
# Voice: warm, calm, concrete, never shaming. Indonesian is written as natural
# parenting register, not a word-for-word gloss of the English.

def d(title, teaching, inPractice, practice, reflection, script, framework=None):
    f = lambda p: {"en": p[0], "id": p[1]}
    out = {
        "title": f(title),
        "teaching": f(teaching),
        "inPractice": f(inPractice),
        "practice": f(practice),
        "reflection": f(reflection),
        "script": f(script),
    }
    if framework:
        out["framework"] = framework
    return out


def fw(title, note, entries):
    """A small comparison grid the app renders as cards.

    entries: (name, tags, looksLike, outcome) — each a (en, id) pair, except
    tags which is a list of (en, id) pairs.
    """
    f = lambda p: {"en": p[0], "id": p[1]}
    return {
        "title": f(title),
        "note": f(note),
        "entries": [
            {
                "name": f(name),
                "tags": [f(t) for t in tags],
                "looksLike": f(looks),
                "outcome": f(outcome),
            }
            for (name, tags, looks, outcome) in entries
        ],
    }


DAYS = {
    1: d(
        ("What effective parenting means",
         "Apa arti mengasuh yang efektif"),
        ("Effective parenting is not the production of instant obedience. It is the "
         "steady work of helping a child grow in five things: character, security, "
         "self-control, wisdom, and relationship. Everything in this guide serves those "
         "five.\n\n"
         "This matters because your definition of success decides your daily behaviour. "
         "Define it narrowly — as quiet, as speed, as compliance — and every small mess "
         "becomes a battle you have to win. Define it as formation, and the same mess "
         "becomes a place to teach. Same child, same spilled cup, completely different "
         "parent.\n\n"
         "Obedience is not the enemy here. A child does need to stop at the road. But "
         "obedience is a tool inside the larger job, not the job itself. When it becomes "
         "the whole goal, you get a child who behaves while watched and little else "
         "underneath.",
         "Mengasuh yang efektif bukanlah menghasilkan kepatuhan seketika. Ia adalah "
         "pekerjaan yang stabil untuk membantu anak bertumbuh dalam lima hal: karakter, "
         "rasa aman, pengendalian diri, kebijaksanaan, dan hubungan. Semua isi panduan "
         "ini melayani kelima hal itu.\n\n"
         "Ini penting karena definisi keberhasilan Anda menentukan perilaku harian Anda. "
         "Artikan sempit — sebagai diam, cepat, patuh — dan setiap kekacauan kecil menjadi "
         "pertempuran yang harus Anda menangkan. Artikan sebagai pembentukan, dan "
         "kekacauan yang sama menjadi ruang untuk mengajar. Anak yang sama, susu tumpah "
         "yang sama, orang tua yang sama sekali berbeda.\n\n"
         "Kepatuhan bukan musuh di sini. Anak memang perlu berhenti di tepi jalan. Tapi "
         "kepatuhan adalah alat di dalam pekerjaan yang lebih besar, bukan pekerjaannya "
         "itu sendiri. Ketika ia menjadi seluruh tujuan, Anda mendapat anak yang "
         "berperilaku baik saat diawasi, dan tak banyak lagi di baliknya."),
        ("A cup of milk goes over. One parent demands an instant cleanup and a neat "
         "apology. Another says, \"It happens — let's get the cloth together.\" The first "
         "has a clean floor. The second is raising a person.",
         "Segelas susu tumpah. Satu orang tua menuntut dibersihkan saat itu juga dan "
         "permintaan maaf yang rapi. Yang lain berkata, \"Tidak apa-apa — ayo ambil lap "
         "bersama.\" Yang pertama mendapat lantai bersih. Yang kedua sedang membentuk manusia."),
        ("Write down the three qualities you most hope your child carries into adulthood. "
         "Keep the list somewhere you will see it this week.",
         "Tuliskan tiga kualitas yang paling Anda harapkan anak bawa sampai dewasa. "
         "Simpan daftar itu di tempat yang akan Anda lihat minggu ini."),
        ("If my child grew up to be exactly what I corrected them into this year, who "
         "would they become?",
         "Jika anak saya tumbuh persis menjadi apa yang saya tegur sepanjang tahun ini, "
         "akan menjadi siapa dia?"),
        ("\"It happens. Let's fix it together.\"",
         "\"Tidak apa-apa. Ayo kita bereskan bersama.\""),
    ),
    2: d(
        ("Parenting as guidance, not control",
         "Mengasuh sebagai bimbingan, bukan kendali"),
        ("Control aims at the next five minutes; guidance aims at the next twenty years.\n\n"
         "Control is not wrong — it is just small. It can be highly effective and still "
         "leave a child with no idea why the rule exists. Its weakness is that it only "
         "works while you are in the room, because the reason lives in you rather than "
         "in the child.\n\n"
         "Guidance is slower and less satisfying. It explains, it involves the child in "
         "the thinking, and it accepts a worse result today for a better one at "
         "fifteen. It teaches a child to carry the reason inside themselves — the only "
         "version that survives your absence, and the only version that still works when "
         "your child is bigger than you and no longer has to comply.",
         "Kendali menyasar lima menit ke depan; bimbingan menyasar dua puluh tahun ke depan.\n\n"
         "Kendali bukan hal yang salah — ia hanya kecil. Ia bisa sangat berhasil dan tetap "
         "membuat anak tak paham mengapa aturan itu ada. Kelemahannya, ia hanya bekerja "
         "selama Anda ada di ruangan, karena alasannya tinggal di dalam diri Anda, bukan "
         "di dalam diri anak.\n\n"
         "Bimbingan lebih lambat dan kurang memuaskan. Ia menjelaskan, melibatkan anak "
         "dalam berpikir, dan menerima hasil yang lebih buruk hari ini demi hasil yang "
         "lebih baik di usia lima belas. Ia mengajarkan anak membawa alasannya di dalam "
         "dirinya — satu-satunya versi yang bertahan saat Anda tak ada, dan satu-satunya "
         "yang masih berlaku ketika anak Anda lebih besar dari Anda dan tak lagi harus menurut."),
        ("\"Because I said so\" ends the conversation now. \"We stop at the road because "
         "cars cannot see you\" ends it forever, because the child can use the reason "
         "when you are not standing there.",
         "\"Pokoknya begitu\" mengakhiri percakapan sekarang. \"Kita berhenti di jalan "
         "karena mobil tidak bisa melihatmu\" mengakhirinya selamanya, karena anak bisa "
         "memakai alasan itu saat Anda tidak di sampingnya."),
        ("Pick one rule you enforce daily. Say the reason out loud once today, in one "
         "short sentence.",
         "Pilih satu aturan yang Anda tegakkan setiap hari. Ucapkan alasannya sekali "
         "hari ini, dalam satu kalimat pendek."),
        ("Which of my rules could my child explain to someone else — and which would "
         "they only be able to obey?",
         "Aturan saya yang mana yang bisa dijelaskan anak kepada orang lain — dan yang "
         "mana yang hanya bisa dia patuhi?"),
        ("\"Here's why this one matters to me.\"",
         "\"Ini alasannya kenapa hal ini penting buat Mama/Papa.\""),
    ),
    3: d(
        ("Long-term goal vs short-term obedience",
         "Tujuan jangka panjang vs kepatuhan sesaat"),
        ("Almost every hard parenting moment is a choice between what works right now "
         "and what builds over years. Short-term obedience is loud and measurable. "
         "Long-term formation is quiet and slow, and it almost never gives you the "
         "satisfaction of winning the moment.",
         "Hampir setiap momen sulit dalam pengasuhan adalah pilihan antara yang berhasil "
         "sekarang dan yang terbangun bertahun-tahun. Kepatuhan sesaat itu nyaring dan "
         "terukur. Pembentukan jangka panjang itu sunyi dan lambat, dan hampir tidak "
         "pernah memberi Anda kepuasan menang saat itu juga."),
        ("Threatening to leave the playground gets a child moving in ten seconds. "
         "Giving a five-minute warning takes longer today and builds a child who can "
         "manage transitions next year.",
         "Mengancam meninggalkan taman membuat anak bergerak dalam sepuluh detik. "
         "Memberi aba-aba lima menit lebih lama hari ini, tapi membentuk anak yang bisa "
         "mengelola perpindahan tahun depan."),
        ("Notice one moment today where you chose speed. Ask what the slower version "
         "would have taught.",
         "Sadari satu momen hari ini saat Anda memilih cepat. Tanyakan, apa yang akan "
         "diajarkan versi yang lebih lambat."),
        ("What am I willing to spend an extra two minutes on today, because it matters "
         "in ten years?",
         "Untuk apa saya rela menambah dua menit hari ini, karena hal itu berarti dalam "
         "sepuluh tahun?"),
        ("\"We have five more minutes, then we go.\"",
         "\"Lima menit lagi, lalu kita pulang.\""),
    ),
    4: d(
        ("Temperament: children differ naturally",
         "Temperamen: anak memang berbeda-beda"),
        ("Children arrive with a temperament already running — some cautious, some "
         "intense, some slow to warm, some in constant motion. Temperament is not "
         "character and it is not your doing. Parenting works best when it stops "
         "fighting a child's wiring and starts working with it.",
         "Anak lahir dengan temperamen yang sudah berjalan — ada yang berhati-hati, ada "
         "yang intens, ada yang butuh waktu menyesuaikan diri, ada yang tak berhenti "
         "bergerak. Temperamen bukan karakter, dan bukan hasil perbuatan Anda. Pengasuhan "
         "paling berhasil ketika berhenti melawan bawaan anak dan mulai bekerja dengannya."),
        ("A slow-to-warm child at a party is not being rude. Pushed to greet everyone, "
         "they shut down. Given ten quiet minutes at the edge of the room, they join "
         "on their own.",
         "Anak yang butuh waktu menyesuaikan diri di sebuah pesta bukan sedang tidak "
         "sopan. Didesak menyapa semua orang, dia menutup diri. Diberi sepuluh menit "
         "tenang di pinggir ruangan, dia bergabung dengan sendirinya."),
        ("Name your child's temperament in one honest word. Adjust one expectation today "
         "to fit it rather than fight it.",
         "Sebutkan temperamen anak Anda dalam satu kata yang jujur. Sesuaikan satu "
         "harapan hari ini agar cocok dengannya, bukan melawannya."),
        ("Where am I asking my child to be a different kind of person rather than a "
         "better version of who they are?",
         "Di mana saya meminta anak menjadi orang yang berbeda, bukan versi yang lebih "
         "baik dari dirinya sendiri?"),
        ("\"You take your time. I'll be right here.\"",
         "\"Pelan-pelan saja. Mama/Papa di sini.\""),
    ),
    5: d(
        ("Developmentally appropriate expectations",
         "Harapan yang sesuai tahap perkembangan"),
        ("A great deal of what parents call defiance is simply a child being asked for "
         "a skill they do not yet have. Waiting, sharing, sitting still and managing "
         "disappointment are all capacities that arrive on a schedule, and no amount of "
         "firmness moves that schedule forward.",
         "Banyak hal yang orang tua sebut pembangkangan sebenarnya hanyalah anak diminta "
         "melakukan keterampilan yang belum dia miliki. Menunggu, berbagi, duduk diam, "
         "dan mengelola kekecewaan adalah kemampuan yang datang sesuai jadwalnya, dan "
         "seberapa pun tegasnya Anda, jadwal itu tidak bisa dipercepat."),
        ("Asking a three-year-old to wait quietly through a forty-minute queue is not a "
         "discipline problem waiting to happen — it is a mismatch between the request "
         "and the child.",
         "Meminta anak tiga tahun menunggu diam dalam antrean empat puluh menit bukan "
         "masalah disiplin yang menunggu terjadi — itu ketidakcocokan antara permintaan "
         "dan kemampuan anak."),
        ("Take the behavior that frustrated you most this week and ask honestly whether "
         "the skill it requires has arrived yet.",
         "Ambil perilaku yang paling membuat Anda frustrasi minggu ini dan tanyakan "
         "dengan jujur apakah keterampilan yang dibutuhkannya sudah muncul."),
        ("Am I disciplining a choice my child made, or a capacity they do not yet have?",
         "Apakah saya sedang mendisiplinkan pilihan anak, atau kemampuan yang belum dia miliki?"),
        ("\"That's hard to do at your age. Let's make it smaller.\"",
         "\"Itu sulit untuk usiamu. Ayo kita perkecil dulu.\""),
    ),
    6: d(
        ("Connection before correction",
         "Terhubung dulu, baru menegur"),
        ("A child who feels unseen cannot take in a lesson, however correct the lesson "
         "is. Connection is not a reward you give after good behavior; it is the "
         "condition that makes teaching possible at all. Thirty seconds of contact "
         "before the correction usually saves ten minutes of resistance after it.",
         "Anak yang merasa tidak dilihat tidak bisa menyerap pelajaran, sebenar apa pun "
         "pelajaran itu. Kedekatan bukan hadiah yang Anda berikan setelah anak berperilaku "
         "baik; ia adalah syarat yang membuat pengajaran mungkin terjadi. Tiga puluh detik "
         "kehadiran sebelum menegur biasanya menghemat sepuluh menit perlawanan sesudahnya."),
        ("Instead of calling the correction across the room, kneel down, catch their eye, "
         "put a hand on their shoulder — then say the hard thing. The words land "
         "differently from that distance.",
         "Alih-alih meneriakkan teguran dari seberang ruangan, berjongkoklah, tatap "
         "matanya, letakkan tangan di bahunya — baru katakan hal yang sulit. Kata-kata "
         "itu terasa berbeda dari jarak sedekat itu."),
        ("Before your next correction today, make contact first: eye level, one touch, "
         "one breath. Then speak.",
         "Sebelum teguran Anda berikutnya hari ini, buat kontak dulu: sejajar mata, satu "
         "sentuhan, satu tarikan napas. Baru bicara."),
        ("Does my child feel met by me before they feel corrected by me?",
         "Apakah anak merasa dijumpai oleh saya sebelum merasa ditegur oleh saya?"),
        ("\"Come here a second. I want to talk with you, not at you.\"",
         "\"Sini sebentar. Mama/Papa mau bicara denganmu, bukan memarahimu.\""),
    ),
    7: d(
        ("Authoritative vs authoritarian parenting",
         "Pengasuhan berwibawa vs otoriter"),
        ("This is the single most useful idea in parenting research, and the two words "
         "sound so alike that most people mix them up. They are close to opposites.\n\n"
         "Every parenting style is a combination of just two things: how much warmth you "
         "give, and how much structure you hold. Put them on two axes and four styles "
         "appear.\n\n"
         "AUTHORITARIAN is high structure, low warmth — rules without relationship. "
         "\"Because I said so.\" It produces obedience while you are watching, and often "
         "anxiety, resentment or skilled concealment underneath.\n\n"
         "PERMISSIVE is high warmth, low structure — relationship without rules. The "
         "child feels loved but unsteered, and children who are unsteered are anxious, "
         "because someone has to be in charge and they suspect it is them.\n\n"
         "AUTHORITATIVE is high warmth AND high structure — clear expectations carried "
         "inside a warm relationship. This is the target. It is the pattern most "
         "consistently linked with children who do well on almost every measure.\n\n"
         "The word you want is authoritative: firm and warm at the same time, in the "
         "same sentence, from the same person.",
         "Ini gagasan paling berguna dalam penelitian pengasuhan, dan dua katanya begitu "
         "mirip sampai kebanyakan orang tertukar. Keduanya nyaris berlawanan.\n\n"
         "Setiap gaya pengasuhan adalah gabungan dua hal saja: seberapa banyak kehangatan "
         "yang Anda beri, dan seberapa banyak struktur yang Anda pegang. Letakkan pada dua "
         "sumbu, dan muncullah empat gaya.\n\n"
         "OTORITER adalah struktur tinggi, kehangatan rendah — aturan tanpa hubungan. "
         "\"Pokoknya begitu.\" Ia menghasilkan kepatuhan selama Anda mengawasi, dan sering "
         "kecemasan, dendam, atau kemahiran menyembunyikan di baliknya.\n\n"
         "PERMISIF adalah kehangatan tinggi, struktur rendah — hubungan tanpa aturan. Anak "
         "merasa disayangi tapi tidak dikemudikan, dan anak yang tak dikemudikan menjadi "
         "cemas, karena harus ada yang memimpin dan dia curiga itu dirinya.\n\n"
         "BERWIBAWA adalah kehangatan tinggi DAN struktur tinggi — harapan yang jelas di "
         "dalam hubungan yang hangat. Inilah sasarannya. Pola ini paling konsisten "
         "dikaitkan dengan anak yang bertumbuh baik di hampir semua ukuran.\n\n"
         "Kata yang Anda tuju adalah berwibawa: tegas dan hangat sekaligus, dalam kalimat "
         "yang sama, dari orang yang sama."),
        ("Same bedtime, four different homes. The authoritarian shouts it. The permissive "
         "abandons it. The uninvolved never set one. The authoritative says, \"I know you "
         "want to keep playing. Bedtime is still eight,\" and holds the line kindly.",
         "Jam tidur yang sama, empat rumah berbeda. Yang otoriter meneriakkannya. Yang "
         "permisif meninggalkannya. Yang tak terlibat tak pernah menetapkannya. Yang "
         "berwibawa berkata, \"Mama tahu kamu masih ingin main. Jam tidur tetap jam "
         "delapan,\" dan memegang batas itu dengan lembut."),
        ("Find yourself honestly on the grid below. Then take one rule you hold today and "
         "add warmth to it without removing the rule.",
         "Temukan posisi Anda dengan jujur pada tabel di bawah. Lalu ambil satu aturan yang "
         "Anda pegang hari ini dan tambahkan kehangatan tanpa menghapus aturannya."),
        ("Which of the four am I on a good day — and which do I slide into when I am "
         "tired?",
         "Saya yang mana dari keempatnya di hari yang baik — dan saya tergelincir ke mana "
         "saat lelah?"),
        ("\"I understand, and the answer is still no.\"",
         "\"Mama/Papa mengerti, dan jawabannya tetap tidak.\""),
        framework=fw(
            ("The four parenting styles", "Empat gaya pengasuhan"),
            ("Warmth and structure are two separate dials, not one. Where are you today?",
             "Kehangatan dan struktur adalah dua tombol terpisah, bukan satu. Anda ada di mana hari ini?"),
            [
                (("Authoritative", "Berwibawa"),
                 [("High warmth", "Kehangatan tinggi"), ("High structure", "Struktur tinggi")],
                 ("Clear rules, explained kindly, held consistently — and the relationship "
                  "stays intact while you hold them.",
                  "Aturan jelas, dijelaskan dengan lembut, dipegang konsisten — dan hubungan "
                  "tetap utuh saat Anda memegangnya."),
                 ("The target. Children tend to be secure, self-controlled and willing to "
                  "be influenced.",
                  "Inilah sasarannya. Anak cenderung merasa aman, mampu mengendalikan diri, "
                  "dan terbuka dipengaruhi.")),
                (("Authoritarian", "Otoriter"),
                 [("Low warmth", "Kehangatan rendah"), ("High structure", "Struktur tinggi")],
                 ("Many rules, little explanation, obedience demanded. \"Because I said so.\"",
                  "Banyak aturan, sedikit penjelasan, kepatuhan dituntut. \"Pokoknya begitu.\""),
                 ("Compliance while watched; often anxiety, resentment, or better hiding "
                  "rather than better choices.",
                  "Patuh selama diawasi; sering muncul cemas, dendam, atau makin pandai "
                  "menyembunyikan — bukan pilihan yang lebih baik.")),
                (("Permissive", "Permisif"),
                 [("High warmth", "Kehangatan tinggi"), ("Low structure", "Struktur rendah")],
                 ("Loving and close, but limits bend whenever they are pushed.",
                  "Penuh kasih dan dekat, tapi batas melunak setiap kali didorong."),
                 ("Children feel loved but unsteered, which often shows up as anxiety and "
                  "difficulty with frustration.",
                  "Anak merasa disayangi tapi tak dikemudikan, yang sering tampak sebagai "
                  "kecemasan dan sulit menahan frustrasi.")),
                (("Uninvolved", "Tidak terlibat"),
                 [("Low warmth", "Kehangatan rendah"), ("Low structure", "Struktur rendah")],
                 ("Little guidance and little connection — usually a sign the parent is "
                  "depleted or overwhelmed, not uncaring.",
                  "Sedikit bimbingan dan sedikit kedekatan — biasanya tanda orang tua "
                  "kehabisan tenaga atau kewalahan, bukan tak peduli."),
                 ("The hardest start for a child. If this describes a season you are in, "
                  "it is worth asking for support.",
                  "Awal yang paling berat bagi anak. Jika ini menggambarkan masa yang "
                  "sedang Anda jalani, layak untuk mencari dukungan.")),
            ],
        ),
    ),
    8: d(
        ("Warmth and structure together",
         "Kehangatan dan struktur bersamaan"),
        ("Yesterday named the four styles. Today is the practical heart of it: warmth "
         "and structure are two separate dials, and most parents turn one down to turn "
         "the other up.\n\n"
         "Warmth without structure leaves a child anxious, because nobody is steering. "
         "Structure without warmth leaves a child compliant but alone. The skill worth "
         "building is holding both at full strength in the same moment — which feels "
         "impossible at 7pm and is mostly a matter of practice.\n\n"
         "The test is simple. When you are at your firmest, does your child still feel "
         "liked by you? If yes, you are being authoritative. If no, the structure dial "
         "went up and the warmth dial quietly went down.",
         "Kemarin kita menamai empat gaya. Hari ini inti praktisnya: kehangatan dan "
         "struktur adalah dua tombol terpisah, dan kebanyakan orang tua menurunkan yang "
         "satu untuk menaikkan yang lain.\n\n"
         "Kehangatan tanpa struktur membuat anak cemas, karena tak ada yang memegang "
         "kemudi. Struktur tanpa kehangatan membuat anak patuh tapi sendirian. "
         "Keterampilan yang layak dibangun adalah memegang keduanya penuh di momen yang "
         "sama — yang terasa mustahil pukul tujuh malam, dan sebagian besar hanyalah soal latihan.\n\n"
         "Ujinya sederhana. Saat Anda sedang paling tegas, apakah anak masih merasa "
         "disayangi oleh Anda? Jika ya, Anda sedang berwibawa. Jika tidak, tombol struktur "
         "naik dan tombol kehangatan diam-diam turun."),
        ("\"I'm not letting you hit your brother, and I'm not going anywhere\" holds the "
         "limit and the relationship in one sentence. The child hears both.",
         "\"Mama tidak akan membiarkan kamu memukul adik, dan Mama tidak akan pergi ke "
         "mana-mana\" memegang batas dan hubungan dalam satu kalimat. Anak mendengar keduanya."),
        ("Practise saying one limit today with warmth in the same breath — the rule and "
         "the reassurance together.",
         "Latih mengucapkan satu batasan hari ini dengan kehangatan dalam satu tarikan "
         "napas — aturan dan penenangan sekaligus."),
        ("Which do I find harder to give when I am tired: the warmth or the structure?",
         "Mana yang lebih sulit saya berikan saat lelah: kehangatannya atau strukturnya?"),
        ("\"I won't let you do that, and I'm staying right here.\"",
         "\"Mama/Papa tidak izinkan itu, dan Mama/Papa tetap di sini.\""),
    ),
    9: d(
        ("Why harshness backfires",
         "Mengapa kekerasan justru merugikan"),
        ("Harshness works quickly, which is exactly why it is so tempting. But it teaches "
         "a child to manage your reaction rather than their own behavior. Over time it "
         "produces better hiding, not better choices — and it spends the trust you will "
         "need when the stakes are higher.",
         "Kekerasan bekerja cepat, dan justru itulah yang membuatnya menggoda. Tapi ia "
         "mengajarkan anak mengelola reaksi Anda, bukan perilakunya sendiri. Seiring "
         "waktu ia menghasilkan kemampuan menyembunyikan yang lebih baik, bukan pilihan "
         "yang lebih baik — dan menghabiskan kepercayaan yang Anda butuhkan saat "
         "taruhannya lebih besar."),
        ("The child who breaks something and hides the pieces has not learned honesty. "
         "They have learned what happens when you find out.",
         "Anak yang memecahkan sesuatu lalu menyembunyikan pecahannya bukan sedang belajar "
         "kejujuran. Dia sedang belajar apa yang terjadi ketika Anda mengetahuinya."),
        ("Notice one moment today when you raised the volume. Ask what it actually "
         "taught, not what it stopped.",
         "Sadari satu momen hari ini saat Anda meninggikan suara. Tanyakan apa yang "
         "sebenarnya diajarkannya, bukan apa yang dihentikannya."),
        ("Do I want my child to behave because they understand, or because they are "
         "afraid of me?",
         "Saya ingin anak berperilaku baik karena dia mengerti, atau karena dia takut "
         "kepada saya?"),
        ("\"I'm going to lower my voice and start again.\"",
         "\"Mama/Papa akan pelankan suara dan mulai lagi.\""),
    ),
    10: d(
        ("Child behavior as communication",
         "Perilaku anak sebagai pesan"),
        ("Behavior is a message sent by a child who cannot yet send it in words. Hitting "
         "often means overwhelmed. Whining often means depleted. Refusing often means "
         "powerless. Read the message and the behavior usually loses most of its force.",
         "Perilaku adalah pesan dari anak yang belum bisa menyampaikannya dengan kata. "
         "Memukul sering berarti kewalahan. Merengek sering berarti kehabisan tenaga. "
         "Menolak sering berarti merasa tidak berdaya. Bacalah pesannya, dan perilaku itu "
         "biasanya kehilangan sebagian besar kekuatannya."),
        ("The tantrum in the supermarket at 5pm is rarely about the sweets. It is about "
         "a tired child at the end of a long day with no words left.",
         "Tantrum di supermarket pukul lima sore jarang soal permennya. Itu soal anak "
         "lelah di penghujung hari panjang yang kehabisan kata-kata."),
        ("Take one repeated behavior and write what it might be saying, before deciding "
         "what to do about it.",
         "Ambil satu perilaku yang berulang dan tuliskan apa yang mungkin sedang "
         "disampaikannya, sebelum memutuskan tindakan."),
        ("What has my child been trying to tell me that I have been answering as "
         "misbehavior?",
         "Apa yang selama ini coba disampaikan anak, tapi saya jawab sebagai kenakalan?"),
        ("\"Something's going on. Help me understand it.\"",
         "\"Ada sesuatu, ya. Bantu Mama/Papa mengerti.\""),
    ),
    11: d(
        ("Co-regulation before self-regulation",
         "Menenangkan bersama sebelum menenangkan diri"),
        ("Children do not learn calm by being told to calm down. They borrow it from a "
         "steady adult nearby, again and again, until eventually they can generate it "
         "themselves. Your regulated nervous system is the teaching tool — long before "
         "any words you use.",
         "Anak tidak belajar tenang dengan disuruh tenang. Mereka meminjamnya dari orang "
         "dewasa yang stabil di dekatnya, berulang kali, sampai akhirnya mereka bisa "
         "memunculkannya sendiri. Sistem saraf Anda yang tenang adalah alat pengajarannya "
         "— jauh sebelum kata-kata apa pun yang Anda pakai."),
        ("Shouting \"CALM DOWN\" at an upset child has never once produced calm. Sitting "
         "beside them and slowing your own breathing frequently does.",
         "Meneriakkan \"TENANG!\" pada anak yang sedang kesal tidak pernah sekali pun "
         "menghasilkan ketenangan. Duduk di sampingnya dan memperlambat napas Anda "
         "sendiri sering kali berhasil."),
        ("The next time your child escalates, regulate yourself first and say nothing "
         "for thirty seconds.",
         "Lain kali anak Anda memuncak, tenangkan diri Anda dulu dan jangan berkata apa "
         "pun selama tiga puluh detik."),
        ("Am I bringing calm into this moment, or adding to the storm?",
         "Apakah saya membawa ketenangan ke momen ini, atau menambah badainya?"),
        ("\"I'm here. We'll wait for this to pass together.\"",
         "\"Mama/Papa di sini. Kita tunggu ini reda bersama.\""),
    ),
    12: d(
        ("Attachment basics",
         "Dasar-dasar kelekatan"),
        ("Attachment is the working answer a child carries to one question: when I need "
         "someone, will they come? Built through thousands of ordinary responses — not "
         "grand gestures — it becomes the template for how safe the world feels and how "
         "much a child will let you influence them later.",
         "Kelekatan adalah jawaban yang dibawa anak atas satu pertanyaan: saat aku "
         "membutuhkan seseorang, apakah dia datang? Terbangun lewat ribuan respons "
         "biasa — bukan gestur besar — ia menjadi cetakan tentang seberapa aman dunia "
         "terasa dan seberapa besar anak mengizinkan Anda memengaruhinya kelak."),
        ("It is not the perfect response that builds security. It is the pattern: mostly "
         "coming, mostly noticing, mostly returning after you get it wrong.",
         "Bukan respons sempurna yang membangun rasa aman. Melainkan polanya: sebagian "
         "besar datang, sebagian besar menyadari, sebagian besar kembali setelah Anda keliru."),
        ("Count the small moments today when your child reached for you and you turned "
         "toward them. Aim for one more.",
         "Hitung momen kecil hari ini saat anak mencari Anda dan Anda berpaling kepadanya. "
         "Tambahkan satu lagi."),
        ("When my child needs me, what do they expect to happen?",
         "Saat anak membutuhkan saya, apa yang dia harapkan terjadi?"),
        ("\"I'm listening. Tell me.\"",
         "\"Mama/Papa dengar. Ceritakan.\""),
    ),
    13: d(
        ("Secure base concept",
         "Konsep rumah aman"),
        ("A child explores in proportion to how safe home base feels. The braver child "
         "is usually not the one pushed hardest, but the one who knows exactly where to "
         "return. Security and independence are not opposites — one is the launching "
         "pad for the other.",
         "Anak menjelajah sebanding dengan rasa amannya terhadap rumah. Anak yang lebih "
         "berani biasanya bukan yang paling didorong, melainkan yang tahu persis ke mana "
         "harus kembali. Rasa aman dan kemandirian bukan lawan — yang satu adalah landasan "
         "bagi yang lain."),
        ("Watch a toddler at a playground: they move out, glance back to check you are "
         "still there, and move out further. The glance is the whole mechanism.",
         "Perhatikan balita di taman bermain: dia menjauh, menoleh memastikan Anda masih "
         "di sana, lalu menjauh lebih jauh lagi. Tolehan itulah seluruh mekanismenya."),
        ("Be findable today. When your child looks over, look back and let them see it.",
         "Jadilah mudah ditemukan hari ini. Saat anak menoleh, balas tatapannya dan "
         "biarkan dia melihatnya."),
        ("Does my child know where home is when something goes wrong?",
         "Apakah anak tahu ke mana pulang saat ada yang tidak beres?"),
        ("\"Go on — I'll be right here when you come back.\"",
         "\"Main saja — Mama/Papa di sini saat kamu kembali.\""),
    ),
    14: d(
        ("Repair after conflict",
         "Memperbaiki setelah bentrok"),
        ("Every parent ruptures the relationship sometimes — the sharp word, the unfair "
         "reaction, the door closed too hard. What shapes a child is not the absence of "
         "rupture but the presence of repair. Repair also teaches the exact skill you "
         "most want them to have in their own future relationships.",
         "Setiap orang tua kadang merobek hubungan — kata yang tajam, reaksi yang tak "
         "adil, pintu yang ditutup terlalu keras. Yang membentuk anak bukan tiadanya "
         "keretakan, melainkan adanya perbaikan. Memperbaiki juga mengajarkan persis "
         "keterampilan yang paling Anda inginkan dia miliki dalam hubungannya kelak."),
        ("\"I was angry earlier and I spoke to you in a way I didn't like. That wasn't "
         "about you.\" It costs a minute and it repairs a great deal.",
         "\"Tadi Mama marah dan bicara dengan cara yang Mama sendiri tidak suka. Itu bukan "
         "salahmu.\" Butuh semenit, dan memperbaiki banyak hal."),
        ("If something went wrong between you today, go back and repair it before bed. "
         "Short is fine.",
         "Jika hari ini ada yang keliru di antara kalian, kembalilah dan perbaiki sebelum "
         "tidur. Singkat pun cukup."),
        ("What is still unrepaired between my child and me from this week?",
         "Apa yang masih belum diperbaiki antara saya dan anak minggu ini?"),
        ("\"I got that wrong earlier. Can we start again?\"",
         "\"Tadi Mama/Papa keliru. Boleh kita mulai lagi?\""),
    ),
    15: d(
        ("Progress over perfection",
         "Kemajuan, bukan kesempurnaan"),
        ("Nobody parents well every day, and the standard was never every day. Research "
         "on secure attachment suggests parents get it right roughly a third of the "
         "time and repair much of the rest. Aim for the direction of travel, not a "
         "spotless record.",
         "Tidak ada yang mengasuh dengan baik setiap hari, dan standarnya memang bukan "
         "setiap hari. Penelitian tentang kelekatan aman menunjukkan orang tua tepat "
         "kira-kira sepertiga waktu, dan memperbaiki sebagian besar sisanya. Kejar arah "
         "perjalanannya, bukan catatan tanpa cela."),
        ("A parent who loses their temper on Tuesday and repairs on Wednesday is "
         "teaching more than a parent who never loses it and never has to model repair.",
         "Orang tua yang hilang kesabaran hari Selasa lalu memperbaikinya hari Rabu "
         "mengajarkan lebih banyak daripada orang tua yang tidak pernah lepas kendali dan "
         "tak pernah perlu mencontohkan perbaikan."),
        ("Name one thing you did better this week than last month. Let it count.",
         "Sebutkan satu hal yang Anda lakukan lebih baik minggu ini dibanding bulan lalu. "
         "Akui itu."),
        ("Am I measuring myself against a real parent, or an imaginary one?",
         "Saya mengukur diri dengan orang tua yang nyata, atau yang khayalan?"),
        ("\"I'm still learning this too.\"",
         "\"Mama/Papa juga masih belajar.\""),
    ),
    16: d(
        ("Parenting under stress",
         "Mengasuh dalam tekanan"),
        ("Your capacity to parent well is not a fixed trait — it moves with your sleep, "
         "your money worries, your marriage and your health. This is not an excuse; it "
         "is information. Parents who plan for their low-capacity hours do far better "
         "than parents who expect to be at their best always.",
         "Kapasitas Anda mengasuh dengan baik bukan sifat tetap — ia bergerak mengikuti "
         "tidur Anda, kekhawatiran keuangan, pernikahan, dan kesehatan Anda. Ini bukan "
         "pembenaran; ini informasi. Orang tua yang menyiapkan diri untuk jam-jam "
         "berkapasitas rendah jauh lebih baik daripada yang berharap selalu prima."),
        ("If 6pm is when you have least left, that is the hour to simplify: fewer "
         "demands, easier dinner, lower standards, earlier bath.",
         "Jika pukul enam sore adalah saat tenaga Anda paling sedikit, itulah jam untuk "
         "menyederhanakan: lebih sedikit tuntutan, makan malam yang mudah, standar yang "
         "diturunkan, mandi lebih awal."),
        ("Identify your lowest-capacity hour today and remove one demand from it.",
         "Kenali jam dengan kapasitas terendah Anda hari ini dan hapus satu tuntutan dari jam itu."),
        ("What am I asking of myself at the hour I have least to give?",
         "Apa yang saya tuntut dari diri sendiri di jam saat saya paling tidak punya tenaga?"),
        ("\"This is a hard week, not a hard child.\"",
         "\"Ini minggu yang berat, bukan anak yang sulit.\""),
    ),
    17: d(
        ("Intergenerational patterns",
         "Pola antargenerasi"),
        ("You are parenting with a script you did not write. Some of it is a gift and "
         "some of it is inherited damage, and most parents cannot tell which is which "
         "until they look. Naming the script is what gives you a choice about keeping it.",
         "Anda mengasuh dengan naskah yang tidak Anda tulis. Sebagiannya adalah anugerah "
         "dan sebagiannya luka warisan, dan kebanyakan orang tua tak bisa membedakan "
         "keduanya sampai mereka menengoknya. Menamai naskah itulah yang memberi Anda "
         "pilihan untuk menyimpannya atau tidak."),
        ("A parent who was never comforted when upset often finds a crying child "
         "unbearable — not from lack of love, but because nobody ever showed them what "
         "comfort looks like.",
         "Orang tua yang dulu tak pernah ditenangkan saat sedih sering merasa tak tahan "
         "melihat anak menangis — bukan karena kurang sayang, tapi karena tak ada yang "
         "pernah menunjukkan seperti apa rupa penghiburan."),
        ("Name one thing from your childhood you are keeping on purpose, and one you are "
         "deliberately not passing on.",
         "Sebutkan satu hal dari masa kecil Anda yang sengaja Anda pertahankan, dan satu "
         "yang sengaja tidak Anda wariskan."),
        ("Which of my reactions belong to my childhood rather than to my child?",
         "Reaksi saya yang mana yang sebenarnya milik masa kecil saya, bukan milik anak saya?"),
        ("\"I get to choose what I pass on.\"",
         "\"Saya yang memilih apa yang saya wariskan.\""),
    ),
    18: d(
        ("Triggers from your own childhood",
         "Pemicu dari masa kecil Anda"),
        ("A trigger is the moment your reaction is far larger than the event. That gap "
         "is almost always old. Disrespect, mess, noise, being ignored — each parent has "
         "their own, and the reaction belongs to a much younger version of you.",
         "Pemicu adalah momen ketika reaksi Anda jauh lebih besar daripada peristiwanya. "
         "Jarak itu hampir selalu berasal dari masa lalu. Ketidaksopanan, berantakan, "
         "berisik, diabaikan — setiap orang tua punya pemicunya sendiri, dan reaksinya "
         "milik versi diri Anda yang jauh lebih muda."),
        ("If an eye-roll produces rage out of all proportion, the rage is rarely about "
         "the eye-roll. It is about what an eye-roll once meant in your house.",
         "Jika mata yang memutar memicu kemarahan yang tidak sebanding, kemarahan itu "
         "jarang soal mata memutarnya. Itu soal apa arti mata memutar dulu di rumah Anda."),
        ("Write down your top three triggers. Notice the one most likely to appear today.",
         "Tuliskan tiga pemicu terbesar Anda. Sadari mana yang paling mungkin muncul hari ini."),
        ("What does my biggest trigger remind me of, when I am honest?",
         "Kalau saya jujur, pemicu terbesar saya mengingatkan saya pada apa?"),
        ("\"This feeling is old. It isn't about my child.\"",
         "\"Perasaan ini lama. Ini bukan tentang anak saya.\""),
    ),
    19: d(
        ("Shame vs responsibility",
         "Rasa malu vs tanggung jawab"),
        ("Responsibility says \"you did something wrong.\" Shame says \"there is something "
         "wrong with you.\" The first grows a conscience; the second grows concealment. "
         "The line between them is usually a single word — the difference between naming "
         "the act and naming the child.",
         "Tanggung jawab berkata \"kamu melakukan hal yang salah.\" Rasa malu berkata \"ada "
         "yang salah dengan dirimu.\" Yang pertama menumbuhkan hati nurani; yang kedua "
         "menumbuhkan kebiasaan menyembunyikan. Batas keduanya biasanya satu kata — beda "
         "antara menyebut perbuatannya dan menyebut anaknya."),
        ("\"That was a lie and lying breaks trust\" teaches. \"You are a liar\" labels — "
         "and children grow into the labels we hand them.",
         "\"Itu bohong, dan bohong merusak kepercayaan\" mengajarkan. \"Kamu pembohong\" "
         "melabeli — dan anak tumbuh menjadi label yang kita berikan."),
        ("Catch one correction today and check it names the behavior, not the child.",
         "Perhatikan satu teguran hari ini dan pastikan ia menyebut perilakunya, bukan anaknya."),
        ("Do my corrections tell my child they made a bad choice, or that they are bad?",
         "Apakah teguran saya memberi tahu anak bahwa dia salah memilih, atau bahwa dia buruk?"),
        ("\"That choice wasn't okay. You are.\"",
         "\"Pilihan itu tidak benar. Tapi kamu tetap baik.\""),
    ),
    20: d(
        ("The role of empathy",
         "Peran empati"),
        ("Empathy is not agreement and it is not surrender. It is showing a child that "
         "their experience registered with you before you deal with the behavior. "
         "Children who feel understood argue less, because most of the fight was about "
         "not being understood in the first place.",
         "Empati bukan persetujuan dan bukan menyerah. Ia adalah menunjukkan kepada anak "
         "bahwa pengalamannya tercatat oleh Anda sebelum Anda menangani perilakunya. Anak "
         "yang merasa dimengerti lebih sedikit membantah, karena sebagian besar "
         "pertengkarannya memang tentang tidak dimengerti."),
        ("\"You really wanted to keep playing, and it's time to stop\" gets further than "
         "\"stop making a fuss\" — and it does not concede the limit at all.",
         "\"Kamu benar-benar masih ingin main, dan sekarang waktunya berhenti\" lebih "
         "berhasil daripada \"jangan rewel\" — dan sama sekali tidak melunakkan batasannya."),
        ("Say the feeling out loud once today before you say the rule.",
         "Ucapkan perasaannya sekali hari ini sebelum Anda menyebut aturannya."),
        ("How often does my child hear me name what they are feeling?",
         "Seberapa sering anak mendengar saya menyebutkan apa yang dia rasakan?"),
        ("\"You wanted that a lot. That's hard.\"",
         "\"Kamu sangat menginginkannya. Itu berat, ya.\""),
    ),
    21: d(
        ("Firmness without anger",
         "Tegas tanpa marah"),
        ("Firmness is about the limit; anger is about your state. They travel together "
         "so often that many parents believe they need the anger to hold the line. They "
         "do not. A limit held calmly is actually harder for a child to argue with than "
         "one held loudly.",
         "Ketegasan adalah soal batasannya; kemarahan adalah soal kondisi Anda. Keduanya "
         "begitu sering datang bersamaan sampai banyak orang tua percaya mereka butuh "
         "marah untuk memegang batas. Tidak. Batas yang dipegang dengan tenang justru "
         "lebih sulit dibantah anak daripada yang dipegang dengan suara keras."),
        ("The quiet \"no, and I mean it\" tends to end a negotiation faster than shouting, "
         "because there is nothing in it for the child to push against.",
         "\"Tidak, dan Mama serius\" yang diucapkan pelan cenderung mengakhiri tawar-menawar "
         "lebih cepat daripada teriakan, karena tak ada yang bisa didorong balik oleh anak."),
        ("Hold one limit today at half your usual volume and notice what changes.",
         "Pegang satu batasan hari ini dengan setengah volume biasa Anda, dan perhatikan "
         "apa yang berubah."),
        ("Do I need the anger to hold the limit, or have I just always used it?",
         "Apakah saya butuh marah untuk memegang batas, atau selama ini memang begitu kebiasaannya?"),
        ("\"The answer is no. I'm not upset with you.\"",
         "\"Jawabannya tidak. Mama/Papa tidak sedang marah padamu.\""),
    ),
    22: d(
        ("Consistency without rigidity",
         "Konsisten tanpa kaku"),
        ("Consistency means a child can predict you. Rigidity means you cannot respond "
         "to what is actually happening. The useful version keeps the principle fixed "
         "and lets the application flex — the bedtime holds, but the bedtime on the "
         "night of a funeral does not have to.",
         "Konsisten berarti anak bisa menebak Anda. Kaku berarti Anda tak bisa menanggapi "
         "apa yang sungguh terjadi. Versi yang berguna menjaga prinsipnya tetap dan "
         "membiarkan penerapannya lentur — jam tidur tetap berlaku, tapi jam tidur di "
         "malam sebuah pemakaman tidak harus."),
        ("Bending once for a real reason, and saying why, does not undo a rule. Bending "
         "randomly, without explanation, is what teaches a child to keep testing.",
         "Melonggarkan sekali karena alasan yang nyata, dan mengatakan alasannya, tidak "
         "membatalkan aturan. Melonggarkan sembarangan tanpa penjelasan itulah yang "
         "mengajari anak untuk terus menguji."),
        ("If you make an exception today, name it out loud as an exception.",
         "Jika hari ini Anda membuat pengecualian, sebutkan dengan jelas bahwa itu pengecualian."),
        ("Are my rules predictable enough for my child to rely on?",
         "Apakah aturan saya cukup bisa ditebak untuk dijadikan pegangan anak?"),
        ("\"Tonight is different, and here's why.\"",
         "\"Malam ini berbeda, dan ini alasannya.\""),
    ),
    23: d(
        ("Why routines matter",
         "Mengapa rutinitas penting"),
        ("A routine is a decision you only have to make once. It removes the negotiation "
         "from the parts of the day that reliably go wrong, and it lets a child know "
         "what comes next — which is, for a small person, a genuine form of safety.",
         "Rutinitas adalah keputusan yang hanya perlu Anda buat sekali. Ia menghapus "
         "tawar-menawar dari bagian hari yang selalu berantakan, dan membuat anak tahu "
         "apa yang datang berikutnya — yang bagi orang kecil adalah bentuk rasa aman yang sungguhan."),
        ("Families who fight nightly about bedtime usually do not have a bedtime problem. "
         "They have a bedtime that gets renegotiated every single night.",
         "Keluarga yang bertengkar setiap malam soal jam tidur biasanya tidak punya "
         "masalah jam tidur. Mereka punya jam tidur yang dinegosiasi ulang setiap malam."),
        ("Pick the messiest transition of your day and write down its steps in a fixed "
         "order.",
         "Pilih perpindahan paling berantakan dalam hari Anda dan tuliskan langkah-langkahnya "
         "dalam urutan yang tetap."),
        ("Which daily argument would simply disappear if the order never changed?",
         "Pertengkaran harian mana yang akan hilang begitu saja jika urutannya tak pernah berubah?"),
        ("\"First this, then that. Same as always.\"",
         "\"Ini dulu, baru itu. Seperti biasa.\""),
    ),
    24: d(
        ("Parenting with intention",
         "Mengasuh dengan niat"),
        ("Most parenting happens on autopilot, which is fine for most of the day. But a "
         "family drifts in whatever direction its habits point. Ten minutes of intention "
         "a week is usually enough to notice the drift and correct the heading.",
         "Sebagian besar pengasuhan berjalan otomatis, dan itu wajar untuk sebagian besar "
         "hari. Tapi keluarga hanyut ke arah yang ditunjuk kebiasaannya. Sepuluh menit "
         "niat dalam seminggu biasanya cukup untuk menyadari hanyutnya dan membetulkan arah."),
        ("The difference between a home that drifts and a home that grows is rarely "
         "effort. It is usually one recurring moment of noticing.",
         "Beda antara rumah yang hanyut dan rumah yang bertumbuh jarang soal usaha. "
         "Biasanya soal satu momen menyadari yang berulang."),
        ("Choose one quality you want more of in your home this month and one action "
         "that serves it.",
         "Pilih satu kualitas yang ingin Anda perbanyak di rumah bulan ini dan satu "
         "tindakan yang mendukungnya."),
        ("If nothing changed, where would our family be a year from now?",
         "Jika tak ada yang berubah, keluarga kami akan ada di mana setahun lagi?"),
        ("\"This is the kind of family we're building.\"",
         "\"Ini keluarga yang sedang kita bangun.\""),
    ),
    25: d(
        ("Emotional safety at home",
         "Rasa aman emosional di rumah"),
        ("Emotional safety is a child's confidence that having a feeling here will not "
         "cost them the relationship. In homes where anger or sadness is punished, "
         "children do not stop feeling — they stop telling. And a child who stops "
         "telling is much harder to protect.",
         "Rasa aman emosional adalah keyakinan anak bahwa memiliki perasaan di rumah ini "
         "tidak akan merenggut hubungannya dengan Anda. Di rumah yang menghukum marah "
         "atau sedih, anak tidak berhenti merasa — mereka berhenti bercerita. Dan anak "
         "yang berhenti bercerita jauh lebih sulit dilindungi."),
        ("The teenager who tells you the difficult thing at 11pm is not a discipline "
         "failure. It is the return on years of safe reactions.",
         "Remaja yang menceritakan hal sulit kepada Anda pukul sebelas malam bukan "
         "kegagalan disiplin. Itu hasil dari bertahun-tahun reaksi yang aman."),
        ("Receive one difficult feeling today without correcting, fixing or minimising it.",
         "Terima satu perasaan sulit hari ini tanpa membetulkan, memperbaiki, atau mengecilkannya."),
        ("Which feelings are not allowed in our home — and what happens to them instead?",
         "Perasaan apa yang tidak boleh ada di rumah kami — dan ke mana perasaan itu pergi?"),
        ("\"You can tell me. I can handle it.\"",
         "\"Kamu boleh cerita. Mama/Papa sanggup mendengarnya.\""),
    ),
    26: d(
        ("How children learn by imitation",
         "Bagaimana anak belajar dengan meniru"),
        ("Children copy what you do far more reliably than what you say, and they copy "
         "it most exactly when you are under pressure. Your behavior in a difficult "
         "moment is the lesson, whatever words accompany it.",
         "Anak meniru apa yang Anda lakukan jauh lebih setia daripada apa yang Anda "
         "katakan, dan mereka menirunya paling persis saat Anda tertekan. Perilaku Anda "
         "di momen sulit itulah pelajarannya, apa pun kata-kata yang menyertainya."),
        ("A parent who shouts \"we don't shout in this house\" has taught the shouting, "
         "not the rule. Children learn the demonstration, not the sentence.",
         "Orang tua yang berteriak \"di rumah ini kita tidak berteriak\" telah mengajarkan "
         "teriakannya, bukan aturannya. Anak belajar dari peragaan, bukan dari kalimatnya."),
        ("Pick one behavior you want from your child and demonstrate it visibly today.",
         "Pilih satu perilaku yang Anda inginkan dari anak dan peragakan dengan jelas hari ini."),
        ("What is my child learning from watching me that I have never actually taught?",
         "Apa yang anak pelajari dari mengamati saya, yang sebenarnya tak pernah saya ajarkan?"),
        ("\"Watch how I handle this one.\"",
         "\"Lihat bagaimana Mama/Papa menghadapi ini.\""),
    ),
    27: d(
        ("Modeling respect",
         "Mencontohkan rasa hormat"),
        ("Respect is taught by being given, not by being demanded. A child spoken to "
         "with courtesy in ordinary moments learns the sound of it and reproduces it. "
         "Respect extracted by force teaches only that the powerful may speak however "
         "they like.",
         "Rasa hormat diajarkan dengan diberikan, bukan dengan dituntut. Anak yang diajak "
         "bicara dengan sopan di momen-momen biasa belajar bunyinya dan menirukannya. "
         "Rasa hormat yang dipaksakan hanya mengajarkan bahwa yang berkuasa boleh bicara "
         "sesukanya."),
        ("Interrupting a child mid-sentence while asking them not to interrupt you is a "
         "lesson — just not the one intended.",
         "Memotong kalimat anak sambil memintanya tidak memotong bicara Anda tetap sebuah "
         "pelajaran — hanya bukan yang dimaksudkan."),
        ("Use please, thank you, and excuse me with your child today as deliberately as "
         "you would with a guest.",
         "Gunakan tolong, terima kasih, dan permisi kepada anak hari ini, sesengaja Anda "
         "menggunakannya kepada tamu."),
        ("Would I speak to a friend the way I spoke to my child today?",
         "Apakah saya akan bicara kepada teman dengan cara saya bicara kepada anak hari ini?"),
        ("\"Thank you for waiting. That helped me.\"",
         "\"Terima kasih sudah menunggu. Itu membantu Mama/Papa.\""),
    ),
    28: d(
        ("Modeling apology",
         "Mencontohkan permintaan maaf"),
        ("An apology from a parent does not weaken authority; it demonstrates that "
         "authority and accountability can live in the same person. A child who has "
         "never seen an adult apologise well has no working template for repairing "
         "their own mistakes.",
         "Permintaan maaf dari orang tua tidak melemahkan wibawa; ia menunjukkan bahwa "
         "wibawa dan tanggung jawab bisa ada pada orang yang sama. Anak yang belum pernah "
         "melihat orang dewasa meminta maaf dengan baik tak punya contoh untuk memperbaiki "
         "kesalahannya sendiri."),
        ("A real apology names the act, owns it, and stops: \"I snapped at you. That "
         "wasn't fair.\" No \"but you were\" attached to the end.",
         "Permintaan maaf yang sungguh menyebut perbuatannya, mengakuinya, lalu berhenti: "
         "\"Mama membentakmu tadi. Itu tidak adil.\" Tanpa \"tapi kamu tadi\" di ujungnya."),
        ("If you owe your child an apology today, give it without adding a justification.",
         "Jika hari ini Anda berhutang maaf kepada anak, berikanlah tanpa menambahkan pembenaran."),
        ("When was the last time my child heard me apologise without a \"but\"?",
         "Kapan terakhir kali anak mendengar saya minta maaf tanpa \"tapi\"?"),
        ("\"I was wrong, and I'm sorry.\"",
         "\"Mama/Papa salah, dan minta maaf.\""),
    ),
    29: d(
        ("Modeling calm",
         "Mencontohkan ketenangan"),
        ("Your calm is contagious, and so is your escalation. Children read tone, face "
         "and body long before they process the words. Managing your own state in a "
         "difficult moment is not avoiding the discipline — it is the first and largest "
         "part of it.",
         "Ketenangan Anda menular, begitu juga kepanikan Anda. Anak membaca nada, wajah, "
         "dan tubuh jauh sebelum mengolah kata-kata. Mengelola kondisi diri di momen "
         "sulit bukan menghindari disiplin — itu bagian pertama dan terbesar darinya."),
        ("Naming your own state out loud does double duty: it steadies you, and it shows "
         "your child that feelings can be handled rather than obeyed.",
         "Menyebutkan kondisi Anda sendiri dengan suara keras berfungsi ganda: menenangkan "
         "Anda, dan menunjukkan kepada anak bahwa perasaan bisa dikelola, bukan dituruti."),
        ("Take one breath before you respond to the first difficult thing today. Just one.",
         "Tarik satu napas sebelum menanggapi hal sulit pertama hari ini. Satu saja."),
        ("What does my child see on my face before I have said anything at all?",
         "Apa yang anak lihat di wajah saya sebelum saya mengucapkan apa pun?"),
        ("\"I need a moment to steady myself first.\"",
         "\"Mama/Papa perlu sebentar untuk menenangkan diri dulu.\""),
    ),
    30: d(
        ("Family culture and values",
         "Budaya dan nilai keluarga"),
        ("Every family already has a culture — a set of things that are normal here. It "
         "forms whether or not anyone chose it, out of what gets repeated, praised and "
         "tolerated. Naming it out loud is what turns an accident into an inheritance.",
         "Setiap keluarga sudah punya budaya — sekumpulan hal yang dianggap wajar di sini. "
         "Ia terbentuk entah ada yang memilihnya atau tidak, dari apa yang diulang, dipuji, "
         "dan dibiarkan. Menyebutkannya dengan lantang itulah yang mengubah kebetulan "
         "menjadi warisan."),
        ("\"In our family, we tell the truth even when it's expensive.\" Said often "
         "enough, that sentence becomes something a child carries out of the house.",
         "\"Di keluarga kita, kita berkata jujur meski itu mahal harganya.\" Diucapkan cukup "
         "sering, kalimat itu menjadi sesuatu yang dibawa anak keluar dari rumah."),
        ("Say one \"in our family, we…\" sentence out loud today and mean it.",
         "Ucapkan satu kalimat \"di keluarga kita, kita…\" hari ini, dan sungguh-sungguhi."),
        ("If my child described our family in three words, what would they say?",
         "Jika anak menggambarkan keluarga kami dalam tiga kata, apa yang akan dia sebut?"),
        ("\"In our family, this is how we do it.\"",
         "\"Di keluarga kita, begini caranya.\""),
    ),
    31: d(
        ("Weekly reflection habit",
         "Kebiasaan refleksi mingguan"),
        ("Reading about parenting changes very little. Reflecting on your own week "
         "changes a great deal, because it is the only way you see your own patterns "
         "instead of your intentions. Twenty minutes, once a week, outperforms any "
         "amount of good advice.",
         "Membaca tentang pengasuhan mengubah sangat sedikit. Merenungkan minggu Anda "
         "sendiri mengubah banyak hal, karena hanya itu cara Anda melihat pola diri, "
         "bukan niat diri. Dua puluh menit, sekali seminggu, mengalahkan nasihat baik "
         "sebanyak apa pun."),
        ("The parents who change are rarely the ones who read most. They are the ones "
         "who stop once a week and ask what actually happened.",
         "Orang tua yang berubah jarang mereka yang paling banyak membaca. Mereka adalah "
         "yang berhenti sekali seminggu dan bertanya apa yang sebenarnya terjadi."),
        ("Set a repeating time this week for one short review. Put it in your calendar now.",
         "Tentukan waktu tetap minggu ini untuk satu tinjauan singkat. Masukkan ke kalender "
         "Anda sekarang."),
        ("What did this week teach me about the parent I am becoming?",
         "Apa yang minggu ini ajarkan tentang orang tua seperti apa saya sedang menjadi?"),
        ("\"Let's look back at the week together.\"",
         "\"Ayo kita tengok kembali minggu ini bersama.\""),
    ),
}
