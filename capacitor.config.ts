import type { CapacitorConfig } from '@capacitor/cli'

const config: CapacitorConfig = {
  appId: 'id.or.ceria.app',
  appName: 'Ceria',
  webDir: 'dist',
  backgroundColor: '#FAF6EE',
  plugins: {
    LocalNotifications: {
      smallIcon: 'ic_stat_icon',
      iconColor: '#2E4FA3',
    },
  },
}

export default config
