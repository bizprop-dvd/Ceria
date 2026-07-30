import { Navigate, useParams } from 'react-router-dom'
import Screen from '../components/Screen'
import PromptField from '../components/PromptField'
import { chapterName, diary, weekByNumber } from '../data/content'
import { useApp } from '../store/AppContext'
import { isUnlocked } from '../lib/freemium'
import type { Role } from '../data/types'

export default function DiaryWeek() {
  const { week } = useParams()
  const {
    t,
    lang,
    edition,
    hasPurchased,
    entries,
    setWeekIntent,
    setSunday,
    setDebrief,
  } = useApp()
  const num = Number(week)
  const wk = weekByNumber(num)

  if (!wk) return <Navigate to="/diary" replace />
  if (!isUnlocked(wk.chapter, hasPurchased)) return <Navigate to="/diary" replace />

  const chapter = chapterName(wk.chapter)
  const sunday = wk.sundayReflection[edition]
  const debriefPrompts = diary.meta.debrief[edition]
  const intentRec = entries.weekIntent[num] ?? {}
  const sundayRec = entries.sunday[num] ?? {}
  const debriefRec = entries.debrief[num] ?? {}

  return (
    <Screen
      back
      title={t(wk.theme)}
      subtitle={`${lang === 'en' ? 'Week' : 'Minggu'} ${wk.week} · ${chapter ? t(chapter) : ''}`}
    >
      <div className="mx-auto max-w-prose pt-2">
        {/* Principle for the week */}
        <div className="card border-l-4 border-l-ceria-teal p-4">
          <p className="font-head text-[17px] leading-snug text-ceria-dark">{t(wk.principle)}</p>
        </div>

        {/* Start of week: intent */}
        <SectionHead
          n={1}
          title={lang === 'en' ? 'Set your intent' : 'Tetapkan niat Anda'}
          note={lang === 'en' ? 'At the start of the week' : 'Di awal minggu'}
        />
        <div className="card p-4">
          <PromptField
            label={t(wk.weekIntent)}
            getValue={(role: Role) => intentRec[role] ?? ''}
            onChange={(role, value) => setWeekIntent(num, role, value)}
          />
        </div>

        {/* Daily reminder pointer */}
        <p className="mt-4 text-center text-xs text-ceria-gray">
          {lang === 'en'
            ? 'Add a few lines each day from the Today tab.'
            : 'Tambahkan beberapa baris setiap hari dari tab Hari Ini.'}
        </p>

        {/* End of week: Sunday reflection */}
        <SectionHead
          n={2}
          title={lang === 'en' ? 'Sunday reflection' : 'Refleksi Minggu'}
          note={lang === 'en' ? 'Look back together' : 'Menengok kembali bersama'}
        />
        <div className="card p-4">
          <PromptField
            label={t(sunday)}
            getValue={(role: Role) => sundayRec[role] ?? ''}
            onChange={(role, value) => setSunday(num, role, value)}
            rows={4}
          />
        </div>

        {/* 5-minute debrief */}
        <SectionHead
          n={3}
          title={lang === 'en' ? '5-minute debrief' : 'Debrief 5 menit'}
          note={
            edition === 'combined'
              ? lang === 'en'
                ? 'A short check-in for both of you'
                : 'Obrolan singkat untuk kalian berdua'
              : lang === 'en'
                ? 'A short check-in with yourself'
                : 'Obrolan singkat dengan diri sendiri'
          }
        />
        <div className="card p-4">
          {debriefPrompts.map((prompt, i) => (
            <PromptField
              key={i}
              label={t(prompt)}
              getValue={(role: Role) => debriefRec[role]?.[i] ?? ''}
              onChange={(role, value) => setDebrief(num, role, i, value)}
              rows={2}
            />
          ))}
          <p className="text-center text-xs text-ceria-gray/80">
            {lang === 'en'
              ? 'Saved automatically on this device.'
              : 'Tersimpan otomatis di perangkat ini.'}
          </p>
        </div>
      </div>
    </Screen>
  )
}

function SectionHead({ n, title, note }: { n: number; title: string; note: string }) {
  return (
    <div className="mb-2 mt-7 flex items-center gap-2.5">
      <span className="flex h-7 w-7 items-center justify-center rounded-full bg-ceria-blue/8 text-sm font-semibold text-ceria-blue">
        {n}
      </span>
      <div>
        <h2 className="font-head text-lg font-semibold leading-none text-ceria-blue">{title}</h2>
        <p className="mt-0.5 text-xs text-ceria-gray">{note}</p>
      </div>
    </div>
  )
}
