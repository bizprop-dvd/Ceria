import type { Edition, Lang, Role } from '../data/types'

export interface Settings {
  onboarded: boolean
  lang: Lang
  edition: Edition
  /** day the family started the diary; drives "current week" on the Today tab */
  startDate: string
  /** evening reminder time, or null if reminders are off */
  reminderTime: { hour: number; minute: number } | null
}

export const DEFAULT_REMINDER = { hour: 20, minute: 0 }

/** Answers for one day: keyed by role. Each role holds one string per prompt. */
export type DailyAnswers = Partial<Record<Role, string[]>>

export interface EntriesState {
  /** daily prompt answers, keyed by local day (YYYY-MM-DD) */
  daily: Record<string, DailyAnswers>
  /** the week's "intent" answer, keyed by week number, per role */
  weekIntent: Record<number, Partial<Record<Role, string>>>
  /** the Sunday reflection answer, keyed by week number, per role */
  sunday: Record<number, Partial<Record<Role, string>>>
  /** the weekly debrief answers, keyed by week number, per role (string[]) */
  debrief: Record<number, Partial<Record<Role, string[]>>>
  /** optional toolkit field answers, keyed by tool number */
  tools: Record<number, string[]>
  /** days of the 365-day guide marked as read, keyed by day number */
  daysRead: Record<number, boolean>
}

export function emptyEntries(): EntriesState {
  return { daily: {}, weekIntent: {}, sunday: {}, debrief: {}, tools: {}, daysRead: {} }
}
