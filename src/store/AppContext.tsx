import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useRef,
  useState,
  type ReactNode,
} from 'react'
import type { Bilingual, Edition, Lang, Role } from '../data/types'
import { dayKey } from '../lib/dates'
import {
  checkEntitlement,
  configurePurchases,
  getUnlockPrice,
  purchaseUnlock,
  restorePurchases,
  type PurchaseResult,
} from '../lib/purchases'
import { scheduleEveningReminder } from '../lib/notifications'
import { getJSON, KEYS, setJSON } from '../lib/storage'
import { computeStreak } from '../lib/streak'
import {
  DEFAULT_REMINDER,
  emptyEntries,
  type EntriesState,
  type Settings,
} from './types'

const DEFAULT_SETTINGS: Settings = {
  onboarded: false,
  lang: 'en',
  edition: 'combined',
  startDate: dayKey(),
  reminderTime: null,
}

interface AppContextValue {
  ready: boolean
  settings: Settings
  entries: EntriesState
  hasPurchased: boolean
  unlockPrice: string | null

  lang: Lang
  edition: Edition
  roles: Role[]
  t: (b: Bilingual | undefined) => string

  setLang: (lang: Lang) => void
  setEdition: (edition: Edition) => void
  updateSettings: (patch: Partial<Settings>) => void
  completeOnboarding: (patch: Partial<Settings>) => void

  setDailyAnswer: (day: string, role: Role, index: number, value: string) => void
  setWeekIntent: (week: number, role: Role, value: string) => void
  setSunday: (week: number, role: Role, value: string) => void
  setDebrief: (week: number, role: Role, index: number, value: string) => void
  setToolField: (tool: number, index: number, value: string) => void
  toggleDayRead: (day: number) => void
  setWeekPhoto: (week: number, dataUri: string | null) => void
  setWeekMood: (week: number, mood: string | null) => void
  daysReadCount: number

  daysWithEntries: Set<string>
  streak: number

  refreshPurchase: () => Promise<void>
  purchase: () => Promise<PurchaseResult>
  restore: () => Promise<PurchaseResult>
}

const AppContext = createContext<AppContextValue | null>(null)

export function AppProvider({ children }: { children: ReactNode }) {
  const [ready, setReady] = useState(false)
  const [settings, setSettings] = useState<Settings>(DEFAULT_SETTINGS)
  const [entries, setEntries] = useState<EntriesState>(emptyEntries())
  const [hasPurchased, setHasPurchased] = useState(false)
  const [unlockPrice, setUnlockPrice] = useState<string | null>(null)

  // ---- initial load ----
  useEffect(() => {
    let cancelled = false
    ;(async () => {
      const [s, e] = await Promise.all([
        getJSON<Settings>(KEYS.settings, DEFAULT_SETTINGS),
        getJSON<EntriesState>(KEYS.entries, emptyEntries()),
      ])
      if (cancelled) return
      setSettings({ ...DEFAULT_SETTINGS, ...s })
      setEntries({ ...emptyEntries(), ...e })
      setReady(true)

      // Purchases + price (native only; browser uses the mock flag).
      await configurePurchases()
      const [owned, price] = await Promise.all([checkEntitlement(), getUnlockPrice()])
      if (cancelled) return
      setHasPurchased(owned)
      setUnlockPrice(price)
    })()
    return () => {
      cancelled = true
    }
  }, [])

  // ---- persistence (only after initial load) ----
  useEffect(() => {
    if (ready) void setJSON(KEYS.settings, settings)
  }, [settings, ready])
  useEffect(() => {
    if (ready) void setJSON(KEYS.entries, entries)
  }, [entries, ready])

  // ---- reminder scheduling ----
  const lastReminder = useRef<string>('')
  useEffect(() => {
    if (!ready) return
    const sig = `${settings.reminderTime?.hour ?? 'x'}:${settings.reminderTime?.minute ?? 'x'}:${settings.lang}`
    if (sig === lastReminder.current) return
    lastReminder.current = sig
    void scheduleEveningReminder(settings.reminderTime, settings.lang)
  }, [settings.reminderTime, settings.lang, ready])

  const t = useCallback(
    (b: Bilingual | undefined) => (b ? b[settings.lang] : ''),
    [settings.lang],
  )

  const roles = useMemo<Role[]>(
    () => (settings.edition === 'combined' ? ['mama', 'papa'] : ['solo']),
    [settings.edition],
  )

  // ---- setters ----
  const updateSettings = useCallback(
    (patch: Partial<Settings>) => setSettings((s) => ({ ...s, ...patch })),
    [],
  )
  const setLang = useCallback((lang: Lang) => updateSettings({ lang }), [updateSettings])
  const setEdition = useCallback(
    (edition: Edition) => updateSettings({ edition }),
    [updateSettings],
  )
  const completeOnboarding = useCallback(
    (patch: Partial<Settings>) => setSettings((s) => ({ ...s, ...patch, onboarded: true })),
    [],
  )

  const setDailyAnswer = useCallback(
    (day: string, role: Role, index: number, value: string) => {
      setEntries((e) => {
        const dayRec = { ...(e.daily[day] ?? {}) }
        const arr = [...(dayRec[role] ?? [])]
        arr[index] = value
        dayRec[role] = arr
        return { ...e, daily: { ...e.daily, [day]: dayRec } }
      })
    },
    [],
  )
  const setWeekIntent = useCallback((week: number, role: Role, value: string) => {
    setEntries((e) => ({
      ...e,
      weekIntent: { ...e.weekIntent, [week]: { ...(e.weekIntent[week] ?? {}), [role]: value } },
    }))
  }, [])
  const setSunday = useCallback((week: number, role: Role, value: string) => {
    setEntries((e) => ({
      ...e,
      sunday: { ...e.sunday, [week]: { ...(e.sunday[week] ?? {}), [role]: value } },
    }))
  }, [])
  const setDebrief = useCallback(
    (week: number, role: Role, index: number, value: string) => {
      setEntries((e) => {
        const wk = { ...(e.debrief[week] ?? {}) }
        const arr = [...(wk[role] ?? [])]
        arr[index] = value
        wk[role] = arr
        return { ...e, debrief: { ...e.debrief, [week]: wk } }
      })
    },
    [],
  )
  const toggleDayRead = useCallback((day: number) => {
    setEntries((e) => {
      const next = { ...e.daysRead }
      if (next[day]) delete next[day]
      else next[day] = true
      return { ...e, daysRead: next }
    })
  }, [])
  const setWeekPhoto = useCallback((week: number, dataUri: string | null) => {
    setEntries((e) => {
      const next = { ...e.weekPhotos }
      if (dataUri) next[week] = dataUri
      else delete next[week]
      return { ...e, weekPhotos: next }
    })
  }, [])
  const setWeekMood = useCallback((week: number, mood: string | null) => {
    setEntries((e) => {
      const next = { ...e.weekMood }
      if (mood) next[week] = mood
      else delete next[week]
      return { ...e, weekMood: next }
    })
  }, [])
  const setToolField = useCallback((tool: number, index: number, value: string) => {
    setEntries((e) => {
      const arr = [...(e.tools[tool] ?? [])]
      arr[index] = value
      return { ...e, tools: { ...e.tools, [tool]: arr } }
    })
  }, [])

  // ---- derived: which days have at least one non-empty answer ----
  const daysWithEntries = useMemo(() => {
    const set = new Set<string>()
    for (const [day, roleRec] of Object.entries(entries.daily)) {
      const any = Object.values(roleRec).some((arr) => (arr ?? []).some((v) => v.trim() !== ''))
      if (any) set.add(day)
    }
    return set
  }, [entries.daily])

  const streak = useMemo(() => computeStreak(daysWithEntries), [daysWithEntries])

  const daysReadCount = useMemo(
    () => Object.keys(entries.daysRead ?? {}).length,
    [entries.daysRead],
  )

  // ---- purchase actions ----
  const refreshPurchase = useCallback(async () => {
    const owned = await checkEntitlement()
    setHasPurchased(owned)
  }, [])
  const purchase = useCallback(async () => {
    const res = await purchaseUnlock()
    if (res.unlocked) setHasPurchased(true)
    return res
  }, [])
  const restore = useCallback(async () => {
    const res = await restorePurchases()
    if (res.unlocked) setHasPurchased(true)
    return res
  }, [])

  const value: AppContextValue = {
    ready,
    settings,
    entries,
    hasPurchased,
    unlockPrice,
    lang: settings.lang,
    edition: settings.edition,
    roles,
    t,
    setLang,
    setEdition,
    updateSettings,
    completeOnboarding,
    setDailyAnswer,
    setWeekIntent,
    setSunday,
    setDebrief,
    setToolField,
    toggleDayRead,
    setWeekPhoto,
    setWeekMood,
    daysReadCount,
    daysWithEntries,
    streak,
    refreshPurchase,
    purchase,
    restore,
  }

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>
}

// eslint-disable-next-line react-refresh/only-export-components
export function useApp(): AppContextValue {
  const ctx = useContext(AppContext)
  if (!ctx) throw new Error('useApp must be used within AppProvider')
  return ctx
}

export { DEFAULT_REMINDER }
