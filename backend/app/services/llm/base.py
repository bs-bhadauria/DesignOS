from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Base interface for all LLM providers.
    """
    
    def __init__(self, model: str):
        self.model = model

    @abstractmethod
    def generate(self, prompt: str | list) -> str:
        """
        Generate content from the given prompt.
        If prompt is a list, it can contain multimodal parts.
        """
        pass