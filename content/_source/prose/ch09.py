# Chapter 9 — Building Character & Responsibility (days 242-270)
#
# Grounded in the founder's guidebook chapter 9 ("Character is built through
# daily small responsibilities held consistently") and toolkit tool 9
# (Responsibility Ladder).
#
# Through-line: character is not taught by lecture. It is built by repeated
# small ownership, held long enough to become who the child is. Day 243 carries
# an age-band grid so parents pitch the responsibility at the right level
# instead of guessing.

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
    242: d(
        ("Character is taught through daily life",
         "Karakter diajarkan lewat kehidupan sehari-hari"),
        ("Nobody has ever become honest because of a speech about honesty. Character is "
         "not installed through explanation. It is worn in, slowly, by doing the same "
         "small thing so many times that it stops feeling like a choice.\n\n"
         "This is good news, because it means you do not need the perfect words. You need "
         "ordinary days used well. The child who carries their plate to the sink every "
         "night is not learning about plates. They are learning that their mess is theirs "
         "to handle — and that lesson will still be there at thirty.",
         "Tidak ada orang yang menjadi jujur karena mendengar ceramah tentang kejujuran. "
         "Karakter tidak dipasang lewat penjelasan. Ia terbentuk pelan-pelan, dengan "
         "melakukan hal kecil yang sama begitu sering sampai tidak lagi terasa sebagai "
         "pilihan.\n\n"
         "Ini kabar baik, karena artinya Anda tidak butuh kata-kata yang sempurna. Anda "
         "butuh hari-hari biasa yang dipakai dengan baik. Anak yang membawa piringnya ke "
         "wastafel setiap malam bukan sedang belajar soal piring. Ia sedang belajar bahwa "
         "kekacauan yang ia buat adalah tanggung jawabnya — dan pelajaran itu masih akan "
         "ada saat ia berusia tiga puluh."),
        ("Pick one thing your child does for the family every single day. Not a list. One "
         "thing, repeated until it disappears into the fabric of the day.",
         "Pilih satu hal yang anak Anda lakukan untuk keluarga setiap hari. Bukan daftar. "
         "Satu hal, diulang sampai menyatu dengan hari itu sendiri."),
        ("Name one daily responsibility your child already carries, even a tiny one. Say "
         "it out loud to them today.",
         "Sebutkan satu tanggung jawab harian yang sudah anak Anda pegang, sekecil apa "
         "pun. Katakan itu kepadanya hari ini."),
        ("What am I teaching by what I let my child skip?",
         "Apa yang saya ajarkan lewat hal-hal yang saya biarkan anak saya lewati?"),
        ("\"That's your job in this family, and you do it.\"",
         "\"Itu tugasmu di keluarga ini, dan kamu mengerjakannya.\""),
        framework=fw(
            ("Character is built, not announced",
             "Karakter dibangun, bukan diumumkan"),
            ("The same value, taught two ways. Only one of them lasts.",
             "Nilai yang sama, diajarkan dengan dua cara. Hanya satu yang bertahan."),
            [
                (("Taught by talking", "Diajarkan lewat bicara"),
                 [("Lecture", "Ceramah"), ("One-off", "Sekali jalan")],
                 ("\"You need to be more responsible.\" Said in frustration, usually after "
                  "something went wrong.",
                  "\"Kamu harus lebih bertanggung jawab.\" Diucapkan dengan kesal, biasanya "
                  "setelah ada yang salah."),
                 ("The child learns what disappoints you. Nothing changes on Monday.",
                  "Anak belajar apa yang mengecewakan Anda. Hari Senin tidak ada yang berubah.")),
                (("Built by doing", "Dibangun lewat melakukan"),
                 [("Repetition", "Pengulangan"), ("Daily", "Harian")],
                 ("One small task the child owns, done every day, whether or not anyone is "
                  "watching or in a good mood.",
                  "Satu tugas kecil yang dipegang anak, dikerjakan setiap hari, entah ada "
                  "yang melihat atau tidak, entah suasana hati sedang baik atau tidak."),
                 ("The child learns who they are. It holds when you are not in the room.",
                  "Anak belajar siapa dirinya. Itu bertahan bahkan saat Anda tidak ada di ruangan.")),
            ],
        ),
    ),

    243: d(
        ("Responsibility by age",
         "Tanggung jawab menurut usia"),
        ("Most responsibility problems are calibration problems. Ask too little and the "
         "child stays helpless long past the age they needed to. Ask too much and they "
         "fail, and failure at the wrong moment teaches them they are not capable.\n\n"
         "The grid below is a starting point, not a rule. Your child is not an average. "
         "Pitch slightly above where they are comfortable and slightly below where they "
         "would drown — that narrow band is where growth actually happens.",
         "Kebanyakan masalah tanggung jawab sebenarnya masalah takaran. Minta terlalu "
         "sedikit, anak tetap tidak berdaya jauh melewati usia yang seharusnya. Minta "
         "terlalu banyak, ia gagal, dan kegagalan di saat yang salah mengajarinya bahwa ia "
         "tidak mampu.\n\n"
         "Tabel di bawah adalah titik awal, bukan aturan. Anak Anda bukan rata-rata. "
         "Taruhlah sedikit di atas zona nyamannya dan sedikit di bawah titik ia akan "
         "tenggelam — di pita sempit itulah pertumbuhan benar-benar terjadi."),
        ("Look at the band above your child's age, not below it. Most parents are one "
         "step behind what their child could already do.",
         "Lihat kelompok usia di atas anak Anda, bukan di bawahnya. Kebanyakan orang tua "
         "tertinggal satu langkah dari apa yang sebenarnya sudah bisa dilakukan anaknya."),
        ("Choose one responsibility from the band above your child's age and hand it over "
         "this week.",
         "Pilih satu tanggung jawab dari kelompok usia di atas anak Anda dan serahkan "
         "minggu ini."),
        ("What am I still doing for my child that they could do themselves?",
         "Apa yang masih saya kerjakan untuk anak saya padahal ia sudah bisa sendiri?"),
        ("\"You're old enough for this now. I'll show you once, then it's yours.\"",
         "\"Kamu sudah cukup besar untuk ini. Mama/Papa tunjukkan sekali, lalu ini jadi tugasmu.\""),
        framework=fw(
            ("What they can carry, roughly",
             "Kira-kira apa yang bisa mereka pegang"),
            ("A guide, not a test. Move a band up or down to fit the child in front of you.",
             "Panduan, bukan ujian. Naikkan atau turunkan satu kelompok sesuai anak yang ada di depan Anda."),
            [
                (("Ages 2-4", "Usia 2-4"),
                 [("Alongside you", "Bersama Anda")],
                 ("Put toys in the box, carry their plate, throw rubbish in the bin, choose "
                  "between two shirts.",
                  "Memasukkan mainan ke kotak, membawa piringnya, membuang sampah ke tempatnya, "
                  "memilih di antara dua baju."),
                 ("I am part of this family and my hands are useful.",
                  "Saya bagian dari keluarga ini dan tangan saya berguna.")),
                (("Ages 5-7", "Usia 5-7"),
                 [("With reminders", "Dengan pengingat")],
                 ("Set the table, make their bed roughly, pack their own school bag, feed a pet.",
                  "Menata meja makan, merapikan tempat tidurnya seadanya, menyiapkan tas "
                  "sekolahnya sendiri, memberi makan hewan peliharaan."),
                 ("Things do not happen by magic. Someone does them, and sometimes that is me.",
                  "Segala sesuatu tidak terjadi dengan sendirinya. Ada yang mengerjakannya, "
                  "dan kadang itu saya.")),
                (("Ages 8-11", "Usia 8-11"),
                 [("Mostly alone", "Sebagian besar sendiri")],
                 ("Wash their own dishes, handle homework without being sat with, keep track "
                  "of their own schedule, help cook a simple dish.",
                  "Mencuci piringnya sendiri, mengerjakan PR tanpa ditunggui, mengingat "
                  "jadwalnya sendiri, membantu memasak masakan sederhana."),
                 ("I can be relied on. People notice when I do not show up.",
                  "Saya bisa diandalkan. Orang tahu kalau saya tidak hadir.")),
                (("Ages 12+", "Usia 12+"),
                 [("Owns the outcome", "Memegang hasilnya")],
                 ("Manage their own money, cook a full meal, take responsibility for a "
                  "younger sibling for an hour, handle their own conflicts first.",
                  "Mengatur uangnya sendiri, memasak satu hidangan penuh, bertanggung jawab "
                  "atas adiknya selama satu jam, menangani konfliknya sendiri lebih dulu."),
                 ("My choices have consequences and I am the one who lives in them.",
                  "Pilihan saya punya akibat, dan saya yang menjalaninya.")),
            ],
        ),
    ),

    244: d(
        ("Building honesty",
         "Menumbuhkan kejujuran"),
        ("Honesty is not built by punishing lies. It is built by making the truth cheap "
         "enough to afford. A child lies when the cost of honesty is higher than the cost "
         "of being caught — and you set that price.\n\n"
         "So lower it. When a child tells you something hard and you keep your face and "
         "your voice steady, you have just taught them that the truth is survivable in "
         "this house. Do that a hundred times and you will still be hearing the truth when "
         "they are sixteen and the stakes are real.",
         "Kejujuran tidak dibangun dengan menghukum kebohongan. Ia dibangun dengan membuat "
         "kebenaran cukup murah untuk dibayar. Anak berbohong ketika ongkos jujur lebih "
         "tinggi daripada ongkos ketahuan — dan Andalah yang menentukan harganya.\n\n"
         "Jadi turunkan harganya. Ketika anak mengatakan sesuatu yang berat dan wajah serta "
         "suara Anda tetap tenang, Anda baru saja mengajarinya bahwa kebenaran bisa selamat "
         "di rumah ini. Lakukan itu seratus kali, dan Anda masih akan mendengar kebenaran "
         "saat ia enam belas tahun dan taruhannya nyata."),
        ("When your child tells you something you did not want to hear, thank them for the "
         "telling before you deal with the thing.",
         "Ketika anak mengatakan sesuatu yang tidak ingin Anda dengar, hargai dulu "
         "keberaniannya mengatakan, sebelum menangani perkaranya."),
        ("Respond to one piece of honesty today with steadiness instead of reaction.",
         "Tanggapi satu kejujuran hari ini dengan ketenangan, bukan reaksi."),
        ("Is the truth safe to tell in my house?",
         "Apakah kebenaran aman untuk diucapkan di rumah saya?"),
        ("\"Thank you for telling me. That took courage. Now let's sort it out.\"",
         "\"Terima kasih sudah memberi tahu. Itu butuh keberanian. Sekarang kita bereskan.\""),
    ),

    245: d(
        ("Building kindness",
         "Menumbuhkan kebaikan hati"),
        ("Kindness is not a feeling you can command. It is an action a child can practise "
         "until the feeling catches up. Telling a child to be kind produces compliance; "
         "giving them something specific to do produces the habit.\n\n"
         "And children read kindness where it is least performed — how you speak to the "
         "person taking your order, whether you carry something heavy for a neighbour, what "
         "you say about someone after they leave the room. That is the curriculum.",
         "Kebaikan hati bukan perasaan yang bisa diperintahkan. Ia tindakan yang bisa "
         "dilatih anak sampai perasaannya menyusul. Menyuruh anak berbaik hati menghasilkan "
         "kepatuhan; memberinya sesuatu yang konkret untuk dilakukan menghasilkan kebiasaan.\n\n"
         "Dan anak membaca kebaikan hati justru di tempat yang paling tidak dipertontonkan — "
         "bagaimana Anda bicara kepada orang yang mencatat pesanan Anda, apakah Anda "
         "membawakan barang berat untuk tetangga, apa yang Anda katakan tentang seseorang "
         "setelah ia pergi. Itulah kurikulumnya."),
        ("Make kindness concrete. \"Be nice to your sister\" is a wish. \"Ask her if she "
         "wants some\" is an instruction a child can follow.",
         "Buat kebaikan hati jadi konkret. \"Baik-baik sama adik\" itu harapan. \"Tanya dia "
         "mau atau tidak\" itu instruksi yang bisa dijalankan anak."),
        ("Give your child one specific kind action to do for someone today.",
         "Beri anak Anda satu tindakan baik yang konkret untuk dilakukan kepada seseorang hari ini."),
        ("How do I speak about people who cannot hear me?",
         "Bagaimana saya bicara tentang orang yang tidak bisa mendengar saya?"),
        ("\"Go and ask her if she wants some too.\"",
         "\"Coba tanya, dia mau juga tidak.\""),
    ),

    246: d(
        ("Building gratitude",
         "Menumbuhkan rasa syukur"),
        ("Gratitude that is demanded is not gratitude — it is a performance the child "
         "learns to produce on cue and feel nothing during. The word \"thank you\" extracted "
         "under pressure builds a habit of saying, not a habit of noticing.\n\n"
         "Real gratitude starts with attention. A child who is helped to see that someone "
         "woke early to cook this, or worked all week to pay for that, feels something "
         "before they say anything. Point at the person behind the thing.",
         "Rasa syukur yang dipaksa bukan rasa syukur — itu pertunjukan yang anak pelajari "
         "untuk ditampilkan saat diminta dan tidak dirasakan sama sekali. Kata \"terima "
         "kasih\" yang ditarik dengan tekanan membangun kebiasaan mengucapkan, bukan "
         "kebiasaan menyadari.\n\n"
         "Rasa syukur yang nyata dimulai dari perhatian. Anak yang dibantu melihat bahwa "
         "ada orang yang bangun pagi memasak ini, atau bekerja seminggu penuh untuk "
         "membayar itu, merasakan sesuatu sebelum mengucapkan apa pun. Tunjuk orang di "
         "balik bendanya."),
        ("Instead of \"say thank you,\" narrate the effort: \"Grandma got up early to make "
         "this for you.\" Let the child arrive at the feeling.",
         "Alih-alih \"bilang terima kasih\", ceritakan usahanya: \"Nenek bangun pagi-pagi "
         "untuk membuat ini untukmu.\" Biarkan anak sampai sendiri pada perasaannya."),
        ("Point out the person behind one everyday thing your child received today.",
         "Tunjukkan orang di balik satu hal biasa yang anak Anda terima hari ini."),
        ("Do I notice the effort behind what I am given?",
         "Apakah saya menyadari usaha di balik apa yang saya terima?"),
        ("\"Someone worked to make that happen for you. Did you see it?\"",
         "\"Ada orang yang berusaha supaya itu bisa terjadi untukmu. Kamu lihat tidak?\""),
    ),

    247: d(
        ("Building perseverance",
         "Menumbuhkan ketekunan"),
        ("Perseverance is not born from encouragement. It is born from having finished "
         "something hard once and remembering the feeling. Every time you rescue a child "
         "from a difficulty they could have survived, you take that memory away from them.\n\n"
         "So the work is mostly restraint. Sit near, stay warm, and do not take over. The "
         "child who wants to quit at minute four and finishes at minute nine has learned "
         "something no encouragement could have given them: that the wanting-to-quit "
         "feeling is not the end of the story.",
         "Ketekunan tidak lahir dari semangat yang diberikan. Ia lahir dari pernah "
         "menyelesaikan sesuatu yang sulit dan mengingat rasanya. Setiap kali Anda "
         "menyelamatkan anak dari kesulitan yang sebenarnya bisa ia lewati, Anda mengambil "
         "ingatan itu darinya.\n\n"
         "Jadi tugasnya sebagian besar adalah menahan diri. Duduk di dekatnya, tetap "
         "hangat, dan jangan mengambil alih. Anak yang ingin menyerah di menit keempat dan "
         "selesai di menit kesembilan telah belajar sesuatu yang tidak bisa diberikan oleh "
         "kalimat penyemangat mana pun: bahwa rasa ingin menyerah bukan akhir ceritanya."),
        ("When your child wants to quit, do not argue and do not take over. Move closer and "
         "say almost nothing.",
         "Ketika anak ingin menyerah, jangan berdebat dan jangan mengambil alih. Mendekatlah "
         "dan hampir tidak usah bicara."),
        ("Let your child finish one hard thing today without you doing it for them.",
         "Biarkan anak menyelesaikan satu hal sulit hari ini tanpa Anda kerjakan untuknya."),
        ("Whose discomfort am I actually rescuing — theirs or mine?",
         "Ketidaknyamanan siapa yang sebenarnya saya selamatkan — dia atau saya?"),
        ("\"This is the hard part. I'm right here. Keep going.\"",
         "\"Ini bagian yang sulitnya. Mama/Papa di sini. Lanjut terus.\""),
    ),

    248: d(
        ("Building humility",
         "Menumbuhkan kerendahan hati"),
        ("Humility is badly taught in most homes because it gets confused with smallness. "
         "Telling a child not to be proud of themselves does not build humility — it builds "
         "shame, and shame makes people defensive, which is the opposite of humble.\n\n"
         "Real humility is accuracy. It is being able to say \"I was wrong\" without the "
         "world ending, and \"I did that well\" without needing anyone to lose. Children "
         "learn it almost entirely from watching a parent admit a mistake out loud and stay "
         "exactly as loved as before.",
         "Kerendahan hati sering salah diajarkan di rumah karena tertukar dengan merasa "
         "kecil. Melarang anak bangga pada dirinya tidak membangun kerendahan hati — itu "
         "membangun rasa malu, dan rasa malu membuat orang defensif, yang justru lawan dari "
         "rendah hati.\n\n"
         "Kerendahan hati yang sejati adalah ketepatan menilai diri. Ia adalah bisa berkata "
         "\"saya salah\" tanpa dunia runtuh, dan \"itu saya kerjakan dengan baik\" tanpa "
         "perlu ada yang kalah. Anak mempelajarinya hampir sepenuhnya dari melihat orang "
         "tuanya mengakui kesalahan dengan lantang dan tetap sama dicintainya."),
        ("Say one mistake of your own out loud in front of your child this week, without "
         "excuses attached.",
         "Ucapkan satu kesalahan Anda sendiri di depan anak minggu ini, tanpa dibarengi alasan."),
        ("Admit something you got wrong today, in front of your child.",
         "Akui satu hal yang Anda lakukan salah hari ini, di depan anak Anda."),
        ("When did I last say \"I was wrong\" where my child could hear it?",
         "Kapan terakhir saya berkata \"saya salah\" di tempat anak saya bisa mendengarnya?"),
        ("\"I got that wrong. I've been thinking about it, and I want to do it differently.\"",
         "\"Itu Mama/Papa yang salah. Sudah dipikirkan, dan Mama/Papa mau melakukannya dengan cara lain.\""),
    ),

    249: d(
        ("Building courage",
         "Menumbuhkan keberanian"),
        ("Courage is not the absence of fear, and children need to be told this plainly "
         "because everything around them suggests otherwise. The brave child in the story "
         "never looks scared. The real brave child is shaking.\n\n"
         "So name it correctly. When your child does something frightening anyway, do not "
         "say \"see, it wasn't scary.\" That erases what they just did. Say \"you were "
         "scared and you did it\" — because that sentence is the definition, and it is the "
         "one they will repeat to themselves later.",
         "Keberanian bukan ketiadaan rasa takut, dan anak perlu diberi tahu ini dengan "
         "jelas karena segala hal di sekitarnya menyiratkan sebaliknya. Anak pemberani di "
         "cerita tidak pernah terlihat takut. Anak pemberani yang sungguhan sedang gemetar.\n\n"
         "Jadi sebutkan dengan tepat. Ketika anak Anda tetap melakukan sesuatu yang "
         "menakutkan, jangan berkata \"tuh, ternyata tidak menakutkan.\" Itu menghapus apa "
         "yang baru saja ia lakukan. Katakan \"kamu takut, dan kamu tetap melakukannya\" — "
         "karena kalimat itulah definisinya, dan itulah yang akan ia ulang kepada dirinya "
         "sendiri nanti."),
        ("Never talk a child out of their fear before they act. Acknowledge the fear, then "
         "stand beside them while they move.",
         "Jangan pernah membujuk anak agar tidak takut sebelum ia bertindak. Akui rasa "
         "takutnya, lalu berdiri di sampingnya saat ia melangkah."),
        ("Name one moment of your child's courage today using the word \"scared\" in it.",
         "Sebutkan satu momen keberanian anak hari ini dengan menyertakan kata \"takut\" di dalamnya."),
        ("Do I treat my child's fear as a problem to remove or a thing to walk through?",
         "Apakah saya memperlakukan rasa takut anak sebagai masalah yang harus dihapus atau "
         "sesuatu yang harus dilewati bersama?"),
        ("\"You were scared and you did it anyway. That's what brave actually is.\"",
         "\"Kamu takut dan tetap melakukannya. Itulah arti berani yang sebenarnya.\""),
    ),

    250: d(
        ("Building self-control",
         "Menumbuhkan pengendalian diri"),
        ("Self-control is a skill with a physical seat. It sits in a part of the brain that "
         "is not finished growing until the mid-twenties, which means every demand for "
         "self-control is a demand on a system still under construction.\n\n"
         "It is also a battery, not a trait. It drains through the day. The child who held "
         "it together for seven hours at school has nothing left at six in the evening — "
         "and that collapse is not a character failure, it is an empty battery. Build the "
         "skill in the morning; forgive the shortfall at night.",
         "Pengendalian diri adalah keterampilan yang punya tempat fisik. Ia berada di bagian "
         "otak yang belum selesai tumbuh sampai usia pertengahan dua puluhan, artinya setiap "
         "tuntutan pengendalian diri adalah tuntutan pada sistem yang masih dibangun.\n\n"
         "Ia juga baterai, bukan sifat bawaan. Ia terkuras sepanjang hari. Anak yang mampu "
         "menahan diri selama tujuh jam di sekolah tidak punya sisa apa-apa pada pukul enam "
         "sore — dan keruntuhan itu bukan kegagalan karakter, itu baterai yang habis. Latih "
         "keterampilannya di pagi hari; maafkan kekurangannya di malam hari."),
        ("Ask for self-control when the tank is full, not at the end of a long day. You are "
         "training a muscle, not testing loyalty.",
         "Mintalah pengendalian diri saat tangkinya penuh, bukan di ujung hari yang panjang. "
         "Anda sedang melatih otot, bukan menguji kesetiaan."),
        ("Notice what time of day your child's self-control runs out. Plan around it.",
         "Perhatikan jam berapa pengendalian diri anak Anda habis. Rencanakan sekitar itu."),
        ("Am I asking for control at the hour my child has the least of it?",
         "Apakah saya menuntut pengendalian diri di jam ketika anak saya paling tidak punya?"),
        ("\"That was hard to hold in, and you held it. I saw.\"",
         "\"Itu berat untuk ditahan, dan kamu bisa menahannya. Mama/Papa lihat kok.\""),
    ),

    251: d(
        ("Building generosity",
         "Menumbuhkan kemurahan hati"),
        ("Forced sharing teaches a child that their things are not really theirs, and a "
         "child who does not feel ownership cannot feel generosity — you cannot give away "
         "what was never yours to begin with.\n\n"
         "So secure ownership first. Let the child have a few things that nobody may take. "
         "Then, from that safe place, giving becomes a real choice rather than a "
         "confiscation, and a real choice is the only kind that builds anything.",
         "Memaksa anak berbagi mengajarinya bahwa barangnya sebenarnya bukan miliknya, dan "
         "anak yang tidak merasa memiliki tidak bisa merasa murah hati — Anda tidak bisa "
         "memberikan apa yang sejak awal bukan milik Anda.\n\n"
         "Jadi amankan dulu rasa memilikinya. Biarkan anak punya beberapa barang yang tidak "
         "boleh diambil siapa pun. Lalu, dari tempat aman itu, memberi menjadi pilihan yang "
         "sungguhan, bukan penyitaan — dan hanya pilihan yang sungguhan yang membangun sesuatu."),
        ("Let your child protect two or three things completely. Generosity grows out of "
         "security, never out of loss.",
         "Biarkan anak melindungi dua atau tiga barang sepenuhnya. Kemurahan hati tumbuh dari "
         "rasa aman, bukan dari kehilangan."),
        ("Let your child freely choose one thing to give or share today — and accept a no.",
         "Biarkan anak memilih sendiri satu hal untuk diberikan atau dibagi hari ini — dan "
         "terima kalau jawabannya tidak."),
        ("Do I ask my child to give away what they were never allowed to own?",
         "Apakah saya meminta anak memberikan sesuatu yang tidak pernah benar-benar boleh ia miliki?"),
        ("\"That one is yours and nobody takes it. The rest, you can decide.\"",
         "\"Yang itu milikmu dan tidak ada yang boleh mengambil. Sisanya, kamu yang memutuskan.\""),
    ),

    252: d(
        ("Building patience",
         "Menumbuhkan kesabaran"),
        ("Patience is waiting without falling apart, and a child can only learn it by "
         "waiting — in small amounts, on purpose, with support. A child whose every want is "
         "met within seconds has never had the chance to practise.\n\n"
         "The trick is to make waiting visible and finite. \"Later\" is unbearable because "
         "it has no shape. \"After we finish this song\" is survivable because the child can "
         "see the end coming. Give the wait an edge and the child can hold it.",
         "Kesabaran adalah menunggu tanpa hancur, dan anak hanya bisa mempelajarinya dengan "
         "menunggu — dalam takaran kecil, dengan sengaja, dengan pendampingan. Anak yang "
         "semua keinginannya dipenuhi dalam hitungan detik tidak pernah punya kesempatan "
         "berlatih.\n\n"
         "Kuncinya adalah membuat penantian terlihat dan ada ujungnya. \"Nanti\" tidak "
         "tertahankan karena tidak berbentuk. \"Setelah lagu ini selesai\" bisa dijalani "
         "karena anak melihat ujungnya mendekat. Beri tepi pada penantian, dan anak bisa "
         "memegangnya."),
        ("Replace \"later\" with a marker the child can see or hear ending: a song, a "
         "timer, the end of a street.",
         "Ganti \"nanti\" dengan penanda yang bisa dilihat atau didengar anak akan berakhir: "
         "satu lagu, pengatur waktu, ujung jalan."),
        ("Give one wait today a visible ending instead of the word \"later.\"",
         "Beri satu penantian hari ini ujung yang terlihat, bukan kata \"nanti\"."),
        ("How well do I wait in front of my child?",
         "Seberapa baik saya menunggu di depan anak saya?"),
        ("\"When this song finishes, it's your turn. Listen for the end.\"",
         "\"Kalau lagu ini selesai, giliranmu. Dengarkan ujungnya.\""),
    ),

    253: d(
        ("Building respect",
         "Menumbuhkan rasa hormat"),
        ("Respect demanded from above is obedience wearing a better name. It produces a "
         "child who is polite to power and dismissive to everyone below it — respectful to "
         "you, rude to the helper, cruel to the smaller child.\n\n"
         "Respect that lasts is learned by receiving it. When you knock before entering, "
         "apologise when you are wrong, and let your child finish their sentence, you are "
         "teaching a standard they will apply everywhere. Children do not do what you say "
         "about respect. They do what you did to them.",
         "Rasa hormat yang dituntut dari atas adalah kepatuhan yang memakai nama lebih "
         "bagus. Ia menghasilkan anak yang sopan kepada yang berkuasa dan meremehkan semua "
         "yang di bawahnya — hormat kepada Anda, kasar kepada asisten rumah tangga, kejam "
         "kepada anak yang lebih kecil.\n\n"
         "Rasa hormat yang bertahan dipelajari dengan menerimanya. Ketika Anda mengetuk "
         "sebelum masuk, minta maaf saat salah, dan membiarkan anak menyelesaikan "
         "kalimatnya, Anda sedang mengajarkan standar yang akan ia terapkan di mana-mana. "
         "Anak tidak melakukan apa yang Anda katakan tentang rasa hormat. Ia melakukan apa "
         "yang Anda lakukan kepadanya."),
        ("Watch how your child treats people who have no power over them. That is the true "
         "reading of what you have taught.",
         "Perhatikan bagaimana anak Anda memperlakukan orang yang tidak punya kuasa atasnya. "
         "Itulah bacaan sejati dari apa yang Anda ajarkan."),
        ("Show your child one act of respect today that you would normally skip — knock, "
         "wait, or let them finish.",
         "Tunjukkan satu tindakan hormat hari ini yang biasanya Anda lewati — mengetuk, "
         "menunggu, atau membiarkannya menyelesaikan kalimat."),
        ("How do I speak to the people in my home who cannot answer back?",
         "Bagaimana saya bicara kepada orang-orang di rumah saya yang tidak bisa membalas?"),
        ("\"I'm sorry, I interrupted you. Go on.\"",
         "\"Maaf, Mama/Papa memotong. Lanjutkan.\""),
    ),

    254: d(
        ("Building accountability",
         "Menumbuhkan tanggung gugat"),
        ("Accountability is not the same as blame. Blame asks who is at fault and stops "
         "there. Accountability asks what needs to happen now, and it always has a next "
         "step attached.\n\n"
         "A child who broke something needs to help fix it, not stand in shame while it is "
         "fixed around them. A child who hurt a friend needs to do something for that "
         "friend, not just say the word sorry and be released. The repair is the lesson. "
         "The apology alone teaches only that words end consequences.",
         "Tanggung gugat tidak sama dengan menyalahkan. Menyalahkan bertanya siapa yang "
         "salah lalu berhenti di situ. Tanggung gugat bertanya apa yang perlu dilakukan "
         "sekarang, dan selalu punya langkah lanjutan.\n\n"
         "Anak yang memecahkan sesuatu perlu ikut membereskannya, bukan berdiri dengan malu "
         "sementara orang lain membereskan di sekitarnya. Anak yang menyakiti temannya perlu "
         "melakukan sesuatu untuk teman itu, bukan hanya mengucapkan maaf lalu dibebaskan. "
         "Perbaikannya adalah pelajarannya. Permintaan maaf saja hanya mengajarkan bahwa "
         "kata-kata bisa mengakhiri akibat."),
        ("After every \"sorry,\" ask the next question: \"and what will you do about it?\"",
         "Setelah setiap \"maaf\", tanyakan pertanyaan berikutnya: \"lalu apa yang akan kamu "
         "lakukan soal itu?\""),
        ("Turn one apology today into a concrete repair.",
         "Ubah satu permintaan maaf hari ini menjadi perbaikan yang nyata."),
        ("Do I stop at sorry, or do I ask for the repair?",
         "Apakah saya berhenti di kata maaf, atau saya meminta perbaikannya?"),
        ("\"Sorry is the first part. What's the second part?\"",
         "\"Maaf itu bagian pertama. Bagian keduanya apa?\""),
    ),

    255: d(
        ("Building a growth mindset",
         "Menumbuhkan pola pikir bertumbuh"),
        ("\"You're so clever\" sounds like the kindest thing you can say and quietly does "
         "damage. It tells a child that ability is a fixed possession — and a child who "
         "believes that will avoid anything hard, because failing would mean losing the "
         "thing you praised.\n\n"
         "Praise the road, not the destination. \"You kept going after it went wrong\" "
         "points at something the child can repeat tomorrow. \"You're a natural\" points at "
         "something they can only lose.",
         "\"Kamu pintar sekali\" terdengar seperti hal paling baik yang bisa Anda ucapkan, "
         "dan diam-diam merusak. Ia memberi tahu anak bahwa kemampuan adalah milik yang "
         "tetap — dan anak yang mempercayai itu akan menghindari segala hal sulit, karena "
         "gagal berarti kehilangan hal yang Anda puji.\n\n"
         "Pujilah jalannya, bukan tujuannya. \"Kamu terus jalan setelah tadi gagal\" menunjuk "
         "pada sesuatu yang bisa anak ulang besok. \"Kamu memang berbakat\" menunjuk pada "
         "sesuatu yang hanya bisa ia hilangkan."),
        ("Praise the process out loud: the trying, the returning, the choosing the harder "
         "way. Skip the labels.",
         "Puji prosesnya dengan lantang: usahanya, kembalinya, pilihannya mengambil jalan "
         "yang lebih sulit. Lewati label-labelnya."),
        ("Replace one label-praise today with a description of what your child actually did.",
         "Ganti satu pujian berlabel hari ini dengan gambaran apa yang benar-benar anak lakukan."),
        ("What can my child repeat tomorrow from the praise I gave today?",
         "Apa yang bisa anak saya ulang besok dari pujian yang saya berikan hari ini?"),
        ("\"You tried it three times. That's the part that matters.\"",
         "\"Kamu mencoba tiga kali. Itu bagian yang penting.\""),
    ),

    256: d(
        ("Encouraging problem solving",
         "Mendorong anak memecahkan masalah"),
        ("Every time you solve a problem for a child who could have solved it, you take a "
         "small deposit out of their confidence. Do it often enough and you produce a "
         "capable child who does not believe they are capable.\n\n"
         "The alternative costs you nothing but patience. Ask before you answer: \"what "
         "have you tried?\" and then wait through the silence. Most children fill it. The "
         "answer they find themselves is worth ten of the answers you hand them.",
         "Setiap kali Anda menyelesaikan masalah untuk anak yang sebenarnya bisa "
         "menyelesaikannya sendiri, Anda mengambil sedikit tabungan dari rasa percaya "
         "dirinya. Lakukan cukup sering dan Anda menghasilkan anak yang mampu tetapi tidak "
         "percaya bahwa dirinya mampu.\n\n"
         "Alternatifnya tidak memakan apa pun kecuali kesabaran. Bertanyalah sebelum "
         "menjawab: \"kamu sudah coba apa?\" lalu tunggu dalam keheningan. Kebanyakan anak "
         "mengisinya. Jawaban yang ia temukan sendiri bernilai sepuluh kali jawaban yang "
         "Anda serahkan."),
        ("Hold your answer for thirty seconds. Ask \"what have you tried?\" and let the "
         "silence do the work.",
         "Tahan jawaban Anda selama tiga puluh detik. Tanyakan \"kamu sudah coba apa?\" dan "
         "biarkan keheningan bekerja."),
        ("Answer one of your child's problems today with a question instead of a solution.",
         "Jawab satu masalah anak hari ini dengan pertanyaan, bukan solusi."),
        ("How quickly do I jump in?",
         "Secepat apa saya turun tangan?"),
        ("\"What have you tried so far?\"",
         "\"Sejauh ini kamu sudah coba apa?\""),
    ),

    257: d(
        ("Allowing productive struggle",
         "Membiarkan perjuangan yang berguna"),
        ("There is a difference between a child who is struggling and a child who is "
         "drowning, and learning to tell them apart is one of the most useful skills a "
         "parent can develop.\n\n"
         "Struggle looks like effort with frustration in it — the child is still trying, "
         "still engaged, still in the task. Drowning looks like despair — the child has "
         "left the task and is now only feeling. Stay out of the first. Step into the "
         "second immediately.",
         "Ada perbedaan antara anak yang sedang berjuang dan anak yang sedang tenggelam, dan "
         "belajar membedakan keduanya adalah salah satu keterampilan paling berguna yang "
         "bisa dimiliki orang tua.\n\n"
         "Berjuang terlihat seperti usaha yang bercampur frustrasi — anak masih mencoba, "
         "masih terlibat, masih di dalam tugasnya. Tenggelam terlihat seperti keputusasaan — "
         "anak sudah meninggalkan tugasnya dan kini hanya merasakan. Jangan masuk ke yang "
         "pertama. Masuklah segera ke yang kedua."),
        ("Learn your child's two faces: frustrated-and-working versus finished-and-flooded. "
         "Only the second needs you.",
         "Kenali dua wajah anak Anda: frustrasi-tapi-masih-bekerja versus sudah-menyerah-dan-"
         "kewalahan. Hanya yang kedua yang membutuhkan Anda."),
        ("Watch one struggle today all the way through without intervening.",
         "Amati satu perjuangan hari ini sampai selesai tanpa ikut campur."),
        ("Can I tell the difference between struggling and drowning?",
         "Bisakah saya membedakan antara berjuang dan tenggelam?"),
        ("\"You're in the hard bit. That's normal. I'm not going anywhere.\"",
         "\"Kamu sedang di bagian sulitnya. Itu wajar. Mama/Papa tidak ke mana-mana.\""),
    ),

    258: d(
        ("Chores as contribution, not punishment",
         "Pekerjaan rumah sebagai kontribusi, bukan hukuman"),
        ("If chores are used as consequences, work becomes a punishment in the child's mind, "
         "and that association is hard to undo. Sweeping the floor should never be what "
         "happens when you are bad.\n\n"
         "Frame chores as membership instead. This family runs on the people in it, and you "
         "are one of them. Not paid, not earned, not a favour to the parent — simply what "
         "belonging looks like in practice. Children resist punishment. They rarely resist "
         "being needed.",
         "Kalau pekerjaan rumah dipakai sebagai hukuman, bekerja menjadi hukuman dalam pikiran "
         "anak, dan kaitan itu sulit dilepaskan. Menyapu lantai tidak boleh menjadi apa yang "
         "terjadi ketika kamu nakal.\n\n"
         "Bingkailah pekerjaan rumah sebagai keanggotaan. Keluarga ini berjalan karena "
         "orang-orang di dalamnya, dan kamu salah satunya. Bukan dibayar, bukan diperoleh, "
         "bukan jasa untuk orang tua — sekadar wujud nyata dari rasa memiliki. Anak melawan "
         "hukuman. Mereka jarang melawan rasa dibutuhkan."),
        ("Never assign a chore as a consequence. Assign it as a share of what the family "
         "needs done.",
         "Jangan pernah memberi pekerjaan rumah sebagai hukuman. Berikan sebagai bagian dari "
         "apa yang perlu dikerjakan keluarga."),
        ("Name one chore today as a contribution to the family, out loud.",
         "Sebutkan satu pekerjaan rumah hari ini sebagai kontribusi untuk keluarga, dengan lantang."),
        ("Is work a punishment or a belonging in my house?",
         "Apakah bekerja itu hukuman atau tanda memiliki di rumah saya?"),
        ("\"This is your part of running this house. We all have one.\"",
         "\"Ini bagianmu dalam menjalankan rumah ini. Kita semua punya bagian.\""),
    ),

    259: d(
        ("Pocket money and money habits",
         "Uang saku dan kebiasaan mengatur uang"),
        ("Money is a skill, and skills need practice with real stakes. A child who has never "
         "controlled money will not suddenly become good with it at eighteen, when the "
         "mistakes are expensive.\n\n"
         "So let them make small mistakes now. Give a small regular amount, let them spend "
         "it badly, and — this is the hard part — do not rescue them from the empty wallet. "
         "The disappointment of a wasted week's money at eight teaches more than any lecture "
         "and costs almost nothing.",
         "Uang adalah keterampilan, dan keterampilan perlu dilatih dengan taruhan yang nyata. "
         "Anak yang tidak pernah memegang uang tidak akan tiba-tiba pandai mengaturnya di usia "
         "delapan belas, saat kesalahannya mahal.\n\n"
         "Jadi biarkan ia membuat kesalahan kecil sekarang. Berikan jumlah kecil secara rutin, "
         "biarkan ia menghabiskannya dengan buruk, dan — ini bagian yang sulit — jangan "
         "menyelamatkannya dari dompet yang kosong. Kekecewaan karena uang seminggu habis "
         "sia-sia di usia delapan mengajarkan lebih banyak daripada ceramah mana pun, dan "
         "hampir tidak ada ongkosnya."),
        ("Give a small fixed amount at a fixed time. Let it run out. Do not top it up early.",
         "Berikan jumlah kecil yang tetap pada waktu yang tetap. Biarkan habis. Jangan "
         "menambah lebih awal."),
        ("Let one money decision today belong entirely to your child.",
         "Biarkan satu keputusan soal uang hari ini sepenuhnya jadi milik anak Anda."),
        ("Do I let my child feel the size of a mistake while it is still small?",
         "Apakah saya membiarkan anak merasakan besarnya kesalahan selagi masih kecil?"),
        ("\"It's yours to decide. And when it's gone, it's gone until next week.\"",
         "\"Kamu yang memutuskan. Dan kalau sudah habis, ya habis sampai minggu depan.\""),
    ),

    260: d(
        ("Delayed gratification games",
         "Permainan menunda kepuasan"),
        ("The famous marshmallow experiment is often told wrong. The children who waited "
         "were not more virtuous — many of them simply came from homes where a promise "
         "reliably came true, so waiting was worth the risk.\n\n"
         "That is the real lesson for parents: a child's ability to delay depends on whether "
         "the adult keeps their word. Every promise you keep raises the child's willingness "
         "to wait. Every one you quietly drop teaches them to grab what is in front of them.",
         "Eksperimen marshmallow yang terkenal sering diceritakan keliru. Anak-anak yang "
         "berhasil menunggu bukan lebih berbudi — banyak dari mereka datang dari rumah tempat "
         "janji memang ditepati, sehingga menunggu sepadan dengan risikonya.\n\n"
         "Itulah pelajaran sesungguhnya bagi orang tua: kemampuan anak menunda bergantung pada "
         "apakah orang dewasanya menepati kata-katanya. Setiap janji yang Anda tepati menaikkan "
         "kesediaan anak untuk menunggu. Setiap janji yang diam-diam Anda batalkan mengajarinya "
         "untuk menyambar apa yang ada di depan mata."),
        ("Make waiting a game with a guaranteed payoff, and then never fail to pay it. Your "
         "reliability is the whole mechanism.",
         "Jadikan menunggu sebuah permainan dengan hadiah yang pasti, lalu jangan pernah gagal "
         "membayarnya. Keandalan Andalah seluruh mekanismenya."),
        ("Make one small promise today and keep it visibly, on time.",
         "Buat satu janji kecil hari ini dan tepati dengan terlihat, tepat waktu."),
        ("Is my word reliable enough to be worth waiting for?",
         "Apakah kata-kata saya cukup bisa diandalkan untuk pantas ditunggu?"),
        ("\"I said after dinner, and it's after dinner. Here you go.\"",
         "\"Mama/Papa bilang setelah makan malam, dan sekarang sudah setelah makan malam. Ini.\""),
    ),

    261: d(
        ("Family service projects",
         "Kegiatan pelayanan keluarga"),
        ("Children learn that the world is bigger than their house by being taken into it "
         "with their hands, not by being told about it at the dinner table.\n\n"
         "Keep it small and real and repeated. Cook for a neighbour who is unwell. Sort "
         "clothes for a family who lost things. Visit someone nobody visits. What matters "
         "is not the size of the help but that the child does the actual work and sees the "
         "actual face — that combination is what changes how a person understands their "
         "own place in the world.",
         "Anak belajar bahwa dunia lebih besar dari rumahnya dengan dibawa ke dalamnya "
         "menggunakan tangannya sendiri, bukan dengan diceritakan di meja makan.\n\n"
         "Buat kecil, nyata, dan berulang. Memasak untuk tetangga yang sedang sakit. Memilah "
         "pakaian untuk keluarga yang kehilangan barang. Menengok orang yang tidak ada yang "
         "menengok. Yang penting bukan besarnya bantuan, melainkan bahwa anak mengerjakan "
         "pekerjaannya sendiri dan melihat wajahnya sendiri — perpaduan itulah yang mengubah "
         "cara seseorang memahami tempatnya di dunia."),
        ("Choose something the child can physically do, for someone whose face they will "
         "actually see.",
         "Pilih sesuatu yang bisa anak kerjakan sendiri secara fisik, untuk seseorang yang "
         "wajahnya benar-benar akan ia lihat."),
        ("Plan one small act of service your family will do together this month.",
         "Rencanakan satu tindakan pelayanan kecil yang akan keluarga Anda lakukan bersama bulan ini."),
        ("When did my child last help someone outside this family?",
         "Kapan terakhir anak saya membantu seseorang di luar keluarga ini?"),
        ("\"Let's do something for them this week. You carry it in.\"",
         "\"Minggu ini kita lakukan sesuatu untuk mereka. Kamu yang membawakannya masuk.\""),
    ),

    262: d(
        ("Teaching gratitude without forcing it",
         "Mengajarkan syukur tanpa memaksa"),
        ("A child ordered to feel grateful learns to fake a feeling, and faking feelings is "
         "a habit that generalises badly. Worse, the order usually arrives with a comparison "
         "attached — \"other children have nothing\" — which produces guilt, not gratitude. "
         "They are different emotions and they lead different places.\n\n"
         "Gratitude grows from noticing enough, not from being told you have too much. Build "
         "a daily habit of naming one good thing, and let the feeling arrive on its own "
         "schedule.",
         "Anak yang diperintah merasa bersyukur belajar memalsukan perasaan, dan memalsukan "
         "perasaan adalah kebiasaan yang menular ke mana-mana. Lebih buruk lagi, perintah itu "
         "biasanya datang dengan perbandingan — \"anak lain tidak punya apa-apa\" — yang "
         "menghasilkan rasa bersalah, bukan syukur. Keduanya emosi yang berbeda dan membawa ke "
         "tempat yang berbeda.\n\n"
         "Syukur tumbuh dari cukup sering menyadari, bukan dari diberi tahu bahwa Anda punya "
         "terlalu banyak. Bangun kebiasaan harian menyebut satu hal baik, dan biarkan "
         "perasaannya datang menurut jadwalnya sendiri."),
        ("Never use another child's hardship to produce gratitude. It produces guilt, and "
         "guilt closes the heart instead of opening it.",
         "Jangan pernah memakai kesusahan anak lain untuk memunculkan rasa syukur. Itu "
         "menghasilkan rasa bersalah, dan rasa bersalah menutup hati, bukan membukanya."),
        ("Name one good thing from today at bedtime, and let your child name one too.",
         "Sebutkan satu hal baik dari hari ini menjelang tidur, dan biarkan anak menyebut satu juga."),
        ("Am I building gratitude or borrowing guilt?",
         "Apakah saya sedang membangun rasa syukur atau meminjam rasa bersalah?"),
        ("\"What was one good thing today? I'll go first.\"",
         "\"Apa satu hal baik hari ini? Mama/Papa duluan, ya.\""),
    ),

    263: d(
        ("Teaching manners without humiliation",
         "Mengajarkan sopan santun tanpa mempermalukan"),
        ("Correcting a child's manners in front of guests teaches one lesson very "
         "efficiently: that you will trade their dignity for your image. That lesson lands "
         "much harder than the one about greeting properly.\n\n"
         "Teach manners in private and in advance. Rehearse the greeting in the car. Then in "
         "the room, if it goes wrong, let it go wrong. Correct it afterwards, quietly, with "
         "the child's face intact. Manners are for the comfort of others — they should not "
         "be installed by making the child uncomfortable in front of everyone.",
         "Menegur sopan santun anak di depan tamu mengajarkan satu pelajaran dengan sangat "
         "efisien: bahwa Anda bersedia menukar harga dirinya dengan citra Anda. Pelajaran itu "
         "menancap jauh lebih dalam daripada pelajaran tentang cara menyapa.\n\n"
         "Ajarkan sopan santun secara pribadi dan di muka. Latih cara menyapa di dalam mobil. "
         "Lalu di ruangan, kalau meleset, biarkan meleset. Perbaiki setelahnya, pelan-pelan, "
         "dengan muka anak tetap utuh. Sopan santun ada untuk kenyamanan orang lain — ia tidak "
         "seharusnya dipasang dengan membuat anak tidak nyaman di depan semua orang."),
        ("Rehearse before, correct after. Never in the middle, never in front of the audience.",
         "Latih sebelumnya, perbaiki sesudahnya. Jangan di tengah-tengah, jangan di depan penonton."),
        ("Rehearse one social moment with your child before it happens today.",
         "Latih satu momen sosial bersama anak sebelum itu terjadi hari ini."),
        ("Do I correct my child for their sake or for how it looks?",
         "Apakah saya menegur anak demi dia, atau demi bagaimana itu terlihat?"),
        ("\"Before we go in — what will you say when you meet her?\"",
         "\"Sebelum kita masuk — kamu mau bilang apa nanti waktu bertemu beliau?\""),
    ),

    264: d(
        ("Teaching hospitality",
         "Mengajarkan keramahan menerima tamu"),
        ("Hospitality is a beautiful thing to hand a child, and in many Indonesian homes it "
         "is already in the air. The trick is to give the child a real role in it rather "
         "than making them a decoration of it.\n\n"
         "Let them carry the tray. Let them show the guest where to sit. Let them ask if "
         "anyone wants more. A child with a job at a gathering is a child learning to think "
         "about other people's comfort — which is, in the end, what hospitality is.",
         "Keramahan menerima tamu adalah hal indah untuk diwariskan kepada anak, dan di banyak "
         "rumah Indonesia hal itu sudah ada di udaranya. Kuncinya adalah memberi anak peran "
         "yang sungguhan di dalamnya, bukan menjadikannya hiasan.\n\n"
         "Biarkan ia membawa nampan. Biarkan ia menunjukkan tempat duduk untuk tamu. Biarkan "
         "ia bertanya apakah ada yang mau tambah. Anak yang punya tugas dalam sebuah "
         "pertemuan adalah anak yang sedang belajar memikirkan kenyamanan orang lain — dan "
         "pada akhirnya, itulah keramahan."),
        ("Give the child one real job every time someone visits. Not a performance — a task "
         "that genuinely helps.",
         "Beri anak satu tugas yang nyata setiap kali ada tamu. Bukan pertunjukan — tugas yang "
         "benar-benar membantu."),
        ("Give your child one hosting job the next time someone comes over.",
         "Beri anak Anda satu tugas menerima tamu di kesempatan berikutnya."),
        ("Does my child have a role in our home, or only an audience seat?",
         "Apakah anak saya punya peran di rumah kami, atau hanya kursi penonton?"),
        ("\"You're in charge of drinks today. Ask everyone what they'd like.\"",
         "\"Hari ini kamu yang urus minuman. Tanya semua orang mau minum apa.\""),
    ),

    265: d(
        ("Teaching care for younger siblings",
         "Mengajarkan menjaga adik"),
        ("There is a version of this that builds a generous older child, and a version that "
         "quietly steals a childhood. The difference is whether the older child is helping "
         "or parenting.\n\n"
         "Helping is bounded: a task, a time, an adult still in charge. Parenting is "
         "unbounded: constant responsibility, blame when things go wrong, no off switch. The "
         "first builds warmth between siblings. The second builds resentment that can last "
         "for decades. Keep the boundary clear and keep the adult job with the adult.",
         "Ada versi yang membangun kakak yang murah hati, dan ada versi yang diam-diam mencuri "
         "masa kanak-kanak. Bedanya ada pada apakah si kakak sedang membantu atau sedang "
         "menjadi orang tua.\n\n"
         "Membantu itu ada batasnya: satu tugas, satu waktu, tetap ada orang dewasa yang "
         "bertanggung jawab. Menjadi orang tua itu tanpa batas: tanggung jawab terus-menerus, "
         "disalahkan kalau ada yang salah, tidak ada tombol berhentinya. Yang pertama "
         "membangun kehangatan antar saudara. Yang kedua membangun kebencian yang bisa "
         "bertahan puluhan tahun. Jaga batasnya tetap jelas dan biarkan tugas orang dewasa "
         "tetap pada orang dewasa."),
        ("Ask the older child for bounded help — one task, one stretch of time — and never "
         "blame them for the younger one's behaviour.",
         "Mintalah bantuan yang berbatas dari si kakak — satu tugas, satu jangka waktu — dan "
         "jangan pernah menyalahkannya atas perilaku adiknya."),
        ("Give your older child one bounded caring task today, then take the job back.",
         "Beri kakak satu tugas menjaga yang berbatas hari ini, lalu ambil kembali tugasnya."),
        ("Am I asking my older child to help, or to parent?",
         "Apakah saya meminta kakak untuk membantu, atau untuk menjadi orang tua?"),
        ("\"Watch him for ten minutes while I finish this — then you're off duty.\"",
         "\"Tolong temani adik sepuluh menit sementara ini Mama/Papa selesaikan — habis itu kamu bebas.\""),
    ),

    266: d(
        ("Teaching ownership of mistakes",
         "Mengajarkan mengakui kesalahan"),
        ("A child who cannot admit a mistake is usually a child who has learned that "
         "admitting one is dangerous. Defensiveness is not arrogance. It is protection, and "
         "it tells you something about what happened the last few times.\n\n"
         "The way in is to make owning a mistake cost less than hiding one. When your child "
         "admits something, the tone must drop, not rise. That is counter-intuitive and it "
         "is the whole technique: the moment of confession is the moment you are gentlest.",
         "Anak yang tidak bisa mengakui kesalahan biasanya anak yang sudah belajar bahwa "
         "mengakui itu berbahaya. Sikap defensif bukan kesombongan. Itu perlindungan, dan itu "
         "memberi tahu Anda sesuatu tentang apa yang terjadi beberapa kali terakhir.\n\n"
         "Jalan masuknya adalah membuat mengakui kesalahan lebih murah daripada "
         "menyembunyikannya. Ketika anak Anda mengakui sesuatu, nada suara harus turun, bukan "
         "naik. Itu berlawanan dengan naluri, dan itulah seluruh tekniknya: momen pengakuan "
         "adalah momen Anda paling lembut."),
        ("Drop your voice the moment your child admits something. Every time. That single "
         "habit rebuilds honesty faster than any rule.",
         "Turunkan nada suara Anda begitu anak mengakui sesuatu. Setiap kali. Kebiasaan tunggal "
         "itu membangun kembali kejujuran lebih cepat daripada aturan apa pun."),
        ("Meet one admission today with a softer voice than the one you started with.",
         "Sambut satu pengakuan hari ini dengan suara yang lebih lembut dari nada awal Anda."),
        ("What happens in my house the moment someone admits fault?",
         "Apa yang terjadi di rumah saya begitu ada yang mengaku salah?"),
        ("\"You told me yourself. That changes how we handle this.\"",
         "\"Kamu sendiri yang memberi tahu. Itu mengubah cara kita menanganinya.\""),
    ),

    267: d(
        ("Building independence in routines",
         "Membangun kemandirian dalam rutinitas"),
        ("Most parents are stuck helping with things their child stopped needing help with "
         "months ago, because the helping is faster and nobody noticed the moment it became "
         "unnecessary.\n\n"
         "Hand it over in stages, not all at once. First you do it while they watch. Then "
         "they do it while you narrate. Then they do it while you are in the room but "
         "silent. Then they do it and tell you when it is done. Four steps, and at the end "
         "you have your morning back and they have something better than a tidy shirt.",
         "Kebanyakan orang tua tersangkut membantu hal-hal yang anaknya sudah tidak butuh "
         "bantuan sejak berbulan-bulan lalu, karena membantu itu lebih cepat dan tidak ada "
         "yang menyadari kapan tepatnya itu jadi tidak perlu.\n\n"
         "Serahkan bertahap, bukan sekaligus. Pertama Anda yang mengerjakan sementara ia "
         "melihat. Lalu ia yang mengerjakan sementara Anda memandu dengan suara. Lalu ia yang "
         "mengerjakan sementara Anda ada di ruangan tapi diam. Lalu ia mengerjakan dan "
         "memberi tahu Anda saat selesai. Empat langkah, dan di ujungnya Anda mendapatkan "
         "pagi Anda kembali dan ia mendapatkan sesuatu yang lebih baik daripada baju yang rapi."),
        ("Move one task one step along the ladder this week: watch, narrate, silent, "
         "independent.",
         "Naikkan satu tugas satu anak tangga minggu ini: dilihat, dipandu, didampingi diam, mandiri."),
        ("Move one routine task one step closer to independent today.",
         "Naikkan satu tugas rutin satu langkah lebih dekat ke mandiri hari ini."),
        ("What am I still doing out of habit rather than need?",
         "Apa yang masih saya kerjakan karena kebiasaan, bukan karena perlu?"),
        ("\"You know how this goes now. I'll be here, but it's yours.\"",
         "\"Kamu sudah tahu caranya sekarang. Mama/Papa di sini, tapi ini tugasmu.\""),
    ),

    268: d(
        ("Letting children do hard things",
         "Membiarkan anak melakukan hal sulit"),
        ("Protecting a child from every hard thing feels like love and functions like a "
         "cage. A child who is never allowed to attempt something beyond them learns that "
         "you do not believe they can — and children usually agree with their parents about "
         "what they are capable of.\n\n"
         "So let them try things that are slightly too big. Let them fail at some of them "
         "with you nearby. The confidence you want them to have at twenty is built out of a "
         "hundred small hard things attempted at eight, and there is no shortcut that skips "
         "the attempting.",
         "Melindungi anak dari setiap hal sulit terasa seperti cinta dan berfungsi seperti "
         "sangkar. Anak yang tidak pernah diizinkan mencoba sesuatu di luar kemampuannya "
         "belajar bahwa Anda tidak percaya ia bisa — dan anak biasanya sependapat dengan orang "
         "tuanya tentang apa yang mampu ia lakukan.\n\n"
         "Jadi biarkan ia mencoba hal-hal yang sedikit terlalu besar. Biarkan ia gagal di "
         "sebagiannya dengan Anda di dekatnya. Rasa percaya diri yang Anda ingin ia punya di "
         "usia dua puluh dibangun dari seratus hal sulit kecil yang dicoba di usia delapan, "
         "dan tidak ada jalan pintas yang melewatkan mencobanya."),
        ("Say yes to one thing this week that makes you slightly nervous and is not actually "
         "dangerous.",
         "Katakan ya pada satu hal minggu ini yang membuat Anda sedikit waswas dan sebenarnya "
         "tidak berbahaya."),
        ("Let your child attempt one thing today that you would normally do for them.",
         "Biarkan anak mencoba satu hal hari ini yang biasanya Anda kerjakan untuknya."),
        ("What is my no actually protecting?",
         "Sebenarnya kata tidak saya sedang melindungi apa?"),
        ("\"It might not work. Try it anyway — I'm here.\"",
         "\"Mungkin tidak berhasil. Coba saja — Mama/Papa di sini.\""),
    ),

    269: d(
        ("Weekly reflection",
         "Refleksi mingguan"),
        ("Character work is slow and almost invisible from inside it, which is why a weekly "
         "look back matters more here than anywhere else in this guide. You will not see "
         "growth day to day. You will see it across weeks.\n\n"
         "Look for evidence rather than feelings: something your child did without being "
         "asked, a task that stopped needing reminders, an apology that arrived unprompted. "
         "One piece of evidence is a real week's progress. That is what this looks like when "
         "it is working.",
         "Kerja membangun karakter itu lambat dan hampir tak terlihat dari dalamnya, dan "
         "karena itulah menengok ke belakang seminggu sekali lebih penting di sini daripada di "
         "bagian mana pun dalam panduan ini. Anda tidak akan melihat pertumbuhannya dari hari "
         "ke hari. Anda akan melihatnya dari minggu ke minggu.\n\n"
         "Carilah bukti, bukan perasaan: sesuatu yang anak lakukan tanpa diminta, tugas yang "
         "berhenti butuh pengingat, permintaan maaf yang datang tanpa dipancing. Satu bukti "
         "sudah kemajuan nyata untuk seminggu. Begitulah bentuknya kalau ini sedang berhasil."),
        ("Write down one piece of evidence, not one feeling. Evidence survives a bad week; "
         "feelings do not.",
         "Tuliskan satu bukti, bukan satu perasaan. Bukti bertahan melewati minggu yang buruk; "
         "perasaan tidak."),
        ("Write down one thing your child did this week without being asked.",
         "Tuliskan satu hal yang anak Anda lakukan minggu ini tanpa diminta."),
        ("What did I see this week that I would have missed a month ago?",
         "Apa yang saya lihat minggu ini yang sebulan lalu pasti saya lewatkan?"),
        ("\"I noticed you did that without anyone asking. I saw it.\"",
         "\"Mama/Papa perhatikan kamu melakukan itu tanpa disuruh siapa pun. Itu terlihat kok.\""),
    ),

    270: d(
        ("Character review day",
         "Hari meninjau karakter"),
        ("Twenty-nine days on character, and the honest summary is short: your child is "
         "becoming someone, and most of what shapes that happens in the ordinary hours "
         "nobody records.\n\n"
         "Do not review this chapter by grading your child. Review it by looking at what you "
         "handed over and what you are still holding. The responsibilities a child carries "
         "at ten predict a great deal about the adult; the lectures they received predict "
         "almost nothing. Choose one thing to hand over this month, and hold it steady long "
         "enough to become theirs.",
         "Dua puluh sembilan hari tentang karakter, dan ringkasan jujurnya pendek: anak Anda "
         "sedang menjadi seseorang, dan sebagian besar yang membentuknya terjadi di jam-jam "
         "biasa yang tidak ada yang mencatat.\n\n"
         "Jangan tinjau bab ini dengan menilai anak Anda. Tinjaulah dengan melihat apa yang "
         "sudah Anda serahkan dan apa yang masih Anda pegang. Tanggung jawab yang dipikul anak "
         "di usia sepuluh sangat menentukan orang dewasa seperti apa ia nanti; ceramah yang ia "
         "terima hampir tidak menentukan apa-apa. Pilih satu hal untuk diserahkan bulan ini, "
         "dan pegang cukup lama sampai itu benar-benar menjadi miliknya."),
        ("Review what you handed over, not how your child performed. The list of "
         "responsibilities is the real scorecard.",
         "Tinjau apa yang Anda serahkan, bukan bagaimana anak Anda tampil. Daftar tanggung "
         "jawabnya itulah rapor yang sesungguhnya."),
        ("List everything your child now owns that they did not own six months ago.",
         "Daftarkan semua hal yang kini menjadi tanggung jawab anak Anda dan enam bulan lalu belum."),
        ("What will I hand over next?",
         "Apa yang akan saya serahkan berikutnya?"),
        ("\"You handle more now than you did six months ago. I've noticed.\"",
         "\"Sekarang kamu memegang lebih banyak dibanding enam bulan lalu. Mama/Papa perhatikan itu.\""),
    ),
}
