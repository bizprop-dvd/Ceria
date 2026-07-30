import { useNavigate } from 'react-router-dom'
import type { ReactNode } from 'react'
import { ChevronLeft } from './icons'

interface ScreenProps {
  title?: string
  subtitle?: string
  back?: boolean
  right?: ReactNode
  children: ReactNode
  /** removes default horizontal padding for edge-to-edge content */
  flush?: boolean
}

/** Standard screen chrome: safe-area-aware header + scrollable body. */
export default function Screen({ title, subtitle, back, right, children, flush }: ScreenProps) {
  const navigate = useNavigate()
  return (
    <div className="flex h-full flex-col">
      {(title || back) && (
        <header
          className="sticky top-0 z-10 bg-ceria-cream/90 backdrop-blur border-b border-ceria-cream-deep"
          style={{ paddingTop: 'var(--safe-top)' }}
        >
          <div className="flex items-center gap-2 px-4 py-3">
            {back && (
              <button
                aria-label="Back"
                onClick={() => navigate(-1)}
                className="-ml-1 flex h-9 w-9 items-center justify-center rounded-full text-ceria-blue active:bg-ceria-cream-deep"
              >
                <ChevronLeft width={22} height={22} />
              </button>
            )}
            <div className="min-w-0 flex-1">
              {title && (
                <h1 className="font-head text-xl font-semibold text-ceria-blue truncate">{title}</h1>
              )}
              {subtitle && <p className="text-xs text-ceria-gray truncate">{subtitle}</p>}
            </div>
            {right}
          </div>
        </header>
      )}
      <main className={`no-scrollbar flex-1 overflow-y-auto ${flush ? '' : 'px-4'} pb-6`}>
        {children}
      </main>
    </div>
  )
}
