"use client";

import { useEffect, useState } from "react";

export default function PreviewPage() {
  const [htmlContent, setHtmlContent] = useState<string | null>(null);

  useEffect(() => {
    const savedHtml = localStorage.getItem("previewHtml");
    if (savedHtml) {
      setHtmlContent(savedHtml);
    } else {
      setHtmlContent("<div style='padding: 20px; color: white;'>No preview available. Please generate a deck first.</div>");
    }
  }, []);

  if (htmlContent === null) {
    return <div className="min-h-screen bg-slate-950 flex items-center justify-center text-white">Loading preview...</div>;
  }

  return (
    <iframe
      title="Generated Document Preview"
      srcDoc={htmlContent}
      className="w-full h-screen border-none bg-slate-950"
    />
  );
}
