# Chapter 10 — Relationship & Attachment (days 271-299)
#
# Grounded in the founder's guidebook chapter 10 ("The relationship is the
# curriculum") and toolkit tool 10 (Connection Tracker, Monday to Sunday).
#
# Through-line: connection is not the reward for good behaviour, it is the
# condition that makes everything else in this guide work. Day 275 carries a
# grid of the signals children send when they need connection, because most of
# them are easy to misread as misbehaviour.

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
    271: d(
        ("One-on-one time",
         "Waktu berdua"),
        ("Of everything in this guide, this is the intervention with the best return for "
         "the least effort. Ten minutes a day, one child, no phone, no agenda. Parents who "
         "actually do it for two weeks usually report that behaviour they had been fighting "
         "for months simply eased.\n\n"
         "It works because most difficult behaviour is a bid for connection made badly. A "
         "child who is reliably filled up does not need to fight for your attention, and a "
         "child who is not will find a way to get it — and the way they find will not be "
         "one you enjoy.",
         "Dari semua yang ada di panduan ini, inilah tindakan dengan hasil terbesar untuk "
         "usaha terkecil. Sepuluh menit sehari, satu anak, tanpa ponsel, tanpa agenda. Orang "
         "tua yang benar-benar melakukannya selama dua minggu biasanya melaporkan bahwa "
         "perilaku yang berbulan-bulan mereka lawan tiba-tiba mereda.\n\n"
         "Ini berhasil karena sebagian besar perilaku sulit adalah upaya mencari kedekatan "
         "yang disampaikan dengan cara buruk. Anak yang isinya terisi dengan andal tidak perlu "
         "berjuang merebut perhatian Anda, dan anak yang tidak terisi akan mencari cara "
         "mendapatkannya — dan cara yang ia temukan tidak akan Anda sukai."),
        ("Ten minutes. One child. Phone in another room. If you have three children, that is "
         "three separate ten-minute blocks, not one thirty-minute group activity.",
         "Sepuluh menit. Satu anak. Ponsel di ruangan lain. Kalau anak Anda tiga, itu berarti "
         "tiga blok sepuluh menit terpisah, bukan satu kegiatan bersama tiga puluh menit."),
        ("Give one child ten uninterrupted minutes today, with your phone out of the room.",
         "Berikan satu anak sepuluh menit tanpa gangguan hari ini, dengan ponsel di luar ruangan."),
        ("When did I last give my child my full attention with nothing else running?",
         "Kapan terakhir saya memberi anak perhatian penuh tanpa ada hal lain yang berjalan?"),
        ("\"The next ten minutes are yours. What do you want to do?\"",
         "\"Sepuluh menit ke depan milikmu. Kamu mau melakukan apa?\""),
    ),

    272: d(
        ("Special time method",
         "Cara menjalankan waktu istimewa"),
        ("The method matters as much as the minutes. Special time has three rules: the "
         "child chooses the activity, you do not teach during it, and you do not end it "
         "early as a punishment.\n\n"
         "That third rule is the one parents break. The moment special time becomes "
         "something that can be withdrawn, it stops being a foundation and becomes leverage "
         "— and a child cannot rest on something that might be taken away. Protect it "
         "absolutely, especially on the days when the child has been difficult. Those are "
         "the days it was designed for.",
         "Caranya sama pentingnya dengan menitnya. Waktu istimewa punya tiga aturan: anak yang "
         "memilih kegiatannya, Anda tidak mengajari selama itu, dan Anda tidak mengakhirinya "
         "lebih awal sebagai hukuman.\n\n"
         "Aturan ketiga itulah yang paling sering dilanggar orang tua. Begitu waktu istimewa "
         "menjadi sesuatu yang bisa dicabut, ia berhenti menjadi fondasi dan berubah menjadi "
         "alat tawar — dan anak tidak bisa bersandar pada sesuatu yang mungkin diambil. "
         "Lindungi mati-matian, terutama di hari-hari ketika anak sedang sulit. Justru untuk "
         "hari-hari itulah ini dirancang."),
        ("Never cancel special time as a consequence. It is not a reward for good behaviour; "
         "it is the ground the good behaviour grows out of.",
         "Jangan pernah membatalkan waktu istimewa sebagai hukuman. Ini bukan hadiah untuk "
         "perilaku baik; ini tanah tempat perilaku baik itu tumbuh."),
        ("Protect today's ten minutes even if the day went badly.",
         "Lindungi sepuluh menit hari ini meski harinya berjalan buruk."),
        ("Have I ever used connection as leverage?",
         "Pernahkah saya memakai kedekatan sebagai alat tawar?"),
        ("\"Today was hard, and we're still doing our ten minutes.\"",
         "\"Hari ini berat, dan sepuluh menit kita tetap jalan.\""),
    ),

    273: d(
        ("Following the child's lead in play",
         "Mengikuti arahan anak dalam bermain"),
        ("Adults are almost incapable of playing without steering. We suggest, we improve, "
         "we turn the game into a lesson about counting. And every correction, however "
         "gentle, tells the child that their way of playing was not quite right.\n\n"
         "Following means doing what they do, saying what they say, and letting the story go "
         "wherever they take it — even when it makes no sense, even when the cars can fly. "
         "For most children this is the rarest experience an adult can offer them: someone "
         "bigger than them who is not trying to change anything.",
         "Orang dewasa hampir tidak sanggup bermain tanpa menyetir. Kita mengusulkan, kita "
         "memperbaiki, kita mengubah permainan menjadi pelajaran berhitung. Dan setiap "
         "koreksi, sehalus apa pun, memberi tahu anak bahwa caranya bermain kurang tepat.\n\n"
         "Mengikuti berarti melakukan apa yang ia lakukan, mengatakan apa yang ia katakan, "
         "dan membiarkan ceritanya pergi ke mana pun ia bawa — meski tidak masuk akal, meski "
         "mobilnya bisa terbang. Bagi kebanyakan anak, ini pengalaman paling langka yang bisa "
         "diberikan orang dewasa: seseorang yang lebih besar darinya dan tidak sedang berusaha "
         "mengubah apa pun."),
        ("Narrate instead of directing. \"The car is going up the wall\" keeps you in their "
         "world; \"why don't you build a road\" pulls them into yours.",
         "Ceritakan, jangan mengarahkan. \"Mobilnya naik ke tembok\" membuat Anda tetap di "
         "dunianya; \"kenapa tidak buat jalan saja\" menarik dia ke dunia Anda."),
        ("Play for ten minutes today without a single suggestion or correction.",
         "Bermainlah sepuluh menit hari ini tanpa satu pun usulan atau koreksi."),
        ("Can I be with my child without improving anything?",
         "Bisakah saya bersama anak tanpa memperbaiki apa pun?"),
        ("\"You decide what happens next. I'll follow.\"",
         "\"Kamu yang menentukan apa yang terjadi berikutnya. Mama/Papa ikut saja.\""),
    ),

    274: d(
        ("Delight in your child",
         "Menikmati kehadiran anak Anda"),
        ("There is a particular thing a face does when someone is glad you walked into the "
         "room. Children read that expression long before they can read words, and they keep "
         "reading it their whole lives.\n\n"
         "Many children are well cared for and rarely delighted in. They are fed, driven, "
         "corrected, and worried about, but they do not often see a face light up at the "
         "sight of them. That expression is not a bonus on top of good parenting. For the "
         "child, it is the evidence that they are wanted rather than merely managed.",
         "Ada ekspresi tertentu di wajah seseorang ketika ia senang Anda masuk ke ruangan. "
         "Anak membaca ekspresi itu jauh sebelum ia bisa membaca kata, dan ia terus membacanya "
         "seumur hidup.\n\n"
         "Banyak anak dirawat dengan baik tetapi jarang dinikmati kehadirannya. Mereka diberi "
         "makan, diantar, dikoreksi, dan dikhawatirkan, tetapi tidak sering melihat wajah yang "
         "berbinar saat melihat mereka. Ekspresi itu bukan bonus di atas pengasuhan yang baik. "
         "Bagi anak, itulah bukti bahwa ia diinginkan, bukan sekadar diurus."),
        ("Let your face show it when your child walks in. Before the questions, before the "
         "instructions — just the face.",
         "Biarkan wajah Anda menunjukkannya ketika anak masuk. Sebelum pertanyaan, sebelum "
         "instruksi — cukup wajahnya."),
        ("Greet your child once today with your face before your words.",
         "Sambut anak Anda sekali hari ini dengan wajah Anda sebelum kata-kata Anda."),
        ("Does my child see that I am glad they exist?",
         "Apakah anak saya melihat bahwa saya senang ia ada?"),
        ("\"There you are. I was hoping you'd come find me.\"",
         "\"Itu dia. Mama/Papa memang lagi berharap kamu datang.\""),
    ),

    275: d(
        ("Attachment signals children send",
         "Sinyal kelekatan yang dikirim anak"),
        ("Children ask for connection in code, and most of the code looks like misbehaviour. "
         "The whining at your elbow while you cook, the sudden silliness the moment you take "
         "a call, the fight picked at bedtime — these are almost never about the thing they "
         "appear to be about.\n\n"
         "Learning to hear the signal underneath changes what you do. You cannot respond well "
         "to a request you have misread as an attack. The grid below covers the four you will "
         "see most often, and the one response that works for all of them: go toward, not "
         "away.",
         "Anak meminta kedekatan dengan kode, dan sebagian besar kodenya tampak seperti "
         "kenakalan. Merengek di samping Anda saat memasak, tiba-tiba konyol begitu Anda "
         "mengangkat telepon, cari ribut menjelang tidur — semua itu hampir tidak pernah "
         "tentang hal yang tampaknya sedang dipermasalahkan.\n\n"
         "Belajar mendengar sinyal di baliknya mengubah apa yang Anda lakukan. Anda tidak bisa "
         "menanggapi dengan baik sebuah permintaan yang Anda salah baca sebagai serangan. "
         "Tabel di bawah memuat empat yang paling sering muncul, dan satu tanggapan yang "
         "berhasil untuk semuanya: mendekat, bukan menjauh."),
        ("When behaviour spikes for no visible reason, try connection before consequence. It "
         "costs two minutes and it is right more often than you expect.",
         "Ketika perilaku memburuk tanpa sebab yang terlihat, coba kedekatan sebelum hukuman. "
         "Ongkosnya dua menit dan lebih sering benar daripada yang Anda kira."),
        ("Catch one bid for connection today and answer it instead of correcting it.",
         "Tangkap satu upaya mencari kedekatan hari ini dan jawablah, jangan koreksi."),
        ("What is my child actually asking for when they act like this?",
         "Apa yang sebenarnya anak saya minta ketika ia bersikap seperti ini?"),
        ("\"Come here a minute. I think you need me.\"",
         "\"Sini sebentar. Kayaknya kamu butuh Mama/Papa.\""),
        framework=fw(
            ("Four bids, badly disguised",
             "Empat permintaan yang menyamar buruk"),
            ("The same request underneath all four: come closer.",
             "Permintaan yang sama di balik keempatnya: mendekatlah."),
            [
                (("The interrupter", "Si penyela"),
                 [("Whining", "Merengek"), ("Clinging", "Menempel")],
                 ("Needs you most urgently the moment you are on the phone, cooking, or "
                  "talking to another adult.",
                  "Paling mendesak membutuhkan Anda tepat saat Anda sedang menelepon, memasak, "
                  "atau bicara dengan orang dewasa lain."),
                 ("\"I lose you when someone else has you.\" Two minutes of full attention "
                  "usually ends it.",
                  "\"Aku kehilangan kamu kalau ada orang lain yang punya kamu.\" Dua menit "
                  "perhatian penuh biasanya menyelesaikannya.")),
                (("The provoker", "Si pemancing"),
                 [("Defiance", "Membangkang"), ("Testing", "Menguji")],
                 ("Picks a fight over nothing, often at bedtime or after you have been away.",
                  "Cari ribut soal hal sepele, sering menjelang tidur atau setelah Anda pergi."),
                 ("\"Are you still on my side?\" Warmth answers it; escalation confirms the "
                  "fear.",
                  "\"Kamu masih di pihakku?\" Kehangatan menjawabnya; membesarkan masalah malah "
                  "membenarkan ketakutannya.")),
                (("The withdrawer", "Si menarik diri"),
                 [("Quiet", "Diam"), ("Door closed", "Pintu tertutup")],
                 ("Goes silent, stays in their room, answers everything with \"fine.\" Easiest "
                  "to miss because it causes no trouble.",
                  "Jadi diam, berlama-lama di kamar, menjawab apa pun dengan \"nggak apa-apa\". "
                  "Paling mudah terlewat karena tidak merepotkan."),
                 ("\"I am not sure you want to come and find me.\" Presence without questions "
                  "works better than questions.",
                  "\"Aku tidak yakin kamu mau datang mencariku.\" Kehadiran tanpa pertanyaan "
                  "lebih berhasil daripada pertanyaan.")),
                (("The regressor", "Si mundur"),
                 [("Baby voice", "Suara bayi"), ("Sudden helplessness", "Tiba-tiba tak berdaya")],
                 ("Suddenly cannot do things they mastered months ago. Common after a new "
                  "sibling, a move, or a hard week.",
                  "Tiba-tiba tidak bisa melakukan hal yang sudah ia kuasai berbulan-bulan lalu. "
                  "Umum setelah ada adik baru, pindah rumah, atau minggu yang berat."),
                 ("\"Am I still the small one you take care of?\" Give the care briefly and "
                  "warmly; it passes.",
                  "\"Aku masih yang kecil yang kamu rawat, kan?\" Berikan perawatan itu sebentar "
                  "dan dengan hangat; ini akan lewat.")),
            ],
        ),
    ),

    276: d(
        ("Reconnecting after absence",
         "Menyambung kembali setelah berpisah"),
        ("Children rarely greet a returning parent with straightforward joy. More often they "
         "ignore you, or fall apart, or turn aggressive within ten minutes of your walking "
         "through the door.\n\n"
         "This is not rejection and it is not ingratitude. It is the release of everything "
         "they held together while you were gone. You are the safe place, and safe places are "
         "where the holding stops. Take the collapse as evidence that you matter, and give "
         "the first fifteen minutes home entirely to reconnection before anything else "
         "starts.",
         "Anak jarang menyambut orang tua yang pulang dengan kegembiraan yang lugas. Lebih "
         "sering mereka mengabaikan Anda, atau hancur menangis, atau berubah agresif dalam "
         "sepuluh menit setelah Anda masuk pintu.\n\n"
         "Ini bukan penolakan dan bukan tidak tahu terima kasih. Ini adalah lepasnya semua "
         "yang ia tahan selama Anda pergi. Anda tempat amannya, dan di tempat aman itulah "
         "menahan diri berhenti. Anggap keruntuhan itu bukti bahwa Anda berarti, dan berikan "
         "lima belas menit pertama di rumah sepenuhnya untuk menyambung kembali sebelum apa "
         "pun dimulai."),
        ("Do not walk in and start managing. Walk in and sit down. The tasks will still be "
         "there in fifteen minutes.",
         "Jangan masuk lalu langsung mengatur. Masuk lalu duduklah. Tugas-tugas itu masih akan "
         "ada lima belas menit lagi."),
        ("Give the first fifteen minutes of your return today to your child, not to the house.",
         "Berikan lima belas menit pertama kepulangan Anda hari ini untuk anak, bukan untuk rumah."),
        ("What does my child's face do in the first minute I come home?",
         "Apa yang terjadi pada wajah anak saya di menit pertama saya pulang?"),
        ("\"I'm back. Nothing else matters for the next few minutes.\"",
         "\"Mama/Papa sudah pulang. Beberapa menit ke depan tidak ada yang lebih penting.\""),
    ),

    277: d(
        ("Reconnecting after school",
         "Menyambung kembali setelah sekolah"),
        ("\"How was school?\" is the least effective question in parenting, and every parent "
         "asks it every day. It arrives at the exact moment the child has the least capacity "
         "to answer — tired, hungry, and still carrying seven hours of holding it together.\n\n"
         "Feed them first, ask nothing, and let the car or the walk be quiet. The information "
         "you want almost always arrives later, sideways, in the bath or in the dark before "
         "sleep. Your job at pickup is to be a soft landing, not an interviewer.",
         "\"Bagaimana sekolahnya?\" adalah pertanyaan paling tidak efektif dalam pengasuhan, "
         "dan setiap orang tua menanyakannya setiap hari. Ia datang tepat di saat anak paling "
         "tidak sanggup menjawab — lelah, lapar, dan masih memikul tujuh jam menahan diri.\n\n"
         "Beri makan dulu, jangan tanya apa-apa, dan biarkan perjalanan pulang berjalan sunyi. "
         "Informasi yang Anda inginkan hampir selalu datang belakangan, dari samping, saat "
         "mandi atau dalam gelap sebelum tidur. Tugas Anda saat menjemput adalah menjadi "
         "pendaratan yang empuk, bukan pewawancara."),
        ("Food and silence first. Questions much later, if at all — most children volunteer "
         "more when nothing is being extracted.",
         "Makanan dan keheningan dulu. Pertanyaan jauh belakangan, kalau perlu — kebanyakan "
         "anak bercerita lebih banyak ketika tidak ada yang sedang digali darinya."),
        ("Skip the questions at pickup today. Offer food and quiet instead.",
         "Lewati pertanyaan saat menjemput hari ini. Tawarkan makanan dan keheningan."),
        ("Am I collecting information or offering rest?",
         "Apakah saya sedang mengumpulkan informasi atau menawarkan istirahat?"),
        ("\"You don't have to tell me anything. Here, eat.\"",
         "\"Nggak usah cerita apa-apa dulu. Nih, makan.\""),
    ),

    278: d(
        ("Repair after discipline",
         "Memperbaiki hubungan setelah mendisiplinkan"),
        ("The moments after a limit are more formative than the limit itself. A child who is "
         "corrected and then left alone in the feeling learns that closeness depends on "
         "behaving. A child who is corrected and then found learns that the relationship "
         "survives their worst.\n\n"
         "Repair does not mean taking the limit back. The rule stands; you simply return to "
         "the child. Both things can be true at once, and holding them together is one of "
         "the more advanced skills in this whole guide.",
         "Momen setelah sebuah batas ditegakkan lebih membentuk daripada batasnya sendiri. "
         "Anak yang dikoreksi lalu ditinggal sendirian dengan perasaannya belajar bahwa "
         "kedekatan bergantung pada berkelakuan baik. Anak yang dikoreksi lalu didatangi "
         "belajar bahwa hubungannya selamat dari sisi terburuknya.\n\n"
         "Memperbaiki bukan berarti menarik kembali batasnya. Aturannya tetap; Anda hanya "
         "kembali kepada anaknya. Keduanya bisa benar sekaligus, dan memegang keduanya "
         "bersamaan adalah salah satu keterampilan paling lanjut di seluruh panduan ini."),
        ("Go back within the hour. Say nothing about the rule. Just be near, and let the "
         "nearness make the point.",
         "Kembalilah dalam satu jam. Jangan bahas aturannya. Cukup berada di dekatnya, dan "
         "biarkan kedekatan itu yang berbicara."),
        ("Return to your child within an hour of the last limit you set today.",
         "Kembalilah kepada anak dalam satu jam setelah batas terakhir yang Anda tegakkan hari ini."),
        ("Does my child know we are alright after I say no?",
         "Apakah anak saya tahu kami baik-baik saja setelah saya berkata tidak?"),
        ("\"That rule still stands. And I still want to be near you.\"",
         "\"Aturannya tetap berlaku. Dan Mama/Papa tetap ingin dekat denganmu.\""),
    ),

    279: d(
        ("Repair after parental anger",
         "Memperbaiki hubungan setelah orang tua marah"),
        ("You will lose your temper. Every parent does, and the ones who claim otherwise are "
         "either lying or not present enough to be tested. What separates homes is not "
         "whether the parent snaps but what happens in the twenty minutes afterwards.\n\n"
         "Repair properly: name what you did, without a because. \"I shouted, and that "
         "wasn't okay\" is repair. \"I shouted because you wouldn't listen\" is a second "
         "attack wearing an apology. The unqualified version teaches your child what an "
         "adult apology looks like — and they will use your template on their own children.",
         "Anda akan kehilangan kesabaran. Setiap orang tua begitu, dan yang mengaku tidak "
         "pernah entah sedang berbohong atau tidak cukup hadir untuk pernah diuji. Yang "
         "membedakan satu rumah dari rumah lain bukan apakah orang tuanya meledak, melainkan "
         "apa yang terjadi dua puluh menit sesudahnya.\n\n"
         "Perbaiki dengan benar: sebutkan apa yang Anda lakukan, tanpa kata karena. \"Mama/Papa "
         "membentak, dan itu tidak benar\" adalah perbaikan. \"Mama/Papa membentak karena kamu "
         "tidak mau dengar\" adalah serangan kedua yang memakai baju permintaan maaf. Versi "
         "tanpa embel-embel mengajari anak seperti apa permintaan maaf orang dewasa — dan ia "
         "akan memakai contoh Anda pada anaknya sendiri."),
        ("Apologise without the word because. The moment you explain, you have moved the "
         "blame back onto the child.",
         "Minta maaf tanpa kata karena. Begitu Anda menjelaskan, Anda sudah memindahkan "
         "kesalahan kembali kepada anak."),
        ("If you lose your temper today, repair it before bedtime with no explanation attached.",
         "Kalau hari ini Anda meledak, perbaiki sebelum waktu tidur tanpa disertai penjelasan."),
        ("Does my apology give the blame back to my child?",
         "Apakah permintaan maaf saya mengembalikan kesalahan kepada anak saya?"),
        ("\"I shouted. That was mine, not yours, and I'm sorry.\"",
         "\"Mama/Papa membentak. Itu salah Mama/Papa, bukan kamu, dan Mama/Papa minta maaf.\""),
    ),

    280: d(
        ("Reducing conditional love messages",
         "Mengurangi pesan cinta bersyarat"),
        ("Almost no parent means to send conditional love, and almost every parent sends it "
         "anyway — in the extra warmth after a good report card, in the coldness that lingers "
         "after a bad afternoon, in the sigh that lands when a child is difficult.\n\n"
         "Children track this with unnerving precision. They notice which version of them "
         "gets the warm voice. And what they learn is not to behave better; it is to hide "
         "the parts of themselves that make the warmth go away. Watch your temperature, not "
         "just your words.",
         "Hampir tidak ada orang tua yang sengaja mengirim cinta bersyarat, dan hampir semua "
         "orang tua tetap mengirimnya — lewat kehangatan ekstra setelah rapor bagus, lewat "
         "dinginnya sikap yang bertahan setelah sore yang buruk, lewat helaan napas yang jatuh "
         "ketika anak sedang sulit.\n\n"
         "Anak melacak ini dengan ketepatan yang mengerikan. Ia tahu versi dirinya yang mana "
         "yang mendapat suara hangat. Dan yang ia pelajari bukan berkelakuan lebih baik; yang "
         "ia pelajari adalah menyembunyikan bagian dirinya yang membuat kehangatan itu pergi. "
         "Perhatikan suhu Anda, bukan hanya kata-kata Anda."),
        ("Track your warmth across a week. If it rises and falls with performance, the child "
         "has already noticed.",
         "Amati kehangatan Anda selama seminggu. Kalau ia naik-turun mengikuti prestasi, anak "
         "sudah lama menyadarinya."),
        ("Give your warmest greeting today to whichever child had the worst day.",
         "Berikan sambutan paling hangat hari ini kepada anak yang harinya paling buruk."),
        ("Which version of my child gets my warm voice?",
         "Versi anak saya yang mana yang mendapat suara hangat saya?"),
        ("\"You don't have to do anything to be loved here.\"",
         "\"Kamu tidak perlu melakukan apa pun untuk dicintai di rumah ini.\""),
    ),

    281: d(
        ("Avoiding favoritism",
         "Menghindari pilih kasih"),
        ("Most parents do have a child who is easier for them, and denying it does more harm "
         "than admitting it privately and adjusting. The easy child matches your temperament, "
         "laughs at your jokes, and does not fight you at bedtime. Of course something in you "
         "relaxes around them.\n\n"
         "The damage is not in the feeling — it is in leaving it unexamined. Count your "
         "minutes honestly. The child who gets less of you is usually the one who is harder "
         "to be with, which means they are also the one who most needs the thing they are "
         "getting least.",
         "Kebanyakan orang tua memang punya anak yang lebih mudah bagi mereka, dan menyangkalnya "
         "lebih merusak daripada mengakuinya diam-diam lalu menyesuaikan diri. Anak yang mudah "
         "cocok dengan watak Anda, tertawa pada lelucon Anda, dan tidak melawan menjelang tidur. "
         "Wajar kalau ada sesuatu dalam diri Anda yang mengendur di dekatnya.\n\n"
         "Kerusakannya bukan pada perasaannya — melainkan pada membiarkannya tak diperiksa. "
         "Hitung menit Anda dengan jujur. Anak yang mendapat lebih sedikit dari Anda biasanya "
         "anak yang lebih sulit didampingi, artinya ia juga anak yang paling membutuhkan hal "
         "yang paling sedikit ia terima."),
        ("Count minutes for one week, per child. The number is usually a surprise, and it is "
         "more honest than your impression.",
         "Hitung menit selama seminggu, per anak. Angkanya biasanya mengejutkan, dan lebih jujur "
         "daripada kesan Anda."),
        ("Give ten minutes today to the child you find hardest.",
         "Berikan sepuluh menit hari ini kepada anak yang paling sulit bagi Anda."),
        ("Which of my children gets the easiest version of me?",
         "Anak saya yang mana yang mendapat versi termudah dari diri saya?"),
        ("\"I've been missing time with you. Let's fix that.\"",
         "\"Mama/Papa kangen waktu berdua sama kamu. Kita perbaiki, ya.\""),
    ),

    282: d(
        ("Different children need different approaches",
         "Anak yang berbeda butuh pendekatan berbeda"),
        ("Fairness in a family is not sameness. The approach that settles one child will "
         "inflame another, and insisting on identical treatment in the name of fairness "
         "guarantees that at least one child is being parented wrong.\n\n"
         "One child needs a firm, short instruction and nothing more. Another needs the same "
         "instruction with thirty seconds of warmth in front of it or they cannot hear it at "
         "all. Same rule, different delivery. That is not favouritism; that is accuracy.",
         "Adil dalam keluarga bukan berarti sama. Pendekatan yang menenangkan satu anak akan "
         "memicu anak yang lain, dan bersikeras memperlakukan semua sama atas nama keadilan "
         "menjamin setidaknya satu anak diasuh dengan cara yang keliru.\n\n"
         "Satu anak butuh instruksi tegas dan pendek, tidak lebih. Anak lain butuh instruksi "
         "yang sama dengan tiga puluh detik kehangatan di depannya, kalau tidak ia sama sekali "
         "tidak bisa mendengarnya. Aturan yang sama, penyampaian yang berbeda. Itu bukan pilih "
         "kasih; itu ketepatan."),
        ("Keep the rules identical and let the delivery differ. Children accept different "
         "approaches; they do not accept different rules.",
         "Pertahankan aturannya persis sama dan biarkan penyampaiannya berbeda. Anak bisa "
         "menerima pendekatan yang berbeda; mereka tidak menerima aturan yang berbeda."),
        ("Deliver the same instruction two different ways today, one per child.",
         "Sampaikan instruksi yang sama dengan dua cara berbeda hari ini, satu untuk tiap anak."),
        ("Am I parenting the child in front of me, or the one I expected?",
         "Apakah saya mengasuh anak yang ada di depan saya, atau anak yang saya bayangkan?"),
        ("\"Same rule for everyone. I just say it differently to each of you.\"",
         "\"Aturannya sama untuk semua. Mama/Papa cuma menyampaikannya beda-beda ke kalian.\""),
    ),

    283: d(
        ("Love languages and children",
         "Bahasa kasih dan anak"),
        ("Parents tend to give love in the form they most want to receive it, which means "
         "some children are being loved generously in a language they do not read.\n\n"
         "The clue is what your child asks for when they are tired or sad. One asks to be "
         "held. One asks you to stay in the room. One brings you a drawing. One wants you to "
         "fix something for them. That request is the language — and it is worth more than "
         "any quiz, because it is what they reach for when the reaching is honest.",
         "Orang tua cenderung memberi cinta dalam bentuk yang paling ingin mereka terima "
         "sendiri, artinya sebagian anak sedang dicintai dengan limpah dalam bahasa yang tidak "
         "bisa mereka baca.\n\n"
         "Petunjuknya ada pada apa yang anak minta ketika ia lelah atau sedih. Satu minta "
         "dipeluk. Satu minta Anda tetap di ruangan. Satu membawakan Anda gambar. Satu ingin "
         "Anda membetulkan sesuatu untuknya. Permintaan itulah bahasanya — dan itu lebih "
         "berharga daripada kuis mana pun, karena itulah yang ia raih ketika permintaannya jujur."),
        ("Watch what your child asks for when they are at their lowest. That is their "
         "language, whatever a book might say.",
         "Perhatikan apa yang anak minta saat ia sedang paling terpuruk. Itulah bahasanya, apa "
         "pun kata buku."),
        ("Offer love today in your child's form, not yours.",
         "Berikan kasih hari ini dalam bentuk milik anak Anda, bukan milik Anda."),
        ("Am I giving love in the shape my child can receive?",
         "Apakah saya memberi kasih dalam bentuk yang bisa diterima anak saya?"),
        ("\"What would help right now — a hug, or me just sitting here?\"",
         "\"Sekarang enaknya apa — dipeluk, atau Mama/Papa duduk di sini saja?\""),
    ),

    284: d(
        ("Affection and consent",
         "Kasih sayang fisik dan izin"),
        ("A child who is required to accept hugs and kisses is learning, very early, that "
         "their body belongs to whoever is asking — and that lesson does not stay inside the "
         "family. It goes with them into every room they enter for the rest of their life.\n\n"
         "This is difficult in cultures where refusing an elder's affection reads as rude, "
         "and the answer is not to abandon warmth but to offer alternatives. A handshake, a "
         "wave, a high five. The child stays polite and keeps the far more important lesson: "
         "no is a sentence that works, even with people you love.",
         "Anak yang diharuskan menerima pelukan dan ciuman sedang belajar, sejak sangat dini, "
         "bahwa tubuhnya milik siapa pun yang meminta — dan pelajaran itu tidak berhenti di "
         "dalam keluarga. Ia ikut ke setiap ruangan yang ia masuki seumur hidupnya.\n\n"
         "Ini sulit di budaya yang menganggap menolak kasih sayang orang yang lebih tua itu "
         "tidak sopan, dan jawabannya bukan meninggalkan kehangatan melainkan menawarkan "
         "alternatif. Salaman, melambai, tos. Anak tetap sopan dan tetap memegang pelajaran "
         "yang jauh lebih penting: kata tidak itu kalimat yang berlaku, bahkan kepada orang "
         "yang kita sayangi."),
        ("Offer a choice rather than a demand: hug, handshake, or wave. The warmth survives; "
         "the consent is preserved.",
         "Tawarkan pilihan, bukan tuntutan: peluk, salaman, atau melambai. Kehangatannya tetap; "
         "izinnya terjaga."),
        ("Ask before one hug today, and accept the answer.",
         "Bertanyalah sebelum satu pelukan hari ini, dan terima jawabannya."),
        ("Does my child know they can say no to touch in this family?",
         "Apakah anak saya tahu ia boleh menolak sentuhan di keluarga ini?"),
        ("\"Hug, handshake, or wave? You choose.\"",
         "\"Peluk, salaman, atau lambai? Kamu yang pilih.\""),
    ),

    285: d(
        ("Building trust through reliability",
         "Membangun kepercayaan lewat keandalan"),
        ("Trust in a family is not built by big declarations. It is built by small promises "
         "kept in a boring, repetitive way until the child stops checking.\n\n"
         "This is why breaking small promises costs more than parents think. A cancelled "
         "park trip is not a small disappointment to a child who has now learned that your "
         "words are provisional. Promise less than you can deliver, and then deliver "
         "everything you promised — including the promises nobody would have noticed you "
         "dropping.",
         "Kepercayaan dalam keluarga tidak dibangun lewat pernyataan besar. Ia dibangun lewat "
         "janji-janji kecil yang ditepati dengan cara membosankan dan berulang sampai anak "
         "berhenti mengecek.\n\n"
         "Karena itulah mengingkari janji kecil berongkos lebih mahal dari perkiraan orang tua. "
         "Batalnya jalan-jalan ke taman bukan kekecewaan kecil bagi anak yang kini belajar "
         "bahwa kata-kata Anda sifatnya sementara. Berjanjilah lebih sedikit dari yang bisa "
         "Anda tepati, lalu tepati semuanya — termasuk janji yang tidak akan ada yang sadar "
         "kalau Anda batalkan."),
        ("If you are not sure you can do it, do not say it. \"I'll try\" is honest; a promise "
         "you might break is not.",
         "Kalau tidak yakin bisa, jangan diucapkan. \"Nanti Mama/Papa usahakan\" itu jujur; "
         "janji yang mungkin Anda langgar tidak."),
        ("Keep every small promise you make today, or do not make it.",
         "Tepati setiap janji kecil yang Anda buat hari ini, atau jangan dibuat."),
        ("Does my child have to check whether I meant it?",
         "Apakah anak saya harus mengecek apakah saya sungguh-sungguh?"),
        ("\"I said I would, so I will. Even though I'm tired.\"",
         "\"Mama/Papa sudah bilang mau, jadi ya dilakukan. Walaupun capek.\""),
    ),

    286: d(
        ("Making home emotionally safe",
         "Membuat rumah aman secara emosional"),
        ("An emotionally safe home is not a home without conflict. It is a home where "
         "conflict is survivable — where nobody is humiliated, nobody is frozen out, and the "
         "argument ends with everyone still belonging.\n\n"
         "Test it with a simple question: when something goes badly wrong for your child, are "
         "you the first person they think of, or the last? The answer is a measurement of "
         "everything you have built, and it is the single most useful piece of information "
         "you can have about your family.",
         "Rumah yang aman secara emosional bukan rumah tanpa konflik. Ia rumah tempat konflik "
         "bisa dilewati — tempat tak ada yang dipermalukan, tak ada yang didiamkan, dan "
         "pertengkaran berakhir dengan semua orang tetap merasa memiliki.\n\n"
         "Ujilah dengan pertanyaan sederhana: ketika terjadi sesuatu yang sangat buruk pada "
         "anak Anda, Andakah orang pertama yang terpikir olehnya, atau yang terakhir? "
         "Jawabannya adalah takaran dari semua yang sudah Anda bangun, dan itu satu-satunya "
         "informasi paling berguna yang bisa Anda punya tentang keluarga Anda."),
        ("Ask yourself whether your child would come to you first with something shameful. "
         "Build toward yes.",
         "Tanyakan pada diri sendiri apakah anak Anda akan datang kepada Anda lebih dulu dengan "
         "sesuatu yang memalukan. Bangunlah menuju jawaban ya."),
        ("Say out loud today that nothing your child tells you will end your love.",
         "Katakan dengan lantang hari ini bahwa tidak ada yang anak ceritakan akan mengakhiri kasih Anda."),
        ("Am I the first person my child would come to, or the last?",
         "Apakah saya orang pertama yang anak saya datangi, atau yang terakhir?"),
        ("\"There is nothing you could tell me that would make me stop loving you.\"",
         "\"Tidak ada satu pun yang bisa kamu ceritakan yang akan membuat Mama/Papa berhenti menyayangimu.\""),
    ),

    287: d(
        ("Shared laughter",
         "Tertawa bersama"),
        ("Laughter is the fastest repair tool a family has, and it is underused because "
         "parents are tired and being funny takes energy that discipline has already spent.\n\n"
         "It is worth the effort anyway. Shared laughter lowers stress hormones in both "
         "bodies at once, and a family that laughs together every day has a reserve to draw "
         "on when the hard weeks arrive. Be careful of one thing only: laughing at a child "
         "and laughing with a child feel identical from the outside and opposite from the "
         "inside.",
         "Tawa adalah alat perbaikan tercepat yang dimiliki sebuah keluarga, dan ia jarang "
         "dipakai karena orang tua lelah dan menjadi lucu butuh energi yang sudah habis "
         "terpakai untuk mendisiplinkan.\n\n"
         "Tetap saja itu sepadan. Tawa bersama menurunkan hormon stres di kedua tubuh "
         "sekaligus, dan keluarga yang tertawa bersama setiap hari punya cadangan untuk "
         "ditarik saat minggu-minggu berat datang. Hati-hati pada satu hal saja: menertawakan "
         "anak dan tertawa bersama anak terlihat sama dari luar dan berlawanan dari dalam."),
        ("Aim for one genuine laugh together a day. Never at the child's expense — that "
         "version teaches them to hide.",
         "Targetkan satu tawa tulus bersama setiap hari. Jangan pernah dengan mengorbankan anak "
         "— versi itu mengajarinya bersembunyi."),
        ("Make your child laugh once today, on purpose.",
         "Buat anak Anda tertawa sekali hari ini, dengan sengaja."),
        ("When did this family last laugh together?",
         "Kapan terakhir keluarga ini tertawa bersama?"),
        ("\"Come here, I've got something ridiculous to show you.\"",
         "\"Sini deh, ada yang konyol mau Mama/Papa tunjukkan.\""),
    ),

    288: d(
        ("Rough-and-tumble play safely",
         "Bermain gulat-gulatan dengan aman"),
        ("Physical play does something no conversation can: it teaches a child where their "
         "body ends, how much force is too much, and how to stop when someone says stop. "
         "Children who never wrestle often struggle to read exactly those limits later.\n\n"
         "The rules are simple. A word that stops everything instantly, honoured every single "
         "time. No pinning a child who cannot get free. And let them win sometimes — a child "
         "who never wins learns that strength always beats them, which is not the lesson you "
         "were going for.",
         "Bermain fisik melakukan sesuatu yang tidak bisa dilakukan percakapan mana pun: ia "
         "mengajari anak di mana tubuhnya berakhir, seberapa banyak tenaga itu terlalu banyak, "
         "dan bagaimana berhenti ketika ada yang bilang berhenti. Anak yang tidak pernah "
         "bergulat sering kesulitan membaca justru batas-batas itu di kemudian hari.\n\n"
         "Aturannya sederhana. Ada satu kata yang menghentikan semuanya seketika, dihormati "
         "setiap kali tanpa kecuali. Jangan mengunci anak sampai ia tidak bisa lepas. Dan "
         "biarkan ia menang sesekali — anak yang tidak pernah menang belajar bahwa kekuatan "
         "selalu mengalahkannya, dan itu bukan pelajaran yang Anda tuju."),
        ("Agree a stop word before you start, and stop the instant it is used — even mid-"
         "laugh. That is where the real lesson lives.",
         "Sepakati kata berhenti sebelum mulai, dan berhentilah begitu kata itu diucapkan — "
         "bahkan di tengah tawa. Di situlah pelajaran sesungguhnya berada."),
        ("Play physically with your child today with an agreed stop word.",
         "Bermainlah secara fisik dengan anak hari ini dengan kata berhenti yang disepakati."),
        ("Do I stop the first time my child says stop?",
         "Apakah saya berhenti pada kali pertama anak saya bilang berhenti?"),
        ("\"Say 'stop' and I stop straight away. Every time. Try it.\"",
         "\"Bilang 'stop' dan Mama/Papa langsung berhenti. Setiap kali. Coba deh.\""),
    ),

    289: d(
        ("Storytelling and bonding",
         "Bercerita dan kedekatan"),
        ("Children are hungry for stories about themselves and about the people they come "
         "from. The story of the night you were born. The story of when your grandfather was "
         "a boy and did something foolish. The story of the year this family had almost "
         "nothing and got through it anyway.\n\n"
         "Research on family stories keeps finding the same thing: children who know where "
         "they come from cope better with difficulty. The stories give them a place to stand "
         "— they belong to something older and more durable than this week.",
         "Anak lapar akan cerita tentang dirinya dan tentang orang-orang asal-usulnya. Cerita "
         "malam ia dilahirkan. Cerita ketika kakeknya masih kecil dan melakukan sesuatu yang "
         "bodoh. Cerita tentang tahun ketika keluarga ini hampir tidak punya apa-apa dan tetap "
         "bisa melewatinya.\n\n"
         "Penelitian tentang cerita keluarga terus menemukan hal yang sama: anak yang tahu dari "
         "mana ia berasal lebih tahan menghadapi kesulitan. Cerita-cerita itu memberinya tempat "
         "berpijak — ia bagian dari sesuatu yang lebih tua dan lebih tahan lama daripada minggu ini."),
        ("Tell one family story a week. Include the hard ones, told at a level the child can "
         "hold — those are the ones that build resilience.",
         "Ceritakan satu kisah keluarga setiap minggu. Termasuk yang berat, disampaikan pada "
         "takaran yang sanggup dipegang anak — justru itulah yang membangun ketahanan."),
        ("Tell your child one true story about your own family tonight.",
         "Ceritakan kepada anak satu kisah nyata tentang keluarga Anda sendiri malam ini."),
        ("What does my child know about where they come from?",
         "Apa yang anak saya tahu tentang dari mana ia berasal?"),
        ("\"Let me tell you about your grandmother when she was your age.\"",
         "\"Mama/Papa ceritakan tentang nenekmu waktu seusiamu, ya.\""),
    ),

    290: d(
        ("Protecting attachment during adolescence",
         "Menjaga kelekatan di masa remaja"),
        ("Adolescents pull away, and parents commonly read the pulling as the end of the "
         "relationship and respond by pulling away too. That mutual retreat is how families "
         "lose teenagers who were never actually lost.\n\n"
         "A teenager needs distance and connection at the same time — which is confusing, and "
         "is nonetheless the job. Stay available without demanding entry. Be in the kitchen "
         "at eleven at night. Drive them places. Teenagers talk in cars and in the dark, and "
         "almost never when a parent has sat them down for a conversation.",
         "Remaja menarik diri, dan orang tua biasanya membaca penarikan itu sebagai akhir dari "
         "hubungan lalu ikut menarik diri juga. Mundur berbarengan itulah cara keluarga "
         "kehilangan remaja yang sebenarnya tidak pernah hilang.\n\n"
         "Remaja butuh jarak dan kedekatan sekaligus — membingungkan, dan tetap saja itulah "
         "tugasnya. Tetap tersedia tanpa menuntut masuk. Berada di dapur pada pukul sebelas "
         "malam. Antarkan mereka ke tempat-tempat. Remaja bicara di dalam mobil dan dalam "
         "gelap, dan hampir tidak pernah ketika orang tuanya sengaja mendudukkan mereka untuk "
         "bicara."),
        ("Be available in the places they actually talk: the car, the kitchen at night, the "
         "walk home. Do not schedule connection.",
         "Hadirlah di tempat mereka benar-benar bicara: mobil, dapur di malam hari, jalan pulang. "
         "Jangan menjadwalkan kedekatan."),
        ("Make yourself available tonight in a place your teenager might talk, without asking "
         "anything.",
         "Sediakan diri Anda malam ini di tempat remaja Anda mungkin bicara, tanpa menanyakan apa pun."),
        ("Am I reading distance as rejection?",
         "Apakah saya membaca jarak sebagai penolakan?"),
        ("\"I'll be up for a while if you feel like company.\"",
         "\"Mama/Papa masih bangun kok, kalau kamu mau ada teman.\""),
    ),

    291: d(
        ("Handling peer-orientation",
         "Menghadapi anak yang lebih berkiblat ke teman"),
        ("When friends become more influential than family, something has usually gone quiet "
         "at home first. Peers do not steal children. They fill a space that was already "
         "empty.\n\n"
         "The answer is not to attack the friends — that reliably pushes the child further "
         "toward them, because now you are the one making them choose. The answer is to make "
         "home warm enough to be worth returning to, and to stay interested in the friends "
         "rather than suspicious of them. Curiosity keeps the door open; criticism closes it.",
         "Ketika teman menjadi lebih berpengaruh daripada keluarga, biasanya ada sesuatu yang "
         "sudah lebih dulu senyap di rumah. Teman sebaya tidak mencuri anak. Mereka mengisi "
         "ruang yang memang sudah kosong.\n\n"
         "Jawabannya bukan menyerang teman-temannya — itu justru mendorong anak makin dekat "
         "kepada mereka, karena kini Andalah yang memaksanya memilih. Jawabannya adalah membuat "
         "rumah cukup hangat untuk layak didatangi kembali, dan tetap tertarik pada teman-"
         "temannya alih-alih curiga kepada mereka. Rasa ingin tahu menjaga pintu tetap terbuka; "
         "kritik menutupnya."),
        ("Invite the friends in rather than shutting them out. You learn more and you stay in "
         "the room.",
         "Undang teman-temannya masuk, jangan ditutup aksesnya. Anda jadi tahu lebih banyak dan "
         "tetap ada di ruangan yang sama."),
        ("Ask one genuinely curious question about your child's friends today.",
         "Ajukan satu pertanyaan yang tulus penasaran tentang teman-teman anak Anda hari ini."),
        ("Is home a place my child wants to come back to?",
         "Apakah rumah adalah tempat yang anak saya ingin datangi kembali?"),
        ("\"Bring them here. I'd like to know who your people are.\"",
         "\"Ajak ke sini. Mama/Papa mau kenal siapa saja orang-orangmu.\""),
    ),

    292: d(
        ("Staying influential as kids grow",
         "Tetap berpengaruh saat anak bertumbuh"),
        ("Your authority over a child expires. Your influence does not have to — but it "
         "converts from one to the other only if the relationship can carry it.\n\n"
         "A parent who spent the early years commanding has nothing left when commanding "
         "stops working around age thirteen. A parent who spent those years connecting still "
         "has a voice at seventeen, at twenty-five, at forty. Influence rides entirely on "
         "relationship, and the exchange rate is set long before you need it.",
         "Kewenangan Anda atas seorang anak ada masa berlakunya. Pengaruh Anda tidak harus "
         "begitu — tetapi yang satu berubah menjadi yang lain hanya jika hubungannya sanggup "
         "menopangnya.\n\n"
         "Orang tua yang menghabiskan tahun-tahun awal dengan memerintah tidak punya sisa apa-"
         "apa ketika memerintah berhenti berhasil di sekitar usia tiga belas. Orang tua yang "
         "menghabiskan tahun-tahun itu dengan membangun kedekatan masih punya suara di usia "
         "tujuh belas, dua puluh lima, empat puluh. Pengaruh sepenuhnya menumpang pada "
         "hubungan, dan nilai tukarnya ditetapkan jauh sebelum Anda membutuhkannya."),
        ("Spend the early years building the relationship you will need later. Authority is "
         "borrowed; influence is earned.",
         "Pakailah tahun-tahun awal untuk membangun hubungan yang akan Anda butuhkan nanti. "
         "Kewenangan itu pinjaman; pengaruh itu diperoleh."),
        ("Ask your child's opinion about something real today, and take it seriously.",
         "Tanyakan pendapat anak Anda tentang sesuatu yang nyata hari ini, dan tanggapi dengan serius."),
        ("What will my voice be worth to my child at twenty?",
         "Seberapa berharga suara saya bagi anak saya di usia dua puluh?"),
        ("\"What do you think we should do? I actually want to know.\"",
         "\"Menurutmu kita sebaiknya bagaimana? Mama/Papa benar-benar mau tahu.\""),
    ),

    293: d(
        ("Inviting conversation without pressure",
         "Mengundang percakapan tanpa menekan"),
        ("Direct questions close children. \"What's wrong?\" asked while looking straight at "
         "them is an interrogation, however kindly meant, and most children respond to "
         "interrogation by producing nothing.\n\n"
         "Talk sideways. Speak while driving, while washing up, while walking — anywhere the "
         "child does not have to hold your gaze. Offer a small piece of yourself first, then "
         "leave a silence. The silence is the invitation. Fill it and you have taken the "
         "space they were about to use.",
         "Pertanyaan langsung menutup anak. \"Kamu kenapa?\" yang ditanyakan sambil menatap "
         "lurus adalah interogasi, sebaik apa pun niatnya, dan kebanyakan anak menanggapi "
         "interogasi dengan tidak mengeluarkan apa-apa.\n\n"
         "Bicaralah dari samping. Bicara sambil menyetir, sambil mencuci piring, sambil "
         "berjalan — di mana pun anak tidak harus menahan tatapan Anda. Tawarkan sepotong "
         "kecil tentang diri Anda dulu, lalu tinggalkan keheningan. Keheningan itulah "
         "undangannya. Kalau Anda mengisinya, Anda telah mengambil ruang yang tadi hendak ia "
         "pakai."),
        ("Offer something about your own day first. Then stop talking and keep your eyes on "
         "the road.",
         "Tawarkan dulu sesuatu tentang hari Anda sendiri. Lalu berhenti bicara dan tetap "
         "arahkan mata ke jalan."),
        ("Start one conversation today side by side instead of face to face.",
         "Mulai satu percakapan hari ini secara berdampingan, bukan berhadapan."),
        ("Do my questions open my child or close them?",
         "Apakah pertanyaan saya membuka anak saya atau menutupnya?"),
        ("\"Something odd happened to me today...\" — then wait.",
         "\"Tadi ada kejadian aneh sama Mama/Papa...\" — lalu tunggu."),
    ),

    294: d(
        ("Presence over performance",
         "Kehadiran di atas penampilan"),
        ("Children do not need the parent from the advertisement — the one who is patient at "
         "all hours, plans elaborate activities, and never checks their phone. They need "
         "someone who is actually there, imperfectly, most days.\n\n"
         "Chasing the performance is exhausting and it produces a parent who is present in "
         "photographs and absent in the room. Ordinary presence beats extraordinary effort. "
         "Sitting on the floor while your child plays, doing nothing impressive at all, is the "
         "whole thing.",
         "Anak tidak membutuhkan orang tua versi iklan — yang sabar sepanjang jam, merancang "
         "kegiatan rumit, dan tidak pernah melihat ponsel. Mereka membutuhkan seseorang yang "
         "benar-benar ada, dengan segala kekurangannya, di sebagian besar hari.\n\n"
         "Mengejar penampilan itu melelahkan dan menghasilkan orang tua yang hadir di foto dan "
         "absen di ruangan. Kehadiran yang biasa mengalahkan usaha yang luar biasa. Duduk di "
         "lantai sementara anak bermain, tanpa melakukan apa pun yang mengesankan, itulah "
         "seluruhnya."),
        ("Lower the production value. Sit on the floor. That is enough, and it always was.",
         "Turunkan tuntutan kemasannya. Duduk di lantai. Itu sudah cukup, dan memang selalu cukup."),
        ("Sit on the floor near your child today and do nothing impressive.",
         "Duduklah di lantai dekat anak Anda hari ini dan jangan lakukan apa pun yang mengesankan."),
        ("Am I performing parenting or doing it?",
         "Apakah saya sedang mempertunjukkan pengasuhan atau menjalankannya?"),
        ("\"I'm just going to sit here with you for a bit.\"",
         "\"Mama/Papa duduk di sini sama kamu sebentar, ya.\""),
    ),

    295: d(
        ("When children withdraw",
         "Ketika anak menarik diri"),
        ("A withdrawing child triggers something urgent in a parent, and the urgency almost "
         "always makes it worse. Pushing at a closed door confirms to the child that opening "
         "it means being flooded.\n\n"
         "Stay near without requiring anything. Bring food. Sit in the same room doing your "
         "own thing. Say one sentence that does not demand a reply and then let it be. "
         "Children come out when the coming out is safe and unremarked — and they come out "
         "faster to a parent who did not make their withdrawal into an event.",
         "Anak yang menarik diri memicu sesuatu yang mendesak dalam diri orang tua, dan "
         "kemendesakan itu hampir selalu memperburuk keadaan. Mendorong pintu yang tertutup "
         "justru membenarkan dugaan anak bahwa membukanya berarti dibanjiri.\n\n"
         "Tetaplah dekat tanpa menuntut apa pun. Bawakan makanan. Duduk di ruangan yang sama "
         "sambil mengerjakan urusan Anda sendiri. Ucapkan satu kalimat yang tidak menuntut "
         "jawaban lalu biarkan. Anak keluar ketika keluar itu aman dan tidak dikomentari — dan "
         "mereka keluar lebih cepat kepada orang tua yang tidak menjadikan penarikan diri itu "
         "sebuah peristiwa."),
        ("Stay in the room without questions. Presence without demand is the only thing that "
         "opens a closed child.",
         "Tetaplah di ruangan tanpa pertanyaan. Kehadiran tanpa tuntutan adalah satu-satunya "
         "yang membuka anak yang menutup diri."),
        ("Be near a withdrawn child today without asking a single question.",
         "Berada di dekat anak yang menarik diri hari ini tanpa satu pun pertanyaan."),
        ("Can I stay close without needing my child to open?",
         "Bisakah saya tetap dekat tanpa mengharuskan anak saya membuka diri?"),
        ("\"I'm not going to ask you anything. I'm just here.\"",
         "\"Mama/Papa tidak akan tanya apa-apa. Cuma di sini saja.\""),
    ),

    296: d(
        ("Supporting introverted children",
         "Mendukung anak yang introver"),
        ("An introverted child is not shy, broken, or in need of fixing. They recharge alone "
         "and spend energy in company, which is a wiring difference rather than a deficiency "
         "— and a house full of extroverts can make such a child feel like a problem to be "
         "solved.\n\n"
         "Protect their recovery time the way you would protect sleep. Do not announce their "
         "quietness to guests. And never apologise for them in their hearing; a child who "
         "hears their parent apologise for who they are learns that who they are is an "
         "inconvenience.",
         "Anak yang introver bukan pemalu, bukan rusak, dan tidak perlu diperbaiki. Ia mengisi "
         "ulang tenaga saat sendirian dan mengeluarkan tenaga saat bersama orang, dan itu "
         "perbedaan cara kerja, bukan kekurangan — dan rumah yang penuh orang ekstrover bisa "
         "membuat anak seperti ini merasa dirinya masalah yang harus diselesaikan.\n\n"
         "Lindungi waktu pemulihannya seperti Anda melindungi tidur. Jangan mengumumkan "
         "pendiamnya kepada tamu. Dan jangan pernah meminta maaf atas dirinya dalam "
         "pendengarannya; anak yang mendengar orang tuanya meminta maaf atas siapa dirinya "
         "belajar bahwa dirinya adalah sebuah kerepotan."),
        ("Build recovery time into busy days, and never explain your child's quietness to "
         "other people while they can hear you.",
         "Sisipkan waktu pemulihan di hari-hari yang padat, dan jangan pernah menjelaskan "
         "pendiamnya anak Anda kepada orang lain dalam jarak dengarnya."),
        ("Protect one stretch of quiet for your child today, and defend it.",
         "Lindungi satu jeda tenang untuk anak Anda hari ini, dan pertahankan."),
        ("Do I treat my child's temperament as a trait or a problem?",
         "Apakah saya memperlakukan watak anak saya sebagai sifat atau sebagai masalah?"),
        ("\"You've had a lot of people today. Go and have some quiet.\"",
         "\"Hari ini kamu ketemu banyak orang. Sana, cari tenang dulu.\""),
    ),

    297: d(
        ("Supporting strong-willed children",
         "Mendukung anak yang berkemauan kuat"),
        ("The strong-willed child is exhausting at four and formidable at twenty-four. The "
         "same quality that makes them argue every limit will one day make them impossible "
         "to bully, hard to manipulate, and unwilling to go along with something wrong "
         "because everyone else did.\n\n"
         "The goal is not to break the will. It is to keep the will and add the skills — "
         "how to disagree respectfully, when to yield, how to pick the fight worth having. "
         "Give them real choices inside firm limits, and you get a partner instead of an "
         "opponent.",
         "Anak yang berkemauan kuat melelahkan di usia empat dan luar biasa tangguh di usia dua "
         "puluh empat. Sifat yang sama yang membuatnya mendebat setiap batas suatu hari akan "
         "membuatnya mustahil ditindas, sulit dimanipulasi, dan tidak mau ikut-ikutan pada hal "
         "yang salah hanya karena semua orang melakukannya.\n\n"
         "Tujuannya bukan mematahkan kemauan itu. Tujuannya menjaga kemauannya dan menambahkan "
         "keterampilannya — cara berbeda pendapat dengan hormat, kapan harus mengalah, "
         "bagaimana memilih pertarungan yang layak. Beri pilihan yang nyata di dalam batas yang "
         "tegas, dan Anda mendapat rekan, bukan lawan."),
        ("Offer real choices inside the limit. The child who feels some control fights the "
         "limit far less.",
         "Tawarkan pilihan yang nyata di dalam batasnya. Anak yang merasa punya sedikit kendali "
         "jauh lebih jarang melawan batas itu."),
        ("Give your strong-willed child one genuine choice today inside a limit you hold.",
         "Beri anak Anda yang berkemauan kuat satu pilihan yang sungguhan hari ini di dalam "
         "batas yang Anda pegang."),
        ("Am I trying to break my child's will or shape it?",
         "Apakah saya sedang berusaha mematahkan kemauan anak saya atau membentuknya?"),
        ("\"You can't change the rule, but you can choose how we do it.\"",
         "\"Aturannya tidak bisa kamu ubah, tapi kamu boleh memilih caranya.\""),
    ),

    298: d(
        ("Weekly reflection",
         "Refleksi mingguan"),
        ("Connection is measurable if you are honest, and the honest measure is not how much "
         "you love your child. It is how much undistracted time they actually received this "
         "week.\n\n"
         "Look at the seven days behind you. On how many of them did your child have your "
         "full attention for even ten minutes? Four out of seven is a good week for a working "
         "parent. Zero is information, not a verdict — and it is the kind of information that "
         "changes next week if you let it.",
         "Kedekatan bisa diukur kalau Anda jujur, dan ukuran yang jujur bukan seberapa besar "
         "Anda mencintai anak Anda. Ukurannya adalah berapa banyak waktu tanpa gangguan yang "
         "benar-benar ia terima minggu ini.\n\n"
         "Lihat tujuh hari di belakang Anda. Berapa hari di antaranya anak Anda mendapat "
         "perhatian penuh Anda meski hanya sepuluh menit? Empat dari tujuh sudah minggu yang "
         "baik untuk orang tua yang bekerja. Nol itu informasi, bukan vonis — dan itu jenis "
         "informasi yang mengubah minggu depan kalau Anda mengizinkannya."),
        ("Count the days, not the intentions. The number is the only honest measure you have.",
         "Hitung harinya, bukan niatnya. Angka itu satu-satunya ukuran jujur yang Anda punya."),
        ("Count how many days this week your child had ten undistracted minutes with you.",
         "Hitung berapa hari minggu ini anak Anda mendapat sepuluh menit tanpa gangguan bersama Anda."),
        ("How many days this week did my child truly have me?",
         "Berapa hari minggu ini anak saya benar-benar memiliki saya?"),
        ("\"I want more days like this one. Same time tomorrow?\"",
         "\"Mama/Papa mau lebih banyak hari seperti hari ini. Besok jam segini lagi, ya?\""),
    ),

    299: d(
        ("Attachment review day",
         "Hari meninjau kelekatan"),
        ("Twenty-nine days on connection, and if you take one thing from this chapter, take "
         "this: the relationship is not the reward for parenting well. It is the mechanism by "
         "which everything else works.\n\n"
         "Every technique in the other eleven chapters lands differently depending on whether "
         "the child feels held by you. The same limit, the same words, the same tone — "
         "delivered inside a warm relationship it teaches, delivered inside a cold one it "
         "only controls. If you are ever unsure what to do next, connection is almost never "
         "the wrong answer.",
         "Dua puluh sembilan hari tentang kedekatan, dan kalau Anda hanya mengambil satu hal "
         "dari bab ini, ambillah yang ini: hubungan bukan hadiah karena berhasil mengasuh "
         "dengan baik. Ia adalah mesin yang membuat semua hal lain bekerja.\n\n"
         "Setiap teknik di sebelas bab lainnya mendarat berbeda tergantung apakah anak merasa "
         "dipegang oleh Anda. Batas yang sama, kata yang sama, nada yang sama — disampaikan di "
         "dalam hubungan yang hangat ia mengajar, disampaikan di dalam hubungan yang dingin ia "
         "hanya mengendalikan. Kalau Anda ragu harus berbuat apa berikutnya, kedekatan hampir "
         "tidak pernah jadi jawaban yang salah."),
        ("When you do not know what to do, connect first. It is right often enough to be a "
         "default.",
         "Ketika Anda tidak tahu harus berbuat apa, dekati dulu. Itu cukup sering benar untuk "
         "dijadikan pilihan bawaan."),
        ("Name one way your relationship with your child is different than it was a month ago.",
         "Sebutkan satu cara hubungan Anda dengan anak berbeda dibanding sebulan lalu."),
        ("If the relationship is the curriculum, what have I been teaching?",
         "Kalau hubungan adalah kurikulumnya, apa yang selama ini saya ajarkan?"),
        ("\"I'm glad you're mine. That's all — no lesson attached.\"",
         "\"Mama/Papa senang kamu anak Mama/Papa. Itu saja — tidak ada pelajarannya.\""),
    ),
}
