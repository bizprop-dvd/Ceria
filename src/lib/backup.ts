import { Capacitor } from '@capacitor/core'
import type { EntriesState, Settings } from '../store/types'
import { emptyEntries } from '../store/types'

/**
 * One backup file holds everything a parent has written: diary answers,
 * toolkit sheets, week photos, which days they have read, and their settings.
 *
 * The file is the parent's own. Nothing here is uploaded anywhere except the
 * destination they choose, and Ceria never holds a copy.
 */

export const BACKUP_VERSION = 1

export interface BackupPayload {
  app: 'ceria'
  version: number
  /** when this backup was written, ISO 8601 */
  savedAt: string
  /** which device wrote it, so a restore can say where it came from */
  device: string
  settings: Settings
  entries: EntriesState
}

export function buildBackup(settings: Settings, entries: EntriesState, device: string): BackupPayload {
  return {
    app: 'ceria',
    version: BACKUP_VERSION,
    savedAt: new Date().toISOString(),
    device,
    settings,
    entries,
  }
}

export function serializeBackup(payload: BackupPayload): string {
  return JSON.stringify(payload, null, 2)
}

export interface ParsedBackup {
  ok: true
  payload: BackupPayload
  summary: BackupSummary
}
export interface ParseError {
  ok: false
  /** 'notCeria' | 'newerVersion' | 'unreadable' — the UI maps these to bilingual copy */
  reason: 'notCeria' | 'newerVersion' | 'unreadable'
}

export interface BackupSummary {
  savedAt: string
  device: string
  /** number of days with at least one diary answer */
  days: number
  /** number of guide days marked read */
  daysRead: number
  photos: number
  children: number
}

/**
 * Parse a file the parent picked. Restoring replaces what is on this device,
 * so this refuses anything it cannot fully understand rather than importing
 * half of it.
 */
export function parseBackup(text: string): ParsedBackup | ParseError {
  let raw: unknown
  try {
    raw = JSON.parse(text)
  } catch {
    return { ok: false, reason: 'unreadable' }
  }
  if (typeof raw !== 'object' || raw === null) return { ok: false, reason: 'unreadable' }
  const p = raw as Partial<BackupPayload>
  if (p.app !== 'ceria' || !p.entries || !p.settings) return { ok: false, reason: 'notCeria' }
  if (typeof p.version !== 'number') return { ok: false, reason: 'notCeria' }
  // A file from a future version may use fields this build would silently drop.
  if (p.version > BACKUP_VERSION) return { ok: false, reason: 'newerVersion' }

  const entries = { ...emptyEntries(), ...p.entries }
  const payload: BackupPayload = {
    app: 'ceria',
    version: p.version,
    savedAt: typeof p.savedAt === 'string' ? p.savedAt : new Date().toISOString(),
    device: typeof p.device === 'string' ? p.device : '—',
    settings: p.settings,
    entries,
  }
  return { ok: true, payload, summary: summarize(payload) }
}

export function summarize(payload: BackupPayload): BackupSummary {
  const e = payload.entries
  const written = Object.values(e.daily ?? {}).filter((day) =>
    Object.values(day ?? {}).some((answers) => (answers ?? []).some((a) => (a ?? '').trim() !== '')),
  ).length
  return {
    savedAt: payload.savedAt,
    device: payload.device,
    days: written,
    daysRead: Object.keys(e.daysRead ?? {}).length,
    photos: Object.keys(e.weekPhotos ?? {}).length,
    children: (e.children ?? []).length,
  }
}

/** A short, human name for this device, used only inside the backup file. */
export function deviceName(): string {
  const platform = Capacitor.getPlatform()
  if (platform === 'ios') return 'iPhone / iPad'
  if (platform === 'android') return 'Android'
  return 'Browser'
}

export function backupFileName(): string {
  const d = new Date()
  const stamp = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(
    d.getDate(),
  ).padStart(2, '0')}`
  return `ceria-cadangan-${stamp}.json`
}

/** The one file Ceria keeps in the parent's Drive; a fixed name so it is overwritten, not multiplied. */
export const DRIVE_FILE_NAME = 'ceria-cadangan.json'
