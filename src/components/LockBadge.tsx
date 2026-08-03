import { useApp } from '../store/AppContext'
import { LockIcon } from './icons'

/** Small "locked" chip shown on paid items in list views. */
export default function LockBadge() {
  const { lang } = useApp()
  return (
    <span className="chip shrink-0 whitespace-nowrap bg-ceria-cream-deep text-ceria-gray">
      <LockIcon width={13} height={13} />
      {lang === 'en' ? 'Locked' : 'Terkunci'}
    </span>
  )
}
