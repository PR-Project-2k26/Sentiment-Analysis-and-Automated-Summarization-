import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { loginUser } from "../../services/authService";

import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import AuthHeader from "../../components/Authentication/AuthHeader";
import AuthInput from "../../components/Authentication/AuthInput";
import PasswordInput from "../../components/Authentication/PasswordInput";
import Divider from "../../components/Authentication/Divider";
import SocialButtons from "../../components/Authentication/SocialButtons";
import AuthFooter from "../../components/Authentication/AuthFooter";

const Login = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [isError, setIsError] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    setMessage("");

    try {
      setLoading(true);

      const response = await loginUser(formData);

      // Save JWT token
      localStorage.setItem("token", response.data.access_token);

      // Save user if backend returns it
      if (response.data.user) {
        localStorage.setItem(
          "user",
          JSON.stringify(response.data.user)
        );
      }

      setIsError(false);
      setMessage("Login successful!");

      setTimeout(() => {
        navigate("/dashboard");
      }, 1000);

    } catch (error) {
      setIsError(true);

      setMessage(
        error.response?.data?.message ||
        "Invalid email or password."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthLayout>
      <AuthCard>
        <form onSubmit={handleLogin}>

          <AuthHeader
            title="Welcome Back 👋"
            subtitle="Sign in to continue using SummarAI."
          />

          {message && (
            <div
              className={`mb-4 rounded-lg border p-3 text-sm ${
                isError
                  ? "border-red-500 bg-red-500/10 text-red-400"
                  : "border-green-500 bg-green-500/10 text-green-400"
              }`}
            >
              {message}
            </div>
          )}

          <AuthInput
            label="Email"
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Enter your email"
          />

          <PasswordInput
            name="password"
            value={formData.password}
            onChange={handleChange}
          />

          <div className="mb-6 flex items-center justify-between">
            <label className="flex items-center gap-2 text-sm text-gray-400">
              <input type="checkbox" />
              Remember Me
            </label>

            <Link
              to="/forgot-password"
              className="text-sm text-blue-400 hover:text-blue-300"
            >
              Forgot Password?
            </Link>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Signing In..." : "Login"}
          </button>

        </form>

        <Divider />

        <SocialButtons />

        <AuthFooter />
      </AuthCard>
    </AuthLayout>
  );
};

export default Login;