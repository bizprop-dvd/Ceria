import { useEffect } from 'react'
import { Link } from 'react-router-dom'
import Screen from '../components/Screen'
import { useApp } from '../store/AppContext'
import { useNews } from '../store/NewsContext'
import { formatDay } from '../lib/dates'
import { CERIA } from '../config'
import { ChevronRight, NewsIcon } from '../components/icons'

/**
 * What Ceria is doing: gatherings, courses, and notes from the foundation.
 *
 * The one screen in the app that is not the parent's own: everything here is
 * written by Ceria's team and read from the foundation's website. Opening the
 * tab is what marks it read, so the dot on the tab bar means "something you
 * have not looked at", not "something you have not tapped".
 */
export default function News() {
  const { lang } = useApp()
  const { items, loading, offline, stale, refresh, markAllSeen } = useNews()

  useEffect(() => {
    if (stale) void refresh()
  }, [stale, refresh])

  // After the list is on screen, not while it is still arriving — otherwise a
  // post that lands a moment later would be marked read before it was shown.
  useEffect(() => {
    if (!loading) markAllSeen()
  }, [loading, items, markAllSeen])

  return (
    <Screen
      title={lang === 'en' ? 'News' : 'Kabar'}
      subtitle={lang === 'en' ? 'From Ceria' : 'Dari Ceria'}
    >
      {loading ? (
        <ListPlaceholder />
      ) : items.length === 0 ? (
        <EmptyNote offline={offline} />
      ) : (
        <ul className="space-y-3 pt-1">
          {items.map((item) => (
            <li key={item.id}>
              <Link
                to={`/news/${encodeURIComponent(item.id)}`}
                className="card block overflow-hidden active:scale-[0.99] transition"
              >
                {item.image && (
                  <img
                    src={item.image}
                    alt=""
                    aria-hidden
                    loading="lazy"
                    decoding="async"
                    className="block h-40 w-full object-cover"
                    style={{ background: '#F2E9D9' }}
                  />
                )}
                <div className="flex items-start gap-3 p-4">
                  <div className="min-w-0 flex-1">
                    <p className="text-[11px] uppercase tracking-[0.08em] text-ceria-gray">
                      {formatDay(item.date, lang)}
                      {item.pinned && (
                        <span className="text-ceria-pink">
                          {lang === 'en' ? ' · Pinned' : ' · Disematkan'}
                        </span>
                      )}
                    </p>
                    <h2 className="mt-0.5 font-head text-[17px] font-semibold leading-snug text-ceria-dark">
                      {item.title[lang]}
                    </h2>
                    <p className="mt-1 line-clamp-2 text-sm leading-relaxed text-ceria-gray">
                      {item.body[lang]}
                    </p>
                  </div>
                  <ChevronRight width={18} height={18} className="mt-1 shrink-0 text-ceria-gray" />
                </div>
              </Link>
            </li>
          ))}
        </ul>
      )}

      {!loading && items.length > 0 && (
        <p className="mt-5 text-center text-xs text-ceria-gray/80">
          {offline
            ? lang === 'en'
              ? 'Saved copy — this will update when you are online.'
              : 'Salinan tersimpan — akan diperbarui saat Anda daring.'
            : lang === 'en'
              ? 'Posted by Ceria. Nothing you write is sent with this.'
              : 'Diposting oleh Ceria. Tidak ada tulisan Anda yang ikut terkirim.'}
        </p>
      )}
    </Screen>
  )
}

/** Nothing to show: either a first run with no connection, or a quiet month. */
function EmptyNote({ offline }: { offline: boolean }) {
  const { lang } = useApp()
  return (
    <div className="card mt-4 p-6 text-center">
      <NewsIcon width={28} height={28} className="mx-auto text-ceria-gray" />
      <p className="mt-2 font-head text-[16px] font-semibold text-ceria-dark">
        {offline
          ? lang === 'en'
            ? 'No connection right now'
            : 'Belum ada koneksi saat ini'
          : lang === 'en'
            ? 'Nothing new just yet'
            : 'Belum ada kabar baru'}
      </p>
      <p className="mt-1 text-sm text-ceria-gray">
        {offline
          ? lang === 'en'
            ? 'Ceria’s updates will appear here once you are online.'
            : 'Kabar dari Ceria akan muncul di sini begitu Anda daring.'
          : lang === 'en'
            ? 'When Ceria announces a gathering or a course, it will appear here.'
            : 'Saat Ceria mengumumkan pertemuan atau kursus, kabarnya muncul di sini.'}
      </p>
      <a
        href={CERIA.instagramUrl}
        target="_blank"
        rel="noreferrer"
        className="chip mt-4 bg-ceria-blue/8 text-ceria-blue"
      >
        Instagram
      </a>
    </div>
  )
}

/** Held for the moment between opening the tab and the saved list being read. */
function ListPlaceholder() {
  return (
    <div className="space-y-3 pt-1" aria-hidden>
      {[0, 1].map((i) => (
        <div key={i} className="card p-4">
          <div className="h-2.5 w-24 animate-pulse rounded bg-ceria-cream-deep" />
          <div className="mt-2 h-4 w-3/4 animate-pulse rounded bg-ceria-cream-deep" />
          <div className="mt-2 h-3 w-full animate-pulse rounded bg-ceria-cream-deep" />
        </div>
      ))}
    </div>
  )
}
