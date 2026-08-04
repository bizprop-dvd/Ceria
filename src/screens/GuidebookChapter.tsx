import { Navigate, useParams, Link, useNavigate } from 'react-router-dom'
import Screen from '../components/Screen'
import ProvisionalNote from '../components/ProvisionalNote'
import { chapterByNumber, daysForChapter } from '../data/content'
import { useApp } from '../store/AppContext'
import { isUnlocked } from '../lib/freemium'
import { chapterTheme, chapterVars } from '../lib/chapterTheme'
import { CheckIcon, ChevronRight, LockIcon, ToolIcon } from '../components/icons'
import { usePaywall } from '../components/PaywallProvider'

export default function GuidebookChapter() {
  const { n } = useParams()
  const { t, lang, hasPurchased } = useApp()
  const num = Number(n)
  const ch = chapterByNumber(num)

  if (!ch) return <Navigate to="/guidebook" replace />
  const unlocked = isUnlocked(ch.number, hasPurchased)

  return (
   <div className="h-full" style={chapterVars(ch.number)}>
    <Screen back title={t(ch.title)} subtitle={lang === 'en' ? `Chapter ${ch.number}` : `Bab ${ch.number}`}>
      <article className="mx-auto max-w-prose pt-2">
        {/* Principle */}
        <div className="card border-l-4 p-4" style={{ borderLeftColor: 'var(--ch-base)' }}>
          <p className="text-xs font-semibold uppercase tracking-wide" style={{ color: 'var(--ch-base)' }}>
            {lang === 'en' ? 'Principle' : 'Prinsip'}
          </p>
          <p className="mt-1 font-head text-lg leading-snug text-ceria-dark">{t(ch.principle)}</p>
        </div>

        {!unlocked ? (
          <LockedChapterNote />
        ) : ch._needsProse ? (
          <ProvisionalNote kind="chapter" />
        ) : (
          <>
            {ch.why && (
              <Section title={lang === 'en' ? 'Why it matters' : 'Mengapa penting'}>
                {t(ch.why)}
              </Section>
            )}
            {ch.inPractice && (
              <Section title={lang === 'en' ? 'In practice' : 'Dalam praktik'}>
                {t(ch.inPractice)}
              </Section>
            )}
            {ch.dailyPractices && (
              <div className="mt-6">
                <h2 className="mb-2 font-head text-lg font-semibold text-ceria-blue">
                  {lang === 'en' ? 'Try this' : 'Coba ini'}
                </h2>
                <ul className="space-y-2">
                  {ch.dailyPractices[lang].map((p, i) => (
                    <li key={i} className="card flex items-start gap-3 p-3">
                      <CheckIcon width={18} height={18} className="mt-0.5 shrink-0 text-ceria-teal" />
                      <span className="text-[15px] leading-relaxed text-ceria-dark">{p}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
            {ch.reflection && (
              <div className="card mt-6 bg-ceria-cream-deep/50 p-4">
                <p className="text-xs font-semibold uppercase tracking-wide text-ceria-pink">
                  {lang === 'en' ? 'Reflect' : 'Renungkan sejenak'}
                </p>
                <p className="mt-1 font-head text-[17px] italic leading-snug text-ceria-dark">
                  {t(ch.reflection)}
                </p>
              </div>
            )}
          </>
        )}

        {/* 365-day practice for this chapter */}
        <DailyDays chapter={ch.number} unlocked={unlocked} />

        {/* Linked tool */}
        {ch.toolRef && (
          <Link
            to={`/toolkit/${ch.toolRef}`}
            className="card mt-6 flex items-center gap-3 p-4 active:scale-[0.99] transition"
          >
            <ToolIcon width={22} height={22} className="shrink-0 text-ceria-blue" />
            <span className="text-sm font-medium text-ceria-blue">
              {lang === 'en' ? 'Open the matching tool' : 'Buka alat yang sesuai'}
            </span>
          </Link>
        )}

        {ch.reference && (
          <p className="mt-6 text-center text-xs text-ceria-gray/80">
            {lang === 'en' ? 'Further reading: ' : 'Bacaan lanjutan: '}
            {ch.reference}
          </p>
        )}
      </article>
    </Screen>
   </div>
  )
}

/** The chapter's slice of the 365-day guide. Hidden until days are authored. */
function DailyDays({ chapter, unlocked }: { chapter: number; unlocked: boolean }) {
  const { t, lang, entries } = useApp()
  const { openPaywall } = usePaywall()
  const days = daysForChapter(chapter)
  const read = entries.daysRead ?? {}
  const theme = chapterTheme(chapter)
  const navigate = useNavigate()
  if (days.length === 0) return null

  return (
    <section className="mt-7">
      <h2 className="font-head text-lg font-semibold" style={{ color: theme.base }}>
        {lang === 'en' ? 'Day by day' : 'Hari demi hari'}
      </h2>
      <p className="mb-2 text-xs text-ceria-gray">
        {lang === 'en'
          ? `${days.length} short readings, one a day.`
          : `${days.length} bacaan singkat, satu setiap hari.`}
      </p>
      <ul className="space-y-2">
        {days.map((d) => (
          <li key={d.day}>
            <button
              onClick={() => (unlocked ? navigate(`/guidebook/day/${d.day}`) : openPaywall())}
              className="card flex w-full items-center gap-3 p-3.5 text-left active:scale-[0.99] transition"
            >
              <span
                className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg text-sm font-semibold"
                style={
                  !unlocked
                    ? { background: '#F2E9D9', color: '#6B7280' }
                    : read[d.day]
                      ? { background: theme.ring, color: '#fff' }
                      : { background: theme.tint, color: theme.base }
                }
              >
                {d.day}
              </span>
              <span className="min-w-0 flex-1 truncate font-head text-[15px] font-semibold text-ceria-dark">
                {t(d.title)}
              </span>
              {unlocked ? (
                <ChevronRight width={18} height={18} className="shrink-0 text-ceria-gray" />
              ) : (
                <LockIcon width={16} height={16} className="shrink-0 text-ceria-gray" />
              )}
            </button>
          </li>
        ))}
      </ul>
    </section>
  )
}

function Section({ title, children }: { title: string; children: string }) {
  return (
    <section className="mt-6">
      <h2 className="mb-1.5 font-head text-lg font-semibold text-ceria-blue">{title}</h2>
      <p className="whitespace-pre-line text-[15px] leading-relaxed text-ceria-dark/90">{children}</p>
    </section>
  )
}

/** Shown in place of a paid chapter's body. */
function LockedChapterNote() {
  const { lang } = useApp()
  const { openPaywall } = usePaywall()
  return (
    <div className="card mt-4 p-5 text-center">
      <LockIcon width={26} height={26} className="mx-auto text-ceria-gray" />
      <p className="mt-2 font-head text-[16px] font-semibold text-ceria-dark">
        {lang === 'en' ? 'Part of the full guide' : 'Bagian dari panduan lengkap'}
      </p>
      <p className="mt-1 text-sm text-ceria-gray">
        {lang === 'en'
          ? 'Chapters 1–4 are free. Unlock the rest whenever you are ready.'
          : 'Bab 1–4 gratis. Buka sisanya kapan pun Anda siap.'}
      </p>
      <button onClick={openPaywall} className="btn-primary mt-4">
        {lang === 'en' ? 'See what is included' : 'Lihat isinya'}
      </button>
    </div>
  )
}
