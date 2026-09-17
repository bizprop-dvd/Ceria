# The News tab — how Ceria posts an update

The app has a **News** tab (Indonesian: *Kabar*) where Ceria announces
gatherings, courses, and news. Everything in it is written by Ceria's team.
Nothing a family writes ever goes there.

This page is for whoever posts the updates and for whoever looks after
yayasanceria.org. It has three parts: **how to post**, **what the web team
sets up once**, and **why it works this way**.

---

## 1. How to post an update

1. Open `tools/news-composer.html` in any browser — double-clicking the file is
   enough. Nothing is installed and nothing is sent anywhere; the page runs on
   your own computer.
2. Load the file that is currently live, so old posts are kept. Either press
   **Ambil dari situs web**, or download `news.json` from the site and choose it
   with **Choose File**. (If this is the first post ever, press **Mulai
   kosong**.)
3. Press **Tulis kabar baru** and write the post. Fill both languages when you
   can; if one is left empty the app shows the other rather than nothing.
4. Press **Unduh news.json**.
5. Send that file to the web team, who replace the file at
   **https://www.yayasanceria.org/app/news.json**.

Within a few hours every phone has it. Nobody needs to update the app, and
neither store has to approve anything — the app only reads a file, and the file
is not part of the app.

### What each field does

| Field | What it does |
| --- | --- |
| **Tanggal** | The date shown on the post, and what it is sorted by. |
| **Tampil sampai** | Optional. After this day the post disappears on its own. Use it for events, so a gathering that has happened is not still being announced. |
| **Sematkan** | Keeps the post at the top of the list, above newer ones. |
| **Judul / Isi** | The post itself. A blank line starts a new paragraph. |
| **Acara** | Optional time and place, shown in a box above the text. |
| **Tautan** | Optional button — a registration form, a WhatsApp group, an article. Must start with `https://`. |
| **Gambar** | Optional picture, `https://` only, about 1200 px wide. It is downloaded when the post is opened, so keep it under ~300 kB. |
| **Kode kabar** | How the app tells posts apart. **Never change it after a post is live** — a changed code makes every phone treat it as a brand-new post. |

### A few habits worth keeping

- **Write as Ceria speaks.** The tab sits beside a parent's diary; an
  announcement that shouts is out of place there.
- **Set "Tampil sampai" on anything with a date.** It is the difference between
  a noticeboard and a pile of old paper.
- **Keep the list short.** Ten or fifteen posts is plenty. Delete the ones
  nobody needs; they are not an archive.
- **Post in Indonesian first.** English can follow, and the app copes if it
  never does.

---

## 2. What the web team sets up once

Publish one file at a URL that will not move:

```
https://www.yayasanceria.org/app/news.json
```

Serve it with:

| Header | Value | Why |
| --- | --- | --- |
| `Content-Type` | `application/json; charset=utf-8` | |
| `Access-Control-Allow-Origin` | `*` | Only needed for the browser build of the app. On a phone the request is made by the operating system, which is not subject to CORS — but set it anyway so the web preview works. |
| `Cache-Control` | `public, max-age=300` | Five minutes. Long enough to be cheap, short enough that a correction is not stuck behind a CDN. |

The file is public and contains nothing private. It replaces the previous one
each time; keeping the old copies is optional but makes mistakes easy to undo.

If the address ever has to change, remember that **installs already out there
keep reading the old one**. Prefer a redirect at the old address over changing
`newsUrl` in the app.

### The file's shape

```json
{
  "updated": "2026-09-17T09:00:00+07:00",
  "items": [
    {
      "id": "2026-09-temu-keluarga",
      "date": "2026-09-28",
      "pinned": true,
      "until": "2026-09-29",
      "title": { "en": "Family gathering in Surabaya", "id": "Temu keluarga di Surabaya" },
      "body":  { "en": "An afternoon together…", "id": "Sore bersama…" },
      "event": {
        "when":  { "en": "Sunday 28 September, 16.00–18.00", "id": "Minggu 28 September, 16.00–18.00" },
        "place": { "en": "Ceria office, Surabaya", "id": "Kantor Ceria, Surabaya" }
      },
      "link": {
        "url": "https://www.yayasanceria.org/daftar",
        "label": { "en": "Tell us you are coming", "id": "Beri tahu kami" }
      },
      "image": "https://www.yayasanceria.org/app/img/temu-sept.jpg"
    }
  ]
}
```

Only `id`, `date`, `title`, and `body` are required. The app reads the file
defensively: a post missing something required is skipped, a post with a bad
date is skipped, and a file that will not parse at all leaves the last good
copy on screen. One bad edit cannot empty the tab or crash the app.

---

## 3. Why a file, and what else was possible

The app asks for one public file and keeps a copy on the phone. That is the
whole mechanism. It costs nothing to run, there is no server to keep patched,
no admin password to lose, and no database holding anything about a family. It
also means the tab works on a bus with no signal — the saved copy is shown, and
the date it was fetched is not hidden from anyone.

Three other routes were considered:

- **A page in the repository, published by GitHub.** Free, and every change is
  versioned and reversible. It needs whoever posts to be comfortable with
  GitHub, which is a real cost for a small team.
- **A Google Sheet, converted to `news.json` on a schedule.** The nicest
  writing experience for a team already in Google Workspace, and the natural
  next step if posting becomes frequent or more than one person does it. It
  needs a small scheduled job to do the converting.
- **A proper backend with admin logins** (Firebase, Supabase, a CMS). This is
  what you move to if you ever want push notifications, several editors with
  different permissions, or scheduled publishing. It also means an account
  system, a bill, something to maintain, and one more place where data about
  families could accumulate. Not worth it to announce a gathering.

Start with the file. Everything above upgrades to the others without the app
changing, because all three end at the same address serving the same JSON.

### What this does not do yet

**Nothing buzzes.** A post appears with a quiet pink dot on the News tab, seen
the next time the app is opened. A phone notification for a new post needs
Firebase Cloud Messaging and a signing key on Ceria's side — a separate
decision, and one that should be made carefully: an app that interrupts a
parent's evening to advertise is exactly what Ceria said it did not want to be.

---

## Where this lives in the code

| File | What it does |
| --- | --- |
| `src/lib/news.ts` | Fetching, caching, and reading the file safely. |
| `src/lib/news.test.ts` | What the app does with a malformed file. |
| `src/store/NewsContext.tsx` | Holds the list for the app; counts what has not been seen. |
| `src/screens/News.tsx`, `src/screens/NewsPost.tsx` | The tab and one post. |
| `src/config.ts` | `newsUrl` — the address above. |
| `public/news.json` | Shipped inside the app; shown only until the phone first reaches the website. Keep it evergreen. |
| `tools/news-composer.html` | The page Ceria's team writes posts in. |
