import { useLayoutEffect, useRef, type TextareaHTMLAttributes } from 'react'

interface AutoTextareaProps extends TextareaHTMLAttributes<HTMLTextAreaElement> {
  /** Minimum height, in lines of text. */
  minRows?: number
}

/**
 * A textarea that grows to fit what has been written.
 *
 * The `rows` attribute sizes a textarea using the browser's default
 * line-height, which is shorter than the app's `leading-relaxed`, so a plain
 * `rows={3}` box clips its own third line. More importantly, a parent writing
 * a long entry should never have part of it scrolled out of sight — this is a
 * diary, and seeing what you wrote is the point.
 */
export default function AutoTextarea({ minRows = 3, className = '', ...props }: AutoTextareaProps) {
  const ref = useRef<HTMLTextAreaElement>(null)

  useLayoutEffect(() => {
    const el = ref.current
    if (!el) return
    el.style.height = 'auto'
    const line = parseFloat(getComputedStyle(el).lineHeight) || 24
    const padding = el.offsetHeight - el.clientHeight + parseFloat(getComputedStyle(el).paddingTop) * 2
    el.style.height = `${Math.max(el.scrollHeight, minRows * line + padding)}px`
  }, [props.value, minRows])

  return (
    <textarea
      ref={ref}
      className={`field resize-none overflow-hidden ${className}`}
      {...props}
    />
  )
}
