interface Option<T extends string> {
  value: T
  label: string
}

interface SegmentedProps<T extends string> {
  value: T
  options: Option<T>[]
  onChange: (value: T) => void
}

/** A small segmented control used for language and edition pickers. */
export default function Segmented<T extends string>({ value, options, onChange }: SegmentedProps<T>) {
  return (
    <div className="inline-flex rounded-full bg-ceria-cream-deep p-1">
      {options.map((opt) => {
        const active = opt.value === value
        return (
          <button
            key={opt.value}
            onClick={() => onChange(opt.value)}
            className={`rounded-full px-4 py-1.5 text-sm font-medium transition ${
              active ? 'bg-white text-ceria-blue shadow-card' : 'text-ceria-gray'
            }`}
          >
            {opt.label}
          </button>
        )
      })}
    </div>
  )
}
