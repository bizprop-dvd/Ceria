import { Link, useNavigate } from 'react-router-dom'
import Screen from '../components/Screen'
import LockBadge from '../components/LockBadge'
import { ChevronRight, LockIcon } from '../components/icons'
import { guidebook, daily, daysForChapter } from '../data/content'
import { useApp } from '../store/AppContext'
import { usePaywall } from '../components/PaywallProvider'
import { isUnlocked } from '../lib/freemium'
import { chapterTheme } from '../lib/chapterTheme'

export default function Guidebook() {
  const { t, lang, hasPurchased, entries, daysReadCount } = useApp()
  const { openPaywall } = usePaywall()
  const navigate = useNavigate()
  const read = entries.daysRead ?? {}

  return (
    <Screen
      title={lang === 'en' ? 'Guidebook' : 'Panduan'}
      subtitle={lang === 'en' ? '12 chapters · 365 days' : '12 bab · 365 hari'}
    >
      {/* Year map entry — the progress artefact */}
      <Link
        to="/guidebook/year"
        className="card mt-1 flex items-center gap-3 p-4 active:scale-[0.99] transition"
      >
        <YearSpark read={read} />
        <div className="min-w-0 flex-1">
          <p className="font-head text-[15px] font-semibold text-ceria-dark">
            {lang === 'en' ? 'Your year' : 'Tahun Anda'}
          </p>
          <p className="text-xs text-ceria-gray">
            {lang === 'en'
              ? `${daysReadCount} of ${daily.meta.totalDays} days`
              : `${daysReadCount} dari ${daily.meta.totalDays} hari`}
          </p>
        </div>
        <ChevronRight className="shrink-0 text-ceria-gray" />
      </Link>

      <ul className="mt-4 space-y-2.5">
        {guidebook.chapters.map((ch) => {
          const unlocked = isUnlocked(ch.number, hasPurchased)
          const theme = chapterTheme(ch.number)
          const days = daysForChapter(ch.number)
          const done = days.filter((d) => read[d.day]).length
          return (
            <li key={ch.number}>
              <button
                onClick={() => (unlocked ? navigate(`/guidebook/${ch.number}`) : openPaywall())}
                className="card flex w-full items-stretch gap-0 overflow-hidden p-0 text-left active:scale-[0.99] transition"
              >
                {/* chapter colour spine */}
                <span
                  aria-hidden
                  className="w-1.5 shrink-0"
                  style={{ background: unlocked ? theme.ring : '#E5DED0' }}
                />
                <span className="flex flex-1 items-center gap-3 p-4">
                  <span
                    className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl font-head text-lg font-semibold"
                    style={
                      unlocked
                        ? { background: theme.tint, color: theme.base }
                        : { background: '#F2E9D9', color: '#6B7280' }
                    }
                  >
                    {ch.number}
                  </span>
                  <span className="min-w-0 flex-1">
                    <span className="block truncate font-head text-[15px] font-semibold text-ceria-dark">
                      {t(ch.title)}
                    </span>
                    <span className="mt-0.5 block line-clamp-2 text-xs text-ceria-gray">
                      {t(ch.principle)}
                    </span>
                    {unlocked && days.length > 0 && (
                      <span
                        className="mt-1.5 block text-[11px] tabular-nums"
                        style={{ color: theme.base }}
                      >
                        {done}/{days.length} {lang === 'en' ? 'days' : 'hari'}
                      </span>
                    )}
                  </span>
                  {unlocked ? (
                    <ChevronRight className="shrink-0 text-ceria-gray" />
                  ) : (
                    <LockBadge />
                  )}
                </span>
              </button>
            </li>
          )
        })}
      </ul>

      {!hasPurchased && (
        <button
          onClick={openPaywall}
          className="mt-4 flex w-full items-center justify-center gap-2 rounded-2xl border border-dashed border-ceria-blue/30 px-4 py-3 text-sm font-medium text-ceria-blue"
        >
          <LockIcon width={16} height={16} />
          {lang === 'en' ? 'Unlock chapters 5–12' : 'Buka bab 5–12'}
        </button>
      )}
    </Screen>
  )
}

/** A miniature of the year map — twelve colour bands, filled as days complete. */
function YearSpark({ read }: { read: Record<number, boolean> }) {
  return (
    <span className="flex h-11 shrink-0 items-end gap-[3px]" aria-hidden>
      {daily.chapters.map((ch) => {
        const theme = chapterTheme(ch.number)
        const days = daily.days.filter((d) => d.chapter === ch.number)
        const done = days.filter((d) => read[d.day]).length
        const frac = days.length ? done / days.length : 0
        return (
          <span
            key={ch.number}
            className="relative w-[4px] overflow-hidden rounded-full"
            style={{ height: '100%', background: theme.tint }}
          >
            <span
              className="absolute bottom-0 left-0 w-full rounded-full"
              style={{ height: `${Math.max(frac * 100, frac > 0 ? 12 : 0)}%`, background: theme.ring }}
            />
          </span>
        )
      })}
    </span>
  )
}
