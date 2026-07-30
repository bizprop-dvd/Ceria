# Ceria Family App

A cross-platform (Android + iOS) mobile app for **Ceria — Yayasan Sukacita
Keluarga Indonesia**. It bundles three of Ceria's parenting products into one
gentle, bilingual companion:

- **Guidebook** — 12-chapter parenting guide
- **Toolkit** — 12 parenting tools / worksheets
- **Diary** — a 52-week dual-track family diary (daily prompts + weekly reflection)

The app is **freemium**: themes 1–4 are free; themes 5–12 unlock with a single
one-time in-app purchase (`ceria_full_unlock`). Content is available in English
and Bahasa Indonesia with a live language toggle. Diary entries are stored
**only on the device** — no cloud, no analytics that read what you write.

> The master specification lives in [`docs/CLAUDE_CODE_BRIEF.md`](docs/CLAUDE_CODE_BRIEF.md).

---

## Tech stack

| Concern    | Choice |
|------------|--------|
| App shell  | Vite + React + TypeScript |
| Native wrap| [Capacitor](https://capacitorjs.com) (one codebase → Android + iOS) |
| IAP        | [RevenueCat](https://www.revenuecat.com) (`@revenuecat/purchases-capacitor`) — wraps Apple StoreKit + Google Play Billing |
| Storage    | Capacitor Preferences (reliable on-device persistence) |
| Reminders  | `@capacitor/local-notifications` |
| Styling    | Tailwind CSS with Ceria brand tokens |
| Routing    | react-router (hash-based, works in the Capacitor webview) |

## Getting started (web)

```bash
npm install
npm run dev        # http://localhost:5173  — the full app runs in the browser
npm run build      # type-check + production build into dist/
```

In the browser the purchase flow is **mocked** (there is no app store), so you
can test the whole freemium experience — paywall, unlock, restore, and the
locked/free gating — end to end. The **More** tab has a "Reset mock purchase"
dev button (browser only) to re-test the paywall.

## Project layout

```
assets/                      App icon + splash sources for @capacitor/assets
  _generate_assets.py        Regenerates them from content/logo.jpg
content/                     Founder content (source of truth — do not invent)
  diary_weeks.json           All 52 weeks, bilingual, complete
  diary_intro.json           Diary front matter (welcome, 5 habits, setup)
  guidebook.json             All 12 chapters, bilingual, complete
  toolkit.json               All 12 tools, bilingual, complete
  logo.jpg
  _source/                   Founder's original scaffold (freemium ref + generator)
docs/CLAUDE_CODE_BRIEF.md    The master spec
public/logo.jpg              Logo served to the app
src/
  data/                      Typed content loaders (types.ts, content.ts)
  lib/                       freemium, storage, purchases, notifications, streak, dates
  store/                     AppContext (settings, entries, purchase state, i18n)
  components/                TabBar, Sheet, PaywallProvider, PromptField, icons, …
  screens/                   Onboarding, Today, Guidebook(+Chapter), Toolkit(+Tool),
                             Diary(+Week), More
capacitor.config.ts
```

## The freemium rule (one rule, everywhere)

```ts
isUnlocked(chapter, hasPurchased)  =>  chapter <= 4 || hasPurchased
```

Defined once in [`src/lib/freemium.ts`](src/lib/freemium.ts) (adapted from the
founder's `content/_source/freemium.reference.ts`). Every content item carries a
`chapter` number; diary weeks map to chapters via `chapterForWeek(week)`
(`ceil(week/4)`, capped at 12). Free tier = chapters 1–4 → Guidebook ch 1–4,
Toolkit tools 1–4, Diary weeks 1–16.

## Content status — complete

All content is extracted from the founder's original PDFs. Nothing is invented.

| Source PDF | Extracted into |
|---|---|
| `Ceria_Family_Toolkit_COMPLETE.pdf` (pp. 8–31) | `guidebook.json` — all 12 chapters |
| `Ceria_Family_Toolkit_COMPLETE.pdf` (pp. 36–47) | `toolkit.json` — all 12 tools |
| `Ceria_Family_Diary_{Combined,Solo}_EN.pdf` | `diary_weeks.json` (52 weeks) + `diary_intro.json` |

- **Guidebook** — every chapter carries principle, "why it matters", "in
  practice", daily practices, reflection, and its reference, in EN + ID.
- **Toolkit** — the print worksheets are adapted for a phone: charts and 7-day
  grids become free-text fields, and reference material (tool 6's feelings word
  bank, tool 10's rules) renders as a `guide` block above the fields.
- **Diary** — the front matter (welcome note, the five habits, "setting up the
  year") is in `diary_intro.json` and shown on the **How this diary works**
  screen, reachable from the ⓘ button on the Diary tab. It is edition-aware:
  Parents and Single parent have their own wording, exactly as in the two PDFs.

Indonesian for the diary front matter is a faithful translation of the founder's
English text (the diary PDFs are English-only); all other content is the
founder's own bilingual copy.

### Language

English and Bahasa Indonesia are **separate, switchable versions** — never shown
side by side. One language renders at a time, chosen with the toggle in
**More → Language**, and the switch applies instantly across every screen. (The
separate **Parents / Single parent** setting is the *diary edition* — Mama &
Papa columns vs. a single column — not a language option. Its stored values
remain `combined` / `solo`, matching the content JSON keys.)

## Building the native apps

Native platform folders (`android/`, `ios/`) are **not** committed — they are
generated. On a machine with the right SDKs:

```bash
# iOS requires macOS + Xcode. Android requires Android Studio / SDK.
cp .env.example .env          # add RevenueCat keys (see below)
npm run build
npx cap add android           # and/or: npx cap add ios   (macOS only)
npx cap sync
npx cap open android          # opens the native IDE to run / archive
```

`capacitor.config.ts` sets `appId: id.or.ceria.app` and `appName: Ceria` — adjust
to Ceria's real bundle identifiers before submitting.

### App icon & splash screen

Source images live in `assets/`, generated from `content/logo.jpg`:

| File | Used for |
|---|---|
| `icon-foreground.png` + `icon-background.png` | Android adaptive icon (star mark on cream) |
| `icon.png` | iOS / single-image icon |
| `splash.png` | Light launch screen (full logo on cream) |
| `splash-dark.png` | Dark launch screen (logo on a cream card over `--ceria-dark`) |

The icon uses the **star mark only** — the "Ceria" wordmark is illegible at
launcher sizes — while the splash uses the full logo.

```bash
npm run assets:source     # regenerate sources from logo.jpg (needs Pillow)
npm run assets:generate   # fan out into android/ and ios/ (run after `cap add`)
```

### RevenueCat / in-app purchase setup

1. Create a RevenueCat project; add the iOS and Android apps.
2. In App Store Connect / Play Console, create a **non-consumable** product with
   ID `ceria_full_unlock`.
3. In RevenueCat, create an entitlement named **`full`** and attach the product,
   then add it to the default **Offering**.
4. Put the **public** SDK keys in `.env` (`VITE_REVENUECAT_IOS_KEY`,
   `VITE_REVENUECAT_ANDROID_KEY`).

The app checks the `full` entitlement on launch, offers "Unlock everything", and
implements **Restore purchases** (required by Apple). See `src/lib/purchases.ts`.

## Ceria values baked in

- **Transparency** — onboarding and the paywall both state plainly that proceeds
  fund Ceria's free community programs.
- **No dark patterns** — no countdowns, fake urgency, or inflated anchor prices.
- **Gentle streak** — a blank *today* never resets the streak; missing days is
  fine ("keep coming back", not "don't break the chain").
- **Privacy** — entries live only on the device.

## Founder to-do (not code)

- Apple Developer account ($99/yr) + Google Play account ($25 once) + a Mac for iOS
- RevenueCat account and the product/entitlement setup above
- Privacy policy URL, store listing copy + screenshots
- Real links in [`src/config.ts`](src/config.ts) (Instagram, website, privacy, support)
- Consider Apple's Small Business Program (commission 30% → 15%)

Optional polish: the toolkit's 7-day charts and 1–5 rating scales are currently
free-text fields. They could become real checkbox grids and sliders in a later
pass — the JSON schema already supports adding new field `type`s.
