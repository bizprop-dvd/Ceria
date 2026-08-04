import { useRef, useState } from 'react'
import { useApp } from '../store/AppContext'

/**
 * One photo per diary week.
 *
 * The image is downscaled and re-encoded on the device before it is saved, so a
 * 4 MB camera photo becomes roughly 100 KB. It is stored as a data URI in the
 * app's own local storage alongside the entries — it is never uploaded, and it
 * does not enter the phone's shared photo library.
 */

const MAX_EDGE = 1000 // px on the long side
const QUALITY = 0.72

async function downscale(file: File): Promise<string> {
  const bitmap = await createImageBitmap(file)
  const scale = Math.min(1, MAX_EDGE / Math.max(bitmap.width, bitmap.height))
  const w = Math.round(bitmap.width * scale)
  const h = Math.round(bitmap.height * scale)
  const canvas = document.createElement('canvas')
  canvas.width = w
  canvas.height = h
  const ctx = canvas.getContext('2d')
  if (!ctx) throw new Error('no canvas context')
  ctx.drawImage(bitmap, 0, 0, w, h)
  bitmap.close?.()
  return canvas.toDataURL('image/jpeg', QUALITY)
}

export default function WeekPhoto({ week }: { week: number }) {
  const { lang, entries, setWeekPhoto } = useApp()
  const inputRef = useRef<HTMLInputElement>(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const photo = entries.weekPhotos?.[week]

  const onPick = async (file: File | undefined) => {
    if (!file) return
    setBusy(true)
    setError(null)
    try {
      setWeekPhoto(week, await downscale(file))
    } catch {
      setError(
        lang === 'en'
          ? 'That image could not be added. Try another one.'
          : 'Gambar ini belum dapat ditambahkan. Silakan coba gambar lain.',
      )
    } finally {
      setBusy(false)
      if (inputRef.current) inputRef.current.value = ''
    }
  }

  return (
    <div>
      <p className="mb-2 font-head text-[15px] font-semibold text-ceria-dark">
        {lang === 'en' ? 'A photo from this week' : 'Satu foto dari minggu ini'}
      </p>

      {photo ? (
        <div className="overflow-hidden rounded-2xl bg-white shadow-card">
          <img
            src={photo}
            alt={lang === 'en' ? `Week ${week}` : `Minggu ${week}`}
            className="block max-h-72 w-full object-cover"
          />
          <div className="flex gap-2 p-2">
            <button
              onClick={() => inputRef.current?.click()}
              className="btn-ghost flex-1 text-sm"
              disabled={busy}
            >
              {lang === 'en' ? 'Replace' : 'Ganti'}
            </button>
            <button
              onClick={() => setWeekPhoto(week, null)}
              className="btn-ghost flex-1 text-sm text-ceria-pink"
              disabled={busy}
            >
              {lang === 'en' ? 'Remove' : 'Hapus'}
            </button>
          </div>
        </div>
      ) : (
        <button
          onClick={() => inputRef.current?.click()}
          disabled={busy}
          className="flex w-full flex-col items-center gap-1.5 rounded-2xl border border-dashed border-ceria-cream-deep bg-white/60 px-4 py-7 transition active:scale-[0.99]"
        >
          <svg
            width={26}
            height={26}
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth={1.6}
            strokeLinecap="round"
            strokeLinejoin="round"
            className="text-ceria-teal"
          >
            <rect x="3" y="5" width="18" height="14" rx="2.5" />
            <circle cx="12" cy="12" r="3.2" />
            <path d="M8 5l1.2-1.8h5.6L16 5" />
          </svg>
          <span className="text-sm font-medium text-ceria-blue">
            {busy
              ? lang === 'en'
                ? 'Adding…'
                : 'Menambahkan…'
              : lang === 'en'
                ? 'Add a photo'
                : 'Tambah foto'}
          </span>
        </button>
      )}

      {error && <p className="mt-2 text-sm text-ceria-pink">{error}</p>}

      <p className="mt-2 text-[11px] leading-relaxed text-ceria-gray/80">
        {lang === 'en'
          ? 'Stays on this phone with your entries. Never uploaded, and not added to your photo gallery.'
          : 'Foto ini hanya tersimpan di ponsel bersama catatan Anda. Foto tidak diunggah dan tidak ditambahkan ke galeri.'}
      </p>

      <input
        ref={inputRef}
        type="file"
        accept="image/*"
        className="hidden"
        onChange={(e) => void onPick(e.target.files?.[0])}
      />
    </div>
  )
}
