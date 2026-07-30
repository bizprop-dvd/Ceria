/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_REVENUECAT_IOS_KEY?: string
  readonly VITE_REVENUECAT_ANDROID_KEY?: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
