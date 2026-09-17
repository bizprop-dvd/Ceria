// Loads the founder's content JSON as typed, immutable data.
// JSON lives at the repo root under content/ (see tsconfig "include").
//
// The 365-day guide is the one exception to loading everything up front. It is
// nearly a megabyte of prose, and a parent opening the app needs a handful of
// titles and one line of advice from it — not all of it. So it is split into a
// small index that ships with the app and twelve chapter files that load when
// someone actually opens a day. See content/_source/split_daily.py.

import diaryJson from '../../content/diary_weeks.json'
import diaryIntroJson from '../../content/diary_intro.json'
import guidebookJson from '../../content/guidebook.json'
import toolkitJson from '../../content/toolkit.json'
import dailyIndexJson from '../../content/daily/index.json'
import type {
  DailyChapterData,
  DailyDay,
  DailyIndexData,
  DailySummary,
  DiaryData,
  DiaryIntroData,
  GuidebookData,
  ToolkitData,
} from './types'

export const diary = diaryJson as DiaryData
export const diaryIntro = diaryIntroJson as unknown as DiaryIntroData
export const guidebook = guidebookJson as GuidebookData
export const toolkit = toolkitJson as ToolkitData
export const daily = dailyIndexJson as unknown as DailyIndexData

/** Authored days only — drafts are never shown. */
export function daysForChapter(chapter: number): DailySummary[] {
  return daily.days.filter((d) => d.chapter === chapter && !d.draft)
}

export function dayByNumber(day: number): DailySummary | undefined {
  const d = daily.days.find((x) => x.day === day)
  return d && !d.draft ? d : undefined
}

/* ---------- the day's full text, fetched a chapter at a time ---------- */

// Vite turns this into one lazily-loaded chunk per chapter file. The glob is
// resolved at build time, so a missing chapter is a missing key, not a 404.
const chapterFiles = import.meta.glob<{ default: DailyChapterData }>(
  '../../content/daily/ch*.json',
)

const loaded = new Map<number, DailyDay[]>()
const inFlight = new Map<number, Promise<DailyDay[]>>()

function pathFor(chapter: number) {
  return `../../content/daily/ch${String(chapter).padStart(2, '0')}.json`
}

/** A chapter already read this session, if any — lets a revisit render at once. */
export function chapterDaysIfLoaded(chapter: number): DailyDay[] | undefined {
  return loaded.get(chapter)
}

/** The full text of one chapter's days. Cached, and never fetched twice at once. */
export function loadChapterDays(chapter: number): Promise<DailyDay[]> {
  const already = loaded.get(chapter)
  if (already) return Promise.resolve(already)

  const pending = inFlight.get(chapter)
  if (pending) return pending

  const load = chapterFiles[pathFor(chapter)]
  if (!load) return Promise.resolve([])

  const promise = load()
    .then((mod) => {
      const days = mod.default.days
      loaded.set(chapter, days)
      return days
    })
    .finally(() => inFlight.delete(chapter))

  inFlight.set(chapter, promise)
  return promise
}

/** The full text of one day. */
export async function loadDay(day: number): Promise<DailyDay | undefined> {
  const summary = dayByNumber(day)
  if (!summary) return undefined
  const days = await loadChapterDays(summary.chapter)
  return days.find((d) => d.day === day)
}

/* ---------- the rest of the content ---------- */

export const CHAPTERS = diary.chapters
export const TOTAL_WEEKS = diary.weeks.length

export function weekByNumber(week: number) {
  return diary.weeks.find((w) => w.week === week)
}

export function chapterByNumber(n: number) {
  return guidebook.chapters.find((c) => c.number === n)
}

export function toolByNumber(n: number) {
  return toolkit.tools.find((t) => t.number === n)
}

export function chapterName(n: number) {
  return CHAPTERS.find((c) => c.number === n)
}
