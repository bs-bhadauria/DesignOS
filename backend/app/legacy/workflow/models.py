from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from .context import WorkflowContext
from .state import WorkflowState
from .types import WorkflowStage, WorkflowStatus


class WorkflowDefinition(BaseModel):
    """
    High-level description of a workflow instance.
    """

    workflow_id: str

    name: str

    stage: WorkflowStage = WorkflowStage.PLANNER

    status: WorkflowStatus = WorkflowStatus.CREATED

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)


class WorkflowResult(BaseModel):
    """
    Final result produced by a workflow.
    """

    success: bool

    output: Any | None = None

    error: str | None = None

    execution_time_ms: int | None = None


class Workflow(BaseModel):
    """
    Aggregate root representing a complete workflow instance.

    A Workflow combines its definition,
    execution context,
    and execution state into a single object
    that can be passed throughout the workflow engine.
    """

    definition: WorkflowDefinition

    context: WorkflowContext

    state: WorkflowState