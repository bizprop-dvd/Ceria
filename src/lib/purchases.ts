// RevenueCat in-app purchase wrapper.
//
// On a native device this talks to Apple StoreKit / Google Play Billing via
// RevenueCat. In the browser (`npm run dev`) there is no store, so we fall
// back to a locally-stored MOCK unlock flag — this lets the whole freemium
// flow be built and tested end-to-end before wiring real store credentials.
//
// The one-time unlock is a NON-CONSUMABLE product (`ceria_full_unlock`) that
// grants the `full` entitlement. Restore is implemented (Apple requires it).

import { Capacitor } from '@capacitor/core'
import { ENTITLEMENT_ID, UNLOCK_PRODUCT_ID } from './freemium'
import { getJSON, KEYS, setJSON } from './storage'

export interface PurchaseResult {
  unlocked: boolean
  cancelled?: boolean
  error?: string
  /** true when this ran against the browser mock rather than a real store */
  mock?: boolean
}

export function isNative(): boolean {
  return Capacitor.isNativePlatform()
}

const IOS_KEY = import.meta.env.VITE_REVENUECAT_IOS_KEY as string | undefined
const ANDROID_KEY = import.meta.env.VITE_REVENUECAT_ANDROID_KEY as string | undefined

/**
 * A build with no store keys in it — the test APK passed round before there is
 * a Play account, so the founder and readers can read the whole book on a real
 * phone. It opens every chapter, and the More screen says so plainly.
 *
 * It cannot leak into a release. A release build carries a RevenueCat key, and
 * the presence of a key switches this off no matter what the flag says.
 */
export function isPreviewBuild(): boolean {
  return import.meta.env.VITE_PREVIEW_UNLOCK === 'true' && !IOS_KEY && !ANDROID_KEY
}

let configured = false

/** Configure the RevenueCat SDK once, using the platform's public API key. */
export async function configurePurchases(): Promise<void> {
  if (!isNative() || configured) return
  const platform = Capacitor.getPlatform()
  const apiKey = platform === 'ios' ? IOS_KEY : ANDROID_KEY
  if (!apiKey) {
    console.warn(
      `[purchases] No RevenueCat API key for ${platform}. Set VITE_REVENUECAT_${platform.toUpperCase()}_KEY.`,
    )
    return
  }
  const { Purchases, LOG_LEVEL } = await import('@revenuecat/purchases-capacitor')
  await Purchases.setLogLevel({ level: LOG_LEVEL.ERROR })
  await Purchases.configure({ apiKey })
  configured = true
}

/** Read current entitlement state (does the user own the unlock?). */
export async function checkEntitlement(): Promise<boolean> {
  if (isPreviewBuild()) return true
  if (!isNative()) {
    return getJSON<boolean>(KEYS.purchase, false)
  }
  try {
    await configurePurchases()
    const { Purchases } = await import('@revenuecat/purchases-capacitor')
    const { customerInfo } = await Purchases.getCustomerInfo()
    return Boolean(customerInfo.entitlements.active[ENTITLEMENT_ID])
  } catch (e) {
    console.warn('[purchases] checkEntitlement failed', e)
    return false
  }
}

/** Localized price string for the unlock, or null if unavailable. */
export async function getUnlockPrice(): Promise<string | null> {
  if (!isNative()) return null
  try {
    await configurePurchases()
    const { Purchases } = await import('@revenuecat/purchases-capacitor')
    const offerings = await Purchases.getOfferings()
    const pkg = findUnlockPackage(offerings)
    return pkg?.product?.priceString ?? null
  } catch {
    return null
  }
}

/** Trigger the store purchase flow (or the browser mock). */
export async function purchaseUnlock(): Promise<PurchaseResult> {
  if (!isNative()) {
    await setJSON(KEYS.purchase, true)
    return { unlocked: true, mock: true }
  }
  try {
    await configurePurchases()
    const { Purchases } = await import('@revenuecat/purchases-capacitor')
    const offerings = await Purchases.getOfferings()
    const pkg = findUnlockPackage(offerings)
    if (!pkg) return { unlocked: false, error: 'Product not available' }
    const { customerInfo } = await Purchases.purchasePackage({ aPackage: pkg })
    return { unlocked: Boolean(customerInfo.entitlements.active[ENTITLEMENT_ID]) }
  } catch (e: unknown) {
    const err = e as { code?: string; message?: string }
    // User cancelling the sheet is not an error worth surfacing loudly.
    const { PURCHASES_ERROR_CODE } = await import('@revenuecat/purchases-capacitor')
    if (err.code === PURCHASES_ERROR_CODE.PURCHASE_CANCELLED_ERROR) {
      return { unlocked: false, cancelled: true }
    }
    return { unlocked: false, error: err.message ?? 'Purchase failed' }
  }
}

/** Restore a previous non-consumable purchase (Apple requires this). */
export async function restorePurchases(): Promise<PurchaseResult> {
  if (!isNative()) {
    const unlocked = await getJSON<boolean>(KEYS.purchase, false)
    return { unlocked, mock: true }
  }
  try {
    await configurePurchases()
    const { Purchases } = await import('@revenuecat/purchases-capacitor')
    const { customerInfo } = await Purchases.restorePurchases()
    return { unlocked: Boolean(customerInfo.entitlements.active[ENTITLEMENT_ID]) }
  } catch (e: unknown) {
    const err = e as { message?: string }
    return { unlocked: false, error: err.message ?? 'Restore failed' }
  }
}

/** DEV ONLY: clear the browser mock unlock so the paywall can be re-tested. */
export async function resetMockPurchase(): Promise<void> {
  if (!isNative()) await setJSON(KEYS.purchase, false)
}

// RevenueCat's offering shape is loosely typed here to avoid coupling to the
// plugin's generated types; we just need the package that maps to our product.
function findUnlockPackage(offerings: any): any | null {
  const current = offerings?.current
  const all: any[] = current?.availablePackages ?? []
  const byProduct = all.find((p) => p?.product?.identifier === UNLOCK_PRODUCT_ID)
  return byProduct ?? all[0] ?? null
}
