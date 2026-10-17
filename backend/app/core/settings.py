from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.

    Loaded automatically from the .env file.
    """

    # ------------------------------------------------------------------
    # Provider Configuration
    # ------------------------------------------------------------------

    DEFAULT_PROVIDER: str = "gemini"

    GEMINI_API_KEY: str

    OPENAI_API_KEY: str = ""

    ANTHROPIC_API_KEY: str = ""

    DEEPSEEK_API_KEY: str = ""
    
    GROQ_API_KEY: str = ""

    LOCAL_MODEL_PATH: str = ""

    # ------------------------------------------------------------------
    # Model Configuration
    # ------------------------------------------------------------------

    MODEL_NAME: str = "gemini-2.5-flash"

    TEMPERATURE: float = 0.7

    MAX_OUTPUT_TOKENS: int = 8192

    REQUEST_TIMEOUT: int = 120

    # ------------------------------------------------------------------
    # Prompt Configuration
    # ------------------------------------------------------------------

    PROMPTS_DIRECTORY: str = "app/prompts"

    # ------------------------------------------------------------------
    # Pydantic Settings Configuration
    # ------------------------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Singleton Settings object.
    """
    return Settings()