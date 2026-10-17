from typing import Any

from pydantic import BaseModel, Field


class WorkflowContext(BaseModel):
    """
    Shared information that travels throughout
    the complete workflow lifecycle.
    """

    workflow_id: str

    user_prompt: str

    shared_data: dict[str, Any] = Field(default_factory=dict)

    metadata: dict[str, Any] = Field(default_factory=dict)