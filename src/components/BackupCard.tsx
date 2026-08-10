import { useEffect, useState } from 'react'
import Segmented from './Segmented'
import { useApp } from '../store/AppContext'
import { buildBackup, deviceName, parseBackup, serializeBackup, type BackupSummary } from '../lib/backup'
import { exportToFile, importFromFile } from '../lib/backupFile'
import { downloadBackup } from '../lib/googleDrive'
import * as google from '../lib/googleAuth'
import type { BackupMode } from '../store/types'

/**
 * Backup settings.
 *
 * Two independent things live here and the copy keeps them apart:
 *   - a plain file the parent saves themselves, which always works
 *   - an optional connection to their own Google Drive, which adds automatic
 *     backups and lets the diary move to another phone
 *
 * Ceria never holds a copy either way. The Drive half only appears in a build
 * that has Google credentials, so it cannot show a dead button.
 */
/** Indonesian does not mark plurals, so only the English side varies. */
function plural(n: number, en: boolean, one: string, many: string, id: string): string {
  if (!en) return id
  return n === 1 ? one : many
}

export default function BackupCard() {
  const { lang, settings, entries, updateSettings, backupNow, applyBackup } = useApp()
  const [busy, setBusy] = useState<null | 'save' | 'open' | 'connect' | 'now' | 'fromDrive'>(null)
  const [msg, setMsg] = useState<string | null>(null)
  const [email, setEmail] = useState<string | null>(null)
  const [pending, setPending] = useState<{ summary: BackupSummary; apply: () => void } | null>(null)

  const en = lang === 'en'
  const driveAvailable = google.isConfigured()

  useEffect(() => {
    void google.currentEmail().then(setEmail)
  }, [])

  const say = (e: string, i: string) => setMsg(en ? e : i)

  /* ---------- the plain file ---------- */

  const onSave = async () => {
    setBusy('save')
    setMsg(null)
    try {
      const text = serializeBackup(buildBackup(settings, entries, deviceName()))
      const shared = await exportToFile(text)
      if (shared) say('Backup saved.', 'Cadangan tersimpan.')
    } catch {
      say('Could not save the backup.', 'Cadangan tidak dapat disimpan.')
    } finally {
      setBusy(null)
    }
  }

  const onOpen = async () => {
    setBusy('open')
    setMsg(null)
    try {
      const text = await importFromFile()
      if (text === null) return
      offer(text)
    } finally {
      setBusy(null)
    }
  }

  /** Show what is in the file and ask before replacing anything. */
  const offer = (text: string) => {
    const parsed = parseBackup(text)
    if (!parsed.ok) {
      if (parsed.reason === 'newerVersion') {
        say(
          'This backup was made by a newer version of Ceria. Please update the app first.',
          'Cadangan ini dibuat oleh Ceria versi yang lebih baru. Perbarui aplikasi terlebih dahulu.',
        )
      } else {
        say('That file is not a Ceria backup.', 'Berkas itu bukan cadangan Ceria.')
      }
      return
    }
    setPending({ summary: parsed.summary, apply: () => applyBackup(parsed.payload) })
  }

  const confirmRestore = () => {
    pending?.apply()
    setPending(null)
    say('Restored.', 'Berhasil dipulihkan.')
  }

  /* ---------- Drive ---------- */

  const onConnect = async () => {
    setBusy('connect')
    setMsg(null)
    try {
      const session = await google.signIn()
      setEmail(session.email)
      say('Google Drive connected.', 'Google Drive terhubung.')
    } catch (e) {
      const err = e as { message?: string }
      if (err.message !== 'cancelled') {
        say('Could not connect to Google Drive.', 'Tidak dapat terhubung ke Google Drive.')
      }
    } finally {
      setBusy(null)
    }
  }

  const onDisconnect = async () => {
    await google.signOut()
    setEmail(null)
    updateSettings({ backupMode: 'off' })
    say(
      'Disconnected. The backup already in your Drive is still yours to keep or delete.',
      'Terputus. Cadangan yang sudah ada di Drive Anda tetap milik Anda, boleh disimpan atau dihapus.',
    )
  }

  const onBackupNow = async () => {
    setBusy('now')
    setMsg(null)
    const res = await backupNow()
    if (res.status === 'done') say('Backed up to Drive.', 'Tercadangkan ke Drive.')
    else if (res.status === 'skipped') say('Connect Google Drive first.', 'Hubungkan Google Drive dulu.')
    else say('Backup failed. Please try again.', 'Pencadangan gagal. Silakan coba lagi.')
    setBusy(null)
  }

  const onRestoreFromDrive = async () => {
    setBusy('fromDrive')
    setMsg(null)
    try {
      const text = await downloadBackup()
      if (text === null) {
        say('No backup found in your Drive yet.', 'Belum ada cadangan di Drive Anda.')
        return
      }
      offer(text)
    } catch {
      say('Could not read the backup from Drive.', 'Tidak dapat membaca cadangan dari Drive.')
    } finally {
      setBusy(null)
    }
  }

  /* ---------- render ---------- */

  const modes: { value: BackupMode; label: string }[] = [
    { value: 'off', label: en ? 'Off' : 'Mati' },
    { value: 'daily', label: en ? 'Daily' : 'Harian' },
    { value: 'live', label: en ? 'Always' : 'Selalu' },
  ]

  const modeNote: Record<BackupMode, string> = {
    off: en
      ? 'Nothing is uploaded. You can still save a backup file yourself.'
      : 'Tidak ada yang diunggah. Anda tetap dapat menyimpan berkas cadangan sendiri.',
    daily: en
      ? 'Once a day, the first time you open Ceria.'
      : 'Sekali sehari, saat pertama kali Anda membuka Ceria.',
    live: en
      ? 'Shortly after you finish writing, each time.'
      : 'Sesaat setelah Anda selesai menulis, setiap kali.',
  }

  return (
    <div className="card p-4">
      <p className="font-head text-[15px] font-semibold text-ceria-dark">
        {en ? 'Backup' : 'Cadangan'}
      </p>
      <p className="mt-0.5 text-xs text-ceria-gray">
        {en
          ? 'Your writing lives on this phone. A backup means a lost or replaced phone does not mean a lost year.'
          : 'Tulisan Anda tersimpan di ponsel ini. Cadangan berarti ponsel yang hilang atau berganti tidak membuat satu tahun catatan ikut hilang.'}
      </p>

      {/* Always available: the plain file */}
      <div className="mt-3 flex gap-2">
        <button onClick={onSave} disabled={busy !== null} className="btn-ghost flex-1 text-ceria-blue">
          {busy === 'save' ? (en ? 'Saving…' : 'Menyimpan…') : en ? 'Save a backup' : 'Simpan cadangan'}
        </button>
        <button onClick={onOpen} disabled={busy !== null} className="btn-ghost flex-1 text-ceria-blue">
          {busy === 'open' ? (en ? 'Opening…' : 'Membuka…') : en ? 'Open a backup' : 'Buka cadangan'}
        </button>
      </div>

      {/* Optional: their own Drive */}
      {driveAvailable && (
        <div className="mt-4 border-t border-ceria-cream-deep pt-4">
          {email ? (
            <>
              <div className="flex items-start justify-between gap-3">
                <div className="min-w-0">
                  <p className="text-[13px] font-semibold text-ceria-dark">
                    {en ? 'Google Drive connected' : 'Google Drive terhubung'}
                  </p>
                  <p className="truncate text-xs text-ceria-gray">{email}</p>
                </div>
                <button onClick={onDisconnect} className="shrink-0 text-xs text-ceria-gray underline">
                  {en ? 'Disconnect' : 'Putuskan'}
                </button>
              </div>

              <p className="mt-3 mb-1.5 text-xs font-semibold uppercase tracking-wide text-ceria-teal">
                {en ? 'Automatic backup' : 'Cadangan otomatis'}
              </p>
              <Segmented<BackupMode>
                value={settings.backupMode}
                onChange={(m) => updateSettings({ backupMode: m })}
                options={modes}
              />
              <p className="mt-1.5 text-xs text-ceria-gray">{modeNote[settings.backupMode]}</p>

              <div className="mt-3 flex gap-2">
                <button
                  onClick={onBackupNow}
                  disabled={busy !== null}
                  className="btn-ghost flex-1 text-ceria-blue"
                >
                  {busy === 'now' ? (en ? 'Backing up…' : 'Mencadangkan…') : en ? 'Back up now' : 'Cadangkan sekarang'}
                </button>
                <button
                  onClick={onRestoreFromDrive}
                  disabled={busy !== null}
                  className="btn-ghost flex-1 text-ceria-blue"
                >
                  {busy === 'fromDrive'
                    ? en
                      ? 'Reading…'
                      : 'Membaca…'
                    : en
                      ? 'Restore from Drive'
                      : 'Pulihkan dari Drive'}
                </button>
              </div>

              {settings.lastBackupAt && (
                <p className="mt-2 text-xs text-ceria-gray">
                  {en ? 'Last backup: ' : 'Cadangan terakhir: '}
                  {new Date(settings.lastBackupAt).toLocaleString(en ? 'en-GB' : 'id-ID')}
                </p>
              )}
            </>
          ) : (
            <>
              <button onClick={onConnect} disabled={busy !== null} className="btn-ghost w-full text-ceria-blue">
                {busy === 'connect'
                  ? en
                    ? 'Connecting…'
                    : 'Menghubungkan…'
                  : en
                    ? 'Connect Google Drive'
                    : 'Hubungkan Google Drive'}
              </button>
              <p className="mt-1.5 text-xs text-ceria-gray">
                {en
                  ? 'The backup goes into your own Drive, in one file only Ceria can open. Ceria can see nothing else in your Drive, and keeps no copy.'
                  : 'Cadangan masuk ke Drive milik Anda sendiri, dalam satu berkas yang hanya dapat dibuka Ceria. Ceria tidak dapat melihat apa pun yang lain di Drive Anda, dan tidak menyimpan salinan.'}
              </p>
            </>
          )}
        </div>
      )}

      {msg && <p className="mt-2 text-xs text-ceria-gray">{msg}</p>}

      {/* Restoring overwrites; show what is in the file first. */}
      {pending && (
        <div className="mt-3 rounded-xl border border-ceria-pink/30 bg-ceria-pink/5 p-3">
          <p className="text-[13px] font-semibold text-ceria-dark">
            {en ? 'Replace what is on this phone?' : 'Ganti isi di ponsel ini?'}
          </p>
          <p className="mt-1 text-xs text-ceria-gray">
            {en ? 'From ' : 'Dari '}
            {pending.summary.device} ·{' '}
            {new Date(pending.summary.savedAt).toLocaleString(en ? 'en-GB' : 'id-ID')}
            <br />
            {pending.summary.days} {plural(pending.summary.days, en, 'day written', 'days written', 'hari terisi')}{' '}
            · {pending.summary.daysRead}{' '}
            {plural(pending.summary.daysRead, en, 'day read', 'days read', 'hari dibaca')} ·{' '}
            {pending.summary.photos} {plural(pending.summary.photos, en, 'photo', 'photos', 'foto')}
          </p>
          <p className="mt-1.5 text-xs text-ceria-gray">
            {en
              ? 'Anything currently on this phone will be replaced. This cannot be undone.'
              : 'Semua yang ada di ponsel ini sekarang akan digantikan. Tindakan ini tidak dapat dibatalkan.'}
          </p>
          <div className="mt-2 flex gap-2">
            <button onClick={confirmRestore} className="btn-primary flex-1 py-2 text-sm">
              {en ? 'Restore' : 'Pulihkan'}
            </button>
            <button onClick={() => setPending(null)} className="btn-ghost flex-1 py-2 text-sm">
              {en ? 'Cancel' : 'Batal'}
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
