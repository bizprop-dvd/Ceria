import { describe, expect, it } from 'vitest'
import { addr, mergeShared, sharedOnly, stamp, type EditedAt } from './shared'
import { emptyEntries, type EntriesState } from './types'

/**
 * These cover the cases where a merge could silently destroy something a
 * parent wrote. That is the whole risk of syncing two phones, so each one is
 * written as the story it represents rather than as an abstract case.
 */

function withTools(tools: EntriesState['tools']): EntriesState {
  return { ...emptyEntries(), tools }
}

const T0 = 1_000_000
const LATER = T0 + 60_000

describe('what is shared', () => {
  it('carries only the family worksheets, never the diary', () => {
    const e: EntriesState = {
      ...emptyEntries(),
      tools: { 1: ['a'] },
      children: [{ id: 1, name: 'Bagas' }],
      daily: { '2026-08-01': { mama: ['private'] } },
      sunday: { 1: { mama: 'private' } },
      weekPhotos: { 1: 'data:image/jpeg;base64,xxx' },
      daysRead: { 5: true },
    }
    const out = sharedOnly(e) as Record<string, unknown>
    expect(Object.keys(out).sort()).toEqual([
      'children',
      'toolInstances',
      'toolPeriodCount',
      'tools',
    ])
    expect(out.daily).toBeUndefined()
    expect(out.sunday).toBeUndefined()
    expect(out.weekPhotos).toBeUndefined()
  })
})

describe('merging two phones', () => {
  it('keeps both parents’ work when they filled in different fields', () => {
    const mama = withTools({ 1: ['mama wrote this', ''] })
    const mamaAt: EditedAt = { [addr.toolField(1, 0)]: T0 }
    const papa = withTools({ 1: ['', 'papa wrote this'] })
    const papaAt: EditedAt = { [addr.toolField(1, 1)]: T0 }

    const { entries } = mergeShared(mama, mamaAt, papa, papaAt)
    expect(entries.tools[1]).toEqual(['mama wrote this', 'papa wrote this'])
  })

  it('takes the newer text when both edited the same field', () => {
    const local = withTools({ 1: ['older'] })
    const remote = withTools({ 1: ['newer'] })
    const { entries, changes } = mergeShared(
      local,
      { [addr.toolField(1, 0)]: T0 },
      remote,
      { [addr.toolField(1, 0)]: LATER },
    )
    expect(entries.tools[1][0]).toBe('newer')
    expect(changes).toContainEqual({ address: addr.toolField(1, 0), from: 'remote' })
  })

  it('keeps the local text when the local edit is newer', () => {
    const local = withTools({ 1: ['newer'] })
    const remote = withTools({ 1: ['older'] })
    const { entries } = mergeShared(
      local,
      { [addr.toolField(1, 0)]: LATER },
      remote,
      { [addr.toolField(1, 0)]: T0 },
    )
    expect(entries.tools[1][0]).toBe('newer')
  })

  it('keeps what is on this phone when neither side has a timestamp', () => {
    // Data written before timestamps existed. Replacing what the parent is
    // looking at, on no evidence, is the worse failure.
    const local = withTools({ 1: ['on this phone'] })
    const remote = withTools({ 1: ['from the other phone'] })
    const { entries } = mergeShared(local, {}, remote, {})
    expect(entries.tools[1][0]).toBe('on this phone')
  })

  it('never reports a change when both phones already agree', () => {
    const local = withTools({ 1: ['same'] })
    const remote = withTools({ 1: ['same'] })
    const { changes } = mergeShared(local, { [addr.toolField(1, 0)]: T0 }, remote, {
      [addr.toolField(1, 0)]: LATER,
    })
    expect(changes).toEqual([])
  })

  it('leaves the diary and photos untouched', () => {
    const local: EntriesState = {
      ...emptyEntries(),
      daily: { '2026-08-01': { mama: ['mine'] } },
      weekPhotos: { 1: 'mine' },
      daysRead: { 3: true },
    }
    const remote: EntriesState = {
      ...emptyEntries(),
      daily: { '2026-08-01': { mama: ['theirs'] } },
      weekPhotos: { 1: 'theirs' },
      daysRead: { 9: true },
    }
    const { entries } = mergeShared(local, {}, remote, {})
    expect(entries.daily['2026-08-01'].mama).toEqual(['mine'])
    expect(entries.weekPhotos[1]).toBe('mine')
    expect(entries.daysRead).toEqual({ 3: true })
  })
})

describe('the children roster', () => {
  it('brings across a child added on the other phone', () => {
    const local: EntriesState = { ...emptyEntries(), children: [{ id: 1, name: 'Bagas' }] }
    const remote: EntriesState = {
      ...emptyEntries(),
      children: [
        { id: 1, name: 'Bagas' },
        { id: 2, name: 'Sari' },
      ],
    }
    const { entries } = mergeShared(local, { [addr.child(1)]: T0 }, remote, {
      [addr.child(1)]: T0,
      [addr.child(2)]: LATER,
    })
    expect(entries.children).toEqual([
      { id: 1, name: 'Bagas' },
      { id: 2, name: 'Sari' },
    ])
  })

  it('does not resurrect a child the other parent removed', () => {
    const local: EntriesState = { ...emptyEntries(), children: [] }
    const remote: EntriesState = { ...emptyEntries(), children: [{ id: 2, name: 'Sari' }] }
    const { entries } = mergeShared(
      local,
      { [addr.childRemoved(2)]: LATER },
      remote,
      { [addr.child(2)]: T0 },
    )
    expect(entries.children).toEqual([])
  })

  it('keeps a child who was renamed after being removed elsewhere', () => {
    // Removed on one phone, then renamed on the other. The later act wins.
    const local: EntriesState = { ...emptyEntries(), children: [] }
    const remote: EntriesState = { ...emptyEntries(), children: [{ id: 2, name: 'Sari Dewi' }] }
    const { entries } = mergeShared(
      local,
      { [addr.childRemoved(2)]: T0 },
      remote,
      { [addr.child(2)]: LATER },
    )
    expect(entries.children).toEqual([{ id: 2, name: 'Sari Dewi' }])
  })
})

describe('period sheets', () => {
  it('keeps the higher count so a sheet someone wrote on is not deleted', () => {
    const local: EntriesState = { ...emptyEntries(), toolPeriodCount: { 11: 3 } }
    const remote: EntriesState = { ...emptyEntries(), toolPeriodCount: { 11: 1 } }
    const { entries } = mergeShared(local, {}, remote, { [addr.periodCount(11)]: LATER })
    expect(entries.toolPeriodCount[11]).toBe(3)
  })
})

describe('stamping', () => {
  it('records the address without disturbing the others', () => {
    const before: EditedAt = { [addr.toolField(1, 0)]: T0 }
    const after = stamp(before, addr.child(2), LATER)
    expect(after[addr.toolField(1, 0)]).toBe(T0)
    expect(after[addr.child(2)]).toBe(LATER)
  })
})
