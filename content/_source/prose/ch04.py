# Chapter 4 — Communication (days 92-121)
#
# Grounded in the founder's guidebook chapter 4 ("Empathy first, then
# redirection") and toolkit tool 4 (Empathy-First Sentence Cards).
#
# Through-line: a child whose feelings are named settles; a child whose feelings
# are dismissed escalates.

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
    92: d(
        ("Listening without interrupting",
         "Mendengarkan tanpa memotong"),
        ("Most parents listen in order to reply. Children can tell, and it changes what "
         "they are willing to bring you.\n\n"
         "Listening without interrupting is harder than it sounds, because children take "
         "a long time to reach the point and the temptation to speed them up is constant. "
         "But the pause you allow is what teaches a child that talking to you is worth "
         "the effort.",
         "Kebanyakan orang tua mendengarkan untuk menjawab. Anak bisa merasakannya, dan itu "
         "mengubah apa yang mereka mau bawa kepada Anda.\n\n"
         "Mendengarkan tanpa memotong lebih sulit daripada kedengarannya, karena anak butuh "
         "waktu lama untuk sampai ke inti dan godaan untuk mempercepatnya terus-menerus ada. "
         "Tapi jeda yang Anda izinkan itulah yang mengajarkan anak bahwa berbicara dengan "
         "Anda sepadan dengan usahanya."),
        ("Try counting three seconds after your child stops speaking before you reply. "
         "They will often add the most important part in those three seconds.",
         "Coba hitung tiga detik setelah anak berhenti bicara sebelum Anda menjawab. Mereka "
         "sering menambahkan bagian terpentingnya di tiga detik itu."),
        ("Let your child finish completely once today, with three seconds of silence after.",
         "Biarkan anak menyelesaikan bicaranya sepenuhnya sekali hari ini, dengan tiga detik "
         "hening setelahnya."),
        ("How often do I finish my child's sentences for them?",
         "Seberapa sering saya menyelesaikan kalimat anak untuknya?"),
        ("\"Take your time. I'm listening.\"",
         "\"Pelan-pelan saja. Mama/Papa dengarkan.\""),
    ),
    93: d(
        ("Reflective listening",
         "Mendengarkan reflektif"),
        ("Reflective listening means saying back what you heard before responding to it. "
         "It sounds mechanical written down and works remarkably well in practice.\n\n"
         "It does two things: it proves you were listening, and it lets your child correct "
         "you — which means you end up responding to what actually happened rather than "
         "what you assumed.",
         "Mendengarkan reflektif berarti mengulang kembali apa yang Anda dengar sebelum "
         "menanggapinya. Kedengarannya mekanis kalau ditulis, dan sangat berhasil dalam praktik.\n\n"
         "Ia melakukan dua hal: membuktikan Anda mendengarkan, dan memberi anak kesempatan "
         "membetulkan Anda — artinya Anda akhirnya menanggapi apa yang sungguh terjadi, "
         "bukan apa yang Anda kira."),
        ("\"So Adi took the ball and nobody let you play?\" Half the time the child says "
         "\"no, actually…\" and tells you the real thing.",
         "\"Jadi Adi mengambil bolanya dan tak ada yang mengajakmu main?\" Separuh waktu anak "
         "menjawab \"bukan, sebenarnya…\" lalu menceritakan yang sesungguhnya."),
        ("Say back what you heard once today before giving any response.",
         "Ulangi apa yang Anda dengar sekali hari ini sebelum memberi tanggapan apa pun."),
        ("How often do I respond to what I assumed rather than what was said?",
         "Seberapa sering saya menanggapi apa yang saya kira, bukan apa yang dikatakan?"),
        ("\"Let me check I've got this right…\"",
         "\"Coba Mama/Papa pastikan dulu, ya…\""),
    ),
    94: d(
        ("Validating feelings",
         "Mengakui perasaan"),
        ("Validation is not agreement. You can fully accept that a feeling is real while "
         "holding a limit completely unchanged — and doing both at once is the core skill "
         "of this chapter.\n\n"
         "Most escalation happens because a child feels their experience was denied. "
         "Denying the feeling almost always makes the behaviour louder and longer.",
         "Mengakui bukan menyetujui. Anda bisa sepenuhnya menerima bahwa suatu perasaan itu "
         "nyata sambil memegang batas yang sama sekali tidak berubah — dan melakukan "
         "keduanya sekaligus adalah keterampilan inti bab ini.\n\n"
         "Sebagian besar eskalasi terjadi karena anak merasa pengalamannya disangkal. "
         "Menyangkal perasaan hampir selalu membuat perilakunya lebih keras dan lebih lama."),
        ("\"You're not sad, it's only a toy\" adds a second injury to the first. \"You're "
         "really sad about that toy\" ends the argument about whether the feeling counts.",
         "\"Kamu tidak sedih, itu cuma mainan\" menambah luka kedua di atas yang pertama. "
         "\"Kamu benar-benar sedih soal mainan itu\" mengakhiri perdebatan tentang apakah "
         "perasaannya berarti."),
        ("Validate one feeling today without adding \"but\" to the end of the sentence.",
         "Akui satu perasaan hari ini tanpa menambahkan \"tapi\" di ujung kalimat."),
        ("Do I accidentally argue with my child about whether their feelings are real?",
         "Apakah saya tanpa sadar berdebat dengan anak tentang apakah perasaannya nyata?"),
        ("\"That really upset you. I get it.\"",
         "\"Itu benar-benar membuatmu kesal. Mama/Papa mengerti.\""),
    ),
    95: d(
        ("Empathy statements",
         "Kalimat empati"),
        ("An empathy statement has a simple shape: name the feeling, name the cause, stop. "
         "\"You're disappointed because we had to leave early.\"\n\n"
         "The stopping is the hard part. Most parents attach a lesson immediately, and the "
         "lesson cancels the empathy. Let the empathy stand alone for a few seconds before "
         "anything else arrives.",
         "Kalimat empati punya bentuk sederhana: sebut perasaannya, sebut penyebabnya, "
         "berhenti. \"Kamu kecewa karena kita harus pulang lebih awal.\"\n\n"
         "Berhentinya itu bagian yang sulit. Kebanyakan orang tua langsung menempelkan "
         "pelajaran, dan pelajaran itu membatalkan empatinya. Biarkan empatinya berdiri "
         "sendiri beberapa detik sebelum apa pun yang lain datang."),
        ("\"You're sad we left, AND next time we'll…\" — the \"and next time\" is where the "
         "empathy usually dies. Say the first half. Wait.",
         "\"Kamu sedih karena kita pulang, DAN lain kali kita…\" — di \"dan lain kali\" itulah "
         "empatinya biasanya mati. Ucapkan separuh pertamanya. Tunggu."),
        ("Say one empathy statement today and stay silent for five seconds afterwards.",
         "Ucapkan satu kalimat empati hari ini dan diamlah lima detik setelahnya."),
        ("Can I say the empathy without immediately attaching the lesson?",
         "Bisakah saya mengucapkan empatinya tanpa langsung menempelkan pelajaran?"),
        ("\"You're disappointed. That makes sense.\"",
         "\"Kamu kecewa. Wajar kok.\""),
    ),
    96: d(
        ("Saying less, connecting more",
         "Bicara lebih sedikit, terhubung lebih banyak"),
        ("Under pressure, most parents talk more. Children under pressure process less. "
         "The two facts collide, and the result is a lot of words that never arrive.\n\n"
         "Fewer words with more presence beats more words with less. In a difficult "
         "moment, one short sentence and a hand on the shoulder does more than a paragraph.",
         "Di bawah tekanan, kebanyakan orang tua bicara lebih banyak. Anak di bawah tekanan "
         "memproses lebih sedikit. Kedua fakta itu bertabrakan, dan hasilnya banyak kata "
         "yang tak pernah sampai.\n\n"
         "Kata yang lebih sedikit dengan kehadiran yang lebih penuh mengalahkan kata yang "
         "lebih banyak dengan kehadiran yang lebih tipis. Di momen sulit, satu kalimat "
         "pendek dan tangan di bahu lebih berguna daripada satu paragraf."),
        ("Count the sentences in your next correction. If there are more than three, the "
         "child stopped listening somewhere around the second.",
         "Hitung jumlah kalimat dalam teguran Anda berikutnya. Jika lebih dari tiga, anak "
         "berhenti mendengarkan di sekitar kalimat kedua."),
        ("Make one correction today in a single sentence. Nothing more.",
         "Sampaikan satu teguran hari ini dalam satu kalimat. Tidak lebih."),
        ("How many of my words in a hard moment are actually landing?",
         "Berapa banyak kata saya di momen sulit yang sebenarnya sampai?"),
        ("\"One thing: shoes on, please.\"",
         "\"Satu hal saja: pakai sepatu, ya.\""),
    ),
    97: d(
        ("Describing instead of accusing",
         "Menggambarkan, bukan menuduh"),
        ("Describing what you see puts the problem in the room. Accusing puts the child on "
         "trial, and a child on trial defends rather than fixes.\n\n"
         "\"There's milk on the floor\" and \"you spilled the milk again\" describe the same "
         "event and produce completely different next thirty seconds.",
         "Menggambarkan apa yang Anda lihat menaruh masalahnya di ruangan. Menuduh menaruh "
         "anaknya di kursi terdakwa, dan anak yang diadili akan membela diri, bukan membereskan.\n\n"
         "\"Ada susu di lantai\" dan \"kamu tumpahkan susu lagi\" menggambarkan peristiwa yang "
         "sama dan menghasilkan tiga puluh detik berikutnya yang sama sekali berbeda."),
        ("Describing also leaves room for the child to volunteer the solution, which is a "
         "far better outcome than being told it.",
         "Menggambarkan juga menyisakan ruang bagi anak untuk menawarkan solusinya sendiri — "
         "hasil yang jauh lebih baik daripada diberi tahu."),
        ("Describe one problem today without using the word \"you\".",
         "Gambarkan satu masalah hari ini tanpa memakai kata \"kamu\"."),
        ("Do my corrections describe the problem, or prosecute the child?",
         "Apakah teguran saya menggambarkan masalahnya, atau mengadili anaknya?"),
        ("\"There's water on the floor.\"",
         "\"Ada air di lantai.\""),
    ),
    98: d(
        ("Curiosity over assumptions",
         "Rasa ingin tahu daripada asumsi"),
        ("You usually know what happened. You usually do not know why, and the why is "
         "where anything useful lives.\n\n"
         "A genuinely curious question — asked without a verdict already loaded — gets "
         "information that an accusation never will. Children can tell the difference "
         "between a question and a trap immediately.",
         "Anda biasanya tahu apa yang terjadi. Anda biasanya tidak tahu mengapa, dan di "
         "\"mengapa\" itulah segala yang berguna berada.\n\n"
         "Pertanyaan yang benar-benar penasaran — diajukan tanpa putusan yang sudah dimuat — "
         "mendapatkan informasi yang tak akan pernah didapat tuduhan. Anak bisa langsung "
         "membedakan pertanyaan dari jebakan."),
        ("\"Why did you do that?\" said sharply is not a question. \"Help me understand what "
         "was going on\" usually is.",
         "\"Kenapa kamu lakukan itu?\" yang diucapkan tajam bukan pertanyaan. \"Bantu Mama/Papa "
         "mengerti apa yang sedang terjadi\" biasanya iya."),
        ("Ask one real question today about something you already think you understand.",
         "Ajukan satu pertanyaan yang sungguhan hari ini tentang hal yang Anda kira sudah Anda pahami."),
        ("When I ask my child why, am I asking or accusing?",
         "Saat saya bertanya mengapa kepada anak, apakah saya bertanya atau menuduh?"),
        ("\"Help me understand what happened.\"",
         "\"Bantu Mama/Papa mengerti apa yang terjadi.\""),
    ),
    99: d(
        ("Open-ended questions",
         "Pertanyaan terbuka"),
        ("\"How was school?\" reliably produces \"fine.\" It is a closed question wearing an "
         "open coat, and it asks a child to summarise seven hours in one word.\n\n"
         "Specific, concrete questions work far better: what made you laugh, who did you "
         "sit with, what was the hardest bit. They give a child somewhere to start.",
         "\"Bagaimana sekolahnya?\" hampir selalu menghasilkan \"biasa aja.\" Ia pertanyaan "
         "tertutup yang mengenakan mantel terbuka, dan meminta anak meringkas tujuh jam "
         "dalam satu kata.\n\n"
         "Pertanyaan yang spesifik dan konkret jauh lebih ampuh: apa yang membuatmu tertawa, "
         "kamu duduk dengan siapa, bagian tersulitnya apa. Semuanya memberi anak titik mulai."),
        ("\"What was the funniest thing that happened today?\" gets a real answer roughly "
         "ten times more often than \"how was your day?\"",
         "\"Apa hal paling lucu yang terjadi hari ini?\" mendapat jawaban sungguhan kira-kira "
         "sepuluh kali lebih sering daripada \"bagaimana harimu?\""),
        ("Replace your usual question today with one specific, concrete one.",
         "Ganti pertanyaan biasa Anda hari ini dengan satu pertanyaan yang spesifik dan konkret."),
        ("What question do I ask every day that never gets a real answer?",
         "Pertanyaan apa yang saya ajukan setiap hari yang tak pernah dapat jawaban sungguhan?"),
        ("\"What made you laugh today?\"",
         "\"Apa yang membuatmu tertawa hari ini?\""),
    ),
    100: d(
        ("Coaching instead of lecturing",
         "Melatih, bukan menceramahi"),
        ("A lecture delivers your conclusion. Coaching helps a child reach their own, "
         "which is the version they remember and can use again.\n\n"
         "Lectures feel productive because you get to say everything you wanted to say. "
         "They are almost entirely unabsorbed after the first thirty seconds.",
         "Ceramah menyampaikan kesimpulan Anda. Melatih membantu anak mencapai kesimpulannya "
         "sendiri — versi yang dia ingat dan bisa dipakai lagi.\n\n"
         "Ceramah terasa produktif karena Anda bisa mengatakan semua yang ingin Anda katakan. "
         "Ia hampir sepenuhnya tidak terserap setelah tiga puluh detik pertama."),
        ("\"What do you think you could do differently?\" takes longer than telling them and "
         "produces something that survives the week.",
         "\"Menurutmu apa yang bisa kamu lakukan berbeda?\" butuh waktu lebih lama daripada "
         "memberi tahu, dan menghasilkan sesuatu yang bertahan seminggu."),
        ("Ask instead of telling once today, even though telling would be faster.",
         "Bertanyalah alih-alih memberi tahu sekali hari ini, meski memberi tahu lebih cepat."),
        ("How long are my lectures, and how much of them lands?",
         "Berapa panjang ceramah saya, dan berapa banyak yang sampai?"),
        ("\"What do you think would work better next time?\"",
         "\"Menurutmu apa yang lebih berhasil lain kali?\""),
    ),
    101: d(
        ("Giving clear instructions",
         "Memberi instruksi yang jelas"),
        ("Many instructions fail on delivery rather than on willingness. Vague, "
         "multi-part, shouted-from-another-room instructions are hard to follow even for "
         "a cooperative child.\n\n"
         "Clear means: close enough to be heard, one thing, stated as an action rather "
         "than a complaint, with a clear moment it applies to.",
         "Banyak instruksi gagal pada cara penyampaiannya, bukan pada kemauan anak. "
         "Instruksi yang kabur, bertingkat, dan diteriakkan dari ruangan lain sulit diikuti "
         "bahkan oleh anak yang kooperatif.\n\n"
         "Jelas berarti: cukup dekat untuk terdengar, satu hal saja, dinyatakan sebagai "
         "tindakan bukan keluhan, dengan waktu penerapan yang jelas."),
        ("\"Can you please be good?\" is not an instruction. \"Put your shoes by the door\" "
         "is one, and a child can actually comply with it.",
         "\"Tolong jadi anak baik, ya?\" bukan instruksi. \"Taruh sepatumu di dekat pintu\" "
         "adalah instruksi, dan anak benar-benar bisa menurutinya."),
        ("Rewrite one vague request today into a concrete action.",
         "Tulis ulang satu permintaan yang kabur hari ini menjadi tindakan yang konkret."),
        ("Are my instructions actually followable as stated?",
         "Apakah instruksi saya benar-benar bisa diikuti sebagaimana diucapkan?"),
        ("\"Shoes by the door, please.\"",
         "\"Sepatu di dekat pintu, ya.\""),
    ),
    102: d(
        ("One-step directions for young kids",
         "Instruksi satu langkah untuk anak kecil"),
        ("Young children hold very little in working memory. A four-part instruction is "
         "not disobeyed so much as lost — usually somewhere around part two.\n\n"
         "One step, completed, then the next. It feels slower and is usually faster, "
         "because nothing has to be repeated.",
         "Anak kecil menampung sangat sedikit dalam memori kerja. Instruksi empat bagian "
         "bukan dilanggar, melainkan hilang — biasanya di sekitar bagian kedua.\n\n"
         "Satu langkah, selesaikan, lalu berikutnya. Terasa lebih lambat dan biasanya lebih "
         "cepat, karena tak ada yang perlu diulang."),
        ("\"Get your bag\" — done — \"now your shoes\" gets a child out of the house faster "
         "than the full list delivered at once.",
         "\"Ambil tasmu\" — selesai — \"sekarang sepatumu\" membuat anak keluar rumah lebih "
         "cepat daripada seluruh daftar yang disampaikan sekaligus."),
        ("Give strictly one instruction at a time to your youngest child today.",
         "Beri satu instruksi saja pada satu waktu kepada anak terkecil Anda hari ini."),
        ("How many steps do I usually give at once?",
         "Berapa langkah yang biasanya saya berikan sekaligus?"),
        ("\"First that. Then I'll tell you the next one.\"",
         "\"Itu dulu. Nanti Mama/Papa kasih tahu berikutnya.\""),
    ),
    103: d(
        ("Eye contact and physical proximity",
         "Kontak mata dan kedekatan fisik"),
        ("Instructions shouted between rooms have a very low success rate, and the failure "
         "is usually blamed on the child.\n\n"
         "Closing the distance, getting to eye level and waiting for their attention "
         "before speaking costs about ten seconds and roughly doubles the chance of being "
         "heard the first time.",
         "Instruksi yang diteriakkan antar ruangan punya tingkat keberhasilan sangat rendah, "
         "dan kegagalannya biasanya ditimpakan pada anak.\n\n"
         "Mendekat, sejajar mata, dan menunggu perhatiannya sebelum bicara memakan sekitar "
         "sepuluh detik dan kira-kira menggandakan peluang didengar pada percobaan pertama."),
        ("Walking into the room to speak is not extra effort. It replaces the three "
         "repetitions you were about to shout.",
         "Berjalan masuk ke ruangan untuk bicara bukan usaha tambahan. Ia menggantikan tiga "
         "pengulangan yang tadinya akan Anda teriakkan."),
        ("Deliver every instruction today from inside the same room, at eye level.",
         "Sampaikan setiap instruksi hari ini dari dalam ruangan yang sama, sejajar mata."),
        ("How many of my instructions are shouted from somewhere else?",
         "Berapa banyak instruksi saya yang diteriakkan dari tempat lain?"),
        ("\"Look at me a second — then I'll ask.\"",
         "\"Lihat Mama/Papa sebentar — baru Mama/Papa minta.\""),
    ),
    104: d(
        ("Connection before commands",
         "Terhubung sebelum memerintah"),
        ("A command that arrives cold is resisted more than the same command arriving "
         "after three seconds of contact. This is not manipulation; it is how "
         "cooperation works between people.\n\n"
         "Notice what they are doing, acknowledge it, then ask. The acknowledgement is "
         "what stops the request feeling like an interruption of their life.",
         "Perintah yang datang dingin lebih dilawan daripada perintah yang sama yang datang "
         "setelah tiga detik kehadiran. Ini bukan manipulasi; begini cara kerja sama antar "
         "manusia berlangsung.\n\n"
         "Sadari apa yang sedang dia lakukan, akui, lalu minta. Pengakuan itulah yang "
         "membuat permintaan Anda tak terasa seperti gangguan atas hidupnya."),
        ("\"That's a big tower — and it's bath time in five minutes\" lands very differently "
         "from \"bath, now.\"",
         "\"Wah menaranya tinggi — dan lima menit lagi waktunya mandi\" terasa sangat berbeda "
         "dari \"mandi, sekarang.\""),
        ("Acknowledge what your child is doing before every request today.",
         "Akui apa yang sedang anak lakukan sebelum setiap permintaan hari ini."),
        ("Do my requests arrive as interruptions?",
         "Apakah permintaan saya datang sebagai gangguan?"),
        ("\"That looks good — and in five minutes we need to stop.\"",
         "\"Bagus, ya — dan lima menit lagi kita perlu berhenti.\""),
    ),
    105: d(
        ("Avoiding sarcasm",
         "Menghindari sindiran"),
        ("Sarcasm requires the listener to hold two meanings at once and choose the "
         "opposite one. Young children cannot do this, so they receive the literal "
         "insult without the joke.\n\n"
         "Older children understand it perfectly, which is worse — they hear contempt "
         "dressed as humour, and contempt is corrosive to a relationship in a way ordinary "
         "anger is not.",
         "Sindiran menuntut pendengar menahan dua makna sekaligus dan memilih yang "
         "berlawanan. Anak kecil belum bisa, jadi mereka menerima hinaan harfiahnya tanpa "
         "leluconnya.\n\n"
         "Anak yang lebih besar memahaminya sempurna, dan itu lebih buruk — mereka mendengar "
         "penghinaan yang berbusana humor, dan penghinaan merusak hubungan dengan cara yang "
         "tak dilakukan kemarahan biasa."),
        ("\"Oh, brilliant, well done\" said flatly after a spill teaches a child that you "
         "will mock them when they fail.",
         "\"Oh, hebat sekali\" yang diucapkan datar setelah sesuatu tumpah mengajarkan anak "
         "bahwa Anda akan mengejeknya saat dia gagal."),
        ("Catch one sarcastic sentence today before it leaves your mouth.",
         "Tangkap satu kalimat sindiran hari ini sebelum keluar dari mulut Anda."),
        ("Do I use humour at my child's expense when I am frustrated?",
         "Apakah saya memakai humor dengan mengorbankan anak saat saya kesal?"),
        ("\"Let me say that again, straight.\"",
         "\"Mama/Papa ulangi lagi, dengan lurus.\""),
    ),
    106: d(
        ("Avoiding labels like lazy or naughty",
         "Menghindari label seperti malas atau nakal"),
        ("Labels are efficient and they stick. A child called lazy often enough stops "
         "trying, because effort now threatens an identity that has already been assigned.\n\n"
         "Labels also travel: siblings adopt them, relatives repeat them, and eventually "
         "the child says it about themselves. What was once a description becomes a "
         "self-fulfilling forecast.",
         "Label itu efisien dan lengket. Anak yang cukup sering disebut malas berhenti "
         "berusaha, karena usaha kini mengancam jati diri yang sudah terlanjur ditetapkan.\n\n"
         "Label juga menular: saudara ikut memakainya, kerabat mengulanginya, dan akhirnya "
         "anak mengatakannya tentang dirinya sendiri. Yang tadinya gambaran menjadi ramalan "
         "yang mewujudkan diri."),
        ("\"He's the difficult one\" said in front of a child often enough becomes a role "
         "the child settles into, because roles are easier than uncertainty.",
         "\"Dia yang susah diatur\" yang diucapkan di depan anak cukup sering menjadi peran "
         "yang dia tempati, karena peran lebih mudah daripada ketidakpastian."),
        ("Catch one label today — even a joking one — and replace it with a description.",
         "Tangkap satu label hari ini — bahkan yang bercanda — dan ganti dengan gambaran."),
        ("What labels does my child hear about themselves in this house?",
         "Label apa yang anak dengar tentang dirinya di rumah ini?"),
        ("\"That's not who you are. That's what happened.\"",
         "\"Itu bukan dirimu. Itu yang terjadi.\""),
    ),
    107: d(
        ("Talking about behavior, not identity",
         "Bicara tentang perilaku, bukan jati diri"),
        ("This is the practical version of yesterday. Every correction can be aimed at "
         "what was done or at who the child is, and the two produce different children "
         "over years.\n\n"
         "Behaviour is changeable, which makes it a useful thing to name. Identity is not, "
         "which makes naming it a dead end.",
         "Ini versi praktis dari kemarin. Setiap teguran bisa diarahkan pada apa yang "
         "dilakukan atau pada siapa anaknya, dan keduanya menghasilkan anak yang berbeda "
         "setelah bertahun-tahun.\n\n"
         "Perilaku bisa diubah, itulah yang membuatnya berguna untuk disebut. Jati diri "
         "tidak, dan itulah yang membuat menyebutnya jadi jalan buntu."),
        ("\"That was unkind\" gives a child something to do differently. \"You're unkind\" "
         "gives them something to be.",
         "\"Tadi itu tidak baik\" memberi anak sesuatu untuk dilakukan berbeda. \"Kamu tidak "
         "baik\" memberinya sesuatu untuk menjadi."),
        ("Aim every correction today at the action. Check each one before you speak.",
         "Arahkan setiap teguran hari ini pada tindakannya. Periksa satu per satu sebelum bicara."),
        ("Do my corrections describe what happened, or who my child is?",
         "Apakah teguran saya menggambarkan apa yang terjadi, atau siapa anak saya?"),
        ("\"That was unkind — and you're not an unkind person.\"",
         "\"Tadi itu tidak baik — dan kamu bukan orang yang tidak baik.\""),
    ),
    108: d(
        ("Timing difficult conversations",
         "Memilih waktu untuk percakapan sulit"),
        ("The right conversation at the wrong moment fails. Nobody absorbs anything while "
         "flooded, hungry, tired, or in front of an audience.\n\n"
         "Most important conversations go better later, sideways, and in motion — in the "
         "car, on a walk, at bedtime — where there is no eye contact to survive and no "
         "audience to perform for.",
         "Percakapan yang tepat di waktu yang salah akan gagal. Tak ada yang menyerap apa "
         "pun saat kewalahan, lapar, lelah, atau di depan penonton.\n\n"
         "Sebagian besar percakapan penting berjalan lebih baik nanti, dari samping, dan "
         "sambil bergerak — di mobil, saat berjalan, menjelang tidur — di mana tak ada "
         "kontak mata yang harus dilalui dan tak ada penonton untuk ditampilkan."),
        ("Teenagers in particular talk more freely side by side than face to face. The car "
         "is not a coincidence; it is the best therapy room most families have.",
         "Remaja khususnya bicara lebih lepas berdampingan daripada berhadapan. Mobil bukan "
         "kebetulan; ia ruang terapi terbaik yang dimiliki kebanyakan keluarga."),
        ("Delay one difficult conversation today to a better moment — and actually return to it.",
         "Tunda satu percakapan sulit hari ini ke momen yang lebih baik — dan benar-benar kembali ke sana."),
        ("When do the real conversations in our family actually happen?",
         "Kapan percakapan yang sungguhan di keluarga kami sebenarnya terjadi?"),
        ("\"Let's talk about this in the car later.\"",
         "\"Nanti kita bicarakan ini di mobil, ya.\""),
    ),
    109: d(
        ("Family meetings",
         "Musyawarah keluarga"),
        ("A short, regular family meeting moves problems out of the heat of the moment "
         "into a calm slot where they can actually be solved.\n\n"
         "Keep it short, keep it predictable, and let children raise items too. A meeting "
         "where only parents set the agenda is not a meeting; it is an announcement.",
         "Musyawarah keluarga yang singkat dan rutin memindahkan masalah dari panasnya momen "
         "ke slot tenang tempat masalah itu benar-benar bisa diselesaikan.\n\n"
         "Buat singkat, buat bisa ditebak, dan biarkan anak juga mengajukan hal. Pertemuan "
         "yang agendanya hanya ditentukan orang tua bukan musyawarah; itu pengumuman."),
        ("Fifteen minutes on a Sunday, with one thing that went well and one thing to fix, "
         "resolves more than hours of scattered arguing.",
         "Lima belas menit di hari Minggu, dengan satu hal yang berjalan baik dan satu hal "
         "untuk dibereskan, menyelesaikan lebih banyak daripada berjam-jam pertengkaran yang tersebar."),
        ("Hold one fifteen-minute family meeting this week. Let a child raise the first item.",
         "Adakan satu musyawarah keluarga lima belas menit minggu ini. Biarkan anak mengajukan hal pertama."),
        ("Where do problems in our family get solved, if anywhere?",
         "Di mana masalah di keluarga kami diselesaikan, kalau ada tempatnya?"),
        ("\"Put it on the list for Sunday.\"",
         "\"Masukkan ke daftar untuk hari Minggu.\""),
    ),
    110: d(
        ("Collaborative problem-solving basics",
         "Dasar memecahkan masalah bersama"),
        ("Collaborative problem-solving has three steps: hear the child's concern, state "
         "yours, then invent solutions together that address both.\n\n"
         "It is slower than imposing a rule and it produces solutions children actually "
         "follow, because they helped build them. It also teaches negotiation, which is a "
         "skill they will need permanently.",
         "Memecahkan masalah bersama punya tiga langkah: dengarkan kekhawatiran anak, "
         "sampaikan kekhawatiran Anda, lalu ciptakan solusi bersama yang menjawab keduanya.\n\n"
         "Ia lebih lambat daripada menjatuhkan aturan, dan menghasilkan solusi yang benar-benar "
         "dijalankan anak, karena mereka ikut membangunnya. Ia juga mengajarkan negosiasi — "
         "keterampilan yang akan mereka butuhkan selamanya."),
        ("\"You want more screen time, I want you sleeping properly. What could work for "
         "both?\" produces better agreements than any rule handed down.",
         "\"Kamu ingin waktu layar lebih banyak, Mama ingin kamu tidur cukup. Apa yang bisa "
         "cocok untuk keduanya?\" menghasilkan kesepakatan yang lebih baik daripada aturan "
         "yang dijatuhkan."),
        ("Solve one recurring problem collaboratively today instead of ruling on it.",
         "Selesaikan satu masalah yang berulang secara bersama hari ini, bukan dengan memutuskan sendiri."),
        ("Which recurring fight could become a shared problem instead?",
         "Pertengkaran berulang mana yang bisa diubah menjadi masalah bersama?"),
        ("\"That's what you want, this is what I need. Ideas?\"",
         "\"Itu maumu, ini yang Mama/Papa butuhkan. Ada ide?\""),
    ),
    111: d(
        ("Negotiation limits",
         "Batas dalam bernegosiasi"),
        ("Not everything is negotiable, and pretending otherwise is its own kind of "
         "dishonesty. Safety, health and core values are decided; bedtime routine details, "
         "sequence and style often are not.\n\n"
         "Being explicit about which is which prevents most of the arguing. Children push "
         "hardest where they cannot tell whether the door is actually closed.",
         "Tidak semuanya bisa dinegosiasikan, dan berpura-pura sebaliknya adalah bentuk "
         "ketidakjujuran tersendiri. Keselamatan, kesehatan, dan nilai inti sudah diputuskan; "
         "rincian rutinitas tidur, urutan, dan gayanya sering tidak.\n\n"
         "Menjelaskan mana yang mana mencegah sebagian besar pertengkaran. Anak mendorong "
         "paling keras di tempat mereka tak bisa tahu apakah pintunya benar-benar tertutup."),
        ("\"This one isn't up for discussion, and that one is\" is a clarity children "
         "actually find reassuring.",
         "\"Yang ini tidak bisa didiskusikan, dan yang itu bisa\" adalah kejelasan yang justru "
         "menenangkan anak."),
        ("Name one non-negotiable and one genuinely open item to your child today.",
         "Sebutkan satu hal yang tidak bisa ditawar dan satu hal yang benar-benar terbuka kepada anak hari ini."),
        ("Does my child know which of my rules can move and which cannot?",
         "Apakah anak tahu aturan saya yang mana yang bisa bergeser dan yang mana yang tidak?"),
        ("\"That one's fixed. This one you can choose.\"",
         "\"Yang itu sudah pasti. Yang ini kamu boleh pilih.\""),
    ),
    112: d(
        ("Teaching emotional vocabulary",
         "Mengajarkan kosakata emosi"),
        ("A child with words for feelings has an alternative to behaviour. This is not a "
         "soft skill; it is one of the most practical discipline interventions available.\n\n"
         "Vocabulary is taught by use, not by lists. Name feelings as they occur — yours "
         "and theirs — and the range grows on its own.",
         "Anak yang punya kata untuk perasaan punya alternatif selain perilaku. Ini bukan "
         "keterampilan lunak; ini salah satu intervensi disiplin paling praktis yang ada.\n\n"
         "Kosakata diajarkan lewat pemakaian, bukan lewat daftar. Sebutkan perasaan saat ia "
         "muncul — milik Anda dan miliknya — dan rentangnya bertumbuh dengan sendirinya."),
        ("Move past happy and sad. Lonely, overwhelmed, embarrassed, proud, disappointed "
         "and jealous each give a child a more precise tool.",
         "Lewati senang dan sedih. Kesepian, kewalahan, malu, bangga, kecewa, dan cemburu "
         "masing-masing memberi anak alat yang lebih presisi."),
        ("Teach one new feeling word today by using it about a real moment.",
         "Ajarkan satu kata perasaan baru hari ini dengan memakainya pada momen yang nyata."),
        ("How many feeling words does my child actually have?",
         "Berapa banyak kata perasaan yang benar-benar anak saya miliki?"),
        ("\"I think that one's called frustrated.\"",
         "\"Sepertinya yang itu namanya frustrasi.\""),
    ),
    113: d(
        ("Helping children tell the story of what happened",
         "Membantu anak menceritakan apa yang terjadi"),
        ("Putting an experience into a sequence — first this, then that, then I felt — is "
         "how children digest difficult events. An unnarrated bad experience tends to stay "
         "raw and reappear as behaviour.\n\n"
         "You do not need to interpret or fix it. Helping them get it into order is most "
         "of the work.",
         "Menyusun pengalaman menjadi urutan — mula-mula ini, lalu itu, lalu aku merasa — "
         "adalah cara anak mencerna kejadian sulit. Pengalaman buruk yang tak pernah "
         "diceritakan cenderung tetap mentah dan muncul lagi sebagai perilaku.\n\n"
         "Anda tak perlu menafsirkan atau membereskannya. Membantunya tersusun rapi sudah "
         "sebagian besar pekerjaannya."),
        ("\"What happened first? And then? And how did that feel?\" turns a jumble into a "
         "story a child can put down.",
         "\"Apa yang terjadi duluan? Lalu? Dan bagaimana rasanya?\" mengubah kekusutan menjadi "
         "cerita yang bisa anak letakkan."),
        ("Help your child narrate one difficult moment today in order.",
         "Bantu anak menceritakan satu momen sulit hari ini secara berurutan."),
        ("Do difficult things get talked through in our house, or just pass?",
         "Apakah hal-hal sulit dibicarakan sampai tuntas di rumah kami, atau hanya berlalu?"),
        ("\"Tell me what happened first.\"",
         "\"Ceritakan, apa yang terjadi duluan.\""),
    ),
    114: d(
        ("Teaching apology meaningfully",
         "Mengajarkan permintaan maaf yang bermakna"),
        ("A forced \"say sorry\" teaches the word and none of the meaning. Children learn to "
         "produce the sound to end the trouble, which is the opposite of what was wanted.\n\n"
         "A real apology has three parts: what I did, how it affected you, what I will do "
         "differently. Children can learn all three, given time and a demonstration.",
         "\"Ayo minta maaf\" yang dipaksakan mengajarkan katanya dan sama sekali bukan maknanya. "
         "Anak belajar memproduksi bunyinya untuk mengakhiri masalah — kebalikan dari yang diinginkan.\n\n"
         "Permintaan maaf yang sungguh punya tiga bagian: apa yang saya lakukan, bagaimana "
         "dampaknya bagi kamu, apa yang akan saya lakukan berbeda. Anak bisa belajar ketiganya, "
         "diberi waktu dan contoh."),
        ("Waiting until a child is calm and then helping them build a real apology teaches "
         "far more than extracting the word immediately.",
         "Menunggu sampai anak tenang lalu membantunya menyusun permintaan maaf yang sungguh "
         "mengajarkan jauh lebih banyak daripada memaksa kata itu keluar seketika."),
        ("Help your child make one apology with all three parts today.",
         "Bantu anak membuat satu permintaan maaf dengan ketiga bagiannya hari ini."),
        ("Am I teaching my child to apologise, or just to say the word?",
         "Apakah saya mengajarkan anak meminta maaf, atau sekadar mengucapkan katanya?"),
        ("\"What did it feel like for them?\"",
         "\"Menurutmu bagaimana rasanya buat dia?\""),
    ),
    115: d(
        ("Teaching restitution",
         "Mengajarkan memperbaiki kerugian"),
        ("Restitution — actually repairing the harm — teaches more than punishment does, "
         "because it is connected to the act rather than imposed on top of it.\n\n"
         "Helping clean up what you knocked over, remaking what you broke, doing something "
         "kind for the person you hurt: each of these closes the loop in a way that sitting "
         "on a step never does.",
         "Memperbaiki kerugian — sungguh-sungguh membereskan kerusakannya — mengajarkan lebih "
         "banyak daripada hukuman, karena ia terhubung dengan perbuatannya, bukan ditimpakan "
         "di atasnya.\n\n"
         "Ikut membersihkan yang dijatuhkan, memperbaiki yang dirusak, melakukan sesuatu yang "
         "baik untuk orang yang disakiti: masing-masing menutup lingkarannya dengan cara yang "
         "tak pernah dilakukan duduk di pojok."),
        ("\"How can you make this better?\" invites repair. \"Go to your room\" invites nothing "
         "except waiting for it to end.",
         "\"Bagaimana caramu memperbaikinya?\" mengundang perbaikan. \"Masuk kamar\" tidak "
         "mengundang apa pun selain menunggu sampai selesai."),
        ("Replace one consequence today with an act of repair.",
         "Ganti satu konsekuensi hari ini dengan tindakan memperbaiki."),
        ("Do my consequences repair anything, or only register displeasure?",
         "Apakah konsekuensi saya memperbaiki sesuatu, atau hanya menyatakan ketidaksenangan?"),
        ("\"How could you put this right?\"",
         "\"Bagaimana kamu bisa membereskannya?\""),
    ),
    116: d(
        ("Helping children ask for help",
         "Membantu anak meminta bantuan"),
        ("Asking for help is a skill, and shame suppresses it. A child who fears looking "
         "stupid will hide difficulty until it becomes a crisis — with homework, with "
         "friendships, and later with much bigger things.\n\n"
         "How you respond to small requests for help now decides whether you get the large "
         "ones later.",
         "Meminta bantuan adalah keterampilan, dan rasa malu menekannya. Anak yang takut "
         "terlihat bodoh akan menyembunyikan kesulitan sampai menjadi krisis — soal PR, soal "
         "pertemanan, dan kelak soal hal-hal yang jauh lebih besar.\n\n"
         "Cara Anda menanggapi permintaan bantuan kecil sekarang menentukan apakah Anda "
         "mendapat yang besar nanti."),
        ("Responding to \"I don't get it\" with warmth rather than exasperation is a small "
         "investment with a very long payoff.",
         "Menanggapi \"aku tidak paham\" dengan kehangatan alih-alih kejengkelan adalah "
         "investasi kecil dengan hasil yang sangat panjang."),
        ("Respond to one request for help today with visible warmth, however inconvenient.",
         "Tanggapi satu permintaan bantuan hari ini dengan kehangatan yang terlihat, "
         "seberapa pun tidak praktisnya."),
        ("Is it safe to be confused in our house?",
         "Apakah aman untuk merasa bingung di rumah kami?"),
        ("\"I'm glad you asked. Let's look at it.\"",
         "\"Bagus kamu bertanya. Ayo kita lihat sama-sama.\""),
    ),
    117: d(
        ("Responding to I hate you",
         "Menanggapi \"aku benci Mama\""),
        ("\"I hate you\" is almost never information about love. It is the largest word a "
         "child has for a feeling that has outgrown their vocabulary — usually powerless, "
         "furious, or wounded.\n\n"
         "Reacting to the words escalates. Responding to the feeling underneath them ends "
         "it, usually faster than you expect.",
         "\"Aku benci Mama\" hampir tak pernah informasi tentang cinta. Itu kata terbesar yang "
         "dimiliki anak untuk perasaan yang melampaui kosakatanya — biasanya tak berdaya, "
         "murka, atau terluka.\n\n"
         "Bereaksi pada kata-katanya memperbesar masalah. Menanggapi perasaan di baliknya "
         "mengakhirinya, biasanya lebih cepat dari perkiraan Anda."),
        ("\"You're really angry with me right now\" defuses. \"Don't you dare speak to me "
         "like that\" guarantees another ten minutes.",
         "\"Kamu benar-benar marah pada Mama sekarang\" meredakan. \"Berani-beraninya bicara "
         "begitu\" menjamin sepuluh menit tambahan."),
        ("If you hear it today, answer the feeling and not the sentence.",
         "Jika Anda mendengarnya hari ini, jawab perasaannya, bukan kalimatnya."),
        ("What is my child usually feeling when they say the worst thing they can think of?",
         "Apa yang biasanya anak rasakan saat dia mengucapkan hal terburuk yang terpikir olehnya?"),
        ("\"You're really angry with me. I can take it.\"",
         "\"Kamu sangat marah pada Mama/Papa. Tidak apa-apa.\""),
    ),
    118: d(
        ("Responding to lying",
         "Menanggapi kebohongan"),
        ("Most childhood lying is fear-driven, not character-driven. Children lie to avoid "
         "a reaction they expect, which means the size of your reaction is one of the main "
         "inputs into how much they lie.\n\n"
         "Making truth cheaper than concealment is the entire strategy. That means "
         "responding to a confession more gently than to a discovery.",
         "Sebagian besar kebohongan anak didorong rasa takut, bukan karakter. Anak berbohong "
         "untuk menghindari reaksi yang mereka perkirakan, artinya besarnya reaksi Anda "
         "adalah salah satu masukan utama seberapa sering mereka berbohong.\n\n"
         "Membuat kejujuran lebih murah daripada menyembunyikan adalah seluruh strateginya. "
         "Itu berarti menanggapi pengakuan dengan lebih lembut daripada menanggapi ketahuan."),
        ("\"Thank you for telling me the truth — that was hard\" costs you the satisfaction "
         "of the telling-off and buys you years of honesty.",
         "\"Terima kasih sudah jujur — itu berat\" menghabiskan kepuasan Anda untuk memarahi "
         "dan membeli bertahun-tahun kejujuran."),
        ("If your child tells you a hard truth today, thank them before anything else.",
         "Jika anak menyampaikan kebenaran yang berat hari ini, berterima kasihlah sebelum hal lain."),
        ("Is telling me the truth safer than hiding it, from my child's point of view?",
         "Dari sudut pandang anak saya, apakah jujur kepada saya lebih aman daripada menyembunyikan?"),
        ("\"Thank you for telling me. That took courage.\"",
         "\"Terima kasih sudah cerita. Itu butuh keberanian.\""),
    ),
    119: d(
        ("Responding to whining",
         "Menanggapi rengekan"),
        ("Whining is almost always a depletion signal wearing an irritating costume. "
         "Correcting the tone while ignoring the need tends to produce more of it.\n\n"
         "Meet the need first. Then, when everyone is calm and nothing is at stake, teach "
         "the tone — because the tone is genuinely worth learning.",
         "Rengekan hampir selalu sinyal kehabisan tenaga yang mengenakan kostum menjengkelkan. "
         "Membetulkan nadanya sambil mengabaikan kebutuhannya cenderung menghasilkan lebih banyak rengekan.\n\n"
         "Penuhi kebutuhannya dulu. Lalu, saat semua tenang dan tak ada yang dipertaruhkan, "
         "ajarkan nadanya — karena nada itu memang layak dipelajari."),
        ("Teaching \"ask me in your normal voice\" works well at 4pm on a good day and works "
         "not at all at 6pm on a hard one.",
         "Mengajarkan \"minta pakai suara biasa\" berhasil baik pukul empat sore di hari yang "
         "baik, dan sama sekali tidak berhasil pukul enam sore di hari yang berat."),
        ("Meet the need behind one whine today, and teach the tone at a calmer hour.",
         "Penuhi kebutuhan di balik satu rengekan hari ini, dan ajarkan nadanya di jam yang lebih tenang."),
        ("Am I trying to teach at the moment my child has least capacity to learn?",
         "Apakah saya mencoba mengajar tepat saat anak paling tidak mampu belajar?"),
        ("\"I want to help. Let's sort out what you need first.\"",
         "\"Mama/Papa mau bantu. Kita bereskan dulu apa yang kamu butuhkan.\""),
    ),
    120: d(
        ("Responding to refusal",
         "Menanggapi penolakan"),
        ("Flat refusal is where parents most often escalate, because it reads as a "
         "challenge to authority. Very often it is something smaller: the child is mid-task, "
         "overwhelmed, or has no route to comply without losing face.\n\n"
         "Offering a way to comply that preserves dignity resolves more refusals than "
         "raising the stakes.",
         "Penolakan mentah adalah tempat orang tua paling sering meningkatkan tensi, karena "
         "terbaca sebagai tantangan atas wibawa. Sangat sering ia sesuatu yang lebih kecil: "
         "anak sedang di tengah kegiatan, kewalahan, atau tak punya jalan untuk menurut tanpa "
         "kehilangan muka.\n\n"
         "Menawarkan cara menurut yang menjaga harga dirinya menyelesaikan lebih banyak "
         "penolakan daripada menaikkan taruhan."),
        ("\"Do you want to do it now or in two minutes?\" hands back enough control to make "
         "compliance possible without anyone backing down.",
         "\"Mau sekarang atau dua menit lagi?\" mengembalikan cukup kendali agar menurut jadi "
         "mungkin tanpa ada yang harus mengalah."),
        ("Give your child a dignified route to comply once today.",
         "Beri anak satu jalan yang terhormat untuk menurut hari ini."),
        ("Do I leave my child a way to say yes without losing face?",
         "Apakah saya menyisakan jalan bagi anak untuk berkata ya tanpa kehilangan muka?"),
        ("\"Now or in two minutes — you pick.\"",
         "\"Sekarang atau dua menit lagi — kamu pilih.\""),
    ),
    121: d(
        ("Weekly reflection",
         "Refleksi mingguan"),
        ("This chapter reduces to one sequence: empathy first, then redirection. Almost "
         "every technique in it is a way of getting the empathy to arrive before the "
         "instruction.\n\n"
         "That order is also the end of the free part of this guide. Chapters 1 to 4 are "
         "the foundation — mindset, development, your own regulation, and communication. "
         "Everything that follows is built on them.",
         "Bab ini menyempit menjadi satu urutan: empati dulu, baru pengarahan. Hampir setiap "
         "teknik di dalamnya adalah cara agar empatinya tiba sebelum instruksinya.\n\n"
         "Urutan itu juga menutup bagian gratis panduan ini. Bab 1 sampai 4 adalah fondasinya "
         "— pola pikir, perkembangan, pengendalian diri Anda, dan komunikasi. Semua yang "
         "menyusul dibangun di atasnya."),
        ("If you only keep one thing from four months of reading, keep the order: feeling "
         "first, then the rule. It changes almost every difficult moment.",
         "Jika dari empat bulan membaca Anda hanya menyimpan satu hal, simpanlah urutannya: "
         "perasaan dulu, baru aturan. Ia mengubah hampir setiap momen sulit."),
        ("Look back at one conflict this week and ask where the empathy went in the sequence.",
         "Tengok satu konflik minggu ini dan tanyakan, di urutan mana empatinya berada."),
        ("In my hardest moments, does empathy come before the instruction or after it?",
         "Di momen tersulit saya, apakah empati datang sebelum instruksi atau sesudahnya?"),
        ("\"Feeling first. Then the rule.\"",
         "\"Perasaan dulu. Baru aturan.\""),
    ),
}
