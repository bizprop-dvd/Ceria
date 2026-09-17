// Opt-in evening reminder via @capacitor/local-notifications.
//
// Gentle by design: the reminder never shames. Copy is an invitation, not a
// nag. Scheduling is a no-op in the browser (no native notifications there).

import { Capacitor } from '@capacitor/core'

const REMINDER_ID = 1001

const REMINDER_TEXT = {
  en: {
    title: 'A quiet moment with Ceria',
    body: 'Whenever you have a minute — even one line about today is enough.',
  },
  id: {
    title: 'Sejenak bersama Ceria',
    body: 'Kapan pun Anda sempat — satu baris tentang hari ini pun sudah cukup.',
  },
}

export function notificationsSupported(): boolean {
  return Capacitor.isNativePlatform()
}

/** Ask for permission. Returns true if granted. */
export async function requestNotificationPermission(): Promise<boolean> {
  if (!notificationsSupported()) return false
  const { LocalNotifications } = await import('@capacitor/local-notifications')
  const res = await LocalNotifications.requestPermissions()
  return res.display === 'granted'
}

/**
 * Schedule (or reschedule) a daily reminder at hh:mm local time.
 * Pass null to cancel.
 */
export async function scheduleEveningReminder(
  time: { hour: number; minute: number } | null,
  lang: 'en' | 'id',
): Promise<void> {
  if (!notificationsSupported()) return
  const { LocalNotifications } = await import('@capacitor/local-notifications')

  // Always clear the existing one first so we don't stack duplicates.
  await LocalNotifications.cancel({ notifications: [{ id: REMINDER_ID }] })
  if (!time) return

  const text = REMINDER_TEXT[lang]
  await LocalNotifications.schedule({
    notifications: [
      {
        id: REMINDER_ID,
        title: text.title,
        body: text.body,
        schedule: {
          on: { hour: time.hour, minute: time.minute },
          allowWhileIdle: true,
        },
      },
    ],
  })
}
