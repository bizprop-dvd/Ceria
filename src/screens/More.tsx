import { useState } from 'react'
import Screen from '../components/Screen'
import Segmented from '../components/Segmented'
import BackupCard from '../components/BackupCard'
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

        {/* Edition — stacked, since these labels are longer than the language ones */}
        <Row
          label={lang === 'en' ? 'Diary edition' : 'Edisi diari'}
          hint={
            lang === 'en'
              ? 'Parents shows Mama & Papa columns; Single parent shows one.'
              : 'Edisi Orang Tua menampilkan kolom Mama dan Papa; Edisi Orang Tua Tunggal menampilkan satu kolom.'
          }
          stacked
        >
          <Segmented<Edition>
            value={edition}
            onChange={setEdition}
            fill
            options={[
              { value: 'combined', label: lang === 'en' ? 'Parents' : 'Orang Tua' },
              { value: 'solo', label: lang === 'en' ? 'Single parent' : 'Orang Tua Tunggal' },
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
                  : 'Pengingat lembut untuk menulis beberapa baris. Sepenuhnya opsional dan tidak memaksa.'}
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
                  {lang === 'en' ? 'Fires only on device' : 'Pengingat hanya aktif di perangkat ini'}
                </span>
              )}
            </div>
          )}
        </div>

        <BackupCard />

        {/* Unlock / status */}
        <div className="card p-4">
          {hasPurchased ? (
            <div className="flex items-center gap-3">
              <CheckIcon className="text-ceria-teal" />
              <div>
                <p className="font-head text-[15px] font-semibold text-ceria-dark">
                  {lang === 'en' ? 'Full access unlocked' : 'Akses penuh sudah terbuka'}
                </p>
                <p className="text-xs text-ceria-gray">
                  {lang === 'en' ? 'Thank you for supporting Ceria.' : 'Terima kasih telah mendukung Ceria.'}
                </p>
              </div>
            </div>
          ) : (
            <button onClick={openPaywall} className="btn-primary w-full">
              <LockIcon width={18} height={18} />
              {lang === 'en' ? 'Unlock everything' : 'Buka akses lengkap'}
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
            <ExtLink href={CERIA.termsUrl}>
              {lang === 'en' ? 'Terms of use' : 'Ketentuan penggunaan'}
            </ExtLink>
            {CERIA.supportEmail && (
              <ExtLink href={`mailto:${CERIA.supportEmail}`}>
                {lang === 'en' ? 'Contact us' : 'Hubungi kami'}
              </ExtLink>
            )}
          </div>

          {/* Educational-content notice — matches the EULA, and Apple looks for it. */}
          <p className="mt-3 text-[12px] leading-relaxed text-ceria-gray/85">
            {lang === 'en'
              ? 'Ceria offers general parenting education. It is not medical advice, therapy, or a substitute for care from a qualified professional. If you are worried about your child or yourself, please seek professional support.'
              : 'Ceria menyediakan edukasi pengasuhan yang bersifat umum. Ceria bukan nasihat medis, terapi, atau pengganti pendampingan dari tenaga profesional yang berkualifikasi. Bila Anda mengkhawatirkan kondisi anak atau diri Anda, silakan mencari dukungan profesional.'}
          </p>
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

function Row({
  label,
  hint,
  stacked,
  children,
}: {
  label: string
  hint?: string
  /** put the control on its own line below the label (for longer labels) */
  stacked?: boolean
  children: React.ReactNode
}) {
  return (
    <div className="card p-4">
      <div className={stacked ? '' : 'flex items-center justify-between gap-3'}>
        <div>
          <p className="font-head text-[15px] font-semibold text-ceria-dark">{label}</p>
          {hint && <p className="mt-0.5 text-xs text-ceria-gray">{hint}</p>}
        </div>
        <div className={stacked ? 'mt-3' : ''}>{children}</div>
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
