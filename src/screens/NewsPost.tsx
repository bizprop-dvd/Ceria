import { Navigate, useParams } from 'react-router-dom'
import Screen from '../components/Screen'
import { useApp } from '../store/AppContext'
import { useNews } from '../store/NewsContext'
import { formatDay } from '../lib/dates'

/** One post from Ceria, in full. */
export default function NewsPost() {
  const { id } = useParams()
  const { lang } = useApp()
  const { byId, loading } = useNews()
  const item = id ? byId(decodeURIComponent(id)) : undefined

  // While the saved list is still being read there is nothing to look up yet;
  // sending the reader back to the list at that moment would look like a bug.
  if (loading) {
    return (
      <Screen back title={lang === 'en' ? 'News' : 'Kabar'}>
        <div />
      </Screen>
    )
  }
  if (!item) return <Navigate to="/news" replace />

  return (
    <Screen back title={lang === 'en' ? 'News' : 'Kabar'}>
      <article className="mx-auto max-w-prose pt-1">
        {item.image && (
          <img
            src={item.image}
            alt=""
            aria-hidden
            decoding="async"
            className="mb-4 block w-full rounded-2xl object-cover"
            style={{ aspectRatio: '3 / 2', background: '#F2E9D9' }}
          />
        )}

        <p className="text-[11px] uppercase tracking-[0.08em] text-ceria-gray">
          {formatDay(item.date, lang)}
        </p>
        <h1 className="mt-1 font-head text-2xl font-semibold leading-snug text-ceria-dark">
          {item.title[lang]}
        </h1>

        {item.event && (
          <div className="card mt-4 border-l-4 border-ceria-teal p-4">
            {item.event.when && (
              <p className="text-[15px] font-semibold text-ceria-dark">{item.event.when[lang]}</p>
            )}
            {item.event.place && (
              <p className="mt-0.5 text-sm text-ceria-gray">{item.event.place[lang]}</p>
            )}
          </div>
        )}

        <p className="mt-4 whitespace-pre-line text-[15px] leading-relaxed text-ceria-dark/90">
          {item.body[lang]}
        </p>

        {item.link && (
          <a
            href={item.link.url}
            target="_blank"
            rel="noreferrer"
            className="btn-primary mt-6 w-full"
          >
            {item.link.label
              ? item.link.label[lang]
              : lang === 'en'
                ? 'Open the link'
                : 'Buka tautan'}
          </a>
        )}

        <p className="mt-6 text-center text-xs text-ceria-gray/80">
          {lang === 'en'
            ? 'Posted by Yayasan Sukacita Keluarga Indonesia.'
            : 'Diposting oleh Yayasan Sukacita Keluarga Indonesia.'}
        </p>
      </article>
    </Screen>
  )
}
