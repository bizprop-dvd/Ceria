import { useNavigate } from 'react-router-dom'
import Screen from '../components/Screen'
import LockBadge from '../components/LockBadge'
import { ChevronRight, LockIcon } from '../components/icons'
import { guidebook } from '../data/content'
import { useApp } from '../store/AppContext'
import { usePaywall } from '../components/PaywallProvider'
import { isUnlocked } from '../lib/freemium'

export default function Guidebook() {
  const { t, lang, hasPurchased } = useApp()
  const { openPaywall } = usePaywall()
  const navigate = useNavigate()

  return (
    <Screen
      title={lang === 'en' ? 'Guidebook' : 'Panduan'}
      subtitle={lang === 'en' ? '12 chapters' : '12 bab'}
    >
      <ul className="mt-1 space-y-2.5">
        {guidebook.chapters.map((ch) => {
          const unlocked = isUnlocked(ch.number, hasPurchased)
          return (
            <li key={ch.number}>
              <button
                onClick={() => (unlocked ? navigate(`/guidebook/${ch.number}`) : openPaywall())}
                className="card flex w-full items-center gap-3 p-4 text-left active:scale-[0.99] transition"
              >
                <span
                  className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-xl font-head text-lg font-semibold ${
                    unlocked ? 'bg-ceria-blue/8 text-ceria-blue' : 'bg-ceria-cream-deep text-ceria-gray'
                  }`}
                >
                  {ch.number}
                </span>
                <div className="min-w-0 flex-1">
                  <p className="font-head text-[15px] font-semibold text-ceria-dark truncate">
                    {t(ch.title)}
                  </p>
                  <p className="mt-0.5 text-xs text-ceria-gray line-clamp-2">{t(ch.principle)}</p>
                </div>
                {unlocked ? (
                  <ChevronRight className="shrink-0 text-ceria-gray" />
                ) : (
                  <LockBadge />
                )}
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
