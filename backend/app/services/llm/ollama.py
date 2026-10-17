import requests
import json

from .base import BaseLLM

class OllamaLLM(BaseLLM):
    """
    Local Ollama implementation of BaseLLM.
    """

    def __init__(self, model: str, base_url: str = "http://127.0.0.1:11434"):
        super().__init__(model)
        self.base_url = base_url

    def generate(self, prompt: str | list) -> str:
        # Extract text for basic LLMs
        text_content = ""
        if isinstance(prompt, list):
            for item in prompt:
                if isinstance(item, str):
                    text_content += item + "\n"
        else:
            text_content = prompt

        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": text_content,
            "stream": False
        }
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        return response.json().get("response", "")
