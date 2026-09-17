# Chapter 7 — Routines and Home Systems (days 182-211)
#
# Grounded in the founder's guidebook chapter 7 ("Calm structure beats constant
# reminding") and toolkit tool 7 (Friction-Point Redesigner).
#
# Through-line: most discipline problems are system problems wearing a costume.

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
    182: d(
        ("Why routines reduce conflict",
         "Mengapa rutinitas mengurangi konflik"),
        ("A routine is a decision made once instead of every day. That is the whole "
         "mechanism, and it is why routines reduce conflict more reliably than any "
         "discipline technique.\n\n"
         "When the order is fixed, there is nothing to negotiate. The child is not "
         "arguing with you; they are following a sequence that exists independently of "
         "your mood, your energy, and how the day has gone.",
         "Rutinitas adalah keputusan yang dibuat sekali, bukan setiap hari. Itulah seluruh "
         "mekanismenya, dan itulah sebabnya rutinitas mengurangi konflik lebih andal "
         "daripada teknik disiplin apa pun.\n\n"
         "Ketika urutannya tetap, tak ada yang perlu dinegosiasikan. Anak tidak sedang "
         "berdebat dengan Anda; dia mengikuti urutan yang ada terlepas dari suasana hati "
         "Anda, tenaga Anda, dan bagaimana hari itu berjalan."),
        ("The families who argue least about bedtime are rarely the strictest. They are "
         "the ones where bedtime stopped being a question some time ago.",
         "Keluarga yang paling jarang bertengkar soal jam tidur jarang yang paling ketat. "
         "Mereka adalah keluarga yang jam tidurnya sudah lama berhenti menjadi pertanyaan."),
        ("Pick the moment you argue about most and ask whether it has a fixed order at all.",
         "Pilih momen yang paling sering jadi bahan pertengkaran dan tanyakan apakah ia "
         "punya urutan tetap sama sekali."),
        ("Which daily fight is really just a decision we keep re-making?",
         "Pertengkaran harian mana yang sebenarnya hanya keputusan yang terus kami buat ulang?"),
        ("\"Same order as always.\"",
         "\"Urutannya sama seperti biasa.\""),
        framework=fw(
            ("Behaviour problem or system problem?", "Masalah perilaku atau masalah sistem?"),
            ("Before deciding on a consequence, check which one you are actually looking at.",
             "Sebelum memutuskan konsekuensi, periksa dulu yang mana yang sebenarnya Anda hadapi."),
            [
                (("System problem", "Masalah sistem"),
                 [("Predictable", "Bisa ditebak"), ("Same time daily", "Jam yang sama tiap hari")],
                 ("It happens at the same point every day, to a child who is otherwise "
                  "fine, and reminding has never fixed it.",
                  "Terjadi di titik yang sama setiap hari, pada anak yang selain itu "
                  "baik-baik saja, dan mengingatkan tak pernah menyelesaikannya."),
                 ("Redesign the moment: fewer steps, clearer order, visible cue. "
                  "Consequences will not touch it.",
                  "Rancang ulang momennya: langkah lebih sedikit, urutan lebih jelas, "
                  "isyarat yang terlihat. Konsekuensi tidak akan menyentuhnya.")),
                (("Behaviour problem", "Masalah perilaku"),
                 [("Varies", "Berubah-ubah"), ("Has a choice in it", "Ada pilihan di dalamnya")],
                 ("It happens across different moments, the child can do it fine at other "
                  "times, and a real choice was made.",
                  "Terjadi di berbagai momen, anak bisa melakukannya dengan baik di waktu "
                  "lain, dan ada pilihan yang sungguh dibuat."),
                 ("Now discipline applies — calm, consistent, connected, as in chapter 5.",
                  "Barulah disiplin berlaku — tenang, konsisten, terhubung, seperti bab 5.")),
            ],
        ),
    ),
    183: d(
        ("Morning routine design",
         "Merancang rutinitas pagi"),
        ("Mornings fail for structural reasons: too many steps, too little time, and "
         "decisions being made while everyone is still half asleep.\n\n"
         "The fix is mostly moving work to the night before. Clothes out, bags packed, "
         "breakfast decided — every decision removed from the morning is a conflict that "
         "cannot happen.",
         "Pagi berantakan karena alasan struktural: terlalu banyak langkah, terlalu sedikit "
         "waktu, dan keputusan dibuat saat semua orang masih setengah tidur.\n\n"
         "Solusinya sebagian besar adalah memindahkan pekerjaan ke malam sebelumnya. Baju "
         "disiapkan, tas dikemas, sarapan diputuskan — setiap keputusan yang dihapus dari "
         "pagi adalah konflik yang tak bisa terjadi."),
        ("Fifteen minutes of preparation at night removes roughly thirty minutes of "
         "conflict in the morning, and everybody arrives in a better mood.",
         "Lima belas menit persiapan di malam hari menghapus kira-kira tiga puluh menit "
         "konflik di pagi hari, dan semua orang tiba dengan suasana hati yang lebih baik."),
        ("Move one morning decision to tonight.",
         "Pindahkan satu keputusan pagi ke malam ini."),
        ("What are we deciding at 7am that could have been decided at 8pm?",
         "Apa yang kami putuskan pukul tujuh pagi, yang sebenarnya bisa diputuskan pukul delapan malam?"),
        ("\"Let's set it out now so the morning is easy.\"",
         "\"Kita siapkan sekarang supaya paginya mudah.\""),
    ),
    184: d(
        ("Bedtime routine design",
         "Merancang rutinitas tidur"),
        ("Bedtime concentrates everything difficult into one half hour: a tired child, a "
         "tired parent, a transition away from something pleasant, and a separation.\n\n"
         "A good bedtime routine is short, always the same order, and moves steadily "
         "toward quieter and darker. Four steps is plenty; the order matters more than "
         "the content.",
         "Waktu tidur memusatkan semua yang sulit ke dalam setengah jam: anak yang lelah, "
         "orang tua yang lelah, perpindahan dari sesuatu yang menyenangkan, dan perpisahan.\n\n"
         "Rutinitas tidur yang baik itu singkat, urutannya selalu sama, dan bergerak mantap "
         "menuju lebih tenang dan lebih gelap. Empat langkah sudah cukup; urutannya lebih "
         "penting daripada isinya."),
        ("Ending in the same place every night — the same chair, the same song, the same "
         "sentence — does more than any of the earlier steps.",
         "Berakhir di tempat yang sama setiap malam — kursi yang sama, lagu yang sama, "
         "kalimat yang sama — lebih berpengaruh daripada langkah-langkah sebelumnya."),
        ("Write your four bedtime steps down tonight and follow them exactly.",
         "Tuliskan empat langkah waktu tidur Anda malam ini dan ikuti persis."),
        ("Does our bedtime move toward calm, or does it get louder as it goes?",
         "Apakah waktu tidur kami bergerak menuju tenang, atau makin ribut seiring berjalannya?"),
        ("\"Four things, then lights out. Same as always.\"",
         "\"Empat hal, lalu lampu mati. Seperti biasa.\""),
    ),
    185: d(
        ("Homework routine",
         "Rutinitas mengerjakan PR"),
        ("Homework conflict is usually about starting, not about working. The resistance "
         "sits at the beginning, and once a child is three minutes in it often "
         "disappears.\n\n"
         "A fixed time, a fixed place, and a first step small enough to be trivial "
         "removes most of it. Negotiating when homework happens each day guarantees a "
         "daily negotiation.",
         "Konflik PR biasanya soal memulai, bukan soal mengerjakan. Perlawanannya ada di "
         "awal, dan begitu anak sudah tiga menit di dalamnya, sering menghilang.\n\n"
         "Waktu yang tetap, tempat yang tetap, dan langkah pertama yang cukup kecil untuk "
         "terasa sepele menghapus sebagian besarnya. Menegosiasikan kapan PR dikerjakan "
         "setiap hari menjamin negosiasi setiap hari."),
        ("\"Just the first question\" gets more homework finished than any argument about "
         "responsibility ever has.",
         "\"Soal pertama saja dulu\" menyelesaikan lebih banyak PR daripada perdebatan apa "
         "pun tentang tanggung jawab."),
        ("Fix the time and place for homework today, and shrink the first step.",
         "Tetapkan waktu dan tempat PR hari ini, dan perkecil langkah pertamanya."),
        ("Is the fight about the work, or about starting it?",
         "Pertengkarannya soal pekerjaannya, atau soal memulainya?"),
        ("\"First line only. Then we'll see.\"",
         "\"Baris pertama saja. Nanti kita lihat.\""),
    ),
    186: d(
        ("Chore routines",
         "Rutinitas pekerjaan rumah"),
        ("Chores work when they are small, attached to an existing anchor, and expected "
         "rather than requested. A chore that has to be asked for is a negotiation "
         "wearing an apron.\n\n"
         "Attach the chore to something that already happens — after dinner, before "
         "screens — so the trigger is the routine rather than your voice.",
         "Pekerjaan rumah berhasil ketika kecil, dilekatkan pada jangkar yang sudah ada, "
         "dan diharapkan, bukan diminta. Tugas yang harus diminta adalah negosiasi yang "
         "memakai celemek.\n\n"
         "Lekatkan tugasnya pada sesuatu yang sudah terjadi — setelah makan malam, sebelum "
         "layar — sehingga pemicunya adalah rutinitasnya, bukan suara Anda."),
        ("\"Plates in the sink before screens\" needs saying for about a week. After that "
         "the sequence carries it.",
         "\"Piring ke wastafel sebelum layar\" perlu diucapkan sekitar seminggu. Setelah "
         "itu urutannya yang membawanya."),
        ("Attach one chore to an existing daily anchor today.",
         "Lekatkan satu tugas rumah pada jangkar harian yang sudah ada hari ini."),
        ("Which chores do I still have to ask for every single time?",
         "Tugas mana yang masih harus saya minta setiap kali?"),
        ("\"That happens before this. That's the order.\"",
         "\"Itu dulu, baru ini. Begitu urutannya.\""),
    ),
    187: d(
        ("Transition warnings",
         "Aba-aba sebelum berpindah"),
        ("Stopping something absorbing requires a gear change children are not yet good "
         "at. A warning gives them time to begin the internal work of letting go.\n\n"
         "Without notice, a child can only protest — they have been ambushed. With notice, "
         "the same instruction is usually accepted, and it costs you two minutes.",
         "Menghentikan sesuatu yang menyerap perhatian butuh pergantian gigi yang belum "
         "dikuasai anak. Aba-aba memberi mereka waktu untuk memulai kerja batin melepaskan.\n\n"
         "Tanpa pemberitahuan, anak hanya bisa memprotes — dia diserang mendadak. Dengan "
         "pemberitahuan, instruksi yang sama biasanya diterima, dan biayanya dua menit."),
        ("Make the warning concrete rather than temporal: young children understand \"after "
         "this episode\" far better than \"in ten minutes\".",
         "Buat aba-abanya konkret, bukan soal waktu: anak kecil jauh lebih paham \"setelah "
         "episode ini\" daripada \"sepuluh menit lagi\"."),
        ("Give a concrete warning before every transition today.",
         "Beri aba-aba yang konkret sebelum setiap perpindahan hari ini."),
        ("How often do my instructions arrive as an ambush?",
         "Seberapa sering instruksi saya datang sebagai serangan mendadak?"),
        ("\"After this one, we stop.\"",
         "\"Setelah yang ini, kita berhenti.\""),
    ),
    188: d(
        ("Visual schedules",
         "Jadwal visual"),
        ("A picture on the wall becomes the thing giving instructions, instead of you. "
         "That small shift changes the relationship: the child is answering to the chart, "
         "not resisting a person.\n\n"
         "It works particularly well for pre-readers, for children who struggle with "
         "working memory, and for any household where mornings involve a lot of shouting.",
         "Gambar di dinding menjadi pihak yang memberi instruksi, bukan Anda. Pergeseran "
         "kecil itu mengubah hubungannya: anak menanggapi tabel, bukan melawan seseorang.\n\n"
         "Ini sangat berhasil untuk anak yang belum membaca, anak yang kesulitan dengan "
         "memori kerja, dan rumah mana pun yang paginya penuh teriakan."),
        ("\"What does the chart say is next?\" takes you out of the conflict entirely, "
         "which is exactly the point.",
         "\"Menurut tabelnya, berikutnya apa?\" mengeluarkan Anda sepenuhnya dari "
         "konfliknya, dan itulah maksudnya."),
        ("Draw or photograph a three-step visual sequence for your worst transition.",
         "Gambar atau foto urutan visual tiga langkah untuk perpindahan terburuk Anda."),
        ("Could my child follow our morning without me speaking at all?",
         "Bisakah anak saya menjalani pagi tanpa saya bicara sama sekali?"),
        ("\"What's next on the chart?\"",
         "\"Berikutnya apa di tabelnya?\""),
    ),
    189: d(
        ("Preparing children ahead of time",
         "Menyiapkan anak sebelumnya"),
        ("Children handle new situations far better when they know what is coming. "
         "Surprise is a load, and a loaded child behaves worse.\n\n"
         "Describe the shape of the thing in advance: where you are going, how long, what "
         "will be expected, and what they can do if it gets hard. Two minutes of preview "
         "prevents a great deal.",
         "Anak menghadapi situasi baru jauh lebih baik ketika tahu apa yang akan datang. "
         "Kejutan adalah beban, dan anak yang terbebani berperilaku lebih buruk.\n\n"
         "Gambarkan bentuk acaranya lebih dulu: ke mana, berapa lama, apa yang diharapkan, "
         "dan apa yang bisa dia lakukan jika terasa berat. Dua menit gambaran awal mencegah banyak hal."),
        ("Including \"and if you need a break, come find me\" gives a child an exit, which "
         "usually means they need it less.",
         "Menyertakan \"dan kalau kamu butuh istirahat, cari Mama ya\" memberi anak jalan "
         "keluar, yang biasanya justru membuatnya lebih jarang membutuhkannya."),
        ("Preview one upcoming situation in three sentences today.",
         "Gambarkan satu situasi yang akan datang dalam tiga kalimat hari ini."),
        ("How much does my child know about what today holds?",
         "Seberapa banyak anak saya tahu tentang apa isi hari ini?"),
        ("\"Here's what's going to happen, and here's what you can do.\"",
         "\"Ini yang akan terjadi, dan ini yang bisa kamu lakukan.\""),
    ),
    190: d(
        ("Organizing toys and materials",
         "Menata mainan dan perlengkapan"),
        ("A child cannot tidy a room they cannot understand. If everything lives in one "
         "large box, tidying is an impossible sorting task, and refusal looks like defiance.\n\n"
         "Fewer toys, visible homes, and containers a child can actually lift make tidying "
         "possible. Most tidying battles are storage design problems.",
         "Anak tak bisa merapikan ruangan yang tak bisa dia pahami. Jika semuanya tinggal "
         "dalam satu kotak besar, merapikan menjadi tugas menyortir yang mustahil, dan "
         "penolakannya tampak seperti pembangkangan.\n\n"
         "Mainan lebih sedikit, rumah yang terlihat, dan wadah yang benar-benar bisa "
         "diangkat anak membuat merapikan menjadi mungkin. Sebagian besar pertengkaran "
         "soal merapikan adalah masalah desain penyimpanan."),
        ("If an adult would struggle to know where something goes, a five-year-old has no "
         "chance at all.",
         "Jika orang dewasa saja kesulitan tahu ke mana sesuatu harus disimpan, anak lima "
         "tahun sama sekali tidak punya peluang."),
        ("Give one category of toys a clear, reachable home today.",
         "Beri satu kategori mainan rumah yang jelas dan terjangkau hari ini."),
        ("Is tidying actually possible for my child, as the room is set up now?",
         "Dengan penataan ruangan sekarang, apakah merapikan sungguh mungkin bagi anak saya?"),
        ("\"Everything has a place. Let's find this one's.\"",
         "\"Semua ada tempatnya. Ayo cari tempat yang ini.\""),
    ),
    191: d(
        ("Simplifying overstimulating spaces",
         "Menyederhanakan ruang yang terlalu ramai"),
        ("Visual noise is a load on a developing brain. Rooms crowded with toys, colour "
         "and choice produce children who flit between things and settle at none.\n\n"
         "Fewer options usually produce deeper play. Rotating toys — half away in a "
         "cupboard, swapped monthly — often makes old toys interesting again.",
         "Kebisingan visual adalah beban bagi otak yang sedang berkembang. Ruangan yang "
         "penuh mainan, warna, dan pilihan menghasilkan anak yang melompat-lompat dan tak "
         "menetap di mana pun.\n\n"
         "Pilihan yang lebih sedikit biasanya menghasilkan permainan yang lebih dalam. "
         "Merotasi mainan — separuh disimpan di lemari, ditukar tiap bulan — sering membuat "
         "mainan lama menarik kembali."),
        ("Parents are often surprised that removing half the toys increases how long a "
         "child plays with the rest.",
         "Orang tua sering terkejut bahwa menyingkirkan separuh mainan justru memperpanjang "
         "waktu anak bermain dengan sisanya."),
        ("Put half of one toy category away today and watch what happens to play.",
         "Simpan separuh dari satu kategori mainan hari ini dan perhatikan apa yang terjadi "
         "pada permainannya."),
        ("Is there more in this room than my child can actually use?",
         "Apakah isi ruangan ini lebih banyak daripada yang sanggup dipakai anak saya?"),
        ("\"Let's put some away for a while.\"",
         "\"Kita simpan sebagian dulu untuk sementara.\""),
    ),
    192: d(
        ("Family meal rhythm",
         "Ritme makan keluarga"),
        ("Regular family meals are one of the most consistently protective routines in "
         "child development — associated with better wellbeing, language and school "
         "outcomes across many studies.\n\n"
         "It is the regularity and the conversation that matter, not the food or the "
         "formality. Three unhurried meals a week beats seven tense ones.",
         "Makan bersama keluarga secara teratur adalah salah satu rutinitas paling "
         "konsisten melindungi dalam perkembangan anak — dikaitkan dengan kesejahteraan, "
         "bahasa, dan hasil sekolah yang lebih baik dalam banyak penelitian.\n\n"
         "Yang penting adalah keteraturan dan percakapannya, bukan makanannya atau "
         "formalitasnya. Tiga kali makan tanpa terburu-buru dalam seminggu mengalahkan "
         "tujuh kali yang penuh ketegangan."),
        ("Protecting three meals a week is realistic for most families. Aiming for every "
         "night and failing tends to end the practice entirely.",
         "Melindungi tiga kali makan seminggu realistis bagi kebanyakan keluarga. Menargetkan "
         "setiap malam lalu gagal cenderung menghentikan kebiasaannya sama sekali."),
        ("Choose the three meals this week you will protect, and put them somewhere visible.",
         "Pilih tiga waktu makan minggu ini yang akan Anda lindungi, dan tulis di tempat yang terlihat."),
        ("How many meals a week do we actually eat together, without screens?",
         "Berapa kali seminggu kami sungguh makan bersama, tanpa layar?"),
        ("\"These three are ours. We eat together.\"",
         "\"Yang tiga ini milik kita. Kita makan bersama.\""),
    ),
    193: d(
        ("Sleep hygiene for children",
         "Kebersihan tidur anak"),
        ("Sleep is the single highest-yield adjustment available to most families, and the "
         "one most often quietly sacrificed. A tired child is more impulsive, more "
         "emotional and far less able to recover from small frustrations.\n\n"
         "The levers are unglamorous and they work: consistent times, a dark cool room, "
         "screens off well before bed, and a wind-down that moves toward quiet.",
         "Tidur adalah penyesuaian dengan hasil tertinggi yang tersedia bagi kebanyakan "
         "keluarga, dan yang paling sering diam-diam dikorbankan. Anak yang lelah lebih "
         "impulsif, lebih emosional, dan jauh lebih sulit pulih dari frustrasi kecil.\n\n"
         "Tuasnya tidak menarik dan memang berhasil: waktu yang konsisten, kamar yang gelap "
         "dan sejuk, layar dimatikan jauh sebelum tidur, dan pendinginan yang bergerak menuju hening."),
        ("Before investigating a child's character, check their sleep for a week. A "
         "surprising number of behaviour problems resolve there.",
         "Sebelum menyelidiki karakter anak, periksa tidurnya selama seminggu. Jumlah "
         "masalah perilaku yang selesai di situ mengejutkan."),
        ("Move one thing earlier tonight — screens off, bath, or bedtime itself.",
         "Majukan satu hal malam ini — layar dimatikan, mandi, atau jam tidurnya sendiri."),
        ("Is my child actually getting enough sleep, honestly counted?",
         "Kalau dihitung jujur, apakah anak saya benar-benar cukup tidur?"),
        ("\"Earlier tonight. Tomorrow will be easier.\"",
         "\"Malam ini lebih awal. Besok akan lebih mudah.\""),
    ),
    194: d(
        ("Device-free family moments",
         "Momen keluarga tanpa gawai"),
        ("Children read parental phone use as a verdict on their own importance, even "
         "when nothing is said. A parent physically present but attentionally elsewhere is "
         "a specific kind of absence, and children feel it precisely.\n\n"
         "Protecting a few device-free windows matters more than the total screen count — "
         "meals, the school pickup, and the last half hour before bed.",
         "Anak membaca penggunaan ponsel orang tua sebagai vonis atas pentingnya diri "
         "mereka, meski tak ada yang dikatakan. Orang tua yang hadir secara fisik tapi "
         "perhatiannya di tempat lain adalah bentuk ketidakhadiran tersendiri, dan anak "
         "merasakannya dengan tepat.\n\n"
         "Melindungi beberapa jendela bebas gawai lebih penting daripada total waktu layar "
         "— saat makan, saat menjemput sekolah, dan setengah jam terakhir sebelum tidur."),
        ("The pickup moment is a small one and a loaded one: a child scanning for your face "
         "and finding the top of your head is a repeated small disappointment.",
         "Momen penjemputan itu kecil dan sarat makna: anak yang mencari wajah Anda lalu "
         "menemukan ubun-ubun Anda mengalami kekecewaan kecil yang berulang."),
        ("Put your phone in another room for one window today.",
         "Letakkan ponsel Anda di ruangan lain untuk satu jendela waktu hari ini."),
        ("What does my child see me choose when they walk into the room?",
         "Apa yang anak lihat saya pilih ketika dia masuk ruangan?"),
        ("\"Phone's away. I'm here.\"",
         "\"Ponsel disimpan. Mama/Papa di sini.\""),
    ),
    195: d(
        ("Car ride routines",
         "Rutinitas di perjalanan"),
        ("The car is one of the best conversation spaces most families have. Side by side, "
         "no eye contact required, a natural time limit, nowhere else to be.\n\n"
         "Teenagers in particular talk more freely there than across a table. It is worth "
         "protecting the car as talking space rather than filling it with screens.",
         "Mobil adalah salah satu ruang percakapan terbaik yang dimiliki kebanyakan "
         "keluarga. Berdampingan, tak perlu kontak mata, ada batas waktu alami, tak ada "
         "tempat lain untuk dituju.\n\n"
         "Remaja khususnya bicara lebih lepas di sana daripada di meja makan. Layak untuk "
         "melindungi mobil sebagai ruang bicara, bukan mengisinya dengan layar."),
        ("The hardest conversations often happen most easily at 40km/h with both people "
         "looking at the road.",
         "Percakapan tersulit sering paling mudah terjadi di kecepatan 40 km/jam dengan "
         "kedua orang menatap jalan."),
        ("Leave the screens off for one journey today and see what gets said.",
         "Matikan layar untuk satu perjalanan hari ini dan lihat apa yang terucap."),
        ("Where do the real conversations in our family happen?",
         "Di mana percakapan yang sungguhan di keluarga kami terjadi?"),
        ("\"Just us and the road for a bit.\"",
         "\"Sebentar cuma kita dan jalanan.\""),
    ),
    196: d(
        ("After-school decompression",
         "Melepas penat sepulang sekolah"),
        ("Children hold themselves together all day at school and let go the moment they "
         "reach the safest person available. The difficult hour after pickup is not a "
         "sign that something went wrong — it is a sign that you are safe.\n\n"
         "Questions and instructions land badly in that window. Food, quiet and a bit of "
         "physical movement land well.",
         "Anak menahan diri sepanjang hari di sekolah dan melepaskannya begitu bertemu "
         "orang paling aman yang tersedia. Jam yang sulit setelah dijemput bukan tanda ada "
         "yang salah — itu tanda bahwa Anda aman.\n\n"
         "Pertanyaan dan instruksi tidak diterima dengan baik di jendela itu. Makanan, "
         "ketenangan, dan sedikit gerak fisik diterima dengan baik."),
        ("\"How was school?\" asked at the school gate is the worst possible timing. The "
         "same question two hours later often gets a real answer.",
         "\"Bagaimana sekolahnya?\" yang ditanyakan di gerbang sekolah adalah waktu paling "
         "buruk. Pertanyaan yang sama dua jam kemudian sering mendapat jawaban sungguhan."),
        ("Offer food and quiet before any questions today.",
         "Tawarkan makanan dan ketenangan sebelum pertanyaan apa pun hari ini."),
        ("What does my child actually need in the first thirty minutes at home?",
         "Apa yang sebenarnya anak butuhkan di tiga puluh menit pertama di rumah?"),
        ("\"Eat first. We can talk later.\"",
         "\"Makan dulu. Nanti kita bisa cerita.\""),
    ),
    197: d(
        ("Weekend rhythm",
         "Ritme akhir pekan"),
        ("Weekends fail in two opposite directions: packed so full that everyone returns "
         "exhausted, or so shapeless that the day dissolves and nobody enjoys it.\n\n"
         "A light rhythm helps — one anchor, one outing, one genuinely unstructured "
         "stretch. Structure and rest are not opposites; rest needs a little structure to "
         "survive.",
         "Akhir pekan gagal dalam dua arah berlawanan: dijejali sampai semua orang pulang "
         "kelelahan, atau tanpa bentuk sama sekali sehingga harinya larut dan tak ada yang "
         "menikmatinya.\n\n"
         "Ritme yang ringan membantu — satu jangkar, satu kegiatan keluar, satu rentang "
         "yang benar-benar bebas. Struktur dan istirahat bukan lawan; istirahat butuh "
         "sedikit struktur untuk bertahan."),
        ("Protecting one unstructured stretch is as deliberate an act as booking an "
         "activity, and usually more valuable.",
         "Melindungi satu rentang waktu tanpa acara sama disengajanya dengan memesan "
         "kegiatan, dan biasanya lebih berharga."),
        ("Name your one weekend anchor and one protected empty stretch.",
         "Sebutkan satu jangkar akhir pekan Anda dan satu rentang kosong yang dilindungi."),
        ("Do we come back from weekends more rested or less?",
         "Apakah kami pulang dari akhir pekan lebih segar atau kurang?"),
        ("\"This bit of Sunday isn't for anything.\"",
         "\"Bagian hari Minggu ini tidak untuk apa-apa.\""),
    ),
    198: d(
        ("Travel routines",
         "Rutinitas saat bepergian"),
        ("Travel removes almost every structure a child relies on at once — bed, food "
         "times, familiar space, predictable order.\n\n"
         "Carrying a few anchors with you does most of the work: the same bedtime "
         "sequence, the same comfort object, roughly the same meal times. Everything else "
         "can move.",
         "Bepergian menghapus hampir semua struktur yang diandalkan anak sekaligus — tempat "
         "tidur, jam makan, ruang yang dikenal, urutan yang bisa ditebak.\n\n"
         "Membawa beberapa jangkar bersama Anda sudah melakukan sebagian besar pekerjaannya: "
         "urutan waktu tidur yang sama, benda kesayangan yang sama, jam makan yang kira-kira "
         "sama. Selebihnya boleh bergeser."),
        ("Lower your behavioural expectations for travel days in advance. A tired child in "
         "an unfamiliar place is not the child you know.",
         "Turunkan harapan perilaku Anda untuk hari perjalanan sejak awal. Anak yang lelah "
         "di tempat asing bukan anak yang Anda kenal."),
        ("Name the two anchors you will carry into your next trip.",
         "Sebutkan dua jangkar yang akan Anda bawa dalam perjalanan berikutnya."),
        ("Which routines matter enough to travel with us?",
         "Rutinitas mana yang cukup penting untuk ikut bepergian bersama kami?"),
        ("\"Different place, same bedtime song.\"",
         "\"Tempat berbeda, lagu tidurnya sama.\""),
    ),
    199: d(
        ("Routines during illness",
         "Rutinitas saat sakit"),
        ("Illness suspends the rules, and it should. A sick child needs comfort, not "
         "consistency, and the household briefly reorganises around them.\n\n"
         "The difficulty comes afterwards. Returning to normal needs naming out loud, or "
         "the temporary arrangements quietly become permanent ones.",
         "Sakit menangguhkan aturan, dan memang seharusnya begitu. Anak yang sakit butuh "
         "penghiburan, bukan konsistensi, dan rumah tangga sejenak menata ulang dirinya di "
         "sekelilingnya.\n\n"
         "Kesulitannya datang sesudahnya. Kembali ke normal perlu disebutkan dengan lantang, "
         "atau pengaturan sementara diam-diam menjadi permanen."),
        ("\"You're better now, so tonight we go back to the usual bedtime\" is a small "
         "sentence that prevents a fortnight of confusion.",
         "\"Kamu sudah sembuh, jadi malam ini kita kembali ke jam tidur biasa\" adalah "
         "kalimat kecil yang mencegah dua minggu kebingungan."),
        ("Name the return to normal out loud the next time someone recovers.",
         "Sebutkan dengan lantang saat kembali ke normal, lain kali ada yang sembuh."),
        ("What did we start during an illness that never stopped?",
         "Apa yang kami mulai saat sakit dan tak pernah berhenti?"),
        ("\"You're well now — back to the usual tonight.\"",
         "\"Kamu sudah sehat — malam ini kembali seperti biasa.\""),
    ),
    200: d(
        ("Routines during holidays",
         "Rutinitas saat liburan"),
        ("Holidays are meant to loosen structure, and they should. But total collapse of "
         "routine tends to produce increasingly difficult children by about day four.\n\n"
         "Keep two anchors — roughly consistent sleep and roughly consistent meals — and "
         "let everything else go. That is usually enough to keep a holiday enjoyable.",
         "Liburan memang untuk mengendurkan struktur, dan seharusnya begitu. Tapi runtuhnya "
         "rutinitas sepenuhnya cenderung menghasilkan anak yang makin sulit sekitar hari keempat.\n\n"
         "Pertahankan dua jangkar — tidur yang kira-kira konsisten dan makan yang kira-kira "
         "konsisten — dan lepaskan selebihnya. Itu biasanya cukup untuk menjaga liburan tetap menyenangkan."),
        ("The fourth day of a holiday is where most families discover which routines were "
         "actually load-bearing.",
         "Hari keempat liburan adalah saat kebanyakan keluarga menemukan rutinitas mana yang "
         "ternyata menopang segalanya."),
        ("Choose your two holiday anchors before the next break begins.",
         "Pilih dua jangkar liburan Anda sebelum liburan berikutnya dimulai."),
        ("Which routines do we need even on holiday?",
         "Rutinitas mana yang tetap kami butuhkan bahkan saat liburan?"),
        ("\"Late is fine — but bed is still bed.\"",
         "\"Boleh agak malam — tapi tidur tetap tidur.\""),
    ),
    201: d(
        ("Managing unpredictability",
         "Mengelola hal yang tak terduga"),
        ("Some seasons cannot be made predictable — shift work, illness, a new baby, "
         "financial stress. Pretending otherwise sets a family up to fail.\n\n"
         "When the week cannot be predictable, make one thing predictable. A single fixed "
         "point that survives everything gives a child something to hold onto.",
         "Sebagian musim memang tak bisa dibuat bisa ditebak — kerja bergilir, sakit, bayi "
         "baru, tekanan keuangan. Berpura-pura sebaliknya menyiapkan keluarga untuk gagal.\n\n"
         "Ketika minggunya tak bisa ditebak, buat satu hal bisa ditebak. Satu titik tetap "
         "yang bertahan melewati segalanya memberi anak sesuatu untuk dipegang."),
        ("It does not have to be big. The same song at bedtime, whoever is doing it, is "
         "enough to anchor a chaotic week.",
         "Tak harus besar. Lagu yang sama menjelang tidur, siapa pun yang menyanyikannya, "
         "sudah cukup menjadi jangkar minggu yang kacau."),
        ("Choose one thing that will happen this week no matter what.",
         "Pilih satu hal yang akan terjadi minggu ini apa pun yang terjadi."),
        ("What is the one fixed point my child can count on?",
         "Apa satu titik tetap yang bisa anak saya andalkan?"),
        ("\"Whatever else happens, we always do this.\"",
         "\"Apa pun yang terjadi, kita selalu melakukan ini.\""),
    ),
    202: d(
        ("Rituals that create belonging",
         "Ritual yang menciptakan rasa memiliki"),
        ("A routine organises the day; a ritual says who we are. The difference is meaning "
         "rather than function — and children remember rituals long after they have "
         "forgotten schedules.\n\n"
         "The smallest repeated things carry the most: a particular Saturday breakfast, a "
         "phrase said at the door, a song only your family sings.",
         "Rutinitas menata hari; ritual menyatakan siapa kita. Bedanya adalah makna, bukan "
         "fungsi — dan anak mengingat ritual jauh setelah mereka lupa jadwal.\n\n"
         "Hal kecil yang paling sering diulang membawa paling banyak makna: sarapan Sabtu "
         "tertentu, kalimat yang diucapkan di pintu, lagu yang hanya keluarga Anda nyanyikan."),
        ("Ask an adult what they remember about their childhood home and you will almost "
         "always get a ritual, never a schedule.",
         "Tanyakan pada orang dewasa apa yang dia ingat tentang rumah masa kecilnya, dan "
         "Anda hampir selalu mendapat sebuah ritual, tak pernah sebuah jadwal."),
        ("Name one thing your family already does that is a ritual, and say so out loud.",
         "Sebutkan satu hal yang sudah keluarga Anda lakukan yang merupakan ritual, dan katakan dengan lantang."),
        ("What will my child remember that we always did?",
         "Apa yang akan anak saya ingat sebagai hal yang selalu kami lakukan?"),
        ("\"This is a thing our family does.\"",
         "\"Ini hal yang keluarga kita lakukan.\""),
    ),
    203: d(
        ("Story time as attachment ritual",
         "Waktu cerita sebagai ritual kelekatan"),
        ("Reading together does far more than build literacy. It is proximity, undivided "
         "attention, a predictable ending to the day, and a shared world — all in fifteen "
         "minutes.\n\n"
         "It is also one of the few rituals that survives into older childhood if you let "
         "it. Children who are read to at nine still want it at eleven, if nobody declares "
         "them too old.",
         "Membaca bersama jauh lebih dari sekadar membangun literasi. Ia adalah kedekatan, "
         "perhatian penuh, akhir hari yang bisa ditebak, dan dunia bersama — semuanya dalam "
         "lima belas menit.\n\n"
         "Ia juga salah satu dari sedikit ritual yang bertahan sampai usia lebih besar jika "
         "Anda membiarkannya. Anak yang dibacakan di usia sembilan tahun masih menginginkannya "
         "di usia sebelas, jika tak ada yang menyatakan dia sudah terlalu besar."),
        ("Being read to remains enjoyable well past the age a child can read alone. Reading "
         "ability and wanting closeness are unrelated.",
         "Dibacakan tetap menyenangkan jauh setelah usia anak bisa membaca sendiri. Kemampuan "
         "membaca dan keinginan akan kedekatan tidak berhubungan."),
        ("Read something aloud today, even to a child who can read perfectly well.",
         "Bacakan sesuatu dengan suara hari ini, bahkan kepada anak yang sudah lancar membaca."),
        ("When did we stop reading together, and why?",
         "Kapan kami berhenti membaca bersama, dan mengapa?"),
        ("\"One chapter. Come sit.\"",
         "\"Satu bab saja. Sini duduk.\""),
    ),
    204: d(
        ("Family values ritual",
         "Ritual nilai keluarga"),
        ("Values transmit through repetition, not announcement. A short regular moment — "
         "prayer, reflection, a gratitude round, a values sentence — does more than any "
         "single conversation about what matters.\n\n"
         "Whatever form fits your family, the requirements are the same: short, regular, "
         "and genuinely meant by the adults.",
         "Nilai diwariskan lewat pengulangan, bukan pengumuman. Momen singkat yang rutin — "
         "doa, refleksi, putaran rasa syukur, satu kalimat nilai — lebih berpengaruh "
         "daripada percakapan tunggal apa pun tentang apa yang penting.\n\n"
         "Bentuk apa pun yang cocok untuk keluarga Anda, syaratnya sama: singkat, rutin, dan "
         "sungguh-sungguh dimaksudkan oleh orang dewasanya."),
        ("Children detect performed values instantly. A ritual the adults do not mean "
         "teaches cynicism rather than the value.",
         "Anak langsung mendeteksi nilai yang cuma dipertunjukkan. Ritual yang tidak "
         "disungguhi orang dewasanya mengajarkan sinisme, bukan nilainya."),
        ("Hold one short values moment today in whatever form fits your family.",
         "Adakan satu momen nilai yang singkat hari ini dalam bentuk apa pun yang cocok untuk keluarga Anda."),
        ("How do our values actually get passed on, in practice?",
         "Bagaimana sebenarnya nilai-nilai kami diwariskan, dalam praktik?"),
        ("\"In our family, this is what we believe.\"",
         "\"Di keluarga kita, inilah yang kita yakini.\""),
    ),
    205: d(
        ("Gratitude rituals",
         "Ritual rasa syukur"),
        ("Gratitude practised regularly shifts what a family notices. It is not about "
         "denying difficulty — it is about widening attention so the good is not "
         "invisible.\n\n"
         "It must be specific to work. \"Thankful for my family\" is a habit of speech; "
         "\"thankful that you waited for me today\" is a habit of attention.",
         "Rasa syukur yang dilatih secara rutin menggeser apa yang diperhatikan sebuah "
         "keluarga. Ini bukan menyangkal kesulitan — ini melebarkan perhatian agar yang baik "
         "tidak menjadi tak terlihat.\n\n"
         "Ia harus spesifik agar berhasil. \"Bersyukur atas keluargaku\" adalah kebiasaan "
         "berbicara; \"bersyukur kamu menungguku hari ini\" adalah kebiasaan memperhatikan."),
        ("Specific gratitude also teaches children to notice each other, which is a "
         "quieter and more lasting gift.",
         "Rasa syukur yang spesifik juga mengajarkan anak memperhatikan satu sama lain — "
         "hadiah yang lebih sunyi dan lebih bertahan."),
        ("Say one specific thank-you to each person in your house today.",
         "Ucapkan satu terima kasih yang spesifik kepada setiap orang di rumah Anda hari ini."),
        ("What do we notice most in this house — what is missing or what is here?",
         "Apa yang paling kami perhatikan di rumah ini — yang kurang atau yang ada?"),
        ("\"I noticed you did that. Thank you.\"",
         "\"Mama/Papa lihat kamu melakukannya. Terima kasih.\""),
    ),
    206: d(
        ("One-on-one time routine",
         "Rutinitas waktu berdua"),
        ("Ten minutes of undivided, child-led time does more for behaviour than most "
         "consequences. It is short enough to be sustainable and specific enough to be felt.\n\n"
         "The rules are simple and hard: phone away, child chooses, no teaching, no "
         "correcting, no improving what they are doing. Just be with them.",
         "Sepuluh menit waktu penuh yang dipimpin anak lebih berpengaruh pada perilaku "
         "daripada kebanyakan konsekuensi. Cukup singkat untuk berkelanjutan dan cukup "
         "spesifik untuk terasa.\n\n"
         "Aturannya sederhana dan sulit: ponsel disimpan, anak yang memilih, tidak "
         "mengajari, tidak menegur, tidak memperbaiki apa yang sedang dia lakukan. Cukup "
         "hadir bersamanya."),
        ("Most parents find the no-teaching rule the hardest. Resisting the urge to improve "
         "the play is most of the exercise.",
         "Kebanyakan orang tua merasa aturan tidak-mengajari paling sulit. Menahan dorongan "
         "memperbaiki permainannya adalah sebagian besar latihannya."),
        ("Give ten child-led minutes today, with no teaching in them at all.",
         "Berikan sepuluh menit yang dipimpin anak hari ini, tanpa mengajari sama sekali."),
        ("When did I last spend ten minutes with my child improving nothing?",
         "Kapan terakhir saya menghabiskan sepuluh menit bersama anak tanpa memperbaiki apa pun?"),
        ("\"Ten minutes, and you're in charge.\"",
         "\"Sepuluh menit, dan kamu yang memimpin.\""),
    ),
    207: d(
        ("Sibling connection rituals",
         "Ritual kedekatan antar saudara"),
        ("Sibling relationships are usually managed reactively — parents intervene in "
         "conflict and leave the rest alone. That means the relationship is mostly "
         "practised in its worst moments.\n\n"
         "Deliberately building good shared moments changes the balance: a job they do "
         "together, a game only they play, a small responsibility they share.",
         "Hubungan antar saudara biasanya dikelola secara reaktif — orang tua turun tangan "
         "saat konflik dan membiarkan sisanya. Artinya hubungan itu sebagian besar dilatih "
         "di momen-momen terburuknya.\n\n"
         "Dengan sengaja membangun momen bersama yang baik mengubah keseimbangannya: satu "
         "tugas yang mereka kerjakan bersama, permainan yang hanya mereka mainkan, tanggung "
         "jawab kecil yang mereka bagi."),
        ("Give siblings something to be on the same side of. Shared tasks build alliance "
         "faster than any lecture about being kind to each other.",
         "Beri saudara sesuatu yang membuat mereka berada di pihak yang sama. Tugas bersama "
         "membangun persekutuan lebih cepat daripada ceramah apa pun tentang saling menyayangi."),
        ("Give your children one small shared job today.",
         "Beri anak-anak Anda satu tugas bersama yang kecil hari ini."),
        ("Do my children have anything they do well together?",
         "Apakah anak-anak saya punya sesuatu yang mereka lakukan bersama dengan baik?"),
        ("\"This one's a two-person job.\"",
         "\"Yang ini pekerjaan untuk dua orang.\""),
    ),
    208: d(
        ("Decluttering family commitments",
         "Merapikan komitmen keluarga"),
        ("Family calendars fill by accretion — each commitment reasonable on its own, the "
         "total quietly unsustainable. Nobody ever decides to be this busy.\n\n"
         "Reviewing the calendar as a whole, rather than one request at a time, is the "
         "only way to see the real load. Then something has to come off.",
         "Kalender keluarga terisi lewat penumpukan — setiap komitmen masuk akal sendiri, "
         "totalnya diam-diam tak sanggup ditanggung. Tak ada yang pernah memutuskan untuk "
         "sesibuk ini.\n\n"
         "Meninjau kalender secara utuh, bukan satu permintaan pada satu waktu, adalah "
         "satu-satunya cara melihat beban yang sebenarnya. Lalu sesuatu harus dilepas."),
        ("Ask the children too. They often name the activity they would drop, and are "
         "rarely asked.",
         "Tanyakan juga pada anak-anak. Mereka sering bisa menyebut kegiatan yang ingin "
         "mereka lepas, dan jarang ditanya."),
        ("Look at the whole week's commitments and name one to remove.",
         "Lihat seluruh komitmen minggu ini dan sebutkan satu yang akan dihapus."),
        ("Did we choose this schedule, or did it accumulate?",
         "Apakah kami memilih jadwal ini, atau ia menumpuk sendiri?"),
        ("\"What would you drop, if you could drop one?\"",
         "\"Kalau boleh melepas satu, kamu mau lepas yang mana?\""),
    ),
    209: d(
        ("Saying no to over-scheduling",
         "Berkata tidak pada jadwal berlebih"),
        ("Every yes to an activity is a no to unstructured time, and unstructured time is "
         "where imagination, rest and sibling relationships actually happen.\n\n"
         "Enrichment has diminishing returns. A child with three activities and no free "
         "afternoons is usually worse off than a child with one and several.",
         "Setiap ya untuk satu kegiatan adalah tidak untuk waktu bebas, dan di waktu bebas "
         "itulah imajinasi, istirahat, dan hubungan antar saudara sesungguhnya terjadi.\n\n"
         "Pengayaan punya hasil yang makin menurun. Anak dengan tiga kegiatan dan tanpa sore "
         "yang kosong biasanya lebih rugi daripada anak dengan satu kegiatan dan beberapa sore kosong."),
        ("The fear of a child falling behind drives most over-scheduling. Rested children "
         "with time to play rarely fall behind at anything that matters.",
         "Ketakutan anak tertinggal mendorong sebagian besar penjadwalan berlebih. Anak yang "
         "cukup istirahat dan punya waktu bermain jarang tertinggal dalam hal yang penting."),
        ("Say no to one addition this week, and protect the empty time it would have taken.",
         "Katakan tidak pada satu tambahan minggu ini, dan lindungi waktu kosong yang akan diambilnya."),
        ("What am I afraid will happen if my child does less?",
         "Apa yang saya takutkan akan terjadi jika anak saya melakukan lebih sedikit?"),
        ("\"Not this term. We've got enough on.\"",
         "\"Semester ini tidak dulu. Kegiatan kita sudah cukup.\""),
    ),
    210: d(
        ("Weekly reflection",
         "Refleksi mingguan"),
        ("This chapter makes one claim: a large share of what looks like misbehaviour is a "
         "system problem in disguise, and systems can be redesigned without any conflict "
         "at all.\n\n"
         "Look back across the month and find the single moment that still goes wrong most "
         "often. Ask honestly whether it is a behaviour problem or a design problem — and "
         "most of the time, it is design.",
         "Bab ini menyatakan satu hal: sebagian besar yang tampak seperti kenakalan "
         "sebenarnya masalah sistem yang menyamar, dan sistem bisa dirancang ulang tanpa "
         "konflik sama sekali.\n\n"
         "Tengok kembali bulan ini dan temukan satu momen yang masih paling sering berantakan. "
         "Tanyakan dengan jujur apakah itu masalah perilaku atau masalah desain — dan "
         "sebagian besar waktu, itu desain."),
        ("Tool 7 in the toolkit, the Friction-Point Redesigner, is built for exactly this "
         "one question.",
         "Alat 7 dalam toolkit, Pemetaan Titik Gesekan, dibuat persis untuk satu pertanyaan ini."),
        ("Take your worst remaining moment and redesign it rather than disciplining it.",
         "Ambil momen tersulit yang tersisa dan rancang ulang, bukan didisiplinkan."),
        ("Which of my discipline problems is actually a design problem?",
         "Masalah disiplin saya yang mana yang sebenarnya masalah desain?"),
        ("\"Let's change the setup, not the child.\"",
         "\"Ayo ubah penataannya, bukan anaknya.\""),
    ),
    211: d(
        ("Family systems review",
         "Tinjauan sistem keluarga"),
        ("Step back from individual moments and look at the household as a system. Where "
         "does the day reliably jam? Who carries more than their share? What has everyone "
         "quietly accepted that nobody actually chose?\n\n"
         "Most families run on arrangements that were never decided. Naming them is what "
         "makes them changeable.",
         "Mundurlah dari momen-momen tunggal dan lihat rumah tangga sebagai sebuah sistem. "
         "Di mana hari itu selalu macet? Siapa yang memikul lebih dari bagiannya? Apa yang "
         "diam-diam diterima semua orang padahal tak ada yang benar-benar memilihnya?\n\n"
         "Kebanyakan keluarga berjalan di atas pengaturan yang tak pernah diputuskan. "
         "Menamainya itulah yang membuatnya bisa diubah."),
        ("The division of household load is worth looking at honestly here. Resentment "
         "about it leaks into parenting more than most couples realise.",
         "Pembagian beban rumah tangga layak ditengok dengan jujur di sini. Dendam soal itu "
         "merembes ke dalam pengasuhan lebih banyak daripada yang disadari kebanyakan pasangan."),
        ("Name one arrangement in your home nobody actually chose, and decide it properly.",
         "Sebutkan satu pengaturan di rumah Anda yang tak pernah benar-benar dipilih siapa pun, "
         "dan putuskan dengan semestinya."),
        ("What does our household run on that we never agreed?",
         "Rumah tangga kami berjalan di atas apa yang sebenarnya tak pernah kami sepakati?"),
        ("\"Can we decide this one on purpose?\"",
         "\"Bisa kita putuskan yang ini dengan sengaja?\""),
    ),
}
