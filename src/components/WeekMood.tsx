import { useApp } from '../store/AppContext'

/**
 * How the week felt — five icons, not a dropdown.
 *
 * Deliberately not a 1-5 rating: a scale invites a parent to score themselves,
 * and this diary never grades anyone. These are five honest weathers, none of
 * them a failure.
 */
export const MOODS = [
  { key: 'steady', en: 'Steady', id: 'Stabil' },
  { key: 'close', en: 'Close', id: 'Dekat' },
  { key: 'tiring', en: 'Tiring', id: 'Melelahkan' },
  { key: 'stormy', en: 'Stormy', id: 'Bergejolak' },
  { key: 'tender', en: 'Tender', id: 'Mengharukan' },
] as const

function MoodGlyph({ mood, active }: { mood: string; active: boolean }) {
  const stroke = active ? '#fff' : 'currentColor'
  const common = {
    width: 24,
    height: 24,
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke,
    strokeWidth: 1.7,
    strokeLinecap: 'round' as const,
    strokeLinejoin: 'round' as const,
  }
  switch (mood) {
    case 'steady': // a level horizon
      return (
        <svg {...common}>
          <path d="M3 12h18" />
          <circle cx="12" cy="12" r="8" />
        </svg>
      )
    case 'close': // two shapes leaning together
      return (
        <svg {...common}>
          <path d="M12 20s-6-3.8-8-7.5A4 4 0 0 1 12 8a4 4 0 0 1 8 4.5c-2 3.7-8 7.5-8 7.5z" />
        </svg>
      )
    case 'tiring': // a waning moon
      return (
        <svg {...common}>
          <path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z" />
        </svg>
      )
    case 'stormy': // cloud with a bolt
      return (
        <svg {...common}>
          <path d="M17 15a3.5 3.5 0 0 0-.5-7 5 5 0 0 0-9.6 1.3A3.4 3.4 0 0 0 7 15" />
          <path d="M12 13l-2 4h3l-1.5 4" />
        </svg>
      )
    case 'tender': // a small sprout
      return (
        <svg {...common}>
          <path d="M12 21v-8" />
          <path d="M12 13c0-3-2.5-5-5.5-5 0 3 2.5 5 5.5 5z" />
          <path d="M12 13c0-3 2.5-5 5.5-5 0 3-2.5 5-5.5 5z" />
        </svg>
      )
    default:
      return null
  }
}

export default function WeekMood({ week }: { week: number }) {
  const { lang, entries, setWeekMood } = useApp()
  const current = entries.weekMood?.[week]

  return (
    <div>
      <p className="mb-2 font-head text-[15px] font-semibold text-ceria-dark">
        {lang === 'en' ? 'How did this week feel?' : 'Bagaimana rasanya minggu ini?'}
      </p>
      <div className="flex flex-wrap gap-2">
        {MOODS.map((m) => {
          const active = current === m.key
          return (
            <button
              key={m.key}
              aria-pressed={active}
              onClick={() => setWeekMood(week, active ? null : m.key)}
              className={`flex min-w-[64px] flex-1 flex-col items-center gap-1 rounded-2xl px-2 py-2.5 text-[11px] font-medium transition active:scale-[0.97] ${
                active
                  ? 'bg-ceria-teal text-white shadow-card'
                  : 'bg-white text-ceria-gray shadow-card'
              }`}
            >
              <MoodGlyph mood={m.key} active={active} />
              {lang === 'en' ? m.en : m.id}
            </button>
          )
        })}
      </div>
      <p className="mt-2 text-[11px] text-ceria-gray/80">
        {lang === 'en'
          ? 'No week is a failing week. This is just weather.'
          : 'Tidak ada minggu yang gagal. Ini hanya cuaca.'}
      </p>
    </div>
  )
}
