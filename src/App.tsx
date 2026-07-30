import { HashRouter, Navigate, Route, Routes } from 'react-router-dom'
import { AppProvider, useApp } from './store/AppContext'
import { PaywallProvider } from './components/PaywallProvider'
import TabBar from './components/TabBar'
import Onboarding from './screens/Onboarding'
import Today from './screens/Today'
import Guidebook from './screens/Guidebook'
import GuidebookChapter from './screens/GuidebookChapter'
import Toolkit from './screens/Toolkit'
import ToolkitTool from './screens/ToolkitTool'
import Diary from './screens/Diary'
import DiaryWeek from './screens/DiaryWeek'
import More from './screens/More'

export default function App() {
  return (
    <AppProvider>
      <PaywallProvider>
        <Shell />
      </PaywallProvider>
    </AppProvider>
  )
}

function Shell() {
  const { ready, settings } = useApp()

  // Fixed phone-width frame, centered on larger screens.
  return (
    <div className="mx-auto flex h-full max-w-md flex-col bg-ceria-cream shadow-xl">
      {!ready ? (
        <Splash />
      ) : !settings.onboarded ? (
        <Onboarding />
      ) : (
        <HashRouter>
          <div className="flex min-h-0 flex-1 flex-col">
            <Routes>
              <Route path="/today" element={<Today />} />
              <Route path="/guidebook" element={<Guidebook />} />
              <Route path="/guidebook/:n" element={<GuidebookChapter />} />
              <Route path="/toolkit" element={<Toolkit />} />
              <Route path="/toolkit/:n" element={<ToolkitTool />} />
              <Route path="/diary" element={<Diary />} />
              <Route path="/diary/:week" element={<DiaryWeek />} />
              <Route path="/more" element={<More />} />
              <Route path="*" element={<Navigate to="/today" replace />} />
            </Routes>
          </div>
          <TabBar />
        </HashRouter>
      )}
    </div>
  )
}

function Splash() {
  return (
    <div className="flex flex-1 flex-col items-center justify-center gap-4">
      <img src="./logo.jpg" alt="Ceria" className="h-20 w-20 animate-pulse rounded-3xl object-cover" />
      <p className="font-head text-lg text-ceria-blue">Ceria</p>
    </div>
  )
}
