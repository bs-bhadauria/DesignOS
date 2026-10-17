"use client";

import { useState } from "react";

import Header from "@/components/designos/Header";
import PromptInput from "@/components/designos/PromptInput";
import ResponseCard from "@/components/designos/ResponseCard";

import { generateDocument } from "@/services/generate";
import { GenerateResponse } from "@/types/generate";

export default function Home() {

  const [prompt, setPrompt] = useState("");
  const [files, setFiles] = useState<File[]>([]);

  const [loading, setLoading] = useState(false);

  const [response, setResponse] =
    useState<GenerateResponse | null>(null);

  async function handleGenerate() {

    try {

      setLoading(true);

      const result =
        await generateDocument({
          prompt,
          files,
        });

      setResponse(result);
      if (result && result.html) {
        localStorage.setItem("previewHtml", result.html);
      }

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }

  }

  return (

    <main className="min-h-screen flex items-center justify-center bg-background">

      <div className="w-full max-w-3xl space-y-10 p-10">

        <Header />

        <PromptInput
          prompt={prompt}
          setPrompt={setPrompt}
          files={files}
          setFiles={setFiles}
          onGenerate={handleGenerate}
          loading={loading}
        />

        <ResponseCard
          response={response}
        />

      </div>

    </main>

  );

}