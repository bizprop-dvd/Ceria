/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_REVENUECAT_IOS_KEY?: string
  readonly VITE_REVENUECAT_ANDROID_KEY?: string
  /** overrides where the News tab reads Ceria's updates from (see src/lib/news.ts) */
  readonly VITE_NEWS_URL?: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
