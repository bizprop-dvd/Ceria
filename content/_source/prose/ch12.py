# Chapter 12 — Integration & Advanced Practice (days 327-365)
#
# Grounded in the founder's guidebook chapter 12 ("Lasting change comes from
# reflection plus small repeated adjustments — not inspiration") and toolkit
# tool 12 (Monthly Family Review).
#
# Through-line: this chapter does not add new material. It turns the previous
# eleven chapters into a working practice — diagnose, change one thing, review
# on a rhythm. Day 329 carries a grid of the four places a repeating problem
# actually lives. Day 350 carries an ordered four-move plan for public
# meltdowns.

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
    327: d(
        ("Reviewing your parenting values",
         "Meninjau nilai pengasuhan Anda"),
        ("Most parents have never written down what they are actually trying to build. They "
         "have inherited a set of values from their own upbringing, absorbed a few more from "
         "the culture around them, and are running on the mix without ever having looked at "
         "it.\n\n"
         "Look at it now. Not the values you would say in public — the ones your daily "
         "behaviour reveals. If a stranger watched your family for a week, what would they "
         "conclude that you value most? The gap between that answer and the one you would give "
         "out loud is the whole work of this final chapter.",
         "Kebanyakan orang tua tidak pernah menuliskan apa yang sebenarnya ingin mereka bangun. "
         "Mereka mewarisi seperangkat nilai dari pengasuhan mereka sendiri, menyerap beberapa "
         "lagi dari budaya di sekitarnya, dan menjalankan campuran itu tanpa pernah "
         "memeriksanya.\n\n"
         "Periksalah sekarang. Bukan nilai yang akan Anda sebutkan di depan umum — melainkan "
         "nilai yang terungkap dari perilaku harian Anda. Kalau ada orang asing mengamati "
         "keluarga Anda selama seminggu, ia akan menyimpulkan Anda paling menghargai apa? Jurang "
         "antara jawaban itu dan jawaban yang akan Anda ucapkan adalah seluruh pekerjaan bab "
         "terakhir ini."),
        ("Write down three values. Then, honestly, write what a week of watching your family "
         "would suggest instead.",
         "Tuliskan tiga nilai. Lalu, dengan jujur, tuliskan apa yang akan disimpulkan seseorang "
         "setelah seminggu mengamati keluarga Anda."),
        ("Write your three most important parenting values in your own words.",
         "Tuliskan tiga nilai pengasuhan Anda yang paling penting dengan kata-kata Anda sendiri."),
        ("What would a week of watching my family say I value?",
         "Kalau ada yang mengamati keluarga saya seminggu, ia akan bilang saya menghargai apa?"),
        ("\"In this family, the thing that matters most to me is...\"",
         "\"Di keluarga ini, hal yang paling penting buat Mama/Papa adalah...\""),
    ),

    328: d(
        ("What is working in your home",
         "Apa yang sudah berjalan baik di rumah Anda"),
        ("Start the review with what works, and not as a courtesy. Parents are trained by "
         "worry to scan for problems, which means the things going well are genuinely "
         "invisible to them — not undervalued, actually unseen.\n\n"
         "Naming what works has a practical purpose beyond morale. Whatever is already "
         "functioning contains the mechanism you will use to fix what is not. If bedtime works "
         "and mornings do not, bedtime is holding a piece of structure that mornings are "
         "missing, and finding it is faster than inventing something new.",
         "Mulailah peninjauan dari apa yang sudah berjalan, dan bukan sekadar basa-basi. Orang "
         "tua dilatih oleh kekhawatiran untuk memindai masalah, artinya hal-hal yang berjalan "
         "baik benar-benar tidak terlihat oleh mereka — bukan kurang dihargai, tapi memang tak "
         "terlihat.\n\n"
         "Menyebut apa yang berhasil punya guna praktis di luar penyemangat. Apa pun yang sudah "
         "berfungsi menyimpan mekanisme yang akan Anda pakai untuk memperbaiki yang belum. Kalau "
         "waktu tidur berjalan baik dan pagi hari tidak, waktu tidur sedang memegang sepotong "
         "struktur yang tidak dimiliki pagi hari, dan menemukannya lebih cepat daripada "
         "mengarang sesuatu yang baru."),
        ("List three things that work, then ask what they have in common. That common thread "
         "is your family's operating principle.",
         "Daftarkan tiga hal yang berjalan baik, lalu tanyakan apa kesamaannya. Benang merah itu "
         "adalah prinsip kerja keluarga Anda."),
        ("Write down three things that genuinely work in your home right now.",
         "Tuliskan tiga hal yang benar-benar berjalan baik di rumah Anda saat ini."),
        ("What is already working that I have stopped noticing?",
         "Apa yang sudah berjalan baik dan berhenti saya sadari?"),
        ("\"We do this part well. I want to say that out loud.\"",
         "\"Bagian ini kita jalankan dengan baik. Mama/Papa mau mengatakannya dengan lantang.\""),
    ),

    329: d(
        ("What keeps repeating",
         "Apa yang terus berulang"),
        ("Every family has two or three problems that come back no matter what is tried, and "
         "the reason they come back is almost never the reason the family assumes.\n\n"
         "A repeating problem is a signal that you have been treating a symptom. Before you try "
         "another technique on it, work out which of the four places below it actually lives. "
         "Getting this diagnosis right is worth more than any amount of extra effort applied to "
         "the wrong layer — most exhausted parents are not under-trying, they are trying in the "
         "wrong place.",
         "Setiap keluarga punya dua atau tiga masalah yang kembali terus apa pun yang dicoba, "
         "dan alasan mereka kembali hampir tidak pernah alasan yang diduga keluarga itu.\n\n"
         "Masalah yang berulang adalah tanda bahwa Anda selama ini menangani gejalanya. Sebelum "
         "mencoba satu teknik lagi, cari tahu masalah itu sebenarnya tinggal di mana dari empat "
         "tempat di bawah. Menegakkan diagnosis ini dengan tepat lebih berharga daripada usaha "
         "tambahan sebanyak apa pun yang diarahkan ke lapisan yang salah — kebanyakan orang tua "
         "yang kelelahan bukan kurang berusaha, mereka berusaha di tempat yang keliru."),
        ("Diagnose the layer before you change the technique. Most repeating problems are "
         "setup problems wearing a behaviour costume.",
         "Tegakkan diagnosis lapisannya sebelum mengganti tekniknya. Kebanyakan masalah berulang "
         "adalah masalah penyiapan yang memakai kostum perilaku."),
        ("Name one repeating problem and decide which layer it actually lives in.",
         "Sebutkan satu masalah yang berulang dan tentukan ia sebenarnya ada di lapisan mana."),
        ("What have I been treating as a behaviour problem that is really a setup problem?",
         "Apa yang selama ini saya perlakukan sebagai masalah perilaku padahal sebenarnya masalah penyiapan?"),
        ("\"This keeps happening. Let's change the situation, not just the reaction.\"",
         "\"Ini terus terjadi. Ayo kita ubah situasinya, bukan cuma reaksinya.\""),
        framework=fw(
            ("Four places a repeating problem lives",
             "Empat tempat masalah berulang bersembunyi"),
            ("Find the layer first. The right fix on the wrong layer still fails.",
             "Temukan lapisannya dulu. Perbaikan yang benar di lapisan yang salah tetap gagal."),
            [
                (("The setup", "Penyiapan"),
                 [("Environment", "Lingkungan"), ("Timing", "Waktu")],
                 ("The problem happens at the same time, in the same place, under the same "
                  "conditions — rushed mornings, the hour before dinner, a room with no space "
                  "to put things.",
                  "Masalahnya terjadi di jam yang sama, tempat yang sama, kondisi yang sama — "
                  "pagi yang terburu-buru, sejam sebelum makan malam, kamar yang tak punya "
                  "tempat menaruh barang."),
                 ("Change the conditions, not the child. This is the most common layer and the "
                  "most often missed.",
                  "Ubah kondisinya, bukan anaknya. Ini lapisan yang paling umum dan paling sering terlewat.")),
                (("The skill", "Keterampilan"),
                 [("Can't yet", "Belum bisa")],
                 ("The child genuinely cannot do what is being asked — cannot wait that long, "
                  "cannot organise that many steps, cannot calm down without help.",
                  "Anak memang belum sanggup melakukan yang diminta — belum bisa menunggu selama "
                  "itu, belum bisa mengatur langkah sebanyak itu, belum bisa menenangkan diri sendiri."),
                 ("Teach and scaffold. Consequences do not install a missing skill, no matter "
                  "how consistently applied.",
                  "Ajarkan dan dampingi. Hukuman tidak memasang keterampilan yang belum ada, "
                  "sekonsisten apa pun diterapkan.")),
                (("The connection", "Kedekatan"),
                 [("Empty tank", "Tangki kosong")],
                 ("The behaviour spikes after absence, after a new sibling, after a stretch of "
                  "busy weeks — and eases after time together.",
                  "Perilakunya memburuk setelah ditinggal, setelah ada adik baru, setelah "
                  "berminggu-minggu yang padat — dan mereda setelah ada waktu bersama."),
                 ("Fill the tank before applying anything else. Ten minutes a day changes this "
                  "layer faster than any rule.",
                  "Isi tangkinya sebelum menerapkan apa pun. Sepuluh menit sehari mengubah "
                  "lapisan ini lebih cepat daripada aturan mana pun.")),
                (("The parent's state", "Kondisi orang tua"),
                 [("Yours", "Milik Anda")],
                 ("The same behaviour is fine on Tuesday and unbearable on Thursday. What "
                  "changed was you — sleep, stress, hunger, a hard week.",
                  "Perilaku yang sama biasa saja hari Selasa dan tak tertahankan hari Kamis. "
                  "Yang berubah adalah Anda — tidur, stres, lapar, minggu yang berat."),
                 ("This is not a failure. It is data. Treat your own state as part of the "
                  "system you are adjusting.",
                  "Ini bukan kegagalan. Ini data. Perlakukan kondisi Anda sendiri sebagai bagian "
                  "dari sistem yang sedang Anda sesuaikan.")),
            ],
        ),
    ),

    330: d(
        ("Identify your top 3 triggers",
         "Kenali 3 pemicu terbesar Anda"),
        ("Your triggers are not random. They cluster around a small number of themes, and each "
         "theme usually has a history — being ignored, being disrespected, feeling out of "
         "control, being made late, mess.\n\n"
         "Naming them does something surprisingly practical. A trigger you have named loses "
         "some of its speed; you get a fraction of a second between the spark and the reaction, "
         "and that fraction is where every good choice you will ever make as a parent lives. "
         "Three is enough. You do not need a complete inventory of yourself to start.",
         "Pemicu Anda tidak acak. Mereka mengumpul di sekitar beberapa tema, dan setiap tema "
         "biasanya punya sejarah — pernah diabaikan, pernah tidak dihormati, merasa lepas "
         "kendali, dibuat terlambat, kekacauan.\n\n"
         "Menyebut namanya melakukan sesuatu yang ternyata sangat praktis. Pemicu yang sudah "
         "Anda beri nama kehilangan sebagian kecepatannya; Anda mendapat sepersekian detik "
         "antara percikan dan reaksi, dan sepersekian detik itulah tempat tinggal setiap pilihan "
         "baik yang akan Anda buat sebagai orang tua. Tiga sudah cukup. Anda tidak perlu "
         "inventaris lengkap tentang diri sendiri untuk memulai."),
        ("Write three. Then notice which one fires most often — that is where the practice "
         "belongs, not spread across all three.",
         "Tulis tiga. Lalu perhatikan mana yang paling sering meletus — di situlah latihannya, "
         "bukan disebar ke ketiganya."),
        ("Write down your three most reliable triggers.",
         "Tuliskan tiga pemicu Anda yang paling sering muncul."),
        ("What do my triggers have in common?",
         "Apa kesamaan dari pemicu-pemicu saya?"),
        ("\"I know this one sets me off. I'm going to slow down here.\"",
         "\"Saya tahu yang ini memicu saya. Di sini saya akan memperlambat diri.\""),
    ),

    331: d(
        ("Identify your child's top 3 triggers",
         "Kenali 3 pemicu terbesar anak Anda"),
        ("Your child has a pattern too, and it is usually more predictable than yours. Hunger "
         "at a particular hour. Transitions without warning. Losing a game. Being rushed. Being "
         "corrected in front of a sibling.\n\n"
         "Once written down, most of these turn out to be preventable rather than manageable — "
         "which is a much better category to be in. A trigger you can see coming stops being a "
         "crisis and becomes a scheduling problem, and scheduling problems are the easiest kind "
         "of parenting problem there is.",
         "Anak Anda juga punya pola, dan biasanya lebih bisa ditebak daripada pola Anda. Lapar "
         "di jam tertentu. Perpindahan kegiatan tanpa peringatan. Kalah main. Diburu-buru. "
         "Ditegur di depan saudaranya.\n\n"
         "Begitu dituliskan, sebagian besar ternyata bisa dicegah alih-alih sekadar dikelola — "
         "dan itu kategori yang jauh lebih baik. Pemicu yang bisa Anda lihat datang berhenti "
         "menjadi krisis dan berubah jadi soal penjadwalan, dan soal penjadwalan adalah jenis "
         "masalah pengasuhan yang paling mudah."),
        ("Write three, then move one from managed to prevented this week.",
         "Tulis tiga, lalu pindahkan satu dari dikelola menjadi dicegah minggu ini."),
        ("Write your child's three most predictable triggers, and prevent one today.",
         "Tuliskan tiga pemicu anak Anda yang paling bisa ditebak, dan cegah satu hari ini."),
        ("Which of my child's meltdowns could I have seen coming an hour earlier?",
         "Ledakan emosi anak saya yang mana yang sebenarnya bisa saya lihat datang sejam sebelumnya?"),
        ("\"I know this bit is hard for you. Let's do it differently today.\"",
         "\"Mama/Papa tahu bagian ini berat buat kamu. Hari ini kita coba cara lain.\""),
    ),

    332: d(
        ("Rewrite one ineffective parenting pattern",
         "Menulis ulang satu pola pengasuhan yang tidak efektif"),
        ("Pick one pattern. Not five — one. The parents who change permanently are almost "
         "always the ones who changed a single thing and held it long enough for it to stop "
         "requiring effort.\n\n"
         "Write it as a swap rather than a resolution. \"I will be more patient\" cannot be "
         "acted on. \"When she refuses to get dressed, I will stop talking and count to ten "
         "before I say anything\" can be done on a specific morning, which means it can also be "
         "practised, missed, and returned to. Resolutions fail because they have no moment "
         "attached.",
         "Pilih satu pola. Bukan lima — satu. Orang tua yang berubah secara permanen hampir "
         "selalu mereka yang mengubah satu hal dan memegangnya cukup lama sampai tidak lagi "
         "butuh usaha.\n\n"
         "Tuliskan sebagai pertukaran, bukan sebagai tekad. \"Saya akan lebih sabar\" tidak bisa "
         "dijalankan. \"Ketika dia menolak berpakaian, saya akan berhenti bicara dan menghitung "
         "sampai sepuluh sebelum mengucapkan apa pun\" bisa dilakukan di pagi yang tertentu, "
         "artinya bisa juga dilatih, terlewat, dan didatangi lagi. Tekad gagal karena tidak "
         "punya momen yang menempel padanya."),
        ("Write it as \"when X happens, I will do Y instead of Z.\" A pattern needs a trigger "
         "and a replacement, not an intention.",
         "Tuliskan sebagai \"ketika X terjadi, saya akan melakukan Y, bukan Z\". Sebuah pola "
         "butuh pemicu dan pengganti, bukan niat."),
        ("Write one when-X-then-Y swap and use it the next time X happens.",
         "Tuliskan satu pertukaran ketika-X-maka-Y dan pakai saat X terjadi berikutnya."),
        ("What is the one pattern I would most like my child not to inherit?",
         "Pola apa yang paling saya harap tidak diwarisi anak saya?"),
        ("\"I'm working on something. You'll see me do it differently.\"",
         "\"Mama/Papa sedang melatih sesuatu. Nanti kamu lihat caranya berbeda.\""),
    ),

    333: d(
        ("Build one new family ritual",
         "Membangun satu ritual keluarga yang baru"),
        ("Rituals are what a child remembers, and almost none of the remembered ones were "
         "expensive. Saturday pancakes. The same song in the car. A particular thing said at "
         "the door every morning.\n\n"
         "What makes a ritual work is not the content but the reliability. It has to happen "
         "whether the week was good or bad, whether anyone is in the mood, whether it is "
         "convenient. That is the entire mechanism: a fixed point in a changing world. Choose "
         "something small enough that you will still be doing it in a year.",
         "Ritual adalah yang diingat anak, dan hampir tidak ada satu pun yang diingat itu mahal. "
         "Panekuk hari Sabtu. Lagu yang sama di mobil. Kalimat tertentu yang diucapkan di pintu "
         "setiap pagi.\n\n"
         "Yang membuat ritual berhasil bukan isinya melainkan keandalannya. Ia harus terjadi "
         "entah minggunya baik atau buruk, entah ada yang sedang mood atau tidak, entah pas atau "
         "tidak. Itulah seluruh mekanismenya: satu titik tetap di dunia yang berubah. Pilih "
         "sesuatu yang cukup kecil sehingga setahun lagi Anda masih menjalankannya."),
        ("Choose small and repeatable over meaningful and occasional. Reliability is the whole "
         "point.",
         "Pilih yang kecil dan bisa diulang daripada yang bermakna tapi sesekali. Keandalan itulah intinya."),
        ("Start one small ritual this week and put it in the same slot every time.",
         "Mulai satu ritual kecil minggu ini dan taruh di slot yang sama setiap kali."),
        ("What will my child tell their own children we always did?",
         "Apa yang akan anak saya ceritakan kepada anaknya sebagai hal yang selalu kami lakukan?"),
        ("\"This is our thing. We do it every week, no matter what.\"",
         "\"Ini kebiasaan kita. Kita lakukan setiap minggu, apa pun yang terjadi.\""),
    ),

    334: d(
        ("Simplify one stressful routine",
         "Menyederhanakan satu rutinitas yang bikin stres"),
        ("Most stressful routines are stressful because they contain more steps than the "
         "available time or the available child can carry. The solution is subtraction, and "
         "parents reach for it last because it feels like lowering standards.\n\n"
         "It is not. Removing two steps from a seven-step bedtime does not make you a worse "
         "parent; it makes bedtime finish. Look at your hardest routine and cut something real "
         "— a step, an expectation, an item of clothing chosen the night before. Simplicity is "
         "an intervention, not a compromise.",
         "Sebagian besar rutinitas yang bikin stres jadi begitu karena berisi lebih banyak "
         "langkah daripada yang sanggup dipikul oleh waktu yang tersedia atau anak yang "
         "tersedia. Solusinya adalah pengurangan, dan orang tua baru meraihnya paling akhir "
         "karena terasa seperti menurunkan standar.\n\n"
         "Bukan begitu. Menghapus dua langkah dari rutinitas tidur yang tujuh langkah tidak "
         "menjadikan Anda orang tua yang lebih buruk; itu membuat waktu tidur selesai. Lihat "
         "rutinitas Anda yang paling berat dan potonglah sesuatu yang nyata — satu langkah, "
         "satu harapan, satu baju yang dipilih malam sebelumnya. Kesederhanaan adalah tindakan, "
         "bukan kompromi."),
        ("Count the steps in your hardest routine, then delete two. If it still works, you "
         "were carrying two steps for nothing.",
         "Hitung langkah dalam rutinitas Anda yang paling berat, lalu hapus dua. Kalau tetap "
         "jalan, berarti dua langkah itu Anda pikul tanpa guna."),
        ("Remove two steps from your hardest daily routine today.",
         "Hapus dua langkah dari rutinitas harian Anda yang paling berat hari ini."),
        ("What am I doing in this routine that nobody would miss?",
         "Apa yang saya lakukan dalam rutinitas ini yang sebenarnya tidak akan dirindukan siapa pun?"),
        ("\"We're cutting this bit. It was making everyone miserable.\"",
         "\"Bagian ini kita hapus. Bikin semua orang sengsara.\""),
    ),

    335: d(
        ("Improve bedtime",
         "Memperbaiki waktu tidur"),
        ("Bedtime resistance is usually about separation rather than sleep. The child is not "
         "fighting rest; they are fighting the end of your company, which is a much more "
         "reasonable thing to fight.\n\n"
         "So front-load the connection instead of rationing it. Ten unhurried minutes at the "
         "start of the routine often shortens the whole thing by twenty, because the child who "
         "has had enough of you stops negotiating for more. Fix the same order of events every "
         "night, keep screens out of the last hour, and be boring after lights out — your "
         "boringness is what lets the day end.",
         "Perlawanan menjelang tidur biasanya soal perpisahan, bukan soal tidur. Anak tidak "
         "sedang melawan istirahat; ia sedang melawan berakhirnya kebersamaan dengan Anda, dan "
         "itu hal yang jauh lebih masuk akal untuk dilawan.\n\n"
         "Jadi tumpuk kedekatannya di depan alih-alih menjatahnya. Sepuluh menit tanpa "
         "terburu-buru di awal rutinitas sering memperpendek keseluruhannya dua puluh menit, "
         "karena anak yang sudah cukup mendapatkan Anda berhenti menawar lagi. Tetapkan urutan "
         "kejadian yang sama setiap malam, jauhkan layar dari satu jam terakhir, dan jadilah "
         "membosankan setelah lampu dimatikan — kebosanan Anda itulah yang membuat hari bisa "
         "berakhir."),
        ("Give the connection first and the routine second. Ten minutes at the start saves "
         "twenty at the end.",
         "Berikan kedekatannya dulu, rutinitasnya belakangan. Sepuluh menit di awal menghemat "
         "dua puluh menit di akhir."),
        ("Give ten unhurried minutes at the start of tonight's bedtime routine.",
         "Berikan sepuluh menit tanpa terburu-buru di awal rutinitas tidur malam ini."),
        ("Is my child fighting sleep or fighting goodbye?",
         "Apakah anak saya melawan tidur atau melawan perpisahan?"),
        ("\"Ten minutes together first, then lights out. Same as always.\"",
         "\"Sepuluh menit bareng dulu, habis itu lampu mati. Seperti biasa.\""),
    ),

    336: d(
        ("Improve mornings",
         "Memperbaiki pagi hari"),
        ("Almost every morning problem is a night-before problem. Clothes, bags, shoes, "
         "documents, and the decision about breakfast can all be moved to a time when nobody is "
         "under pressure, and moving them is worth more than any amount of shouting at "
         "seven-fifteen.\n\n"
         "The other half is the wake-up itself. A child dragged from sleep into instruction "
         "starts the day in resistance. Wake them a few minutes earlier than strictly needed "
         "and give the first two of those minutes to warmth rather than logistics. It sounds "
         "sentimental and it measurably changes how the next hour goes.",
         "Hampir semua masalah pagi hari sebenarnya masalah malam sebelumnya. Baju, tas, sepatu, "
         "dokumen, dan keputusan soal sarapan semuanya bisa dipindahkan ke waktu ketika tidak "
         "ada yang tertekan, dan memindahkannya lebih berharga daripada bentakan sebanyak apa "
         "pun pada pukul tujuh lewat lima belas.\n\n"
         "Separuh lainnya adalah cara membangunkannya. Anak yang diseret dari tidur langsung ke "
         "instruksi memulai harinya dengan perlawanan. Bangunkan beberapa menit lebih awal dari "
         "yang sebenarnya perlu dan berikan dua menit pertama untuk kehangatan, bukan urusan "
         "logistik. Kedengarannya melankolis dan itu terukur mengubah jalannya satu jam berikutnya."),
        ("Move every decision to the night before, and give the first two minutes of the day "
         "to warmth instead of instructions.",
         "Pindahkan setiap keputusan ke malam sebelumnya, dan berikan dua menit pertama hari itu "
         "untuk kehangatan, bukan instruksi."),
        ("Prepare tomorrow morning tonight, and wake your child gently.",
         "Siapkan pagi besok malam ini, dan bangunkan anak Anda dengan lembut."),
        ("How does the first sentence of the day sound in my house?",
         "Bagaimana bunyi kalimat pertama di hari itu di rumah saya?"),
        ("\"Morning. Two more minutes, then we start.\"",
         "\"Pagi. Dua menit lagi, baru kita mulai.\""),
    ),

    337: d(
        ("Improve sibling relations",
         "Memperbaiki hubungan antar saudara"),
        ("Sibling conflict is worsened by the two things parents most naturally do: judging "
         "who started it and comparing the children. The first turns every fight into a court "
         "case worth arguing; the second creates a permanent rivalry that has nothing to do "
         "with the toy.\n\n"
         "Stop refereeing small disputes. Describe the problem, hand it back, and let them "
         "solve it — \"there is one ball and two of you, that is a hard problem\" is often "
         "enough. Step in fully for anything physical or cruel. And find them something to do "
         "together on the same side; shared work builds alliance faster than any lecture about "
         "being kind.",
         "Konflik antar saudara diperburuk oleh dua hal yang paling alami dilakukan orang tua: "
         "menghakimi siapa yang memulai dan membandingkan anak-anaknya. Yang pertama mengubah "
         "setiap pertengkaran menjadi sidang yang layak diperdebatkan; yang kedua menciptakan "
         "persaingan permanen yang sama sekali tidak ada hubungannya dengan mainan itu.\n\n"
         "Berhentilah menjadi wasit untuk perselisihan kecil. Gambarkan masalahnya, kembalikan "
         "kepada mereka, dan biarkan mereka menyelesaikannya — \"bolanya satu, kalian dua, itu "
         "masalah yang sulit\" sering sudah cukup. Turun tangan penuh untuk apa pun yang fisik "
         "atau kejam. Dan carikan mereka sesuatu untuk dikerjakan bersama di pihak yang sama; "
         "kerja bersama membangun persekutuan lebih cepat daripada ceramah tentang berbaik hati."),
        ("Describe the problem and hand it back. Intervene fully only for physical harm or "
         "cruelty — and never compare them.",
         "Gambarkan masalahnya dan kembalikan kepada mereka. Turun tangan penuh hanya untuk "
         "kekerasan fisik atau kekejaman — dan jangan pernah membandingkan mereka."),
        ("Hand one sibling dispute back to them today instead of judging it.",
         "Kembalikan satu perselisihan antar saudara kepada mereka hari ini alih-alih menghakiminya."),
        ("Am I a judge in this house, or a coach?",
         "Apakah saya hakim di rumah ini, atau pelatih?"),
        ("\"Two of you, one ball. That's a hard problem. I'll be in the kitchen.\"",
         "\"Kalian berdua, bolanya satu. Itu masalah yang sulit. Mama/Papa di dapur, ya.\""),
    ),

    338: d(
        ("Improve listening at home",
         "Memperbaiki cara mendengarkan di rumah"),
        ("Children stop talking to parents who fix, advise, or correct — not immediately, but "
         "steadily, over years, until one day a teenager answers everything with \"nothing.\"\n\n"
         "The repair is unglamorous and it works: listen without solving. Reflect back what you "
         "heard before responding to it. Ask one more question instead of offering one answer. "
         "Most children do not want the problem taken away; they want the experience of being "
         "accurately heard by someone who matters, and they will keep coming back to whoever "
         "gives them that.",
         "Anak berhenti bicara kepada orang tua yang membetulkan, menasihati, atau mengoreksi — "
         "tidak seketika, tapi terus-menerus, bertahun-tahun, sampai suatu hari seorang remaja "
         "menjawab semuanya dengan \"nggak ada apa-apa\".\n\n"
         "Perbaikannya tidak megah dan itu berhasil: dengarkan tanpa menyelesaikan. Pantulkan "
         "kembali apa yang Anda dengar sebelum menanggapinya. Ajukan satu pertanyaan lagi "
         "alih-alih menawarkan satu jawaban. Kebanyakan anak tidak ingin masalahnya diambil; "
         "mereka ingin pengalaman didengar dengan tepat oleh orang yang berarti, dan mereka akan "
         "terus kembali kepada siapa pun yang memberikan itu."),
        ("Reflect before you respond. \"So it felt unfair\" earns more of the story than any "
         "advice you could give.",
         "Pantulkan sebelum menanggapi. \"Jadi rasanya tidak adil, ya\" mendapatkan lebih banyak "
         "cerita daripada nasihat apa pun yang bisa Anda berikan."),
        ("Listen to one thing today without solving any part of it.",
         "Dengarkan satu hal hari ini tanpa menyelesaikan bagian mana pun darinya."),
        ("When my child talks, am I listening or preparing my reply?",
         "Ketika anak saya bicara, apakah saya mendengarkan atau menyiapkan jawaban?"),
        ("\"That sounds hard. Tell me more.\"",
         "\"Kedengarannya berat. Cerita lagi, dong.\""),
    ),

    339: d(
        ("Improve repair after conflict",
         "Memperbaiki cara berbaikan setelah konflik"),
        ("A family is not measured by how rarely it fights but by how reliably it comes back "
         "together afterwards. Children who grow up watching conflict end in repair learn that "
         "relationships are durable. Children who watch conflict end in silence learn that "
         "closeness is conditional and fragile.\n\n"
         "Make repair a house habit rather than an event. It does not require a long "
         "conversation — a hand on a shoulder, a returned presence, one honest sentence. What "
         "matters is that it always happens, and that the adult goes first, every time, without "
         "waiting to see whether the child will.",
         "Sebuah keluarga tidak diukur dari seberapa jarang bertengkar melainkan dari seberapa "
         "andal mereka kembali bersama sesudahnya. Anak yang tumbuh melihat konflik berakhir "
         "dengan perbaikan belajar bahwa hubungan itu tahan lama. Anak yang melihat konflik "
         "berakhir dengan kebisuan belajar bahwa kedekatan itu bersyarat dan rapuh.\n\n"
         "Jadikan berbaikan kebiasaan rumah, bukan peristiwa. Ia tidak butuh percakapan panjang "
         "— tangan di bahu, kehadiran yang kembali, satu kalimat jujur. Yang penting adalah itu "
         "selalu terjadi, dan orang dewasa yang memulai lebih dulu, setiap kali, tanpa menunggu "
         "apakah anaknya akan memulai."),
        ("The adult goes first, always. Waiting for a child to repair first teaches them that "
         "repair is a defeat.",
         "Orang dewasa yang memulai lebih dulu, selalu. Menunggu anak berbaikan lebih dulu "
         "mengajarinya bahwa berbaikan itu kekalahan."),
        ("Go first in one repair today, without waiting.",
         "Mulailah lebih dulu dalam satu perbaikan hari ini, tanpa menunggu."),
        ("How does a fight end in this house?",
         "Bagaimana pertengkaran berakhir di rumah ini?"),
        ("\"We're not finished being okay. Come here.\"",
         "\"Kita belum selesai baik-baik saja. Sini.\""),
    ),

    340: d(
        ("Improve consistency between caregivers",
         "Memperbaiki keselarasan antar pengasuh"),
        ("Consistency between adults matters more than the specific rules being consistent "
         "about. A child can live comfortably under strict rules or relaxed ones. What they "
         "cannot do is live under rules that change depending on who is in the room.\n\n"
         "Agree three rules — only three — with every adult who cares for your child: the "
         "grandparents, the helper, the co-parent. Write them somewhere visible. Everything "
         "else can vary. Three shared certainties do more for a child's sense of safety than "
         "thirty rules that only one adult enforces.",
         "Keselarasan antar orang dewasa lebih penting daripada aturan spesifik yang "
         "diselaraskan. Anak bisa hidup nyaman di bawah aturan yang ketat maupun yang longgar. "
         "Yang tidak bisa mereka lakukan adalah hidup di bawah aturan yang berubah tergantung "
         "siapa yang ada di ruangan.\n\n"
         "Sepakati tiga aturan — hanya tiga — dengan setiap orang dewasa yang mengasuh anak "
         "Anda: kakek-nenek, pengasuh, pasangan. Tuliskan di tempat yang terlihat. Selebihnya "
         "boleh berbeda-beda. Tiga kepastian bersama lebih berguna bagi rasa aman anak daripada "
         "tiga puluh aturan yang hanya ditegakkan satu orang dewasa."),
        ("Three rules, written down, agreed by everyone. Everything else can differ from house "
         "to house and adult to adult.",
         "Tiga aturan, dituliskan, disepakati semua orang. Selebihnya boleh berbeda dari rumah "
         "ke rumah dan dari orang ke orang."),
        ("Agree three shared rules with every adult who cares for your child.",
         "Sepakati tiga aturan bersama dengan setiap orang dewasa yang mengasuh anak Anda."),
        ("Which of our rules survives whoever is in the room?",
         "Aturan kami yang mana yang bertahan siapa pun yang ada di ruangan?"),
        ("\"These three are the same everywhere. The rest is up to whoever's here.\"",
         "\"Tiga ini sama di mana pun. Selebihnya terserah siapa yang sedang di sini.\""),
    ),

    341: d(
        ("Improve your calm-down plan",
         "Memperbaiki rencana menenangkan diri Anda"),
        ("You cannot decide to be calm in the moment you have already lost it. What you can do "
         "is decide, in advance and in writing, what you will do when you feel it starting — "
         "because a plan made in a calm hour is available to a flooded brain in a way that good "
         "intentions are not.\n\n"
         "Make it concrete and small. Where you go. What you say before you go. How long you "
         "stay there. Who you tell. And practise it once while nothing is wrong, so that the "
         "route is familiar before you need it at speed.",
         "Anda tidak bisa memutuskan untuk tenang di saat Anda sudah kehilangan ketenangan. Yang "
         "bisa Anda lakukan adalah memutuskan, di muka dan tertulis, apa yang akan Anda lakukan "
         "ketika mulai terasa — karena rencana yang dibuat di jam yang tenang bisa diakses oleh "
         "otak yang sedang kebanjiran, sementara niat baik tidak.\n\n"
         "Buat konkret dan kecil. Ke mana Anda pergi. Apa yang Anda ucapkan sebelum pergi. "
         "Berapa lama Anda di sana. Kepada siapa Anda memberi tahu. Dan latih sekali saat tidak "
         "ada masalah, supaya jalurnya sudah familiar sebelum Anda membutuhkannya dengan cepat."),
        ("Write the plan while calm: the sentence, the place, the length. Then rehearse it once "
         "when nothing is wrong.",
         "Tulis rencananya saat tenang: kalimatnya, tempatnya, lamanya. Lalu latih sekali saat "
         "tidak ada masalah."),
        ("Write your four-line calm-down plan and say it out loud once today.",
         "Tulis rencana menenangkan diri Anda dalam empat baris dan ucapkan sekali hari ini."),
        ("What do I actually do at the moment I feel it rising?",
         "Apa yang benar-benar saya lakukan pada saat saya merasakannya mulai naik?"),
        ("\"I'm getting too angry to be useful. I'll be back in five minutes.\"",
         "\"Mama/Papa terlalu marah untuk bisa berguna sekarang. Lima menit lagi kembali.\""),
    ),

    342: d(
        ("Improve emotional coaching language",
         "Memperbaiki bahasa pendampingan emosi"),
        ("The words you use for feelings become the words your child has for their own inner "
         "life, and a child with only three words for what they feel is genuinely less able to "
         "manage what they feel.\n\n"
         "Widen the vocabulary in ordinary moments, not just in crises. Disappointed, "
         "frustrated, nervous, embarrassed, left out, overwhelmed, relieved. Name your own too — "
         "\"I'm frustrated, not angry with you\" teaches precision and models that adults have "
         "an inner life they can describe rather than only act out.",
         "Kata-kata yang Anda pakai untuk perasaan menjadi kata-kata yang dimiliki anak untuk "
         "kehidupan batinnya sendiri, dan anak yang hanya punya tiga kata untuk apa yang ia "
         "rasakan memang benar-benar lebih sulit mengelola apa yang ia rasakan.\n\n"
         "Perluas kosakatanya di momen-momen biasa, bukan hanya saat krisis. Kecewa, frustrasi, "
         "gugup, malu, merasa tersisih, kewalahan, lega. Sebut juga milik Anda sendiri — \"Mama/"
         "Papa frustrasi, bukan marah sama kamu\" mengajarkan ketepatan dan mencontohkan bahwa "
         "orang dewasa punya kehidupan batin yang bisa digambarkan, bukan hanya dilampiaskan."),
        ("Add one new feeling word a week, used in ordinary moments rather than saved for "
         "explosions.",
         "Tambahkan satu kata perasaan baru setiap minggu, dipakai di momen biasa alih-alih "
         "disimpan untuk saat meledak."),
        ("Use one precise feeling word today for yourself, out loud.",
         "Pakai satu kata perasaan yang tepat untuk diri Anda hari ini, dengan lantang."),
        ("How many words does my child have for what they feel?",
         "Berapa banyak kata yang anak saya punya untuk apa yang ia rasakan?"),
        ("\"I'm frustrated right now. Not angry with you — frustrated.\"",
         "\"Mama/Papa lagi frustrasi. Bukan marah sama kamu — frustrasi.\""),
    ),

    343: d(
        ("Improve discipline plan",
         "Memperbaiki rencana pendisiplinan"),
        ("Discipline works when it is decided in advance and applied without heat. It fails "
         "when it is invented mid-argument, because a consequence chosen while angry is almost "
         "always too big, and a consequence too big to enforce gets abandoned — which teaches "
         "the child that limits are negotiable.\n\n"
         "So write the plan for the three or four things that actually keep happening. Decide "
         "the response now, while you can think. Make it small enough that you will follow "
         "through on a bad night. Consistency at low intensity beats severity applied "
         "unpredictably, every time.",
         "Pendisiplinan berhasil ketika diputuskan di muka dan diterapkan tanpa panas. Ia gagal "
         "ketika dikarang di tengah pertengkaran, karena hukuman yang dipilih saat marah hampir "
         "selalu terlalu besar, dan hukuman yang terlalu besar untuk ditegakkan akhirnya "
         "ditinggalkan — dan itu mengajari anak bahwa batas itu bisa ditawar.\n\n"
         "Jadi tulislah rencana untuk tiga atau empat hal yang memang terus terjadi. Putuskan "
         "tanggapannya sekarang, selagi Anda bisa berpikir. Buat cukup kecil sehingga Anda akan "
         "tetap menjalankannya di malam yang buruk. Konsistensi dengan intensitas rendah "
         "mengalahkan kekerasan yang diterapkan tak terduga, setiap kali."),
        ("Decide consequences in advance and keep them small enough to enforce on your worst "
         "day. Unenforced limits teach the opposite of what you intended.",
         "Putuskan konsekuensinya di muka dan buat cukup kecil untuk bisa ditegakkan di hari "
         "terburuk Anda. Batas yang tidak ditegakkan mengajarkan kebalikan dari yang Anda maksud."),
        ("Write your response in advance for the three things that keep happening.",
         "Tuliskan tanggapan Anda di muka untuk tiga hal yang terus terjadi."),
        ("Do I decide consequences while calm or while angry?",
         "Apakah saya memutuskan konsekuensi saat tenang atau saat marah?"),
        ("\"You already know what happens next. We agreed it last week.\"",
         "\"Kamu sudah tahu apa yang terjadi berikutnya. Kita sepakati minggu lalu.\""),
    ),

    344: d(
        ("Improve praise and encouragement",
         "Memperbaiki pujian dan dorongan"),
        ("There is a difference between praise and encouragement that sounds like hairsplitting "
         "and is not. Praise evaluates the child — \"good boy,\" \"you're so smart\" — and makes "
         "them dependent on your verdict. Encouragement describes what you saw and hands the "
         "judgement back to them.\n\n"
         "The practical test is whether your sentence would still be true if nobody had been "
         "watching. \"You worked on that for an hour\" is a fact the child owns. \"I'm so proud "
         "of you\" is a fact about you, and a child raised on it learns to perform for an "
         "audience rather than to work for a reason.",
         "Ada perbedaan antara memuji dan mendorong yang terdengar seperti membelah rambut dan "
         "sebenarnya tidak. Memuji menilai anaknya — \"anak pintar\", \"kamu cerdas sekali\" — "
         "dan membuatnya bergantung pada vonis Anda. Mendorong menggambarkan apa yang Anda lihat "
         "dan mengembalikan penilaiannya kepada dia.\n\n"
         "Ujian praktisnya adalah apakah kalimat Anda tetap benar seandainya tidak ada yang "
         "menonton. \"Kamu mengerjakan itu satu jam\" adalah fakta yang dimiliki anak. \"Mama/"
         "Papa bangga sekali sama kamu\" adalah fakta tentang Anda, dan anak yang dibesarkan "
         "dengan itu belajar tampil untuk penonton alih-alih bekerja karena alasan."),
        ("Describe instead of evaluating. If the sentence is about your feeling, it is praise; "
         "if it is about their action, it is encouragement.",
         "Gambarkan, jangan menilai. Kalau kalimatnya tentang perasaan Anda, itu pujian; kalau "
         "tentang tindakannya, itu dorongan."),
        ("Replace one piece of praise today with a description of what you actually saw.",
         "Ganti satu pujian hari ini dengan gambaran apa yang benar-benar Anda lihat."),
        ("Do my compliments describe my child or my opinion of them?",
         "Apakah pujian saya menggambarkan anak saya atau pendapat saya tentangnya?"),
        ("\"You stayed with that for an hour. What do you think of it?\"",
         "\"Kamu bertahan mengerjakan itu satu jam. Menurut kamu sendiri gimana?\""),
    ),

    345: d(
        ("Improve screen boundaries",
         "Memperbaiki batas penggunaan layar"),
        ("Screen limits that depend on a child voluntarily stopping will fail, because the "
         "product is designed by people whose job is to prevent exactly that. Willpower is the "
         "wrong tool.\n\n"
         "Build the boundary into the structure instead. Devices charge in a shared room "
         "overnight. Screens off an hour before bed. Times agreed at the start of the day, not "
         "negotiated at the point of switching off. And give a warning before the end — the "
         "sudden removal of a screen is what produces most of the explosions parents blame on "
         "the screen itself.",
         "Batas layar yang bergantung pada anak berhenti secara sukarela akan gagal, karena "
         "produknya dirancang oleh orang-orang yang pekerjaannya justru mencegah hal itu. "
         "Kekuatan kehendak adalah alat yang keliru.\n\n"
         "Bangunlah batas itu ke dalam strukturnya. Perangkat diisi daya di ruang bersama "
         "semalaman. Layar mati satu jam sebelum tidur. Waktunya disepakati di awal hari, bukan "
         "ditawar di titik mematikan. Dan beri peringatan sebelum berakhir — pencabutan layar "
         "yang mendadak itulah yang memicu sebagian besar ledakan yang orang tua salahkan pada "
         "layarnya."),
        ("Structure over willpower, and always give a five-minute warning before the end.",
         "Struktur di atas kekuatan kehendak, dan selalu beri peringatan lima menit sebelum berakhir."),
        ("Give a five-minute warning before every screen ends today.",
         "Beri peringatan lima menit sebelum setiap sesi layar berakhir hari ini."),
        ("Am I relying on my child's willpower to enforce my rule?",
         "Apakah saya mengandalkan kekuatan kehendak anak untuk menegakkan aturan saya?"),
        ("\"Five more minutes, then it goes on the shelf. I'll tell you when.\"",
         "\"Lima menit lagi, habis itu ditaruh di rak. Nanti Mama/Papa kasih tahu.\""),
    ),

    346: d(
        ("Improve homework support",
         "Memperbaiki pendampingan mengerjakan PR"),
        ("The most common homework mistake is a parent taking ownership of the outcome. Once "
         "the grade becomes yours, the child has no reason to hold it, and every evening turns "
         "into a negotiation about your anxiety.\n\n"
         "Provide the conditions and hand back the work. A fixed time, a cleared table, your "
         "presence in the room, help when asked. Not sitting over them, not correcting every "
         "line, not finishing it at eleven at night because it has to be right. A child who "
         "hands in imperfect work they did themselves has learned more than one who hands in "
         "perfect work you rescued.",
         "Kesalahan paling umum soal PR adalah orang tua mengambil alih kepemilikan hasilnya. "
         "Begitu nilainya menjadi milik Anda, anak tidak punya alasan memegangnya, dan setiap "
         "malam berubah menjadi perundingan tentang kecemasan Anda.\n\n"
         "Sediakan kondisinya dan kembalikan pekerjaannya. Waktu yang tetap, meja yang kosong, "
         "kehadiran Anda di ruangan, bantuan ketika diminta. Bukan menunggui di atas kepalanya, "
         "bukan mengoreksi setiap baris, bukan menyelesaikannya pukul sebelas malam karena harus "
         "benar. Anak yang mengumpulkan pekerjaan tidak sempurna yang ia kerjakan sendiri telah "
         "belajar lebih banyak daripada anak yang mengumpulkan pekerjaan sempurna yang Anda selamatkan."),
        ("Own the conditions, not the outcome. Be nearby and available; do not sit over the "
         "work.",
         "Milikilah kondisinya, bukan hasilnya. Beradalah di dekatnya dan tersedia; jangan "
         "menunggui pekerjaannya."),
        ("Let one piece of homework be handed in exactly as your child did it.",
         "Biarkan satu PR dikumpulkan persis seperti yang anak Anda kerjakan."),
        ("Whose homework is this?",
         "PR ini sebenarnya milik siapa?"),
        ("\"I'm here if you want me. It's your work, though.\"",
         "\"Mama/Papa di sini kalau kamu butuh. Tapi ini pekerjaanmu, ya.\""),
    ),

    347: d(
        ("Improve one-on-one connection",
         "Memperbaiki waktu berdua"),
        ("If everything else in this chapter is too much, do this one. Ten minutes, one child, "
         "no phone, most days. It is the single highest-return practice in the whole year, and "
         "it is the first thing to disappear in a busy week.\n\n"
         "Improve it by making it smaller and more certain rather than longer and more "
         "ambitious. Attach it to something that already happens — the drive, the bath, the walk "
         "— so it does not depend on finding time you do not have. A ritual that survives your "
         "worst week is worth more than an ideal one that only happens when things are calm.",
         "Kalau semua hal lain di bab ini terlalu banyak, lakukan yang satu ini. Sepuluh menit, "
         "satu anak, tanpa ponsel, di sebagian besar hari. Ini praktik dengan hasil tertinggi di "
         "sepanjang tahun ini, dan ini pula yang pertama menghilang di minggu yang sibuk.\n\n"
         "Perbaiki dengan membuatnya lebih kecil dan lebih pasti, bukan lebih lama dan lebih "
         "ambisius. Tempelkan pada sesuatu yang sudah terjadi — perjalanan, mandi, jalan kaki — "
         "supaya tidak bergantung pada menemukan waktu yang tidak Anda punya. Ritual yang "
         "selamat melewati minggu terburuk Anda lebih berharga daripada ritual ideal yang hanya "
         "terjadi saat keadaan sedang tenang."),
        ("Attach the ten minutes to something that already happens every day. Do not schedule "
         "it into a gap you have to create.",
         "Tempelkan sepuluh menit itu pada sesuatu yang memang sudah terjadi setiap hari. Jangan "
         "menjadwalkannya di celah yang harus Anda ciptakan."),
        ("Attach your ten minutes to an existing daily moment starting today.",
         "Tempelkan sepuluh menit Anda pada momen harian yang sudah ada, mulai hari ini."),
        ("What already happens every day that I could build this into?",
         "Apa yang sudah terjadi setiap hari yang bisa saya sisipi ini?"),
        ("\"Same time, same place, every day. That's ours.\"",
         "\"Jam yang sama, tempat yang sama, setiap hari. Itu milik kita.\""),
    ),

    348: d(
        ("Create a family rules page",
         "Membuat halaman aturan keluarga"),
        ("A short written list of rules removes an astonishing amount of daily friction, "
         "because most arguments are not about the rule but about whether the rule exists.\n\n"
         "Keep it to five or fewer, phrase them positively, and — this matters — write them "
         "with your children rather than for them. A rule a child helped write is a rule they "
         "will remind their sibling about. And include the adults: if the rule says phones stay "
         "off the table, that must be true of your phone, or the whole page teaches something "
         "you did not intend.",
         "Daftar aturan tertulis yang pendek menghilangkan gesekan harian dalam jumlah yang "
         "mengejutkan, karena sebagian besar pertengkaran bukan tentang aturannya melainkan "
         "tentang apakah aturan itu ada.\n\n"
         "Batasi lima atau kurang, rumuskan secara positif, dan — ini penting — tulislah bersama "
         "anak-anak Anda, bukan untuk mereka. Aturan yang ikut ditulis anak adalah aturan yang "
         "akan ia ingatkan kepada saudaranya. Dan sertakan orang dewasanya: kalau aturannya "
         "berbunyi ponsel tidak di meja makan, itu harus berlaku untuk ponsel Anda, atau seluruh "
         "halaman itu mengajarkan sesuatu yang tidak Anda maksudkan."),
        ("Five rules, positively phrased, written together, and binding on the adults too.",
         "Lima aturan, dirumuskan positif, ditulis bersama, dan mengikat orang dewasanya juga."),
        ("Write five family rules together with your children this week.",
         "Tulis lima aturan keluarga bersama anak-anak Anda minggu ini."),
        ("Do our rules apply to me?",
         "Apakah aturan kami berlaku untuk saya?"),
        ("\"Let's write these together. They apply to me as well.\"",
         "\"Ayo kita tulis ini bareng. Ini berlaku untuk Mama/Papa juga.\""),
    ),

    349: d(
        ("Create a family meeting routine",
         "Membuat rutinitas rapat keluarga"),
        ("A weekly family meeting sounds formal and works because it moves problems out of the "
         "moment. Instead of arguing about the shared tablet at the point of conflict, it goes "
         "on the list and gets discussed on Sunday when nobody is holding it.\n\n"
         "Keep it short — fifteen minutes is plenty. Start with appreciations, because a meeting "
         "that only ever handles complaints becomes something children dread. Let children raise "
         "items and let their proposals actually win sometimes; a meeting where the adults always "
         "get their way is not a meeting, and children work that out within a fortnight.",
         "Rapat keluarga mingguan terdengar formal dan berhasil karena ia memindahkan masalah "
         "keluar dari momennya. Alih-alih bertengkar soal tablet bersama tepat saat konflik, "
         "masalahnya masuk daftar dan dibahas hari Minggu ketika tidak ada yang sedang "
         "memegangnya.\n\n"
         "Buat singkat — lima belas menit sudah lebih dari cukup. Mulai dengan apresiasi, karena "
         "rapat yang isinya hanya keluhan akan menjadi hal yang ditakuti anak. Biarkan anak "
         "mengajukan usulan dan biarkan usulan mereka benar-benar menang sesekali; rapat di mana "
         "orang dewasa selalu menang bukan rapat, dan anak menyadari itu dalam dua minggu."),
        ("Fifteen minutes, appreciations first, and at least one decision the children actually "
         "make.",
         "Lima belas menit, apresiasi dulu, dan setidaknya satu keputusan yang benar-benar dibuat "
         "anak-anak."),
        ("Hold one fifteen-minute family meeting this week, starting with appreciations.",
         "Adakan satu rapat keluarga lima belas menit minggu ini, dimulai dengan apresiasi."),
        ("Do my children have any real say in how this family runs?",
         "Apakah anak-anak saya punya suara yang nyata dalam menjalankan keluarga ini?"),
        ("\"This one's your decision. We'll do it your way and see.\"",
         "\"Yang ini keputusan kalian. Kita jalankan dengan cara kalian dan lihat hasilnya.\""),
    ),

    350: d(
        ("Create a crisis plan for public meltdowns",
         "Membuat rencana darurat untuk ledakan emosi di tempat umum"),
        ("A public meltdown is not the moment to work out your approach. Decide it now, while "
         "you are calm and nobody is watching, and then follow the same four moves every time "
         "so that neither of you has to think.\n\n"
         "The order below matters more than the content. Safety first, then reduce the "
         "stimulation, then wait — most of a meltdown cannot be shortened by anything you say — "
         "and only afterwards, much later, the conversation. Trying to reason with a flooded "
         "child in a crowded place is the single most common mistake, and it extends the "
         "episode every time.",
         "Ledakan emosi di tempat umum bukan saat yang tepat untuk memikirkan pendekatan Anda. "
         "Putuskan sekarang, selagi Anda tenang dan tidak ada yang menonton, lalu jalankan empat "
         "langkah yang sama setiap kali supaya tidak ada dari kalian berdua yang harus berpikir.\n\n"
         "Urutan di bawah lebih penting daripada isinya. Keselamatan dulu, lalu kurangi "
         "rangsangannya, lalu tunggu — sebagian besar ledakan emosi tidak bisa dipersingkat oleh "
         "apa pun yang Anda ucapkan — dan baru sesudahnya, jauh kemudian, percakapannya. Mencoba "
         "berlogika dengan anak yang sedang kebanjiran emosi di tempat ramai adalah kesalahan "
         "yang paling umum, dan itu memperpanjang episodenya setiap kali."),
        ("Follow the four moves in order, every time. A plan you repeat becomes automatic, and "
         "automatic is what you need when you have no capacity to decide.",
         "Ikuti empat langkah itu berurutan, setiap kali. Rencana yang diulang menjadi otomatis, "
         "dan otomatis itulah yang Anda butuhkan saat tak ada ruang untuk memutuskan."),
        ("Memorise the four moves so you have them the next time it happens in public.",
         "Hafalkan empat langkah itu supaya Anda memilikinya saat kejadian berikutnya di tempat umum."),
        ("What do I usually do in public that I would never do at home?",
         "Apa yang biasanya saya lakukan di tempat umum yang tidak akan pernah saya lakukan di rumah?"),
        ("\"I'm going to pick you up and we're going outside. I'm not angry.\"",
         "\"Mama/Papa gendong kamu dan kita keluar. Mama/Papa tidak marah.\""),
        framework=fw(
            ("Four moves, in order",
             "Empat langkah, berurutan"),
            ("Do them in this sequence. Skipping to move four is the usual mistake.",
             "Lakukan dengan urutan ini. Melompat ke langkah empat adalah kesalahan yang biasa terjadi."),
            [
                (("1. Safety", "1. Keselamatan"),
                 [("First", "Pertama")],
                 ("Move the child away from roads, stairs, glass, crowds. Carry them if needed. "
                  "Say almost nothing.",
                  "Jauhkan anak dari jalan, tangga, kaca, kerumunan. Gendong kalau perlu. Hampir "
                  "tidak usah bicara."),
                 ("Nothing else can happen until this is done.",
                  "Tidak ada yang bisa dilakukan sebelum ini beres.")),
                (("2. Reduce input", "2. Kurangi rangsangan"),
                 [("Quiet", "Sunyi"), ("Fewer eyes", "Lebih sedikit yang menonton")],
                 ("Find a quieter corner, the car, outside the shop. Stop talking. Ignore the "
                  "audience entirely.",
                  "Cari sudut yang lebih sunyi, mobil, luar toko. Berhenti bicara. Abaikan "
                  "penonton sepenuhnya."),
                 ("An overloaded nervous system settles faster with less coming in.",
                  "Sistem saraf yang kelebihan beban mereda lebih cepat dengan lebih sedikit yang masuk.")),
                (("3. Wait", "3. Tunggu"),
                 [("Presence", "Kehadiran"), ("No words", "Tanpa kata")],
                 ("Stay close, stay calm, say one short sentence at most. Do not reason, "
                  "threaten, or bargain.",
                  "Tetap dekat, tetap tenang, ucapkan paling banyak satu kalimat pendek. Jangan "
                  "berlogika, mengancam, atau menawar."),
                 ("The storm ends on its own schedule. Your job is to be there when it does.",
                  "Badainya berakhir menurut jadwalnya sendiri. Tugas Anda adalah ada di sana saat itu terjadi.")),
                (("4. Talk, later", "4. Bicara, nanti"),
                 [("Much later", "Jauh kemudian")],
                 ("At home, calm, hours later if needed: what happened, what we will do next "
                  "time.",
                  "Di rumah, dalam keadaan tenang, berjam-jam kemudian kalau perlu: apa yang "
                  "terjadi, apa yang akan kita lakukan lain kali."),
                 ("This is the only stage where teaching is possible. Doing it earlier wastes it.",
                  "Ini satu-satunya tahap ketika mengajar itu mungkin. Melakukannya lebih awal hanya sia-sia.")),
            ],
        ),
    ),

    351: d(
        ("Create a school partnership plan",
         "Membuat rencana kemitraan dengan sekolah"),
        ("Teachers and parents want the same thing and routinely end up on opposite sides, "
         "usually because the only contact between them happens when something has gone wrong.\n\n"
         "Change the pattern. Introduce yourself early in the year, before there is a problem. "
         "Ask what would help. When a difficulty comes, arrive curious rather than armed — "
         "\"help me understand what you are seeing\" opens a conversation that "
         "\"my child says\" closes. And never criticise a teacher in front of your child; you "
         "will need that teacher's authority to hold for the rest of the year.",
         "Guru dan orang tua menginginkan hal yang sama dan rutin berakhir di sisi yang "
         "berlawanan, biasanya karena satu-satunya kontak di antara mereka terjadi saat ada yang "
         "salah.\n\n"
         "Ubah polanya. Perkenalkan diri di awal tahun ajaran, sebelum ada masalah. Tanyakan apa "
         "yang akan membantu. Ketika kesulitan datang, hadirlah dengan rasa ingin tahu, bukan "
         "dengan senjata — \"tolong bantu saya memahami apa yang Ibu/Bapak lihat\" membuka "
         "percakapan yang ditutup oleh \"kata anak saya\". Dan jangan pernah mengkritik guru di "
         "depan anak Anda; Anda akan membutuhkan wibawa guru itu bertahan sepanjang tahun."),
        ("Make contact before there is a problem, and open every hard conversation with a "
         "question rather than a position.",
         "Jalin kontak sebelum ada masalah, dan buka setiap percakapan yang sulit dengan "
         "pertanyaan, bukan dengan posisi."),
        ("Send one friendly message to your child's teacher this week, with no problem attached.",
         "Kirim satu pesan ramah kepada guru anak Anda minggu ini, tanpa membawa masalah."),
        ("Does my child's teacher hear from me only when something is wrong?",
         "Apakah guru anak saya hanya mendengar kabar dari saya ketika ada yang salah?"),
        ("\"Help me understand what you're seeing in class.\"",
         "\"Tolong bantu saya memahami apa yang Ibu/Bapak lihat di kelas.\""),
    ),

    352: d(
        ("Create a grandparent/caregiver alignment plan",
         "Membuat rencana keselarasan dengan kakek-nenek dan pengasuh"),
        ("You have already sorted your rules into tiers. Now turn it into an actual conversation, "
         "and have it at a calm moment rather than immediately after something went wrong.\n\n"
         "Lead with appreciation, because it is true and because it opens the door: they are "
         "helping, and in many families that help is what makes work possible at all. Then bring "
         "two non-negotiables, not a list. Explain the reason rather than issuing the rule — "
         "\"the doctor was clear about this\" travels much further than \"I've decided.\" And "
         "then let everything outside those two go, visibly and generously.",
         "Anda sudah memilah aturan Anda ke dalam tingkatan. Sekarang ubah itu menjadi percakapan "
         "yang sungguhan, dan lakukan di saat tenang, bukan tepat setelah ada yang salah.\n\n"
         "Awali dengan penghargaan, karena itu benar dan karena itu membuka pintu: mereka sedang "
         "membantu, dan di banyak keluarga bantuan itulah yang membuat bekerja jadi mungkin sama "
         "sekali. Lalu bawa dua hal yang tak bisa ditawar, bukan sebuah daftar. Jelaskan alasannya "
         "alih-alih menjatuhkan aturan — \"dokternya tegas soal ini\" menempuh jarak jauh lebih "
         "panjang daripada \"saya sudah memutuskan\". Lalu lepaskan segala hal di luar dua itu, "
         "dengan terlihat dan dengan lapang."),
        ("Appreciation first, two non-negotiables with reasons attached, and everything else "
         "visibly released.",
         "Penghargaan dulu, dua hal yang tak bisa ditawar dengan alasannya, dan selebihnya "
         "dilepaskan dengan terlihat."),
        ("Have the alignment conversation this week, at a calm moment, with only two asks.",
         "Lakukan percakapan keselarasan itu minggu ini, di saat tenang, dengan hanya dua permintaan."),
        ("Have I ever thanked them properly for what they do?",
         "Pernahkah saya berterima kasih dengan sungguh-sungguh atas apa yang mereka lakukan?"),
        ("\"We couldn't manage without you. There are just two things I need to hold.\"",
         "\"Kami tidak akan sanggup tanpa Ibu/Bapak. Cuma ada dua hal yang perlu saya pegang.\""),
    ),

    353: d(
        ("Create age-appropriate responsibility charts",
         "Membuat daftar tanggung jawab sesuai usia"),
        ("Write it down and put it where everyone can see it. A visible chart moves the "
         "authority from you to the wall, and a child arguing with a chart is a much shorter "
         "argument than a child arguing with a parent.\n\n"
         "Keep the list short and let the child help write it. Include one thing that is "
         "slightly beyond them — a chart with nothing to grow into is just a record of what "
         "already happens. And review it every few months, because responsibilities that were "
         "right in March quietly become babyish by September, and nobody notices until the "
         "child resents them.",
         "Tuliskan dan tempel di tempat semua orang bisa melihat. Daftar yang terlihat memindahkan "
         "wibawa dari Anda ke dinding, dan anak yang berdebat dengan daftar adalah perdebatan yang "
         "jauh lebih pendek daripada anak yang berdebat dengan orang tua.\n\n"
         "Buat daftarnya pendek dan biarkan anak ikut menulis. Sertakan satu hal yang sedikit di "
         "atas kemampuannya — daftar tanpa sesuatu untuk ditumbuhi hanyalah catatan atas apa yang "
         "sudah terjadi. Dan tinjau setiap beberapa bulan, karena tanggung jawab yang pas di "
         "bulan Maret diam-diam menjadi kekanak-kanakan pada bulan September, dan tidak ada yang "
         "menyadarinya sampai anaknya jengkel."),
        ("Short list, written together, visible on a wall, with one item slightly beyond current "
         "reach — and reviewed every few months.",
         "Daftar pendek, ditulis bersama, terlihat di dinding, dengan satu butir yang sedikit di "
         "atas jangkauan saat ini — dan ditinjau setiap beberapa bulan."),
        ("Make a short responsibility chart with your child and put it on the wall.",
         "Buat daftar tanggung jawab yang pendek bersama anak Anda dan tempel di dinding."),
        ("When did I last update what I expect my child to handle?",
         "Kapan terakhir saya memperbarui apa yang saya harapkan bisa anak saya tangani?"),
        ("\"Let's write your list. What do you think you're ready for?\"",
         "\"Ayo kita tulis daftarmu. Menurutmu kamu sudah siap untuk apa?\""),
    ),

    354: d(
        ("Parenting review: what changed this year",
         "Tinjauan pengasuhan: apa yang berubah tahun ini"),
        ("A year is long enough to have changed something and short enough to remember what it "
         "was. Look back deliberately rather than trusting your impression, because impressions "
         "in parenting are shaped almost entirely by the last bad week.\n\n"
         "Name concrete differences. A phrase you stopped using. A routine that runs without a "
         "fight now. A situation that used to end in shouting and no longer does. If you can "
         "name two, that is a real year of change — parenting shifts slowly, and two is more "
         "than most people manage.",
         "Setahun cukup panjang untuk mengubah sesuatu dan cukup pendek untuk mengingat apa yang "
         "diubah. Tengoklah ke belakang dengan sengaja alih-alih mempercayai kesan Anda, karena "
         "kesan dalam pengasuhan hampir sepenuhnya dibentuk oleh minggu buruk yang terakhir.\n\n"
         "Sebutkan perbedaan yang konkret. Satu kalimat yang berhenti Anda pakai. Satu rutinitas "
         "yang kini berjalan tanpa pertengkaran. Satu situasi yang dulu berakhir dengan bentakan "
         "dan sekarang tidak lagi. Kalau Anda bisa menyebut dua, itu setahun perubahan yang "
         "nyata — pengasuhan bergeser pelan, dan dua sudah lebih dari yang dicapai kebanyakan orang."),
        ("Name concrete changes, not feelings. \"I stopped saying that sentence\" is evidence; "
         "\"I feel calmer\" is weather.",
         "Sebutkan perubahan yang konkret, bukan perasaan. \"Saya berhenti mengucapkan kalimat "
         "itu\" adalah bukti; \"saya merasa lebih tenang\" adalah cuaca."),
        ("Write down two concrete things that are different in your parenting this year.",
         "Tuliskan dua hal konkret yang berbeda dalam pengasuhan Anda tahun ini."),
        ("What can I point to that is genuinely different?",
         "Apa yang bisa saya tunjuk sebagai sesuatu yang benar-benar berbeda?"),
        ("\"I used to handle that differently. I don't anymore.\"",
         "\"Dulu Mama/Papa menangani itu dengan cara lain. Sekarang tidak lagi.\""),
    ),

    355: d(
        ("Personal reflection: what changed in me",
         "Refleksi pribadi: apa yang berubah dalam diri saya"),
        ("The changes that last are not techniques. They are changes in the parent — a shorter "
         "fuse lengthened, an old reflex interrupted, a sentence from your own childhood that "
         "stopped coming out of your mouth.\n\n"
         "This is the harder review and the more important one. Ask what you understand now "
         "that you did not a year ago, particularly about yourself. Most parents who change "
         "deeply describe the same thing: at some point they stopped trying to fix the child "
         "and started noticing their own part in the pattern.",
         "Perubahan yang bertahan bukan teknik. Ia perubahan dalam diri orang tuanya — sumbu "
         "pendek yang memanjang, refleks lama yang terputus, satu kalimat dari masa kecil Anda "
         "sendiri yang berhenti keluar dari mulut Anda.\n\n"
         "Ini peninjauan yang lebih sulit dan lebih penting. Tanyakan apa yang kini Anda pahami "
         "dan setahun lalu belum, terutama tentang diri sendiri. Kebanyakan orang tua yang "
         "berubah secara mendalam menggambarkan hal yang sama: pada titik tertentu mereka "
         "berhenti berusaha memperbaiki anaknya dan mulai menyadari bagian mereka sendiri dalam "
         "polanya."),
        ("Ask what you understand about yourself now that you did not a year ago. That answer "
         "is the real progress.",
         "Tanyakan apa yang kini Anda pahami tentang diri sendiri dan setahun lalu belum. Jawaban "
         "itulah kemajuan yang sesungguhnya."),
        ("Write one sentence about how you have changed as a person this year.",
         "Tuliskan satu kalimat tentang bagaimana Anda berubah sebagai pribadi tahun ini."),
        ("What do I understand about myself now that I did not before?",
         "Apa yang saya pahami tentang diri saya sekarang dan sebelumnya tidak?"),
        ("\"I'm not the same parent I was a year ago.\"",
         "\"Saya bukan orang tua yang sama seperti setahun lalu.\""),
    ),

    356: d(
        ("Marriage/co-parenting review",
         "Tinjauan pernikahan dan pengasuhan bersama"),
        ("The relationship between the adults is the ceiling on the whole family, and it is "
         "usually the thing given the least attention, because children are loud and a marriage "
         "is patient until it is not.\n\n"
         "Review it honestly. When did you last have a conversation that was not logistics? Do "
         "you undermine each other in front of the children? Is there a resentment that has been "
         "quietly accumulating for a year? For separated co-parents the questions are the same "
         "in different clothes: can we make a decision without a fight, and can our child feel "
         "the difference. Fixing this improves everything downstream of it.",
         "Hubungan antara orang dewasanya adalah langit-langit bagi seluruh keluarga, dan "
         "biasanya itulah yang paling sedikit diperhatikan, karena anak-anak berisik dan sebuah "
         "pernikahan itu sabar sampai ia tidak lagi sabar.\n\n"
         "Tinjaulah dengan jujur. Kapan terakhir kalian bercakap-cakap yang bukan soal urusan "
         "teknis? Apakah kalian saling menjatuhkan di depan anak? Adakah kejengkelan yang "
         "diam-diam menumpuk selama setahun? Bagi orang tua yang berpisah, pertanyaannya sama "
         "dengan baju yang berbeda: bisakah kami mengambil keputusan tanpa bertengkar, dan "
         "bisakah anak kami merasakan bedanya. Memperbaiki ini memperbaiki semua yang ada di "
         "hilirnya."),
        ("Have one conversation this week that is not about logistics. The children benefit "
         "from it more than from anything you do directly for them.",
         "Lakukan satu percakapan minggu ini yang bukan soal urusan teknis. Anak-anak lebih "
         "diuntungkan olehnya daripada oleh apa pun yang Anda lakukan langsung untuk mereka."),
        ("Have one non-logistical conversation with your co-parent this week.",
         "Lakukan satu percakapan yang bukan urusan teknis dengan pasangan pengasuh Anda minggu ini."),
        ("When did we last talk about something other than the children?",
         "Kapan terakhir kami membicarakan sesuatu selain anak-anak?"),
        ("\"Can we talk about something that isn't the schedule?\"",
         "\"Bisa nggak kita ngobrol soal yang bukan jadwal?\""),
    ),

    357: d(
        ("Child relationship review",
         "Tinjauan hubungan dengan tiap anak"),
        ("Do this one child at a time, because the answers differ more than parents expect and "
         "averaging them hides the child who is struggling.\n\n"
         "For each: what is our relationship like right now, honestly? What does this child need "
         "from me that they are not getting? When did we last enjoy each other's company with "
         "nothing being managed? Some of the answers will be uncomfortable. Discomfort in this "
         "particular review is a sign it is being done properly rather than a sign that "
         "something is wrong with you.",
         "Lakukan ini satu anak pada satu waktu, karena jawabannya lebih berbeda daripada dugaan "
         "orang tua dan merata-ratakannya justru menyembunyikan anak yang sedang kesulitan.\n\n"
         "Untuk masing-masing: bagaimana hubungan kami sekarang, sejujurnya? Apa yang anak ini "
         "butuhkan dari saya dan belum ia dapatkan? Kapan terakhir kami menikmati kebersamaan "
         "tanpa ada yang sedang diurus? Beberapa jawabannya akan tidak nyaman. Ketidaknyamanan "
         "dalam peninjauan yang satu ini adalah tanda bahwa ia dilakukan dengan benar, bukan "
         "tanda ada yang salah dengan Anda."),
        ("One child at a time, three questions each, written down. Averaging hides the one who "
         "needs you.",
         "Satu anak pada satu waktu, tiga pertanyaan untuk masing-masing, dituliskan. "
         "Merata-ratakan menyembunyikan anak yang membutuhkan Anda."),
        ("Answer three honest questions about your relationship with each child.",
         "Jawab tiga pertanyaan jujur tentang hubungan Anda dengan tiap anak."),
        ("Which of my children am I furthest from right now?",
         "Anak saya yang mana yang saat ini paling jauh dari saya?"),
        ("\"I want to know how things are between us. Really.\"",
         "\"Mama/Papa ingin tahu bagaimana sebenarnya hubungan kita. Yang jujur.\""),
    ),

    358: d(
        ("Family culture review",
         "Tinjauan budaya keluarga"),
        ("Every family has a culture, whether or not anyone designed it. It is made of what is "
         "normal here: how loud we get, what we laugh at, whether we say sorry, what happens "
         "when someone fails, who does the invisible work.\n\n"
         "Name yours as it actually is, not as you would describe it to a neighbour. A child "
         "absorbs this culture completely and carries it into their own house thirty years from "
         "now, usually without ever examining it — the same way you absorbed yours. That is why "
         "the honest version of this review is worth the discomfort.",
         "Setiap keluarga punya budaya, entah ada yang merancangnya atau tidak. Ia terbuat dari "
         "apa yang dianggap biasa di sini: seberapa keras kita bersuara, apa yang kita tertawakan, "
         "apakah kita meminta maaf, apa yang terjadi ketika ada yang gagal, siapa yang mengerjakan "
         "pekerjaan yang tak terlihat.\n\n"
         "Sebutkan budaya Anda apa adanya, bukan sebagaimana Anda akan menggambarkannya kepada "
         "tetangga. Anak menyerap budaya ini sepenuhnya dan membawanya ke rumahnya sendiri tiga "
         "puluh tahun dari sekarang, biasanya tanpa pernah memeriksanya — persis seperti Anda "
         "menyerap budaya Anda. Karena itulah versi jujur dari peninjauan ini sepadan dengan "
         "ketidaknyamanannya."),
        ("Describe what is normal in your home, not what is aspirational. Normal is what gets "
         "inherited.",
         "Gambarkan apa yang biasa di rumah Anda, bukan apa yang dicita-citakan. Yang biasa itulah "
         "yang diwariskan."),
        ("Write three sentences describing your family's culture as it actually is.",
         "Tulis tiga kalimat yang menggambarkan budaya keluarga Anda apa adanya."),
        ("What is normal in this house that I would not want repeated in my child's house?",
         "Apa yang biasa di rumah ini yang tidak ingin saya lihat terulang di rumah anak saya?"),
        ("\"This is how we do things here — and I get to decide whether that stays true.\"",
         "\"Beginilah cara kami di sini — dan saya yang menentukan apakah itu tetap begitu.\""),
    ),

    359: d(
        ("What to keep next year",
         "Apa yang dipertahankan tahun depan"),
        ("Deciding what to keep is not a formality. Good practices die from neglect rather than "
         "from decision, and the ones most likely to disappear are the quiet ones that nobody "
         "notices working.\n\n"
         "Name them explicitly and protect them by name. The ten minutes. The Saturday ritual. "
         "The way you now pause before responding. Write them down and treat them as commitments "
         "rather than habits, because a habit fails silently in a busy month and a commitment "
         "gets noticed when it slips.",
         "Memutuskan apa yang dipertahankan bukan formalitas. Praktik yang baik mati karena "
         "terabaikan, bukan karena diputuskan, dan yang paling mungkin lenyap adalah yang "
         "senyap — yang tidak ada yang menyadari sedang bekerja.\n\n"
         "Sebutkan dengan tegas dan lindungi dengan namanya. Sepuluh menit itu. Ritual hari "
         "Sabtu. Cara Anda kini berhenti sejenak sebelum menanggapi. Tuliskan dan perlakukan "
         "sebagai komitmen alih-alih kebiasaan, karena kebiasaan gagal dalam senyap di bulan "
         "yang sibuk sementara komitmen ketahuan ketika ia meleset."),
        ("Write the keep list by name. Anything unnamed will quietly vanish in the first busy "
         "month.",
         "Tulis daftar yang dipertahankan dengan namanya. Apa pun yang tak disebut akan lenyap "
         "diam-diam di bulan sibuk yang pertama."),
        ("Write down three things you are keeping next year.",
         "Tuliskan tiga hal yang Anda pertahankan tahun depan."),
        ("What would I most regret losing without noticing?",
         "Apa yang paling saya sesali kalau hilang tanpa saya sadari?"),
        ("\"This one we keep. It works.\"",
         "\"Yang ini kita pertahankan. Ini berhasil.\""),
    ),

    360: d(
        ("What to stop next year",
         "Apa yang dihentikan tahun depan"),
        ("This is the hardest list because stopping requires admitting something has not been "
         "working, sometimes for years.\n\n"
         "Be specific and be kind to yourself in the same sentence. A phrase you want out of "
         "your mouth. A consequence you keep threatening and never enforce. An activity everyone "
         "attends and nobody enjoys. A comparison between two children that you have made a "
         "hundred times. Choose one — one — and stop it. Stopping a single thing completely is "
         "worth more than intending to stop five.",
         "Ini daftar yang paling sulit karena berhenti menuntut pengakuan bahwa sesuatu selama "
         "ini tidak berhasil, kadang selama bertahun-tahun.\n\n"
         "Jadilah spesifik dan berbaik hatilah pada diri sendiri dalam kalimat yang sama. Satu "
         "kalimat yang ingin Anda hapus dari mulut Anda. Satu ancaman hukuman yang terus Anda "
         "sebut dan tak pernah Anda tegakkan. Satu kegiatan yang semua orang hadiri dan tak ada "
         "yang menikmati. Satu perbandingan antara dua anak yang sudah Anda ucapkan seratus kali. "
         "Pilih satu — satu — dan hentikan. Menghentikan satu hal sepenuhnya lebih berharga "
         "daripada berniat menghentikan lima."),
        ("One thing, stopped completely. Five things intended is the same as nothing.",
         "Satu hal, dihentikan sepenuhnya. Lima hal yang diniatkan sama saja dengan tidak ada."),
        ("Name the one thing you are stopping, and say it out loud.",
         "Sebutkan satu hal yang Anda hentikan, dan ucapkan dengan lantang."),
        ("What have I been doing for years that has never once worked?",
         "Apa yang bertahun-tahun saya lakukan dan tidak sekali pun berhasil?"),
        ("\"I'm not going to do that anymore. It never helped either of us.\"",
         "\"Mama/Papa tidak akan melakukan itu lagi. Itu tidak pernah membantu kita berdua.\""),
    ),

    361: d(
        ("What to start next year",
         "Apa yang dimulai tahun depan"),
        ("Keep this list short. Parents leave a year of reflection with fifteen new intentions "
         "and reliably keep none of them, because fifteen changes compete with each other for "
         "the same small supply of attention.\n\n"
         "Choose one thing to start. Make it specific enough to schedule and small enough to do "
         "on a bad day. Then hold it for ninety days without adding anything else. One change "
         "that survives three months has become part of how your family works; ten changes "
         "attempted in January are a memory by March.",
         "Buat daftar ini pendek. Orang tua meninggalkan setahun refleksi dengan lima belas niat "
         "baru dan hampir pasti tidak menjalankan satu pun, karena lima belas perubahan saling "
         "berebut persediaan perhatian yang sama-sama sedikit.\n\n"
         "Pilih satu hal untuk dimulai. Buat cukup spesifik untuk dijadwalkan dan cukup kecil "
         "untuk dikerjakan di hari yang buruk. Lalu pegang selama sembilan puluh hari tanpa "
         "menambah apa pun. Satu perubahan yang selamat tiga bulan sudah menjadi bagian dari cara "
         "keluarga Anda bekerja; sepuluh perubahan yang dicoba di bulan Januari tinggal kenangan "
         "pada bulan Maret."),
        ("One new thing, specific enough to schedule, held for ninety days before you add "
         "anything else.",
         "Satu hal baru, cukup spesifik untuk dijadwalkan, dipegang sembilan puluh hari sebelum "
         "Anda menambahkan apa pun."),
        ("Choose the one thing you will start, and put it in the calendar.",
         "Pilih satu hal yang akan Anda mulai, dan masukkan ke kalender."),
        ("If I could only change one thing, which one would change the most?",
         "Kalau saya hanya boleh mengubah satu hal, yang mana yang paling banyak mengubah?"),
        ("\"Starting Monday, we're doing this. Just this one thing.\"",
         "\"Mulai Senin, kita jalankan ini. Cuma satu ini.\""),
    ),

    362: d(
        ("Write a family mission statement",
         "Menulis pernyataan misi keluarga"),
        ("This sounds corporate and does not have to be. Two or three sentences, in your own "
         "language, describing what this family is for and how the people in it treat each "
         "other.\n\n"
         "Write it with your children if they are old enough — their contributions are usually "
         "better than the adults', because they say what they actually see. Put it somewhere "
         "visible. Its real value comes later, on the difficult days, when it is the thing you "
         "read to remember what you were building before this week got loud.",
         "Ini terdengar seperti bahasa perusahaan dan tidak harus begitu. Dua atau tiga kalimat, "
         "dalam bahasa Anda sendiri, yang menggambarkan untuk apa keluarga ini ada dan bagaimana "
         "orang-orang di dalamnya saling memperlakukan.\n\n"
         "Tulislah bersama anak-anak Anda kalau mereka sudah cukup besar — sumbangan mereka "
         "biasanya lebih bagus daripada yang dari orang dewasa, karena mereka mengatakan apa yang "
         "benar-benar mereka lihat. Taruh di tempat yang terlihat. Nilai sesungguhnya baru datang "
         "kemudian, di hari-hari yang berat, ketika itulah yang Anda baca untuk mengingat apa yang "
         "sedang Anda bangun sebelum minggu ini jadi berisik."),
        ("Two or three sentences, written together, in ordinary words. Put it where you will "
         "see it on a bad day.",
         "Dua atau tiga kalimat, ditulis bersama, dengan kata-kata biasa. Taruh di tempat yang "
         "akan Anda lihat di hari yang buruk."),
        ("Write two sentences describing what your family is for.",
         "Tulis dua kalimat yang menggambarkan untuk apa keluarga Anda ada."),
        ("What is this family for?",
         "Untuk apa keluarga ini ada?"),
        ("\"Let's write down what we're about. All of us.\"",
         "\"Ayo kita tulis kita ini sebenarnya tentang apa. Kita semua.\""),
    ),

    363: d(
        ("Celebrate growth",
         "Merayakan pertumbuhan"),
        ("Parents are extraordinarily bad at this. A year of genuine effort gets summarised as "
         "\"I still shout sometimes,\" and everything that changed is invisible next to "
         "everything that has not.\n\n"
         "Celebrate anyway, and do it out loud in front of your children — not to be praised, "
         "but because a family that can notice its own progress is a family that keeps going. "
         "Name what is better than it was. Say it at dinner. Children need to see adults "
         "acknowledge growth, because that is how they learn to acknowledge their own instead of "
         "only cataloguing their failures.",
         "Orang tua luar biasa buruk dalam hal ini. Setahun usaha yang sungguhan diringkas "
         "menjadi \"saya masih suka membentak\", dan semua yang berubah tidak terlihat di samping "
         "semua yang belum.\n\n"
         "Tetaplah merayakan, dan lakukan dengan lantang di depan anak-anak Anda — bukan untuk "
         "dipuji, melainkan karena keluarga yang bisa menyadari kemajuannya sendiri adalah "
         "keluarga yang terus berjalan. Sebutkan apa yang lebih baik dari sebelumnya. Katakan di "
         "meja makan. Anak perlu melihat orang dewasa mengakui pertumbuhan, karena begitulah "
         "mereka belajar mengakui pertumbuhannya sendiri alih-alih hanya mencatat kegagalannya."),
        ("Say one improvement out loud at dinner. Not a speech — one sentence, in front of "
         "everyone.",
         "Sebutkan satu kemajuan dengan lantang di meja makan. Bukan pidato — satu kalimat, di "
         "depan semua orang."),
        ("Name one thing your family does better now, out loud at dinner.",
         "Sebutkan satu hal yang kini keluarga Anda lakukan lebih baik, dengan lantang di meja makan."),
        ("Why do I find it so hard to say we did well?",
         "Kenapa saya begitu sulit mengatakan bahwa kami sudah melakukannya dengan baik?"),
        ("\"We're better at this than we were a year ago. All of us.\"",
         "\"Kita lebih baik dalam hal ini dibanding setahun lalu. Kita semua.\""),
    ),

    364: d(
        ("Plan next 90 days",
         "Merencanakan 90 hari ke depan"),
        ("A year is too long to plan and a week is too short to change anything. Ninety days is "
         "the useful unit: long enough for a new practice to become normal, short enough that "
         "you can still see the end of it.\n\n"
         "So write the next ninety days rather than the next year. One thing you are keeping, "
         "one thing you are stopping, one thing you are starting. Put a date in the calendar to "
         "look at it again. That review date is the part everyone skips and the part that makes "
         "the whole thing work — a plan without a review date is a wish.",
         "Setahun terlalu panjang untuk direncanakan dan seminggu terlalu pendek untuk mengubah "
         "apa pun. Sembilan puluh hari adalah satuan yang berguna: cukup panjang bagi praktik "
         "baru untuk menjadi biasa, cukup pendek sehingga Anda masih bisa melihat ujungnya.\n\n"
         "Jadi tulislah sembilan puluh hari ke depan, bukan setahun ke depan. Satu hal yang Anda "
         "pertahankan, satu hal yang Anda hentikan, satu hal yang Anda mulai. Taruh satu tanggal "
         "di kalender untuk melihatnya lagi. Tanggal peninjauan itulah bagian yang semua orang "
         "lewati dan bagian yang membuat semuanya bekerja — rencana tanpa tanggal peninjauan "
         "hanyalah harapan."),
        ("Three lines and a date. Put the review date in the calendar now, not later.",
         "Tiga baris dan satu tanggal. Masukkan tanggal peninjauan ke kalender sekarang, bukan nanti."),
        ("Write your ninety-day plan in three lines and set the review date.",
         "Tulis rencana sembilan puluh hari Anda dalam tiga baris dan tetapkan tanggal peninjauannya."),
        ("When will I actually look at this again?",
         "Kapan saya benar-benar akan melihat ini lagi?"),
        ("\"Three months from today, we look at this again.\"",
         "\"Tiga bulan dari hari ini, kita lihat ini lagi.\""),
    ),

    365: d(
        ("Final integration and recommitment",
         "Penyatuan akhir dan komitmen baru"),
        ("Three hundred and sixty-five days. If you have arrived here having missed weeks at a "
         "time, that is not a failure — that is what a real year with children looks like, and "
         "the guide was built expecting it.\n\n"
         "What is worth carrying out of this year is smaller than everything you read. Children "
         "do not need a perfect parent; the research is unusually clear that they need a "
         "good-enough one who repairs reliably. The relationship is the curriculum. Small "
         "consistent things beat large occasional ones. And the parent you are becoming matters "
         "more than any technique you learned along the way.\n\n"
         "Tomorrow is day one again, and it always is. Begin where you are.",
         "Tiga ratus enam puluh lima hari. Kalau Anda tiba di sini setelah melewatkan berminggu-"
         "minggu sekaligus, itu bukan kegagalan — begitulah rupa satu tahun yang nyata bersama "
         "anak-anak, dan panduan ini dibuat dengan memperhitungkan hal itu.\n\n"
         "Yang layak dibawa keluar dari tahun ini lebih sedikit daripada semua yang Anda baca. "
         "Anak tidak membutuhkan orang tua yang sempurna; penelitian luar biasa jelas bahwa yang "
         "mereka butuhkan adalah orang tua yang cukup baik dan bisa diandalkan untuk berbaikan. "
         "Hubungan adalah kurikulumnya. Hal kecil yang konsisten mengalahkan hal besar yang "
         "sesekali. Dan orang tua yang sedang Anda jadi lebih penting daripada teknik apa pun "
         "yang Anda pelajari di sepanjang jalan.\n\n"
         "Besok adalah hari pertama lagi, dan memang selalu begitu. Mulailah dari tempat Anda berada."),
        ("Carry three things, not three hundred: connect first, change one thing at a time, and "
         "repair every time you get it wrong.",
         "Bawalah tiga hal, bukan tiga ratus: dekati dulu, ubah satu hal pada satu waktu, dan "
         "berbaikanlah setiap kali Anda keliru."),
        ("Write one sentence about the parent you are choosing to be this year.",
         "Tulis satu kalimat tentang orang tua seperti apa yang Anda pilih untuk menjadi tahun ini."),
        ("What kind of parent am I choosing to be tomorrow?",
         "Orang tua seperti apa yang saya pilih untuk menjadi besok?"),
        ("\"I'm not finished learning how to do this. I'm still here.\"",
         "\"Saya belum selesai belajar melakukan ini. Saya masih di sini.\""),
    ),
}
