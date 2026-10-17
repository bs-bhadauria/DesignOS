import api from "./api";

export interface GenerateRequest {
  prompt: string;
  files?: File[];
}

export interface GenerateResponse {
  success: boolean;
  request_id: string;
  status: string;
  html: string;
}

export async function generateDocument(
  data: GenerateRequest
): Promise<GenerateResponse> {
  const formData = new FormData();
  formData.append("prompt", data.prompt);
  
  if (data.files && data.files.length > 0) {
    data.files.forEach((file) => {
      formData.append("files", file);
    });
  }

  const response = await fetch("http://127.0.0.1:8001/api/v1/generate", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error(`Server returned ${response.status}: ${await response.text()}`);
  }

  const result = await response.json();
  return result;
}
