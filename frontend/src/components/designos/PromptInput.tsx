import { useRef, useState, DragEvent } from "react";
import { Button } from "@/components/ui/button";
import { Plus, X, File as FileIcon, Image as ImageIcon } from "lucide-react";

interface Props {
  prompt: string;
  setPrompt: (value: string) => void;
  files: File[];
  setFiles: (files: File[] | ((prev: File[]) => File[])) => void;
  onGenerate: () => void;
  loading: boolean;
}

const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
const ALLOWED_TYPES = ["application/pdf", "image/jpeg", "image/png", "image/webp"];

export default function PromptInput({
  prompt,
  setPrompt,
  files,
  setFiles,
  onGenerate,
  loading,
}: Props) {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  const handleFileSelect = (newFiles: FileList | null) => {
    if (!newFiles || loading) return;
    setErrorMsg("");
    
    const validFiles: File[] = [];
    Array.from(newFiles).forEach((file) => {
      if (!ALLOWED_TYPES.includes(file.type)) {
        setErrorMsg(`Invalid file type: ${file.name}. Only PDF and Images allowed.`);
        return;
      }
      if (file.size > MAX_FILE_SIZE) {
        setErrorMsg(`File too large: ${file.name}. Max 10MB allowed.`);
        return;
      }
      validFiles.push(file);
    });

    if (validFiles.length > 0) {
      setFiles((prev) => [...prev, ...validFiles]);
    }
    
    // Reset file input
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const removeFile = (index: number) => {
    if (loading) return;
    setFiles((prev) => prev.filter((_, i) => i !== index));
  };

  const onDragOver = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    if (loading) return;
    setIsDragging(true);
  };

  const onDragLeave = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    if (loading) return;
    setIsDragging(false);
  };

  const onDrop = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    if (loading) return;
    setIsDragging(false);
    handleFileSelect(e.dataTransfer.files);
  };

  return (
    <div className="space-y-4">
      {/* File Pills */}
      {files.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {files.map((file, i) => (
            <div key={i} className="flex items-center gap-2 bg-slate-100 px-3 py-1.5 rounded-full text-sm border border-slate-200">
              {file.type.startsWith("image/") ? <ImageIcon size={14} /> : <FileIcon size={14} />}
              <span className="truncate max-w-[150px]">{file.name}</span>
              <button 
                onClick={() => removeFile(i)} 
                className="text-slate-500 hover:text-red-500 rounded-full p-0.5 disabled:opacity-50"
                disabled={loading}
              >
                <X size={14} />
              </button>
            </div>
          ))}
        </div>
      )}

      {errorMsg && <p className="text-sm text-red-500">{errorMsg}</p>}

      {/* Input Area */}
      <div 
        className={`relative rounded-xl border p-2 transition-colors ${isDragging ? "border-blue-500 bg-blue-50" : "border-slate-300"} ${loading ? "opacity-70 pointer-events-none" : ""}`}
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
        onDrop={onDrop}
      >
        <textarea
          className="w-full bg-transparent p-2 min-h-[120px] outline-none resize-none"
          placeholder="What would you like to create today? You can drag and drop PDFs or images here..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          disabled={loading}
        />
        
        {/* Actions Bar */}
        <div className="flex justify-between items-center px-2 pt-2 border-t border-slate-100">
          <div>
            <input 
              type="file" 
              multiple 
              className="hidden" 
              ref={fileInputRef}
              accept=".pdf,image/png,image/jpeg,image/webp"
              onChange={(e) => handleFileSelect(e.target.files)}
              disabled={loading}
            />
            <button 
              onClick={() => fileInputRef.current?.click()}
              className="p-2 text-slate-500 hover:text-slate-800 hover:bg-slate-100 rounded-full transition-colors flex items-center gap-1 disabled:opacity-50"
              title="Attach files"
              disabled={loading}
            >
              <Plus size={20} />
            </button>
          </div>
          <Button
            onClick={onGenerate}
            disabled={loading || (!prompt.trim() && files.length === 0)}
            className="px-6"
          >
            {loading ? "Generating..." : "Generate"}
          </Button>
        </div>
      </div>
    </div>
  );
}
