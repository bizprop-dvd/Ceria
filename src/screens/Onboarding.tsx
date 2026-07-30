import { useState } from 'react'
import { useApp } from '../store/AppContext'
import { dayKey } from '../lib/dates'
import { ABOUT } from '../config'
import { HeartIcon } from '../components/icons'
import type { Edition, Lang } from '../data/types'

type Step = 'welcome' | 'language' | 'edition'

export default function Onboarding() {
  const { completeOnboarding } = useApp()
  const [step, setStep] = useState<Step>('welcome')
  const [lang, setLang] = useState<Lang>('en')
  const [edition, setEdition] = useState<Edition>('combined')

  const finish = () => completeOnboarding({ lang, edition, startDate: dayKey() })

  return (
    <div
      className="flex h-full flex-col bg-gradient-to-b from-ceria-cream to-ceria-cream-deep/60 px-6"
      style={{ paddingTop: 'calc(var(--safe-top) + 2rem)', paddingBottom: 'calc(var(--safe-bottom) + 1.5rem)' }}
    >
      {step === 'welcome' && <Welcome lang={lang} onNext={() => setStep('language')} />}
      {step === 'language' && (
        <LanguagePick value={lang} onPick={setLang} onNext={() => setStep('edition')} />
      )}
      {step === 'edition' && (
        <EditionPick lang={lang} value={edition} onPick={setEdition} onFinish={finish} />
      )}

      <Dots step={step} />
    </div>
  )
}

function Welcome({ lang, onNext }: { lang: Lang; onNext: () => void }) {
  const about = ABOUT[lang]
  return (
    <div className="flex flex-1 flex-col items-center justify-center text-center">
      <img src="./logo.jpg" alt="Ceria" className="mb-6 h-24 w-24 rounded-3xl object-cover shadow-card" />
      <h1 className="font-head text-3xl font-semibold text-ceria-blue">
        {lang === 'en' ? 'Welcome to Ceria' : 'Selamat datang di Ceria'}
      </h1>
      <p className="mt-3 max-w-sm text-[15px] leading-relaxed text-ceria-dark/80">{about.mission}</p>
      <div className="mt-4 flex max-w-sm items-start gap-2 rounded-2xl bg-ceria-teal/8 px-4 py-3 text-left">
        <HeartIcon width={20} height={20} className="mt-0.5 shrink-0 text-ceria-teal" />
        <p className="text-[13px] leading-relaxed text-ceria-dark/75">{about.proceeds}</p>
      </div>
      <button className="btn-primary mt-8 w-full max-w-sm" onClick={onNext}>
        {lang === 'en' ? 'Get started' : 'Mulai'}
      </button>
    </div>
  )
}

function LanguagePick({
  value,
  onPick,
  onNext,
}: {
  value: Lang
  onPick: (l: Lang) => void
  onNext: () => void
}) {
  return (
    <div className="flex flex-1 flex-col justify-center">
      <h2 className="font-head text-2xl font-semibold text-ceria-blue">Choose your language</h2>
      <p className="mt-1 text-sm text-ceria-gray">Pilih bahasa Anda</p>
      <div className="mt-6 space-y-3">
        <BigChoice active={value === 'en'} title="English" subtitle="Read the app in English" onClick={() => onPick('en')} />
        <BigChoice active={value === 'id'} title="Bahasa Indonesia" subtitle="Baca aplikasi dalam Bahasa Indonesia" onClick={() => onPick('id')} />
      </div>
      <button className="btn-primary mt-8 w-full" onClick={onNext}>
        {value === 'en' ? 'Continue' : 'Lanjut'}
      </button>
    </div>
  )
}

function EditionPick({
  lang,
  value,
  onPick,
  onFinish,
}: {
  lang: Lang
  value: Edition
  onPick: (e: Edition) => void
  onFinish: () => void
}) {
  return (
    <div className="flex flex-1 flex-col justify-center">
      <h2 className="font-head text-2xl font-semibold text-ceria-blue">
        {lang === 'en' ? 'How will you journal?' : 'Bagaimana Anda akan menulis diari?'}
      </h2>
      <p className="mt-1 text-sm text-ceria-gray">
        {lang === 'en' ? 'You can change this anytime in More.' : 'Anda bisa mengubahnya kapan saja di Lainnya.'}
      </p>
      <div className="mt-6 space-y-3">
        <BigChoice
          active={value === 'combined'}
          title={lang === 'en' ? 'Parents — Mama & Papa' : 'Orang Tua — Mama & Papa'}
          subtitle={
            lang === 'en'
              ? 'Two gentle columns, one for each parent.'
              : 'Dua kolom lembut, satu untuk setiap orang tua.'
          }
          onClick={() => onPick('combined')}
        />
        <BigChoice
          active={value === 'solo'}
          title={lang === 'en' ? 'Single parent' : 'Orang Tua Tunggal'}
          subtitle={
            lang === 'en' ? 'A single space, just for you.' : 'Satu ruang, khusus untuk Anda.'
          }
          onClick={() => onPick('solo')}
        />
      </div>
      <button className="btn-primary mt-8 w-full" onClick={onFinish}>
        {lang === 'en' ? 'Enter Ceria' : 'Masuk ke Ceria'}
      </button>
    </div>
  )
}

function BigChoice({
  active,
  title,
  subtitle,
  onClick,
}: {
  active: boolean
  title: string
  subtitle: string
  onClick: () => void
}) {
  return (
    <button
      onClick={onClick}
      className={`w-full rounded-2xl border-2 p-4 text-left transition active:scale-[0.99] ${
        active ? 'border-ceria-blue bg-white shadow-card' : 'border-transparent bg-white/70'
      }`}
    >
      <p className="font-head text-lg font-semibold text-ceria-dark">{title}</p>
      <p className="mt-0.5 text-sm text-ceria-gray">{subtitle}</p>
    </button>
  )
}

function Dots({ step }: { step: Step }) {
  const order: Step[] = ['welcome', 'language', 'edition']
  return (
    <div className="flex justify-center gap-2 pt-4">
      {order.map((s) => (
        <span
          key={s}
          className={`h-1.5 rounded-full transition-all ${
            s === step ? 'w-6 bg-ceria-blue' : 'w-1.5 bg-ceria-cream-deep'
          }`}
        />
      ))}
    </div>
  )
}
