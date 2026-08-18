# Ceria Family App — Claude Code Build Brief

> Hand this entire folder to Claude Code. This document is the master spec.
> Read it fully before writing any code.

---

## 1. What we are building

A cross-platform mobile app (Android + iOS) for **Ceria** (Yayasan Sukacita
Keluarga Indonesia) that bundles three existing content products into one app:

1. **Toolkit** — 12 printable-style parenting tools (worksheets, trackers, charts)
2. **Guidebook** — 12-chapter bilingual parenting guide
3. **Diary** — 52-week dual-track family diary (daily prompts + weekly reflection)

The app is **freemium**:
- **Free**: everything mapping to Chapters 1–4 (the first four themes)
- **Paid**: Chapters 5–12, unlocked by a single one-time in-app purchase

Content is bilingual (English + Bahasa Indonesia) with a language toggle.

---

## 2. The single most important architectural constraint: IN-APP PURCHASE

The founder has chosen the **official app store + IAP** route (not PWA, not
web-unlock). This has hard consequences that shape the whole build:

- **Apple App Store and Google Play REQUIRE their own in-app purchase system**
  for unlocking digital content. You may NOT use Midtrans, Xendit, or any
  local Indonesian payment gateway to unlock Chapters 5–12 inside the app.
  Apple/Google will reject the app.
- Use **RevenueCat** (https://www.revenuecat.com) as the IAP abstraction layer.
  It wraps both Apple StoreKit and Google Play Billing behind one SDK, has a
  generous free tier, and is the standard choice for Capacitor/React Native apps.
- The purchase is a **non-consumable one-time unlock** (buy once, unlocked
  forever, restorable on reinstall). NOT a subscription.
- Product ID suggestion: `ceria_full_unlock`
- You must implement **"Restore Purchases"** — Apple requires it for approval.

### Pricing note for the founder (not a code task)
Apple/Google take 15–30% commission. For a yayasan whose proceeds fund free
programs, price accordingly. A one-time unlock around IDR 249,000–349,000 is
reasonable. Apple's Small Business Program drops commission to 15% if annual
revenue is under USD 1M — the founder should enroll.

---

## 3. Tech stack (chosen, do not re-litigate)

- **Vite + React + TypeScript** — app shell and UI
- **Capacitor** (https://capacitorjs.com) — wraps the web app into native
  Android + iOS binaries
- **RevenueCat** (`@revenuecat/purchases-capacitor`) — IAP
- **Capacitor Preferences API** — local storage for diary entries (NOT
  localStorage — Capacitor Preferences persists reliably on device)
- **Tailwind CSS** — styling, using Ceria brand tokens (below)
- **react-router** — navigation (hash-based, works in Capacitor webview)

### Why this stack
One codebase → both platforms. The founder already scoped Vite + Capacitor in
prior planning. RevenueCat is the least-painful path to compliant IAP.

---

## 4. Ceria brand tokens

```
--ceria-blue:      #2E4FA3   (primary, deep blue)
--ceria-pink:      #E91E80   (accent, magenta pink)
--ceria-cream:     #FAF6EE   (light background)
--ceria-cream-deep:#F2E9D9   (card background)
--ceria-dark:      #1F2937   (body text)
--ceria-gray:      #6B7280   (muted text)
--ceria-teal:      #0E9488   (secondary accent, highlights)
```

Logo file is in `content/logo.jpg`. Header font: a warm serif (e.g. "Lora" or
"Georgia"). Body font: clean sans (e.g. "Inter" or system default).

Visual style should match the existing PDF products: soft, warm, calm. NOT
clinical, NOT corporate. This is a family-nurturing product.

---

## 5. Freemium rule (implement as ONE rule everywhere)

There are 12 "chapters"/themes. The four free ones:

1. Parenting Mindset / Pola Pikir Pengasuhan
2. Child Development / Perkembangan Anak
3. Parent Self-Regulation / Regulasi Diri Orang Tua
4. Communication / Komunikasi

**Free tier unlocks:**
- Guidebook chapters 1–4
- Toolkit tools 1–4
- Diary weeks 1–16 (weeks 1–4 map to chapter 1, 5–8 to chapter 2, etc.)

**Paid tier (after `ceria_full_unlock`):**
- Guidebook chapters 5–12
- Toolkit tools 5–12
- Diary weeks 17–52
- Monthly reviews, quarterly check-ins, and year-end review beyond week 16

Implement a single helper: `isUnlocked(chapterNumber, hasPurchased)` →
`chapterNumber <= 4 || hasPurchased`. Every locked item shows a paywall
sheet with a single "Unlock everything" CTA and a "Restore purchases" link.

Content data (see section 7) carries a `chapter` field on every item so the
gate is trivial to apply.

---

## 6. App structure / screens

```
App
├── Onboarding (first launch)
│   ├── Welcome + Ceria mission (proceeds fund free programs)
│   ├── Language pick (EN / ID)
│   └── Edition pick (Combined "Mama & Papa" / Solo)   ← diary mode
├── Home (tab bar)
│   ├── Tab 1: Today        → today's diary prompt + streak
│   ├── Tab 2: Guidebook    → 12 chapters (5–12 locked)
│   ├── Tab 3: Toolkit      → 12 tools (5–12 locked)
│   ├── Tab 4: Diary        → 52 weeks (17–52 locked)
│   └── Tab 5: More         → language, edition, restore purchase,
│                              about Ceria, IG link, unlock
├── Paywall sheet (modal, triggered by any locked item)
└── Settings
```

### Diary interactivity (the app's core value over the PDF)
- Daily entry: three prompts, typed input, autosaved to Capacitor Preferences
- Combined edition: two sub-columns (Mama / Papa) per prompt
- Solo edition: single input per prompt
- Weekly reflection + 5-minute debrief screens
- A simple **streak counter** (consecutive days with at least one entry) —
  gentle, never punishing. No red numbers, no guilt. Missing days is fine.
- **Local reminder notification** (opt-in) at a user-chosen time each evening,
  using `@capacitor/local-notifications`.

### Guidebook & Toolkit
- Guidebook: render each chapter as scrollable formatted text (from JSON).
- Toolkit: render each tool as an interactive-ish page. For v1, tools can be
  read-only descriptions + a "fill on paper or in Diary" note, OR simple
  fillable text fields saved locally. Start read-only; make fillable later.

---

## 7. Content data

All content must live as **structured JSON**, not PDFs. The PDFs were the
print product; the app needs data it can render natively.

This package includes:
- `content/diary_weeks.json`      — all 52 weeks (themes, prompts, reflections), EN+ID
- `content/guidebook.json`        — 12 chapters, EN+ID (STARTER — see note)
- `content/toolkit.json`          — 12 tools, EN+ID (STARTER — see note)
- `content/logo.jpg`              — Ceria logo

**IMPORTANT NOTE ON CONTENT COMPLETENESS:**
The diary JSON is complete (all 52 weeks). The guidebook and toolkit JSON are
STARTERS containing chapters 1–4 fully written plus the structure/titles for
5–12. The full prose for guidebook chapters 5–12 and toolkit tools 5–12 exists
in the founder's original PDF products (`Ceria_Family_Toolkit_Guidebook.pdf`
and the 12 toolkit PDFs). Claude Code should ask the founder to drop those
PDFs into the project, then extract and convert the remaining chapters to
match the JSON schema. Do NOT invent parenting content — extract it from the
founder's existing materials.

---

## 8. Build order (suggested for Claude Code)

1. Scaffold Vite + React + TS + Tailwind + Capacitor
2. Wire brand tokens + fonts + logo
3. Build navigation shell (tab bar, 5 tabs)
4. Load diary JSON, build the Diary browser (weeks list → week detail)
5. Build daily entry + local save (Capacitor Preferences)
6. Build Guidebook + Toolkit readers from JSON
7. Implement the freemium gate (`isUnlocked`) + paywall sheet (mocked purchase first)
8. Integrate RevenueCat, wire real IAP + restore
9. Local notifications (evening reminder) + streak
10. Onboarding flow
11. Add Android + iOS platforms, test in emulator/simulator
12. Founder supplies: store assets, screenshots, developer accounts, signing

Get each step working and visible before moving on. Test in the browser
(`npm run dev`) throughout; only add native platforms once the web app works.

---

## 9. What the founder must provide (not code)

- Apple Developer account (USD 99/year) + Google Play account (USD 25 one-time)
- A Mac (or Mac cloud service) to build and submit the iOS app — REQUIRED,
  no way around this for iOS
- RevenueCat account (free tier)
- App Store product configured (`ceria_full_unlock`, non-consumable)
- Full text for guidebook ch. 5–12 and toolkit tools 5–12 (from existing PDFs)
- App icon + splash (can be derived from logo)
- Privacy policy URL (required by both stores) — even a simple one
- Store listing copy + screenshots

---

## 10. Things to get right (Ceria values)

- **Transparency**: onboarding and paywall both state plainly that proceeds
  fund Ceria's free community programs. This is a yayasan, not a startup.
- **No dark patterns**: no fake urgency, no countdown timers, no "X people
  bought this", no inflated "was IDR 900k now 249k" anchors. The founder has
  been explicit about ethical marketing throughout.
- **Gentle tone**: the streak and reminders must never shame. A missed day is
  normal. The whole diary philosophy is "keep coming back", not "don't break
  the chain".
- **Child safety / privacy**: diary entries are private, stored locally on
  device only (no cloud in v1). Say so clearly. No analytics that read entry
  content.
