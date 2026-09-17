// Local-date helpers. All diary keys use the device's local calendar day,
// never UTC, so "today" matches what the parent sees on their clock.

import type { Lang } from '../data/types'

export function dayKey(d = new Date()): string {
  const y = d.getFullYear()
  const m = String(d.getMonth() + 1).padStart(2, '0')
  const day = String(d.getDate()).padStart(2, '0')
  return `${y}-${m}-${day}`
}

export function parseDayKey(key: string): Date {
  const [y, m, d] = key.split('-').map(Number)
  return new Date(y, m - 1, d)
}

/** Whole days between two local dates (b - a), ignoring time of day. */
export function daysBetween(a: Date, b: Date): number {
  const da = new Date(a.getFullYear(), a.getMonth(), a.getDate())
  const db = new Date(b.getFullYear(), b.getMonth(), b.getDate())
  return Math.round((db.getTime() - da.getTime()) / 86400000)
}

/** Which diary week (1..52) corresponds to today, given a start date. */
export function currentWeek(startDateKey: string, totalWeeks: number): number {
  const start = parseDayKey(startDateKey)
  const diff = daysBetween(start, new Date())
  const wk = Math.floor(diff / 7) + 1
  return Math.min(Math.max(wk, 1), totalWeeks)
}

// Written out rather than left to Intl: a cheap Android build can ship a
// WebView with a trimmed locale database, and a date that silently falls back
// to English months in the Indonesian app would look like a bug.
const MONTHS: Record<Lang, string[]> = {
  en: [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December',
  ],
  id: [
    'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
    'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember',
  ],
}

/** "2026-09-28" -> "28 September 2026". Returns the key itself if it is malformed. */
export function formatDay(key: string, lang: Lang): string {
  const [y, m, d] = key.split('-').map(Number)
  const month = MONTHS[lang][m - 1]
  if (!y || !month || !d) return key
  return `${d} ${month} ${y}`
}
