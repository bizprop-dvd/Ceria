/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        ceria: {
          blue: '#2E4FA3',
          pink: '#E91E80',
          cream: '#FAF6EE',
          'cream-deep': '#F2E9D9',
          dark: '#1F2937',
          gray: '#6B7280',
          teal: '#0E9488',
        },
      },
      fontFamily: {
        // Warm serif for headings, clean sans for body.
        serif: ['Lora', 'Georgia', 'Cambria', 'Times New Roman', 'serif'],
        sans: ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      borderRadius: {
        xl: '1rem',
        '2xl': '1.25rem',
      },
      boxShadow: {
        card: '0 2px 12px rgba(31, 41, 55, 0.06)',
        sheet: '0 -8px 30px rgba(31, 41, 55, 0.15)',
      },
    },
  },
  plugins: [],
}
