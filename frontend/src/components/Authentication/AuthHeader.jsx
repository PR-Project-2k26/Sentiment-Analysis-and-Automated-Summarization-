const AuthHeader = ({
  title = "Sign In",
  subtitle,
}) => {
  return (
    <div className="mb-8">
      <h2 className="text-3xl font-bold tracking-tight text-white">
        {title}
      </h2>

      {subtitle && (
        <p className="mt-2 text-sm leading-6 text-gray-400">
          {subtitle}
        </p>
      )}
    </div>
  );
};

export default AuthHeader;