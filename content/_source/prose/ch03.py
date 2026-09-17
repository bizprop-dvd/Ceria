# Chapter 3 — Parent Self-Regulation (days 62-91)
#
# Grounded in the founder's guidebook chapter 3 ("You cannot regulate your child
# if you cannot regulate yourself") and toolkit tool 3 (Parent Trigger Tracker).
#
# Through-line: the body teaches first; the words come second.

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
    62: d(
        ("Recognizing your parenting triggers",
         "Mengenali pemicu Anda dalam mengasuh"),
        ("A trigger is any moment where your reaction is bigger than the event. That gap "
         "is the signal — it means something older than this moment has been touched.\n\n"
         "Most parents have three or four, and they are remarkably consistent: being "
         "ignored, mess, noise, disrespect, whining, being late. Knowing yours in advance "
         "converts an ambush into something you can prepare for.",
         "Pemicu adalah momen ketika reaksi Anda lebih besar daripada peristiwanya. Jarak "
         "itulah sinyalnya — artinya ada sesuatu yang lebih tua dari momen ini yang tersentuh.\n\n"
         "Kebanyakan orang tua punya tiga atau empat, dan pemicunya sangat konsisten: "
         "diabaikan, berantakan, berisik, ketidaksopanan, rengekan, terlambat. Mengetahui "
         "milik Anda lebih dulu mengubah serangan mendadak menjadi sesuatu yang bisa Anda siapkan."),
        ("You cannot manage a trigger you have never named. Once named, it announces "
         "itself a few seconds earlier — and those seconds are where the choice lives.",
         "Anda tak bisa mengelola pemicu yang tak pernah Anda namai. Setelah dinamai, ia "
         "mengumumkan dirinya beberapa detik lebih awal — dan di detik-detik itulah pilihan berada."),
        ("Write down your top three triggers today. Keep the list where only you will see it.",
         "Tuliskan tiga pemicu terbesar Anda hari ini. Simpan daftarnya di tempat yang hanya Anda lihat."),
        ("Which of my reactions is consistently bigger than the thing that caused it?",
         "Reaksi saya yang mana yang secara konsisten lebih besar daripada penyebabnya?"),
        ("\"That one always gets me. Now I know.\"",
         "\"Yang itu selalu memancing saya. Sekarang saya tahu.\""),
    ),
    63: d(
        ("Pause before reacting",
         "Jeda sebelum bereaksi"),
        ("Between what happens and what you do there is a gap. It is very short, but it "
         "is real, and almost all of parenting quality lives inside it.\n\n"
         "Widening that gap is the single most useful skill in this chapter. You are not "
         "trying to feel less — you are trying to put two seconds between the feeling and "
         "the response.",
         "Antara apa yang terjadi dan apa yang Anda lakukan ada sebuah jeda. Ia sangat "
         "singkat, tapi nyata, dan hampir seluruh mutu pengasuhan tinggal di dalamnya.\n\n"
         "Melebarkan jeda itu adalah keterampilan paling berguna di bab ini. Anda tidak "
         "sedang berusaha merasa lebih sedikit — Anda sedang berusaha menyisipkan dua detik "
         "antara perasaan dan respons."),
        ("Two seconds is enough to change the sentence that comes out. It is rarely enough "
         "to change the feeling, and it does not need to be.",
         "Dua detik cukup untuk mengubah kalimat yang keluar. Ia jarang cukup untuk mengubah "
         "perasaannya, dan memang tidak perlu."),
        ("Put a two-second pause before your first reaction today. Just the first one.",
         "Sisipkan jeda dua detik sebelum reaksi pertama Anda hari ini. Yang pertama saja."),
        ("What would I have said today if I had waited two more seconds?",
         "Apa yang akan saya katakan hari ini jika saya menunggu dua detik lagi?"),
        ("\"Give me a second.\"",
         "\"Sebentar ya.\""),
    ),
    64: d(
        ("Breathing before speaking",
         "Bernapas sebelum bicara"),
        ("Breathing is not a soft option; it is the fastest available lever on your own "
         "physiology. A long exhale genuinely slows the heart and takes the edge off the "
         "stress response, and it takes about four seconds.\n\n"
         "This matters because your calm is not only for you. Your child's nervous system "
         "is reading yours continuously.",
         "Bernapas bukan pilihan yang lembek; ia tuas tercepat yang tersedia atas fisiologi "
         "Anda sendiri. Embusan napas yang panjang sungguh memperlambat detak jantung dan "
         "meredakan respons stres, dan hanya butuh sekitar empat detik.\n\n"
         "Ini penting karena ketenangan Anda bukan hanya untuk Anda. Sistem saraf anak "
         "membaca sistem saraf Anda terus-menerus."),
        ("One slow out-breath before you speak changes the tone of the sentence more "
         "reliably than deciding to sound calm.",
         "Satu embusan napas pelan sebelum bicara mengubah nada kalimat lebih andal daripada "
         "sekadar memutuskan untuk terdengar tenang."),
        ("Take one long exhale before responding to the first difficulty today.",
         "Ambil satu embusan panjang sebelum menanggapi kesulitan pertama hari ini."),
        ("What does my body do in the second before I lose my temper?",
         "Apa yang tubuh saya lakukan sedetik sebelum saya hilang kesabaran?"),
        ("\"Let me breathe for a second first.\"",
         "\"Mama/Papa tarik napas dulu sebentar.\""),
    ),
    65: d(
        ("Naming your own emotion",
         "Menamai emosi Anda sendiri"),
        ("Saying what you feel, out loud, does two jobs at once. It steadies you — naming "
         "a feeling measurably reduces its intensity — and it shows your child that "
         "feelings can be handled rather than obeyed.\n\n"
         "Name the feeling, not the blame. \"I am frustrated\" teaches. \"You are making me "
         "furious\" hands your child responsibility for your emotional state, which is a "
         "weight no child should carry.",
         "Mengucapkan apa yang Anda rasakan, dengan suara, melakukan dua hal sekaligus. Ia "
         "menenangkan Anda — menamai perasaan terbukti menurunkan intensitasnya — dan "
         "menunjukkan kepada anak bahwa perasaan bisa dikelola, bukan dituruti.\n\n"
         "Namai perasaannya, bukan tuduhannya. \"Mama sedang kesal\" mengajarkan. \"Kamu "
         "membuat Mama marah\" menyerahkan tanggung jawab atas kondisi emosi Anda kepada "
         "anak — beban yang tak seharusnya dipikul anak mana pun."),
        ("\"I'm feeling really frustrated right now, so I'm going to slow down\" models the "
         "whole skill in one sentence.",
         "\"Mama sedang sangat kesal sekarang, jadi Mama akan pelan-pelan dulu\" mencontohkan "
         "seluruh keterampilannya dalam satu kalimat."),
        ("Name one of your own feelings out loud in front of your child today.",
         "Sebutkan satu perasaan Anda sendiri dengan suara di depan anak hari ini."),
        ("Does my child ever hear me name a feeling without blaming someone for it?",
         "Pernahkah anak mendengar saya menyebut perasaan tanpa menyalahkan siapa pun?"),
        ("\"I'm frustrated. That's mine to handle.\"",
         "\"Mama/Papa sedang kesal. Itu urusan Mama/Papa untuk kelola.\""),
    ),
    66: d(
        ("When to step away briefly",
         "Kapan menjauh sejenak"),
        ("Walking away for a minute is not abandoning your child and it is not losing the "
         "argument. It is the adult version of the very skill you keep asking them to "
         "learn.\n\n"
         "The difference between a helpful break and a frightening one is announcement. "
         "Say you are going, say you are coming back, and come back.",
         "Menjauh sebentar bukan meninggalkan anak dan bukan kalah dalam perdebatan. Itu "
         "versi dewasa dari keterampilan yang terus Anda minta anak pelajari.\n\n"
         "Beda antara jeda yang membantu dan yang menakutkan adalah pemberitahuan. Katakan "
         "Anda pergi, katakan Anda akan kembali, lalu kembalilah."),
        ("Silently storming out teaches abandonment. \"I need two minutes, then I'm coming "
         "back\" teaches self-regulation.",
         "Pergi diam-diam sambil membanting mengajarkan ditinggalkan. \"Mama perlu dua menit, "
         "lalu Mama kembali\" mengajarkan pengendalian diri."),
        ("If you need a break today, announce it and return when you said you would.",
         "Jika Anda butuh jeda hari ini, umumkan dan kembalilah tepat seperti yang Anda katakan."),
        ("Do I leave the room in a way that reassures, or in a way that frightens?",
         "Apakah saya meninggalkan ruangan dengan cara yang menenangkan, atau yang menakutkan?"),
        ("\"I need two minutes. I'm coming straight back.\"",
         "\"Mama/Papa perlu dua menit. Nanti langsung kembali.\""),
    ),
    67: d(
        ("Yelling: why it escalates",
         "Berteriak: mengapa justru memperburuk"),
        ("Yelling works the first few times, which is exactly the trap. It raises the "
         "volume of the whole household, requires escalation to keep working, and teaches "
         "children that loudness is how conflict gets resolved.\n\n"
         "It also floods the child, which means the lesson you were trying to deliver "
         "does not land at all. You get compliance and no learning.",
         "Berteriak berhasil beberapa kali pertama, dan itulah jebakannya. Ia menaikkan "
         "volume seluruh rumah, menuntut eskalasi agar tetap mempan, dan mengajarkan anak "
         "bahwa kerasnya suara adalah cara konflik diselesaikan.\n\n"
         "Ia juga membanjiri anak, artinya pelajaran yang ingin Anda sampaikan sama sekali "
         "tidak sampai. Anda mendapat kepatuhan tanpa pembelajaran."),
        ("Notice how a shouted instruction has to be repeated louder next week. That is "
         "the escalation cost, arriving on schedule.",
         "Perhatikan bagaimana instruksi yang diteriakkan harus diulang lebih keras minggu "
         "depan. Itulah biaya eskalasi, datang tepat waktu."),
        ("If you raise your voice today, lower it mid-sentence and start again.",
         "Jika Anda meninggikan suara hari ini, turunkan di tengah kalimat dan mulai lagi."),
        ("What is my yelling actually achieving, once the moment has passed?",
         "Apa yang sebenarnya dicapai teriakan saya, setelah momennya berlalu?"),
        ("\"I'm starting that again, quieter.\"",
         "\"Mama/Papa ulangi lagi, lebih pelan.\""),
    ),
    68: d(
        ("Calm voice practice",
         "Melatih suara yang tenang"),
        ("Children process tone before content. Lowering your pitch and slowing your pace "
         "carries more authority than volume does, and it is a skill you can rehearse "
         "when nothing is wrong.\n\n"
         "Quiet is not weak. A low, slow, unhurried sentence is genuinely harder for a "
         "child to argue with than a shouted one.",
         "Anak memproses nada sebelum isi. Menurunkan nada dan memperlambat tempo membawa "
         "lebih banyak wibawa daripada volume, dan ini keterampilan yang bisa Anda latih "
         "saat tidak ada masalah.\n\n"
         "Pelan bukan berarti lemah. Kalimat yang rendah, lambat, dan tak terburu-buru "
         "sungguh lebih sulit dibantah anak daripada yang diteriakkan."),
        ("Try saying the same instruction twice — once fast and high, once slow and low. "
         "The second one is the one that gets obeyed.",
         "Coba ucapkan instruksi yang sama dua kali — sekali cepat dan tinggi, sekali lambat "
         "dan rendah. Yang kedua itulah yang dituruti."),
        ("Deliver one instruction today deliberately slower and lower than usual.",
         "Sampaikan satu instruksi hari ini dengan sengaja lebih lambat dan lebih rendah dari biasanya."),
        ("What happens in my house when I get quieter instead of louder?",
         "Apa yang terjadi di rumah saya ketika saya justru memelankan suara, bukan mengeraskannya?"),
        ("\"I'm going to say this once, quietly.\"",
         "\"Mama/Papa akan mengatakannya sekali, dengan pelan.\""),
    ),
    69: d(
        ("Body language awareness",
         "Menyadari bahasa tubuh"),
        ("Your face and posture arrive before your words and are believed over them. A "
         "child reads a tight jaw, folded arms and a looming stance as threat, whatever "
         "the sentence says.\n\n"
         "Getting down to eye level does more to lower conflict than most verbal "
         "techniques, because it removes the physical signal of confrontation.",
         "Wajah dan postur Anda tiba lebih dulu daripada kata-kata Anda, dan lebih dipercaya. "
         "Anak membaca rahang yang mengencang, tangan bersedekap, dan tubuh yang menjulang "
         "sebagai ancaman, apa pun bunyi kalimatnya.\n\n"
         "Menurunkan diri sejajar mata lebih menurunkan konflik daripada kebanyakan teknik "
         "verbal, karena ia menghapus sinyal fisik konfrontasi."),
        ("The same words said standing over a child and said kneeling beside them are two "
         "different messages.",
         "Kata-kata yang sama, diucapkan sambil berdiri menjulang dan sambil berjongkok di "
         "sampingnya, adalah dua pesan yang berbeda."),
        ("Get to your child's eye level for every difficult conversation today.",
         "Turunkan diri sejajar mata anak untuk setiap percakapan sulit hari ini."),
        ("What does my body say before I open my mouth?",
         "Apa yang tubuh saya katakan sebelum saya membuka mulut?"),
        ("\"Let me come down to you.\"",
         "\"Mama/Papa turun dulu ke bawah, ya.\""),
    ),
    70: d(
        ("Parental stress signs",
         "Tanda-tanda stres pada orang tua"),
        ("Stress announces itself in the body before it reaches your awareness: shortened "
         "patience, a tight chest, disrupted sleep, irritation at things that were fine "
         "last week.\n\n"
         "Learning your own early signs is genuinely protective, because the moment to "
         "act is well before the moment you snap.",
         "Stres mengumumkan dirinya di tubuh sebelum sampai ke kesadaran Anda: kesabaran "
         "yang memendek, dada yang sesak, tidur yang terganggu, mudah jengkel pada hal yang "
         "minggu lalu biasa saja.\n\n"
         "Mengenali tanda-tanda awal Anda sendiri sungguh melindungi, karena saat yang tepat "
         "untuk bertindak adalah jauh sebelum saat Anda meledak."),
        ("If your fuse has been shorter for three days, that is data about your load, not "
         "about your child's behaviour.",
         "Jika sumbu Anda memendek selama tiga hari, itu data tentang beban Anda, bukan "
         "tentang perilaku anak."),
        ("Name your own earliest stress sign today, before it reaches the family.",
         "Sebutkan tanda stres paling awal Anda hari ini, sebelum sampai ke keluarga."),
        ("What is my body telling me that I have been ignoring?",
         "Apa yang tubuh saya sampaikan yang selama ini saya abaikan?"),
        ("\"I'm running low. I need to do something about that.\"",
         "\"Tenaga saya menipis. Saya perlu melakukan sesuatu untuk itu.\""),
    ),
    71: d(
        ("Burnout in parenting",
         "Kelelahan mendalam dalam mengasuh"),
        ("Parental burnout is real and distinct from ordinary tiredness. It shows up as "
         "emotional distance from your children, a sense of being a failure as a parent, "
         "and exhaustion that sleep does not fix.\n\n"
         "It is not a character problem and it does not respond to trying harder. It "
         "responds to reduced load and increased support — and it is worth asking for help.",
         "Kelelahan mendalam pada orang tua itu nyata dan berbeda dari lelah biasa. Ia "
         "muncul sebagai jarak emosional dari anak, perasaan gagal sebagai orang tua, dan "
         "keletihan yang tak sembuh dengan tidur.\n\n"
         "Ini bukan masalah karakter dan tidak sembuh dengan berusaha lebih keras. Ia "
         "membaik dengan beban yang dikurangi dan dukungan yang ditambah — dan layak untuk "
         "meminta bantuan."),
        ("Feeling numb toward your children is one of the clearest signals, and one of the "
         "most frightening to admit. It is a sign of depletion, not of not loving them.",
         "Merasa mati rasa terhadap anak adalah salah satu sinyal paling jelas, dan paling "
         "menakutkan untuk diakui. Itu tanda kehabisan tenaga, bukan tanda tidak menyayangi mereka."),
        ("Remove one non-essential commitment from this week. Actually remove it.",
         "Hapus satu komitmen yang tidak esensial dari minggu ini. Betul-betul hapus."),
        ("Am I tired, or am I depleted in a way that rest alone is not fixing?",
         "Apakah saya lelah, atau kehabisan tenaga dengan cara yang tak sembuh hanya dengan istirahat?"),
        ("\"I need help with this, and that's allowed.\"",
         "\"Saya butuh bantuan untuk ini, dan itu boleh.\""),
    ),
    72: d(
        ("Repair after losing your temper",
         "Memperbaiki setelah hilang kesabaran"),
        ("You will lose your temper. The research on secure attachment does not describe "
         "parents who never rupture — it describes parents who repair.\n\n"
         "Repair is not weakness and it does not undo the limit you were holding. It "
         "separates the rule, which stands, from the delivery, which was not okay.",
         "Anda akan hilang kesabaran. Penelitian tentang kelekatan aman tidak menggambarkan "
         "orang tua yang tak pernah retak — ia menggambarkan orang tua yang memperbaiki.\n\n"
         "Memperbaiki bukan kelemahan dan tidak membatalkan batas yang Anda pegang. Ia "
         "memisahkan aturannya, yang tetap berlaku, dari cara penyampaiannya, yang tidak baik."),
        ("\"The rule about hitting still stands. The way I shouted at you was not okay, "
         "and I'm sorry.\" Both halves matter.",
         "\"Aturan soal memukul tetap berlaku. Cara Mama membentakmu tadi tidak baik, dan "
         "Mama minta maaf.\" Kedua bagiannya sama penting."),
        ("If you lose your temper today, repair before bedtime — and keep the limit.",
         "Jika Anda hilang kesabaran hari ini, perbaiki sebelum waktu tidur — dan pertahankan batasnya."),
        ("Do I repair, or do I just wait for the atmosphere to pass?",
         "Apakah saya memperbaiki, atau hanya menunggu suasananya berlalu?"),
        ("\"The rule stands. How I said it doesn't.\"",
         "\"Aturannya tetap. Cara Mama/Papa menyampaikannya tidak.\""),
    ),
    73: d(
        ("Apologizing to your child",
         "Meminta maaf kepada anak"),
        ("A clean apology has three parts and no fourth: name what you did, acknowledge "
         "the effect, and stop. The moment \"but you were\" appears, it stops being an "
         "apology and becomes a continued argument.\n\n"
         "Children who receive real apologies learn how to give them. This is one of the "
         "few things you can teach entirely by demonstration.",
         "Permintaan maaf yang bersih punya tiga bagian dan tidak ada yang keempat: sebut "
         "apa yang Anda lakukan, akui dampaknya, lalu berhenti. Begitu \"tapi kamu tadi\" "
         "muncul, ia berhenti menjadi permintaan maaf dan berubah jadi lanjutan perdebatan.\n\n"
         "Anak yang menerima permintaan maaf yang sungguh belajar cara memberikannya. Ini "
         "salah satu dari sedikit hal yang bisa Anda ajarkan sepenuhnya lewat peragaan."),
        ("\"I shouted. That must have felt horrible. I'm sorry.\" Then silence. The silence "
         "is part of the apology.",
         "\"Mama membentak tadi. Pasti rasanya tidak enak. Mama minta maaf.\" Lalu diam. "
         "Diamnya adalah bagian dari permintaan maaf itu."),
        ("Give one apology today with no justification attached to the end of it.",
         "Berikan satu permintaan maaf hari ini tanpa pembenaran apa pun di ujungnya."),
        ("Can I apologise without defending myself in the same breath?",
         "Bisakah saya minta maaf tanpa membela diri di napas yang sama?"),
        ("\"I'm sorry. That's all — no buts.\"",
         "\"Mama/Papa minta maaf. Itu saja — tanpa tapi.\""),
    ),
    74: d(
        ("Boundaries for parents",
         "Batasan untuk orang tua"),
        ("Boundaries are not only something you set for children. A parent with no "
         "boundaries becomes depleted, and a depleted parent has nothing left to regulate "
         "with.\n\n"
         "Saying no to something outside the family — an extra commitment, a request, an "
         "expectation — is often what makes yes possible inside it.",
         "Batasan bukan hanya sesuatu yang Anda tetapkan untuk anak. Orang tua tanpa batas "
         "akan kehabisan tenaga, dan orang tua yang kehabisan tenaga tak punya apa-apa lagi "
         "untuk menenangkan.\n\n"
         "Berkata tidak pada sesuatu di luar keluarga — komitmen tambahan, permintaan, "
         "harapan orang — sering justru yang memungkinkan Anda berkata ya di dalam keluarga."),
        ("The parent who says yes to everything outside the home usually has the shortest "
         "fuse inside it.",
         "Orang tua yang mengiyakan segalanya di luar rumah biasanya punya sumbu terpendek "
         "di dalam rumah."),
        ("Say no to one thing this week that would have cost you your evening patience.",
         "Katakan tidak pada satu hal minggu ini yang akan menghabiskan kesabaran malam Anda."),
        ("What am I saying yes to that my family pays for?",
         "Apa yang saya iyakan, yang harganya dibayar oleh keluarga saya?"),
        ("\"I can't take that on right now.\"",
         "\"Saya tidak bisa mengambil itu sekarang.\""),
    ),
    75: d(
        ("Self-care without guilt",
         "Merawat diri tanpa rasa bersalah"),
        ("Self-care in parenting is not indulgence; it is maintenance of the instrument "
         "your child depends on. A rested parent has patience available. An empty one does "
         "not, however much they love their child.\n\n"
         "Guilt about it is nearly universal and almost always misplaced. Your child does "
         "not need a martyr — they need someone with enough left to be kind at 6pm.",
         "Merawat diri dalam pengasuhan bukan memanjakan diri; ia perawatan atas alat yang "
         "diandalkan anak Anda. Orang tua yang cukup istirahat punya kesabaran yang "
         "tersedia. Yang kosong tidak punya, sebesar apa pun sayangnya pada anak.\n\n"
         "Rasa bersalah soal ini hampir universal dan hampir selalu salah alamat. Anak Anda "
         "tidak butuh martir — dia butuh seseorang yang masih punya cukup tenaga untuk "
         "bersikap baik pukul enam sore."),
        ("Twenty minutes that restores you is not stolen from your child. It is usually "
         "returned to them with interest that same evening.",
         "Dua puluh menit yang memulihkan Anda bukan dicuri dari anak. Biasanya ia "
         "dikembalikan kepadanya dengan bunga di malam yang sama."),
        ("Take twenty minutes today for something that restores you, without apologising "
         "for it.",
         "Ambil dua puluh menit hari ini untuk sesuatu yang memulihkan Anda, tanpa meminta maaf."),
        ("What restores me, and when did I last do it?",
         "Apa yang memulihkan saya, dan kapan terakhir kali saya melakukannya?"),
        ("\"I'm taking twenty minutes. I'll be better company after.\"",
         "\"Saya ambil dua puluh menit dulu. Setelah itu saya akan lebih enak diajak bersama.\""),
    ),
    76: d(
        ("Protecting sleep as a parent",
         "Menjaga tidur sebagai orang tua"),
        ("Your own sleep is the most direct lever on your patience, and the easiest one to "
         "sacrifice quietly. The hour reclaimed after bedtime is precious, and it is often "
         "paid for the next evening with a shorter fuse.\n\n"
         "You cannot always get more sleep. But most parents can get some, and the "
         "difference is usually visible within a few days.",
         "Tidur Anda sendiri adalah tuas paling langsung atas kesabaran Anda, dan yang "
         "paling mudah dikorbankan diam-diam. Satu jam yang direbut setelah anak tidur itu "
         "berharga, dan sering dibayar keesokan sorenya dengan sumbu yang lebih pendek.\n\n"
         "Anda tidak selalu bisa mendapat tidur lebih banyak. Tapi kebanyakan orang tua bisa "
         "mendapat sebagian, dan bedanya biasanya terlihat dalam beberapa hari."),
        ("The scrolling hour after the children sleep feels like recovery and usually is "
         "not. Actual sleep outperforms it every time.",
         "Satu jam menggulir layar setelah anak tidur terasa seperti pemulihan, dan biasanya "
         "bukan. Tidur yang sungguhan selalu lebih unggul."),
        ("Go to bed thirty minutes earlier tonight and notice tomorrow evening.",
         "Tidurlah tiga puluh menit lebih awal malam ini dan perhatikan besok sore."),
        ("How much of my impatience is simply my own sleep debt?",
         "Seberapa banyak ketidaksabaran saya sebenarnya hanyalah utang tidur saya sendiri?"),
        ("\"I'm going to sleep. Tomorrow needs me more than tonight does.\"",
         "\"Saya mau tidur. Besok lebih membutuhkan saya daripada malam ini.\""),
    ),
    77: d(
        ("Couples and co-parenting stress",
         "Stres pasangan dan pengasuhan bersama"),
        ("Tension between parents leaks into parenting, whether or not anyone raises their "
         "voice. Children are extremely good at detecting atmosphere and usually assume "
         "they are somehow the cause.\n\n"
         "Protecting the couple relationship is not separate from parenting. For most "
         "families it is one of the highest-yield things you can do for the children.",
         "Ketegangan antara orang tua merembes ke dalam pengasuhan, ada atau tidak ada yang "
         "meninggikan suara. Anak sangat pandai mendeteksi suasana dan biasanya mengira "
         "merekalah penyebabnya.\n\n"
         "Melindungi hubungan pasangan bukan hal yang terpisah dari pengasuhan. Bagi "
         "kebanyakan keluarga, itu salah satu hal berhasil-guna tertinggi yang bisa Anda "
         "lakukan untuk anak."),
        ("Children rarely need to be told there is tension. They have usually known for "
         "days and have been quietly adjusting their behaviour around it.",
         "Anak jarang perlu diberi tahu bahwa ada ketegangan. Biasanya mereka sudah tahu "
         "berhari-hari dan diam-diam menyesuaikan perilakunya."),
        ("Spend ten uninterrupted minutes with your partner today that is not about logistics.",
         "Luangkan sepuluh menit tanpa gangguan bersama pasangan hari ini yang bukan soal urusan teknis."),
        ("What is my child absorbing from the atmosphere between us?",
         "Apa yang anak serap dari suasana di antara kami?"),
        ("\"Can we have ten minutes that isn't about the schedule?\"",
         "\"Bisa kita punya sepuluh menit yang bukan soal jadwal?\""),
    ),
    78: d(
        ("Aligning parenting values with spouse",
         "Menyelaraskan nilai pengasuhan dengan pasangan"),
        ("Two parents will never agree on everything, and they do not need to. What "
         "matters is agreeing on the few things that recur — bedtime, screens, how "
         "discipline is delivered — so a child is not managing two different systems.\n\n"
         "Alignment is built in calm moments, in advance. It cannot be negotiated in the "
         "middle of an incident.",
         "Dua orang tua tidak akan pernah sepakat dalam segalanya, dan memang tidak perlu. "
         "Yang penting adalah menyepakati beberapa hal yang berulang — jam tidur, layar, "
         "cara disiplin disampaikan — agar anak tidak mengelola dua sistem berbeda.\n\n"
         "Keselarasan dibangun di momen yang tenang, jauh sebelumnya. Ia tak bisa "
         "dinegosiasikan di tengah kejadian."),
        ("Pick the three rules that come up most often and agree those. The rest can "
         "safely differ.",
         "Pilih tiga aturan yang paling sering muncul dan sepakati itu. Sisanya aman untuk berbeda."),
        ("Agree one recurring rule with your partner today, outside of any incident.",
         "Sepakati satu aturan yang berulang bersama pasangan hari ini, di luar kejadian apa pun."),
        ("Which rule do we most often contradict each other on?",
         "Aturan mana yang paling sering membuat kami saling bertentangan?"),
        ("\"Can we decide this one now, while it's calm?\"",
         "\"Bisa kita putuskan yang ini sekarang, selagi tenang?\""),
    ),
    79: d(
        ("Handling disagreement in front of children",
         "Menangani perbedaan pendapat di depan anak"),
        ("Children do not need parents who never disagree. They need to see disagreement "
         "handled without contempt — that is a lesson they will use in every relationship "
         "they ever have.\n\n"
         "What harms is not the disagreement but undermining: contradicting the other "
         "parent's decision in front of the child, which teaches that rules are "
         "negotiable if you find the right adult.",
         "Anak tidak butuh orang tua yang tak pernah berbeda pendapat. Mereka perlu melihat "
         "perbedaan pendapat ditangani tanpa penghinaan — pelajaran yang akan mereka pakai "
         "dalam setiap hubungan sepanjang hidup.\n\n"
         "Yang merusak bukan perbedaannya, melainkan tindakan menjatuhkan: membantah "
         "keputusan orang tua lain di depan anak, yang mengajarkan bahwa aturan bisa "
         "ditawar asal menemukan orang dewasa yang tepat."),
        ("\"We'll talk about it and come back to you\" holds the united front without "
         "requiring either parent to pretend to agree.",
         "\"Kami bicarakan dulu lalu kembali ke kamu\" menjaga barisan tetap satu tanpa "
         "menuntut salah satu orang tua berpura-pura setuju."),
        ("If you disagree in front of your child today, defer it rather than fight it there.",
         "Jika Anda berbeda pendapat di depan anak hari ini, tunda dulu, jangan diperdebatkan di situ."),
        ("Do we undermine each other in front of the children without meaning to?",
         "Apakah kami saling menjatuhkan di depan anak tanpa bermaksud begitu?"),
        ("\"We'll discuss it and let you know.\"",
         "\"Kami bicarakan dulu, nanti kami kabari.\""),
    ),
    80: d(
        ("When guilt is useful and when it is not",
         "Kapan rasa bersalah berguna dan kapan tidak"),
        ("Useful guilt is specific and points at an action: I snapped, I will repair. It "
         "is brief and it produces a change.\n\n"
         "Useless guilt is global and points at your identity: I am a bad parent. It "
         "produces rumination, not repair, and it usually makes the next hour worse rather "
         "than better.",
         "Rasa bersalah yang berguna itu spesifik dan menunjuk pada tindakan: saya "
         "membentak, saya akan memperbaikinya. Ia singkat dan menghasilkan perubahan.\n\n"
         "Rasa bersalah yang tidak berguna itu menyeluruh dan menunjuk pada jati diri Anda: "
         "saya orang tua yang buruk. Ia menghasilkan perenungan berputar, bukan perbaikan, "
         "dan biasanya membuat satu jam berikutnya lebih buruk, bukan lebih baik."),
        ("\"That was a bad moment\" leads somewhere. \"I am a bad mother\" leads nowhere and "
         "costs you the energy repair requires.",
         "\"Tadi momen yang buruk\" membawa ke suatu tempat. \"Saya ibu yang buruk\" tidak "
         "membawa ke mana-mana dan menghabiskan tenaga yang dibutuhkan untuk memperbaiki."),
        ("Convert one global guilt into one specific action today.",
         "Ubah satu rasa bersalah yang menyeluruh menjadi satu tindakan spesifik hari ini."),
        ("Is my guilt telling me to do something, or just telling me I am bad?",
         "Apakah rasa bersalah saya menyuruh melakukan sesuatu, atau hanya berkata bahwa saya buruk?"),
        ("\"That was a bad moment, not a bad parent.\"",
         "\"Itu momen yang buruk, bukan orang tua yang buruk.\""),
    ),
    81: d(
        ("Perfectionism in parenting",
         "Perfeksionisme dalam mengasuh"),
        ("Perfectionism looks like high standards and behaves like a tax. It makes "
         "ordinary mistakes feel catastrophic, makes repair harder because admitting fault "
         "costs more, and it is exhausting to live beside.\n\n"
         "Children raised by a perfectionist parent often become perfectionists "
         "themselves, which is rarely the inheritance anyone intended.",
         "Perfeksionisme tampak seperti standar tinggi dan berperilaku seperti pajak. Ia "
         "membuat kesalahan biasa terasa bencana, membuat perbaikan lebih sulit karena "
         "mengakui kesalahan jadi terasa mahal, dan melelahkan untuk didampingi.\n\n"
         "Anak yang dibesarkan orang tua perfeksionis sering menjadi perfeksionis juga — "
         "warisan yang jarang diniatkan siapa pun."),
        ("A parent who can say \"that went badly and it's fine\" gives a child permission "
         "to be a learner rather than a performer.",
         "Orang tua yang bisa berkata \"tadi kurang baik dan tidak apa-apa\" memberi anak izin "
         "menjadi pembelajar, bukan penampil."),
        ("Let one thing be visibly good enough today, in front of your child.",
         "Biarkan satu hal terlihat cukup baik saja hari ini, di depan anak Anda."),
        ("What standard am I holding that is costing more than it returns?",
         "Standar apa yang saya pegang yang biayanya lebih besar daripada hasilnya?"),
        ("\"That's good enough, and that's fine.\"",
         "\"Itu sudah cukup baik, dan tidak apa-apa.\""),
    ),
    82: d(
        ("Comparison with other families",
         "Membandingkan dengan keluarga lain"),
        ("You compare your whole reality — the tantrums, the mess, the hard evenings — "
         "with other families' visible surface. It is not a fair comparison and it never "
         "produces anything useful.\n\n"
         "Every calm family you envy has hours you have never seen. Comparison mostly "
         "damages your confidence, and low confidence makes worse parents than low skill "
         "does.",
         "Anda membandingkan seluruh kenyataan Anda — tantrum, kekacauan, sore-sore yang "
         "berat — dengan permukaan yang terlihat dari keluarga lain. Itu perbandingan yang "
         "tidak adil dan tak pernah menghasilkan apa pun yang berguna.\n\n"
         "Setiap keluarga tenang yang Anda cemburui punya jam-jam yang tak pernah Anda "
         "lihat. Membandingkan terutama merusak kepercayaan diri Anda, dan kepercayaan diri "
         "yang rendah menghasilkan orang tua yang lebih buruk daripada keterampilan yang rendah."),
        ("The family that looks effortless at the school gate had their own difficult "
         "morning twenty minutes earlier.",
         "Keluarga yang tampak santai di gerbang sekolah punya pagi sulitnya sendiri dua "
         "puluh menit sebelumnya."),
        ("Notice one comparison today and put it down deliberately.",
         "Sadari satu perbandingan hari ini dan letakkan dengan sengaja."),
        ("Who am I comparing myself to, and what am I not seeing about them?",
         "Dengan siapa saya membandingkan diri, dan apa yang tak saya lihat dari mereka?"),
        ("\"I only see their outside and all of my inside.\"",
         "\"Saya hanya melihat luar mereka dan seluruh dalam diri saya.\""),
    ),
    83: d(
        ("Social media pressure",
         "Tekanan media sosial"),
        ("Social media presents parenting as a performance with an audience, which is "
         "precisely the wrong frame. It amplifies comparison, sells certainty about "
         "questions that have none, and makes ordinary difficulty feel like failure.\n\n"
         "Curating what you consume is a genuine parenting intervention. Accounts that "
         "leave you feeling inadequate are not helping your children.",
         "Media sosial menyajikan pengasuhan sebagai pertunjukan dengan penonton, dan itu "
         "persis kerangka yang keliru. Ia memperbesar perbandingan, menjual kepastian atas "
         "pertanyaan yang tak punya kepastian, dan membuat kesulitan biasa terasa seperti kegagalan.\n\n"
         "Menyaring apa yang Anda konsumsi adalah intervensi pengasuhan yang sungguhan. Akun "
         "yang membuat Anda merasa tidak cukup tidak sedang membantu anak Anda."),
        ("Unfollowing three accounts that make you feel like a failure is a more effective "
         "parenting change than most techniques.",
         "Berhenti mengikuti tiga akun yang membuat Anda merasa gagal adalah perubahan "
         "pengasuhan yang lebih efektif daripada kebanyakan teknik."),
        ("Unfollow or mute one account today that consistently makes you feel worse.",
         "Berhenti ikuti atau bisukan satu akun hari ini yang selalu membuat Anda merasa lebih buruk."),
        ("Which accounts leave me a worse parent for the next hour?",
         "Akun mana yang membuat saya menjadi orang tua yang lebih buruk selama satu jam berikutnya?"),
        ("\"This isn't helping me. I'm putting it down.\"",
         "\"Ini tidak membantu saya. Saya letakkan dulu.\""),
    ),
    84: d(
        ("Using reflection journals",
         "Menggunakan jurnal refleksi"),
        ("Writing changes what reading cannot, because it forces specificity. \"I was "
         "impatient this week\" becomes \"I was impatient at 6pm on three days, all before "
         "dinner\" — and the second one tells you what to do.\n\n"
         "This is the whole reason the diary in this app exists. A few honest lines beat "
         "any amount of resolve.",
         "Menulis mengubah apa yang tak bisa diubah membaca, karena ia memaksa kejelasan. "
         "\"Minggu ini saya tidak sabar\" menjadi \"saya tidak sabar pukul enam sore di tiga "
         "hari, semuanya sebelum makan malam\" — dan yang kedua memberi tahu apa yang harus dilakukan.\n\n"
         "Inilah seluruh alasan diari dalam aplikasi ini ada. Beberapa baris yang jujur "
         "mengalahkan tekad sebanyak apa pun."),
        ("Patterns are invisible from inside a single day. They only appear when a week is "
         "written down and read back.",
         "Pola tak terlihat dari dalam satu hari. Ia baru muncul ketika satu minggu ditulis "
         "dan dibaca ulang."),
        ("Write three honest lines about today in the diary, even if they are unflattering.",
         "Tulis tiga baris jujur tentang hari ini di diari, meski tidak enak dibaca."),
        ("What pattern would I see if I actually wrote this week down?",
         "Pola apa yang akan saya lihat jika saya benar-benar menuliskan minggu ini?"),
        ("\"Three lines. That's all it takes.\"",
         "\"Tiga baris. Itu saja cukup.\""),
    ),
    85: d(
        ("One-minute reset techniques",
         "Teknik pemulihan satu menit"),
        ("You rarely get twenty minutes in the middle of a hard afternoon, but you can "
         "almost always find sixty seconds. Cold water on the wrists, a slow exhale, "
         "stepping outside, unclenching your jaw, putting your feet flat on the floor — "
         "each genuinely shifts your physiology.\n\n"
         "Have one chosen in advance. Deciding what to do while flooded almost never works.",
         "Anda jarang mendapat dua puluh menit di tengah sore yang berat, tapi Anda hampir "
         "selalu bisa menemukan enam puluh detik. Air dingin di pergelangan tangan, embusan "
         "napas pelan, keluar sebentar, mengendurkan rahang, menapakkan kaki rata di lantai "
         "— masing-masing sungguh menggeser fisiologi Anda.\n\n"
         "Pilih satu sejak awal. Memutuskan mau melakukan apa saat sedang kewalahan hampir "
         "tidak pernah berhasil."),
        ("The parent who has already decided \"I go to the sink and run cold water\" uses it. "
         "The parent deciding in the moment does not.",
         "Orang tua yang sudah memutuskan \"saya ke wastafel dan menyalakan air dingin\" "
         "memakainya. Yang memutuskan saat itu juga tidak."),
        ("Choose your one-minute reset now, before you need it.",
         "Pilih pemulihan satu menit Anda sekarang, sebelum Anda membutuhkannya."),
        ("What is my reset, and have I actually decided it in advance?",
         "Apa pemulihan saya, dan sudahkah saya benar-benar memutuskannya lebih dulu?"),
        ("\"One minute. Then I'll come back to this.\"",
         "\"Satu menit. Lalu Mama/Papa kembali ke sini.\""),
    ),
    86: d(
        ("Parenting scripts to replace anger",
         "Kalimat siap pakai pengganti kemarahan"),
        ("In a flooded moment you do not compose sentences — you reach for whatever is "
         "already loaded. If nothing is loaded, what comes out is usually whatever you "
         "heard as a child.\n\n"
         "Writing two or three sentences in advance, and rehearsing them when calm, means "
         "there is something better within reach when it matters.",
         "Di momen yang kewalahan Anda tidak menyusun kalimat — Anda meraih apa pun yang "
         "sudah termuat. Jika tidak ada yang termuat, yang keluar biasanya apa pun yang "
         "dulu Anda dengar sewaktu kecil.\n\n"
         "Menulis dua atau tiga kalimat sejak awal, dan melatihnya saat tenang, berarti ada "
         "sesuatu yang lebih baik dalam jangkauan saat dibutuhkan."),
        ("\"I'm too angry to talk about this well right now\" is a sentence worth having "
         "loaded. It is honest, it is calm, and it buys time.",
         "\"Mama terlalu marah untuk membicarakan ini dengan baik sekarang\" adalah kalimat "
         "yang layak dimuat lebih dulu. Ia jujur, tenang, dan membeli waktu."),
        ("Write two sentences you want available next time, and say them aloud once.",
         "Tuliskan dua kalimat yang Anda ingin tersedia lain kali, dan ucapkan sekali dengan suara."),
        ("What comes out of my mouth automatically, and where did I learn it?",
         "Apa yang keluar otomatis dari mulut saya, dan di mana saya mempelajarinya?"),
        ("\"I'm too angry to do this well right now.\"",
         "\"Mama/Papa terlalu marah untuk menangani ini dengan baik sekarang.\""),
    ),
    87: d(
        ("Staying calm during defiance",
         "Tetap tenang saat anak membangkang"),
        ("Defiance is designed to pull you in, and the pull is strongest when you feel "
         "your authority is being tested in front of others.\n\n"
         "The move that works is boring and repeatable: state the limit once, stop "
         "explaining, and let the silence do the work. Every extra sentence hands the "
         "child more to argue with.",
         "Pembangkangan dirancang untuk menarik Anda masuk, dan tarikannya paling kuat saat "
         "Anda merasa wibawa Anda sedang diuji di depan orang lain.\n\n"
         "Langkah yang berhasil itu membosankan dan bisa diulang: sebutkan batasnya sekali, "
         "berhenti menjelaskan, dan biarkan keheningan bekerja. Setiap kalimat tambahan "
         "memberi anak lebih banyak bahan untuk dibantah."),
        ("Repeating the same short sentence calmly — without new arguments — ends "
         "resistance faster than any escalation.",
         "Mengulang kalimat pendek yang sama dengan tenang — tanpa argumen baru — mengakhiri "
         "perlawanan lebih cepat daripada eskalasi apa pun."),
        ("Say your limit once today, then stop talking and stay put.",
         "Ucapkan batas Anda sekali hari ini, lalu berhenti bicara dan tetap di tempat."),
        ("Do I keep explaining because it helps, or because I feel challenged?",
         "Apakah saya terus menjelaskan karena itu membantu, atau karena saya merasa ditantang?"),
        ("\"I've said what I'm going to say.\"",
         "\"Mama/Papa sudah mengatakan yang perlu dikatakan.\""),
    ),
    88: d(
        ("Staying calm during whining",
         "Tetap tenang saat anak merengek"),
        ("Whining is physically grating by design — it is engineered to be hard to ignore. "
         "It usually signals depletion: tiredness, hunger, or a need for connection that "
         "has not been met in a better way.\n\n"
         "Answering the need rather than the noise resolves it faster than correcting the "
         "tone, though the tone is worth teaching once everyone is calm.",
         "Rengekan memang secara fisik menjengkelkan — ia dirancang agar sulit diabaikan. "
         "Biasanya ia menandakan kehabisan tenaga: lelah, lapar, atau kebutuhan akan "
         "kedekatan yang belum terpenuhi dengan cara yang lebih baik.\n\n"
         "Menjawab kebutuhannya, bukan bunyinya, menyelesaikannya lebih cepat daripada "
         "membetulkan nadanya — meski nada itu layak diajarkan setelah semua orang tenang."),
        ("\"You sound like you're running out of energy. Come here\" often ends whining "
         "faster than \"use your normal voice.\"",
         "\"Sepertinya tenagamu habis. Sini\" sering menghentikan rengekan lebih cepat "
         "daripada \"pakai suara biasa.\""),
        ("Answer the need under one whine today instead of correcting the sound.",
         "Jawab kebutuhan di balik satu rengekan hari ini, bukan membetulkan bunyinya."),
        ("What is usually true about my child when the whining starts?",
         "Apa yang biasanya sedang terjadi pada anak saya saat rengekan mulai?"),
        ("\"You sound worn out. Let's sit down a minute.\"",
         "\"Sepertinya kamu capek. Ayo duduk sebentar.\""),
    ),
    89: d(
        ("Staying calm during sibling fights",
         "Tetap tenang saat anak-anak bertengkar"),
        ("Sibling fights pull parents into the role of judge, and the judge role is a trap "
         "— it teaches children to compete for your verdict instead of learning to "
         "negotiate.\n\n"
         "Unless someone is unsafe, the more useful position is coach: describe what you "
         "see, name both needs, and hand the problem back.",
         "Pertengkaran saudara menarik orang tua ke peran hakim, dan peran hakim itu jebakan "
         "— ia mengajarkan anak bersaing memperebutkan putusan Anda alih-alih belajar bernegosiasi.\n\n"
         "Kecuali ada yang tidak aman, posisi yang lebih berguna adalah pelatih: gambarkan "
         "apa yang Anda lihat, sebutkan kebutuhan keduanya, dan kembalikan masalahnya."),
        ("\"You both want the same toy. That's a hard problem. What could work?\" builds "
         "skill that a verdict never does.",
         "\"Kalian berdua ingin mainan yang sama. Itu masalah yang sulit. Apa yang bisa "
         "dilakukan?\" membangun keterampilan yang tak pernah dibangun oleh sebuah putusan."),
        ("Coach one sibling conflict today instead of judging it.",
         "Latih satu konflik saudara hari ini alih-alih mengadilinya."),
        ("Am I the judge in my house, or the coach?",
         "Apakah saya hakim di rumah saya, atau pelatih?"),
        ("\"That's a hard problem. What could you two try?\"",
         "\"Itu masalah yang sulit. Kalian berdua mau coba apa?\""),
    ),
    90: d(
        ("Staying calm in public",
         "Tetap tenang di tempat umum"),
        ("Public difficulty is harder because of the audience, not the child. The "
         "imagined judgement of strangers pushes parents into harsher responses than they "
         "would ever choose at home.\n\n"
         "Deciding in advance that you will parent the same way in public as in private "
         "removes most of the pressure. The strangers will forget within minutes; your "
         "child will not.",
         "Kesulitan di tempat umum terasa lebih berat karena penontonnya, bukan karena "
         "anaknya. Bayangan penilaian orang asing mendorong orang tua ke respons yang jauh "
         "lebih keras daripada yang akan mereka pilih di rumah.\n\n"
         "Memutuskan sejak awal bahwa Anda akan mengasuh dengan cara yang sama di tempat "
         "umum maupun di rumah menghapus sebagian besar tekanannya. Orang asing akan lupa "
         "dalam hitungan menit; anak Anda tidak."),
        ("Most of the strangers watching are either sympathetic or not watching at all. "
         "Almost none of them will remember it by evening.",
         "Sebagian besar orang asing yang melihat entah bersimpati atau sebenarnya tidak "
         "memperhatikan. Hampir tak satu pun mengingatnya sampai malam."),
        ("If a hard moment happens in public today, respond exactly as you would at home.",
         "Jika momen sulit terjadi di tempat umum hari ini, tanggapi persis seperti di rumah."),
        ("Am I parenting my child right now, or the strangers watching?",
         "Apakah saya sedang mengasuh anak saya sekarang, atau mengasuh orang asing yang menonton?"),
        ("\"I'm going to handle this the way I would at home.\"",
         "\"Saya akan menangani ini seperti di rumah.\""),
    ),
    91: d(
        ("Weekly reflection",
         "Refleksi mingguan"),
        ("This chapter has one claim: your regulation comes first, because your child "
         "borrows it. Everything else — the scripts, the pauses, the breathing — is "
         "machinery in service of that.\n\n"
         "Look back across the month and find the pattern rather than the incidents. Most "
         "parents discover their hardest moments cluster at a particular hour, in a "
         "particular state, around a particular trigger. That cluster is where the leverage is.",
         "Bab ini punya satu klaim: pengendalian diri Anda datang lebih dulu, karena anak "
         "meminjamnya. Selebihnya — kalimat siap pakai, jeda, pernapasan — adalah mesin yang "
         "melayani hal itu.\n\n"
         "Tengok kembali sebulan ini dan carilah polanya, bukan kejadiannya. Kebanyakan "
         "orang tua menemukan momen tersulit mereka menumpuk di jam tertentu, dalam kondisi "
         "tertentu, di sekitar pemicu tertentu. Tumpukan itulah letak daya ungkitnya."),
        ("Three bad evenings in a month is not a character verdict. It is a pattern with a "
         "cause, and causes can be changed.",
         "Tiga sore yang buruk dalam sebulan bukan vonis atas karakter. Itu pola dengan "
         "sebab, dan sebab bisa diubah."),
        ("Find the hour and the trigger your hardest moments cluster around this month.",
         "Temukan jam dan pemicu tempat momen tersulit Anda menumpuk bulan ini."),
        ("When I am at my worst, what is almost always true about my state?",
         "Saat saya sedang paling buruk, apa yang hampir selalu benar tentang kondisi saya?"),
        ("\"I can't pour calm I don't have. Start there.\"",
         "\"Saya tak bisa menuangkan ketenangan yang tak saya punya. Mulai dari situ.\""),
    ),
}
