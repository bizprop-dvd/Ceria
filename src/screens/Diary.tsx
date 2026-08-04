import { Link, useNavigate } from 'react-router-dom'
import Screen from '../components/Screen'
import { ChevronRight, InfoIcon, LockIcon } from '../components/icons'
import { CHAPTERS, diary } from '../data/content'
import { useApp } from '../store/AppContext'
import { usePaywall } from '../components/PaywallProvider'
import { isUnlocked } from '../lib/freemium'
import { currentWeek } from '../lib/dates'
import { TOTAL_WEEKS } from '../data/content'

export default function Diary() {
  const { t, lang, hasPurchased, settings } = useApp()
  const { openPaywall } = usePaywall()
  const navigate = useNavigate()
  const thisWeek = currentWeek(settings.startDate, TOTAL_WEEKS)

  return (
    <Screen
      title={lang === 'en' ? 'Diary' : 'Diari'}
      subtitle={lang === 'en' ? '52 weeks · one gentle year' : '52 minggu · satu tahun yang dijalani dengan lembut'}
      right={
        <Link
          to="/diary/about"
          aria-label={lang === 'en' ? 'How this diary works' : 'Cara kerja diari ini'}
          className="flex h-9 w-9 items-center justify-center rounded-full text-ceria-blue active:bg-ceria-cream-deep"
        >
          <InfoIcon width={22} height={22} />
        </Link>
      }
    >
      <div className="mt-1 space-y-6">
        {CHAPTERS.map((chapter) => {
          const weeks = diary.weeks.filter((w) => w.chapter === chapter.number)
          const unlocked = isUnlocked(chapter.number, hasPurchased)
          return (
            <section key={chapter.number}>
              <div className="mb-2 flex items-center gap-2">
                <h2 className="font-head text-sm font-semibold uppercase tracking-wide text-ceria-teal">
                  {lang === 'en' ? `Theme ${chapter.number}` : `Tema ${chapter.number}`} ·{' '}
                  {t(chapter)}
                </h2>
                {!unlocked && <LockIcon width={14} height={14} className="text-ceria-gray" />}
              </div>
              <ul className="space-y-2">
                {weeks.map((w) => {
                  const isNow = w.week === thisWeek
                  return (
                    <li key={w.week}>
                      <button
                        onClick={() => (unlocked ? navigate(`/diary/${w.week}`) : openPaywall())}
                        className={`card flex w-full items-center gap-3 p-3.5 text-left active:scale-[0.99] transition ${
                          isNow ? 'ring-2 ring-ceria-teal/40' : ''
                        }`}
                      >
                        <span
                          className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-lg text-sm font-semibold ${
                            unlocked
                              ? 'bg-ceria-blue/8 text-ceria-blue'
                              : 'bg-ceria-cream-deep text-ceria-gray'
                          }`}
                        >
                          {w.week}
                        </span>
                        <div className="min-w-0 flex-1">
                          <p className="font-head text-[15px] font-semibold text-ceria-dark truncate">
                            {t(w.theme)}
                          </p>
                          {isNow && (
                            <span className="chip mt-0.5 bg-ceria-teal/12 text-ceria-teal">
                              {lang === 'en' ? 'This week' : 'Minggu ini'}
                            </span>
                          )}
                        </div>
                        {unlocked ? (
                          <ChevronRight className="shrink-0 text-ceria-gray" />
                        ) : (
                          <LockIcon width={16} height={16} className="shrink-0 text-ceria-gray" />
                        )}
                      </button>
                    </li>
                  )
                })}
              </ul>
            </section>
          )
        })}
      </div>
    </Screen>
  )
}
