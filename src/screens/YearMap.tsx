import { useNavigate } from 'react-router-dom'
import Screen from '../components/Screen'
import { daily, chapterName } from '../data/content'
import { useApp } from '../store/AppContext'
import { usePaywall } from '../components/PaywallProvider'
import { isUnlocked } from '../lib/freemium'
import { chapterTheme } from '../lib/chapterTheme'
import { LockIcon } from '../components/icons'

/**
 * The year at a glance: 365 dots in twelve colour bands, filled as days are
 * completed. This is the progress artefact — the screen worth screenshotting.
 */
export default function YearMap() {
  const { lang, t, hasPurchased, entries, daysReadCount } = useApp()
  const { openPaywall } = usePaywall()
  const navigate = useNavigate()
  const read = entries.daysRead ?? {}

  const pct = Math.round((daysReadCount / daily.meta.totalDays) * 100)

  return (
    <Screen
      back
      title={lang === 'en' ? 'Your year' : 'Tahun Anda'}
      subtitle={
        lang === 'en'
          ? `${daysReadCount} of ${daily.meta.totalDays} days`
          : `${daysReadCount} dari ${daily.meta.totalDays} hari`
      }
    >
      <div className="mx-auto max-w-prose pt-2">
        {/* Headline number — gentle, never a scold */}
        <div className="card flex items-center gap-4 p-4">
          <ProgressRing pct={pct} />
          <div className="min-w-0">
            <p className="font-head text-lg font-semibold text-ceria-dark">
              {daysReadCount === 0
                ? lang === 'en'
                  ? 'The year is ahead of you'
                  : 'Satu tahun perjalanan ada di depan Anda'
                : lang === 'en'
                  ? `${daysReadCount} days walked`
                  : `${daysReadCount} hari telah dijalani`}
            </p>
            <p className="mt-0.5 text-sm text-ceria-gray">
              {lang === 'en'
                ? 'There is no wrong pace. Skipped days stay open.'
                : 'Tidak ada ritme yang keliru. Hari yang terlewat tetap dapat dilanjutkan.'}
            </p>
          </div>
        </div>

        {/* Twelve bands */}
        <div className="mt-5 space-y-5">
          {daily.chapters.map((ch) => {
            const theme = chapterTheme(ch.number)
            const name = chapterName(ch.number)
            const unlocked = isUnlocked(ch.number, hasPurchased)
            const days = daily.days.filter((d) => d.chapter === ch.number)
            const doneInCh = days.filter((d) => read[d.day]).length

            return (
              <section key={ch.number}>
                <div className="mb-2 flex items-baseline gap-2">
                  <span
                    className="h-2.5 w-2.5 shrink-0 rounded-full"
                    style={{ background: theme.ring }}
                    aria-hidden
                  />
                  <h2
                    className="font-head text-[15px] font-semibold"
                    style={{ color: theme.base }}
                  >
                    {name ? t(name) : `Chapter ${ch.number}`}
                  </h2>
                  {!unlocked && (
                    <LockIcon width={13} height={13} className="shrink-0 text-ceria-gray" />
                  )}
                  <span className="ml-auto text-[11px] tabular-nums text-ceria-gray">
                    {doneInCh}/{days.length}
                  </span>
                </div>

                <div className="flex flex-wrap gap-[5px]">
                  {days.map((d) => {
                    const done = Boolean(read[d.day])
                    const authored = !d.draft
                    const tappable = unlocked && authored
                    return (
                      <button
                        key={d.day}
                        aria-label={`${lang === 'en' ? 'Day' : 'Hari'} ${d.day}`}
                        title={`${lang === 'en' ? 'Day' : 'Hari'} ${d.day}`}
                        disabled={!authored && unlocked}
                        onClick={() =>
                          tappable ? navigate(`/guidebook/day/${d.day}`) : openPaywall()
                        }
                        className="h-[13px] w-[13px] rounded-full transition active:scale-90 disabled:active:scale-100"
                        style={{
                          background: done ? theme.ring : 'transparent',
                          border: done ? 'none' : `1.5px solid ${theme.ring}`,
                          opacity: done ? 1 : authored && unlocked ? 0.45 : 0.18,
                        }}
                      />
                    )
                  })}
                </div>
              </section>
            )
          })}
        </div>

        <p className="mt-6 text-center text-[12px] text-ceria-gray/80">
          {lang === 'en'
            ? 'Faded dots are days still being written.'
            : 'Titik yang tampak samar menandai hari yang masih menunggu untuk dituliskan.'}
        </p>
      </div>
    </Screen>
  )
}

function ProgressRing({ pct }: { pct: number }) {
  const size = 60
  const stroke = 6
  const r = (size - stroke) / 2
  const c = 2 * Math.PI * r
  return (
    <svg width={size} height={size} className="shrink-0" role="img" aria-label={`${pct}%`}>
      <circle
        cx={size / 2}
        cy={size / 2}
        r={r}
        fill="none"
        stroke="#F2E9D9"
        strokeWidth={stroke}
      />
      <circle
        cx={size / 2}
        cy={size / 2}
        r={r}
        fill="none"
        stroke="#0E9488"
        strokeWidth={stroke}
        strokeLinecap="round"
        strokeDasharray={c}
        strokeDashoffset={c - (c * pct) / 100}
        transform={`rotate(-90 ${size / 2} ${size / 2})`}
      />
      <text
        x="50%"
        y="50%"
        textAnchor="middle"
        dominantBaseline="central"
        className="fill-ceria-dark font-semibold"
        style={{ fontSize: 15 }}
      >
        {pct}%
      </text>
    </svg>
  )
}
