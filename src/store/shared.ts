import type { EntriesState } from './types'

/**
 * Which of a family's data is shared between two parents, and which belongs to
 * the person who wrote it.
 *
 * The rule, in the founder's words: the worksheets are the family's, the
 * writing is the person's.
 *
 * SHARED — one copy per family, the same on both phones:
 *   tools, toolInstances, toolPeriodCount, children
 *
 * PERSONAL — stays on the phone it was written on:
 *   daily, weekIntent, sunday, debrief, daysRead, weekMood, weekPhotos
 *
 * Photos are personal by size rather than by principle: a photo a week for a
 * year is far more data than everything else combined, and pushing it between
 * two phones would cost a parent real money on a metered plan.
 *
 * Nothing here uploads anything. This module only decides what belongs to whom
 * and how to combine two copies without losing anyone's work.
 */

export const SHARED_KEYS = ['tools', 'toolInstances', 'toolPeriodCount', 'children'] as const
export type SharedKey = (typeof SHARED_KEYS)[number]

/**
 * A stable address for one editable thing, used as the key for its timestamp.
 * Addresses must never be reformatted: an old backup's timestamps are matched
 * against them by string.
 */
export const addr = {
  toolField: (tool: number, index: number) => `tools:${tool}:${index}`,
  instanceField: (tool: number, instance: number, index: number) =>
    `toolInstances:${tool}:${instance}:${index}`,
  periodCount: (tool: number) => `toolPeriodCount:${tool}`,
  child: (id: number) => `children:${id}`,
  /** Tombstone. A removed child has to beat its own earlier edit, or a merge resurrects it. */
  childRemoved: (id: number) => `children:${id}:removed`,
}

export type EditedAt = Record<string, number>

/** Stamp one address as edited now. */
export function stamp(edited: EditedAt, address: string, at = Date.now()): EditedAt {
  return { ...edited, [address]: at }
}

export interface MergeChange {
  address: string
  /** where the winning value came from */
  from: 'local' | 'remote'
}

export interface MergeResult {
  entries: EntriesState
  changes: MergeChange[]
  editedAt: EditedAt
}

/**
 * Combine this phone's shared data with another phone's, field by field.
 *
 * The most recently edited value wins per field, so two parents filling in
 * different worksheets on the same evening both keep their work — only the
 * same field edited on both phones has to pick a winner.
 *
 * When neither side has a timestamp the local value is kept. That case only
 * arises for data written before this existed, and silently replacing what is
 * on the phone in front of the parent is the worse failure.
 *
 * Personal data is never touched: whatever is in `local` passes straight
 * through.
 */
export function mergeShared(
  local: EntriesState,
  localEdited: EditedAt,
  remote: EntriesState,
  remoteEdited: EditedAt,
): MergeResult {
  const changes: MergeChange[] = []
  const editedAt: EditedAt = { ...localEdited }

  /** Decide one field. Returns the winning value and records where it came from. */
  function pick<T>(address: string, localValue: T, remoteValue: T, equal: (a: T, b: T) => boolean): T {
    const lt = localEdited[address] ?? 0
    const rt = remoteEdited[address] ?? 0
    if (equal(localValue, remoteValue)) {
      // Same content: keep the earlier timestamp so a no-op sync does not make
      // this field look freshly edited to the other phone.
      if (rt && (!lt || rt < lt)) editedAt[address] = rt
      return localValue
    }
    if (rt > lt) {
      editedAt[address] = rt
      changes.push({ address, from: 'remote' })
      return remoteValue
    }
    changes.push({ address, from: 'local' })
    return localValue
  }

  const sameStr = (a: string | undefined, b: string | undefined) => (a ?? '') === (b ?? '')

  /* ---- tools: Record<toolNumber, string[]> ---- */
  const tools: EntriesState['tools'] = {}
  for (const key of union(Object.keys(local.tools ?? {}), Object.keys(remote.tools ?? {}))) {
    const tool = Number(key)
    const l = local.tools?.[tool] ?? []
    const r = remote.tools?.[tool] ?? []
    const out: string[] = []
    for (let i = 0; i < Math.max(l.length, r.length); i++) {
      out[i] = pick(addr.toolField(tool, i), l[i], r[i], sameStr) ?? ''
    }
    tools[tool] = out
  }

  /* ---- toolInstances: Record<`${tool}:${instance}`, string[]> ---- */
  const toolInstances: EntriesState['toolInstances'] = {}
  for (const key of union(
    Object.keys(local.toolInstances ?? {}),
    Object.keys(remote.toolInstances ?? {}),
  )) {
    const [tool, instance] = key.split(':').map(Number)
    const l = local.toolInstances?.[key] ?? []
    const r = remote.toolInstances?.[key] ?? []
    const out: string[] = []
    for (let i = 0; i < Math.max(l.length, r.length); i++) {
      out[i] = pick(addr.instanceField(tool, instance, i), l[i], r[i], sameStr) ?? ''
    }
    toolInstances[key] = out
  }

  /* ---- toolPeriodCount: Record<toolNumber, number> ---- */
  const toolPeriodCount: EntriesState['toolPeriodCount'] = {}
  for (const key of union(
    Object.keys(local.toolPeriodCount ?? {}),
    Object.keys(remote.toolPeriodCount ?? {}),
  )) {
    const tool = Number(key)
    const l = local.toolPeriodCount?.[tool]
    const r = remote.toolPeriodCount?.[tool]
    // Parts are only ever added, so the higher count is never wrong — taking the
    // max avoids a merge deleting a sheet someone has already written on.
    toolPeriodCount[tool] = Math.max(l ?? 0, r ?? 0)
    const rt = remoteEdited[addr.periodCount(tool)] ?? 0
    const lt = localEdited[addr.periodCount(tool)] ?? 0
    if (rt > lt) editedAt[addr.periodCount(tool)] = rt
  }

  /* ---- children ---- */
  const byId = new Map<number, { id: number; name: string }>()
  for (const c of local.children ?? []) byId.set(c.id, { ...c })
  const ids = union(
    (local.children ?? []).map((c) => String(c.id)),
    (remote.children ?? []).map((c) => String(c.id)),
  )
  const children: { id: number; name: string }[] = []
  for (const key of ids) {
    const id = Number(key)
    const l = (local.children ?? []).find((c) => c.id === id)
    const r = (remote.children ?? []).find((c) => c.id === id)

    // A child removed on one phone stays removed unless the other phone edited
    // them more recently than the removal.
    const removedAt = Math.max(
      localEdited[addr.childRemoved(id)] ?? 0,
      remoteEdited[addr.childRemoved(id)] ?? 0,
    )
    const editedOn = Math.max(localEdited[addr.child(id)] ?? 0, remoteEdited[addr.child(id)] ?? 0)
    if (removedAt && removedAt >= editedOn) {
      editedAt[addr.childRemoved(id)] = removedAt
      continue
    }

    const name = pick(addr.child(id), l?.name, r?.name, sameStr) ?? ''
    children.push({ id, name })
  }
  children.sort((a, b) => a.id - b.id)
  byId.clear()

  return {
    entries: { ...local, tools, toolInstances, toolPeriodCount, children },
    changes,
    editedAt,
  }
}

function union(a: string[], b: string[]): string[] {
  return [...new Set([...a, ...b])]
}

/** Everything shared, for sending to the other phone. Personal data is left behind. */
export function sharedOnly(entries: EntriesState): Pick<EntriesState, SharedKey> {
  return {
    tools: entries.tools ?? {},
    toolInstances: entries.toolInstances ?? {},
    toolPeriodCount: entries.toolPeriodCount ?? {},
    children: entries.children ?? [],
  }
}
