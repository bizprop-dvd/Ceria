/**
 * Ceria freemium gate — the single source of truth for what's free vs paid.
 * Adapted from the founder's scaffold/freemium.ts.
 *
 * RULE: Chapters 1-4 are free. Everything else requires the one-time
 * `ceria_full_unlock` purchase.
 */

import type { Bilingual } from '../data/types'

export const FREE_THROUGH_CHAPTER = 4
export const UNLOCK_PRODUCT_ID = 'ceria_full_unlock'
/** RevenueCat entitlement identifier that the product grants. */
export const ENTITLEMENT_ID = 'full'

/** Diary: weeks 1-4 => ch1, 5-8 => ch2, ... capped at 12. */
export function chapterForWeek(week: number): number {
  return Math.min(12, Math.ceil(week / 4))
}

/** The core gate. Use this everywhere. */
export function isUnlocked(chapter: number, hasPurchased: boolean): boolean {
  return chapter <= FREE_THROUGH_CHAPTER || hasPurchased
}

/** Convenience for diary weeks. */
export function isWeekUnlocked(week: number, hasPurchased: boolean): boolean {
  return isUnlocked(chapterForWeek(week), hasPurchased)
}

/**
 * Paywall copy (bilingual). Kept honest — no fake urgency, no countdowns,
 * no inflated anchor prices. States plainly that proceeds fund free programs.
 */
export const paywallCopy: Record<'en' | 'id', {
  title: string
  body: string
  cta: string
  restore: string
  transparency: string
  maybeLater: string
  purchasing: string
  restoring: string
  restoredNothing: string
  purchaseFailed: string
  priceFallback: string
}> = {
  en: {
    title: 'Unlock the full journey',
    body: 'Chapters 1–4 are yours for free. Unlock all 12 chapters — the complete guidebook, all 12 tools, and the full 52-week diary — with a single one-time purchase.',
    cta: 'Unlock everything',
    restore: 'Restore purchase',
    transparency:
      'Ceria is a nonprofit foundation. Your purchase helps fund free parenting and marriage programs for families who cannot pay.',
    maybeLater: 'Maybe later',
    purchasing: 'Opening checkout…',
    restoring: 'Restoring…',
    restoredNothing: 'No previous purchase was found on this account.',
    purchaseFailed: 'The purchase did not complete. You have not been charged.',
    priceFallback: 'One-time purchase',
  },
  id: {
    title: 'Buka seluruh perjalanan',
    body: 'Bab 1–4 gratis untuk Anda. Buka seluruh 12 bab — panduan lengkap, 12 alat, dan diari penuh 52 minggu — dengan satu kali pembelian.',
    cta: 'Buka semuanya',
    restore: 'Pulihkan pembelian',
    transparency:
      'Ceria adalah yayasan nirlaba. Pembelian Anda membantu mendanai program pengasuhan dan pernikahan gratis bagi keluarga yang tidak mampu.',
    maybeLater: 'Nanti saja',
    purchasing: 'Membuka pembayaran…',
    restoring: 'Memulihkan…',
    restoredNothing: 'Tidak ada pembelian sebelumnya pada akun ini.',
    purchaseFailed: 'Pembelian tidak selesai. Anda tidak dikenai biaya.',
    priceFallback: 'Pembelian satu kali',
  },
}

export function pick(b: Bilingual, lang: 'en' | 'id'): string {
  return b[lang]
}
