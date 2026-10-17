from enum import Enum


class WorkflowStatus(str, Enum):
    """
    Current execution status of a workflow.
    """

    CREATED = "created"
    READY = "ready"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class WorkflowStage(str, Enum):
    """
    Current stage being executed within the workflow.
    """

    PLANNER = "planner"
    DESIGNER = "designer"
    RENDERER = "renderer"
    REVIEWER = "reviewer"