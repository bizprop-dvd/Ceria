# Ceria Family App — Handoff Package

This folder is a **starter package to hand to Claude Code** to build the Ceria
family app (Android + iOS). It contains the spec, the freemium logic, and the
content data already converted to JSON.

## What's inside

```
ceria_app/
├── README.md                     ← you are here
├── docs/
│   └── CLAUDE_CODE_BRIEF.md       ← THE MASTER SPEC. Read this first.
├── content/
│   ├── diary_weeks.json           ← all 52 weeks, bilingual, complete
│   ├── guidebook.json             ← ch 1–4 full; 5–12 need prose (from PDF)
│   ├── toolkit.json               ← tools 1–4 full; 5–12 need fields (from PDF)
│   └── logo.jpg                   ← Ceria logo
└── scaffold/
    ├── freemium.ts                ← drop-in freemium gate (the one rule)
    └── gen_diary_json.py          ← regenerates diary_weeks.json if needed
```

## How to use this (founder steps)

1. **Open Claude Code** in an empty project folder.
2. Copy this entire `ceria_app/` folder into that project.
3. Tell Claude Code: *"Read docs/CLAUDE_CODE_BRIEF.md and build the app it
   describes. Start by scaffolding Vite + React + TS + Tailwind + Capacitor,
   then build the navigation shell and the Diary from content/diary_weeks.json."*
4. Work through the build order in the brief, testing in the browser as you go.
5. When Claude Code asks for the full prose of guidebook chapters 5–12 and
   toolkit tools 5–12, drop your existing PDFs into the project so it can
   extract them. **Do not let it invent parenting content.**

## The freemium rule (in one sentence)

Chapters 1–4 are free; chapters 5–12 unlock with a single one-time purchase
(`ceria_full_unlock`). See `scaffold/freemium.ts` — it's ready to drop in.

## Critical constraint (read before pricing anything)

Because this ships on the App Store and Play Store, **you must use Apple/Google
in-app purchase** (via RevenueCat) to unlock content — not Midtrans or Xendit.
Apple/Google take 15–30%. Enroll in Apple's Small Business Program to drop to
15%. This is explained in the brief.

## What you'll need to provide later

- Apple Developer account ($99/yr) + Google Play account ($25 one-time)
- A Mac (or Mac cloud) to build/submit iOS — unavoidable
- RevenueCat account (free tier)
- Full prose for guidebook ch 5–12 + toolkit tools 5–12 (from your PDFs)
- App icon + splash, privacy policy URL, store screenshots + listing copy

## A note from the build so far

The diary content (all 52 weeks, both languages, both editions' Sunday
questions) is complete and verified in `diary_weeks.json`. The guidebook and
toolkit have their first 4 chapters fully written — enough to build and test
the entire free tier and the paywall — with the remaining chapters stubbed so
Claude Code knows exactly what to extract from your existing PDF products.
