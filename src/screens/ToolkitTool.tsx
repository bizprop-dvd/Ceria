import { useEffect, useMemo, useRef, useState } from 'react'
import { Navigate, useParams } from 'react-router-dom'
import Screen from '../components/Screen'
import ProvisionalNote from '../components/ProvisionalNote'
import { toolByNumber } from '../data/content'
import { useApp } from '../store/AppContext'
import { isUnlocked } from '../lib/freemium'
import type { Bilingual, ToolkitField } from '../data/types'

const MONTHS = {
  en: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  id: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
}

const WEEKDAYS = {
  en: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  id: ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min'],
}

/** Instance 1 -> Year 1 Part 1, 2 -> Year 1 Part 2, 3 -> Year 2 Part 1, … */
function periodLabel(id: number, partsPerYear: number, lang: 'en' | 'id'): string {
  const year = Math.floor((id - 1) / partsPerYear) + 1
  const part = ((id - 1) % partsPerYear) + 1
  return lang === 'en' ? `Year ${year} · Part ${part}` : `Tahun ${year} · Bagian ${part}`
}

/** Mon=1 … Sun=7, matching the tab ids. */
function todayWeekday(): number {
  const js = new Date().getDay() // Sun=0
  return js === 0 ? 7 : js
}

export default function ToolkitTool() {
  const { n } = useParams()
  const {
    t,
    lang,
    hasPurchased,
    entries,
    setToolField,
    addChild,
    addToolPeriod,
    removeChild,
    setChildName,
  } = useApp()
  const num = Number(n)
  const tool = toolByNumber(num)
  const kind = tool?.repeat?.kind

  // Month sheets open on the current month, weekday sheets on today.
  const [instance, setInstance] = useState(() =>
    kind === 'month' ? new Date().getMonth() + 1 : kind === 'weekday' ? todayWeekday() : 1,
  )

  const children = useMemo(() => entries.children ?? [], [entries.children])

  // A per-child tool always needs at least one sheet to write on.
  useEffect(() => {
    if (kind === 'child' && children.length === 0) setInstance(addChild())
  }, [kind, children.length, addChild])

  if (!tool) return <Navigate to="/toolkit" replace />
  if (!isUnlocked(tool.chapter, hasPurchased)) return <Navigate to="/toolkit" replace />

  const repeats = Boolean(tool.repeat)
  const saved = repeats
    ? (entries.toolInstances?.[`${num}:${instance}`] ?? [])
    : (entries.tools[num] ?? [])
  const summarySaved = entries.tools[num] ?? []

  const onChange = (i: number, value: string) =>
    repeats ? setToolField(num, i, value, instance) : setToolField(num, i, value)

  const filled = (id: number) =>
    (entries.toolInstances?.[`${num}:${id}`] ?? []).some((v) => (v ?? '').trim() !== '')

  const activeChild = children.find((c) => c.id === instance) ?? children[0]
  const periodCount = entries.toolPeriodCount?.[num] ?? 1
  // The previous part's answers, shown faded behind the empty fields so a
  // parent can see what they wrote last time without it being pre-filled.
  const shadow =
    kind === 'period' && instance > 1
      ? (entries.toolInstances?.[`${num}:${instance - 1}`] ?? [])
      : []

  const tabItems =
    kind === 'month'
      ? Array.from({ length: (tool.repeat as { count: number }).count ?? 12 }, (_, i) => ({
          id: i + 1,
          label: MONTHS[lang][i],
        }))
      : kind === 'weekday'
        ? WEEKDAYS[lang].map((label, i) => ({ id: i + 1, label }))
        : kind === 'period'
          ? Array.from({ length: periodCount }, (_, i) => ({
              id: i + 1,
              label: periodLabel(i + 1, (tool.repeat as { partsPerYear: number }).partsPerYear, lang),
            }))
        : children.map((c, i) => ({
            id: c.id,
            label: firstName(c.name) || (lang === 'en' ? `Child ${i + 1}` : `Anak ${i + 1}`),
          }))

  const onAddChild = () => setInstance(addChild())
  const onRemoveChild = () => {
    const remaining = children.filter((c) => c.id !== instance)
    removeChild(instance)
    setInstance(remaining[0]?.id ?? 1)
  }

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
              <Tabs
                label={
                  kind === 'month'
                    ? lang === 'en'
                      ? 'Month'
                      : 'Bulan'
                    : kind === 'weekday'
                      ? lang === 'en'
                        ? 'Day'
                        : 'Hari'
                      : kind === 'period'
                        ? lang === 'en'
                          ? 'Review'
                          : 'Tinjauan'
                        : lang === 'en'
                          ? 'Child'
                          : 'Anak'
                }
                items={tabItems}
                value={instance}
                onChange={setInstance}
                dot={filled}
                onAdd={
                  kind === 'child'
                    ? onAddChild
                    : kind === 'period'
                      ? () => setInstance(addToolPeriod(num))
                      : undefined
                }
                addLabel={
                  kind === 'child'
                    ? lang === 'en'
                      ? 'Add a child'
                      : 'Tambah anak'
                    : lang === 'en'
                      ? 'Add the next part'
                      : 'Tambah bagian berikutnya'
                }
              />
            )}

            {/* The child's name — shared across every per-child tool */}
            {kind === 'child' && activeChild && (
              <div className="mt-4">
                <label className="mb-1.5 block font-head text-[15px] font-semibold text-ceria-dark">
                  {t((tool.repeat as { nameLabel: Bilingual }).nameLabel)}
                </label>
                <input
                  type="text"
                  className="field"
                  value={activeChild.name}
                  placeholder={lang === 'en' ? 'e.g. Bagas' : 'mis. Bagas'}
                  onChange={(e) => setChildName(activeChild.id, e.target.value)}
                />
                <p className="mt-1.5 text-[11px] text-ceria-gray/80">
                  {lang === 'en'
                    ? 'Children you add here appear on every tool that works child by child.'
                    : 'Anak yang Anda tambahkan di sini muncul di setiap alat yang bekerja per anak.'}
                </p>
              </div>
            )}

            <FieldList
              fields={tool.fields}
              values={saved}
              onChange={onChange}
              keyPrefix={String(instance)}
              shadow={shadow}
              shadowNote={
                lang === 'en'
                  ? `From ${periodLabel(instance - 1, (tool.repeat as { partsPerYear: number })?.partsPerYear ?? 2, lang)}`
                  : `Dari ${periodLabel(instance - 1, (tool.repeat as { partsPerYear: number })?.partsPerYear ?? 2, lang)}`
              }
            />

            {/* Asked once for the whole tool, not per tab */}
            {tool.summaryFields && tool.summaryFields.length > 0 && (
              <div className="mt-6 border-t border-ceria-cream-deep pt-5">
                <FieldList
                  fields={tool.summaryFields}
                  values={summarySaved}
                  onChange={(i, v) => setToolField(num, i, v)}
                  keyPrefix="summary"
                />
              </div>
            )}

            {kind === 'child' && children.length > 1 && (
              <button
                onClick={onRemoveChild}
                className="btn-ghost mt-4 w-full text-sm text-ceria-pink"
              >
                {lang === 'en'
                  ? `Remove ${firstName(activeChild?.name ?? '') || 'this child'} from all tools`
                  : `Hapus ${firstName(activeChild?.name ?? '') || 'anak ini'} dari semua alat`}
              </button>
            )}

            <p className="mt-4 text-center text-xs text-ceria-gray/80">
              {kind === 'month'
                ? lang === 'en'
                  ? 'Each month is saved separately on this device.'
                  : 'Setiap bulan tersimpan terpisah di perangkat ini.'
                : kind === 'weekday'
                  ? lang === 'en'
                    ? 'Each day is saved separately on this device.'
                    : 'Setiap hari tersimpan terpisah di perangkat ini.'
                  : kind === 'child'
                    ? lang === 'en'
                      ? 'Each child has their own sheet, saved on this device.'
                      : 'Setiap anak punya lembarnya sendiri, tersimpan di perangkat ini.'
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

function FieldList({
  fields,
  values,
  onChange,
  keyPrefix,
  shadow = [],
  shadowNote,
}: {
  fields: ToolkitField[]
  values: string[]
  onChange: (index: number, value: string) => void
  keyPrefix: string
  /** the previous part's answers, shown faded for comparison */
  shadow?: string[]
  shadowNote?: string
}) {
  const { t } = useApp()
  return (
    <div className="mt-5 space-y-4">
      {fields.map((field, i) => (
        <div key={`${keyPrefix}-${i}`}>
          <label className="mb-1.5 block font-head text-[15px] font-semibold text-ceria-dark">
            {t(field.label)}
          </label>
          {field.type === 'text' ? (
            <input
              type="text"
              className="field"
              value={values[i] ?? ''}
              onChange={(e) => onChange(i, e.target.value)}
            />
          ) : (
            <textarea
              className="field resize-none"
              rows={4}
              value={values[i] ?? ''}
              onChange={(e) => onChange(i, e.target.value)}
            />
          )}
          {(shadow[i] ?? '').trim() !== '' && (
            <div className="mt-1.5 rounded-xl border border-dashed border-ceria-cream-deep bg-ceria-cream-deep/25 px-3 py-2">
              {shadowNote && (
                <p className="text-[10px] uppercase tracking-[0.08em] text-ceria-gray/70">
                  {shadowNote}
                </p>
              )}
              <p className="mt-0.5 whitespace-pre-line text-[13px] leading-relaxed text-ceria-gray/70">
                {shadow[i]}
              </p>
            </div>
          )}
        </div>
      ))}
    </div>
  )
}

/** The word a tab shows — parents often type a full name. */
function firstName(name: string): string {
  return name.trim().split(/\s+/)[0] ?? ''
}

/** A scrollable tab strip, optionally with an add button at the end. */
function Tabs({
  label,
  items,
  value,
  onChange,
  dot,
  onAdd,
  addLabel,
}: {
  label: string
  items: { id: number; label: string }[]
  value: number
  onChange: (id: number) => void
  dot?: (id: number) => boolean
  onAdd?: () => void
  addLabel?: string
}) {
  const activeRef = useRef<HTMLButtonElement>(null)
  useEffect(() => {
    activeRef.current?.scrollIntoView({ block: 'nearest', inline: 'center' })
  }, [value])

  return (
    <div className="mt-5">
      <p className="mb-1.5 text-[11px] font-semibold uppercase tracking-[0.08em] text-ceria-gray">
        {label}
      </p>
      <div className="no-scrollbar -mx-4 flex items-center gap-1.5 overflow-x-auto px-4 pb-1">
        {items.map((it) => {
          const active = it.id === value
          return (
            <button
              key={it.id}
              ref={active ? activeRef : undefined}
              onClick={() => onChange(it.id)}
              aria-pressed={active}
              className={`relative max-w-[9rem] shrink-0 truncate rounded-full px-3.5 py-1.5 text-[13px] font-medium transition ${
                active
                  ? 'bg-ceria-pink text-white shadow-card'
                  : 'bg-white text-ceria-gray shadow-card'
              }`}
            >
              {it.label}
              {dot?.(it.id) && !active && (
                <span
                  aria-hidden
                  className="absolute right-1.5 top-1.5 h-1.5 w-1.5 rounded-full bg-ceria-teal"
                />
              )}
            </button>
          )
        })}
        {onAdd && (
          <button
            onClick={onAdd}
            aria-label={addLabel}
            title={addLabel}
            className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-dashed border-ceria-pink/40 text-ceria-pink transition active:scale-95"
          >
            <svg
              width={17}
              height={17}
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth={2}
              strokeLinecap="round"
            >
              <path d="M12 5v14M5 12h14" />
            </svg>
          </button>
        )}
      </div>
    </div>
  )
}
