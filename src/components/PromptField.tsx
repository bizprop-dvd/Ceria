import { useApp } from '../store/AppContext'
import type { Role } from '../data/types'

const ROLE_LABEL: Record<Role, { en: string; id: string }> = {
  solo: { en: 'You', id: 'Anda' },
  mama: { en: 'Mama', id: 'Mama' },
  papa: { en: 'Papa', id: 'Papa' },
}

interface PromptFieldProps {
  label: string
  hint?: string
  getValue: (role: Role) => string
  onChange: (role: Role, value: string) => void
  rows?: number
  placeholder?: string
}

/**
 * Renders one prompt. In the Combined edition it shows two gentle sub-columns
 * (Mama / Papa); in Solo it shows a single input. Autosaves on every keystroke
 * via the onChange handler (persistence is debounced in the store's effect).
 */
export default function PromptField({
  label,
  hint,
  getValue,
  onChange,
  rows = 3,
  placeholder,
}: PromptFieldProps) {
  const { roles, lang } = useApp()
  const combined = roles.length > 1

  return (
    <div className="mb-5">
      <label className="mb-1.5 block font-head text-[15px] font-semibold text-ceria-dark">
        {label}
      </label>
      {hint && <p className="mb-2 text-xs text-ceria-gray">{hint}</p>}
      <div className={combined ? 'grid grid-cols-1 gap-3 sm:grid-cols-2' : ''}>
        {roles.map((role) => (
          <div key={role}>
            {combined && (
              <span className="mb-1 block text-xs font-semibold uppercase tracking-wide text-ceria-teal">
                {ROLE_LABEL[role][lang]}
              </span>
            )}
            <textarea
              className="field resize-none"
              rows={rows}
              placeholder={placeholder}
              value={getValue(role)}
              onChange={(e) => onChange(role, e.target.value)}
            />
          </div>
        ))}
      </div>
    </div>
  )
}
