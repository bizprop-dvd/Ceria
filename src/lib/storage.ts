// Thin wrapper over Capacitor Preferences. Preferences has a web
// implementation (backed by localStorage), so this works in `npm run dev`
// and persists reliably on device.

import { Preferences } from '@capacitor/preferences'

export async function getJSON<T>(key: string, fallback: T): Promise<T> {
  try {
    const { value } = await Preferences.get({ key })
    if (value == null) return fallback
    return JSON.parse(value) as T
  } catch {
    return fallback
  }
}

export async function setJSON(key: string, value: unknown): Promise<void> {
  try {
    await Preferences.set({ key, value: JSON.stringify(value) })
  } catch {
    // Best-effort. Never let a storage error crash the UI.
  }
}

export const KEYS = {
  settings: 'ceria.settings',
  entries: 'ceria.entries',
  purchase: 'ceria.purchase.mock',
} as const
