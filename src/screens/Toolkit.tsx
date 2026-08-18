import { useNavigate } from 'react-router-dom'
import Screen from '../components/Screen'
import LockBadge from '../components/LockBadge'
import { ChevronRight, LockIcon } from '../components/icons'
import { toolkit } from '../data/content'
import { useApp } from '../store/AppContext'
import { usePaywall } from '../components/PaywallProvider'
import { isUnlocked } from '../lib/freemium'

export default function Toolkit() {
  const { t, lang, hasPurchased } = useApp()
  const { openPaywall } = usePaywall()
  const navigate = useNavigate()

  return (
    <Screen
      title={lang === 'en' ? 'Toolkit' : 'Alat'}
      subtitle={lang === 'en' ? '12 tools' : '12 alat'}
    >
      <ul className="mt-1 space-y-2.5">
        {toolkit.tools.map((tool) => {
          const unlocked = isUnlocked(tool.chapter, hasPurchased)
          return (
            <li key={tool.number}>
              <button
                onClick={() => (unlocked ? navigate(`/toolkit/${tool.number}`) : openPaywall())}
                className="card flex w-full items-center gap-3 p-4 text-left active:scale-[0.99] transition"
              >
                <span
                  className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-xl font-head text-lg font-semibold ${
                    unlocked ? 'bg-ceria-pink/8 text-ceria-pink' : 'bg-ceria-cream-deep text-ceria-gray'
                  }`}
                >
                  {tool.number}
                </span>
                <div className="min-w-0 flex-1">
                  <p className="font-head text-[15px] font-semibold text-ceria-dark truncate">
                    {t(tool.title)}
                  </p>
                  <p className="mt-0.5 text-xs text-ceria-gray line-clamp-2">{t(tool.purpose)}</p>
                </div>
                {unlocked ? <ChevronRight className="shrink-0 text-ceria-gray" /> : <LockBadge />}
              </button>
            </li>
          )
        })}
      </ul>

      <p className="mt-4 text-center text-xs text-ceria-gray/80">{t(toolkit.meta.transparencyLine)}</p>

      {!hasPurchased && (
        <button
          onClick={openPaywall}
          className="mt-3 flex w-full items-center justify-center gap-2 rounded-2xl border border-dashed border-ceria-pink/30 px-4 py-3 text-sm font-medium text-ceria-pink"
        >
          <LockIcon width={16} height={16} />
          {lang === 'en' ? 'Unlock tools 5–12' : 'Buka alat 5–12'}
        </button>
      )}
    </Screen>
  )
}
