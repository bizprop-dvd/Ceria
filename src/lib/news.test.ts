import { describe, expect, it } from 'vitest'
import { parseFeed, visibleItems } from './news'

const post = {
  id: 'gathering',
  date: '2026-09-28',
  title: { en: 'Gathering', id: 'Temu keluarga' },
  body: { en: 'Come along.', id: 'Mari hadir.' },
}

describe('parseFeed', () => {
  it('keeps a whole post', () => {
    const feed = parseFeed({ updated: '2026-09-17', items: [post] })
    expect(feed?.items).toHaveLength(1)
    expect(feed?.updated).toBe('2026-09-17')
  })

  it('refuses anything that is not a feed', () => {
    expect(parseFeed(null)).toBeNull()
    expect(parseFeed('<html>404</html>')).toBeNull()
    expect(parseFeed({ items: 'soon' })).toBeNull()
  })

  // The file is edited by hand, so one bad post must not take the rest down.
  it('drops posts that are missing what a post needs', () => {
    const feed = parseFeed({
      items: [
        post,
        { id: 'no-date', title: post.title, body: post.body },
        { date: '2026-09-01', title: post.title, body: post.body },
        { id: 'bad-date', date: '28/09/2026', title: post.title, body: post.body },
        { id: 'no-body', date: '2026-09-01', title: post.title },
      ],
    })
    expect(feed?.items.map((i) => i.id)).toEqual(['gathering'])
  })

  it('keeps the first of two posts sharing an id', () => {
    const feed = parseFeed({ items: [post, { ...post, title: { en: 'Later', id: 'Nanti' } }] })
    expect(feed?.items).toHaveLength(1)
    expect(feed?.items[0].title.en).toBe('Gathering')
  })

  // Half-translated is better than not posted at all.
  it('fills a missing language from the one that is there', () => {
    const feed = parseFeed({
      items: [{ ...post, title: { id: 'Temu keluarga' }, body: 'Mari hadir.' }],
    })
    expect(feed?.items[0].title.en).toBe('Temu keluarga')
    expect(feed?.items[0].body.en).toBe('Mari hadir.')
  })

  it('ignores a link or picture that is not https', () => {
    const feed = parseFeed({
      items: [{ ...post, image: 'http://example.org/p.jpg', link: { url: 'javascript:alert(1)' } }],
    })
    expect(feed?.items[0].image).toBeUndefined()
    expect(feed?.items[0].link).toBeUndefined()
  })
})

describe('visibleItems', () => {
  const feed = parseFeed({
    items: [
      { ...post, id: 'old', date: '2026-08-01' },
      { ...post, id: 'new', date: '2026-09-12' },
      { ...post, id: 'notice', date: '2026-07-01', pinned: true },
      { ...post, id: 'finished', date: '2026-09-01', until: '2026-09-16' },
      { ...post, id: 'today', date: '2026-09-17', until: '2026-09-17' },
    ],
  })!

  it('puts pinned first, then the newest', () => {
    expect(visibleItems(feed, '2026-09-17').map((i) => i.id)).toEqual([
      'notice',
      'today',
      'new',
      'old',
    ])
  })

  it('drops a post whose day has passed, and keeps one ending today', () => {
    const ids = visibleItems(feed, '2026-09-17').map((i) => i.id)
    expect(ids).not.toContain('finished')
    expect(ids).toContain('today')
  })
})
