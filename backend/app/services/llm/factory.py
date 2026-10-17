from app.core.config import config
from app.core.providers import Provider

from .base import BaseLLM
from .registry import LLMRegistry


class LLMFactory:
    """
    Factory responsible for creating
    LLM provider instances.
    """

    @staticmethod
    def create() -> BaseLLM:
        """
        Create the configured LLM provider.
        """

        provider = Provider(
            config.settings.DEFAULT_PROVIDER
        )

        implementation = LLMRegistry.get(
            provider
        )

        return implementation()