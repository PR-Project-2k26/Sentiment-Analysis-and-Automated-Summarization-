import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { registerUser } from "../../services/authService";

import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import AuthHeader from "../../components/Authentication/AuthHeader";
import AuthInput from "../../components/Authentication/AuthInput";
import PasswordInput from "../../components/Authentication/PasswordInput";

const Register = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
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

  const handleRegister = async (e) => {
    e.preventDefault();

    setMessage("");

    try {
      setLoading(true);

      const response = await registerUser(formData);

      setIsError(false);
      setMessage(response.data.message);

      setTimeout(() => {
        navigate("/login");
      }, 1500);

    } catch (error) {
      setIsError(true);

      setMessage(
        error.response?.data?.message ||
        "Registration failed."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthLayout>
      <AuthCard>

        <AuthHeader
          title="Create Account"
          subtitle="Create your SummarAI account to continue."
        />

        <form onSubmit={handleRegister} className="space-y-5">

          {message && (
            <div
              className={`rounded-lg border p-3 text-sm ${
                isError
                  ? "border-red-500 bg-red-500/10 text-red-400"
                  : "border-green-500 bg-green-500/10 text-green-400"
              }`}
            >
              {message}
            </div>
          )}

          <AuthInput
            label="Full Name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="John Doe"
          />

          <AuthInput
            label="Email Address"
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="john@example.com"
          />

          <PasswordInput
            name="password"
            value={formData.password}
            onChange={handleChange}
          />

          <label className="flex items-center gap-2 text-sm text-gray-400">
            <input type="checkbox" required />
            I agree to the Terms & Conditions
          </label>

          <button
            type="submit"
            disabled={loading}
            className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:opacity-60"
          >
            {loading
              ? "Creating Account..."
              : "Create Account"}
          </button>

        </form>

        <div className="mt-8 border-t border-white/10 pt-6">
          <p className="text-center text-sm text-gray-400">
            Already have an account?{" "}
            <Link
              to="/login"
              className="font-semibold text-blue-500 hover:text-blue-400"
            >
              Sign In
            </Link>
          </p>
        </div>

      </AuthCard>
    </AuthLayout>
  );
};

export default Register;