const FileUploadBox = () => {
  return (
    <label className="flex h-56 cursor-pointer flex-col items-center justify-center rounded-2xl border-2 border-dashed border-gray-600 bg-white/5 transition hover:border-blue-500 hover:bg-white/10">
      <span className="text-5xl">📁</span>

      <h2 className="mt-4 text-xl font-semibold text-white">
        Drag & Drop your file
      </h2>

      <p className="mt-2 text-gray-400">
        or click to browse
      </p>

      <input
        type="file"
        className="hidden"
      />
    </label>
  );
};

export default FileUploadBox;