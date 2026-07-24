import { useState } from "react";
import { useNavigate } from "react-router-dom";
import DashboardLayout from "../../components/Layout/DashboardLayout";
import { changePassword } from "../../services/settingsService";

const Settings = () => {
  const navigate = useNavigate();

  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handlePasswordChange = async () => {
    if (!currentPassword || !newPassword || !confirmPassword) {
      alert("Please fill all fields.");
      return;
    }

    if (newPassword !== confirmPassword) {
      alert("New password and confirm password do not match.");
      return;
    }

    try {
      const response = await changePassword({
        currentPassword,
        newPassword,
      });

      alert(response.data.message);

      setCurrentPassword("");
      setNewPassword("");
      setConfirmPassword("");
    } catch (error) {
      alert(
        error.response?.data?.message ||
          "Failed to update password."
      );
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");

    navigate("/login");
  };

  return (
    <DashboardLayout>
      <div className="mx-auto max-w-3xl space-y-8">

        <div className="rounded-2xl border border-white/10 bg-white/5 p-8">
          <h1 className="mb-8 text-3xl font-bold text-white">
            ⚙️ Settings
          </h1>

          <h2 className="mb-6 text-xl font-semibold text-white">
            Change Password
          </h2>

          <div className="space-y-5">

            <input
              type="password"
              placeholder="Current Password"
              value={currentPassword}
              onChange={(e) =>
                setCurrentPassword(e.target.value)
              }
              className="w-full rounded-xl border border-white/10 bg-[#111] p-3 text-white outline-none"
            />

            <input
              type="password"
              placeholder="New Password"
              value={newPassword}
              onChange={(e) =>
                setNewPassword(e.target.value)
              }
              className="w-full rounded-xl border border-white/10 bg-[#111] p-3 text-white outline-none"
            />

            <input
              type="password"
              placeholder="Confirm New Password"
              value={confirmPassword}
              onChange={(e) =>
                setConfirmPassword(e.target.value)
              }
              className="w-full rounded-xl border border-white/10 bg-[#111] p-3 text-white outline-none"
            />

            <button
              onClick={handlePasswordChange}
              className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:bg-blue-700"
            >
              Update Password
            </button>

          </div>
        </div>

        <div className="rounded-2xl border border-red-500/30 bg-red-500/10 p-8">

          <h2 className="mb-4 text-2xl font-bold text-red-400">
            Logout
          </h2>

          <p className="mb-6 text-gray-300">
            Logout from your current session.
          </p>

          <button
            onClick={handleLogout}
            className="rounded-xl bg-red-600 px-6 py-3 font-semibold text-white transition hover:bg-red-700"
          >
            Logout
          </button>

        </div>

      </div>
    </DashboardLayout>
  );
};

export default Settings;