import { Navigate, useParams, Link } from 'react-router-dom'
import Screen from '../components/Screen'
import ProvisionalNote from '../components/ProvisionalNote'
import { chapterByNumber, daysForChapter } from '../data/content'
import { useApp } from '../store/AppContext'
import { isUnlocked } from '../lib/freemium'
import { CheckIcon, ChevronRight, ToolIcon } from '../components/icons'

export default function GuidebookChapter() {
  const { n } = useParams()
  const { t, lang, hasPurchased } = useApp()
  const num = Number(n)
  const ch = chapterByNumber(num)

  if (!ch) return <Navigate to="/guidebook" replace />
  if (!isUnlocked(ch.number, hasPurchased)) return <Navigate to="/guidebook" replace />

  return (
    <Screen back title={t(ch.title)} subtitle={lang === 'en' ? `Chapter ${ch.number}` : `Bab ${ch.number}`}>
      <article className="mx-auto max-w-prose pt-2">
        {/* Principle */}
        <div className="card border-l-4 border-l-ceria-teal p-4">
          <p className="text-xs font-semibold uppercase tracking-wide text-ceria-teal">
            {lang === 'en' ? 'Principle' : 'Prinsip'}
          </p>
          <p className="mt-1 font-head text-lg leading-snug text-ceria-dark">{t(ch.principle)}</p>
        </div>

        {ch._needsProse ? (
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
                  {lang === 'en' ? 'Reflect' : 'Renungkan'}
                </p>
                <p className="mt-1 font-head text-[17px] italic leading-snug text-ceria-dark">
                  {t(ch.reflection)}
                </p>
              </div>
            )}
          </>
        )}

        {/* 365-day practice for this chapter */}
        <DailyDays chapter={ch.number} />

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
  )
}

/** The chapter's slice of the 365-day guide. Hidden until days are authored. */
function DailyDays({ chapter }: { chapter: number }) {
  const { t, lang } = useApp()
  const days = daysForChapter(chapter)
  if (days.length === 0) return null

  return (
    <section className="mt-7">
      <h2 className="font-head text-lg font-semibold text-ceria-blue">
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
            <Link
              to={`/guidebook/day/${d.day}`}
              className="card flex items-center gap-3 p-3.5 active:scale-[0.99] transition"
            >
              <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-ceria-blue/8 text-sm font-semibold text-ceria-blue">
                {d.day}
              </span>
              <span className="min-w-0 flex-1 truncate font-head text-[15px] font-semibold text-ceria-dark">
                {t(d.title)}
              </span>
              <ChevronRight width={18} height={18} className="shrink-0 text-ceria-gray" />
            </Link>
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
