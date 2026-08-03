import { useEffect, useRef, useState } from 'react'
import { Navigate, useParams } from 'react-router-dom'
import Screen from '../components/Screen'
import ProvisionalNote from '../components/ProvisionalNote'
import { toolByNumber } from '../data/content'
import { useApp } from '../store/AppContext'
import { isUnlocked } from '../lib/freemium'

const MONTHS = {
  en: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  id: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
}

export default function ToolkitTool() {
  const { n } = useParams()
  const { t, lang, hasPurchased, entries, setToolField } = useApp()
  const num = Number(n)
  const tool = toolByNumber(num)

  // Repeatable tools open on the current calendar month.
  const [instance, setInstance] = useState(() => new Date().getMonth() + 1)

  if (!tool) return <Navigate to="/toolkit" replace />
  if (!isUnlocked(tool.chapter, hasPurchased)) return <Navigate to="/toolkit" replace />

  const repeats = Boolean(tool.repeat)
  const saved = repeats
    ? (entries.toolInstances?.[`${num}:${instance}`] ?? [])
    : (entries.tools[num] ?? [])

  const onChange = (i: number, value: string) =>
    repeats ? setToolField(num, i, value, instance) : setToolField(num, i, value)

  /** Which instances already have something written — shown as a dot on the tab. */
  const filled = (m: number) =>
    (entries.toolInstances?.[`${num}:${m}`] ?? []).some((v) => (v ?? '').trim() !== '')

  return (
    <Screen
      back
      title={t(tool.title)}
      subtitle={lang === 'en' ? `Tool ${tool.number}` : `Alat ${tool.number}`}
    >
      <div className="mx-auto max-w-prose pt-2">
        <div className="card border-l-4 border-l-ceria-pink p-4">
          <p className="text-xs font-semibold uppercase tracking-wide text-ceria-pink">
            {lang === 'en' ? 'Purpose' : 'Tujuan'}
          </p>
          <p className="mt-1 text-[15px] leading-relaxed text-ceria-dark">{t(tool.purpose)}</p>
        </div>

        {tool._needsFields || !tool.fields ? (
          <ProvisionalNote kind="tool" />
        ) : (
          <>
            {tool.guide && tool.guide[lang].length > 0 && (
              <div className="card mt-4 bg-ceria-cream-deep/40 p-4">
                <ul className="space-y-1.5">
                  {tool.guide[lang].map((line, i) => (
                    <li key={i} className="text-[13px] leading-relaxed text-ceria-dark/80">
                      {line}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {repeats && (
              <MonthTabs
                count={tool.repeat!.count}
                value={instance}
                onChange={setInstance}
                filled={filled}
                lang={lang}
              />
            )}

            <div className="mt-5 space-y-4">
              {tool.fields.map((field, i) => (
                <div key={`${instance}-${i}`}>
                  <label className="mb-1.5 block font-head text-[15px] font-semibold text-ceria-dark">
                    {t(field.label)}
                  </label>
                  <textarea
                    className="field resize-none"
                    rows={field.type === 'longtext' ? 4 : 2}
                    value={saved[i] ?? ''}
                    onChange={(e) => onChange(i, e.target.value)}
                  />
                </div>
              ))}
            </div>

            <p className="mt-4 text-center text-xs text-ceria-gray/80">
              {repeats
                ? lang === 'en'
                  ? 'Each month is saved separately on this device.'
                  : 'Setiap bulan tersimpan terpisah di perangkat ini.'
                : lang === 'en'
                  ? 'Your answers are saved on this device.'
                  : 'Jawaban Anda tersimpan di perangkat ini.'}
            </p>
          </>
        )}
      </div>
    </Screen>
  )
}

/** Twelve month tabs, scrollable, with a dot on months that have entries. */
function MonthTabs({
  count,
  value,
  onChange,
  filled,
  lang,
}: {
  count: number
  value: number
  onChange: (m: number) => void
  filled: (m: number) => boolean
  lang: 'en' | 'id'
}) {
  const scroller = useRef<HTMLDivElement>(null)
  const activeRef = useRef<HTMLButtonElement>(null)

  // Keep the selected month in view when it changes.
  useEffect(() => {
    activeRef.current?.scrollIntoView({ block: 'nearest', inline: 'center' })
  }, [value])

  return (
    <div className="mt-5">
      <p className="mb-1.5 text-[11px] font-semibold uppercase tracking-[0.08em] text-ceria-gray">
        {lang === 'en' ? 'Month' : 'Bulan'}
      </p>
      <div
        ref={scroller}
        className="no-scrollbar -mx-4 flex gap-1.5 overflow-x-auto px-4 pb-1"
      >
        {Array.from({ length: count }, (_, i) => i + 1).map((m) => {
          const active = m === value
          return (
            <button
              key={m}
              ref={active ? activeRef : undefined}
              onClick={() => onChange(m)}
              aria-pressed={active}
              className={`relative shrink-0 rounded-full px-3.5 py-1.5 text-[13px] font-medium transition ${
                active
                  ? 'bg-ceria-pink text-white shadow-card'
                  : 'bg-white text-ceria-gray shadow-card'
              }`}
            >
              {MONTHS[lang][m - 1]}
              {filled(m) && !active && (
                <span
                  aria-hidden
                  className="absolute right-1.5 top-1.5 h-1.5 w-1.5 rounded-full bg-ceria-teal"
                />
              )}
            </button>
          )
        })}
      </div>
    </div>
  )
}
