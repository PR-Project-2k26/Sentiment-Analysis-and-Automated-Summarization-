import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../../services/api";

import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import PasswordInput from "../../components/Authentication/PasswordInput";

const ResetPassword = () => {
  const { token } = useParams();
  const navigate = useNavigate();

  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [isError, setIsError] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);
    setMessage("");

    try {
      const response = await api.post(
        `/auth/reset-password/${token}`,
        {
          password,
        }
      );

      setIsError(false);
      setMessage(response.data.message);

      setTimeout(() => {
        navigate("/login");
      }, 2000);

    } catch (error) {
      setIsError(true);

      setMessage(
        error.response?.data?.message ||
        "Failed to reset password."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthLayout>
      <AuthCard>

        <div className="mb-8">
          <h2 className="text-3xl font-bold text-white">
            Reset Password
          </h2>

          <p className="mt-2 text-sm text-gray-400">
            Enter your new password below.
          </p>
        </div>

        <form onSubmit={handleSubmit}>

          {message && (
            <div
              className={`mb-5 rounded-lg border p-3 text-sm ${
                isError
                  ? "border-red-500 bg-red-500/10 text-red-400"
                  : "border-green-500 bg-green-500/10 text-green-400"
              }`}
            >
              {message}
            </div>
          )}

          <PasswordInput
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button
            type="submit"
            disabled={loading}
            className="mt-2 w-full rounded-xl bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700 disabled:opacity-60"
          >
            {loading
              ? "Updating..."
              : "Reset Password"}
          </button>

        </form>

      </AuthCard>
    </AuthLayout>
  );
};

export default ResetPassword;