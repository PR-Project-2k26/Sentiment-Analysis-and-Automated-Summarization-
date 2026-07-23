import { Link } from "react-router-dom";

const AuthFooter = () => {
  return (
    <p className="mt-8 text-center text-gray-400">
      Don't have an account?{" "}
      <Link
        to="/register"
        className="font-medium text-blue-500 hover:text-blue-400"
      >
        Create Account
      </Link>
    </p>
  );
};

export default AuthFooter;