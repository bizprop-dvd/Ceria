import { useApp } from '../store/AppContext'

/**
 * Shown on guidebook chapters / toolkit tools whose full content still has to
 * be extracted from the founder's original PDFs. Honest placeholder, not
 * invented content.
 */
export default function ProvisionalNote({ kind }: { kind: 'chapter' | 'tool' }) {
  const { lang } = useApp()
  const copy = {
    en: {
      chapter: 'The full text of this chapter is being prepared from Ceria’s original guidebook. The principle above is complete; the detailed guidance is on its way.',
      tool: 'This tool’s full worksheet is being prepared from Ceria’s original toolkit. Its purpose above is complete; the fillable layout is on its way.',
    },
    id: {
      chapter: 'Teks lengkap bab ini sedang disiapkan dari panduan asli Ceria. Prinsip di atas sudah lengkap; panduan terperinci akan segera hadir.',
      tool: 'Lembar kerja lengkap alat ini sedang disiapkan dari toolkit asli Ceria. Tujuannya di atas sudah lengkap; format isian akan segera hadir.',
    },
  }
  return (
    <div className="card mt-4 border-dashed border-ceria-cream-deep bg-ceria-cream-deep/40 p-4">
      <p className="text-sm leading-relaxed text-ceria-gray">{copy[lang][kind]}</p>
    </div>
  )
}
