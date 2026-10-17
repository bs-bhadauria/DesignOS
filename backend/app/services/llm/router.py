import logging
from .base import BaseLLM

logger = logging.getLogger(__name__)

class LLMRouter:
    """
    Router that takes a list of LLMs and provides automatic fallback.
    If the primary model fails (e.g. 429 Quota Exceeded), it tries the next one.
    """

    def __init__(self, models: list[BaseLLM]):
        if not models:
            raise ValueError("LLMRouter requires at least one model.")
        self.models = models

    def generate(self, prompt: str | list) -> str:
        last_exception = None
        for i, model in enumerate(self.models):
            try:
                # logger.info(f"LLMRouter: Attempting generation with {model.__class__.__name__} ({model.model})")
                print(f"[LLMRouter] Attempting with {model.__class__.__name__} ({model.model})")
                return model.generate(prompt)
            except Exception as e:
                last_exception = e
                print(f"[LLMRouter] Error with {model.__class__.__name__} ({model.model}): {e}")
                # logger.warning(f"LLMRouter: Error with {model.__class__.__name__} ({model.model}): {e}")
                if i < len(self.models) - 1:
                    print(f"[LLMRouter] Falling back to next model...")
                    # logger.info(f"LLMRouter: Falling back to next model...")
                else:
                    print(f"[LLMRouter] All models failed.")
                    # logger.error("LLMRouter: All models failed.")
                    raise last_exception
        
        raise last_exception
