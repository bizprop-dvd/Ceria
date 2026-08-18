// Types mirror the founder's content JSON exactly (content/*.json).
// Do not change these without updating the JSON schema.

export type Lang = 'en' | 'id'
/**
 * Diary edition. The stored keys stay 'combined' / 'solo' because the content
 * JSON is keyed that way; the UI labels them "Parents" and "Single parent".
 */
export type Edition = 'combined' | 'solo'
export type Role = 'solo' | 'mama' | 'papa'

export interface Bilingual {
  en: string
  id: string
}

export interface BilingualList {
  en: string[]
  id: string[]
}

/* ---------- Diary ---------- */

export interface DiaryChapterRef {
  number: number
  en: string
  id: string
}

export interface DiaryMeta {
  product: 'diary'
  freeThroughChapter: number
  dailyPrompts: Bilingual[]
  debrief: {
    combined: Bilingual[]
    solo: Bilingual[]
  }
}

export interface DiaryWeek {
  week: number
  chapter: number
  locked: boolean
  theme: Bilingual
  principle: Bilingual
  weekIntent: Bilingual
  sundayReflection: {
    combined: Bilingual
    solo: Bilingual
  }
}

export interface DiaryData {
  meta: DiaryMeta
  chapters: DiaryChapterRef[]
  weeks: DiaryWeek[]
}

/* ---------- Guidebook ---------- */

export interface GuidebookChapter {
  number: number
  locked: boolean
  title: Bilingual
  principle: Bilingual
  why?: Bilingual
  inPractice?: Bilingual
  dailyPractices?: BilingualList
  reflection?: Bilingual
  toolRef?: number
  reference?: string
  /** true when full prose still must be extracted from the founder's PDF */
  _needsProse?: boolean
}

export interface GuidebookData {
  meta: { product: 'guidebook'; freeThroughChapter: number; note: string }
  chapters: GuidebookChapter[]
}

/* ---------- Toolkit ---------- */

export interface ToolkitField {
  type: 'text' | 'longtext'
  label: Bilingual
}

export interface ToolkitTool {
  number: number
  locked: boolean
  chapter: number
  title: Bilingual
  purpose: Bilingual
  /** optional reference/helper lines shown above the fields (word banks, rules, examples) */
  guide?: BilingualList
  /**
   * Tools meant to be filled more than once.
   *  - 'month': a fixed set of instances, one per month of the year
   *  - 'child': instances the parent adds themselves, each named
   */
  repeat?:
    | { kind: 'month'; count: number }
    | { kind: 'weekday' }
    | { kind: 'period'; partsPerYear: number }
    | { kind: 'child'; nameLabel: Bilingual }
  /** fields asked once for the whole tool, not per instance (e.g. a weekly summary) */
  summaryFields?: ToolkitField[]
  fields?: ToolkitField[]
  /** true when the field layout still must be extracted from the founder's PDF */
  _needsFields?: boolean
}

export interface ToolkitData {
  meta: {
    product: 'toolkit'
    freeThroughChapter: number
    note: string
    transparencyLine: Bilingual
  }
  tools: ToolkitTool[]
}

/* ---------- 365-day companion guide ---------- */

export interface FrameworkEntry {
  name: Bilingual
  tags: Bilingual[]
  looksLike: Bilingual
  outcome: Bilingual
}

/** A small comparison grid rendered as cards (e.g. the four parenting styles). */
export interface Framework {
  title: Bilingual
  note: Bilingual
  entries: FrameworkEntry[]
}

export interface DailyDay {
  day: number
  chapter: number
  title: Bilingual
  teaching: Bilingual
  inPractice: Bilingual
  practice: Bilingual
  reflection: Bilingual
  script: Bilingual
  support: Bilingual
  reference: string
  framework?: Framework
  /** true while the day's prose has not been authored yet — hidden in the app */
  draft: boolean
}

/**
 * What is known about a day without loading its chapter.
 *
 * Enough to list the day, link to it, and rotate its line of advice on the
 * Today screen. The teaching itself arrives only when the day is opened.
 */
export type DailySummary = Pick<
  DailyDay,
  'day' | 'chapter' | 'title' | 'draft' | 'reflection' | 'script'
>

export interface DailyRangeItem {
  n: number
  range: [number, number]
  text: Bilingual
}

export interface DailyMeta {
  product: 'daily'
  version: number
  totalDays: number
  freeThroughChapter: number
  authoredDays: number
  note: string
}

export interface DailyChapterRange {
  number: number
  dayStart: number
  dayEnd: number
  dayCount: number
}

/** content/daily/index.json — everything the app needs before a day is opened. */
export interface DailyIndexData {
  meta: DailyMeta
  chapters: DailyChapterRange[]
  days: DailySummary[]
  weeklyExercises: DailyRangeItem[]
  monthlyReviews: DailyRangeItem[]
}

/** content/daily/chNN.json — one chapter's full text, loaded on demand. */
export interface DailyChapterData {
  days: DailyDay[]
}

/** The whole guide in one object. Only the content pipeline still reads this. */
export interface DailyData extends Omit<DailyIndexData, 'days'> {
  days: DailyDay[]
}

/* ---------- Diary front-matter ("how this diary works") ---------- */

export interface DiaryHabit {
  title: Bilingual
  body: Bilingual
}

export interface DiaryIntroData {
  welcome: Record<Edition, Bilingual>
  howToUse: Record<Edition, DiaryHabit[]>
  settingUp: {
    intro: Bilingual
    combined: { prompts: Bilingual[] }
    solo: { prompts: Bilingual[] }
  }
}
