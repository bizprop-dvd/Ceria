import { useState } from 'react'
import Screen from '../components/Screen'
import Segmented from '../components/Segmented'
import { useApp, DEFAULT_REMINDER } from '../store/AppContext'
import { usePaywall } from '../components/PaywallProvider'
import { isNative, resetMockPurchase } from '../lib/purchases'
import { requestNotificationPermission } from '../lib/notifications'
import { CERIA, ABOUT } from '../config'
import { CheckIcon, HeartIcon, LockIcon } from '../components/icons'
import type { Edition, Lang } from '../data/types'

export default function More() {
  const { lang, edition, setLang, setEdition, settings, updateSettings, hasPurchased, restore, refreshPurchase } =
    useApp()
  const { openPaywall } = usePaywall()
  const [restoreMsg, setRestoreMsg] = useState<string | null>(null)
  const about = ABOUT[lang]

  const reminderOn = settings.reminderTime !== null
  const reminderValue = settings.reminderTime
    ? `${String(settings.reminderTime.hour).padStart(2, '0')}:${String(settings.reminderTime.minute).padStart(2, '0')}`
    : `${String(DEFAULT_REMINDER.hour).padStart(2, '0')}:${String(DEFAULT_REMINDER.minute).padStart(2, '0')}`

  const toggleReminder = async (on: boolean) => {
    if (on) {
      if (isNative()) {
        const granted = await requestNotificationPermission()
        if (!granted) return
      }
      updateSettings({ reminderTime: DEFAULT_REMINDER })
    } else {
      updateSettings({ reminderTime: null })
    }
  }

  const changeReminderTime = (v: string) => {
    const [h, m] = v.split(':').map(Number)
    updateSettings({ reminderTime: { hour: h, minute: m } })
  }

  const onRestore = async () => {
    setRestoreMsg(lang === 'en' ? 'Restoring…' : 'Memulihkan…')
    const res = await restore()
    if (res.unlocked) {
      setRestoreMsg(lang === 'en' ? 'Restored — everything is unlocked.' : 'Dipulihkan — semua terbuka.')
    } else {
      setRestoreMsg(
        lang === 'en'
          ? 'No previous purchase found on this account.'
          : 'Tidak ada pembelian sebelumnya pada akun ini.',
      )
    }
  }

  return (
    <Screen title={lang === 'en' ? 'More' : 'Lainnya'}>
      <div className="space-y-6 pt-2">
        {/* Language */}
        <Row label={lang === 'en' ? 'Language' : 'Bahasa'}>
          <Segmented<Lang>
            value={lang}
            onChange={setLang}
            options={[
              { value: 'en', label: 'English' },
              { value: 'id', label: 'Indonesia' },
            ]}
          />
        </Row>

        {/* Edition */}
        <Row
          label={lang === 'en' ? 'Diary edition' : 'Edisi diari'}
          hint={
            lang === 'en'
              ? 'Combined shows Mama & Papa columns; Solo shows one.'
              : 'Gabungan menampilkan kolom Mama & Papa; Solo menampilkan satu.'
          }
        >
          <Segmented<Edition>
            value={edition}
            onChange={setEdition}
            options={[
              { value: 'combined', label: lang === 'en' ? 'Mama & Papa' : 'Mama & Papa' },
              { value: 'solo', label: 'Solo' },
            ]}
          />
        </Row>

        {/* Reminder */}
        <div className="card p-4">
          <div className="flex items-center justify-between">
            <div className="pr-3">
              <p className="font-head text-[15px] font-semibold text-ceria-dark">
                {lang === 'en' ? 'Evening reminder' : 'Pengingat malam'}
              </p>
              <p className="mt-0.5 text-xs text-ceria-gray">
                {lang === 'en'
                  ? 'A gentle nudge to write a few lines. Optional, never pushy.'
                  : 'Ajakan lembut untuk menulis beberapa baris. Opsional, tidak memaksa.'}
              </p>
            </div>
            <Toggle on={reminderOn} onChange={toggleReminder} />
          </div>
          {reminderOn && (
            <div className="mt-3 flex items-center gap-3">
              <input
                type="time"
                value={reminderValue}
                onChange={(e) => changeReminderTime(e.target.value)}
                className="field w-auto"
              />
              {!isNative() && (
                <span className="text-xs text-ceria-gray/80">
                  {lang === 'en' ? 'Fires only on device' : 'Aktif hanya di perangkat'}
                </span>
              )}
            </div>
          )}
        </div>

        {/* Unlock / status */}
        <div className="card p-4">
          {hasPurchased ? (
            <div className="flex items-center gap-3">
              <CheckIcon className="text-ceria-teal" />
              <div>
                <p className="font-head text-[15px] font-semibold text-ceria-dark">
                  {lang === 'en' ? 'Full access unlocked' : 'Akses penuh terbuka'}
                </p>
                <p className="text-xs text-ceria-gray">
                  {lang === 'en' ? 'Thank you for supporting Ceria.' : 'Terima kasih telah mendukung Ceria.'}
                </p>
              </div>
            </div>
          ) : (
            <button onClick={openPaywall} className="btn-primary w-full">
              <LockIcon width={18} height={18} />
              {lang === 'en' ? 'Unlock everything' : 'Buka semuanya'}
            </button>
          )}
          <button
            onClick={onRestore}
            className="btn-ghost mt-2 w-full text-ceria-blue"
          >
            {lang === 'en' ? 'Restore purchase' : 'Pulihkan pembelian'}
          </button>
          {restoreMsg && <p className="mt-1 text-center text-xs text-ceria-gray">{restoreMsg}</p>}
        </div>

        {/* About Ceria */}
        <div className="card p-4">
          <div className="mb-2 flex items-center gap-2">
            <HeartIcon width={20} height={20} className="text-ceria-pink" />
            <h2 className="font-head text-lg font-semibold text-ceria-blue">
              {lang === 'en' ? 'About Ceria' : 'Tentang Ceria'}
            </h2>
          </div>
          <p className="text-sm leading-relaxed text-ceria-dark/85">{about.mission}</p>
          <p className="mt-2 text-sm leading-relaxed text-ceria-dark/85">{about.proceeds}</p>
          <p className="mt-2 rounded-xl bg-ceria-teal/8 p-3 text-[13px] leading-relaxed text-ceria-dark/80">
            {about.privacy}
          </p>
          <div className="mt-3 flex flex-wrap gap-2">
            <ExtLink href={CERIA.instagramUrl}>Instagram</ExtLink>
            <ExtLink href={CERIA.websiteUrl}>{lang === 'en' ? 'Website' : 'Situs web'}</ExtLink>
            <ExtLink href={CERIA.privacyPolicyUrl}>
              {lang === 'en' ? 'Privacy policy' : 'Kebijakan privasi'}
            </ExtLink>
          </div>
        </div>

        {/* Dev tools — browser only */}
        {!isNative() && (
          <div className="card border-dashed border-ceria-cream-deep p-4">
            <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-ceria-gray">
              Dev tools (browser only)
            </p>
            <button
              onClick={async () => {
                await resetMockPurchase()
                await refreshPurchase()
                setRestoreMsg(null)
              }}
              className="btn-ghost text-ceria-pink"
            >
              Reset mock purchase
            </button>
          </div>
        )}

        <p className="pb-2 text-center text-xs text-ceria-gray/70">Ceria · v0.1.0</p>
      </div>
    </Screen>
  )
}

function Row({ label, hint, children }: { label: string; hint?: string; children: React.ReactNode }) {
  return (
    <div className="card p-4">
      <div className="flex items-center justify-between gap-3">
        <div>
          <p className="font-head text-[15px] font-semibold text-ceria-dark">{label}</p>
          {hint && <p className="mt-0.5 text-xs text-ceria-gray">{hint}</p>}
        </div>
        {children}
      </div>
    </div>
  )
}

function Toggle({ on, onChange }: { on: boolean; onChange: (on: boolean) => void }) {
  return (
    <button
      role="switch"
      aria-checked={on}
      onClick={() => onChange(!on)}
      className={`relative h-7 w-12 shrink-0 rounded-full transition ${
        on ? 'bg-ceria-teal' : 'bg-ceria-cream-deep'
      }`}
    >
      <span
        className={`absolute top-0.5 h-6 w-6 rounded-full bg-white shadow transition ${
          on ? 'left-[1.375rem]' : 'left-0.5'
        }`}
      />
    </button>
  )
}

function ExtLink({ href, children }: { href: string; children: React.ReactNode }) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noreferrer"
      className="chip bg-ceria-blue/8 text-ceria-blue"
    >
      {children}
    </a>
  )
}
