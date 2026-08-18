/**
 * Chapter identity as colour.
 *
 * Twelve chapters, twelve hues drawn from one soft palette so the app has
 * twelve visual moods rather than one. Every hue is muted and sits calmly on
 * the cream ground — none of them shout, and none of them fight the Ceria
 * brand blue/pink/teal.
 *
 * Each chapter supplies:
 *   base  — text and accent colour; contrast-checked against cream (#FAF6EE)
 *   tint  — a very light wash for scenario cards and chips
 *   ring  — the dot/ring colour in the year grid
 *
 * Applied as CSS custom properties (--ch-base / --ch-tint / --ch-ring) on a
 * wrapper, because Tailwind cannot see interpolated class names.
 */

export interface ChapterTheme {
  base: string
  tint: string
  ring: string
}

const THEMES: Record<number, ChapterTheme> = {
  //  1 Parenting Mindset — the brand blue, the anchor of the whole guide
  1: { base: '#2E4FA3', tint: '#EAEEF8', ring: '#4A68B5' },
  //  2 Child Development — teal, growth
  2: { base: '#0E7C74', tint: '#E4F2F0', ring: '#2A9A91' },
  //  3 Parent Self-Regulation — sage, steadiness
  3: { base: '#5A7A52', tint: '#EDF2EA', ring: '#7A9970' },
  //  4 Communication — warm amber, voice
  4: { base: '#A8712A', tint: '#F8EFE0', ring: '#C08D45' },
  //  5 Discipline — terracotta, firm and warm
  5: { base: '#A85440', tint: '#F8EAE5', ring: '#C1705A' },
  //  6 Emotional Coaching — rose, feeling
  6: { base: '#A8476B', tint: '#F8E9EF', ring: '#C26385' },
  //  7 Routines & Home Systems — indigo, structure
  7: { base: '#4A4E8C', tint: '#EBECF6', ring: '#666BA5' },
  //  8 Behavior Challenges — plum, the puzzle
  8: { base: '#7A4A82', tint: '#F2E9F4', ring: '#95649C' },
  //  9 Character & Responsibility — olive, slow growth
  9: { base: '#6E7233', tint: '#F1F2E3', ring: '#8C9150' },
  // 10 Relationship & Attachment — coral, warmth
  10: { base: '#B25545', tint: '#FAEAE6', ring: '#CA7061' },
  // 11 Special Contexts — slate, harder weather
  11: { base: '#4F6572', tint: '#EBEFF2', ring: '#6C838F' },
  // 12 Integration — bronze, the year gathered up
  12: { base: '#8A6438', tint: '#F5EDE2', ring: '#A57E52' },
}

const FALLBACK: ChapterTheme = { base: '#2E4FA3', tint: '#EAEEF8', ring: '#4A68B5' }

export function chapterTheme(chapter: number): ChapterTheme {
  return THEMES[chapter] ?? FALLBACK
}

/** Inline style object exposing the chapter theme as CSS custom properties. */
export function chapterVars(chapter: number): React.CSSProperties {
  const t = chapterTheme(chapter)
  return {
    ['--ch-base' as string]: t.base,
    ['--ch-tint' as string]: t.tint,
    ['--ch-ring' as string]: t.ring,
  }
}
