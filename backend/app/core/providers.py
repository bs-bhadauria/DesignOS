from enum import Enum


class Provider(str, Enum):
    """
    Supported LLM providers.
    """

    GEMINI = "gemini"

    OPENAI = "openai"

    ANTHROPIC = "anthropic"

    DEEPSEEK = "deepseek"

    LOCAL = "local"


SUPPORTED_PROVIDERS = {
    Provider.GEMINI,
    Provider.OPENAI,
    Provider.ANTHROPIC,
    Provider.DEEPSEEK,
    Provider.LOCAL,
}