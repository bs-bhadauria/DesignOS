from .models import Workflow
from .types import WorkflowStage, WorkflowStatus


class WorkflowEngine:
    """
    Coordinates the lifecycle of a workflow.

    The WorkflowEngine is responsible only for
    managing workflow state transitions.

    It does NOT execute agents.
    It does NOT communicate with LLM providers.
    It does NOT perform rendering.

    Those responsibilities belong to other
    architectural components.
    """

    @staticmethod
    def create(workflow: Workflow) -> Workflow:
        """
        Initialize a workflow.

        A newly created workflow enters the READY state.
        """

        workflow.state.current_status = WorkflowStatus.READY

        workflow.definition.status = WorkflowStatus.READY

        return workflow

    @staticmethod
    def start(workflow: Workflow) -> Workflow:
        """
        Start workflow execution.
        """

        workflow.state.current_status = WorkflowStatus.RUNNING

        workflow.definition.status = WorkflowStatus.RUNNING

        return workflow

    @staticmethod
    def advance(workflow: Workflow) -> Workflow:
        """
        Advance the workflow to the next stage.
        """

        current = workflow.state.current_stage

        if current == WorkflowStage.PLANNER:
            next_stage = WorkflowStage.DESIGNER

        elif current == WorkflowStage.DESIGNER:
            next_stage = WorkflowStage.RENDERER

        elif current == WorkflowStage.RENDERER:
            next_stage = WorkflowStage.REVIEWER

        else:
            return workflow

        workflow.state.current_stage = next_stage
        workflow.state.active_agent = next_stage

        workflow.definition.stage = next_stage

        return workflow

    @staticmethod
    def complete(workflow: Workflow) -> Workflow:
        """
        Mark workflow as completed.
        """

        workflow.state.current_status = WorkflowStatus.COMPLETED

        workflow.definition.status = WorkflowStatus.COMPLETED

        return workflow

    @staticmethod
    def fail(workflow: Workflow) -> Workflow:
        """
        Mark workflow as failed.
        """

        workflow.state.current_status = WorkflowStatus.FAILED

        workflow.definition.status = WorkflowStatus.FAILED

        return workflow