import { NavLink } from 'react-router-dom'
import { useApp } from '../store/AppContext'
import { useNews } from '../store/NewsContext'
import { BookIcon, DiaryIcon, MoreIcon, NewsIcon, SunIcon, ToolIcon } from './icons'
import type { ComponentType, SVGProps } from 'react'

interface Tab {
  to: string
  icon: ComponentType<SVGProps<SVGSVGElement>>
  label: { en: string; id: string }
}

const TABS: Tab[] = [
  { to: '/today', icon: SunIcon, label: { en: 'Today', id: 'Hari Ini' } },
  { to: '/guidebook', icon: BookIcon, label: { en: 'Guide', id: 'Panduan' } },
  { to: '/toolkit', icon: ToolIcon, label: { en: 'Toolkit', id: 'Alat' } },
  { to: '/diary', icon: DiaryIcon, label: { en: 'Diary', id: 'Diari' } },
  { to: '/news', icon: NewsIcon, label: { en: 'News', id: 'Kabar' } },
  { to: '/more', icon: MoreIcon, label: { en: 'More', id: 'Lainnya' } },
]

/**
 * Floating glass tab bar.
 *
 * Sits above the content on a translucent, heavily blurred pill rather than a
 * flat opaque strip — closer to the frosted-glass bars in current phone OS
 * design. The active tab gets its own lighter glass capsule.
 *
 * Content scrolls underneath, so every scrollable screen leaves bottom padding
 * (see Screen.tsx) to keep the last element clear of the bar.
 */
export default function TabBar() {
  const { lang } = useApp()
  const { unread } = useNews()
  return (
    <nav
      className="pointer-events-none absolute inset-x-0 bottom-0 z-30"
      style={{ paddingBottom: 'calc(var(--safe-bottom) + 0.5rem)' }}
    >
      <div className="mx-auto max-w-md px-3">
        <ul
          className="pointer-events-auto flex items-center gap-0.5 rounded-[26px] border border-white/60 p-1.5"
          style={{
            background: 'rgba(255, 253, 250, 0.72)',
            backdropFilter: 'blur(22px) saturate(180%)',
            WebkitBackdropFilter: 'blur(22px) saturate(180%)',
            boxShadow:
              '0 8px 28px rgba(31,41,55,0.13), 0 1px 0 rgba(255,255,255,0.85) inset',
          }}
        >
          {TABS.map(({ to, icon: Icon, label }) => (
            <li key={to} className="flex-1">
              <NavLink
                to={to}
                className={({ isActive }) =>
                  `relative flex flex-col items-center gap-0.5 rounded-[20px] px-0.5 py-2 text-[10px] font-medium whitespace-nowrap transition-all duration-200 ${
                    isActive ? 'text-ceria-blue' : 'text-ceria-gray/80'
                  }`
                }
                style={({ isActive }) =>
                  isActive
                    ? {
                        background: 'rgba(255,255,255,0.9)',
                        boxShadow:
                          '0 2px 8px rgba(46,79,163,0.14), 0 1px 0 rgba(255,255,255,0.9) inset',
                      }
                    : undefined
                }
              >
                {({ isActive }) => (
                  <>
                    <span className="relative">
                      <Icon width={22} height={22} strokeWidth={isActive ? 2.1 : 1.7} />
                      {/* Something from Ceria that has not been looked at. A quiet
                          dot rather than a count: it is an invitation, not a chore. */}
                      {to === '/news' && unread > 0 && (
                        <span
                          className="absolute -right-0.5 -top-0.5 h-2 w-2 rounded-full bg-ceria-pink ring-2 ring-white"
                          aria-label={lang === 'en' ? 'New posts' : 'Ada kabar baru'}
                          role="status"
                        />
                      )}
                    </span>
                    {label[lang]}
                  </>
                )}
              </NavLink>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  )
}
