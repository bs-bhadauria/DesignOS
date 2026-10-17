from abc import ABC, abstractmethod


class LLMInterface(ABC):
    """
    Common interface implemented by every
    Large Language Model provider.
    """

    @abstractmethod
    async def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from the LLM.
        """
        raise NotImplementedError