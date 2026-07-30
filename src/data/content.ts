// Loads the founder's content JSON as typed, immutable data.
// JSON lives at the repo root under content/ (see tsconfig "include").

import diaryJson from '../../content/diary_weeks.json'
import guidebookJson from '../../content/guidebook.json'
import toolkitJson from '../../content/toolkit.json'
import type { DiaryData, GuidebookData, ToolkitData } from './types'

export const diary = diaryJson as DiaryData
export const guidebook = guidebookJson as GuidebookData
export const toolkit = toolkitJson as ToolkitData

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
