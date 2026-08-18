import { useEffect, useState } from 'react'
import { Navigate, useParams, Link } from 'react-router-dom'
import Screen from '../components/Screen'
import {
  chapterDaysIfLoaded,
  chapterName,
  dayByNumber,
  daysForChapter,
  loadChapterDays,
} from '../data/content'
import { useApp } from '../store/AppContext'
import { isUnlocked } from '../lib/freemium'
import { chapterVars } from '../lib/chapterTheme'
import { ChevronLeft, ChevronRight, CheckIcon, SparkIcon } from '../components/icons'
import type { Framework } from '../data/types'

export default function DailyDay() {
  const { d } = useParams()
  const { t, lang, hasPurchased, entries, toggleDayRead } = useApp()
  const num = Number(d)
  const summary = dayByNumber(num)

  // The day's text lives in its chapter's file. The module cache is the source
  // of truth; this state only exists to re-render once a fetch lands.
  const [, setLoads] = useState(0)
  const day = summary
    ? chapterDaysIfLoaded(summary.chapter)?.find((x) => x.day === num)
    : undefined
  const chapterNumber = summary?.chapter
  const needsLoad = Boolean(summary) && !day

  useEffect(() => {
    if (!chapterNumber || !needsLoad) return
    let live = true
    loadChapterDays(chapterNumber).then(() => {
      if (live) setLoads((n) => n + 1)
    })
    return () => {
      live = false
    }
  }, [chapterNumber, needsLoad])

  if (!summary) return <Navigate to="/guidebook" replace />
  if (!isUnlocked(summary.chapter, hasPurchased)) return <Navigate to="/guidebook" replace />

  const siblings = daysForChapter(summary.chapter)
  const idx = siblings.findIndex((x) => x.day === summary.day)
  const prev = idx > 0 ? siblings[idx - 1] : undefined
  const next = idx >= 0 && idx < siblings.length - 1 ? siblings[idx + 1] : undefined
  const chapter = chapterName(summary.chapter)
  const isRead = Boolean(entries.daysRead?.[summary.day])

  if (!day) {
    return (
      <div className="h-full" style={chapterVars(summary.chapter)}>
        <Screen
          back
          title={t(summary.title)}
          subtitle={`${lang === 'en' ? 'Day' : 'Hari'} ${summary.day} · ${chapter ? t(chapter) : ''}`}
        >
          <ReadingPlaceholder />
        </Screen>
      </div>
    )
  }

  return (
    <div className="h-full" style={chapterVars(day.chapter)}>
      <Screen
        back
        title={t(day.title)}
        subtitle={`${lang === 'en' ? 'Day' : 'Hari'} ${day.day} · ${chapter ? t(chapter) : ''}`}
      >
        <article className="mx-auto max-w-prose pt-2">
          {/* TEACHING — plain prose, no card. This is the reading. */}
          <section className="px-0.5">
            <p className="whitespace-pre-line text-[16px] leading-[1.75] text-ceria-dark/90">
              {t(day.teaching)}
            </p>
          </section>

          {day.framework && <FrameworkCards framework={day.framework} />}

          {/* IN PRACTICE — a scenario card, tinted in the chapter colour. */}
          <section
            className="mt-6 rounded-2xl p-4"
            style={{ background: 'var(--ch-tint)' }}
          >
            <p
              className="text-[11px] font-semibold uppercase tracking-[0.08em]"
              style={{ color: 'var(--ch-base)' }}
            >
              {lang === 'en' ? 'In practice' : 'Dalam praktik'}
            </p>
            <p className="mt-1.5 whitespace-pre-line text-[15px] leading-relaxed text-ceria-dark/90">
              {t(day.inPractice)}
            </p>
          </section>

          {/* SCRIPT — the speech bubble. The most shareable thing in the book. */}
          <section className="mt-6">
            <div className="relative rounded-3xl bg-white px-5 py-6 shadow-card">
              <p className="text-center font-head text-[21px] leading-[1.45] text-ceria-dark">
                {t(day.script)}
              </p>
              {/* bubble tail */}
              <span
                aria-hidden
                className="absolute -bottom-[9px] left-9 h-5 w-5 rotate-45 rounded-[3px] bg-white"
              />
            </div>
            <p className="mt-3 pl-9 text-[11px] uppercase tracking-[0.08em] text-ceria-gray">
              {lang === 'en' ? 'Words you can use' : 'Kata-kata yang bisa dicoba'}
            </p>
          </section>

          {/* TRY THIS — the single action, led by the chapter colour. */}
          <section className="mt-6 flex gap-3">
            <span
              aria-hidden
              className="mt-0.5 w-1 shrink-0 rounded-full"
              style={{ background: 'var(--ch-ring)' }}
            />
            <div>
              <p
                className="text-[11px] font-semibold uppercase tracking-[0.08em]"
                style={{ color: 'var(--ch-base)' }}
              >
                {lang === 'en' ? 'Try this today' : 'Coba lakukan hari ini'}
              </p>
              <p className="mt-1 text-[15px] leading-relaxed text-ceria-dark">
                {t(day.practice)}
              </p>
            </div>
          </section>

          {/* REFLECT — quiet, italic, no box. A question to sit with. */}
          <section className="mt-6 border-t border-ceria-cream-deep pt-5">
            <p className="text-[11px] uppercase tracking-[0.08em] text-ceria-gray">
              {lang === 'en' ? 'Reflect' : 'Renungkan sejenak'}
            </p>
            <p className="mt-1.5 font-head text-[18px] italic leading-snug text-ceria-dark/85">
              {t(day.reflection)}
            </p>
          </section>

          {/* Mark as read */}
          <button
            onClick={() => toggleDayRead(day.day)}
            className="mt-7 flex w-full items-center justify-center gap-2 rounded-full py-3 text-[15px] font-semibold transition active:scale-[0.99]"
            style={
              isRead
                ? { background: 'var(--ch-tint)', color: 'var(--ch-base)' }
                : { background: 'var(--ch-base)', color: '#fff' }
            }
          >
            <CheckIcon width={18} height={18} />
            {isRead
              ? lang === 'en'
                ? 'Done today'
                : 'Selesai hari ini'
              : lang === 'en'
                ? 'Mark as done'
                : 'Tandai sudah dilakukan'}
          </button>

          {/* SUPPORT — a quiet footnote. Never an alarm. */}
          <p className="mt-6 text-[12px] leading-relaxed text-ceria-gray/70">
            {t(day.support)}
          </p>

          {day.reference && (
            <p className="mt-2 text-[12px] text-ceria-gray/70">
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
    </div>
  )
}

/**
 * Shown for the moment a chapter's text is being read from the app's own
 * files. Quiet grey bars in the shape of the reading, so the screen settles
 * into place rather than flashing a spinner.
 */
function ReadingPlaceholder() {
  const widths = ['100%', '96%', '88%', '100%', '92%', '70%']
  return (
    <div className="mx-auto max-w-prose animate-pulse pt-4" aria-hidden>
      {widths.map((w, i) => (
        <span
          key={i}
          className="mb-3 block h-3.5 rounded-full bg-ceria-cream-deep"
          style={{ width: w }}
        />
      ))}
      <span className="mt-7 block h-28 rounded-2xl bg-ceria-cream-deep" />
    </div>
  )
}

/** A teaching grid — e.g. the four parenting styles. */
function FrameworkCards({ framework }: { framework: Framework }) {
  const { t } = useApp()
  return (
    <section className="mt-6">
      <div className="mb-1.5 flex items-center gap-2">
        <SparkIcon width={18} height={18} style={{ color: 'var(--ch-base)' }} />
        <h2 className="font-head text-lg font-semibold" style={{ color: 'var(--ch-base)' }}>
          {t(framework.title)}
        </h2>
      </div>
      <p className="mb-3 text-sm text-ceria-gray">{t(framework.note)}</p>
      <ul className="grid grid-cols-1 gap-2.5">
        {framework.entries.map((e, i) => (
          <li
            key={i}
            className="rounded-2xl border border-black/[0.04] bg-white p-4 shadow-card"
          >
            <p className="font-head text-[16px] font-semibold text-ceria-dark">{t(e.name)}</p>
            <div className="mt-1.5 flex flex-wrap gap-1.5">
              {e.tags.map((tag, j) => (
                <span
                  key={j}
                  className="chip"
                  style={{ background: 'var(--ch-tint)', color: 'var(--ch-base)' }}
                >
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
