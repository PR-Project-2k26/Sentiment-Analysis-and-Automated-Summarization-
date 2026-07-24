import { useRef } from "react";

const FileUploadBox = ({ selectedFile, onFileSelect }) => {
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];

    if (file) {
      onFileSelect(file);
    }
  };

  return (
    <label
      className="flex h-56 cursor-pointer flex-col items-center justify-center rounded-2xl border-2 border-dashed border-gray-600 bg-white/5 transition hover:border-blue-500 hover:bg-white/10"
      onClick={() => fileInputRef.current.click()}
    >
      <span className="text-5xl">📄</span>

      <h2 className="mt-4 text-xl font-semibold text-white">
        {selectedFile ? selectedFile.name : "Drag & Drop your Resume"}
      </h2>

      <p className="mt-2 text-gray-400">
        {selectedFile
          ? `${(selectedFile.size / 1024).toFixed(2)} KB`
          : "or click to browse"}
      </p>

      <input
        ref={fileInputRef}
        type="file"
        accept=".pdf"
        className="hidden"
        onChange={handleFileChange}
      />
    </label>
  );
};

export default FileUploadBox;