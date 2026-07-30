import { NavLink } from 'react-router-dom'
import { useApp } from '../store/AppContext'
import { BookIcon, DiaryIcon, MoreIcon, SunIcon, ToolIcon } from './icons'
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
  { to: '/more', icon: MoreIcon, label: { en: 'More', id: 'Lainnya' } },
]

export default function TabBar() {
  const { lang } = useApp()
  return (
    <nav
      className="shrink-0 border-t border-ceria-cream-deep bg-ceria-cream/95 backdrop-blur"
      style={{ paddingBottom: 'var(--safe-bottom)' }}
    >
      <ul className="mx-auto flex max-w-md">
        {TABS.map(({ to, icon: Icon, label }) => (
          <li key={to} className="flex-1">
            <NavLink
              to={to}
              className={({ isActive }) =>
                `flex flex-col items-center gap-0.5 py-2 text-[11px] font-medium transition ${
                  isActive ? 'text-ceria-blue' : 'text-ceria-gray'
                }`
              }
            >
              {({ isActive }) => (
                <>
                  <Icon
                    width={24}
                    height={24}
                    strokeWidth={isActive ? 2.1 : 1.7}
                  />
                  {label[lang]}
                </>
              )}
            </NavLink>
          </li>
        ))}
      </ul>
    </nav>
  )
}
