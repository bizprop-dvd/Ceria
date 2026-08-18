import { Capacitor } from '@capacitor/core'
import { Directory, Encoding, Filesystem } from '@capacitor/filesystem'
import { Share } from '@capacitor/share'
import { backupFileName } from './backup'

/**
 * Saving and opening a backup as an ordinary file, with no account anywhere.
 *
 * On a phone this writes the file and opens the share sheet, so the parent
 * sends it wherever they already keep things — Drive, WhatsApp to themselves,
 * email. In a browser it downloads. Either way the file is theirs and Ceria
 * never sees it.
 */

/** Write the backup and hand it to the parent. Returns false if they cancelled. */
export async function exportToFile(contents: string): Promise<boolean> {
  const name = backupFileName()

  if (!Capacitor.isNativePlatform()) {
    const url = URL.createObjectURL(new Blob([contents], { type: 'application/json' }))
    const a = document.createElement('a')
    a.href = url
    a.download = name
    document.body.appendChild(a)
    a.click()
    a.remove()
    URL.revokeObjectURL(url)
    return true
  }

  await Filesystem.writeFile({
    path: name,
    data: contents,
    directory: Directory.Cache,
    encoding: Encoding.UTF8,
  })
  const { uri } = await Filesystem.getUri({ path: name, directory: Directory.Cache })
  try {
    await Share.share({ title: 'Ceria', url: uri })
    return true
  } catch {
    // Share throws when the sheet is dismissed; that is a cancel, not a failure.
    return false
  }
}

/**
 * Ask the parent for a backup file and read it.
 *
 * Uses a plain file input, which the native webview maps to the system file
 * picker, so this needs no extra plugin on either platform. Resolves null if
 * they close the picker without choosing.
 */
export function importFromFile(): Promise<string | null> {
  return new Promise((resolve) => {
    const input = document.createElement('input')
    input.type = 'file'
    input.accept = 'application/json,.json'
    input.style.position = 'fixed'
    input.style.left = '-9999px'

    let settled = false
    const done = (value: string | null) => {
      if (settled) return
      settled = true
      input.remove()
      window.removeEventListener('focus', onFocus)
      resolve(value)
    }

    // No 'cancel' event fires reliably across webviews; returning focus with
    // no file chosen is the signal that they backed out.
    const onFocus = () => setTimeout(() => { if (!input.files?.length) done(null) }, 800)

    input.addEventListener('change', () => {
      const file = input.files?.[0]
      if (!file) return done(null)
      const reader = new FileReader()
      reader.onload = () => done(typeof reader.result === 'string' ? reader.result : null)
      reader.onerror = () => done(null)
      reader.readAsText(file)
    })

    document.body.appendChild(input)
    window.addEventListener('focus', onFocus)
    input.click()
  })
}
