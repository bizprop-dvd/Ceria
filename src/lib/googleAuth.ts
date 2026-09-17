import { App } from '@capacitor/app'
import { Browser } from '@capacitor/browser'
import { Capacitor } from '@capacitor/core'
import { getJSON, setJSON, KEYS } from './storage'

/**
 * Google sign-in for Drive backup, using OAuth with PKCE in the system browser.
 *
 * PKCE means no client secret is ever shipped inside the app — a secret in a
 * downloadable app is not a secret. Google also requires the system browser
 * rather than an in-app webview for sign-in, which is why this opens Browser
 * and listens for the redirect back.
 *
 * SCOPE: 'drive.file' only — the app can see just the files it created itself,
 * never the rest of the parent's Drive. This matters beyond privacy: broader
 * Drive scopes put the project into Google's restricted tier, which requires a
 * paid third-party security assessment every year.
 *
 * NOT YET RUNNABLE. It needs OAuth client IDs from the foundation's Google
 * Cloud project (see .env.example). Until those exist isConfigured() is false
 * and the UI hides Drive entirely.
 */

const SCOPE = 'https://www.googleapis.com/auth/drive.file email'
const AUTH_ENDPOINT = 'https://accounts.google.com/o/oauth2/v2/auth'
const TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token'

const IOS_CLIENT_ID = import.meta.env.VITE_GOOGLE_IOS_CLIENT_ID as string | undefined
const ANDROID_CLIENT_ID = import.meta.env.VITE_GOOGLE_ANDROID_CLIENT_ID as string | undefined
/** Reverse-DNS form of the client id, e.g. com.googleusercontent.apps.123-abc */
const REDIRECT_SCHEME = import.meta.env.VITE_GOOGLE_REDIRECT_SCHEME as string | undefined

export interface GoogleSession {
  accessToken: string
  refreshToken: string | null
  /** epoch ms */
  expiresAt: number
  email: string | null
}

export function isConfigured(): boolean {
  if (!Capacitor.isNativePlatform()) return false
  const id = Capacitor.getPlatform() === 'ios' ? IOS_CLIENT_ID : ANDROID_CLIENT_ID
  return Boolean(id && REDIRECT_SCHEME)
}

function clientId(): string {
  const id = Capacitor.getPlatform() === 'ios' ? IOS_CLIENT_ID : ANDROID_CLIENT_ID
  if (!id) throw new Error('Google client id not configured')
  return id
}

/* ---------- PKCE ---------- */

function base64url(bytes: Uint8Array): string {
  let s = ''
  bytes.forEach((b) => (s += String.fromCharCode(b)))
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

function randomVerifier(): string {
  return base64url(crypto.getRandomValues(new Uint8Array(64)))
}

async function challengeFor(verifier: string): Promise<string> {
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(verifier))
  return base64url(new Uint8Array(digest))
}

/* ---------- sign in ---------- */

/**
 * Opens Google in the system browser and resolves once the parent comes back.
 * Rejects if they close the browser without finishing.
 */
export async function signIn(): Promise<GoogleSession> {
  if (!isConfigured()) throw new Error('Google sign-in is not configured in this build')

  const verifier = randomVerifier()
  const challenge = await challengeFor(verifier)
  const state = base64url(crypto.getRandomValues(new Uint8Array(16)))
  const redirectUri = `${REDIRECT_SCHEME}:/oauth2redirect`

  const url =
    `${AUTH_ENDPOINT}?client_id=${encodeURIComponent(clientId())}` +
    `&redirect_uri=${encodeURIComponent(redirectUri)}` +
    `&response_type=code&scope=${encodeURIComponent(SCOPE)}` +
    `&code_challenge=${challenge}&code_challenge_method=S256` +
    `&state=${state}&access_type=offline&prompt=consent`

  const code = await new Promise<string>((resolve, reject) => {
    let settled = false
    const finish = (fn: () => void) => {
      if (settled) return
      settled = true
      void listener.then((l) => l.remove())
      void closed.then((l) => l.remove())
      fn()
    }

    const listener = App.addListener('appUrlOpen', ({ url: incoming }) => {
      if (!incoming.startsWith(redirectUri)) return
      const params = new URLSearchParams(incoming.split('?')[1] ?? '')
      void Browser.close()
      if (params.get('state') !== state) return finish(() => reject(new Error('state mismatch')))
      const got = params.get('code')
      if (!got) return finish(() => reject(new Error(params.get('error') ?? 'no code')))
      finish(() => resolve(got))
    })

    // If they back out of the browser, don't hang forever.
    const closed = Browser.addListener('browserFinished', () =>
      finish(() => reject(new Error('cancelled'))),
    )

    void Browser.open({ url })
  })

  const session = await exchange({
    grant_type: 'authorization_code',
    code,
    client_id: clientId(),
    redirect_uri: redirectUri,
    code_verifier: verifier,
  })
  await setJSON(KEYS.googleSession, session)
  return session
}

async function exchange(body: Record<string, string>): Promise<GoogleSession> {
  const res = await fetch(TOKEN_ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(body).toString(),
  })
  if (!res.ok) throw new Error(`Google token request failed (${res.status})`)
  const json = (await res.json()) as {
    access_token: string
    refresh_token?: string
    expires_in: number
    id_token?: string
  }
  return {
    accessToken: json.access_token,
    refreshToken: json.refresh_token ?? null,
    expiresAt: Date.now() + json.expires_in * 1000,
    email: emailFromIdToken(json.id_token),
  }
}

function emailFromIdToken(idToken?: string): string | null {
  if (!idToken) return null
  try {
    const claims = JSON.parse(atob(idToken.split('.')[1].replace(/-/g, '+').replace(/_/g, '/')))
    return typeof claims.email === 'string' ? claims.email : null
  } catch {
    return null
  }
}

/** A valid access token, refreshed if needed. Null if not signed in. */
export async function getAccessToken(): Promise<string | null> {
  const session = await getJSON<GoogleSession | null>(KEYS.googleSession, null)
  if (!session) return null
  if (Date.now() < session.expiresAt - 60_000) return session.accessToken
  if (!session.refreshToken) return null
  try {
    const refreshed = await exchange({
      grant_type: 'refresh_token',
      refresh_token: session.refreshToken,
      client_id: clientId(),
    })
    // Google does not resend the refresh token on a refresh; keep the old one.
    const merged = { ...refreshed, refreshToken: refreshed.refreshToken ?? session.refreshToken }
    await setJSON(KEYS.googleSession, merged)
    return merged.accessToken
  } catch {
    return null
  }
}

export async function currentEmail(): Promise<string | null> {
  const session = await getJSON<GoogleSession | null>(KEYS.googleSession, null)
  return session?.email ?? null
}

export async function isSignedIn(): Promise<boolean> {
  return (await getJSON<GoogleSession | null>(KEYS.googleSession, null)) !== null
}

/**
 * Disconnect. Revokes the token with Google so the app's access really ends,
 * not just locally — Apple requires an in-app way to undo this.
 */
export async function signOut(): Promise<void> {
  const session = await getJSON<GoogleSession | null>(KEYS.googleSession, null)
  if (session) {
    try {
      await fetch(`https://oauth2.googleapis.com/revoke?token=${session.accessToken}`, {
        method: 'POST',
      })
    } catch {
      // Best effort — the local session is cleared regardless.
    }
  }
  await setJSON(KEYS.googleSession, null)
}
