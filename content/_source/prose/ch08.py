# Chapter 8 — Behavior Challenges (days 212-241)
#
# Grounded in the founder's guidebook chapter 8 ("Repeating behavior has a
# function — find the function before changing the behavior") and toolkit tool 8
# (ABC Log).
#
# Through-line: diagnose before you intervene. Several days here touch clinical
# ground, and each one points to professional support rather than pretending to
# replace it.

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
    212: d(
        ("Defiance: first principles",
         "Pembangkangan: prinsip dasarnya"),
        ("Defiance is the behaviour parents take most personally, which is exactly why it "
         "is handled worst. It reads as a challenge to your authority, and that reading "
         "makes the response about you rather than about the child.\n\n"
         "Underneath most defiance sits something smaller: a need for control, a "
         "transition handled badly, an overwhelmed child with no route to comply without "
         "losing face. Find that, and the defiance usually shrinks.",
         "Pembangkangan adalah perilaku yang paling dianggap pribadi oleh orang tua, dan "
         "justru karena itu paling buruk ditangani. Ia terbaca sebagai tantangan atas "
         "wibawa Anda, dan pembacaan itu membuat responsnya tentang Anda, bukan tentang anak.\n\n"
         "Di balik sebagian besar pembangkangan duduk sesuatu yang lebih kecil: kebutuhan "
         "akan kendali, perpindahan yang ditangani buruk, anak kewalahan tanpa jalan untuk "
         "menurut tanpa kehilangan muka. Temukan itu, dan pembangkangannya biasanya mengecil."),
        ("A child who says no in front of others is often not refusing the task. They are "
         "refusing to be seen obeying instantly.",
         "Anak yang berkata tidak di depan orang lain sering bukan menolak tugasnya. Dia "
         "menolak terlihat langsung menurut."),
        ("Give one dignified route to comply today rather than raising the stakes.",
         "Beri satu jalan yang terhormat untuk menurut hari ini, bukan menaikkan taruhan."),
        ("Do I take my child's no personally?",
         "Apakah saya menganggap kata tidak dari anak sebagai serangan pribadi?"),
        ("\"You can start now, or after this song. Up to you.\"",
         "\"Kamu boleh mulai sekarang, atau setelah lagu ini. Terserah kamu.\""),
        framework=fw(
            ("Four common functions", "Empat fungsi yang umum"),
            ("Repeating behaviour is doing a job. Work out which one before deciding anything.",
             "Perilaku yang berulang sedang melakukan sebuah tugas. Cari tahu yang mana sebelum memutuskan apa pun."),
            [
                (("To get attention", "Mendapat perhatian"),
                 [("Happens when you're busy", "Muncul saat Anda sibuk")],
                 ("Peaks when your attention is elsewhere — the phone, a sibling, a "
                  "visitor — and eases the moment you engage.",
                  "Memuncak saat perhatian Anda di tempat lain — ponsel, adik, tamu — dan "
                  "mereda begitu Anda hadir."),
                 ("Give attention before it is demanded, at a moment nothing is wrong.",
                  "Berikan perhatian sebelum diminta, di saat tak ada masalah.")),
                (("To get control", "Mendapat kendali"),
                 [("Around instructions", "Di sekitar instruksi")],
                 ("Clusters around being told what to do, especially in front of other "
                  "people.",
                  "Menumpuk di sekitar saat disuruh, terutama di depan orang lain."),
                 ("Hand back small real choices inside your limits.",
                  "Kembalikan pilihan kecil yang nyata di dalam batas Anda.")),
                (("To escape something", "Menghindari sesuatu"),
                 [("Before a hard task", "Sebelum tugas sulit")],
                 ("Appears just before a difficult or shaming task — homework, reading "
                  "aloud, getting dressed.",
                  "Muncul tepat sebelum tugas yang sulit atau memalukan — PR, membaca "
                  "keras, berpakaian."),
                 ("Shrink the task until starting is easy. The avoidance usually goes with it.",
                  "Perkecil tugasnya sampai memulainya mudah. Penghindarannya biasanya ikut hilang.")),
                (("To meet a body need", "Memenuhi kebutuhan tubuh"),
                 [("Same time daily", "Jam yang sama tiap hari")],
                 ("Tied to tiredness, hunger, or sensory overload, and worst at "
                  "predictable hours.",
                  "Terkait kelelahan, lapar, atau kelebihan rangsang, dan terburuk di "
                  "jam-jam yang bisa diperkirakan."),
                 ("Meet the need first. No consequence works on a body running empty.",
                  "Penuhi kebutuhannya dulu. Tak ada konsekuensi yang mempan pada tubuh yang kosong.")),
            ],
        ),
    ),
    213: d(
        ("Power struggles",
         "Adu kuasa"),
        ("A power struggle requires two participants. The moment you are trying to win, "
         "you have already joined one — and there is no version of winning that leaves the "
         "relationship better than it was.\n\n"
         "Stepping out is not losing. State the limit once, stop explaining, and let the "
         "silence hold it. Every extra sentence hands the child more to push against.",
         "Adu kuasa membutuhkan dua peserta. Begitu Anda berusaha menang, Anda sudah ikut "
         "di dalamnya — dan tak ada versi kemenangan yang meninggalkan hubungannya lebih "
         "baik dari sebelumnya.\n\n"
         "Keluar dari situ bukan kalah. Sebutkan batasnya sekali, berhenti menjelaskan, dan "
         "biarkan keheningan yang memegangnya. Setiap kalimat tambahan memberi anak lebih "
         "banyak bahan untuk didorong."),
        ("Notice the moment you start wanting to win. That feeling is the signal to stop "
         "talking, not to try harder.",
         "Sadari momen ketika Anda mulai ingin menang. Perasaan itu adalah tanda untuk "
         "berhenti bicara, bukan untuk berusaha lebih keras."),
        ("Step out of one power struggle today by simply repeating the limit and waiting.",
         "Keluar dari satu adu kuasa hari ini dengan sekadar mengulang batasnya dan menunggu."),
        ("What am I actually trying to win?",
         "Sebenarnya saya sedang berusaha memenangkan apa?"),
        ("\"That's my answer. I'm not going to argue it.\"",
         "\"Itu jawaban Mama/Papa. Tidak akan diperdebatkan.\""),
    ),
    214: d(
        ("Attention-seeking behavior",
         "Perilaku mencari perhatian"),
        ("The phrase is usually dismissive, as though attention were a frivolous thing to "
         "want. For a child, attention is a genuine need — and behaviour is the tool that "
         "reliably produces it.\n\n"
         "If difficult behaviour is the only dependable route to your full attention, a "
         "child will keep taking it. The answer is rarely less attention; it is attention "
         "that arrives before the behaviour does.",
         "Ungkapan ini biasanya diucapkan dengan meremehkan, seolah perhatian adalah "
         "keinginan sepele. Bagi anak, perhatian adalah kebutuhan yang sungguh — dan "
         "perilaku adalah alat yang paling andal menghasilkannya.\n\n"
         "Jika perilaku sulit adalah satu-satunya jalan andal menuju perhatian penuh Anda, "
         "anak akan terus menempuhnya. Jawabannya jarang mengurangi perhatian; melainkan "
         "perhatian yang datang sebelum perilakunya."),
        ("Ten minutes given freely in the afternoon usually costs less than the hour "
         "extracted through trouble at bedtime.",
         "Sepuluh menit yang diberikan cuma-cuma di sore hari biasanya lebih murah daripada "
         "satu jam yang dipaksa keluar lewat keributan menjelang tidur."),
        ("Give attention today at a moment nothing is wrong.",
         "Berikan perhatian hari ini di saat tak ada masalah apa pun."),
        ("What is the most reliable way for my child to get my full attention?",
         "Apa cara paling andal bagi anak saya untuk mendapat perhatian penuh saya?"),
        ("\"Come sit with me for ten minutes. No reason.\"",
         "\"Sini duduk sama Mama/Papa sepuluh menit. Tanpa alasan apa-apa.\""),
    ),
    215: d(
        ("Aggression between siblings",
         "Agresi antar saudara"),
        ("Some sibling conflict is normal and useful; aggression is where the line sits. "
         "Safety is not negotiable, and stopping it is not the same as refereeing who "
         "started it.\n\n"
         "Separate first, calm both, and only afterwards work out what happened. Trying to "
         "establish blame while either child is still flooded achieves nothing.",
         "Sebagian konflik antar saudara wajar dan berguna; agresi adalah tempat garisnya "
         "berada. Keselamatan tidak bisa ditawar, dan menghentikannya berbeda dengan "
         "mewasiti siapa yang memulai.\n\n"
         "Pisahkan dulu, tenangkan keduanya, dan baru sesudahnya cari tahu apa yang terjadi. "
         "Berusaha menetapkan siapa yang salah selagi salah satu anak masih kewalahan tak "
         "menghasilkan apa pun."),
        ("Comforting the hurt child first, without immediately prosecuting the other, "
         "teaches more about harm than any consequence delivered in the moment.",
         "Menenangkan anak yang tersakiti lebih dulu, tanpa langsung mengadili yang lain, "
         "mengajarkan lebih banyak tentang menyakiti daripada konsekuensi apa pun saat itu juga."),
        ("Separate and calm before investigating, next time it happens.",
         "Pisahkan dan tenangkan sebelum menyelidiki, lain kali ini terjadi."),
        ("Do I investigate before anyone is calm enough to be honest?",
         "Apakah saya menyelidiki sebelum ada yang cukup tenang untuk jujur?"),
        ("\"Safe first. We'll talk after.\"",
         "\"Aman dulu. Nanti kita bicara.\""),
    ),
    216: d(
        ("Hitting and biting",
         "Memukul dan menggigit"),
        ("In young children, hitting and biting are almost always communication rather than "
         "cruelty — the fastest available response when a feeling arrives faster than any "
         "word for it.\n\n"
         "The limit is absolute and the tone can still be calm. Stop it, name the feeling, "
         "and supply the words the child did not have.",
         "Pada anak kecil, memukul dan menggigit hampir selalu komunikasi, bukan kekejaman "
         "— respons tercepat yang tersedia ketika perasaan datang lebih cepat daripada kata "
         "untuknya.\n\n"
         "Batasnya mutlak dan nadanya tetap bisa tenang. Hentikan, namai perasaannya, dan "
         "sediakan kata-kata yang belum anak miliki."),
        ("\"You were angry and you wanted the toy. Hands are not for hitting. You can say "
         "'my turn'\" — limit, feeling, and the missing skill in three short sentences.",
         "\"Kamu marah dan kamu mau mainannya. Tangan bukan untuk memukul. Kamu bisa bilang "
         "'giliranku'\" — batas, perasaan, dan keterampilan yang hilang dalam tiga kalimat pendek."),
        ("Supply the missing words immediately after stopping the behaviour today.",
         "Sediakan kata-kata yang hilang segera setelah menghentikan perilakunya hari ini."),
        ("Does my child have any word for what they are feeling in that moment?",
         "Apakah anak saya punya kata untuk apa yang dia rasakan di momen itu?"),
        ("\"Hands are not for hitting. Say 'my turn'.\"",
         "\"Tangan bukan untuk memukul. Bilang 'giliranku'.\""),
    ),
    217: d(
        ("Throwing objects",
         "Melempar benda"),
        ("Throwing has several very different causes: experimenting with cause and effect, "
         "discharging a feeling too big to hold, or seeking a reliable reaction from you.\n\n"
         "The response differs by cause. Experimentation needs redirection to something "
         "throwable; discharge needs regulation; reaction-seeking needs a calm, boring, "
         "consistent answer.",
         "Melempar punya beberapa sebab yang sangat berbeda: bereksperimen dengan sebab dan "
         "akibat, melepaskan perasaan yang terlalu besar untuk ditahan, atau mencari reaksi "
         "yang andal dari Anda.\n\n"
         "Responsnya berbeda menurut sebabnya. Eksperimen butuh dialihkan ke sesuatu yang "
         "boleh dilempar; pelepasan butuh penenangan; pencarian reaksi butuh jawaban yang "
         "tenang, membosankan, dan konsisten."),
        ("A toddler throwing food is usually running an experiment, not being defiant. "
         "Giving them something they may throw ends the experiment honourably.",
         "Balita yang melempar makanan biasanya sedang bereksperimen, bukan membangkang. "
         "Memberinya sesuatu yang boleh dilempar mengakhiri eksperimennya dengan terhormat."),
        ("Work out which of the three causes is behind one throwing incident today.",
         "Cari tahu mana dari tiga sebab itu yang ada di balik satu kejadian melempar hari ini."),
        ("Is my child experimenting, discharging, or watching for my reaction?",
         "Apakah anak saya bereksperimen, melepaskan perasaan, atau menunggu reaksi saya?"),
        ("\"Not that. Here — you can throw this.\"",
         "\"Bukan itu. Ini — yang ini boleh dilempar.\""),
    ),
    218: d(
        ("Screaming",
         "Menjerit"),
        ("Screaming is effective, which is the whole problem: it is loud, hard to ignore, "
         "and usually produces an immediate response of some kind.\n\n"
         "For younger children it is often overload rather than strategy. For older ones it "
         "may be the only volume at which they have ever felt heard, which is worth sitting "
         "with honestly.",
         "Menjerit itu efektif, dan justru itulah seluruh masalahnya: keras, sulit "
         "diabaikan, dan biasanya langsung menghasilkan semacam respons.\n\n"
         "Untuk anak yang lebih kecil, ia sering kelebihan beban, bukan strategi. Untuk yang "
         "lebih besar, mungkin itulah satu-satunya volume yang pernah membuatnya merasa "
         "didengar — dan itu layak direnungkan dengan jujur."),
        ("Lowering your own voice in response works better than matching it. Two people "
         "shouting has never once resolved anything.",
         "Menurunkan suara Anda sendiri sebagai jawaban lebih berhasil daripada menyamainya. "
         "Dua orang berteriak tak pernah sekali pun menyelesaikan apa pun."),
        ("Answer one raised voice today with a quieter one.",
         "Jawab satu suara yang meninggi hari ini dengan suara yang lebih pelan."),
        ("Does my child have to get loud to be heard here?",
         "Apakah anak saya harus mengeraskan suara agar didengar di sini?"),
        ("\"I can hear you. I'm listening.\"",
         "\"Mama/Papa dengar. Mama/Papa mendengarkan.\""),
    ),
    219: d(
        ("Running away in public",
         "Berlari menjauh di tempat umum"),
        ("This one is genuinely a safety issue, so it is handled differently from the rest. "
         "The rule is absolute and taught in advance, not negotiated in a car park.\n\n"
         "Practise it somewhere safe, hold hands where the risk is real, and keep the "
         "response consistent and unfrightening — fear teaches poorly and this rule needs "
         "to hold under stress.",
         "Yang ini sungguh soal keselamatan, jadi ditangani berbeda dari yang lain. "
         "Aturannya mutlak dan diajarkan sejak awal, bukan dinegosiasikan di tempat parkir.\n\n"
         "Latih di tempat yang aman, pegang tangan di tempat yang risikonya nyata, dan jaga "
         "responsnya tetap konsisten dan tidak menakutkan — rasa takut mengajarkan dengan "
         "buruk, dan aturan ini harus bertahan saat tertekan."),
        ("Rehearsing \"stop\" as a game in a safe place builds a reflex that works when it "
         "actually matters.",
         "Melatih \"berhenti\" sebagai permainan di tempat aman membangun refleks yang "
         "bekerja saat benar-benar dibutuhkan."),
        ("Practise the stopping rule somewhere safe today.",
         "Latih aturan berhenti di tempat yang aman hari ini."),
        ("Has my child ever practised this rule when nothing was at stake?",
         "Pernahkah anak saya melatih aturan ini saat tak ada risiko?"),
        ("\"When I say stop, feet stop. Let's practise.\"",
         "\"Kalau Mama/Papa bilang berhenti, kaki berhenti. Ayo latihan.\""),
    ),
    220: d(
        ("Lying",
         "Berbohong"),
        ("Most childhood lying is fear-driven rather than character-driven. Children lie to "
         "avoid a reaction they expect, which means the size of your reaction is one of the "
         "main inputs into how often they lie.\n\n"
         "The strategy is to make truth cheaper than concealment — which means responding "
         "to a confession more gently than to a discovery, every time.",
         "Sebagian besar kebohongan anak didorong rasa takut, bukan karakter. Anak berbohong "
         "untuk menghindari reaksi yang mereka perkirakan, artinya besarnya reaksi Anda "
         "adalah salah satu masukan utama seberapa sering mereka berbohong.\n\n"
         "Strateginya adalah membuat kejujuran lebih murah daripada menyembunyikan — artinya "
         "menanggapi pengakuan lebih lembut daripada menanggapi ketahuan, setiap kali."),
        ("Avoid the trap question. Asking \"did you do this?\" when you already know invites "
         "a lie; saying \"I can see what happened, tell me about it\" does not.",
         "Hindari pertanyaan jebakan. Bertanya \"kamu yang melakukan ini?\" padahal Anda sudah "
         "tahu mengundang kebohongan; berkata \"Mama lihat apa yang terjadi, ceritakan\" tidak."),
        ("Thank your child for one hard truth today before addressing anything else.",
         "Berterima kasihlah atas satu kejujuran yang berat hari ini sebelum membahas hal lain."),
        ("From my child's view, is honesty safer than hiding?",
         "Dari sudut pandang anak saya, apakah jujur lebih aman daripada menyembunyikan?"),
        ("\"Thank you for telling me. That was brave.\"",
         "\"Terima kasih sudah cerita. Itu berani.\""),
    ),
    221: d(
        ("Stealing",
         "Mengambil yang bukan miliknya"),
        ("In young children, taking is often a developmental matter — ownership is a "
         "concept that takes years to fully form. In older children it usually signals "
         "something else: impulse difficulty, social pressure, or an unmet need.\n\n"
         "Handle it calmly and require restitution. Shame is especially counterproductive "
         "here, because a child who feels defined as a thief has little reason to stop.",
         "Pada anak kecil, mengambil sering soal perkembangan — kepemilikan adalah konsep "
         "yang butuh bertahun-tahun untuk terbentuk penuh. Pada anak yang lebih besar, ia "
         "biasanya menandakan hal lain: kesulitan menahan dorongan, tekanan sosial, atau "
         "kebutuhan yang tak terpenuhi.\n\n"
         "Tangani dengan tenang dan minta perbaikan. Rasa malu sangat kontraproduktif di "
         "sini, karena anak yang merasa dilabeli pencuri tak punya banyak alasan untuk berhenti."),
        ("Returning the item together — walking in with them rather than sending them — "
         "teaches accountability without public humiliation.",
         "Mengembalikan barangnya bersama-sama — masuk bersamanya, bukan menyuruhnya sendiri "
         "— mengajarkan tanggung jawab tanpa mempermalukan di depan umum."),
        ("If it happens, require return and repair, calmly and privately.",
         "Jika terjadi, minta pengembalian dan perbaikan, dengan tenang dan secara pribadi."),
        ("Would my reaction make it safer to hide this next time?",
         "Apakah reaksi saya akan membuat lebih aman untuk menyembunyikannya lain kali?"),
        ("\"We're going to put this right together.\"",
         "\"Kita akan membereskan ini bersama-sama.\""),
    ),
    222: d(
        ("Swearing",
         "Berkata kasar"),
        ("Young children swear because a word produced a spectacular reaction. Older "
         "children swear to belong, to test, or because everyone around them does.\n\n"
         "A big reaction is fuel for the first group and evidence of a button for the "
         "second. A flat, brief, unimpressed correction works better than outrage in both "
         "cases.",
         "Anak kecil berkata kasar karena satu kata menghasilkan reaksi yang spektakuler. "
         "Anak yang lebih besar berkata kasar untuk diterima, untuk menguji, atau karena "
         "semua orang di sekitarnya begitu.\n\n"
         "Reaksi besar adalah bahan bakar bagi kelompok pertama dan bukti adanya tombol bagi "
         "kelompok kedua. Teguran yang datar, singkat, dan tak terkesan lebih berhasil "
         "daripada kemarahan pada keduanya."),
        ("Worth checking honestly where the word was learned. Households often supply the "
         "vocabulary they then punish.",
         "Layak diperiksa dengan jujur di mana kata itu dipelajari. Rumah sering menyediakan "
         "kosakata yang kemudian dihukumnya."),
        ("Respond flatly rather than dramatically to one word today.",
         "Tanggapi satu kata dengan datar, bukan dramatis, hari ini."),
        ("Where did my child learn that word?",
         "Di mana anak saya belajar kata itu?"),
        ("\"We don't use that one. Try again.\"",
         "\"Kita tidak pakai kata itu. Coba lagi.\""),
    ),
    223: d(
        ("Rudeness",
         "Ketidaksopanan"),
        ("Rudeness is often a poorly expressed need for autonomy or a feeling with no "
         "better outlet. That does not make it acceptable, and it does change the response.\n\n"
         "Name the behaviour and the alternative in one calm sentence, and address it in "
         "private. Rudeness corrected in front of an audience almost always escalates.",
         "Ketidaksopanan sering adalah kebutuhan akan otonomi yang diungkapkan dengan buruk, "
         "atau perasaan tanpa saluran yang lebih baik. Itu tidak membuatnya bisa diterima, "
         "dan memang mengubah responsnya.\n\n"
         "Sebutkan perilakunya dan alternatifnya dalam satu kalimat yang tenang, dan bahas "
         "secara pribadi. Ketidaksopanan yang ditegur di depan penonton hampir selalu memburuk."),
        ("Modelling matters more than correcting here. A household where adults are courteous "
         "to children produces courteous children far more reliably than one that demands it.",
         "Keteladanan lebih penting daripada teguran di sini. Rumah yang orang dewasanya "
         "sopan kepada anak menghasilkan anak yang sopan jauh lebih andal daripada rumah yang menuntutnya."),
        ("Correct one instance of rudeness privately today, with the alternative attached.",
         "Tegur satu ketidaksopanan secara pribadi hari ini, dengan alternatifnya disertakan."),
        ("Am I courteous to my child in the way I expect them to be to me?",
         "Apakah saya sopan kepada anak dengan cara yang saya harapkan dia sopan kepada saya?"),
        ("\"Not like that. Say it again properly.\"",
         "\"Bukan begitu. Ulangi dengan baik.\""),
    ),
    224: d(
        ("Backtalk",
         "Membantah"),
        ("Backtalk sits awkwardly between disrespect and healthy self-advocacy, and telling "
         "them apart matters. A child who can disagree respectfully has a genuinely "
         "valuable skill — including for refusing adults who should be refused.\n\n"
         "Correct the tone, keep the right to disagree. \"You can tell me you think that's "
         "unfair. Not in that voice.\"",
         "Membantah berada di posisi canggung antara tidak hormat dan membela diri secara "
         "sehat, dan membedakannya penting. Anak yang bisa berbeda pendapat dengan hormat "
         "punya keterampilan yang sungguh berharga — termasuk untuk menolak orang dewasa "
         "yang memang harus ditolak.\n\n"
         "Betulkan nadanya, pertahankan haknya untuk berbeda pendapat. \"Kamu boleh bilang "
         "menurutmu itu tidak adil. Bukan dengan nada itu.\""),
        ("Shutting down all disagreement produces a child who complies with everyone, which "
         "is not the safety it appears to be.",
         "Membungkam semua perbedaan pendapat menghasilkan anak yang menurut kepada siapa "
         "pun — dan itu bukan keamanan seperti yang tampaknya."),
        ("Separate the tone from the content in one disagreement today.",
         "Pisahkan nada dari isinya dalam satu perbedaan pendapat hari ini."),
        ("Do I want a child who never argues, or one who argues well?",
         "Saya ingin anak yang tak pernah membantah, atau yang membantah dengan baik?"),
        ("\"You can disagree. Try that again respectfully.\"",
         "\"Kamu boleh tidak setuju. Coba ulangi dengan hormat.\""),
    ),
    225: d(
        ("Whining",
         "Merengek"),
        ("Whining is engineered to be hard to ignore, and it almost always signals "
         "depletion — tiredness, hunger, or a need for connection unmet in a better way.\n\n"
         "Correcting the tone while ignoring the need produces more whining. Meet the need "
         "first; teach the tone later, when everyone is calm and nothing is at stake.",
         "Rengekan memang dirancang agar sulit diabaikan, dan hampir selalu menandakan "
         "kehabisan tenaga — lelah, lapar, atau kebutuhan akan kedekatan yang tak terpenuhi "
         "dengan cara yang lebih baik.\n\n"
         "Membetulkan nadanya sambil mengabaikan kebutuhannya menghasilkan lebih banyak "
         "rengekan. Penuhi kebutuhannya dulu; ajarkan nadanya nanti, saat semua tenang dan "
         "tak ada yang dipertaruhkan."),
        ("\"You sound like you're running out of energy — come here\" ends whining faster "
         "than \"use your normal voice\" almost every time.",
         "\"Sepertinya tenagamu habis — sini\" menghentikan rengekan lebih cepat daripada "
         "\"pakai suara biasa\" hampir setiap kali."),
        ("Answer the need behind one whine today rather than the sound.",
         "Jawab kebutuhan di balik satu rengekan hari ini, bukan bunyinya."),
        ("What does the whining always come just after?",
         "Rengekan itu selalu muncul tepat setelah apa?"),
        ("\"You sound worn out. Come sit a minute.\"",
         "\"Sepertinya kamu capek. Sini duduk sebentar.\""),
    ),
    226: d(
        ("Bedwetting without shame",
         "Mengompol tanpa mempermalukan"),
        ("Bedwetting is almost never within a child's control. It is common, largely "
         "developmental, and frequently runs in families — a parent who wet the bed late "
         "often has a child who does.\n\n"
         "Shame makes it worse and lasts far longer than the bedwetting. Keep it practical "
         "and matter-of-fact, and speak to a doctor if it persists or restarts after a dry "
         "period.",
         "Mengompol hampir tak pernah dalam kendali anak. Ia umum, sebagian besar soal "
         "perkembangan, dan sering menurun dalam keluarga — orang tua yang dulu mengompol "
         "sampai besar sering punya anak yang begitu juga.\n\n"
         "Rasa malu memperburuknya dan bertahan jauh lebih lama daripada mengompolnya. Jaga "
         "tetap praktis dan biasa saja, dan bicarakan dengan dokter jika terus berlanjut "
         "atau muncul lagi setelah periode kering."),
        ("Involving the child in the practical side without blame — carrying the sheets, "
         "not being scolded — preserves dignity while it resolves on its own timeline.",
         "Melibatkan anak dalam sisi praktisnya tanpa menyalahkan — membawa seprainya, tanpa "
         "dimarahi — menjaga martabatnya sementara hal itu selesai sesuai waktunya sendiri."),
        ("Keep tonight's response entirely matter-of-fact, whatever happens.",
         "Jaga respons malam ini sepenuhnya biasa saja, apa pun yang terjadi."),
        ("Does my child feel ashamed of something they cannot control?",
         "Apakah anak saya merasa malu atas sesuatu yang tak bisa dia kendalikan?"),
        ("\"Bodies do this sometimes. Let's sort the sheets.\"",
         "\"Tubuh kadang begitu. Ayo kita ganti seprainya.\""),
    ),
    227: d(
        ("Toilet resistance",
         "Menolak toilet"),
        ("Toilet training is one of the few areas where a child holds complete physical "
         "control, which is exactly why pressure backfires so reliably.\n\n"
         "Resistance usually means the child is not ready, or that the process has become a "
         "battleground. Backing off entirely for a few weeks resolves more cases than any "
         "amount of encouragement.",
         "Toilet training adalah salah satu dari sedikit wilayah di mana anak memegang "
         "kendali fisik sepenuhnya, dan justru itulah sebabnya tekanan selalu berbalik.\n\n"
         "Penolakan biasanya berarti anak belum siap, atau prosesnya sudah menjadi medan "
         "pertempuran. Mundur sepenuhnya selama beberapa minggu menyelesaikan lebih banyak "
         "kasus daripada dorongan sebanyak apa pun."),
        ("Nobody arrives at adulthood still in nappies. The timeline genuinely does not "
         "predict anything about the child.",
         "Tak ada yang sampai dewasa masih memakai popok. Garis waktunya sungguh tidak "
         "meramalkan apa pun tentang anaknya."),
        ("Take all pressure off this for a week if it has become a fight.",
         "Lepaskan semua tekanan soal ini selama seminggu jika sudah menjadi pertengkaran."),
        ("Whose timeline are we actually working to?",
         "Sebenarnya kami mengikuti garis waktu siapa?"),
        ("\"When you're ready. No rush at all.\"",
         "\"Kalau kamu sudah siap. Tidak buru-buru.\""),
    ),
    228: d(
        ("Sleep refusal",
         "Menolak tidur"),
        ("Sleep refusal usually has one of three causes: not actually tired, anxious about "
         "separation, or the routine has become a negotiation.\n\n"
         "Each needs a different answer — a later start, more connection before sleep, or a "
         "fixed sequence held without discussion. Applying the wrong one keeps everyone up.",
         "Menolak tidur biasanya punya salah satu dari tiga sebab: memang belum mengantuk, "
         "cemas berpisah, atau rutinitasnya sudah menjadi negosiasi.\n\n"
         "Masing-masing butuh jawaban berbeda — mulai lebih malam, lebih banyak kedekatan "
         "sebelum tidur, atau urutan tetap yang dipegang tanpa diskusi. Menerapkan yang "
         "salah membuat semua orang tetap terjaga."),
        ("The endless requests — water, one more story, a question — are usually about "
         "separation rather than thirst. More connection earlier tends to shorten them.",
         "Permintaan tanpa akhir — air, satu cerita lagi, satu pertanyaan — biasanya soal "
         "perpisahan, bukan haus. Lebih banyak kedekatan lebih awal cenderung memperpendeknya."),
        ("Work out which of the three is behind tonight's resistance.",
         "Cari tahu mana dari ketiganya yang ada di balik perlawanan malam ini."),
        ("Is my child not tired, or not ready to be apart from me?",
         "Apakah anak saya belum mengantuk, atau belum siap berpisah dari saya?"),
        ("\"I'll check on you in five minutes. I always do.\"",
         "\"Mama/Papa lihat lagi lima menit lagi. Selalu begitu.\""),
    ),
    229: d(
        ("Separation difficulties",
         "Kesulitan berpisah"),
        ("Separation distress is a sign of attachment working, not of a spoiled child. It "
         "peaks at predictable ages and returns during change — a new school, a new "
         "sibling, a move.\n\n"
         "Long goodbyes make it worse and slipping away makes it much worse. A short, warm, "
         "identical ritual with a clear promise of return works best.",
         "Kesedihan berpisah adalah tanda kelekatan sedang bekerja, bukan tanda anak dimanja. "
         "Ia memuncak di usia yang bisa diperkirakan dan kembali saat ada perubahan — sekolah "
         "baru, adik baru, pindah rumah.\n\n"
         "Perpisahan yang berlarut memperburuk, dan pergi diam-diam jauh lebih memperburuk. "
         "Ritual yang singkat, hangat, selalu sama, dengan janji kembali yang jelas paling ampuh."),
        ("Sneaking out avoids one minute of crying and costs weeks of vigilance, because "
         "the child learns you might vanish at any moment.",
         "Pergi mengendap menghindari satu menit tangisan dan menghabiskan berminggu-minggu "
         "kewaspadaan, karena anak belajar Anda bisa menghilang kapan saja."),
        ("Use exactly the same goodbye ritual today as yesterday.",
         "Gunakan ritual perpisahan yang persis sama hari ini seperti kemarin."),
        ("Is my goodbye predictable enough to lean on?",
         "Apakah cara saya berpamitan cukup bisa ditebak untuk jadi pegangan?"),
        ("\"Kiss, wave, and I'm back after lunch.\"",
         "\"Cium, lambai, dan Mama/Papa kembali setelah makan siang.\""),
    ),
    230: d(
        ("School refusal basics",
         "Dasar penolakan sekolah"),
        ("School refusal is rarely laziness. Underneath it usually sits anxiety, a social "
         "difficulty, an academic struggle the child is ashamed of, or something happening "
         "at school nobody has been told about.\n\n"
         "Find the cause before applying pressure. Persistent refusal warrants a "
         "conversation with the school and, often, a professional — this is one to take "
         "seriously early.",
         "Penolakan sekolah jarang kemalasan. Di baliknya biasanya duduk kecemasan, kesulitan "
         "sosial, perjuangan akademik yang anak malu mengakuinya, atau sesuatu yang terjadi di "
         "sekolah yang belum diceritakan kepada siapa pun.\n\n"
         "Temukan sebabnya sebelum menerapkan tekanan. Penolakan yang terus berlanjut layak "
         "dibicarakan dengan sekolah dan, sering kali, dengan tenaga profesional — yang ini "
         "perlu ditanggapi serius sejak awal."),
        ("Ask what specifically about school is hard. \"I don't want to go\" is a headline; "
         "the story underneath is usually specific and often fixable.",
         "Tanyakan bagian mana dari sekolah yang terasa berat. \"Aku tidak mau sekolah\" adalah "
         "judulnya; cerita di baliknya biasanya spesifik dan sering bisa dibereskan."),
        ("Ask what specifically is hard, without arguing about attendance today.",
         "Tanyakan bagian mana yang terasa berat, tanpa berdebat soal kehadiran hari ini."),
        ("What might my child not have told me about school?",
         "Apa yang mungkin belum anak ceritakan kepada saya tentang sekolah?"),
        ("\"Which part is the hardest part?\"",
         "\"Bagian mana yang paling berat?\""),
    ),
    231: d(
        ("Homework avoidance",
         "Menghindari PR"),
        ("Avoidance and laziness look identical from outside and are entirely different "
         "inside. A child who expects to fail avoids starting; the avoidance protects them "
         "from evidence of not being clever.\n\n"
         "Shrink the first step until it is trivially achievable, and sit nearby. Most "
         "resistance lives at the beginning, not in the middle.",
         "Menghindar dan malas tampak identik dari luar dan sama sekali berbeda di dalam. "
         "Anak yang memperkirakan dirinya gagal menghindari memulai; penghindaran itu "
         "melindunginya dari bukti bahwa dia tidak pintar.\n\n"
         "Perkecil langkah pertama sampai sepele untuk dicapai, dan duduk di dekatnya. "
         "Sebagian besar perlawanan tinggal di awal, bukan di tengah."),
        ("\"Just the first question, then we'll see\" gets more done than any conversation "
         "about responsibility.",
         "\"Soal pertama saja dulu, nanti kita lihat\" menyelesaikan lebih banyak daripada "
         "percakapan apa pun tentang tanggung jawab."),
        ("Shrink one task to a trivially small first step today.",
         "Perkecil satu tugas menjadi langkah pertama yang sangat kecil hari ini."),
        ("What size does a task have to be before my child will start it?",
         "Sebesar apa tugasnya supaya anak saya mau memulainya?"),
        ("\"Just the first line. I'll sit here.\"",
         "\"Baris pertama saja. Mama/Papa duduk di sini.\""),
    ),
    232: d(
        ("Perfectionism in children",
         "Perfeksionisme pada anak"),
        ("Perfectionism looks like high standards and functions as fear. A perfectionist "
         "child avoids anything they might not excel at, which narrows their world "
         "considerably over time.\n\n"
         "Praise effort and strategy rather than results, and let them see you fail at "
         "something and be fine. Your visible relationship with your own mistakes is the "
         "strongest teaching available.",
         "Perfeksionisme tampak seperti standar tinggi dan berfungsi sebagai rasa takut. Anak "
         "perfeksionis menghindari apa pun yang mungkin tak dia kuasai, dan itu mempersempit "
         "dunianya cukup jauh seiring waktu.\n\n"
         "Puji usaha dan strategi, bukan hasil, dan biarkan dia melihat Anda gagal pada "
         "sesuatu dan baik-baik saja. Hubungan Anda yang terlihat dengan kesalahan Anda "
         "sendiri adalah pengajaran terkuat yang tersedia."),
        ("Perfectionist children usually have a perfectionist parent. That is not blame — "
         "it is the most useful place to start.",
         "Anak perfeksionis biasanya punya orang tua perfeksionis. Ini bukan menyalahkan — "
         "ini tempat paling berguna untuk memulai."),
        ("Fail visibly at something small today and be visibly fine about it.",
         "Gagal secara terlihat pada sesuatu yang kecil hari ini dan tunjukkan Anda baik-baik saja."),
        ("What does my child see me do when I get something wrong?",
         "Apa yang anak lihat saya lakukan ketika saya melakukan kesalahan?"),
        ("\"I got that wrong. Good thing it's not important.\"",
         "\"Mama/Papa salah tadi. Untung bukan hal penting.\""),
    ),
    233: d(
        ("Social exclusion and hurt feelings",
         "Dikucilkan dan perasaan terluka"),
        ("Exclusion hurts genuinely, and adult instinct is to minimise it — \"find other "
         "friends\", \"they're not worth it\". Both land as dismissal.\n\n"
         "Acknowledge the hurt fully first. Only afterwards, and only if wanted, move to "
         "what might help. Being believed about the pain matters more than the strategy.",
         "Dikucilkan itu sungguh menyakitkan, dan naluri orang dewasa adalah mengecilkannya "
         "— \"cari teman lain\", \"dia tidak sepadan\". Keduanya terasa sebagai pengabaian.\n\n"
         "Akui lukanya sepenuhnya dulu. Baru setelahnya, dan hanya jika diinginkan, beralih ke "
         "apa yang mungkin membantu. Dipercaya soal rasa sakitnya lebih penting daripada strateginya."),
        ("Persistent, targeted exclusion is bullying and warrants the school being told. "
         "The line is repetition and intent.",
         "Pengucilan yang terus-menerus dan terarah adalah perundungan dan layak dilaporkan "
         "ke sekolah. Batasnya adalah pengulangan dan kesengajaan."),
        ("Acknowledge one social hurt fully today before offering any strategy.",
         "Akui satu luka sosial sepenuhnya hari ini sebelum menawarkan strategi apa pun."),
        ("Does my child believe I take their social world seriously?",
         "Apakah anak percaya saya menganggap serius dunia sosialnya?"),
        ("\"That really hurts. I'm glad you told me.\"",
         "\"Itu sungguh menyakitkan. Mama/Papa senang kamu cerita.\""),
    ),
    234: d(
        ("Fear of failure",
         "Takut gagal"),
        ("Fear of failure produces avoidance, and avoidance produces less practice, which "
         "makes failure more likely. It is a loop, and it tightens quietly over years.\n\n"
         "Break it by making failure ordinary and survivable in your household — talked "
         "about, not hidden, and never punished when it was the result of a genuine attempt.",
         "Takut gagal menghasilkan penghindaran, dan penghindaran menghasilkan lebih sedikit "
         "latihan, yang membuat kegagalan lebih mungkin. Ini lingkaran, dan ia mengencang "
         "diam-diam selama bertahun-tahun.\n\n"
         "Putuskan dengan membuat kegagalan menjadi biasa dan bisa dilalui di rumah Anda — "
         "dibicarakan, tidak disembunyikan, dan tak pernah dihukum bila itu hasil dari usaha yang sungguh."),
        ("Talking about your own failures at dinner does more than any encouragement. It "
         "makes failure a normal part of a life, rather than a verdict on one.",
         "Menceritakan kegagalan Anda sendiri saat makan malam lebih berguna daripada "
         "dorongan apa pun. Ia menjadikan kegagalan bagian wajar dari sebuah hidup, bukan "
         "vonis atasnya."),
        ("Tell your child about something you failed at today.",
         "Ceritakan kepada anak tentang sesuatu yang Anda gagal lakukan hari ini."),
        ("Is failure allowed to be ordinary in our house?",
         "Apakah kegagalan boleh menjadi hal biasa di rumah kami?"),
        ("\"I tried and it didn't work. I'll try again.\"",
         "\"Mama/Papa mencoba dan gagal. Nanti coba lagi.\""),
    ),
    235: d(
        ("Excessive reassurance-seeking",
         "Terlalu sering mencari penenangan"),
        ("Repeated questions — am I okay, do you still love me, will it be fine — usually "
         "signal anxiety rather than neediness. Each answer relieves it briefly and, over "
         "time, feeds the loop.\n\n"
         "Answer once warmly, then shift to building their own capacity: what do you think? "
         "That transfers the reassurance from you to them, which is the version that lasts.",
         "Pertanyaan yang berulang — aku baik-baik saja kan, Mama masih sayang aku kan, nanti "
         "akan baik-baik saja kan — biasanya menandakan kecemasan, bukan manja. Setiap jawaban "
         "meredakannya sebentar dan, seiring waktu, memberi makan lingkarannya.\n\n"
         "Jawab sekali dengan hangat, lalu beralih membangun kemampuannya sendiri: menurutmu "
         "bagaimana? Itu memindahkan penenangan dari Anda kepadanya — versi yang bertahan."),
        ("\"You've asked me that a few times — what does your own answer say?\" said warmly "
         "builds something an answer from you never can.",
         "\"Kamu sudah tanya itu beberapa kali — menurut jawabanmu sendiri bagaimana?\" yang "
         "diucapkan hangat membangun sesuatu yang tak bisa dibangun oleh jawaban Anda."),
        ("Answer once, then hand one reassurance question back gently today.",
         "Jawab sekali, lalu kembalikan satu pertanyaan penenangan dengan lembut hari ini."),
        ("Am I relieving my child's anxiety or feeding it?",
         "Apakah saya meredakan kecemasan anak atau memberinya makan?"),
        ("\"What do you think? I trust your read.\"",
         "\"Menurutmu bagaimana? Mama/Papa percaya penilaianmu.\""),
    ),
    236: d(
        ("Nail biting and habits",
         "Menggigit kuku dan kebiasaan lain"),
        ("Body-focused habits — nail biting, hair twisting, skin picking — are usually "
         "self-soothing rather than defiance. They increase with stress and are largely "
         "unconscious.\n\n"
         "Punishment and constant correction reliably make them worse by adding shame to "
         "the stress that caused them. Reducing the underlying stress works better than "
         "attacking the habit.",
         "Kebiasaan yang berpusat pada tubuh — menggigit kuku, memilin rambut, mengelupas "
         "kulit — biasanya cara menenangkan diri, bukan pembangkangan. Ia meningkat saat "
         "stres dan sebagian besar tidak disadari.\n\n"
         "Hukuman dan teguran terus-menerus selalu memperburuknya dengan menambahkan rasa "
         "malu di atas stres yang menyebabkannya. Mengurangi stres yang mendasarinya lebih "
         "berhasil daripada menyerang kebiasaannya."),
        ("Offering a substitute — something to hold or fidget with — works better than "
         "asking a child to simply stop doing something they are not aware of doing.",
         "Menawarkan pengganti — sesuatu untuk dipegang atau dimainkan — lebih berhasil "
         "daripada meminta anak berhenti melakukan sesuatu yang tak dia sadari sedang dia lakukan."),
        ("Notice when the habit increases today, and treat that as the information.",
         "Perhatikan kapan kebiasaannya meningkat hari ini, dan perlakukan itu sebagai informasi."),
        ("What is happening around my child when this increases?",
         "Apa yang sedang terjadi di sekitar anak saya saat ini meningkat?"),
        ("\"Here, hold this instead.\"",
         "\"Ini, pegang ini saja.\""),
    ),
    237: d(
        ("Screen dependency patterns",
         "Pola ketergantungan layar"),
        ("Screens are engineered by large teams to be difficult to stop, so a child "
         "struggling to stop is not displaying weak character.\n\n"
         "Watch the pattern rather than the total: is screen time replacing sleep, "
         "friendship, movement or food? Displacement matters more than duration, and it is "
         "the more useful thing to measure.",
         "Layar dirancang oleh tim besar agar sulit dihentikan, jadi anak yang kesulitan "
         "berhenti bukan sedang menunjukkan karakter yang lemah.\n\n"
         "Perhatikan polanya, bukan totalnya: apakah waktu layar menggantikan tidur, "
         "pertemanan, gerak, atau makan? Penggeseran lebih penting daripada durasi, dan itu "
         "hal yang lebih berguna untuk diukur."),
        ("Agreeing the end point before a session begins turns you from the person who "
         "takes it away into the person keeping an agreement.",
         "Menyepakati titik akhir sebelum sesi dimulai mengubah Anda dari orang yang "
         "merebutnya menjadi orang yang menepati kesepakatan."),
        ("Check what screens are displacing this week, rather than counting hours.",
         "Periksa apa yang digeser oleh layar minggu ini, bukan menghitung jamnya."),
        ("What is screen time taking the place of in my child's day?",
         "Waktu layar menggantikan apa dalam hari anak saya?"),
        ("\"What did the screen take the place of today?\"",
         "\"Hari ini layar menggantikan kegiatan apa?\""),
    ),
    238: d(
        ("Risky internet behavior basics",
         "Dasar perilaku berisiko di internet"),
        ("The protective factor that matters most online is not monitoring software. It is "
         "whether a child will tell you when something goes wrong.\n\n"
         "That depends almost entirely on how you responded the last few times they brought "
         "you something difficult. A child who fears losing their device will hide exactly "
         "the things you most need to know.",
         "Faktor pelindung yang paling penting di dunia daring bukan perangkat lunak "
         "pengawas. Melainkan apakah anak akan memberi tahu Anda ketika ada yang tidak beres.\n\n"
         "Itu hampir sepenuhnya bergantung pada bagaimana Anda menanggapi beberapa kali "
         "terakhir dia membawakan sesuatu yang sulit. Anak yang takut kehilangan gawainya "
         "akan menyembunyikan persis hal-hal yang paling perlu Anda ketahui."),
        ("Say the rule out loud in advance: \"if anything online worries you, you can tell "
         "me and you will not lose your device for it.\" Then keep that promise.",
         "Ucapkan aturannya sejak awal: \"kalau ada hal di internet yang membuatmu khawatir, "
         "kamu boleh cerita dan gawaimu tidak akan disita karena itu.\" Lalu tepati janji itu."),
        ("Make that promise explicitly today, and mean it.",
         "Sampaikan janji itu secara jelas hari ini, dan sungguh-sungguhi."),
        ("Would my child tell me if something frightening happened online?",
         "Apakah anak saya akan bercerita jika sesuatu yang menakutkan terjadi di internet?"),
        ("\"Tell me and you won't lose it. That's a promise.\"",
         "\"Cerita saja, gawaimu tidak akan disita. Itu janji.\""),
    ),
    239: d(
        ("When behavior may signal anxiety",
         "Ketika perilaku mungkin menandakan kecemasan"),
        ("Anxiety in children frequently looks like something else: anger, refusal, "
         "control-seeking, stomach aches, sleep trouble, or an insistence on things being "
         "exactly right.\n\n"
         "Anxious children are often described as difficult long before anyone recognises "
         "the anxiety. If a behaviour is persistent, worsening, and clusters around "
         "uncertainty or separation, it is worth a professional opinion.",
         "Kecemasan pada anak sering tampak seperti hal lain: marah, menolak, mencari "
         "kendali, sakit perut, sulit tidur, atau bersikeras segalanya harus persis benar.\n\n"
         "Anak yang cemas sering disebut sulit jauh sebelum ada yang mengenali kecemasannya. "
         "Jika sebuah perilaku terus berlanjut, memburuk, dan menumpuk di sekitar "
         "ketidakpastian atau perpisahan, layak untuk meminta pendapat profesional."),
        ("Reassurance relieves anxiety briefly and can strengthen it over time. Building a "
         "child's own coping capacity is the version that lasts — and professional guidance "
         "genuinely helps here.",
         "Penenangan meredakan kecemasan sebentar dan bisa menguatkannya seiring waktu. "
         "Membangun kemampuan anak mengatasi sendiri adalah versi yang bertahan — dan "
         "panduan profesional sungguh membantu di sini."),
        ("Note whether one difficult behaviour clusters around uncertainty or separation.",
         "Catat apakah satu perilaku sulit menumpuk di sekitar ketidakpastian atau perpisahan."),
        ("Could what I have been calling difficult actually be frightened?",
         "Mungkinkah yang selama ini saya sebut sulit sebenarnya adalah ketakutan?"),
        ("\"Something's worrying you. Let's work it out together.\"",
         "\"Ada yang membuatmu khawatir. Ayo kita cari tahu bersama.\""),
    ),
    240: d(
        ("When behavior may signal ADHD or neurodivergence",
         "Ketika perilaku mungkin menandakan ADHD atau neurodivergensi"),
        ("Some children are not choosing the behaviour that frustrates you, and no amount "
         "of consistency will change it, because the difficulty is in how their brain is "
         "wired rather than in their willingness.\n\n"
         "Signs worth noticing: difficulties present across every setting, not just home; "
         "far outside what is typical for the age; persisting despite genuinely consistent "
         "parenting; and causing real distress. That combination deserves a proper "
         "assessment — this guide cannot diagnose, and an early accurate answer changes a "
         "childhood.",
         "Sebagian anak tidak sedang memilih perilaku yang membuat Anda frustrasi, dan "
         "sekonsisten apa pun Anda tak akan mengubahnya, karena kesulitannya ada pada cara "
         "otaknya tersusun, bukan pada kemauannya.\n\n"
         "Tanda yang layak diperhatikan: kesulitan muncul di semua tempat, bukan hanya di "
         "rumah; jauh di luar yang lazim untuk usianya; bertahan meski pengasuhan sungguh "
         "konsisten; dan menimbulkan kesusahan yang nyata. Kombinasi itu layak mendapat "
         "pemeriksaan yang semestinya — panduan ini tidak bisa mendiagnosis, dan jawaban yang "
         "tepat sejak dini mengubah sebuah masa kanak."),
        ("Many parents delay assessment out of fear of a label. In practice an accurate "
         "understanding usually reduces blame — of the child and of the parents.",
         "Banyak orang tua menunda pemeriksaan karena takut label. Dalam praktik, pemahaman "
         "yang tepat biasanya justru mengurangi saling menyalahkan — pada anak dan pada orang tuanya."),
        ("If this describes your child, write down what you have noticed and take it to a "
         "professional.",
         "Jika ini menggambarkan anak Anda, tuliskan apa yang Anda perhatikan dan bawa ke tenaga profesional."),
        ("Have I been asking my child for something they genuinely cannot yet do?",
         "Apakah selama ini saya meminta anak melakukan sesuatu yang sungguh belum bisa dia lakukan?"),
        ("\"This isn't you being naughty. Let's get help understanding it.\"",
         "\"Ini bukan kamu nakal. Ayo kita cari bantuan untuk memahaminya.\""),
    ),
    241: d(
        ("Weekly reflection",
         "Refleksi mingguan"),
        ("This chapter asks for one discipline: diagnose before intervening. A behaviour "
         "that has survived several months of consistent consequences is telling you the "
         "diagnosis was wrong, not that the consequence was too small.\n\n"
         "Take the behaviour that has troubled you longest and run it through tool 8, the "
         "ABC log, across six incidents. The pattern is almost always visible by the "
         "fourth.",
         "Bab ini meminta satu disiplin: diagnosis sebelum bertindak. Perilaku yang bertahan "
         "melewati beberapa bulan konsekuensi yang konsisten sedang memberi tahu Anda bahwa "
         "diagnosisnya salah, bukan bahwa konsekuensinya kurang besar.\n\n"
         "Ambil perilaku yang paling lama mengganggu Anda dan jalankan lewat alat 8, catatan "
         "ABC, selama enam kejadian. Polanya hampir selalu terlihat pada kejadian keempat."),
        ("If a behaviour is persistent, worsening, unusual for the age, or significantly "
         "affecting family life, that is the point to involve a professional rather than "
         "keep adjusting alone.",
         "Jika sebuah perilaku terus berlanjut, memburuk, tidak lazim untuk usianya, atau "
         "sangat memengaruhi kehidupan keluarga, itulah saatnya melibatkan tenaga "
         "profesional, bukan terus menyesuaikan sendirian."),
        ("Start an ABC log on your most persistent behaviour this week.",
         "Mulai catatan ABC untuk perilaku Anda yang paling membandel minggu ini."),
        ("What function has this behaviour been serving all along?",
         "Fungsi apa yang selama ini dijalankan perilaku ini?"),
        ("\"What is this behaviour doing for you?\"",
         "\"Perilaku ini sedang membantumu untuk apa?\""),
    ),
}
