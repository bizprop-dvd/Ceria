import { getAccessToken } from './googleAuth'
import { DRIVE_FILE_NAME } from './backup'

/**
 * Read and write Ceria's single backup file in the parent's own Google Drive.
 *
 * Because the app holds only the 'drive.file' scope, it can see nothing in
 * Drive except files it created itself. The file is visible to the parent in
 * their Drive, deliberately — they should be able to see it, move it, or throw
 * it away without asking anyone.
 *
 * One fixed filename, so each backup replaces the last rather than leaving a
 * trail of dated copies the parent has to tidy up.
 */

const FILES = 'https://www.googleapis.com/drive/v3/files'
const UPLOAD = 'https://www.googleapis.com/upload/drive/v3/files'

export interface DriveFile {
  id: string
  modifiedTime: string
}

async function auth(): Promise<string> {
  const token = await getAccessToken()
  if (!token) throw new Error('not-signed-in')
  return token
}

/** The existing backup file, or null if this is the first one. */
export async function findBackup(): Promise<DriveFile | null> {
  const token = await auth()
  const q = encodeURIComponent(`name='${DRIVE_FILE_NAME}' and trashed=false`)
  const res = await fetch(`${FILES}?q=${q}&fields=files(id,modifiedTime)&pageSize=1`, {
    headers: { Authorization: `Bearer ${token}` },
  })
  if (!res.ok) throw new Error(`Drive lookup failed (${res.status})`)
  const json = (await res.json()) as { files?: DriveFile[] }
  return json.files?.[0] ?? null
}

/** Write the backup, replacing the previous one. Returns the file id. */
export async function uploadBackup(contents: string): Promise<string> {
  const token = await auth()
  const existing = await findBackup()

  const boundary = `ceria${Math.random().toString(36).slice(2)}`
  const metadata = existing
    ? { name: DRIVE_FILE_NAME }
    : { name: DRIVE_FILE_NAME, mimeType: 'application/json' }
  const body =
    `--${boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n` +
    `${JSON.stringify(metadata)}\r\n` +
    `--${boundary}\r\nContent-Type: application/json\r\n\r\n` +
    `${contents}\r\n--${boundary}--`

  const url = existing
    ? `${UPLOAD}/${existing.id}?uploadType=multipart&fields=id`
    : `${UPLOAD}?uploadType=multipart&fields=id`

  const res = await fetch(url, {
    method: existing ? 'PATCH' : 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': `multipart/related; boundary=${boundary}`,
    },
    body,
  })
  if (!res.ok) throw new Error(`Drive upload failed (${res.status})`)
  const json = (await res.json()) as { id: string }
  return json.id
}

/** The contents of the backup file, or null if there is not one yet. */
export async function downloadBackup(): Promise<string | null> {
  const token = await auth()
  const file = await findBackup()
  if (!file) return null
  const res = await fetch(`${FILES}/${file.id}?alt=media`, {
    headers: { Authorization: `Bearer ${token}` },
  })
  if (!res.ok) throw new Error(`Drive download failed (${res.status})`)
  return await res.text()
}

/** Remove the backup from Drive — part of disconnecting cleanly. */
export async function deleteBackup(): Promise<void> {
  const token = await auth()
  const file = await findBackup()
  if (!file) return
  await fetch(`${FILES}/${file.id}`, {
    method: 'DELETE',
    headers: { Authorization: `Bearer ${token}` },
  })
}
