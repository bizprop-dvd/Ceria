# Chapter 6 — Emotional Coaching (days 152-181)
#
# Grounded in the founder's guidebook chapter 6 ("Name it to tame it") and
# toolkit tool 6 (Name-It-To-Tame-It Chart).
#
# Through-line: accept every feeling, guide the action.

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
    152: d(
        ("Emotion coaching overview",
         "Sekilas tentang pendampingan emosi"),
        ("Emotion coaching is a specific sequence, not a general warmth. It has four "
         "steps: notice the feeling, name it, allow it, and only then guide the "
         "behaviour.\n\n"
         "Most parents skip straight to step four, which is why so many hard moments "
         "last longer than they need to. A child whose feeling has not been "
         "acknowledged spends their energy insisting on it rather than moving through it.",
         "Pendampingan emosi adalah urutan yang spesifik, bukan sekadar kehangatan umum. "
         "Ia punya empat langkah: sadari perasaannya, namai, izinkan, dan baru setelah "
         "itu arahkan perilakunya.\n\n"
         "Kebanyakan orang tua langsung melompat ke langkah keempat, dan itulah sebabnya "
         "banyak momen sulit berlangsung lebih lama dari seharusnya. Anak yang perasaannya "
         "belum diakui menghabiskan tenaganya untuk bersikeras, bukan untuk melewatinya."),
        ("The four steps take about fifteen seconds. Skipping them usually costs ten "
         "minutes.",
         "Empat langkah itu memakan sekitar lima belas detik. Melewatinya biasanya "
         "menghabiskan sepuluh menit."),
        ("Run all four steps once today, in order, and notice how long the moment lasts.",
         "Jalankan keempat langkah sekali hari ini, berurutan, dan perhatikan berapa lama "
         "momennya bertahan."),
        ("Which of the four steps do I skip most often?",
         "Langkah mana dari keempatnya yang paling sering saya lewati?"),
        ("\"I see it. Let's sit with it a second.\"",
         "\"Mama/Papa lihat. Ayo kita rasakan sebentar.\""),
        framework=fw(
            ("The four steps", "Empat langkahnya"),
            ("In order. The behaviour step only works once the first three have happened.",
             "Berurutan. Langkah perilaku hanya berhasil setelah tiga langkah pertama terjadi."),
            [
                (("1. Notice", "1. Sadari"),
                 [("Before words", "Sebelum kata")],
                 ("Catch the feeling early — in the face, the body, the tone — before it "
                  "has become behaviour.",
                  "Tangkap perasaannya lebih awal — di wajah, tubuh, nada suara — sebelum "
                  "berubah menjadi perilaku."),
                 ("Small feelings caught early rarely become big ones.",
                  "Perasaan kecil yang ditangkap lebih awal jarang membesar.")),
                (("2. Name", "2. Namai"),
                 [("Give it a word", "Beri satu kata")],
                 ("Say what you think it is, tentatively: \"that looks like frustration.\"",
                  "Katakan apa yang Anda kira, dengan hati-hati: \"sepertinya itu rasa kesal.\""),
                 ("Naming a feeling measurably lowers its intensity, in children and adults.",
                  "Menamai perasaan terbukti menurunkan intensitasnya, pada anak maupun orang dewasa.")),
                (("3. Allow", "3. Izinkan"),
                 [("No fixing yet", "Belum membetulkan")],
                 ("Let the feeling exist without arguing with it, minimising it or "
                  "rushing to solve it.",
                  "Biarkan perasaan itu ada tanpa dibantah, dikecilkan, atau buru-buru diselesaikan."),
                 ("This is the step most often skipped, and the one that ends the moment "
                  "fastest.",
                  "Inilah langkah yang paling sering dilewati, dan yang paling cepat mengakhiri momennya.")),
                (("4. Guide", "4. Arahkan"),
                 [("Now the limit", "Baru batasnya")],
                 ("Now address the behaviour: \"you can be furious AND you cannot hit.\"",
                  "Baru tangani perilakunya: \"kamu boleh sangat marah DAN tidak boleh memukul.\""),
                 ("The limit holds fully. It simply arrives after the feeling was received.",
                  "Batasnya tetap penuh. Ia hanya datang setelah perasaannya diterima.")),
            ],
        ),
    ),
    153: d(
        ("Emotions are not misbehavior",
         "Emosi bukan kenakalan"),
        ("Anger is not rudeness. Sadness is not manipulation. Fear is not weakness. "
         "Feelings arrive unbidden and are not moral events — what a child does with them "
         "is.\n\n"
         "Punishing a feeling teaches a child to hide it, and a hidden feeling does not "
         "disappear. It simply stops being something you can help with.",
         "Marah bukan kekurangajaran. Sedih bukan manipulasi. Takut bukan kelemahan. "
         "Perasaan datang tanpa diundang dan bukan peristiwa moral — yang dilakukan anak "
         "dengan perasaan itulah yang moral.\n\n"
         "Menghukum perasaan mengajarkan anak menyembunyikannya, dan perasaan yang "
         "disembunyikan tidak hilang. Ia hanya berhenti menjadi sesuatu yang bisa Anda bantu."),
        ("\"Don't be angry\" is an instruction no human can follow. \"You can be angry, "
         "and you cannot throw that\" is one every child can.",
         "\"Jangan marah\" adalah instruksi yang tak bisa dituruti manusia mana pun. \"Kamu "
         "boleh marah, dan tidak boleh melempar itu\" bisa dituruti setiap anak."),
        ("Separate the feeling from the action once today, out loud.",
         "Pisahkan perasaan dari tindakan sekali hari ini, dengan suara."),
        ("Do I treat any of my child's feelings as bad behaviour?",
         "Apakah saya memperlakukan sebagian perasaan anak sebagai perilaku buruk?"),
        ("\"The feeling is fine. That action isn't.\"",
         "\"Perasaannya tidak apa-apa. Tindakannya yang tidak boleh.\""),
    ),
    154: d(
        ("Accept feelings, guide actions",
         "Terima perasaan, arahkan tindakan"),
        ("This is the sentence the whole chapter rests on. Every feeling is allowed; not "
         "every action is. Holding both halves at once is what makes a child feel "
         "understood and still safely bounded.\n\n"
         "Parents who only accept feelings end up without limits. Parents who only guide "
         "actions end up without trust. You need both, in that order.",
         "Inilah kalimat yang menopang seluruh bab ini. Setiap perasaan diizinkan; tidak "
         "setiap tindakan. Memegang kedua bagian sekaligus itulah yang membuat anak merasa "
         "dimengerti sekaligus terjaga dengan aman.\n\n"
         "Orang tua yang hanya menerima perasaan berakhir tanpa batas. Orang tua yang hanya "
         "mengarahkan tindakan berakhir tanpa kepercayaan. Anda butuh keduanya, dalam urutan itu."),
        ("The word that joins them is AND, never BUT. \"But\" cancels whatever came before "
         "it; \"and\" lets both stand.",
         "Kata yang menyatukannya adalah DAN, bukan TAPI. \"Tapi\" membatalkan apa pun "
         "sebelumnya; \"dan\" membiarkan keduanya berdiri."),
        ("Use \"and\" instead of \"but\" in every correction today.",
         "Gunakan \"dan\" alih-alih \"tapi\" dalam setiap teguran hari ini."),
        ("How often do I cancel my own empathy with the word but?",
         "Seberapa sering saya membatalkan empati saya sendiri dengan kata tapi?"),
        ("\"You're allowed to feel that, and we still can't do that.\"",
         "\"Kamu boleh merasa begitu, dan kita tetap tidak boleh melakukan itu.\""),
    ),
    155: d(
        ("Naming feelings",
         "Menamai perasaan"),
        ("Naming is the mechanism, not a nicety. When a feeling receives a label, the "
         "storm settles measurably — \"frustrated\" is calmer than the wordless, hot, "
         "full-body version of the same thing.\n\n"
         "Offer the name tentatively rather than declaring it. A child correcting you — "
         "\"no, I'm embarrassed\" — has just done the exact work you were hoping for.",
         "Menamai adalah mekanismenya, bukan basa-basi. Ketika sebuah perasaan mendapat "
         "label, badainya mereda secara terukur — \"kesal\" lebih tenang daripada versi "
         "tanpa kata, panas, dan memenuhi seluruh tubuh dari hal yang sama.\n\n"
         "Tawarkan namanya dengan hati-hati, jangan menyatakannya. Anak yang membetulkan "
         "Anda — \"bukan, aku malu\" — baru saja melakukan persis pekerjaan yang Anda harapkan."),
        ("\"Is that frustrated or is it disappointed?\" invites a child into their own "
         "experience instead of handing them a verdict about it.",
         "\"Itu kesal atau kecewa?\" mengajak anak masuk ke pengalamannya sendiri, bukan "
         "menyodorkan vonis tentangnya."),
        ("Offer a feeling word as a question today, not a statement.",
         "Tawarkan satu kata perasaan sebagai pertanyaan hari ini, bukan pernyataan."),
        ("Do I tell my child what they feel, or ask?",
         "Apakah saya memberi tahu anak apa yang dia rasakan, atau bertanya?"),
        ("\"That looks like frustration. Am I close?\"",
         "\"Sepertinya itu kesal. Mendekati?\""),
    ),
    156: d(
        ("Teaching calming tools",
         "Mengajarkan cara menenangkan diri"),
        ("Children do not calm down because they are told to. They calm down because they "
         "have a tool and have practised it when nothing was wrong.\n\n"
         "Teach the tool in a calm moment; use it in a hard one. A breathing technique "
         "introduced mid-meltdown has never worked for anyone.",
         "Anak tidak menjadi tenang karena disuruh. Mereka menjadi tenang karena punya "
         "alat dan sudah melatihnya saat tak ada masalah.\n\n"
         "Ajarkan alatnya di momen tenang; pakai di momen sulit. Teknik pernapasan yang "
         "diperkenalkan di tengah meltdown tak pernah berhasil untuk siapa pun."),
        ("Blowing out imaginary candles, squeezing a cushion, counting things that are "
         "blue — small, concrete, practised in advance.",
         "Meniup lilin khayalan, meremas bantal, menghitung benda berwarna biru — kecil, "
         "konkret, dan sudah dilatih sebelumnya."),
        ("Practise one calming tool today while everyone is calm.",
         "Latih satu cara menenangkan diri hari ini selagi semua orang tenang."),
        ("Does my child have any tool at all, or only my instruction to calm down?",
         "Apakah anak saya punya alat, atau hanya perintah saya untuk tenang?"),
        ("\"Let's practise it now, while it's easy.\"",
         "\"Ayo kita latih sekarang, selagi mudah.\""),
    ),
    157: d(
        ("Comfort before correction",
         "Menenangkan sebelum menegur"),
        ("A distressed child cannot learn. The thinking part of the brain is offline, and "
         "any lesson delivered there is lost — often along with some trust.\n\n"
         "Comfort first, teach later. \"Later\" can be five minutes; it does not have to "
         "be a different day, and the lesson still lands.",
         "Anak yang sedang tertekan tak bisa belajar. Bagian otak yang berpikir sedang "
         "tidak aktif, dan pelajaran apa pun yang disampaikan di sana akan hilang — sering "
         "bersama sebagian kepercayaannya.\n\n"
         "Tenangkan dulu, ajarkan kemudian. \"Kemudian\" bisa berarti lima menit; tak harus "
         "hari yang berbeda, dan pelajarannya tetap sampai."),
        ("The lesson delivered at full volume during the storm is remembered as the storm. "
         "The same lesson five minutes later is remembered as the lesson.",
         "Pelajaran yang disampaikan dengan suara penuh di tengah badai diingat sebagai "
         "badainya. Pelajaran yang sama lima menit kemudian diingat sebagai pelajarannya."),
        ("Delay one correction today until your child is genuinely calm.",
         "Tunda satu teguran hari ini sampai anak benar-benar tenang."),
        ("Am I teaching at the moment my child is least able to hear it?",
         "Apakah saya mengajar tepat saat anak paling tidak mampu mendengarnya?"),
        ("\"First let's settle. We'll talk in a minute.\"",
         "\"Kita tenang dulu. Sebentar lagi kita bicara.\""),
    ),
    158: d(
        ("Helping children tolerate frustration",
         "Membantu anak menahan frustrasi"),
        ("Frustration tolerance grows through manageable difficulty with someone steady "
         "nearby. Too much help and it never builds; too little and the child is "
         "overwhelmed into avoidance.\n\n"
         "The useful position is beside them, narrating rather than rescuing: \"that bit "
         "is tricky — try turning it.\"",
         "Ketahanan menghadapi frustrasi tumbuh lewat kesulitan yang terkelola dengan "
         "seseorang yang stabil di dekatnya. Terlalu banyak bantuan, ia tak pernah "
         "terbangun; terlalu sedikit, anak kewalahan dan memilih menghindar.\n\n"
         "Posisi yang berguna adalah di sampingnya, menarasikan alih-alih menyelamatkan: "
         "\"bagian itu memang sulit — coba diputar.\""),
        ("Waiting one extra minute before helping is often the entire intervention.",
         "Menunggu satu menit lebih lama sebelum membantu sering kali sudah seluruh intervensinya."),
        ("Narrate instead of rescuing once today.",
         "Narasikan alih-alih menyelamatkan sekali hari ini."),
        ("Do I step in because my child needs it, or because their struggle is hard for me?",
         "Apakah saya turun tangan karena anak membutuhkannya, atau karena perjuangannya berat bagi saya?"),
        ("\"That's a hard bit. I'm right here while you try.\"",
         "\"Itu bagian yang sulit. Mama/Papa di sini sambil kamu coba.\""),
    ),
    159: d(
        ("Helping children handle disappointment",
         "Membantu anak menghadapi kekecewaan"),
        ("Disappointment cannot be argued away, and trying makes it worse. The instinct to "
         "explain why it is not so bad reads to a child as their feeling being dismissed.\n\n"
         "Sit with it briefly, name it, and resist the urge to immediately offer a "
         "replacement. Learning that disappointment passes is more valuable than being "
         "spared it.",
         "Kekecewaan tak bisa dihilangkan dengan perdebatan, dan mencobanya justru "
         "memperburuk. Dorongan untuk menjelaskan bahwa \"tidak seburuk itu\" terbaca oleh "
         "anak sebagai perasaannya diabaikan.\n\n"
         "Temani sebentar, namai, dan tahan dorongan untuk langsung menawarkan pengganti. "
         "Belajar bahwa kekecewaan itu berlalu lebih berharga daripada dihindarkan darinya."),
        ("\"I know. You really wanted that\" ends it faster than a list of reasons it does "
         "not matter.",
         "\"Mama tahu. Kamu benar-benar menginginkannya\" mengakhirinya lebih cepat "
         "daripada daftar alasan bahwa itu tidak penting."),
        ("Let one disappointment stand today without fixing or replacing it.",
         "Biarkan satu kekecewaan berdiri hari ini tanpa dibetulkan atau diganti."),
        ("Do I rush to fix disappointment because my child needs it, or because I do?",
         "Apakah saya buru-buru membereskan kekecewaan karena anak membutuhkannya, atau karena saya?"),
        ("\"I know. You really wanted that.\"",
         "\"Mama/Papa tahu. Kamu benar-benar menginginkannya.\""),
    ),
    160: d(
        ("Helping children handle embarrassment",
         "Membantu anak menghadapi rasa malu"),
        ("Embarrassment is felt more intensely by children than adults remember, and it "
         "is made much worse by an audience. A child who is embarrassed usually wants "
         "the moment to be smaller, not discussed.\n\n"
         "Reduce the audience, lower your voice, and address it later in private. Teasing "
         "about it, even affectionately, tends to be remembered for years.",
         "Rasa malu dirasakan anak jauh lebih kuat daripada yang diingat orang dewasa, dan "
         "jauh memburuk bila ada penonton. Anak yang malu biasanya ingin momennya menjadi "
         "lebih kecil, bukan dibahas.\n\n"
         "Kurangi penontonnya, pelankan suara, dan bahas nanti secara pribadi. Menggoda "
         "soal itu, bahkan dengan sayang, cenderung diingat bertahun-tahun."),
        ("Stepping between your child and the onlookers does more than any words. Make "
         "the moment smaller first.",
         "Berdiri di antara anak dan orang-orang yang menonton lebih berguna daripada "
         "kata-kata apa pun. Perkecil momennya dulu."),
        ("Shrink one embarrassing moment today instead of discussing it.",
         "Perkecil satu momen memalukan hari ini alih-alih membahasnya."),
        ("Do I ever make my child's embarrassment into a family story?",
         "Apakah saya pernah menjadikan rasa malu anak sebagai cerita keluarga?"),
        ("\"Come here. We'll talk about it later, just us.\"",
         "\"Sini. Nanti kita bicarakan berdua saja.\""),
    ),
    161: d(
        ("Helping children handle jealousy",
         "Membantu anak menghadapi rasa cemburu"),
        ("Jealousy is usually a fear about supply — that there is not enough love, "
         "attention or fairness to go around. Shaming it drives it underground, where it "
         "comes out sideways at a sibling.\n\n"
         "Naming it without judgement is what shrinks it: \"it's hard when she gets "
         "something and you don't.\"",
         "Cemburu biasanya adalah ketakutan soal persediaan — bahwa kasih sayang, "
         "perhatian, atau keadilan tidak cukup untuk semua. Mempermalukannya membuatnya "
         "turun ke bawah tanah, lalu keluar menyamping ke arah saudaranya.\n\n"
         "Menamainya tanpa menghakimi itulah yang mengecilkannya: \"berat ya, saat dia dapat "
         "sesuatu dan kamu tidak.\""),
        ("\"Don't be jealous\" has never once reduced jealousy. Naming it accurately "
         "usually does within a minute or two.",
         "\"Jangan cemburu\" tak pernah sekali pun mengurangi rasa cemburu. Menamainya "
         "dengan tepat biasanya berhasil dalam satu dua menit."),
        ("Name jealousy without judgement today if it appears.",
         "Namai rasa cemburu tanpa menghakimi hari ini jika ia muncul."),
        ("What is my child actually afraid of running out of?",
         "Anak saya sebenarnya takut kehabisan apa?"),
        ("\"It's hard watching that. Makes sense.\"",
         "\"Berat ya melihat itu. Wajar kok.\""),
    ),
    162: d(
        ("Helping children handle fear",
         "Membantu anak menghadapi rasa takut"),
        ("Fear does not respond to logic, because it was not built by logic. Explaining "
         "that something is impossible rarely helps a frightened child and often adds "
         "shame to the fear.\n\n"
         "What works is company plus a small piece of control: check together, leave a "
         "light, give them something they can do.",
         "Rasa takut tidak menanggapi logika, karena ia memang tidak dibangun oleh logika. "
         "Menjelaskan bahwa sesuatu mustahil jarang membantu anak yang ketakutan dan sering "
         "menambahkan rasa malu di atas rasa takutnya.\n\n"
         "Yang berhasil adalah kehadiran ditambah sepotong kendali: periksa bersama, biarkan "
         "satu lampu menyala, beri dia sesuatu yang bisa dia lakukan."),
        ("Bravery is not the absence of fear. It is doing the thing while afraid, which "
         "requires the fear to be allowed to exist first.",
         "Berani bukan tiadanya rasa takut. Berani adalah melakukannya sambil takut — dan "
         "itu menuntut rasa takutnya diizinkan ada lebih dulu."),
        ("Meet one fear with company and a small piece of control today.",
         "Hadapi satu ketakutan dengan kehadiran dan sepotong kendali kecil hari ini."),
        ("Do I try to talk my child out of fear, or help them carry it?",
         "Apakah saya membujuk anak agar tidak takut, atau membantunya memikulnya?"),
        ("\"It's okay to be scared. I'll come with you.\"",
         "\"Tidak apa-apa takut. Mama/Papa temani.\""),
    ),
    163: d(
        ("Helping children handle anger",
         "Membantu anak menghadapi kemarahan"),
        ("Anger is usually a second feeling sitting on top of a first one — hurt, fear, "
         "powerlessness, or shame. Treating the anger alone tends to miss what is "
         "actually going on.\n\n"
         "Allow the anger fully, hold the behaviour limit firmly, and look underneath it "
         "once everyone is calm.",
         "Kemarahan biasanya perasaan kedua yang duduk di atas perasaan pertama — terluka, "
         "takut, tak berdaya, atau malu. Menangani kemarahannya saja cenderung melewatkan "
         "apa yang sebenarnya terjadi.\n\n"
         "Izinkan kemarahannya sepenuhnya, pegang batas perilakunya dengan tegas, dan "
         "tengok apa yang ada di baliknya setelah semua tenang."),
        ("The child who is furious about a lost game is often not angry about the game. "
         "They are ashamed of losing in front of someone.",
         "Anak yang murka karena kalah permainan sering bukan marah soal permainannya. Dia "
         "malu karena kalah di depan orang lain."),
        ("Look for the feeling underneath one burst of anger today.",
         "Cari perasaan di balik satu ledakan kemarahan hari ini."),
        ("What tends to sit underneath my child's anger?",
         "Apa yang biasanya ada di balik kemarahan anak saya?"),
        ("\"You're furious. Something hurt first, I think.\"",
         "\"Kamu marah sekali. Sepertinya ada yang menyakitkan lebih dulu.\""),
    ),
    164: d(
        ("Helping children handle sadness",
         "Membantu anak menghadapi kesedihan"),
        ("Sadness makes adults uncomfortable, so we rush it — distract, cheer up, offer a "
         "treat. A child learns from this that sadness is not welcome here.\n\n"
         "Sadness does not need fixing. It needs company. Sitting quietly beside a sad "
         "child, doing nothing, is genuinely the skill.",
         "Kesedihan membuat orang dewasa tidak nyaman, jadi kita memburu-burunya — "
         "mengalihkan, menghibur, menawarkan sesuatu. Anak belajar dari ini bahwa kesedihan "
         "tidak diterima di sini.\n\n"
         "Kesedihan tidak perlu dibereskan. Ia butuh ditemani. Duduk diam di samping anak "
         "yang sedih, tanpa melakukan apa pun, sungguh-sungguh adalah keterampilannya."),
        ("\"Do you want to talk, or do you want me to just sit here?\" is one of the most "
         "useful questions in parenting.",
         "\"Mau cerita, atau mau Mama duduk di sini saja?\" adalah salah satu pertanyaan "
         "paling berguna dalam pengasuhan."),
        ("Sit with one sad moment today without trying to lift it.",
         "Temani satu momen sedih hari ini tanpa berusaha mengangkatnya."),
        ("Can I be near my child's sadness without needing to end it?",
         "Bisakah saya berada dekat kesedihan anak tanpa perlu mengakhirinya?"),
        ("\"You don't have to cheer up. I'll stay.\"",
         "\"Kamu tidak harus langsung senang. Mama/Papa tetap di sini.\""),
    ),
    165: d(
        ("Helping children recover after conflict",
         "Membantu anak pulih setelah bentrok"),
        ("What happens after a conflict matters more than the conflict. A child left alone "
         "in the aftermath concludes that being difficult costs them the relationship.\n\n"
         "You do not need a long conversation. Returning warmly, once things have settled, "
         "does almost all of the work.",
         "Apa yang terjadi setelah bentrok lebih penting daripada bentroknya. Anak yang "
         "ditinggal sendirian sesudahnya menyimpulkan bahwa menjadi sulit membuatnya "
         "kehilangan hubungan.\n\n"
         "Anda tak perlu percakapan panjang. Kembali dengan hangat, setelah semuanya reda, "
         "sudah melakukan hampir seluruh pekerjaannya."),
        ("A hand on the back and \"we're okay\" repairs more than a twenty-minute "
         "post-mortem of what went wrong.",
         "Tangan di punggung dan \"kita baik-baik saja\" memperbaiki lebih banyak daripada "
         "dua puluh menit membedah apa yang salah."),
        ("Return warmly after the next difficult moment, without re-litigating it.",
         "Kembalilah dengan hangat setelah momen sulit berikutnya, tanpa mengungkitnya lagi."),
        ("What does my child conclude from how our conflicts end?",
         "Apa kesimpulan anak dari cara pertengkaran kami berakhir?"),
        ("\"We're okay. That's over now.\"",
         "\"Kita baik-baik saja. Itu sudah selesai.\""),
    ),
    166: d(
        ("What not to say to upset children",
         "Yang sebaiknya tidak dikatakan pada anak yang kesal"),
        ("A short list of phrases that reliably make things worse, all of them well "
         "intentioned: \"you're fine\", \"stop crying\", \"it's not a big deal\", \"other "
         "children have it worse\", \"you're being dramatic\".\n\n"
         "Each one tells a child their read on their own experience is wrong. That is the "
         "opposite of what emotional development needs.",
         "Sebuah daftar pendek kalimat yang selalu memperburuk keadaan, semuanya dengan "
         "niat baik: \"kamu tidak apa-apa\", \"berhenti menangis\", \"itu bukan masalah "
         "besar\", \"anak lain lebih susah\", \"kamu berlebihan\".\n\n"
         "Masing-masing memberi tahu anak bahwa pembacaannya atas pengalamannya sendiri "
         "keliru. Itu kebalikan dari yang dibutuhkan perkembangan emosi."),
        ("Replace all of them with one sentence: \"that's hard.\" It is almost always true "
         "and it almost always helps.",
         "Ganti semuanya dengan satu kalimat: \"itu berat ya.\" Hampir selalu benar dan "
         "hampir selalu membantu."),
        ("Catch one of these phrases before it leaves your mouth today.",
         "Tangkap salah satu kalimat ini sebelum keluar dari mulut Anda hari ini."),
        ("Which of these did I hear as a child, and which do I still say?",
         "Kalimat mana dari ini yang saya dengar sewaktu kecil, dan mana yang masih saya ucapkan?"),
        ("\"That's hard.\"",
         "\"Itu berat, ya.\""),
    ),
    167: d(
        ("Emotion coaching during tantrums",
         "Mendampingi emosi saat tantrum"),
        ("During a full tantrum, coaching is mostly presence. The child cannot process "
         "language well, so long sentences are wasted and questions are unanswerable.\n\n"
         "Stay close, stay calm, keep everyone safe, and say very little. The coaching "
         "happens afterwards.",
         "Saat tantrum sedang penuh, mendampingi sebagian besar berarti hadir. Anak belum "
         "bisa mengolah bahasa dengan baik, jadi kalimat panjang terbuang dan pertanyaan "
         "tak terjawab.\n\n"
         "Tetap dekat, tetap tenang, jaga semua orang aman, dan bicara sesedikit mungkin. "
         "Pendampingannya terjadi sesudahnya."),
        ("Three or four words, repeated calmly, is the right amount of language: \"I'm "
         "here. You're safe.\"",
         "Tiga atau empat kata, diulang dengan tenang, adalah takaran bahasa yang tepat: "
         "\"Mama di sini. Kamu aman.\""),
        ("Use fewer than six words during the next tantrum.",
         "Gunakan kurang dari enam kata saat tantrum berikutnya."),
        ("How much do I talk during a tantrum, and does any of it land?",
         "Seberapa banyak saya bicara saat tantrum, dan adakah yang sampai?"),
        ("\"I'm here. You're safe.\"",
         "\"Mama/Papa di sini. Kamu aman.\""),
    ),
    168: d(
        ("Emotion coaching after tantrums",
         "Mendampingi emosi setelah tantrum"),
        ("The teaching window opens once a child is calm and connected again — usually "
         "some minutes after, sometimes at bedtime.\n\n"
         "Keep it short and curious rather than corrective: what happened, what it felt "
         "like, what might help next time. A long inquest turns the repair back into a "
         "conflict.",
         "Jendela pengajaran terbuka setelah anak tenang dan terhubung kembali — biasanya "
         "beberapa menit sesudahnya, kadang menjelang tidur.\n\n"
         "Buatlah singkat dan penuh rasa ingin tahu, bukan menegur: apa yang terjadi, "
         "bagaimana rasanya, apa yang mungkin membantu lain kali. Interogasi panjang "
         "mengubah perbaikan kembali menjadi konflik."),
        ("Three questions is plenty. More than that and a child starts defending rather "
         "than reflecting.",
         "Tiga pertanyaan sudah cukup. Lebih dari itu, anak mulai membela diri, bukan merenung."),
        ("Debrief one hard moment today with three short questions, no more.",
         "Bahas satu momen sulit hari ini dengan tiga pertanyaan pendek, tidak lebih."),
        ("Do my after-the-fact conversations feel like curiosity or like a trial?",
         "Apakah percakapan saya setelahnya terasa seperti rasa ingin tahu atau seperti persidangan?"),
        ("\"What was that like for you?\"",
         "\"Tadi rasanya bagaimana buat kamu?\""),
    ),
    169: d(
        ("Building emotional vocabulary at dinner",
         "Membangun kosakata emosi saat makan malam"),
        ("Emotional vocabulary grows fastest in ordinary conversation, not in crisis. The "
         "dinner table is the most reliable slot most families have.\n\n"
         "A simple round — one good thing, one hard thing — teaches children that feelings "
         "are ordinary table conversation rather than emergencies.",
         "Kosakata emosi tumbuh paling cepat dalam percakapan biasa, bukan dalam krisis. "
         "Meja makan adalah slot paling andal yang dimiliki kebanyakan keluarga.\n\n"
         "Satu putaran sederhana — satu hal baik, satu hal sulit — mengajarkan anak bahwa "
         "perasaan adalah obrolan meja makan yang wajar, bukan keadaan darurat."),
        ("Parents answering honestly is the part that makes it work. A child will not go "
         "deeper than the adults do.",
         "Orang tua yang menjawab jujur adalah bagian yang membuatnya berhasil. Anak tak "
         "akan masuk lebih dalam daripada orang dewasanya."),
        ("Run one round of high and low at a meal today, and answer honestly yourself.",
         "Jalankan satu putaran hal terbaik dan tersulit saat makan hari ini, dan jawab dengan jujur juga."),
        ("Do feelings get talked about in our house when nothing is wrong?",
         "Apakah perasaan dibicarakan di rumah kami saat tidak ada masalah?"),
        ("\"One good thing and one hard thing — I'll start.\"",
         "\"Satu hal baik dan satu hal sulit — Mama/Papa duluan.\""),
    ),
    170: d(
        ("Feelings charts and tools",
         "Tabel dan alat perasaan"),
        ("A visual chart gives a child a way to point when words are out of reach, which "
         "is exactly when they most need one.\n\n"
         "Keep it visible and low — on the fridge, by the bed — and use it yourself "
         "sometimes. A tool only parents refer to becomes a test rather than a help.",
         "Tabel visual memberi anak cara menunjuk ketika kata-kata tak terjangkau, dan itu "
         "persis saat mereka paling membutuhkannya.\n\n"
         "Simpan di tempat terlihat dan rendah — di kulkas, di dekat tempat tidur — dan "
         "kadang pakai sendiri. Alat yang hanya dirujuk orang tua berubah menjadi ujian, "
         "bukan bantuan."),
        ("Tool 6 in the toolkit — the Name-It-To-Tame-It chart — is built for exactly "
         "this, with a feelings word bank in both languages.",
         "Alat 6 dalam toolkit — tabel Namai & Tenangkan — dibuat persis untuk ini, dengan "
         "bank kata perasaan dalam dua bahasa."),
        ("Put a feelings chart somewhere your child can reach it today.",
         "Letakkan tabel perasaan di tempat yang bisa dijangkau anak hari ini."),
        ("Where would my child point, if pointing were easier than talking?",
         "Ke mana anak saya akan menunjuk, jika menunjuk lebih mudah daripada bicara?"),
        ("\"Show me which one it's closest to.\"",
         "\"Tunjukkan yang paling mirip dengan perasaanmu.\""),
    ),
    171: d(
        ("Co-regulating through touch and tone",
         "Menenangkan bersama lewat sentuhan dan nada"),
        ("Before words work, the body does. A hand on the back, a lower voice, a slower "
         "pace and matching your child's level all calm a nervous system faster than any "
         "sentence.\n\n"
         "Some children need less touch, not more, when upset. Watch which yours is — "
         "pushing closeness on a child who needs space escalates things.",
         "Sebelum kata-kata bekerja, tubuh yang bekerja. Tangan di punggung, suara yang "
         "lebih rendah, tempo yang lebih lambat, dan menyejajarkan diri dengan tinggi anak "
         "menenangkan sistem saraf lebih cepat daripada kalimat apa pun.\n\n"
         "Sebagian anak butuh lebih sedikit sentuhan, bukan lebih, saat kesal. Perhatikan "
         "anak Anda yang mana — memaksakan kedekatan pada anak yang butuh ruang justru memperparah."),
        ("Sitting down so you are lower than your child changes the whole dynamic of a "
         "difficult moment.",
         "Duduk sehingga posisi Anda lebih rendah daripada anak mengubah seluruh dinamika "
         "sebuah momen sulit."),
        ("Lower your voice and your height in the next hard moment.",
         "Turunkan suara dan tinggi badan Anda di momen sulit berikutnya."),
        ("Does my child settle faster with more closeness or with more space?",
         "Apakah anak saya lebih cepat tenang dengan lebih banyak kedekatan atau lebih banyak ruang?"),
        ("\"I'm going to sit here with you.\"",
         "\"Mama/Papa duduk di sini menemanimu.\""),
    ),
    172: d(
        ("Coaching problem solving after calm",
         "Melatih pemecahan masalah setelah tenang"),
        ("Once a child is calm, the same difficulty becomes a solvable problem rather than "
         "a storm. This is the moment to invite their thinking rather than supply yours.\n\n"
         "\"What could you try next time?\" produces a plan the child owns. A plan they "
         "own is one they might actually use.",
         "Setelah anak tenang, kesulitan yang sama berubah menjadi masalah yang bisa "
         "dipecahkan, bukan badai. Inilah saatnya mengundang pemikirannya, bukan menyodorkan pemikiran Anda.\n\n"
         "\"Lain kali kamu bisa coba apa?\" menghasilkan rencana yang dimiliki anak. Rencana "
         "yang dia miliki adalah rencana yang mungkin benar-benar dia pakai."),
        ("If they cannot think of anything, offer two options rather than one answer. "
         "Choosing still counts as ownership.",
         "Jika dia tak terpikir apa pun, tawarkan dua opsi, bukan satu jawaban. Memilih "
         "tetap terhitung sebagai kepemilikan."),
        ("Ask for your child's idea before offering yours today.",
         "Tanyakan ide anak sebelum menawarkan ide Anda hari ini."),
        ("Whose solutions does my child usually end up with?",
         "Solusi siapa yang biasanya berakhir dipakai anak saya?"),
        ("\"What could we try next time?\"",
         "\"Lain kali kita bisa coba apa?\""),
    ),
    173: d(
        ("Teaching coping choices",
         "Mengajarkan pilihan cara mengatasi"),
        ("A child with one coping strategy has no strategy — if it fails they are stuck. "
         "A short menu, built together and practised in calm, gives them somewhere to go.\n\n"
         "Move, breathe, squeeze, draw, talk, be alone for a bit. Different feelings and "
         "different children need different ones.",
         "Anak dengan satu cara mengatasi berarti tak punya cara — jika gagal, dia macet. "
         "Daftar pendek, dibuat bersama dan dilatih saat tenang, memberinya tempat untuk pergi.\n\n"
         "Bergerak, bernapas, meremas, menggambar, bicara, sendiri sebentar. Perasaan yang "
         "berbeda dan anak yang berbeda membutuhkan cara yang berbeda."),
        ("Write the menu down and put it where the child can see it. In a hard moment, "
         "nobody remembers a list that lives only in a conversation.",
         "Tuliskan daftarnya dan letakkan di tempat anak bisa melihatnya. Di momen sulit, "
         "tak ada yang ingat daftar yang hanya hidup dalam percakapan."),
        ("Build a short coping menu with your child today, in their words.",
         "Susun daftar pendek cara mengatasi bersama anak hari ini, dengan kata-katanya."),
        ("What does my child currently do when a feeling gets big?",
         "Apa yang biasanya anak lakukan saat perasaannya membesar?"),
        ("\"Which one do you want to try — move, breathe, or squeeze?\"",
         "\"Mau coba yang mana — gerak, tarik napas, atau meremas?\""),
    ),
    174: d(
        ("Teaching self-talk",
         "Mengajarkan bicara pada diri sendiri"),
        ("Children internalise the voice they hear most. The way you speak to your child "
         "in difficulty becomes, over years, the way they speak to themselves in "
         "difficulty.\n\n"
         "This is worth pausing on. Your tone during their failures is being installed as "
         "their inner voice during future ones.",
         "Anak menginternalisasi suara yang paling sering mereka dengar. Cara Anda bicara "
         "kepada anak saat kesulitan menjadi, setelah bertahun-tahun, cara dia bicara "
         "kepada dirinya sendiri saat kesulitan.\n\n"
         "Ini layak direnungkan sejenak. Nada Anda saat dia gagal sedang dipasang sebagai "
         "suara batinnya saat gagal di masa depan."),
        ("Teach the phrase out loud: \"this is hard and I can do hard things.\" Said "
         "enough times by you, it eventually gets said by them.",
         "Ajarkan kalimatnya dengan suara: \"ini sulit dan aku bisa melakukan hal sulit.\" "
         "Cukup sering Anda ucapkan, akhirnya dia yang mengucapkannya."),
        ("Say one encouraging sentence out loud today that you would want your child to "
         "say to themselves.",
         "Ucapkan satu kalimat menyemangati hari ini yang Anda ingin anak katakan pada dirinya sendiri."),
        ("If my voice became my child's inner voice, what would they be hearing?",
         "Jika suara saya menjadi suara batin anak, apa yang akan dia dengar?"),
        ("\"This is hard, and you can do hard things.\"",
         "\"Ini sulit, dan kamu bisa melakukan hal yang sulit.\""),
    ),
    175: d(
        ("Teaching resilience",
         "Mengajarkan ketangguhan"),
        ("Resilience is not toughness and it is not the absence of distress. It is the "
         "capacity to be knocked down and to recover — and recovery is learned by "
         "recovering, repeatedly, with support.\n\n"
         "A child protected from all difficulty gets no practice. A child left alone in "
         "difficulty gets overwhelmed. Resilience grows in the space between.",
         "Ketangguhan bukan kekerasan hati dan bukan tiadanya kesusahan. Ia kemampuan "
         "untuk terjatuh dan bangkit — dan bangkit dipelajari dengan bangkit, berulang "
         "kali, dengan dukungan.\n\n"
         "Anak yang dilindungi dari semua kesulitan tak dapat latihan. Anak yang "
         "ditinggalkan dalam kesulitan menjadi kewalahan. Ketangguhan tumbuh di ruang di antaranya."),
        ("Your steadiness is what makes their difficulty survivable. That is the support "
         "half of the equation, and it is not optional.",
         "Ketenangan Anda yang membuat kesulitannya bisa dilalui. Itulah separuh dukungan "
         "dari persamaan ini, dan ia bukan pilihan."),
        ("Let one difficulty stand today while staying visibly beside your child.",
         "Biarkan satu kesulitan berdiri hari ini sambil Anda tetap terlihat berada di samping anak."),
        ("Am I building resilience, or just removing obstacles?",
         "Apakah saya membangun ketangguhan, atau hanya menyingkirkan hambatan?"),
        ("\"You've come back from hard things before.\"",
         "\"Kamu pernah bangkit dari hal sulit sebelumnya.\""),
    ),
    176: d(
        ("Helping children face small challenges",
         "Membantu anak menghadapi tantangan kecil"),
        ("Confidence is built from evidence, and evidence comes from doing slightly hard "
         "things and surviving them. Small, frequent challenges beat rare big ones.\n\n"
         "Ordering their own food, carrying something breakable, asking a shopkeeper a "
         "question — each is a small deposit into a child's sense of their own capability.",
         "Kepercayaan diri dibangun dari bukti, dan bukti datang dari melakukan hal yang "
         "agak sulit lalu selamat melewatinya. Tantangan kecil yang sering mengalahkan "
         "tantangan besar yang jarang.\n\n"
         "Memesan makanannya sendiri, membawa sesuatu yang mudah pecah, bertanya kepada "
         "penjual — masing-masing adalah setoran kecil ke rasa mampu dalam diri anak."),
        ("Doing it for them is faster today and costs a little of their confidence every "
         "single time.",
         "Melakukannya untuk dia lebih cepat hari ini, dan setiap kali menghabiskan sedikit "
         "kepercayaan dirinya."),
        ("Let your child do one slightly hard thing themselves today.",
         "Biarkan anak melakukan satu hal yang agak sulit sendiri hari ini."),
        ("What am I still doing for my child that they could now do themselves?",
         "Apa yang masih saya lakukan untuk anak, yang sebenarnya kini bisa dia lakukan sendiri?"),
        ("\"You ask them. I'll be right here.\"",
         "\"Kamu yang tanya, ya. Mama/Papa di sini.\""),
    ),
    177: d(
        ("Avoiding overprotection",
         "Menghindari perlindungan berlebihan"),
        ("Overprotection is love pointed slightly wrong. It removes the difficulty and, "
         "with it, the message that the child could have handled it.\n\n"
         "The signal to watch for is your own anxiety driving the decision. If you are "
         "stepping in to settle your own nerves rather than to meet a real risk, that is "
         "the moment to pause.",
         "Perlindungan berlebihan adalah kasih sayang yang arahnya sedikit meleset. Ia "
         "menghapus kesulitannya, dan bersamanya pesan bahwa anak sebenarnya sanggup.\n\n"
         "Sinyal yang perlu diperhatikan adalah kecemasan Anda sendiri yang menggerakkan "
         "keputusan. Jika Anda turun tangan untuk menenangkan saraf Anda sendiri, bukan "
         "menghadapi risiko yang nyata, itulah saat untuk berhenti sejenak."),
        ("\"Be careful\" said fifty times a day teaches a child that the world is mostly "
         "dangerous and they are mostly incapable.",
         "\"Hati-hati\" yang diucapkan lima puluh kali sehari mengajarkan anak bahwa dunia "
         "sebagian besar berbahaya dan dirinya sebagian besar tidak mampu."),
        ("Notice one moment today when you protect out of your own anxiety, and hold back.",
         "Sadari satu momen hari ini saat Anda melindungi karena kecemasan Anda sendiri, dan tahan diri."),
        ("Whose discomfort am I actually preventing?",
         "Ketidaknyamanan siapa yang sebenarnya sedang saya cegah?"),
        ("\"I think you've got this.\"",
         "\"Mama/Papa rasa kamu bisa.\""),
    ),
    178: d(
        ("Encouraging bravery gradually",
         "Menumbuhkan keberanian secara bertahap"),
        ("Bravery is built in steps small enough to succeed at. Pushing a frightened child "
         "into the deep end teaches fear, not courage.\n\n"
         "Break the feared thing into pieces and let them win at each one. Look at it, "
         "stand near it, touch it, try it — each step at their pace, with company.",
         "Keberanian dibangun dalam langkah yang cukup kecil untuk berhasil. Mendorong anak "
         "yang ketakutan ke bagian terdalam mengajarkan rasa takut, bukan keberanian.\n\n"
         "Pecah hal yang ditakuti menjadi bagian-bagian dan biarkan dia menang di setiap "
         "bagian. Melihatnya, berdiri di dekatnya, menyentuhnya, mencobanya — setiap "
         "langkah sesuai temponya, dengan ditemani."),
        ("A child who takes one step and succeeds will usually offer to take the next one "
         "themselves. That offer is the goal.",
         "Anak yang mengambil satu langkah dan berhasil biasanya menawarkan diri mengambil "
         "langkah berikutnya. Tawaran itulah tujuannya."),
        ("Break one feared thing into a first tiny step today.",
         "Pecah satu hal yang ditakuti menjadi satu langkah kecil pertama hari ini."),
        ("Am I asking for a leap where a step would do?",
         "Apakah saya meminta lompatan padahal satu langkah sudah cukup?"),
        ("\"Just look at it with me. That's all for now.\"",
         "\"Lihat saja dulu sama Mama/Papa. Itu dulu.\""),
    ),
    179: d(
        ("Repairing hurt feelings among siblings",
         "Memperbaiki perasaan yang terluka antar saudara"),
        ("A forced apology between siblings teaches performance. What teaches repair is "
         "helping the one who caused harm understand its effect, then do something real "
         "about it.\n\n"
         "The hurt child also needs their feeling acknowledged by you — not only an "
         "apology extracted from their sibling.",
         "Permintaan maaf yang dipaksakan antar saudara mengajarkan sandiwara. Yang "
         "mengajarkan perbaikan adalah membantu yang menyakiti memahami dampaknya, lalu "
         "melakukan sesuatu yang nyata untuk itu.\n\n"
         "Anak yang tersakiti juga butuh perasaannya diakui oleh Anda — bukan hanya "
         "permintaan maaf yang dipaksa keluar dari saudaranya."),
        ("\"What could you do to make her feel better?\" produces repair. \"Say sorry\" "
         "produces the word and nothing behind it.",
         "\"Apa yang bisa kamu lakukan supaya dia merasa lebih baik?\" menghasilkan "
         "perbaikan. \"Minta maaf\" menghasilkan katanya dan tak ada apa-apa di baliknya."),
        ("Guide one real repair between siblings today instead of an apology.",
         "Bimbing satu perbaikan yang nyata antar saudara hari ini, bukan permintaan maaf."),
        ("Do apologies in our house mean anything, or just end the trouble?",
         "Apakah permintaan maaf di rumah kami berarti sesuatu, atau hanya mengakhiri masalah?"),
        ("\"What would help her feel better?\"",
         "\"Apa yang bisa membuat dia merasa lebih baik?\""),
    ),
    180: d(
        ("Weekly reflection",
         "Refleksi mingguan"),
        ("This chapter rests on one order of operations: accept the feeling, then guide "
         "the action. Everything else is technique in service of that.\n\n"
         "Look back over the month and check which feelings you find easiest to sit with "
         "and which you rush. Most parents have one that is genuinely hard — usually the "
         "one they were not allowed to have themselves.",
         "Bab ini bertumpu pada satu urutan: terima perasaannya, lalu arahkan tindakannya. "
         "Selebihnya adalah teknik yang melayani hal itu.\n\n"
         "Tengok kembali bulan ini dan periksa perasaan mana yang paling mudah Anda temani "
         "dan mana yang Anda buru-buru. Kebanyakan orang tua punya satu yang sungguh sulit "
         "— biasanya perasaan yang dulu tidak boleh mereka miliki sendiri."),
        ("The feeling you find hardest in your child is very often the one nobody made "
         "room for in you.",
         "Perasaan yang paling sulit Anda hadapi pada anak sering kali adalah perasaan yang "
         "dulu tak ada yang memberi ruang untuknya dalam diri Anda."),
        ("Name the feeling you find hardest to sit with, and where you learned that.",
         "Sebutkan perasaan yang paling sulit Anda temani, dan di mana Anda mempelajarinya."),
        ("Which of my child's feelings do I rush the most?",
         "Perasaan anak yang mana yang paling saya buru-buru?"),
        ("\"All feelings are allowed here.\"",
         "\"Semua perasaan boleh ada di sini.\""),
    ),
    181: d(
        ("Review and practice day",
         "Hari peninjauan dan latihan"),
        ("No new material today. Pick the one emotion-coaching move from this month that "
         "would change the most in your home, and practise only that.\n\n"
         "Most parents already know more than they use. The gap between knowing and doing "
         "closes through repetition of a single small thing, not through more reading.",
         "Tidak ada materi baru hari ini. Pilih satu langkah pendampingan emosi dari bulan "
         "ini yang paling akan mengubah rumah Anda, dan latih itu saja.\n\n"
         "Kebanyakan orang tua sudah tahu lebih banyak daripada yang mereka pakai. Jarak "
         "antara tahu dan melakukan tertutup lewat pengulangan satu hal kecil, bukan lewat "
         "membaca lebih banyak."),
        ("One move, practised for a week, beats thirty moves read once. Choose the one "
         "that fits the moment your family struggles with most.",
         "Satu langkah, dilatih seminggu, mengalahkan tiga puluh langkah yang dibaca sekali. "
         "Pilih yang paling cocok dengan momen tersulit keluarga Anda."),
        ("Choose one move from this month and use only that one, all week.",
         "Pilih satu langkah dari bulan ini dan pakai hanya itu, sepanjang minggu."),
        ("Which single change would matter most in our home right now?",
         "Satu perubahan mana yang paling berarti di rumah kami saat ini?"),
        ("\"One thing, done often. That's the whole method.\"",
         "\"Satu hal, sering dilakukan. Itu seluruh metodenya.\""),
    ),
}
