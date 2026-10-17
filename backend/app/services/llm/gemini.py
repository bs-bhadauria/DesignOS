from google import genai

from app.core.config import config

from .base import BaseLLM


class GeminiLLM(BaseLLM):
    """
    Gemini implementation of BaseLLM.
    """

    def __init__(self, model: str):
        super().__init__(model)
        self.client = genai.Client(
            api_key=config.settings.GEMINI_API_KEY,
        )

    def generate(
        self,
        prompt: str | list,
    ) -> str:
        
        contents = prompt
        if isinstance(prompt, list):
            contents = []
            for item in prompt:
                if isinstance(item, dict) and "data" in item and "mime_type" in item:
                    contents.append(
                        genai.types.Part.from_bytes(
                            data=item["data"],
                            mime_type=item["mime_type"],
                        )
                    )
                else:
                    contents.append(item)

        response = self.client.models.generate_content(
            model=self.model,
            contents=contents,
        )

        return response.text