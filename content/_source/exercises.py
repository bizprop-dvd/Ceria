"""Authored weekly exercises and monthly reviews.

The founder's manuscript supplies only 12 distinct weekly exercises — one per
chapter, repeated across every week of that chapter — and a single monthly
review repeated all twelve times. A parent reaching week 5 met the same
sentence they saw in week 1, and every month closed identically.

These are 52 and 12 distinct items, each grounded in the days that week or
month actually covers. Where the manuscript's exercise fits a week well it is
kept, carrying the founder's reviewed Indonesian unchanged — weeks 1, 6, 10,
14, 18, 23, 27, 32, 36, 40, 44 and 48, and month 1. So all twelve of the
manuscript's exercises survive; the other forty weeks and eleven months are
new.

Indonesian follows the register of the founder's 2026-08-04 review: warm,
unhurried, "Anda" throughout, and never phrased as an instruction a tired
parent could fail.

build_daily.py prefers these over the manuscript.
"""


def e(en, id_):
    return {"en": en, "id": id_}


WEEKLY = {
    # ---- Chapter 1 · Parenting Mindset ----------------------------------
    1: e(
        "Write one paragraph on how you want to be remembered by your child, then "
        "identify one daily habit that supports that vision.",
        "Tuliskan satu paragraf tentang bagaimana Anda berharap anak mengenang "
        "kehadiran Anda, lalu pilih satu kebiasaan kecil setiap hari yang mendukung "
        "harapan tersebut."),
    2: e(
        "Before correcting anything this week, connect first — a touch, a look, or "
        "one warm sentence. Notice what changes in how your child answers you.",
        "Sebelum menegur apa pun minggu ini, dekati anak lebih dulu — sentuhan, "
        "tatapan, atau satu kalimat hangat. Perhatikan apa yang berubah dari cara "
        "anak menanggapi Anda."),
    3: e(
        "Notice one moment this week when your reaction felt larger than the "
        "situation, and write down what it reminded you of.",
        "Sadari satu momen minggu ini ketika reaksi Anda terasa lebih besar daripada "
        "kejadiannya, lalu tuliskan hal apa dari masa lalu yang mungkin teringat "
        "saat itu."),
    4: e(
        "Choose one thing you want your child to learn by watching you, and do it "
        "visibly at least three times this week.",
        "Pilih satu hal yang Anda ingin anak pelajari dengan melihat Anda, lalu "
        "lakukan hal itu secara terlihat sekurangnya tiga kali minggu ini."),

    # ---- Chapter 2 · Child Development -----------------------------------
    5: e(
        "Name one house rule your family keeps and say out loud, once this week, why "
        "it matters to you — not that it exists, but why.",
        "Sebutkan satu aturan yang keluarga Anda pegang, lalu sekali minggu ini "
        "katakan dengan lantang mengapa hal itu penting bagi Anda — bukan sekadar "
        "bahwa aturannya ada, melainkan alasannya."),
    6: e(
        "Observe one child behavior this week and reinterpret it using development "
        "rather than morality.",
        "Amati satu perilaku anak minggu ini, lalu cobalah memahaminya melalui tahap "
        "perkembangan, bukan dengan menilainya sebagai baik atau buruk."),
    7: e(
        "Track what time of day your child struggles most this week. Look for sleep, "
        "hunger or too much noise before you look for a reason.",
        "Catat jam berapa anak Anda paling sering kesulitan minggu ini. Periksa dulu "
        "soal tidur, lapar, atau suasana yang terlalu ramai sebelum mencari sebab "
        "yang lain."),
    8: e(
        "Give one transition a warning this week — five minutes, then two, then now — "
        "and see whether the ending goes more gently.",
        "Beri satu perpindahan kegiatan sebuah aba-aba minggu ini — lima menit lagi, "
        "lalu dua menit, lalu sekarang — dan perhatikan apakah peralihannya terasa "
        "lebih lembut."),

    # ---- Chapter 3 · Parent Self-Regulation ------------------------------
    9: e(
        "Write down the three things most likely to set you off, and keep the list "
        "somewhere you will see it before the hard hour of the day.",
        "Tuliskan tiga hal yang paling mudah memancing emosi Anda, lalu simpan "
        "catatan itu di tempat yang akan Anda lihat sebelum jam tersulit dalam hari "
        "Anda."),
    10: e(
        "Track your top three parenting triggers this week and note what helped you "
        "stay steadier.",
        "Catat tiga hal yang paling mudah memancing emosi Anda minggu ini, lalu "
        "tuliskan apa yang membantu Anda tetap lebih tenang."),
    11: e(
        "Repair once this week without the word \"because\" — name what you did, and "
        "stop there.",
        "Perbaiki keadaan sekali minggu ini tanpa memakai kata \"karena\" — sebutkan "
        "apa yang Anda lakukan, lalu berhenti di situ."),
    12: e(
        "Agree one thing with the other adult in your home this week, decided away "
        "from the children and held in front of them.",
        "Sepakati satu hal dengan orang dewasa lain di rumah minggu ini — diputuskan "
        "jauh dari anak-anak, lalu dipegang bersama di hadapan mereka."),

    # ---- Chapter 4 · Communication ---------------------------------------
    13: e(
        "Decide now what you will do the next time you feel your temper rising, and "
        "say the sentence out loud once while everything is calm.",
        "Tentukan sekarang apa yang akan Anda lakukan saat emosi mulai naik, lalu "
        "ucapkan kalimatnya sekali dengan lantang selagi suasana masih tenang."),
    14: e(
        "Practice one empathy-first sentence every day this week before correcting "
        "or directing.",
        "Gunakan satu kalimat empati setiap hari minggu ini sebelum mengoreksi atau "
        "memberikan arahan."),
    15: e(
        "Ask one open question a day this week and let the silence after it last "
        "longer than feels comfortable.",
        "Ajukan satu pertanyaan terbuka setiap hari minggu ini, lalu biarkan "
        "keheningan sesudahnya berlangsung sedikit lebih lama daripada yang terasa "
        "nyaman."),
    16: e(
        "Catch yourself once this week before a label — lazy, naughty, difficult — "
        "and describe what happened instead.",
        "Tangkap diri Anda sekali minggu ini sebelum melabeli anak — malas, nakal, "
        "susah diatur — lalu gambarkan saja apa yang terjadi."),

    # ---- Chapter 5 · Discipline -------------------------------------------
    17: e(
        "Let your child tell the story of one incident all the way through this week "
        "before you say anything about it.",
        "Biarkan anak menceritakan satu kejadian sampai selesai minggu ini sebelum "
        "Anda mengatakan apa pun tentangnya."),
    18: e(
        "Choose one recurring behavior and create a calmer, clearer discipline plan "
        "with one consistent follow-through.",
        "Pilih satu perilaku yang berulang, lalu susun respons disiplin yang lebih "
        "tenang dan jelas dengan tindak lanjut yang konsisten."),
    19: e(
        "State one limit once this week, then stop explaining and let the silence "
        "hold it.",
        "Sebutkan satu batas sekali saja minggu ini, lalu berhenti menjelaskan dan "
        "biarkan keheningan yang menjaganya."),
    20: e(
        "Notice one small good thing your child does each day this week and say it "
        "out loud on the spot.",
        "Perhatikan satu hal baik yang kecil dari anak Anda setiap hari minggu ini, "
        "lalu sebutkan saat itu juga."),

    # ---- Chapter 6 · Emotional Coaching ------------------------------------
    21: e(
        "Describe what your child actually did this week instead of praising who "
        "they are. Effort, not label.",
        "Gambarkan apa yang benar-benar anak lakukan minggu ini alih-alih memuji "
        "dirinya. Usahanya, bukan labelnya."),
    22: e(
        "Sit beside one upset child this week without fixing, explaining, or "
        "hurrying the feeling along.",
        "Duduklah di samping anak yang sedang kecewa minggu ini tanpa membetulkan, "
        "menjelaskan, atau terburu-buru menyudahi perasaannya."),
    23: e(
        "At least three times this week, help your child name a feeling before "
        "discussing behavior.",
        "Pada tiga kesempatan minggu ini, bantu anak menamai perasaannya sebelum "
        "membicarakan perilakunya."),
    24: e(
        "Return to your child within the hour after one hard moment this week, and "
        "say nothing about the rule.",
        "Datangi kembali anak Anda dalam satu jam setelah satu momen yang berat "
        "minggu ini, dan jangan bahas aturannya."),

    # ---- Chapter 7 · Routines & Home Systems --------------------------------
    25: e(
        "Add one new feeling word to your family's vocabulary this week, and use it "
        "about yourself first.",
        "Tambahkan satu kata perasaan baru ke perbendaharaan keluarga minggu ini, "
        "dan pakailah lebih dulu untuk diri Anda sendiri."),
    26: e(
        "Let your child finish one difficult thing this week while you stay nearby "
        "and keep your hands to yourself.",
        "Biarkan anak menyelesaikan satu hal yang sulit minggu ini sementara Anda "
        "tetap di dekatnya tanpa ikut mengerjakan."),
    27: e(
        "Redesign one household friction point into a simple routine with fewer "
        "reminders.",
        "Rancang ulang satu titik ketegangan di rumah menjadi rutinitas sederhana "
        "yang memerlukan lebih sedikit pengingat."),
    28: e(
        "Count the steps in your hardest daily routine this week, then remove two "
        "and see whether anyone misses them.",
        "Hitung langkah-langkah dalam rutinitas harian Anda yang paling berat minggu "
        "ini, lalu hilangkan dua di antaranya dan lihat apakah ada yang merasa "
        "kehilangan."),

    # ---- Chapter 8 · Behavior Challenges -------------------------------------
    29: e(
        "Protect one small ritual this week even on the day it is least convenient. "
        "That day is the one that teaches it is real.",
        "Jagalah satu ritual kecil minggu ini, bahkan pada hari yang paling tidak "
        "memungkinkan. Justru hari itulah yang menunjukkan bahwa ritual ini "
        "sungguh-sungguh ada."),
    30: e(
        "Say no to one thing on the family calendar this week and leave the space "
        "empty.",
        "Tolak satu kegiatan dalam jadwal keluarga minggu ini, lalu biarkan ruang "
        "itu tetap kosong."),
    31: e(
        "Watch one repeating behavior this week and write down what happened in the "
        "ten minutes before it, not during.",
        "Amati satu perilaku yang berulang minggu ini, lalu tuliskan apa yang "
        "terjadi pada sepuluh menit sebelumnya, bukan saat kejadiannya."),
    32: e(
        "Use an ABC log this week: Antecedent, Behavior, Consequence, for one "
        "repeating issue.",
        "Gunakan Catatan ABC minggu ini—Pemicu, Perilaku, Akibat—untuk memahami satu "
        "persoalan yang terus berulang."),

    # ---- Chapter 9 · Building Character & Responsibility -----------------------
    33: e(
        "Meet one hard admission this week with a softer voice than the one you "
        "started the sentence with.",
        "Sambut satu pengakuan yang berat minggu ini dengan suara yang lebih lembut "
        "daripada nada saat Anda mulai bicara."),
    34: e(
        "Shrink one task your child avoids until starting it is easy, and sit with "
        "them for the first line only.",
        "Perkecil satu tugas yang dihindari anak sampai memulainya terasa mudah, "
        "lalu temani ia hanya untuk baris pertamanya."),
    35: e(
        "Hand one responsibility to your child that belongs to the age just above "
        "them, and show them once.",
        "Serahkan satu tanggung jawab kepada anak yang biasanya untuk usia sedikit "
        "di atasnya, lalu tunjukkan caranya sekali saja."),
    36: e(
        "Create one small daily responsibility for your child and keep it consistent "
        "for the week.",
        "Pilih satu tanggung jawab kecil setiap hari untuk anak, lalu dampingi secara "
        "konsisten selama satu minggu."),

    # ---- Chapter 10 · Relationship & Attachment ---------------------------------
    37: e(
        "Answer one of your child's problems with a question this week instead of a "
        "solution, then wait.",
        "Jawab satu masalah anak Anda dengan pertanyaan minggu ini alih-alih dengan "
        "solusi, lalu tunggulah."),
    38: e(
        "Keep every small promise you make this week, including the ones nobody "
        "would notice you dropping.",
        "Tepati setiap janji kecil yang Anda buat minggu ini, termasuk janji yang "
        "tidak akan ada yang menyadari kalau Anda batalkan."),
    39: e(
        "Let your face show that you are glad to see your child, before any question "
        "or instruction, every day this week.",
        "Biarkan wajah Anda menunjukkan bahwa Anda senang melihat anak, sebelum "
        "pertanyaan atau arahan apa pun, setiap hari minggu ini."),
    40: e(
        "Schedule at least 10 minutes of undistracted one-on-one time on three "
        "separate days this week.",
        "Sediakan sekurangnya 10 menit waktu berdua tanpa gangguan pada tiga hari "
        "yang berbeda minggu ini."),

    # ---- Chapter 11 · Special Contexts --------------------------------------------
    41: e(
        "Give ten minutes this week to whichever child you find hardest to be with "
        "right now.",
        "Berikan sepuluh menit minggu ini kepada anak yang saat ini paling sulit "
        "Anda dampingi."),
    42: e(
        "Make yourself available this week in the place your child actually talks — "
        "the car, the kitchen at night — and ask nothing.",
        "Sediakan diri Anda minggu ini di tempat anak biasanya mau bercerita — di "
        "mobil, di dapur pada malam hari — dan jangan menanyakan apa pun."),
    43: e(
        "Name the pressure your family is actually under this week, in one honest "
        "sentence, and make clear it is not your child's doing.",
        "Sebutkan tekanan yang sedang keluarga Anda hadapi minggu ini dalam satu "
        "kalimat yang jujur, dan perjelas bahwa itu bukan karena anak Anda."),
    44: e(
        "Identify one pressure point in your family context and make one "
        "compassionate adjustment.",
        "Kenali satu sumber tekanan dalam keadaan keluarga, lalu buat satu "
        "penyesuaian yang penuh pengertian."),

    # ---- Chapter 12 · Integration & Advanced Practice ---------------------------------
    45: e(
        "Write down the three people you could call at ten at night, and send a "
        "message to one of them this week.",
        "Tuliskan tiga orang yang bisa Anda hubungi pada pukul sepuluh malam, lalu "
        "kirimkan pesan kepada salah satunya minggu ini."),
    46: e(
        "Say the no-secrets rule out loud to your child this week, calmly, long "
        "before you think it is needed.",
        "Ucapkan aturan tidak ada rahasia kepada anak Anda minggu ini dengan tenang, "
        "jauh sebelum Anda merasa itu diperlukan."),
    47: e(
        "List three things that genuinely work in your home right now, then ask what "
        "they have in common.",
        "Daftarkan tiga hal yang benar-benar berjalan baik di rumah Anda saat ini, "
        "lalu tanyakan apa kesamaan di antara ketiganya."),
    48: e(
        "Review your notes from the week and choose one family pattern to improve "
        "over the next seven days.",
        "Baca kembali catatan minggu ini, lalu pilih satu pola keluarga yang ingin "
        "dibuat lebih baik dalam tujuh hari ke depan."),
    49: e(
        "Write your calm-down plan in four lines this week — the sentence, the "
        "place, how long, who you tell — and rehearse it once.",
        "Tuliskan rencana menenangkan diri Anda dalam empat baris minggu ini — "
        "kalimatnya, tempatnya, berapa lama, siapa yang diberi tahu — lalu latih "
        "sekali."),
    50: e(
        "Write five family rules together with your children this week, phrased "
        "positively, binding on the adults too.",
        "Tuliskan lima aturan keluarga bersama anak-anak minggu ini, dirumuskan "
        "secara positif, dan berlaku juga bagi orang dewasanya."),
    51: e(
        "Answer three honest questions about each child this week, one child at a "
        "time, written down rather than thought about.",
        "Jawab tiga pertanyaan jujur tentang setiap anak minggu ini, satu anak pada "
        "satu waktu, dituliskan dan bukan sekadar dipikirkan."),
    52: e(
        "Write your next ninety days in three lines — one thing to keep, one to "
        "stop, one to start — and put the review date in the calendar.",
        "Tuliskan sembilan puluh hari ke depan dalam tiga baris — satu hal yang "
        "dipertahankan, satu yang dihentikan, satu yang dimulai — lalu catat tanggal "
        "peninjauannya di kalender."),
}


MONTHLY = {
    1: e(
        "What improved this month, what kept repeating, what triggered me most, what "
        "helped my child most, and what one change will I carry into next month?",
        "Apa yang membaik bulan ini? Apa yang terus berulang? Apa yang paling "
        "memancing emosi saya? Apa yang paling membantu anak? Perubahan kecil apa "
        "yang ingin saya teruskan ke bulan depan?"),
    2: e(
        "Which behavior did I read as defiance this month that was really my child's "
        "age, and what did I do differently once I saw it?",
        "Perilaku mana bulan ini yang saya baca sebagai pembangkangan padahal "
        "sebenarnya wajar untuk usianya, dan apa yang saya lakukan berbeda setelah "
        "menyadarinya?"),
    3: e(
        "When did I lose my temper this month, what was happening in me beforehand, "
        "and how did I repair it?",
        "Kapan saya kehilangan kesabaran bulan ini, apa yang sedang terjadi dalam "
        "diri saya sebelumnya, dan bagaimana saya memperbaikinya?"),
    4: e(
        "What did my child tell me this month that they might not have told me three "
        "months ago, and what made that possible?",
        "Apa yang anak ceritakan kepada saya bulan ini yang mungkin belum tentu ia "
        "ceritakan tiga bulan lalu, dan apa yang membuatnya bisa terjadi?"),
    5: e(
        "Which limit did I hold calmly this month, which one did I abandon halfway, "
        "and what made the difference between them?",
        "Batas mana yang bulan ini saya pegang dengan tenang, batas mana yang saya "
        "tinggalkan di tengah jalan, dan apa yang membedakan keduanya?"),
    6: e(
        "When did I sit with my child's feeling instead of solving it this month, "
        "and what happened next?",
        "Kapan bulan ini saya menemani perasaan anak alih-alih buru-buru "
        "menyelesaikannya, dan apa yang terjadi sesudahnya?"),
    7: e(
        "Which routine runs without a fight now, which one still costs us most, and "
        "what would removing two steps do to it?",
        "Rutinitas mana yang kini berjalan tanpa pertengkaran, mana yang masih "
        "paling menguras kami, dan apa yang terjadi bila dua langkahnya "
        "dihilangkan?"),
    8: e(
        "What need was underneath the behavior that repeated most this month — "
        "attention, control, escape, or a tired body?",
        "Kebutuhan apa yang ada di balik perilaku yang paling sering berulang bulan "
        "ini — perhatian, kendali, ingin menghindar, atau tubuh yang lelah?"),
    9: e(
        "What does my child now handle that they did not six months ago, and what "
        "will I hand over next?",
        "Apa yang kini sanggup anak saya kerjakan dan enam bulan lalu belum, dan apa "
        "yang akan saya serahkan berikutnya?"),
    10: e(
        "How many days this month did my child have my full attention for even ten "
        "minutes, and what got in the way on the other days?",
        "Berapa hari bulan ini anak saya benar-benar mendapat perhatian penuh saya "
        "meski hanya sepuluh menit, dan apa yang menghalangi pada hari-hari "
        "lainnya?"),
    11: e(
        "What pressure is my family carrying that is not my child's doing, and which "
        "expectation can I lower next month?",
        "Tekanan apa yang sedang keluarga saya pikul dan bukan disebabkan oleh anak, "
        "dan harapan mana yang bisa saya turunkan bulan depan?"),
    12: e(
        "Looking across the whole year: what is genuinely different in how I parent, "
        "what changed in me, and what one thing am I carrying forward?",
        "Menengok sepanjang tahun ini: apa yang benar-benar berbeda dari cara saya "
        "mengasuh, apa yang berubah dalam diri saya, dan satu hal apa yang saya bawa "
        "ke depan?"),
}
