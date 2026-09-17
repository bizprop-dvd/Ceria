import { readFileSync } from 'node:fs'
import { defineConfig, type Plugin } from 'vite'
import react from '@vitejs/plugin-react'
import { viteSingleFile } from 'vite-plugin-singlefile'

// Builds one self-contained .html file for sharing with reviewers who should
// not need GitHub, a terminal, or a server. Not used by the app or Capacitor.
//
// vite-plugin-singlefile inlines the bundled JS and CSS, but files served from
// public/ are copied rather than bundled, so the logo would 404 when the page
// is opened from disk. inlinePublicImages() rewrites those references to data
// URIs after the HTML is generated.
function inlinePublicImages(files: string[]): Plugin {
  return {
    name: 'ceria:inline-public-images',
    enforce: 'post',
    generateBundle(_opts, bundle) {
      const uris = new Map(
        files.map((f) => [f, `data:image/jpeg;base64,${readFileSync(`public/${f}`).toString('base64')}`]),
      )
      for (const asset of Object.values(bundle)) {
        if (asset.type !== 'asset' || !asset.fileName.endsWith('.html')) continue
        let html = asset.source as string
        for (const [name, uri] of uris) {
          html = html.split(`./${name}`).join(uri).split(`/${name}`).join(uri)
        }
        asset.source = html
      }
    },
  }
}

export default defineConfig({
  plugins: [react(), viteSingleFile(), inlinePublicImages(['logo.jpg'])],
  base: './',
  build: {
    outDir: 'preview-dist',
    assetsInlineLimit: 100000000,
    cssCodeSplit: false,
    reportCompressedSize: false,
  },
})
