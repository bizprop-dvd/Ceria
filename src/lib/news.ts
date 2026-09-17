/**
 * Ceria's own noticeboard: events, gatherings, and news from the foundation.
 *
 * HOW IT WORKS
 *
 * The app reads one small file that Ceria publishes on its own website:
 *
 *     https://www.yayasanceria.org/app/news.json
 *
 * There is no server here and no account. The app asks for that file, keeps a
 * copy on the phone, and shows the copy — so the News tab works on a bus with
 * no signal, and a failed request costs a parent nothing but an older list.
 *
 * The request is a plain GET of a public file. No identifier, no query string,
 * nothing about the family goes out with it. That is what lets the store
 * listing keep saying the app collects nothing.
 *
 * Because the file is edited by people rather than generated, everything here
 * is written to survive a bad edit: an item missing a title, a date typed
 * wrong, a trailing comma. Anything that does not parse is dropped, and the
 * last good copy stays on screen.
 */

import { CapacitorHttp } from '@capacitor/core'
import { CERIA } from '../config'
import type { Bilingual } from '../data/types'
import { KEYS, getJSON, setJSON } from './storage'

export interface NewsItem {
  /** stable id, e.g. "2026-09-gathering-surabaya" — decides what counts as unread */
  id: string
  /** the day the post is dated, YYYY-MM-DD */
  date: string
  title: Bilingual
  body: Bilingual
  /** optional picture, an absolute https URL */
  image?: string
  /** optional button: registration form, WhatsApp group, article */
  link?: { url: string; label?: Bilingual }
  /** optional details for something happening at a time and place */
  event?: { when?: Bilingual; place?: Bilingual }
  /** keep at the top of the list */
  pinned?: boolean
  /** hide from the list after this day, YYYY-MM-DD (an event that has passed) */
  until?: string
}

export interface NewsFeed {
  /** when Ceria last edited the file, ISO 8601 — informational only */
  updated: string | null
  items: NewsItem[]
}

interface CachedFeed {
  feed: NewsFeed
  fetchedAt: number
}

/** Where the file lives. A build may override it, which is how staging is tested. */
export const FEED_URL = import.meta.env.VITE_NEWS_URL || CERIA.newsUrl

/** Shipped inside the app, shown until the phone first reaches the internet. */
const SEED_URL = './news.json'

/** How long a fetched copy is treated as current. */
export const STALE_AFTER_MS = 6 * 60 * 60 * 1000

const TIMEOUT_MS = 8000

export const EMPTY_FEED: NewsFeed = { updated: null, items: [] }

/* ---------- reading ---------- */

export async function loadCachedFeed(): Promise<CachedFeed | null> {
  const cached = await getJSON<CachedFeed | null>(KEYS.news, null)
  if (!cached || typeof cached.fetchedAt !== 'number') return null
  const feed = parseFeed(cached.feed)
  return feed ? { feed, fetchedAt: cached.fetchedAt } : null
}

export function isStale(fetchedAt: number | null): boolean {
  return fetchedAt === null || Date.now() - fetchedAt > STALE_AFTER_MS
}

/**
 * Ask the website for the current file. Returns null when it cannot be
 * reached or what came back is not a usable feed — never throws, and never
 * replaces a good cached copy with an empty one.
 */
export async function fetchFeed(): Promise<NewsFeed | null> {
  const feed = parseFeed(await getRemoteJSON(FEED_URL))
  if (feed) await setJSON(KEYS.news, { feed, fetchedAt: Date.now() } satisfies CachedFeed)
  return feed
}

/** The copy that ships with the app. Used only when there is nothing else. */
export async function loadSeedFeed(): Promise<NewsFeed | null> {
  return parseFeed(await getLocalJSON(SEED_URL))
}

/* ---------- what to show ---------- */

/**
 * The items worth showing today: nothing that has expired, pinned first, then
 * newest first. `today` is passed in so the caller decides what "now" means.
 */
export function visibleItems(feed: NewsFeed, today: string): NewsItem[] {
  return feed.items
    .filter((item) => !item.until || item.until >= today)
    .sort((a, b) => {
      if (Boolean(a.pinned) !== Boolean(b.pinned)) return a.pinned ? -1 : 1
      return b.date.localeCompare(a.date)
    })
}

/* ---------- what has been read ---------- */

export async function loadSeen(): Promise<string[]> {
  const seen = await getJSON<unknown>(KEYS.newsSeen, [])
  return Array.isArray(seen) ? seen.filter((id): id is string => typeof id === 'string') : []
}

/**
 * Remember which posts have been seen. Callers pass only ids that are still in
 * the feed, so the list cannot grow without bound as Ceria posts over the years.
 */
export async function saveSeen(ids: string[]): Promise<void> {
  await setJSON(KEYS.newsSeen, ids)
}

/* ---------- parsing ---------- */

/**
 * Turn whatever came back into a feed, keeping only the items that are whole.
 * A post with no title in one language falls back to the other rather than
 * disappearing — a half-translated post is still news.
 */
export function parseFeed(raw: unknown): NewsFeed | null {
  if (!isRecord(raw) || !Array.isArray(raw.items)) return null
  const items: NewsItem[] = []
  const seenIds = new Set<string>()
  for (const entry of raw.items) {
    const item = parseItem(entry)
    if (!item || seenIds.has(item.id)) continue
    seenIds.add(item.id)
    items.push(item)
  }
  return { updated: typeof raw.updated === 'string' ? raw.updated : null, items }
}

function parseItem(raw: unknown): NewsItem | null {
  if (!isRecord(raw)) return null
  const id = typeof raw.id === 'string' ? raw.id.trim() : ''
  const title = parseBilingual(raw.title)
  const body = parseBilingual(raw.body)
  if (!id || !title || !body || !isDay(raw.date)) return null

  const item: NewsItem = { id, date: raw.date, title, body }
  if (typeof raw.image === 'string' && isHttps(raw.image)) item.image = raw.image
  if (isRecord(raw.link) && typeof raw.link.url === 'string' && isHttps(raw.link.url)) {
    const label = parseBilingual(raw.link.label)
    item.link = label ? { url: raw.link.url, label } : { url: raw.link.url }
  }
  if (isRecord(raw.event)) {
    const when = parseBilingual(raw.event.when)
    const place = parseBilingual(raw.event.place)
    if (when || place) item.event = { ...(when && { when }), ...(place && { place }) }
  }
  if (raw.pinned === true) item.pinned = true
  if (isDay(raw.until)) item.until = raw.until
  return item
}

/** Accepts {en, id}, or one plain string used for both languages. */
function parseBilingual(raw: unknown): Bilingual | null {
  if (typeof raw === 'string') {
    const text = raw.trim()
    return text ? { en: text, id: text } : null
  }
  if (!isRecord(raw)) return null
  const en = typeof raw.en === 'string' ? raw.en.trim() : ''
  const id = typeof raw.id === 'string' ? raw.id.trim() : ''
  if (!en && !id) return null
  return { en: en || id, id: id || en }
}

function isRecord(v: unknown): v is Record<string, unknown> {
  return typeof v === 'object' && v !== null && !Array.isArray(v)
}

function isDay(v: unknown): v is string {
  return typeof v === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(v)
}

function isHttps(url: string): boolean {
  return /^https:\/\//i.test(url)
}

/* ---------- transport ---------- */

/**
 * Fetch from the website.
 *
 * On a phone this goes out through the operating system rather than the
 * WebView, so the file does not need CORS headers to be readable in the app.
 * In a browser it falls back to the WebView's own request, which does — see
 * docs/news.md for what the web team has to set.
 */
async function getRemoteJSON(url: string): Promise<unknown | null> {
  try {
    const res = await CapacitorHttp.get({
      url,
      headers: { Accept: 'application/json' },
      connectTimeout: TIMEOUT_MS,
      readTimeout: TIMEOUT_MS,
    })
    if (res.status < 200 || res.status >= 300) return null
    return typeof res.data === 'string' ? JSON.parse(res.data) : res.data
  } catch {
    return null
  }
}

/** Fetch a file that ships inside the app. */
async function getLocalJSON(url: string): Promise<unknown | null> {
  const abort = new AbortController()
  const timer = setTimeout(() => abort.abort(), TIMEOUT_MS)
  try {
    const res = await fetch(url, { signal: abort.signal })
    return res.ok ? await res.json() : null
  } catch {
    return null
  } finally {
    clearTimeout(timer)
  }
}
