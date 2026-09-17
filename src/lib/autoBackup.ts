import { buildBackup, deviceName, parseBackup, serializeBackup } from './backup'
import { uploadBackup } from './googleDrive'
import { isSignedIn } from './googleAuth'
import type { EntriesState, Settings } from '../store/types'

/**
 * Decides when a Drive backup should happen, and makes sure only one runs at a
 * time.
 *
 * 'live' does not upload on every keystroke — a parent writing a paragraph
 * would otherwise fire dozens of uploads and flatten their battery and data
 * allowance. It waits for a pause in the writing, then sends once.
 */

/** Quiet period after the last change before a 'live' backup goes up. */
export const LIVE_DEBOUNCE_MS = 20_000

export type BackupOutcome =
  | { status: 'done'; at: string }
  | { status: 'skipped' }
  | { status: 'failed'; error: string }

let inFlight: Promise<BackupOutcome> | null = null

/**
 * Upload now. Concurrent callers share one upload rather than racing, which
 * also stops a 'live' trigger and the daily trigger from both writing at once
 * and leaving whichever finished last in the file.
 */
export function runBackup(settings: Settings, entries: EntriesState): Promise<BackupOutcome> {
  if (inFlight) return inFlight
  inFlight = (async (): Promise<BackupOutcome> => {
    try {
      if (!(await isSignedIn())) return { status: 'skipped' }
      const payload = buildBackup(settings, entries, deviceName())
      const text = serializeBackup(payload)
      // Cheap guard against uploading something we could not read back.
      const check = parseBackup(text)
      if (!check.ok) return { status: 'failed', error: 'could not build a valid backup' }
      await uploadBackup(text)
      return { status: 'done', at: payload.savedAt }
    } catch (e) {
      const err = e as { message?: string }
      return { status: 'failed', error: err.message ?? 'backup failed' }
    } finally {
      inFlight = null
    }
  })()
  return inFlight
}

/** True when a daily backup is owed: none yet, or the last one was on an earlier day. */
export function dailyBackupDue(lastBackupAt: string | null, now = new Date()): boolean {
  if (!lastBackupAt) return true
  const last = new Date(lastBackupAt)
  if (Number.isNaN(last.getTime())) return true
  return (
    last.getFullYear() !== now.getFullYear() ||
    last.getMonth() !== now.getMonth() ||
    last.getDate() !== now.getDate()
  )
}
