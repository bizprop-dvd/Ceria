import { createContext, useCallback, useContext, useState, type ReactNode } from 'react'
import { useApp } from '../store/AppContext'
import { isNative } from '../lib/purchases'
import { paywallCopy } from '../lib/freemium'
import Sheet from './Sheet'
import { HeartIcon, LockIcon, SparkIcon } from './icons'

interface PaywallContextValue {
  openPaywall: () => void
}
const PaywallContext = createContext<PaywallContextValue | null>(null)

type Status =
  | { kind: 'idle' }
  | { kind: 'working'; label: string }
  | { kind: 'error'; message: string }
  | { kind: 'info'; message: string }

export function PaywallProvider({ children }: { children: ReactNode }) {
  const { lang, hasPurchased, unlockPrice, purchase, restore } = useApp()
  const [open, setOpen] = useState(false)
  const [status, setStatus] = useState<Status>({ kind: 'idle' })
  const c = paywallCopy[lang]

  const openPaywall = useCallback(() => {
    setStatus({ kind: 'idle' })
    setOpen(true)
  }, [])
  const close = useCallback(() => setOpen(false), [])

  const onPurchase = async () => {
    setStatus({ kind: 'working', label: c.purchasing })
    const res = await purchase()
    if (res.unlocked) {
      setOpen(false)
      setStatus({ kind: 'idle' })
    } else if (res.cancelled) {
      setStatus({ kind: 'idle' })
    } else {
      setStatus({ kind: 'error', message: res.error ?? c.purchaseFailed })
    }
  }

  const onRestore = async () => {
    setStatus({ kind: 'working', label: c.restoring })
    const res = await restore()
    if (res.unlocked) {
      setOpen(false)
      setStatus({ kind: 'idle' })
    } else {
      setStatus({ kind: 'info', message: res.error ?? c.restoredNothing })
    }
  }

  const working = status.kind === 'working'

  return (
    <PaywallContext.Provider value={{ openPaywall }}>
      {children}
      <Sheet open={open} onClose={close} labelledBy="paywall-title">
        <div className="text-center">
          <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-full bg-ceria-pink/10 text-ceria-pink">
            <SparkIcon width={28} height={28} />
          </div>
          <h2 id="paywall-title" className="font-head text-2xl font-semibold text-ceria-blue">
            {c.title}
          </h2>
          <p className="mt-2 text-[15px] leading-relaxed text-ceria-dark/80">{c.body}</p>

          {/* Transparency — a yayasan, stated plainly. No dark patterns. */}
          <div className="mt-4 flex items-start gap-2 rounded-2xl bg-ceria-teal/8 px-4 py-3 text-left">
            <HeartIcon width={20} height={20} className="mt-0.5 shrink-0 text-ceria-teal" />
            <p className="text-[13px] leading-relaxed text-ceria-dark/75">{c.transparency}</p>
          </div>

          {status.kind === 'error' && (
            <p className="mt-3 text-sm text-ceria-pink">{status.message}</p>
          )}
          {status.kind === 'info' && (
            <p className="mt-3 text-sm text-ceria-gray">{status.message}</p>
          )}

          <div className="mt-5 space-y-2">
            <button className="btn-primary w-full" onClick={onPurchase} disabled={working || hasPurchased}>
              <LockIcon width={18} height={18} />
              {working && status.label === c.purchasing ? c.purchasing : c.cta}
              {unlockPrice ? <span className="opacity-90">· {unlockPrice}</span> : null}
            </button>
            <button className="btn-ghost w-full" onClick={onRestore} disabled={working}>
              {working && status.label === c.restoring ? c.restoring : c.restore}
            </button>
            <button className="btn-ghost w-full text-ceria-gray" onClick={close} disabled={working}>
              {c.maybeLater}
            </button>
          </div>

          {!isNative() && (
            <p className="mt-3 text-[11px] text-ceria-gray/70">
              Dev build · store checkout is mocked in the browser
            </p>
          )}
        </div>
      </Sheet>
    </PaywallContext.Provider>
  )
}

// eslint-disable-next-line react-refresh/only-export-components
export function usePaywall(): PaywallContextValue {
  const ctx = useContext(PaywallContext)
  if (!ctx) throw new Error('usePaywall must be used within PaywallProvider')
  return ctx
}
