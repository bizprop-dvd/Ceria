import json

def b(en, id): return {"en": en, "id": id}

data = {
    "_note": "Diary front-matter extracted from Ceria_Family_Diary_{Combined,Solo}_EN.pdf. "
             "Indonesian is a faithful translation of the founder's English text.",
    "welcome": {
        "combined": b(
            "If you opened this diary, something brought you both here. A wish to parent more "
            "steadily. A hope to do this work as a team rather than two tired people running "
            "parallel shifts. A quiet sense that what you build together is bigger than what "
            "either of you builds alone.\n\n"
            "This diary is small on purpose. Three short prompts a day per parent, one shared "
            "reflection on Sundays, a five-minute review at the end of the week. It is built to "
            "fit into a tired Tuesday night, not a perfect Saturday.\n\n"
            "There is no right way to use this. Skip days. Come back. Write a single line. Write a "
            "paragraph. Whatever lands today is enough.\n\n"
            "From all of us at Ceria — welcome to the year.",
            "Jika Anda berdua membuka diari ini, pasti ada sesuatu yang membawa Anda ke sini. "
            "Keinginan untuk mengasuh dengan lebih tenang. Harapan untuk melakukannya sebagai tim, "
            "bukan dua orang lelah yang berjalan sendiri-sendiri. Perasaan diam bahwa apa yang "
            "Anda bangun bersama lebih besar daripada yang bisa dibangun sendiri.\n\n"
            "Diari ini sengaja dibuat kecil. Tiga pertanyaan singkat setiap hari untuk tiap orang "
            "tua, satu refleksi bersama di hari Minggu, dan tinjauan lima menit di akhir minggu. "
            "Dibuat agar muat di malam Selasa yang lelah, bukan Sabtu yang sempurna.\n\n"
            "Tidak ada cara yang benar untuk memakainya. Lewati beberapa hari. Kembali lagi. Tulis "
            "satu baris. Tulis satu paragraf. Apa pun yang muncul hari ini sudah cukup.\n\n"
            "Dari kami semua di Ceria — selamat datang di tahun ini.",
        ),
        "solo": b(
            "If you opened this diary, something brought you here. A wish to be more present. A "
            "hope to parent with less yelling and more vision. A quiet sense that you want this "
            "work to compound, not just survive.\n\n"
            "This diary is small on purpose. Three short prompts a day, one reflection on Sundays, "
            "a five-minute review at the end of the week. It is built to fit into a tired Tuesday "
            "night, not a perfect Saturday.\n\n"
            "There is no right way to use this. Skip days. Come back. Write a single line. Write a "
            "paragraph. Whatever lands today is enough.\n\n"
            "From all of us at Ceria — welcome to the year.",
            "Jika Anda membuka diari ini, pasti ada sesuatu yang membawa Anda ke sini. Keinginan "
            "untuk lebih hadir. Harapan untuk mengasuh dengan lebih sedikit teriakan dan lebih "
            "banyak visi. Perasaan diam bahwa Anda ingin pekerjaan ini bertumbuh, bukan sekadar "
            "bertahan.\n\n"
            "Diari ini sengaja dibuat kecil. Tiga pertanyaan singkat setiap hari, satu refleksi di "
            "hari Minggu, dan tinjauan lima menit di akhir minggu. Dibuat agar muat di malam "
            "Selasa yang lelah, bukan Sabtu yang sempurna.\n\n"
            "Tidak ada cara yang benar untuk memakainya. Lewati beberapa hari. Kembali lagi. Tulis "
            "satu baris. Tulis satu paragraf. Apa pun yang muncul hari ini sudah cukup.\n\n"
            "Dari kami semua di Ceria — selamat datang di tahun ini.",
        ),
    },
    "howToUse": {
        "combined": [
            {"title": b("Three minutes a day", "Tiga menit sehari"),
             "body": b("Open the diary at night. Write one moment with your child, one feeling you noticed, one thing you want to try tomorrow. That's it.",
                       "Buka diari di malam hari. Tulis satu momen bersama anak, satu perasaan yang Anda sadari, satu hal yang ingin Anda coba besok. Itu saja.")},
            {"title": b("Read on Sunday", "Membaca di hari Minggu"),
             "body": b("Once a week, sit with the Sunday reflection question. Write your own answer. Then read your partner's. Don't debate. Just read.",
                       "Sekali seminggu, renungkan pertanyaan refleksi Minggu. Tulis jawaban Anda sendiri. Lalu baca jawaban pasangan Anda. Jangan berdebat. Cukup baca.")},
            {"title": b("Five-minute weekly debrief", "Debrief mingguan lima menit"),
             "body": b("Sunday night, take five minutes together: one thing that worked, one thing that didn't, one agreement for next week.",
                       "Malam Minggu, luangkan lima menit bersama: satu hal yang berhasil, satu yang tidak, satu kesepakatan untuk minggu depan.")},
            {"title": b("Monthly review", "Tinjauan bulanan"),
             "body": b("Every fourth week, the diary pauses for a one-page monthly review. This is where scattered effort starts to compound.",
                       "Setiap minggu keempat, diari berhenti sejenak untuk tinjauan bulanan satu halaman. Di sinilah usaha yang tersebar mulai berbuah.")},
            {"title": b("Imperfect is enough", "Tidak sempurna pun cukup"),
             "body": b("Skip days. Skip weeks. Come back. The diary is here to serve you, not the other way around. Three honest entries are worth more than thirty performed ones.",
                       "Lewati beberapa hari. Lewati beberapa minggu. Kembali lagi. Diari ini untuk melayani Anda, bukan sebaliknya. Tiga catatan yang jujur lebih berharga daripada tiga puluh yang dibuat-buat.")},
        ],
        "solo": [
            {"title": b("Three minutes a day", "Tiga menit sehari"),
             "body": b("Open the diary at night. Write one moment with your child, one feeling you noticed, one thing you want to try tomorrow. That's it.",
                       "Buka diari di malam hari. Tulis satu momen bersama anak, satu perasaan yang Anda sadari, satu hal yang ingin Anda coba besok. Itu saja.")},
            {"title": b("Reflect on Sunday", "Refleksi di hari Minggu"),
             "body": b("Once a week, sit with the Sunday reflection question. Write more here than on weekdays. This is where small noticing turns into seeing.",
                       "Sekali seminggu, renungkan pertanyaan refleksi Minggu. Tulis lebih banyak di sini daripada di hari biasa. Di sinilah perhatian kecil berubah menjadi pemahaman.")},
            {"title": b("Five-minute weekly review", "Tinjauan mingguan lima menit"),
             "body": b("Sunday night, take five minutes alone: one thing that worked, one thing that didn't, one intention for next week.",
                       "Malam Minggu, luangkan lima menit sendiri: satu hal yang berhasil, satu yang tidak, satu niat untuk minggu depan.")},
            {"title": b("Monthly review", "Tinjauan bulanan"),
             "body": b("Every fourth week, the diary pauses for a one-page monthly review. This is where scattered effort starts to compound.",
                       "Setiap minggu keempat, diari berhenti sejenak untuk tinjauan bulanan satu halaman. Di sinilah usaha yang tersebar mulai berbuah.")},
            {"title": b("Imperfect is enough", "Tidak sempurna pun cukup"),
             "body": b("Skip days. Skip weeks. Come back. The diary is here to serve you, not the other way around. Three honest entries are worth more than thirty performed ones.",
                       "Lewati beberapa hari. Lewati beberapa minggu. Kembali lagi. Diari ini untuk melayani Anda, bukan sebaliknya. Tiga catatan yang jujur lebih berharga daripada tiga puluh yang dibuat-buat.")},
        ],
    },
    "settingUp": {
        "intro": b("Three short prompts before you begin. Whatever you write — that's where you're starting from.",
                   "Tiga pertanyaan singkat sebelum memulai. Apa pun yang Anda tulis — dari situlah Anda memulai."),
        "combined": {
            "prompts": [
                b("What season is our family actually in right now?", "Sedang berada di musim apa keluarga kami saat ini?"),
                b("What kind of parents do we hope to become this year?", "Menjadi orang tua seperti apa yang kami harapkan tahun ini?"),
                b("What's one thing we want our home to feel more like?", "Satu hal apa yang ingin kami rasakan lebih kuat di rumah kami?"),
            ],
        },
        "solo": {
            "prompts": [
                b("What season is my family actually in right now?", "Sedang berada di musim apa keluarga saya saat ini?"),
                b("What kind of parent do I hope to become this year?", "Menjadi orang tua seperti apa yang saya harapkan tahun ini?"),
                b("What's one thing I want our home to feel more like?", "Satu hal apa yang ingin saya rasakan lebih kuat di rumah kami?"),
            ],
        },
    },
}

json.dump(data, open("/home/user/Ceria/content/diary_intro.json", "w"), ensure_ascii=False, indent=2)
print("wrote diary_intro.json")
