import os
from groq import Groq

from app.core.config import config
from .base import BaseLLM

class GroqLLM(BaseLLM):
    """
    Groq implementation of BaseLLM.
    """

    def __init__(self, model: str):
        super().__init__(model)
        api_key = getattr(config.settings, "GROQ_API_KEY", os.environ.get("GROQ_API_KEY", ""))
        self.client = Groq(api_key=api_key)

    def generate(self, prompt: str | list) -> str:
        # Groq currently mainly supports text, or specific vision models. 
        # We'll extract text from the list for simple fallback.
        text_content = ""
        if isinstance(prompt, list):
            for item in prompt:
                if isinstance(item, str):
                    text_content += item + "\n"
        else:
            text_content = prompt

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": text_content,
                }
            ],
            model=self.model,
        )
        return chat_completion.choices[0].message.content
