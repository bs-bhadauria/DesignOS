from typing import Dict, Type

from app.core.providers import Provider

from .base import BaseLLM
from .gemini import GeminiClient


class LLMRegistry:
    """
    Runtime registry of all available
    LLM implementations.
    """

    _providers: Dict[
        Provider,
        Type[BaseLLM],
    ] = {
        Provider.GEMINI: GeminiClient,
    }

    @classmethod
    def register(
        cls,
        provider: Provider,
        implementation: Type[BaseLLM],
    ) -> None:
        """
        Register a provider implementation.
        """
        cls._providers[provider] = implementation

    @classmethod
    def get(
        cls,
        provider: Provider,
    ) -> Type[BaseLLM]:
        """
        Get provider implementation.
        """
        if provider not in cls._providers:
            raise ValueError(
                f"Unsupported provider: {provider}"
            )

        return cls._providers[provider]

    @classmethod
    def available(cls):
        """
        Return all registered providers.
        """
        return list(cls._providers.keys())