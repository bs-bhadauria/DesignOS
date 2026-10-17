from pathlib import Path

from .loader import KnowledgeLoader
from .models import KnowledgeItem


class KnowledgeRepository:
    """
    Repository responsible for locating
    knowledge assets.

    It knows WHERE files are stored.

    It does NOT know:
    - Planner
    - Designer
    - Workflow
    - Agents
    """

    def __init__(self):
        root = Path(__file__).resolve().parent.parent

        self._knowledge = {
            "identity": root / "prompts/core/identity.txt",
            "design_principles": root / "prompts/core/design_principles.txt",
            "design_language": root / "prompts/core/design_language.md",
            "information_architecture": (
                root / "prompts/core/information_architecture.txt"
            ),
        }

    def get(self, name: str) -> KnowledgeItem:
        """
        Return a knowledge asset by name.
        """

        if name not in self._knowledge:
            raise KeyError(
                f"Knowledge asset '{name}' does not exist."
            )

        return KnowledgeLoader.load(
            self._knowledge[name]
        )

    def list(self) -> list[str]:
        """
        Return all available knowledge names.
        """

        return sorted(
            self._knowledge.keys()
        )