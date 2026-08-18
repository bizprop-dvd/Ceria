import { Link } from 'react-router-dom'
import { useApp } from '../store/AppContext'
import { diary, weekByNumber, chapterName } from '../data/content'
import { currentWeek, dayKey } from '../lib/dates'
import { TOTAL_WEEKS } from '../data/content'
import { hasEntryToday } from '../lib/streak'
import PromptField from '../components/PromptField'
import WeekRing from '../components/WeekRing'
import { ChevronRight } from '../components/icons'
import { quoteForDay } from '../lib/dailyQuote'
import type { Role } from '../data/types'

export default function Today() {
  const { t, lang, settings, entries, setDailyAnswer, streak, daysWithEntries, hasPurchased } =
    useApp()
  const today = dayKey()
  const wkNum = currentWeek(settings.startDate, TOTAL_WEEKS)
  const week = weekByNumber(wkNum)
  const chapter = week ? chapterName(week.chapter) : undefined
  const todayAnswers = entries.daily[today] ?? {}
  const doneToday = hasEntryToday(daysWithEntries)
  const quote = quoteForDay(today, hasPurchased)

  const greeting = greetingFor(lang)


  return (
    <div className="flex h-full flex-col">
      <header
        className="sticky top-0 z-10 bg-ceria-cream/90 px-4 pb-3 backdrop-blur"
        style={{ paddingTop: 'calc(var(--safe-top) + 0.75rem)' }}
      >
        <div className="flex items-center gap-3">
          <img src="./logo.jpg" alt="Ceria" className="h-10 w-10 rounded-xl object-cover" />
          <div>
            <p className="text-xs text-ceria-gray">{greeting}</p>
            <h1 className="font-head text-xl font-semibold text-ceria-blue">
              {lang === 'en' ? 'Today' : 'Hari Ini'}
            </h1>
          </div>
        </div>
      </header>

      <main
        className="no-scrollbar flex-1 overflow-y-auto px-4"
        style={{ paddingBottom: 'calc(var(--safe-bottom) + 6.25rem)' }}
      >
        {/* A line from the guide — rotates daily, always Ceria's own words */}
        {quote && (
          <Link
            to={`/guidebook/day/${quote.day}`}
            className="card mt-1 block p-5 active:scale-[0.99] transition"
          >
            <p className="font-head text-[19px] leading-[1.45] text-ceria-dark">
              {t(quote.text)}
            </p>
            <p className="mt-2.5 text-[11px] uppercase tracking-[0.08em] text-ceria-gray">
              {lang === 'en' ? `Day ${quote.day}` : `Hari ${quote.day}`}
              {' · '}
              {doneToday
                ? streak > 0
                  ? lang === 'en'
                    ? `${streak} ${streak === 1 ? 'day' : 'days'} of showing up`
                    : `${streak} hari meluangkan waktu untuk hadir`
                  : lang === 'en'
                    ? 'Written today'
                    : 'Sudah ditulis hari ini'
                : lang === 'en'
                  ? 'A fresh page whenever you are ready'
                  : 'Halaman baru menunggu kapan pun Anda siap'}
            </p>
          </Link>
        )}

        {/* The week as a ring */}
        <div className="mt-3">
          <WeekRing week={wkNum} />
        </div>

        {/* This week's theme */}
        {week && (
          <Link
            to={`/diary/${week.week}`}
            className="card mt-3 flex items-center gap-3 p-4 active:scale-[0.99] transition"
          >
            <div className="min-w-0 flex-1">
              <p className="text-xs font-semibold uppercase tracking-wide text-ceria-teal">
                {lang === 'en' ? `Week ${week.week}` : `Minggu ${week.week}`} ·{' '}
                {chapter ? t(chapter) : ''}
              </p>
              <p className="font-head text-lg font-semibold text-ceria-dark truncate">
                {t(week.theme)}
              </p>
              <p className="mt-0.5 text-sm text-ceria-gray line-clamp-2">{t(week.principle)}</p>
            </div>
            <ChevronRight className="shrink-0 text-ceria-gray" />
          </Link>
        )}

        {/* Today's daily prompts */}
        <h2 className="mb-2 mt-6 font-head text-lg font-semibold text-ceria-blue">
          {lang === 'en' ? 'A few lines for today' : 'Beberapa baris untuk hari ini'}
        </h2>
        <div className="card p-4">
          {diary.meta.dailyPrompts.map((prompt, i) => (
            <PromptField
              key={i}
              label={t(prompt)}
              getValue={(role: Role) => todayAnswers[role]?.[i] ?? ''}
              onChange={(role, value) => setDailyAnswer(today, role, i, value)}
              rows={2}
            />
          ))}
          <p className="text-center text-xs text-ceria-gray/80">
            {lang === 'en'
              ? 'Saved automatically on this device.'
              : 'Tersimpan otomatis di perangkat ini.'}
          </p>
        </div>
      </main>
    </div>
  )
}

function greetingFor(lang: 'en' | 'id'): string {
  const h = new Date().getHours()
  if (lang === 'en') {
    if (h < 12) return 'Good morning'
    if (h < 18) return 'Good afternoon'
    return 'Good evening'
  }
  if (h < 11) return 'Selamat pagi'
  if (h < 15) return 'Selamat siang'
  if (h < 19) return 'Selamat sore'
  return 'Selamat malam'
}
