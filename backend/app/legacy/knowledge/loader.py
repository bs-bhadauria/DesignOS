from pathlib import Path

from .models import KnowledgeItem, KnowledgeType


class KnowledgeLoader:
    """
    Responsible for loading knowledge assets
    from the filesystem.

    This class only knows how to read files.

    It does NOT know:
    - Planner
    - Designer
    - Repository
    - Agents
    """

    @staticmethod
    def load(path: str | Path) -> KnowledgeItem:
        """
        Load a knowledge file from disk.
        """

        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"Knowledge file '{file_path}' not found."
            )

        suffix = file_path.suffix.lower()

        if suffix == ".md":
            knowledge_type = KnowledgeType.MARKDOWN

        elif suffix == ".txt":
            knowledge_type = KnowledgeType.TEXT

        elif suffix == ".json":
            knowledge_type = KnowledgeType.JSON

        else:
            raise ValueError(
                f"Unsupported knowledge file type: {suffix}"
            )

        content = file_path.read_text(
            encoding="utf-8"
        )

        return KnowledgeItem(
            name=file_path.stem,
            path=str(file_path),
            knowledge_type=knowledge_type,
            content=content,
        )