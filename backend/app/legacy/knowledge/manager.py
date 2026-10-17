from .models import KnowledgeItem
from .repository import KnowledgeRepository


class KnowledgeManager:
    """
    Public interface for accessing the DesignOS
    Knowledge Layer.

    Agents interact ONLY with this class.

    Responsibilities:
    - Retrieve knowledge assets
    - List available knowledge
    - Keep agents independent from storage details
    """

    def __init__(self):
        self.repository = KnowledgeRepository()

    def get(self, name: str) -> KnowledgeItem:
        """
        Retrieve a knowledge asset by name.

        Example:
            manager.get("identity")
        """

        return self.repository.get(name)

    def list(self) -> list[str]:
        """
        Return all available knowledge assets.

        Example:
            manager.list()
        """

        return self.repository.list()

    def exists(self, name: str) -> bool:
        """
        Check whether a knowledge asset exists.
        """

        return name in self.repository.list()