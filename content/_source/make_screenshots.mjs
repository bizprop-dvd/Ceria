/**
 * Generate app screenshots from the built preview.
 *
 * Seeds a small amount of plausible sample content first — empty screens read
 * as an unfinished app, and every screen here is one a real parent would have
 * filled in by week three. The sample text is invented, not anyone's diary.
 *
 * Run the preview server first:  npm run preview
 * Then:  node content/_source/make_screenshots.mjs [outDir]
 */

import { chromium } from '/home/user/Ceria/node_modules/playwright-core/index.mjs'
import { mkdirSync } from 'node:fs'

const OUT = process.argv[2] || 'content/_source/out/screenshots'
const BASE = 'http://localhost:4173/'
const CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

// A parent about ten weeks in: some days read, a few entries, a mood, two children.
const SAMPLE = {
  id: {
    daily: {
      one: 'Bagas menumpahkan air di meja. Saya sempat mau marah, tapi tarik napas dulu.',
      two: 'Lega. Ternyata bisa juga tidak membentak.',
      three: 'Besok saya mau lebih banyak mendengar sebelum menegur.',
    },
    intent: 'Minggu ini saya mau lebih tenang di pagi hari.',
    children: ['Bagas', 'Sari'],
    tool: [
      'Jujur, berani mencoba, dan peduli pada orang lain.',
      'Lambat bersiap di pagi hari, dan nada suaranya kalau sedang lelah.',
      'Saya bilang ingin dia berani, tapi yang paling sering saya tegur justru caranya bicara.',
      'Dari "jangan lelet" menjadi "ayo kita siapkan tasmu malam ini".',
    ],
  },
  en: {
    daily: {
      one: 'Bagas spilled water on the table. I nearly snapped, then took a breath first.',
      two: 'Relieved. It turns out I can do this without raising my voice.',
      three: 'Tomorrow I want to listen more before I correct.',
    },
    intent: 'This week I want to be calmer in the mornings.',
    children: ['Bagas', 'Sari'],
    tool: [
      'Honest, willing to try, and thoughtful toward other people.',
      'Being slow in the mornings, and his tone when he is tired.',
      'I say I want him brave, but what I correct most is how he speaks.',
      'From "stop dawdling" to "let us pack your bag tonight".',
    ],
  },
}

function entriesFor(lang) {
  const s = SAMPLE[lang]
  const today = new Date()
  const key = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(
    today.getDate(),
  ).padStart(2, '0')}`
  const daysRead = {}
  for (let d = 1; d <= 44; d++) if (d % 7 !== 0) daysRead[d] = true
  return {
    daily: { [key]: { mama: [s.daily.one, s.daily.two, s.daily.three], papa: ['', '', ''] } },
    weekIntent: { 1: { mama: s.intent }, 7: { mama: s.intent } },
    sunday: {},
    debrief: {},
    tools: { 1: s.tool },
    toolInstances: { '1:1': s.tool },
    children: s.children.map((name, i) => ({ id: i + 1, name })),
    toolPeriodCount: {},
    daysRead,
    weekPhotos: {},
    weekMood: { 7: 'steady', 8: 'close', 9: 'tiring' },
  }
}

// [route, filename, optional text to scroll into view first]
const SHOTS = [
  ['#/', 'today'],
  ['#/guidebook/year', 'year-map'],
  ['#/guidebook/day/7', 'day-framework', { id: 'Empat gaya pengasuhan', en: 'The four parenting styles' }],
  ['#/guidebook/day/12', 'day-reading'],
  ['#/guidebook', 'chapters'],
  ['#/toolkit/1', 'toolkit'],
  ['#/diary/1', 'diary'],
]

const browser = await chromium.launch({ executablePath: CHROME })
const errs = []

for (const lang of ['id', 'en']) {
  const dir = `${OUT}/${lang}`
  mkdirSync(dir, { recursive: true })
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3 })
  const page = await ctx.newPage()
  page.on('pageerror', (e) => errs.push(`${lang}: ${e.message}`))

  await page.goto(BASE, { waitUntil: 'networkidle' })
  await page.evaluate(
    ([l, entries]) => {
      localStorage.setItem(
        'CapacitorStorage.ceria.settings',
        JSON.stringify({
          onboarded: true,
          lang: l,
          edition: 'combined',
          startDate: new Date(Date.now() - 62 * 864e5).toISOString().slice(0, 10),
          reminderTime: { hour: 20, minute: 0 },
        }),
      )
      localStorage.setItem('CapacitorStorage.ceria.entries', JSON.stringify(entries))
    },
    [lang, entriesFor(lang)],
  )

  // The app reads storage once at boot, and navigating to '#/' from '/' is a
  // hash change rather than a load — so reload explicitly or the seed is ignored.
  await page.reload({ waitUntil: 'networkidle' })
  await page.waitForTimeout(600)

  for (const [route, name, anchor] of SHOTS) {
    await page.goto(BASE + route, { waitUntil: 'networkidle' })
    await page.reload({ waitUntil: 'networkidle' })
    await page.waitForTimeout(700)
    if (anchor) {
      const target = page.getByText(anchor[lang], { exact: false }).first()
      if (await target.count()) {
        await target.scrollIntoViewIfNeeded()
        await page.waitForTimeout(400)
      }
    }
    // A mistyped route redirects rather than 404s, and the shot then silently
    // duplicates whatever screen it landed on. Fail loudly instead.
    // '#/' is the app's home and normalises to '#/today'; anything else that
    // moves means the route was wrong.
    const norm = (h) => (h === '#/' || h === '' ? '#/today' : h)
    const landed = norm(new URL(page.url()).hash)
    if (landed !== norm(route)) {
      errs.push(`${lang}/${name}: asked for ${route}, landed on ${landed}`)
    }
    await page.screenshot({ path: `${dir}/${name}.png` })
    process.stdout.write(`  ${lang}/${name}.png\n`)
  }
  await ctx.close()
}

console.log(errs.length ? `ERRORS: ${errs.slice(0, 5).join(' | ')}` : 'no page errors')
await browser.close()
