/**
 * A rotating line of parenting advice for the Today screen.
 *
 * Drawn from the reflections and scripts already authored in the 365-day guide,
 * so it is always Ceria's own words rather than generic filler. Only authored
 * days are used, and only chapters the reader has access to — a free reader
 * never sees a line from a paid chapter.
 *
 * The choice is stable for a given day (seeded by the date) so the line does
 * not shuffle every time the screen re-renders, and it walks the whole pool
 * rather than repeating.
 */

import { daily } from '../data/content'
import { isUnlocked } from './freemium'
import type { Bilingual } from '../data/types'

export interface DailyQuote {
  text: Bilingual
  day: number
  chapter: number
}

function hashDate(key: string): number {
  let h = 0
  for (let i = 0; i < key.length; i++) h = (h * 31 + key.charCodeAt(i)) | 0
  return Math.abs(h)
}

/** Pick one line of advice for the given local day key. */
export function quoteForDay(dateKey: string, hasPurchased: boolean): DailyQuote | null {
  const pool: DailyQuote[] = []
  for (const d of daily.days) {
    if (d.draft) continue
    if (!isUnlocked(d.chapter, hasPurchased)) continue
    // Reflections read as advice to sit with; scripts as words to use.
    if (d.reflection?.en) pool.push({ text: d.reflection, day: d.day, chapter: d.chapter })
    if (d.script?.en) pool.push({ text: d.script, day: d.day, chapter: d.chapter })
  }
  if (pool.length === 0) return null
  return pool[hashDate(dateKey) % pool.length]
}
