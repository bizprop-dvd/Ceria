import { daily } from '../data/content'
import { useApp } from '../store/AppContext'
import { dayKey, parseDayKey } from '../lib/dates'

/**
 * The week as a 7-segment ring, one segment per day, filled from diary
 * entries. Gentle by design: empty segments are simply unfilled, never red.
 * The current weekly exercise sits beside it when one is authored.
 */
export default function WeekRing({ week }: { week: number }) {
  const { lang, t, settings, daysWithEntries } = useApp()

  // The 7 local dates of this diary week, derived from the start date.
  const start = parseDayKey(settings.startDate)
  const first = new Date(start)
  first.setDate(first.getDate() + (week - 1) * 7)
  const days: { key: string; done: boolean; isToday: boolean }[] = []
  const todayKey = dayKey()
  for (let i = 0; i < 7; i++) {
    const d = new Date(first)
    d.setDate(d.getDate() + i)
    const key = dayKey(d)
    days.push({ key, done: daysWithEntries.has(key), isToday: key === todayKey })
  }
  const doneCount = days.filter((d) => d.done).length

  const exercise = daily.weeklyExercises.find((w) => w.n === week)
  const exerciseText = exercise ? t(exercise.text) : ''

  return (
    <div className="card flex items-center gap-4 p-4">
      <Ring days={days} />
      <div className="min-w-0 flex-1">
        <p className="font-head text-[15px] font-semibold text-ceria-dark">
          {lang === 'en' ? `Week ${week}` : `Minggu ${week}`}
          <span className="ml-2 text-[12px] font-normal tabular-nums text-ceria-gray">
            {doneCount}/7
          </span>
        </p>
        {exerciseText ? (
          <p className="mt-0.5 text-[13px] leading-snug text-ceria-gray line-clamp-3">
            {exerciseText}
          </p>
        ) : (
          <p className="mt-0.5 text-[13px] text-ceria-gray">
            {lang === 'en'
              ? 'A few lines a day is the whole practice.'
              : 'Beberapa baris sehari — itulah seluruh latihannya.'}
          </p>
        )}
      </div>
    </div>
  )
}

function Ring({ days }: { days: { done: boolean; isToday: boolean }[] }) {
  const size = 64
  const stroke = 7
  const r = (size - stroke) / 2
  const c = 2 * Math.PI * r
  const seg = c / 7
  const gap = 3
  return (
    <svg width={size} height={size} className="shrink-0 -rotate-90" aria-hidden>
      {days.map((d, i) => (
        <circle
          key={i}
          cx={size / 2}
          cy={size / 2}
          r={r}
          fill="none"
          stroke={d.done ? '#0E9488' : d.isToday ? '#E91E80' : '#F2E9D9'}
          strokeWidth={stroke}
          strokeLinecap="round"
          strokeDasharray={`${seg - gap} ${c - seg + gap}`}
          strokeDashoffset={-i * seg}
          opacity={d.done ? 1 : d.isToday ? 0.55 : 1}
        />
      ))}
    </svg>
  )
}
