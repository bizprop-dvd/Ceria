import Screen from '../components/Screen'
import { diaryIntro } from '../data/content'
import { useApp } from '../store/AppContext'

export default function DiaryAbout() {
  const { t, lang, edition } = useApp()
  const welcome = diaryIntro.welcome[edition]
  const habits = diaryIntro.howToUse[edition]
  const setup = diaryIntro.settingUp[edition].prompts

  return (
    <Screen back title={lang === 'en' ? 'How this diary works' : 'Cara kerja diari ini'}>
      <article className="mx-auto max-w-prose pt-2">
        {/* Welcome */}
        <div className="card p-4">
          <h2 className="font-head text-lg font-semibold text-ceria-blue">
            {lang === 'en' ? 'A note before you begin' : 'Sepatah kata sebelum memulai'}
          </h2>
          <p className="mt-2 whitespace-pre-line text-[15px] leading-relaxed text-ceria-dark/85">
            {t(welcome)}
          </p>
        </div>

        {/* How to use — five habits */}
        <h2 className="mb-2 mt-6 font-head text-lg font-semibold text-ceria-blue">
          {lang === 'en' ? 'Five small habits' : 'Lima kebiasaan kecil'}
        </h2>
        <ol className="space-y-2.5">
          {habits.map((h, i) => (
            <li key={i} className="card flex gap-3 p-4">
              <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-ceria-teal/12 text-sm font-semibold text-ceria-teal">
                {i + 1}
              </span>
              <div>
                <p className="font-head text-[15px] font-semibold text-ceria-dark">{t(h.title)}</p>
                <p className="mt-0.5 text-sm leading-relaxed text-ceria-gray">{t(h.body)}</p>
              </div>
            </li>
          ))}
        </ol>

        {/* Setting up the year */}
        <h2 className="mb-1.5 mt-6 font-head text-lg font-semibold text-ceria-blue">
          {lang === 'en' ? 'Setting up the year' : 'Menyiapkan tahun ini'}
        </h2>
        <p className="mb-2 text-sm text-ceria-gray">{t(diaryIntro.settingUp.intro)}</p>
        <ul className="space-y-2">
          {setup.map((p, i) => (
            <li key={i} className="card bg-ceria-cream-deep/40 p-3.5">
              <p className="font-head text-[15px] leading-snug text-ceria-dark">{t(p)}</p>
            </li>
          ))}
        </ul>
      </article>
    </Screen>
  )
}
