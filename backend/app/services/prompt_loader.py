from pathlib import Path


class PromptLoader:
    """
    Responsible for loading prompt templates
    from the prompts directory.
    """

    def __init__(self):
        self.prompts_dir = (
            Path(__file__).resolve().parent.parent / "prompts"
        )

    def load(self, template_name: str) -> str:
        """
        Load a prompt template.

        Example:
            load("startup_pitch")
        """

        template_path = self.prompts_dir / f"{template_name}.txt"

        if not template_path.exists():
            raise FileNotFoundError(
                f"Prompt template '{template_name}' not found."
            )

        return template_path.read_text(
            encoding="utf-8"
        )