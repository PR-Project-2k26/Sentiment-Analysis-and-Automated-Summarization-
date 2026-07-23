import { BrowserRouter, Routes, Route } from "react-router-dom";

// Landing Page
import Home from "../pages/Landing/Home";

// Authentication Pages
import Login from "../pages/Auth/Login";
import Register from "../pages/Auth/Register";
import ForgotPassword from "../pages/Auth/ForgotPassword";

// Dashboard
import Dashboard from "../pages/Dashboard/Dashboard";

// History
import History from "../pages/History/History";

// AI Module Pages
import Resume from "../pages/Modules/Resume";
import PDF from "../pages/Modules/PDF";
import Video from "../pages/Modules/Video";
import Audio from "../pages/Modules/Audio";
import Text from "../pages/Modules/Text";

// User Pages
import Profile from "../pages/Profile/Profile";
import Settings from "../pages/Settings/Settings";

// Protected Route
import ProtectedRoute from "./ProtectedRoute";

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

        {/* Protected Routes */}

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/history"
          element={
            <ProtectedRoute>
              <History />
            </ProtectedRoute>
          }
        />

        <Route
          path="/resume"
          element={
            <ProtectedRoute>
              <Resume />
            </ProtectedRoute>
          }
        />

        <Route
          path="/pdf"
          element={
            <ProtectedRoute>
              <PDF />
            </ProtectedRoute>
          }
        />

        <Route
          path="/video"
          element={
            <ProtectedRoute>
              <Video />
            </ProtectedRoute>
          }
        />

        <Route
          path="/audio"
          element={
            <ProtectedRoute>
              <Audio />
            </ProtectedRoute>
          }
        />

        <Route
          path="/text"
          element={
            <ProtectedRoute>
              <Text />
            </ProtectedRoute>
          }
        />

        <Route
          path="/profile"
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          }
        />

        <Route
          path="/settings"
          element={
            <ProtectedRoute>
              <Settings />
            </ProtectedRoute>
          }
        />

        {/* 404 Page */}
        <Route
          path="*"
          element={
            <div className="min-h-screen flex items-center justify-center bg-[#09090B] text-4xl font-bold text-white">
              404 | Page Not Found
            </div>
          }
        />

      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;