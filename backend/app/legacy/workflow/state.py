from pydantic import BaseModel

from .types import WorkflowStage, WorkflowStatus


class WorkflowState(BaseModel):
    """
    Represents the current execution state
    of a workflow instance.
    """

    current_stage: WorkflowStage = WorkflowStage.PLANNER

    current_status: WorkflowStatus = WorkflowStatus.CREATED

    active_agent: WorkflowStage = WorkflowStage.PLANNER

    retry_count: int = 0