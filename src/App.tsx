import { Suspense, lazy } from 'react'
import { HashRouter, Navigate, Route, Routes } from 'react-router-dom'
import { AppProvider, useApp } from './store/AppContext'
import { PaywallProvider } from './components/PaywallProvider'
import TabBar from './components/TabBar'
import Onboarding from './screens/Onboarding'
import Today from './screens/Today'

// Today and the onboarding are what a parent sees when the app opens, so they
// ship in the first file. The rest arrive when they are opened — on a cheap
// phone that is the difference between the app appearing and the app thinking.
const Guidebook = lazy(() => import('./screens/Guidebook'))
const GuidebookChapter = lazy(() => import('./screens/GuidebookChapter'))
const DailyDay = lazy(() => import('./screens/DailyDay'))
const YearMap = lazy(() => import('./screens/YearMap'))
const Toolkit = lazy(() => import('./screens/Toolkit'))
const ToolkitTool = lazy(() => import('./screens/ToolkitTool'))
const Diary = lazy(() => import('./screens/Diary'))
const DiaryWeek = lazy(() => import('./screens/DiaryWeek'))
const DiaryAbout = lazy(() => import('./screens/DiaryAbout'))
const More = lazy(() => import('./screens/More'))

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
    <div className="relative mx-auto flex h-full max-w-md flex-col overflow-hidden bg-ceria-cream shadow-xl">
      {!ready ? (
        <Splash />
      ) : !settings.onboarded ? (
        <Onboarding />
      ) : (
        <HashRouter>
          <div className="flex min-h-0 flex-1 flex-col">
            <Suspense fallback={<ScreenLoading />}>
              <Routes>
                <Route path="/today" element={<Today />} />
                <Route path="/guidebook" element={<Guidebook />} />
                <Route path="/guidebook/year" element={<YearMap />} />
                <Route path="/guidebook/day/:d" element={<DailyDay />} />
                <Route path="/guidebook/:n" element={<GuidebookChapter />} />
                <Route path="/toolkit" element={<Toolkit />} />
                <Route path="/toolkit/:n" element={<ToolkitTool />} />
                <Route path="/diary" element={<Diary />} />
                <Route path="/diary/about" element={<DiaryAbout />} />
                <Route path="/diary/:week" element={<DiaryWeek />} />
                <Route path="/more" element={<More />} />
                <Route path="*" element={<Navigate to="/today" replace />} />
              </Routes>
            </Suspense>
          </div>
          <TabBar />
        </HashRouter>
      )}
    </div>
  )
}

/**
 * Held while a screen's code is read from the app's own files — normally a
 * frame or two. Deliberately blank rather than a spinner: a spinner that
 * flashes for 30ms reads as a stutter.
 */
function ScreenLoading() {
  return <div className="flex-1" aria-hidden />
}

function Splash() {
  return (
    <div className="flex flex-1 flex-col items-center justify-center gap-4">
      <img src="./logo.jpg" alt="Ceria" className="h-20 w-20 animate-pulse rounded-3xl object-cover" />
      <p className="font-head text-lg text-ceria-blue">Ceria</p>
    </div>
  )
}
