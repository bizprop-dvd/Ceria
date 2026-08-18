import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Capacitor loads the built web assets from the local filesystem inside the
// native webview, so we use relative asset paths (base: './').
export default defineConfig({
  plugins: [react()],
  base: './',
  server: {
    host: true,
    port: 5173,
  },
  build: {
    outDir: 'dist',
  },
})
