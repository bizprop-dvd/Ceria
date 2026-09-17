import { useEffect, type ReactNode } from 'react'

interface SheetProps {
  open: boolean
  onClose: () => void
  children: ReactNode
  labelledBy?: string
}

/** A calm bottom sheet modal with a scrim. Closes on scrim tap / Escape. */
export default function Sheet({ open, onClose, children, labelledBy }: SheetProps) {
  useEffect(() => {
    if (!open) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose()
    }
    document.addEventListener('keydown', onKey)
    document.body.style.overflow = 'hidden'
    return () => {
      document.removeEventListener('keydown', onKey)
      document.body.style.overflow = ''
    }
  }, [open, onClose])

  if (!open) return null

  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center">
      <div
        className="absolute inset-0 bg-ceria-dark/40 animate-[fadeIn_.2s_ease]"
        onClick={onClose}
        aria-hidden
      />
      <div
        role="dialog"
        aria-modal="true"
        aria-labelledby={labelledBy}
        className="relative w-full max-w-md bg-ceria-cream rounded-t-3xl shadow-sheet
          px-5 pt-3 pb-[calc(1.25rem+var(--safe-bottom))] animate-[slideUp_.28s_cubic-bezier(0.2,0.8,0.2,1)]"
      >
        <div className="mx-auto mb-3 h-1.5 w-10 rounded-full bg-ceria-cream-deep" />
        {children}
      </div>
      <style>{`
        @keyframes fadeIn { from { opacity: 0 } to { opacity: 1 } }
        @keyframes slideUp { from { transform: translateY(100%) } to { transform: translateY(0) } }
      `}</style>
    </div>
  )
}
