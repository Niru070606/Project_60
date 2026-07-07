import { Routes, Route } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Dashboard from "../pages/Dashboard";
import Chat from "../pages/Chat";
import Memory from "../pages/Memory";
import Mood from "../pages/Mood";
import Personality from "../pages/Personality";
import Survey from "../pages/Survey";
import Analytics from "../pages/Analytics";
import History from "../pages/History";
import Settings from "../pages/Settings";

export default function AppRoutes() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route index element={<Dashboard />} />
        <Route path="chat" element={<Chat />} />
        <Route path="memory" element={<Memory />} />
        <Route path="mood" element={<Mood />} />
        <Route path="personality" element={<Personality />} />
        <Route path="survey" element={<Survey />} />
        <Route path="analytics" element={<Analytics />} />
        <Route path="history" element={<History />} />
        <Route path="settings" element={<Settings />} />
      </Route>
    </Routes>
  );
}
