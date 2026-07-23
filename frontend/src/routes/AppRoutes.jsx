import { BrowserRouter, Routes, Route } from "react-router-dom";

// Landing Page
import Home from "../pages/Landing/Home";

// Authentication Pages
import Login from "../pages/Auth/Login";
import Register from "../pages/Auth/Register";
import ForgotPassword from "../pages/Auth/ForgotPassword";

// Dashboard
import Dashboard from "../pages/Dashboard/Dashboard";

// AI Module Pages
import Resume from "../pages/Modules/Resume";
import PDF from "../pages/Modules/PDF";
import Video from "../pages/Modules/Video";
import Audio from "../pages/Modules/Audio";
import Text from "../pages/Modules/Text";
import Profile from "../pages/Profile/Profile";
import Settings from "../pages/Settings/Settings";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        {/* Landing Page */}
        <Route path="/" element={<Home />} />

        {/* Authentication */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />

        {/* Dashboard */}
        <Route path="/dashboard" element={<Dashboard />} />

        {/* AI Modules */}
        <Route path="/resume" element={<Resume />} />
        <Route path="/pdf" element={<PDF />} />
        <Route path="/video" element={<Video />} />
        <Route path="/audio" element={<Audio />} />
        <Route path="/text" element={<Text />} />

        <Route path="/profile" element={<Profile />} />
        <Route path="/settings" element={<Settings />} />

        {/* 404 Page */}
        <Route
          path="*"
          element={
            <div className="min-h-screen bg-[#09090B] flex items-center justify-center text-white text-4xl font-bold">
              404 | Page Not Found
            </div>
          }
        />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;