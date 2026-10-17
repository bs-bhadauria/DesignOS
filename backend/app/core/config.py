from app.core.settings import Settings, get_settings


class AppConfig:
    """
    Central application configuration.

    This class exposes all configuration
    required by the application.
    """

    def __init__(
        self,
        settings: Settings,
    ):
        self.settings = settings

    @property
    def default_provider(self) -> str:
        return self.settings.DEFAULT_PROVIDER

    @property
    def model(self) -> str:
        return self.settings.MODEL_NAME

    @property
    def temperature(self) -> float:
        return self.settings.TEMPERATURE

    @property
    def max_output_tokens(self) -> int:
        return self.settings.MAX_OUTPUT_TOKENS

    @property
    def timeout(self) -> int:
        return self.settings.REQUEST_TIMEOUT

    @property
    def prompts_directory(self) -> str:
        return self.settings.PROMPTS_DIRECTORY


config = AppConfig(
    get_settings()
)