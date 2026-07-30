import { Navigate, useParams } from 'react-router-dom'
import Screen from '../components/Screen'
import ProvisionalNote from '../components/ProvisionalNote'
import { toolByNumber } from '../data/content'
import { useApp } from '../store/AppContext'
import { isUnlocked } from '../lib/freemium'

export default function ToolkitTool() {
  const { n } = useParams()
  const { t, lang, hasPurchased, entries, setToolField } = useApp()
  const num = Number(n)
  const tool = toolByNumber(num)

  if (!tool) return <Navigate to="/toolkit" replace />
  if (!isUnlocked(tool.chapter, hasPurchased)) return <Navigate to="/toolkit" replace />

  const saved = entries.tools[num] ?? []

  return (
    <Screen back title={t(tool.title)} subtitle={lang === 'en' ? `Tool ${tool.number}` : `Alat ${tool.number}`}>
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
            <div className="mt-5 space-y-4">
              {tool.fields.map((field, i) => (
                <div key={i}>
                  <label className="mb-1.5 block font-head text-[15px] font-semibold text-ceria-dark">
                    {t(field.label)}
                  </label>
                  <textarea
                    className="field resize-none"
                    rows={field.type === 'longtext' ? 4 : 2}
                    value={saved[i] ?? ''}
                    onChange={(e) => setToolField(num, i, e.target.value)}
                  />
                </div>
              ))}
            </div>
            <p className="mt-4 text-center text-xs text-ceria-gray/80">
              {lang === 'en'
                ? 'Your answers are saved on this device.'
                : 'Jawaban Anda tersimpan di perangkat ini.'}
            </p>
          </>
        )}
      </div>
    </Screen>
  )
}
