import { useState } from "react";
import { Link } from "react-router-dom";

import { forgotPassword } from "../../services/authService";

import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import AuthInput from "../../components/Authentication/AuthInput";

const ForgotPassword = () => {
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [isError, setIsError] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);
    setMessage("");

    try {
      const response = await forgotPassword(email);

      setIsError(false);
      setMessage(response.data.message);
    } catch (error) {
      setIsError(true);
      setMessage(
        error.response?.data?.message ||
          "Something went wrong. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthLayout>
      <AuthCard>

        <div className="mb-8">
          <h2 className="text-3xl font-bold tracking-tight text-white">
            Forgot Password
          </h2>

          <p className="mt-2 text-sm leading-6 text-gray-400">
            Enter your email address and we'll send you a password reset link.
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

          <AuthInput
            label="Email Address"
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="john@example.com"
          />

          <button
            type="submit"
            disabled={loading}
            className="mt-2 w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Sending..." : "Send Reset Link"}
          </button>

        </form>

        <div className="mt-8 border-t border-white/10 pt-6">
          <p className="text-center text-sm text-gray-400">
            Remember your password?{" "}
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

export default ForgotPassword;