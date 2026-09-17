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
import { App as CapApp } from '@capacitor/app'
import { dayKey } from '../lib/dates'
import {
  EMPTY_FEED,
  fetchFeed,
  isStale,
  loadCachedFeed,
  loadSeedFeed,
  loadSeen,
  saveSeen,
  visibleItems,
  type NewsFeed,
  type NewsItem,
} from '../lib/news'

interface NewsContextValue {
  /** what to show today: expired posts dropped, pinned first, newest first */
  items: NewsItem[]
  /** true only while the very first list is being found — there is nothing to show yet */
  loading: boolean
  /** how many posts this device has not opened the News tab on yet */
  unread: number
  /** when the app last successfully read the file, or null if it never has */
  fetchedAt: number | null
  /** the last attempt failed; the list on screen is a saved copy */
  offline: boolean
  /** the copy on screen is old enough to be worth asking again */
  stale: boolean
  refresh: () => Promise<void>
  markAllSeen: () => void
  byId: (id: string) => NewsItem | undefined
}

const NewsContext = createContext<NewsContextValue | null>(null)

/**
 * Keeps Ceria's noticeboard in memory for the whole app.
 *
 * Deliberately quiet: nothing here ever blocks a screen, shows an error, or
 * waits on the network before the app can be used. The worst a dead connection
 * does is leave yesterday's list in place.
 */
export function NewsProvider({ children }: { children: ReactNode }) {
  const [feed, setFeed] = useState<NewsFeed>(EMPTY_FEED)
  const [fetchedAt, setFetchedAt] = useState<number | null>(null)
  const [seen, setSeen] = useState<string[]>([])
  const [loading, setLoading] = useState(true)
  const [offline, setOffline] = useState(false)
  // Guards against two refreshes at once — the tab opening while the one
  // started at launch is still in the air.
  const busy = useRef(false)
  // Read by the resume listener, which is installed once and would otherwise
  // capture the value of fetchedAt from the render that installed it.
  const fetchedAtRef = useRef<number | null>(null)
  fetchedAtRef.current = fetchedAt

  const refresh = useCallback(async () => {
    if (busy.current) return
    busy.current = true
    try {
      const fresh = await fetchFeed()
      if (fresh) {
        setFeed(fresh)
        setFetchedAt(Date.now())
        setOffline(false)
      } else {
        setOffline(true)
      }
    } finally {
      busy.current = false
    }
  }, [])

  // First list, then an update if the saved one is old.
  useEffect(() => {
    let cancelled = false
    ;(async () => {
      const [cached, alreadySeen] = await Promise.all([loadCachedFeed(), loadSeen()])
      if (cancelled) return
      setSeen(alreadySeen)
      if (cached) {
        setFeed(cached.feed)
        setFetchedAt(cached.fetchedAt)
      } else {
        // Nothing has ever been downloaded: show what shipped with the app so
        // the tab is not blank on a first run with no signal.
        const seed = await loadSeedFeed()
        if (cancelled) return
        if (seed) setFeed(seed)
      }
      setLoading(false)
      if (isStale(cached?.fetchedAt ?? null)) await refresh()
    })()
    return () => {
      cancelled = true
    }
  }, [refresh])

  // A phone that was asleep for a day comes back to a current list.
  useEffect(() => {
    let remove: (() => void) | undefined
    void CapApp.addListener('appStateChange', ({ isActive }) => {
      if (isActive && isStale(fetchedAtRef.current)) void refresh()
    }).then((handle) => {
      remove = () => void handle.remove()
    })
    return () => remove?.()
  }, [refresh])

  const items = useMemo(() => visibleItems(feed, dayKey()), [feed])

  const unread = useMemo(() => {
    const read = new Set(seen)
    return items.filter((item) => !read.has(item.id)).length
  }, [items, seen])

  /**
   * Called when the list is opened. Only ids still on the list are kept, so a
   * post that Ceria takes down does not sit in this device's memory forever.
   */
  const markAllSeen = useCallback(() => {
    const ids = items.map((item) => item.id)
    const same = ids.length === seen.length && ids.every((id) => seen.includes(id))
    if (same) return
    setSeen(ids)
    void saveSeen(ids)
  }, [items, seen])

  const byId = useCallback((id: string) => feed.items.find((item) => item.id === id), [feed])

  const value: NewsContextValue = {
    items,
    loading,
    unread,
    fetchedAt,
    offline,
    stale: isStale(fetchedAt),
    refresh,
    markAllSeen,
    byId,
  }

  return <NewsContext.Provider value={value}>{children}</NewsContext.Provider>
}

// eslint-disable-next-line react-refresh/only-export-components
export function useNews(): NewsContextValue {
  const ctx = useContext(NewsContext)
  if (!ctx) throw new Error('useNews must be used within NewsProvider')
  return ctx
}
