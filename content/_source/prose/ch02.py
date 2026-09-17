# Chapter 2 — Child Development Basics (days 32-61)
#
# Grounded in the founder's guidebook chapter 2 ("Most 'bad behavior' is
# developmental, not moral") and toolkit tool 2 (Behavior Reframe Card).
#
# Through-line: read behaviour as capacity, not character.

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
    f = lambda p: {"en": p[0], "id": p[1]}
    return {
        "title": f(title),
        "note": f(note),
        "entries": [
            {"name": f(n), "tags": [f(t) for t in tags], "looksLike": f(l), "outcome": f(o)}
            for (n, tags, l, o) in entries
        ],
    }


DAYS = {
    32: d(
        ("Brain development in children",
         "Perkembangan otak anak"),
        ("A child's brain is not a small adult brain. It is built from the bottom up: "
         "the survival and emotion systems come online early, and the part that plans, "
         "waits and reasons keeps building well into the twenties.\n\n"
         "This single fact reframes most of parenting. When a child melts down, the "
         "upstairs brain has gone offline and the downstairs brain is driving. You "
         "cannot reason with a part of the brain that is not currently receiving "
         "visitors — you can only help it come back online.",
         "Otak anak bukan otak dewasa versi kecil. Ia dibangun dari bawah ke atas: "
         "sistem bertahan hidup dan emosi aktif lebih dulu, sementara bagian yang "
         "merencanakan, menunggu, dan menalar terus terbangun hingga usia dua puluhan.\n\n"
         "Satu fakta ini mengubah cara pandang atas sebagian besar pengasuhan. Saat anak "
         "meledak, otak bagian atas sedang tidak aktif dan otak bagian bawah yang "
         "menyetir. Anda tak bisa berdebat dengan bagian otak yang sedang tidak menerima "
         "tamu — Anda hanya bisa membantunya kembali menyala."),
        ("Explaining why hitting is wrong to a screaming four-year-old is like sending a "
         "letter to an address nobody is home at. Calm first, teach second.",
         "Menjelaskan mengapa memukul itu salah kepada anak empat tahun yang menjerit "
         "seperti mengirim surat ke rumah yang sedang kosong. Tenangkan dulu, ajarkan kemudian."),
        ("The next time your child is flooded, say nothing instructive until they are "
         "calm. Teach afterwards.",
         "Lain kali anak Anda kewalahan, jangan katakan apa pun yang bersifat mengajari "
         "sampai dia tenang. Ajarkan setelahnya."),
        ("How often do I try to teach at exactly the moment my child cannot learn?",
         "Seberapa sering saya mencoba mengajar tepat di saat anak tidak bisa belajar?"),
        ("\"Let's get calm first. We'll talk after.\"",
         "\"Kita tenang dulu. Nanti kita bicara.\""),
    ),
    33: d(
        ("Executive function basics",
         "Dasar fungsi eksekutif"),
        ("Executive function is the set of mental skills behind almost everything we ask "
         "children to do: holding an instruction in mind, resisting an impulse, "
         "switching tasks, planning ahead. It is a slow-growing system, and it is the "
         "first thing to collapse under tiredness, hunger or stress.\n\n"
         "Much of what looks like not listening is actually a working-memory limit. A "
         "child asked to do four things has usually retained one.",
         "Fungsi eksekutif adalah kumpulan keterampilan mental di balik hampir semua yang "
         "kita minta dari anak: menahan instruksi dalam pikiran, menahan dorongan, "
         "berpindah tugas, merencanakan. Ia sistem yang tumbuh perlahan, dan yang pertama "
         "runtuh saat lelah, lapar, atau stres.\n\n"
         "Banyak hal yang tampak seperti tidak mendengarkan sebenarnya adalah batas memori "
         "kerja. Anak yang diminta melakukan empat hal biasanya hanya menyimpan satu."),
        ("\"Go upstairs, get your socks, brush your teeth and bring your bag down\" "
         "reliably produces a child standing upstairs holding one sock.",
         "\"Naik ke atas, ambil kaus kaki, sikat gigi, lalu bawa turun tasmu\" hampir "
         "selalu menghasilkan anak yang berdiri di atas sambil memegang satu kaus kaki."),
        ("Give one instruction at a time today. Wait for it to finish before adding the next.",
         "Beri satu instruksi saja hari ini. Tunggu sampai selesai sebelum menambah berikutnya."),
        ("Am I asking for more steps than my child can currently hold in mind?",
         "Apakah saya meminta lebih banyak langkah daripada yang bisa anak tampung dalam pikirannya?"),
        ("\"Just the first thing. Come back and I'll tell you the next.\"",
         "\"Yang pertama dulu. Balik lagi, nanti Mama/Papa kasih tahu berikutnya.\""),
    ),
    34: d(
        ("Impulse control develops slowly",
         "Pengendalian dorongan tumbuh perlahan"),
        ("Impulse control is not a decision a child makes; it is a capacity that grows, "
         "unevenly, over roughly two decades. A child who knows a rule perfectly can "
         "still break it seconds later, and both things can be true at once.\n\n"
         "This is why repetition matters more than severity. The lesson is not missing — "
         "the brakes are still being installed.",
         "Pengendalian dorongan bukan keputusan yang diambil anak; ia kemampuan yang "
         "tumbuh, tidak merata, selama kira-kira dua dekade. Anak yang hafal betul sebuah "
         "aturan tetap bisa melanggarnya beberapa detik kemudian, dan kedua hal itu bisa "
         "benar bersamaan.\n\n"
         "Karena itulah pengulangan lebih penting daripada kerasnya hukuman. Pelajarannya "
         "tidak hilang — remnya yang masih dipasang."),
        ("\"You KNEW not to do that!\" is usually true and usually beside the point. "
         "Knowing and stopping are two different systems.",
         "\"Kamu TAHU itu tidak boleh!\" biasanya benar, dan biasanya tidak relevan. "
         "Mengetahui dan menahan diri adalah dua sistem yang berbeda."),
        ("Repeat one rule calmly today without adding frustration that your child already "
         "knows it.",
         "Ulangi satu aturan dengan tenang hari ini tanpa menambahkan kekesalan bahwa anak "
         "sudah tahu."),
        ("Do I treat a repeated mistake as defiance when it may just be an unfinished skill?",
         "Apakah saya menganggap kesalahan berulang sebagai pembangkangan, padahal mungkin "
         "keterampilan yang belum selesai?"),
        ("\"I know you know. It's still hard, and that's okay.\"",
         "\"Mama/Papa tahu kamu tahu. Tetap sulit, dan itu wajar.\""),
    ),
    35: d(
        ("Emotional development stages",
         "Tahap perkembangan emosi"),
        ("Feelings arrive long before the words for them. A toddler feels envy without "
         "any name for it; a six-year-old can name sad but not disappointed; a teenager "
         "can name it precisely and still be swamped by it.\n\n"
         "Emotional development is not about feeling less. It is about the growing "
         "distance between having a feeling and being run by it — and that distance is "
         "built mostly by having feelings received calmly by an adult.",
         "Perasaan datang jauh sebelum kata-kata untuknya. Balita merasa iri tanpa nama "
         "untuk rasa itu; anak enam tahun bisa menyebut sedih tapi belum kecewa; remaja "
         "bisa menyebutnya persis dan tetap tenggelam di dalamnya.\n\n"
         "Perkembangan emosi bukan soal merasa lebih sedikit. Ia soal jarak yang tumbuh "
         "antara memiliki perasaan dan dikendalikan olehnya — dan jarak itu terbangun "
         "terutama dengan perasaan yang diterima dengan tenang oleh orang dewasa."),
        ("The child who screams \"I HATE YOU\" is not making a considered statement. They "
         "are using the biggest word available for a feeling too big for their vocabulary.",
         "Anak yang menjerit \"AKU BENCI MAMA\" tidak sedang membuat pernyataan yang "
         "dipikirkan. Dia memakai kata terbesar yang dia punya untuk perasaan yang terlalu "
         "besar bagi kosakatanya."),
        ("Give one feeling its correct name for your child today, and leave it there.",
         "Berikan satu perasaan nama yang tepat untuk anak hari ini, dan biarkan begitu saja."),
        ("Which feelings does my child have no words for yet?",
         "Perasaan apa yang belum punya kata bagi anak saya?"),
        ("\"That looks like disappointment. Is that close?\"",
         "\"Sepertinya itu kecewa. Mendekati, ya?\""),
    ),
    36: d(
        ("Language and behavior",
         "Bahasa dan perilaku"),
        ("Behaviour fills the space language cannot yet reach. A child who lacks the "
         "words for \"I need help and I feel stupid\" will often throw the book instead. "
         "The throwing is the sentence.\n\n"
         "As vocabulary grows, behaviour usually settles — which is why giving a child "
         "words is one of the most practical discipline strategies there is.",
         "Perilaku mengisi ruang yang belum terjangkau bahasa. Anak yang tak punya kata "
         "untuk \"aku butuh bantuan dan aku merasa bodoh\" sering melempar bukunya. "
         "Lemparan itulah kalimatnya.\n\n"
         "Seiring kosakata bertumbuh, perilaku biasanya mereda — itulah sebabnya memberi "
         "anak kata-kata adalah salah satu strategi disiplin paling praktis yang ada."),
        ("Handing a child the sentence they could not find — \"this is too hard and I "
         "want to give up\" — often ends the behaviour on the spot.",
         "Memberikan kalimat yang tak bisa anak temukan — \"ini terlalu sulit dan aku "
         "ingin menyerah\" — sering langsung menghentikan perilakunya."),
        ("When behaviour appears today, offer the words for it before responding to it.",
         "Saat perilaku muncul hari ini, tawarkan kata-katanya dulu sebelum menanggapinya."),
        ("What might my child be saying with behaviour because they lack the sentence?",
         "Apa yang mungkin anak sampaikan lewat perilaku karena dia tak punya kalimatnya?"),
        ("\"I think you're trying to tell me something. Let me try.\"",
         "\"Sepertinya kamu sedang ingin menyampaikan sesuatu. Mama/Papa coba tebak, ya.\""),
    ),
    37: d(
        ("Why toddlers say no",
         "Mengapa balita berkata tidak"),
        ("Around two, a child discovers they are a separate person with their own will. "
         "\"No\" is the first tool for testing that discovery, and it gets used on "
         "everything, including things they actually want.\n\n"
         "This is developmental progress, not rudeness. The task is not to crush the no "
         "but to keep it from running the household — usually by offering small, real "
         "choices inside your limits.",
         "Sekitar usia dua tahun, anak menemukan bahwa dirinya adalah pribadi terpisah "
         "dengan kehendaknya sendiri. \"Tidak\" adalah alat pertama untuk menguji penemuan "
         "itu, dan dipakai untuk segalanya, termasuk hal yang sebenarnya dia inginkan.\n\n"
         "Ini kemajuan perkembangan, bukan kekurangajaran. Tugasnya bukan menghancurkan "
         "kata tidak, melainkan menjaganya agar tak mengendalikan rumah — biasanya dengan "
         "menawarkan pilihan kecil yang nyata di dalam batas Anda."),
        ("\"Do you want to put your shoes on?\" invites a no. \"Red shoes or blue shoes?\" "
         "keeps the limit and hands over the part that can safely be handed over.",
         "\"Mau pakai sepatu?\" mengundang jawaban tidak. \"Sepatu merah atau biru?\" "
         "menjaga batasnya dan menyerahkan bagian yang memang aman diserahkan."),
        ("Convert one instruction today into a choice between two acceptable options.",
         "Ubah satu instruksi hari ini menjadi pilihan antara dua opsi yang sama-sama Anda terima."),
        ("Where could I hand my child a small real choice without losing the limit?",
         "Di mana saya bisa memberi anak pilihan kecil yang nyata tanpa kehilangan batasnya?"),
        ("\"This one or that one — you choose.\"",
         "\"Yang ini atau yang itu — kamu yang pilih.\""),
    ),
    38: d(
        ("Preschool imagination and fear",
         "Imajinasi dan ketakutan anak prasekolah"),
        ("Preschool imagination is powerful and not yet fenced off from reality. The same "
         "mind that invents wonderful games invents convincing monsters, and the child "
         "cannot reliably tell you which is which.\n\n"
         "Arguing that a fear is illogical does not help, because the fear was never "
         "built by logic. Comfort and a small ritual of control work far better.",
         "Imajinasi anak prasekolah sangat kuat dan belum berpagar dari kenyataan. Pikiran "
         "yang sama yang menciptakan permainan indah juga menciptakan monster yang "
         "meyakinkan, dan anak belum bisa memilah mana yang mana.\n\n"
         "Berdebat bahwa ketakutan itu tak masuk akal tidak membantu, karena ketakutan itu "
         "memang tidak dibangun oleh logika. Penghiburan dan ritual kecil yang memberi "
         "kendali jauh lebih ampuh."),
        ("\"There are no monsters\" rarely lands. A torch by the bed and a checked "
         "cupboard hands the child a way to manage the fear themselves.",
         "\"Tidak ada monster\" jarang mempan. Senter di samping tempat tidur dan lemari "
         "yang sudah diperiksa memberi anak cara mengelola ketakutannya sendiri."),
        ("Meet one fear today with comfort and a small ritual instead of an argument.",
         "Hadapi satu ketakutan hari ini dengan penghiburan dan ritual kecil, bukan perdebatan."),
        ("Do I try to talk my child out of fear, or help them feel able to face it?",
         "Apakah saya membujuk anak agar tidak takut, atau membantunya merasa sanggup menghadapinya?"),
        ("\"That feels real to you. Let's check it together.\"",
         "\"Buat kamu itu terasa nyata. Ayo kita periksa bersama.\""),
    ),
    39: d(
        ("School-age fairness sensitivity",
         "Kepekaan anak usia sekolah terhadap keadilan"),
        ("Somewhere around six or seven, fairness becomes enormous. Children start "
         "tracking who got more, who went first, who was believed. This is genuine moral "
         "development, and it is also exhausting.\n\n"
         "Fairness at this age means identical. It takes years to grow into the more "
         "useful version — fair means each person gets what they need.",
         "Sekitar usia enam atau tujuh tahun, keadilan menjadi hal yang besar. Anak mulai "
         "mencatat siapa dapat lebih banyak, siapa duluan, siapa yang dipercaya. Ini "
         "perkembangan moral yang sungguh, dan sekaligus melelahkan.\n\n"
         "Adil di usia ini berarti sama persis. Butuh bertahun-tahun untuk tumbuh ke versi "
         "yang lebih berguna — adil berarti setiap orang mendapat apa yang dia butuhkan."),
        ("Measuring the juice to the millimetre teaches that identical is the standard. "
         "\"You each get what you need\" teaches something they will use for life.",
         "Mengukur jus sampai milimeter mengajarkan bahwa sama persis adalah standarnya. "
         "\"Kalian masing-masing dapat sesuai kebutuhan\" mengajarkan sesuatu yang dipakai seumur hidup."),
        ("Answer one fairness complaint today with need rather than measurement.",
         "Jawab satu keluhan soal keadilan hari ini dengan kebutuhan, bukan dengan ukuran."),
        ("Am I teaching my children that fair means identical?",
         "Apakah saya mengajarkan anak bahwa adil berarti sama persis?"),
        ("\"Not the same — but each of you gets what you need.\"",
         "\"Tidak sama — tapi kalian masing-masing dapat yang dibutuhkan.\""),
    ),
    40: d(
        ("Adolescents and autonomy",
         "Remaja dan otonomi"),
        ("Adolescence is not a malfunction; it is the developmental job of becoming a "
         "separate person. Pushing away is how that work gets done, and it is aimed at "
         "the role of parent rather than at you.\n\n"
         "The parents who keep influence in these years are usually not the strictest. "
         "They are the ones who let go of the small things early enough to still be "
         "trusted on the large ones.",
         "Masa remaja bukan kerusakan; ia tugas perkembangan untuk menjadi pribadi yang "
         "terpisah. Menjauh adalah cara pekerjaan itu dilakukan, dan sasarannya adalah "
         "peran orang tua, bukan diri Anda.\n\n"
         "Orang tua yang tetap punya pengaruh di tahun-tahun ini biasanya bukan yang "
         "paling ketat. Mereka yang cukup awal melepaskan hal-hal kecil sehingga masih "
         "dipercaya untuk hal-hal besar."),
        ("Fighting over hairstyle spends the credibility you will need for the "
         "conversation about the party, the car and the friend you are worried about.",
         "Bertengkar soal model rambut menghabiskan kredibilitas yang Anda butuhkan untuk "
         "percakapan tentang pesta, kendaraan, dan teman yang Anda khawatirkan."),
        ("Pick one small thing you have been fighting over and hand it to your teenager today.",
         "Pilih satu hal kecil yang selama ini jadi bahan pertengkaran dan serahkan kepada remaja Anda hari ini."),
        ("Which battles am I fighting that cost more than they are worth?",
         "Pertarungan mana yang saya jalani dengan biaya lebih besar daripada nilainya?"),
        ("\"That one's yours to decide.\"",
         "\"Yang itu kamu yang putuskan.\""),
    ),
    41: d(
        ("Sleep and behavior",
         "Tidur dan perilaku"),
        ("Sleep debt looks exactly like a behaviour problem. A tired child is more "
         "impulsive, more emotional, less able to switch tasks and far less able to "
         "recover from small frustrations.\n\n"
         "Before investigating a child's character, check the sleep. It is the single "
         "highest-yield adjustment in family life and the one most often skipped.",
         "Utang tidur tampak persis seperti masalah perilaku. Anak yang lelah lebih "
         "impulsif, lebih emosional, lebih sulit berpindah tugas, dan jauh lebih sulit "
         "pulih dari frustrasi kecil.\n\n"
         "Sebelum menyelidiki karakter anak, periksa tidurnya. Ini penyesuaian dengan "
         "hasil tertinggi dalam kehidupan keluarga, dan yang paling sering dilewatkan."),
        ("A week of earlier bedtimes has resolved more \"behaviour problems\" than most "
         "discipline plans.",
         "Seminggu jam tidur yang lebih awal telah menyelesaikan lebih banyak \"masalah "
         "perilaku\" daripada kebanyakan rencana disiplin."),
        ("Move bedtime fifteen minutes earlier tonight and watch tomorrow evening.",
         "Majukan jam tidur lima belas menit malam ini dan perhatikan besok sore."),
        ("How much of what frustrates me is simply tiredness — mine or theirs?",
         "Seberapa banyak hal yang membuat saya frustrasi sebenarnya hanya kelelahan — saya atau anak?"),
        ("\"I think we're both tired. Let's make tonight easier.\"",
         "\"Sepertinya kita berdua lelah. Malam ini kita permudah saja.\""),
    ),
    42: d(
        ("Hunger and behavior",
         "Lapar dan perilaku"),
        ("Blood sugar drives mood far more than most parents account for. The witching "
         "hour before dinner is not a coincidence of character — it is a small body "
         "running low with no vocabulary for what is wrong.\n\n"
         "Feeding a child before a difficult moment is not indulgence. It is removing a "
         "cause.",
         "Gula darah memengaruhi suasana hati jauh lebih besar daripada yang diperhitungkan "
         "kebanyakan orang tua. Jam-jam sulit menjelang makan malam bukan kebetulan "
         "karakter — itu tubuh kecil yang kehabisan tenaga tanpa kosakata untuk menjelaskannya.\n\n"
         "Memberi anak makan sebelum momen sulit bukan memanjakan. Itu menghapus penyebab."),
        ("A snack at 5pm prevents more conflict than any consequence delivered at 5.15pm.",
         "Camilan pukul lima sore mencegah lebih banyak konflik daripada konsekuensi apa "
         "pun yang diberikan pukul 5.15."),
        ("Feed your child before the hardest hour today rather than during it.",
         "Beri anak makan sebelum jam tersulit hari ini, bukan saat jam itu berlangsung."),
        ("What time of day do things reliably fall apart, and what is missing then?",
         "Jam berapa hal-hal selalu berantakan, dan apa yang sebenarnya kurang saat itu?"),
        ("\"Let's eat something first, then we'll sort this out.\"",
         "\"Makan dulu sedikit, baru kita bereskan ini.\""),
    ),
    43: d(
        ("Sensory overload",
         "Kelebihan rangsang"),
        ("Children vary enormously in how much noise, light, texture and crowding they "
         "can process. A child at their sensory limit behaves like a child being "
         "difficult, but nothing about it is chosen.\n\n"
         "Some children need far more quiet than the household provides, and they cannot "
         "usually tell you so — they can only show you.",
         "Anak sangat berbeda-beda dalam menoleransi kebisingan, cahaya, tekstur, dan "
         "keramaian. Anak yang mencapai batas indranya berperilaku seperti anak yang sedang "
         "menyulitkan, padahal tak ada bagian darinya yang dipilih.\n\n"
         "Sebagian anak butuh jauh lebih banyak ketenangan daripada yang rumah sediakan, "
         "dan biasanya mereka tak bisa mengatakannya — hanya bisa menunjukkannya."),
        ("The child who falls apart at the end of a birthday party is not ungrateful. "
         "They have been processing noise and people for three hours.",
         "Anak yang berantakan di akhir pesta ulang tahun bukan tidak tahu berterima kasih. "
         "Dia sudah memproses kebisingan dan orang selama tiga jam."),
        ("Give one quiet, low-stimulation gap in your child's day today.",
         "Berikan satu jeda tenang dengan rangsang rendah dalam hari anak Anda."),
        ("Does my child get enough quiet, or only enough activity?",
         "Apakah anak saya cukup mendapat ketenangan, atau hanya cukup kegiatan?"),
        ("\"It's loud in here. Let's find somewhere quieter.\"",
         "\"Di sini berisik. Ayo cari tempat yang lebih tenang.\""),
    ),
    44: d(
        ("Transitions are hard for kids",
         "Perpindahan itu sulit bagi anak"),
        ("Most daily conflict clusters at transitions: leaving the house, coming off "
         "screens, ending play, starting bed. Stopping something absorbing requires a "
         "gear-change children are not yet good at.\n\n"
         "Warning is the whole technique. A child given notice can begin the internal "
         "work of letting go; a child given no notice can only protest.",
         "Sebagian besar konflik harian menumpuk di perpindahan: keluar rumah, berhenti "
         "dari layar, mengakhiri permainan, mulai tidur. Menghentikan sesuatu yang "
         "menyerap perhatian butuh pergantian gigi yang belum dikuasai anak.\n\n"
         "Aba-aba adalah seluruh tekniknya. Anak yang diberi tahu bisa memulai kerja batin "
         "untuk melepaskan; anak yang tidak diberi tahu hanya bisa memprotes."),
        ("\"Two more minutes, then shoes\" turns an ambush into a plan, and takes almost "
         "no extra time.",
         "\"Dua menit lagi, lalu pakai sepatu\" mengubah serangan mendadak menjadi rencana, "
         "dan hampir tidak menambah waktu."),
        ("Give a warning before every transition today. Every one.",
         "Beri aba-aba sebelum setiap perpindahan hari ini. Setiap kali."),
        ("Which transition causes the most conflict in our day?",
         "Perpindahan mana yang paling banyak menimbulkan konflik dalam hari kami?"),
        ("\"Two more minutes, then we stop.\"",
         "\"Dua menit lagi, lalu kita berhenti.\""),
    ),
    45: d(
        ("Boredom and behavior",
         "Bosan dan perilaku"),
        ("Boredom is uncomfortable, and an uncomfortable child generates activity — "
         "usually the kind you notice. A great deal of low-level trouble is simply an "
         "under-occupied brain looking for input.\n\n"
         "Boredom is also valuable. It is the raw material of imagination, and a child "
         "who is never bored never learns to generate their own ideas.",
         "Bosan itu tidak nyaman, dan anak yang tidak nyaman menciptakan kegiatan — "
         "biasanya jenis yang Anda sadari. Banyak kekacauan kecil sebenarnya hanyalah otak "
         "yang kurang kerjaan mencari masukan.\n\n"
         "Bosan juga berharga. Ia bahan mentah imajinasi, dan anak yang tak pernah bosan "
         "tak pernah belajar memunculkan gagasannya sendiri."),
        ("The trick is not to eliminate boredom but to stop rescuing from it instantly. "
         "The ten minutes after \"I'm bored\" is where invention happens.",
         "Kuncinya bukan menghapus rasa bosan, tapi berhenti langsung menyelamatkan dari "
         "rasa itu. Sepuluh menit setelah \"aku bosan\" adalah saat penemuan terjadi."),
        ("When your child says they are bored today, wait ten minutes before offering anything.",
         "Saat anak berkata bosan hari ini, tunggu sepuluh menit sebelum menawarkan apa pun."),
        ("Do I fill every empty moment for my child before they can fill it themselves?",
         "Apakah saya mengisi setiap momen kosong anak sebelum dia sempat mengisinya sendiri?"),
        ("\"Being bored is allowed. Something will come to you.\"",
         "\"Boleh kok bosan. Nanti juga ada ide yang datang.\""),
    ),
    46: d(
        ("The need for play",
         "Kebutuhan akan bermain"),
        ("Play is not what children do when the important work is finished. It is how "
         "the important work gets done — negotiation, risk, recovery from losing, trying "
         "on roles, and processing whatever has happened lately.\n\n"
         "A child short on play will usually show it in behaviour, not in words.",
         "Bermain bukan yang anak lakukan setelah pekerjaan penting selesai. Bermain adalah "
         "cara pekerjaan penting itu dikerjakan — bernegosiasi, mengambil risiko, pulih "
         "dari kalah, mencoba berbagai peran, dan mengolah apa pun yang baru terjadi.\n\n"
         "Anak yang kekurangan bermain biasanya menunjukkannya lewat perilaku, bukan lewat kata."),
        ("Watch what a child re-enacts in play after a hard week. It is usually the exact "
         "thing they are trying to digest.",
         "Perhatikan apa yang anak perankan ulang dalam permainan setelah minggu yang berat. "
         "Biasanya persis hal yang sedang dia coba cerna."),
        ("Protect one block of unstructured play today. No instructions, no improving it.",
         "Lindungi satu blok waktu bermain bebas hari ini. Tanpa instruksi, tanpa dibetulkan."),
        ("Does my child get enough play that has no purpose attached to it?",
         "Apakah anak cukup mendapat waktu bermain yang tidak dilekati tujuan apa pun?"),
        ("\"You play. I'll just watch.\"",
         "\"Kamu main saja. Mama/Papa lihat saja.\""),
    ),
    47: d(
        ("Attachment across ages",
         "Kelekatan di berbagai usia"),
        ("The need for a secure base never ends; only its shape changes. A toddler needs "
         "your body, a school-age child needs your attention, a teenager needs your "
         "availability — and each will test that it is still there.\n\n"
         "Teenagers who seem to need you least often need you most; they simply need you "
         "differently, and usually late at night.",
         "Kebutuhan akan rumah aman tidak pernah berakhir; hanya bentuknya yang berubah. "
         "Balita butuh tubuh Anda, anak usia sekolah butuh perhatian Anda, remaja butuh "
         "ketersediaan Anda — dan masing-masing akan menguji apakah itu masih ada.\n\n"
         "Remaja yang tampak paling tidak membutuhkan Anda sering justru paling "
         "membutuhkan; mereka hanya membutuhkan dengan cara berbeda, dan biasanya larut malam."),
        ("The teenager who ignores you all day and then talks at 11pm is not being "
         "inconsistent. That is what availability looks like at that age.",
         "Remaja yang mengabaikan Anda seharian lalu bicara pukul sebelas malam bukan "
         "sedang tidak konsisten. Begitulah rupa ketersediaan di usia itu."),
        ("Be available in the form your child's age actually needs today.",
         "Hadirlah dalam bentuk yang benar-benar dibutuhkan usia anak Anda hari ini."),
        ("Am I still offering the version of closeness my child has outgrown?",
         "Apakah saya masih menawarkan bentuk kedekatan yang sudah tak sesuai usia anak?"),
        ("\"I'm around whenever you want to talk.\"",
         "\"Mama/Papa ada kapan pun kamu mau bicara.\""),
    ),
    48: d(
        ("Separation anxiety",
         "Kecemasan berpisah"),
        ("Separation distress is a sign of attachment working, not of a child being "
         "spoiled. It peaks at predictable ages and returns during change — a new school, "
         "a new sibling, a house move.\n\n"
         "Long goodbyes make it worse; sneaking away makes it much worse. A short, warm, "
         "reliable ritual and a clear promise of return works best.",
         "Kesedihan saat berpisah adalah tanda kelekatan sedang bekerja, bukan tanda anak "
         "dimanja. Ia memuncak di usia-usia yang bisa diperkirakan dan kembali saat ada "
         "perubahan — sekolah baru, adik baru, pindah rumah.\n\n"
         "Perpisahan yang berlarut memperburuknya; pergi diam-diam jauh lebih memperburuk. "
         "Ritual singkat, hangat, dan konsisten dengan janji kembali yang jelas paling ampuh."),
        ("The same three-step goodbye every morning — hug, phrase, wave — outperforms any "
         "amount of reassurance improvised at the door.",
         "Perpisahan tiga langkah yang sama setiap pagi — peluk, kalimat, lambaian — lebih "
         "ampuh daripada penenangan sebanyak apa pun yang diimprovisasi di pintu."),
        ("Build a short goodbye ritual today and use exactly the same one tomorrow.",
         "Bangun ritual perpisahan singkat hari ini dan pakai persis yang sama besok."),
        ("Is my goodbye predictable enough for my child to lean on?",
         "Apakah cara saya berpamitan cukup bisa ditebak untuk jadi pegangan anak?"),
        ("\"Kiss, wave, and I'll be back after snack time.\"",
         "\"Cium, lambai, dan Mama/Papa kembali setelah waktu camilan.\""),
    ),
    49: d(
        ("Sibling rivalry basics",
         "Dasar persaingan saudara"),
        ("Sibling conflict is not a sign of a failing family. It is where children learn "
         "negotiation, repair and the management of envy, in the safest available "
         "laboratory.\n\n"
         "The parenting error that intensifies it most is judging every incident. "
         "Constant refereeing teaches children to compete for your verdict rather than "
         "to solve anything.",
         "Konflik antarsaudara bukan tanda keluarga yang gagal. Di situlah anak belajar "
         "bernegosiasi, memperbaiki, dan mengelola rasa iri, di laboratorium paling aman "
         "yang tersedia.\n\n"
         "Kesalahan pengasuhan yang paling memperparahnya adalah mengadili setiap kejadian. "
         "Terus-menerus menjadi wasit mengajarkan anak bersaing memperebutkan putusan Anda, "
         "bukan menyelesaikan apa pun."),
        ("\"You two work it out; I'll help if it gets unsafe\" builds more skill than any "
         "ruling on who started it.",
         "\"Kalian selesaikan berdua; Mama/Papa bantu kalau sudah tidak aman\" membangun "
         "lebih banyak keterampilan daripada putusan siapa yang mulai."),
        ("Step back from one sibling dispute today unless someone is unsafe.",
         "Mundur dari satu pertengkaran saudara hari ini, kecuali ada yang tidak aman."),
        ("Am I refereeing conflicts my children could learn to settle themselves?",
         "Apakah saya mewasiti konflik yang sebenarnya bisa anak-anak selesaikan sendiri?"),
        ("\"I trust you both to sort this one out.\"",
         "\"Mama/Papa percaya kalian bisa menyelesaikan yang ini.\""),
    ),
    50: d(
        ("Attention-seeking behavior",
         "Perilaku mencari perhatian"),
        ("\"Attention-seeking\" is usually said dismissively, as if attention were a "
         "frivolous thing to want. For a child, attention is a genuine need, and "
         "behaviour is the tool that reliably produces it.\n\n"
         "If difficult behaviour is the only reliable route to your full attention, a "
         "child will keep taking it. The fix is rarely less attention — it is attention "
         "that arrives before the behaviour.",
         "\"Cari perhatian\" biasanya diucapkan dengan nada meremehkan, seolah perhatian "
         "adalah keinginan yang sepele. Bagi anak, perhatian adalah kebutuhan yang "
         "sungguh, dan perilaku adalah alat yang paling andal menghasilkannya.\n\n"
         "Jika perilaku sulit adalah satu-satunya jalan andal menuju perhatian penuh Anda, "
         "anak akan terus menempuhnya. Solusinya jarang mengurangi perhatian — melainkan "
         "perhatian yang datang sebelum perilakunya."),
        ("Ten minutes of undivided attention given freely in the afternoon often removes "
         "the need for an hour of it extracted by trouble at bedtime.",
         "Sepuluh menit perhatian penuh yang diberikan cuma-cuma di sore hari sering "
         "menghapus kebutuhan satu jam perhatian yang dipaksa lewat keributan menjelang tidur."),
        ("Give attention today before it is asked for, at a moment nothing is wrong.",
         "Berikan perhatian hari ini sebelum diminta, di saat tak ada masalah apa pun."),
        ("Is difficult behaviour the most reliable way to get my full attention?",
         "Apakah perilaku sulit adalah cara paling andal mendapatkan perhatian penuh saya?"),
        ("\"I've got ten minutes and they're all yours.\"",
         "\"Mama/Papa punya sepuluh menit dan semuanya buat kamu.\""),
    ),
    51: d(
        ("Emotional flooding",
         "Emosi yang meluap"),
        ("Flooding is the point where feeling overwhelms function. Heart rate climbs, "
         "reasoning drops away, and nothing you say is being processed — in a child or "
         "in you.\n\n"
         "The only useful move is to lower the temperature and wait. Every attempt to "
         "teach during flooding is wasted, and most of it adds fuel.",
         "Meluap adalah titik saat perasaan mengalahkan fungsi. Detak jantung naik, "
         "penalaran menghilang, dan tak ada yang Anda katakan sedang diproses — baik pada "
         "anak maupun pada Anda.\n\n"
         "Satu-satunya langkah berguna adalah menurunkan suhu dan menunggu. Setiap upaya "
         "mengajar saat meluap terbuang percuma, dan sebagian besar justru menambah bahan bakar."),
        ("You can often see the moment it happens — the eyes change and the words stop "
         "working. That is the signal to stop talking, not to talk louder.",
         "Anda sering bisa melihat momen itu terjadi — matanya berubah dan kata-kata "
         "berhenti bekerja. Itu tanda untuk berhenti bicara, bukan bicara lebih keras."),
        ("Spot flooding once today — in your child or yourself — and pause instead of pushing.",
         "Kenali satu kali luapan hari ini — pada anak atau diri Anda — dan berhentilah, "
         "jangan mendesak."),
        ("What does my child look like in the moment before they lose control?",
         "Seperti apa rupa anak saya sesaat sebelum dia kehilangan kendali?"),
        ("\"We'll come back to this when we're both calmer.\"",
         "\"Kita bahas lagi nanti setelah kita berdua lebih tenang.\""),
    ),
    52: d(
        ("Tantrum vs meltdown",
         "Tantrum vs meltdown"),
        ("These look similar and need opposite responses. A tantrum is goal-directed — "
         "there is a want, and the child is still partly in control, often checking "
         "whether it is working. A meltdown is a nervous system overwhelmed; there is no "
         "goal and no control left.\n\n"
         "Tantrums need a calm, unmoved limit. Meltdowns need comfort and less input. "
         "Treating a meltdown as manipulation is one of the most common and most costly "
         "misreadings in parenting.",
         "Keduanya tampak mirip dan membutuhkan respons yang berlawanan. Tantrum punya "
         "tujuan — ada yang diinginkan, dan anak masih sebagian memegang kendali, sering "
         "mengecek apakah caranya berhasil. Meltdown adalah sistem saraf yang kewalahan; "
         "tak ada tujuan dan tak ada kendali tersisa.\n\n"
         "Tantrum butuh batas yang tenang dan tak bergeser. Meltdown butuh penghiburan dan "
         "lebih sedikit rangsangan. Menganggap meltdown sebagai manipulasi adalah salah "
         "satu salah baca paling umum dan paling mahal dalam pengasuhan."),
        ("A tantrum usually pauses if the audience changes. A meltdown does not pause for "
         "anything, because nobody is steering it.",
         "Tantrum biasanya berhenti sejenak jika penontonnya berubah. Meltdown tidak "
         "berhenti untuk apa pun, karena tak ada yang mengemudikannya."),
        ("Next time, ask yourself which one you are watching before you decide how to respond.",
         "Lain kali, tanyakan pada diri sendiri yang mana yang sedang Anda saksikan sebelum "
         "memutuskan cara menanggapi."),
        ("Have I been treating overwhelm as manipulation?",
         "Apakah selama ini saya menganggap kewalahan sebagai manipulasi?"),
        ("\"I'm here. You don't have to talk yet.\"",
         "\"Mama/Papa di sini. Kamu belum perlu bicara.\""),
        framework=fw(
            ("Tantrum or meltdown?", "Tantrum atau meltdown?"),
            ("They look alike and need opposite responses. Check which one you are seeing.",
             "Keduanya mirip dan butuh respons berlawanan. Periksa mana yang Anda lihat."),
            [
                (("Tantrum", "Tantrum"),
                 [("Has a goal", "Ada tujuannya"), ("Some control left", "Masih ada kendali")],
                 ("There is a want. The child may check whether it is working, and it often "
                  "eases when the audience changes.",
                  "Ada sesuatu yang diinginkan. Anak mungkin mengecek apakah caranya berhasil, "
                  "dan sering mereda saat penontonnya berubah."),
                 ("Respond with a calm, unmoved limit. Stay kind, do not renegotiate.",
                  "Tanggapi dengan batas yang tenang dan tak bergeser. Tetap ramah, jangan "
                  "menegosiasi ulang.")),
                (("Meltdown", "Meltdown"),
                 [("No goal", "Tanpa tujuan"), ("Overwhelmed", "Kewalahan")],
                 ("The nervous system is flooded. It does not pause for an audience and the "
                  "child cannot stop it at will.",
                  "Sistem sarafnya kebanjiran. Tidak berhenti karena ada penonton, dan anak "
                  "tak bisa menghentikannya sesuka hati."),
                 ("Respond with comfort, quiet and less input. Teach much later, if at all.",
                  "Tanggapi dengan penghiburan, ketenangan, dan rangsangan yang dikurangi. "
                  "Ajarkan jauh setelahnya, kalau memang perlu.")),
            ],
        ),
    ),
    53: d(
        ("Delay of gratification",
         "Menunda kepuasan"),
        ("Waiting is a skill, not a virtue, and it is built by practice at the right "
         "size. A child who cannot wait five minutes today can usually wait six next "
         "month if the waiting is scaffolded rather than demanded.\n\n"
         "What helps most is not willpower but distraction and a visible end point — the "
         "same strategies adults quietly use.",
         "Menunggu adalah keterampilan, bukan kebajikan, dan dibangun lewat latihan dengan "
         "takaran yang tepat. Anak yang hari ini tak bisa menunggu lima menit biasanya bisa "
         "menunggu enam menit bulan depan jika penantiannya ditopang, bukan dituntut.\n\n"
         "Yang paling membantu bukan tekad, melainkan pengalihan perhatian dan titik akhir "
         "yang terlihat — strategi yang sama yang diam-diam dipakai orang dewasa."),
        ("\"Wait\" is hard. \"Wait until the timer rings\" is much easier, because the end "
         "is visible and no longer depends on your mood.",
         "\"Tunggu\" itu sulit. \"Tunggu sampai alarmnya bunyi\" jauh lebih mudah, karena "
         "akhirnya terlihat dan tak lagi bergantung pada suasana hati Anda."),
        ("Make one wait visible today with a timer, a song, or a countable thing.",
         "Buat satu penantian terlihat hari ini dengan pengatur waktu, lagu, atau sesuatu yang bisa dihitung."),
        ("Am I asking my child to wait without giving them anything to hold on to?",
         "Apakah saya meminta anak menunggu tanpa memberinya pegangan apa pun?"),
        ("\"When the timer rings, it's your turn.\"",
         "\"Kalau alarmnya bunyi, giliranmu.\""),
    ),
    54: d(
        ("Frustration tolerance",
         "Ketahanan menghadapi frustrasi"),
        ("Frustration tolerance grows the same way muscle does: through manageable "
         "resistance, repeated. A child rescued from every difficulty never builds it; a "
         "child abandoned in difficulty is overwhelmed and builds avoidance instead.\n\n"
         "The useful position is beside them — close enough to steady, far enough that "
         "the struggle is still theirs.",
         "Ketahanan menghadapi frustrasi tumbuh seperti otot: lewat hambatan yang "
         "terkelola, diulang-ulang. Anak yang diselamatkan dari setiap kesulitan tak pernah "
         "membangunnya; anak yang ditinggalkan dalam kesulitan menjadi kewalahan dan justru "
         "membangun kebiasaan menghindar.\n\n"
         "Posisi yang berguna adalah di sampingnya — cukup dekat untuk menenangkan, cukup "
         "jauh agar perjuangan itu tetap miliknya."),
        ("Taking the puzzle and finishing it ends the crying and ends the learning. "
         "Sitting nearby saying \"try turning it\" keeps both alive.",
         "Mengambil puzzle dan menyelesaikannya menghentikan tangisan sekaligus "
         "menghentikan pembelajaran. Duduk di dekatnya sambil berkata \"coba diputar\" "
         "menjaga keduanya tetap hidup."),
        ("Let your child struggle productively for one extra minute today before helping.",
         "Biarkan anak berjuang secara produktif satu menit lebih lama hari ini sebelum Anda membantu."),
        ("Do I rescue my child from struggle they could grow through?",
         "Apakah saya menyelamatkan anak dari perjuangan yang justru bisa menumbuhkannya?"),
        ("\"This is tricky. I'll stay while you try.\"",
         "\"Ini memang rumit. Mama/Papa temani sambil kamu coba.\""),
    ),
    55: d(
        ("Social learning",
         "Belajar dari lingkungan sosial"),
        ("Children learn social behaviour mostly by watching it, and they watch everyone "
         "— you, siblings, classmates, screens. What gets modelled repeatedly becomes "
         "normal, whether or not anyone intended to teach it.\n\n"
         "This is why the social environment you choose matters as much as the "
         "instructions you give.",
         "Anak belajar perilaku sosial terutama dengan mengamatinya, dan mereka mengamati "
         "semua orang — Anda, saudara, teman sekelas, layar. Apa yang berulang kali "
         "dicontohkan menjadi hal yang wajar, terlepas ada atau tidaknya niat mengajarkan.\n\n"
         "Karena itu lingkungan sosial yang Anda pilih sama pentingnya dengan instruksi yang Anda beri."),
        ("A child who sees adults apologise, thank and disagree respectfully acquires "
         "those moves without a single lesson on them.",
         "Anak yang melihat orang dewasa meminta maaf, berterima kasih, dan berbeda pendapat "
         "dengan hormat menyerap gerakan itu tanpa satu pun pelajaran khusus."),
        ("Point out one good social move you saw today — in anyone — and name why it worked.",
         "Tunjukkan satu tindakan sosial baik yang Anda lihat hari ini — dari siapa pun — dan "
         "sebutkan mengapa itu berhasil."),
        ("What social behaviour is my child seeing most often at home?",
         "Perilaku sosial apa yang paling sering anak lihat di rumah?"),
        ("\"Did you see how she handled that? That was kind.\"",
         "\"Lihat tadi bagaimana dia menanganinya? Itu baik sekali.\""),
    ),
    56: d(
        ("Peer influence",
         "Pengaruh teman sebaya"),
        ("Peer influence rises through childhood and peaks in adolescence, and this is "
         "normal rather than a failure of your authority. Peers shape style, language and "
         "short-term choices most strongly.\n\n"
         "Parents keep more influence than they think on the deeper things — values, "
         "identity, long-term direction — provided the relationship stays open enough for "
         "those conversations to happen at all.",
         "Pengaruh teman sebaya meningkat sepanjang masa kanak dan memuncak di masa remaja, "
         "dan ini normal, bukan kegagalan wibawa Anda. Teman sebaya paling kuat membentuk "
         "gaya, bahasa, dan pilihan jangka pendek.\n\n"
         "Orang tua menyimpan lebih banyak pengaruh daripada yang mereka kira pada hal-hal "
         "yang lebih dalam — nilai, jati diri, arah jangka panjang — asalkan hubungannya "
         "cukup terbuka agar percakapan itu bisa terjadi."),
        ("Banning a friendship outright usually drives it underground. Staying curious "
         "about it keeps you in the conversation where you can still have an effect.",
         "Melarang pertemanan secara mutlak biasanya membuatnya berpindah ke bawah tanah. "
         "Tetap penasaran tentangnya menjaga Anda dalam percakapan, tempat Anda masih bisa berpengaruh."),
        ("Ask one genuinely curious question about your child's friends today, with no "
         "verdict attached.",
         "Ajukan satu pertanyaan yang benar-benar penasaran tentang teman anak hari ini, tanpa penilaian."),
        ("Do my children's friendships get curiosity from me, or judgement?",
         "Apakah pertemanan anak saya mendapat rasa penasaran dari saya, atau penghakiman?"),
        ("\"Tell me what you like about them.\"",
         "\"Ceritakan, apa yang kamu suka dari dia.\""),
    ),
    57: d(
        ("Praise and motivation",
         "Pujian dan motivasi"),
        ("Not all praise helps. Praise aimed at fixed traits — clever, talented, good — "
         "quietly teaches a child that ability is a thing you either have or lack, which "
         "makes hard tasks threatening.\n\n"
         "Praise aimed at effort, strategy and choice teaches that difficulty is normal "
         "and improvable. The difference is a few words and it compounds for years.",
         "Tidak semua pujian membantu. Pujian yang menyasar sifat tetap — pintar, berbakat, "
         "anak baik — diam-diam mengajarkan bahwa kemampuan adalah sesuatu yang dimiliki "
         "atau tidak, sehingga tugas sulit terasa mengancam.\n\n"
         "Pujian yang menyasar usaha, strategi, dan pilihan mengajarkan bahwa kesulitan itu "
         "wajar dan bisa diperbaiki. Bedanya hanya beberapa kata, dan efeknya menumpuk bertahun-tahun."),
        ("\"You're so clever\" makes failure evidence against the label. \"You kept going "
         "when that got hard\" makes effort the thing that counts.",
         "\"Kamu pintar sekali\" membuat kegagalan menjadi bukti yang melawan label itu. "
         "\"Kamu terus berusaha waktu itu jadi sulit\" membuat usaha jadi hal yang dihitung."),
        ("Praise one specific effort today instead of one general trait.",
         "Puji satu usaha yang spesifik hari ini, bukan satu sifat yang umum."),
        ("Does my praise make my child braver about hard things, or more careful?",
         "Apakah pujian saya membuat anak lebih berani menghadapi hal sulit, atau justru lebih hati-hati?"),
        ("\"You worked hard at that. I saw it.\"",
         "\"Kamu berusaha keras tadi. Mama/Papa lihat.\""),
    ),
    58: d(
        ("Intrinsic vs extrinsic motivation",
         "Motivasi dari dalam vs dari luar"),
        ("Rewards work quickly and can quietly replace the reason. A child paid to read "
         "often reads until the payment stops. The reward becomes the point, and the "
         "original interest fades.\n\n"
         "Extrinsic motivation is not banned — it is useful for genuinely dull necessary "
         "tasks. Just avoid attaching it to things you want your child to love.",
         "Imbalan bekerja cepat dan diam-diam bisa menggantikan alasannya. Anak yang dibayar "
         "untuk membaca sering membaca sampai bayarannya berhenti. Imbalan menjadi tujuannya, "
         "dan minat aslinya memudar.\n\n"
         "Motivasi dari luar tidak dilarang — ia berguna untuk tugas wajib yang memang "
         "membosankan. Hanya saja, hindari melekatkannya pada hal yang Anda ingin anak cintai."),
        ("Sticker charts are fine for tooth-brushing. They are risky for reading, drawing "
         "or music, where you want the child to keep going after the stickers stop.",
         "Tabel stiker cocok untuk menyikat gigi. Ia berisiko untuk membaca, menggambar, atau "
         "musik, di mana Anda ingin anak terus melakukannya setelah stikernya habis."),
        ("Notice one thing your child does for its own sake today and protect it from rewards.",
         "Sadari satu hal yang anak lakukan karena dia menyukainya hari ini, dan lindungi dari imbalan."),
        ("Am I paying for something my child was already willing to do?",
         "Apakah saya sedang membayar sesuatu yang sebenarnya sudah anak mau lakukan?"),
        ("\"You did that because you wanted to. That's the best reason.\"",
         "\"Kamu melakukannya karena kamu mau. Itu alasan terbaik.\""),
    ),
    59: d(
        ("Shame sensitivity in children",
         "Kepekaan anak terhadap rasa malu"),
        ("Children are far more shame-sensitive than adults remember being. Being "
         "corrected in front of others, or having a mistake named publicly, lands much "
         "harder than the same correction given privately.\n\n"
         "Shame does not produce better behaviour. It produces concealment, defensiveness "
         "and, over time, a child who would rather lie than be seen failing.",
         "Anak jauh lebih peka terhadap rasa malu daripada yang diingat orang dewasa. "
         "Ditegur di depan orang lain, atau kesalahannya disebut di muka umum, terasa jauh "
         "lebih berat daripada teguran yang sama secara pribadi.\n\n"
         "Rasa malu tidak menghasilkan perilaku yang lebih baik. Ia menghasilkan kebiasaan "
         "menyembunyikan, sikap membela diri, dan lama-kelamaan anak yang lebih memilih "
         "berbohong daripada terlihat gagal."),
        ("Pulling a child aside to correct them costs you ten seconds and saves them the "
         "part that actually does the damage.",
         "Menarik anak ke samping untuk menegurnya menghabiskan sepuluh detik Anda dan "
         "menyelamatkannya dari bagian yang sesungguhnya merusak."),
        ("Deliver every correction privately today, even the small ones.",
         "Sampaikan setiap teguran secara pribadi hari ini, bahkan yang kecil sekalipun."),
        ("Do I correct my child in front of people without noticing?",
         "Apakah saya menegur anak di depan orang lain tanpa menyadarinya?"),
        ("\"Come here a moment — just you and me.\"",
         "\"Sini sebentar — kita berdua saja.\""),
    ),
    60: d(
        ("What misbehavior often really means",
         "Apa arti sebenarnya di balik kenakalan"),
        ("Pull this chapter together and a pattern appears. Behind most repeated "
         "misbehaviour sits one of a short list: tiredness, hunger, sensory overload, a "
         "transition, a missing skill, an unmet need for connection, or a feeling with "
         "no words.\n\n"
         "None of those are moral failures, and none of them are fixed by punishment. "
         "Read the cause and the response usually becomes obvious.",
         "Satukan bab ini dan sebuah pola muncul. Di balik sebagian besar kenakalan yang "
         "berulang duduk salah satu dari daftar pendek ini: kelelahan, lapar, kelebihan "
         "rangsang, perpindahan, keterampilan yang belum ada, kebutuhan kedekatan yang tak "
         "terpenuhi, atau perasaan tanpa kata.\n\n"
         "Tak satu pun dari itu kegagalan moral, dan tak satu pun diperbaiki oleh hukuman. "
         "Baca penyebabnya, dan responsnya biasanya menjadi jelas."),
        ("Ask \"what is underneath this?\" before \"what is the consequence for this?\" and "
         "most discipline problems change shape.",
         "Tanyakan \"apa yang ada di baliknya?\" sebelum \"apa konsekuensinya?\" dan sebagian "
         "besar masalah disiplin berubah bentuk."),
        ("Take the behaviour that troubles you most and match it to one cause from the list.",
         "Ambil perilaku yang paling mengganggu Anda dan cocokkan dengan satu penyebab dari daftar."),
        ("What is the most common cause underneath my child's hardest behaviour?",
         "Apa penyebab yang paling sering ada di balik perilaku tersulit anak saya?"),
        ("\"Something's underneath this. Let's find it.\"",
         "\"Ada sesuatu di baliknya. Ayo kita cari.\""),
    ),
    61: d(
        ("Weekly reflection",
         "Refleksi mingguan"),
        ("A month of development reading changes little unless it changes how you read "
         "one specific child. Take the behaviour that has frustrated you most this month "
         "and re-read it through everything in this chapter.\n\n"
         "Most parents find the same thing: the behaviour that looked like defiance was "
         "capacity, tiredness or an unmet need — and once seen that way, it stops being "
         "a fight.",
         "Sebulan membaca soal perkembangan hanya sedikit mengubah, kecuali ia mengubah cara "
         "Anda membaca satu anak tertentu. Ambil perilaku yang paling membuat Anda frustrasi "
         "bulan ini dan baca ulang lewat semua isi bab ini.\n\n"
         "Kebanyakan orang tua menemukan hal yang sama: perilaku yang tampak seperti "
         "pembangkangan ternyata soal kemampuan, kelelahan, atau kebutuhan yang tak "
         "terpenuhi — dan begitu dilihat seperti itu, ia berhenti menjadi pertengkaran."),
        ("The reframe is the whole gain of this chapter. Same child, same behaviour, "
         "different explanation — and a completely different response available to you.",
         "Pemaknaan ulang itulah seluruh hasil bab ini. Anak yang sama, perilaku yang sama, "
         "penjelasan yang berbeda — dan respons yang sama sekali berbeda kini tersedia bagi Anda."),
        ("Write down one behaviour and the developmental explanation you now think sits "
         "under it.",
         "Tuliskan satu perilaku dan penjelasan perkembangan yang kini Anda yakini ada di baliknya."),
        ("What did I used to call naughty that I would now call developmental?",
         "Apa yang dulu saya sebut nakal, yang kini saya sebut sebagai hal perkembangan?"),
        ("\"You're not giving me a hard time. You're having a hard time.\"",
         "\"Kamu bukan sedang menyulitkan Mama/Papa. Kamu sedang kesulitan.\""),
    ),
}
