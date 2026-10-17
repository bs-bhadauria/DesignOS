from functools import lru_cache

from app.agents.document_agent import DocumentAgent
from app.services.generation_service import GenerationService
from app.services.prompt_loader import PromptLoader


@lru_cache
def get_prompt_loader() -> PromptLoader:
    """
    Singleton Prompt Loader.
    """
    return PromptLoader()


from app.services.llm.gemini import GeminiLLM
from app.services.llm.groq import GroqLLM
from app.services.llm.ollama import OllamaLLM
from app.services.llm.router import LLMRouter

@lru_cache
def get_llm() -> LLMRouter:
    """
    Singleton LLMRouter Provider with Fallbacks.
    """
    # Primary: Gemini 1.5 Flash (Generous Free Tier)
    # Fallback 1: Gemini 1.5 Pro (If Flash fails for some reason)
    # Fallback 2: Groq Llama 3 (Extremely Fast, Free API)
    # Fallback 3: Local Ollama (DeepSeek Coder - 100% Free, Offline)
    
    models = [
        GeminiLLM(model="gemini-2.5-flash"),
        GroqLLM(model="llama-3.3-70b-versatile"),
        OllamaLLM(model="deepseek-coder:6.7b"),
        OllamaLLM(model="qwen2.5-coder:14b")
    ]
    return LLMRouter(models=models)


@lru_cache
def get_document_agent() -> DocumentAgent:
    """
    Singleton Document Agent.
    """
    return DocumentAgent(
        prompt_loader=get_prompt_loader(),
        llm=get_llm(),
    )


@lru_cache
def get_generation_service() -> GenerationService:
    """
    Singleton Generation Service.
    """
    return GenerationService(
        agent=get_document_agent(),
    )