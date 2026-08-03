import { Navigate, useParams, Link } from 'react-router-dom'
import Screen from '../components/Screen'
import { dayByNumber, daysForChapter, chapterName } from '../data/content'
import { useApp } from '../store/AppContext'
import { isUnlocked } from '../lib/freemium'
import { ChevronLeft, ChevronRight, SparkIcon } from '../components/icons'
import type { Framework } from '../data/types'

export default function DailyDay() {
  const { d } = useParams()
  const { t, lang, hasPurchased } = useApp()
  const num = Number(d)
  const day = dayByNumber(num)

  if (!day) return <Navigate to="/guidebook" replace />
  if (!isUnlocked(day.chapter, hasPurchased)) return <Navigate to="/guidebook" replace />

  const siblings = daysForChapter(day.chapter)
  const idx = siblings.findIndex((x) => x.day === day.day)
  const prev = idx > 0 ? siblings[idx - 1] : undefined
  const next = idx >= 0 && idx < siblings.length - 1 ? siblings[idx + 1] : undefined
  const chapter = chapterName(day.chapter)

  return (
    <Screen
      back
      title={t(day.title)}
      subtitle={`${lang === 'en' ? 'Day' : 'Hari'} ${day.day} · ${chapter ? t(chapter) : ''}`}
    >
      <article className="mx-auto max-w-prose pt-2">
        {/* Teaching */}
        <section className="card p-4">
          <p className="whitespace-pre-line text-[15px] leading-relaxed text-ceria-dark/90">
            {t(day.teaching)}
          </p>
        </section>

        {day.framework && <FrameworkCards framework={day.framework} />}

        {/* In practice */}
        <Block label={lang === 'en' ? 'In practice' : 'Dalam praktik'} text={t(day.inPractice)} />

        {/* Today's practice */}
        <div className="card mt-4 border-l-4 border-l-ceria-blue p-4">
          <p className="text-xs font-semibold uppercase tracking-wide text-ceria-blue">
            {lang === 'en' ? 'Try this today' : 'Coba ini hari ini'}
          </p>
          <p className="mt-1 text-[15px] leading-relaxed text-ceria-dark">{t(day.practice)}</p>
        </div>

        {/* Script */}
        <div className="mt-4 rounded-2xl bg-ceria-cream-deep/60 p-4">
          <p className="text-xs font-semibold uppercase tracking-wide text-ceria-gray">
            {lang === 'en' ? 'Words you can use' : 'Kata yang bisa dipakai'}
          </p>
          <p className="mt-1 font-head text-[17px] leading-snug text-ceria-dark">
            {t(day.script)}
          </p>
        </div>

        {/* Reflection */}
        <div className="card mt-4 bg-ceria-pink/[0.04] p-4">
          <p className="text-xs font-semibold uppercase tracking-wide text-ceria-pink">
            {lang === 'en' ? 'Reflect' : 'Renungkan'}
          </p>
          <p className="mt-1 font-head text-[17px] italic leading-snug text-ceria-dark">
            {t(day.reflection)}
          </p>
        </div>

        {/* Safeguarding note */}
        <p className="mt-4 text-[12px] leading-relaxed text-ceria-gray/80">{t(day.support)}</p>

        {day.reference && (
          <p className="mt-2 text-center text-xs text-ceria-gray/80">
            {lang === 'en' ? 'Further reading: ' : 'Bacaan lanjutan: '}
            {day.reference}
          </p>
        )}

        {/* Prev / next within the chapter */}
        <nav className="mt-6 flex items-stretch gap-2">
          {prev ? (
            <Link
              to={`/guidebook/day/${prev.day}`}
              className="card flex flex-1 items-center gap-2 p-3 active:scale-[0.99] transition"
            >
              <ChevronLeft width={18} height={18} className="shrink-0 text-ceria-gray" />
              <span className="min-w-0">
                <span className="block text-[11px] text-ceria-gray">
                  {lang === 'en' ? `Day ${prev.day}` : `Hari ${prev.day}`}
                </span>
                <span className="block truncate text-[13px] font-medium text-ceria-dark">
                  {t(prev.title)}
                </span>
              </span>
            </Link>
          ) : (
            <span className="flex-1" />
          )}
          {next ? (
            <Link
              to={`/guidebook/day/${next.day}`}
              className="card flex flex-1 items-center justify-end gap-2 p-3 text-right active:scale-[0.99] transition"
            >
              <span className="min-w-0">
                <span className="block text-[11px] text-ceria-gray">
                  {lang === 'en' ? `Day ${next.day}` : `Hari ${next.day}`}
                </span>
                <span className="block truncate text-[13px] font-medium text-ceria-dark">
                  {t(next.title)}
                </span>
              </span>
              <ChevronRight width={18} height={18} className="shrink-0 text-ceria-gray" />
            </Link>
          ) : (
            <span className="flex-1" />
          )}
        </nav>
      </article>
    </Screen>
  )
}

// Classes are written out in full — Tailwind cannot see interpolated names.
function Block({ label, text }: { label: string; text: string }) {
  return (
    <section className="card mt-4 border-l-4 border-l-ceria-teal p-4">
      <p className="text-xs font-semibold uppercase tracking-wide text-ceria-teal">{label}</p>
      <p className="mt-1 whitespace-pre-line text-[15px] leading-relaxed text-ceria-dark/90">
        {text}
      </p>
    </section>
  )
}

/** Renders a teaching grid — e.g. the four parenting styles. */
function FrameworkCards({ framework }: { framework: Framework }) {
  const { t } = useApp()
  return (
    <section className="mt-5">
      <div className="mb-2 flex items-center gap-2">
        <SparkIcon width={18} height={18} className="shrink-0 text-ceria-pink" />
        <h2 className="font-head text-lg font-semibold text-ceria-blue">
          {t(framework.title)}
        </h2>
      </div>
      <p className="mb-3 text-sm text-ceria-gray">{t(framework.note)}</p>
      <ul className="grid grid-cols-1 gap-2.5">
        {framework.entries.map((e, i) => (
          <li key={i} className="card p-4">
            <p className="font-head text-[16px] font-semibold text-ceria-dark">{t(e.name)}</p>
            <div className="mt-1.5 flex flex-wrap gap-1.5">
              {e.tags.map((tag, j) => (
                <span key={j} className="chip bg-ceria-blue/8 text-ceria-blue">
                  {t(tag)}
                </span>
              ))}
            </div>
            <p className="mt-2 text-[14px] leading-relaxed text-ceria-dark/85">{t(e.looksLike)}</p>
            <p className="mt-1.5 text-[13px] leading-relaxed text-ceria-gray">{t(e.outcome)}</p>
          </li>
        ))}
      </ul>
    </section>
  )
}
