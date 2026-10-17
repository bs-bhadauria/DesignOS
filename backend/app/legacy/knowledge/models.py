from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class KnowledgeType(str, Enum):
    """
    Supported knowledge source types.
    """

    MARKDOWN = "markdown"
    TEXT = "text"
    JSON = "json"


class KnowledgeItem(BaseModel):
    """
    Represents a single knowledge asset available
    to the DesignOS agents.
    """

    name: str

    path: str

    knowledge_type: KnowledgeType

    content: str

    created_at: datetime = Field(default_factory=datetime.utcnow)

    metadata: dict = Field(default_factory=dict)