// Types mirror the founder's content JSON exactly (content/*.json).
// Do not change these without updating the JSON schema.

export type Lang = 'en' | 'id'
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
