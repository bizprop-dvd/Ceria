import { dayKey, daysBetween, parseDayKey } from './dates'

/**
 * Gentle streak: the count of consecutive days (ending today, or yesterday if
 * today is still blank) that have at least one diary entry.
 *
 * Design choice for kindness: a blank *today* does not reset the streak — we
 * count back from yesterday — so the number never drops to zero just because
 * it's early in the day. Missing days is fine; this is "keep coming back",
 * not "don't break the chain".
 */
export function computeStreak(daysWithEntries: Set<string>): number {
  const today = new Date()
  const todayKey = dayKey(today)

  // Start from today if it has an entry, otherwise from yesterday.
  let cursor = new Date(today)
  if (!daysWithEntries.has(todayKey)) {
    cursor.setDate(cursor.getDate() - 1)
  }

  let streak = 0
  while (daysWithEntries.has(dayKey(cursor))) {
    streak++
    cursor.setDate(cursor.getDate() - 1)
  }
  return streak
}

/** True if the most recent entry day is today. */
export function hasEntryToday(daysWithEntries: Set<string>): boolean {
  return daysWithEntries.has(dayKey())
}

/** Total distinct days journalled — a gentle, always-growing number. */
export function totalDaysJournalled(daysWithEntries: Set<string>): number {
  return daysWithEntries.size
}

/** Days since the most recent entry (for a soft "welcome back" line). */
export function daysSinceLast(daysWithEntries: Set<string>): number | null {
  if (daysWithEntries.size === 0) return null
  const keys = [...daysWithEntries].sort()
  const last = parseDayKey(keys[keys.length - 1])
  return daysBetween(last, new Date())
}
