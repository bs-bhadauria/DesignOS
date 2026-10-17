from app.agents.base import BaseAgent
from app.workflow.models import Workflow, WorkflowResult


class WorkflowExecutor:
    """
    Executes workflow stages by delegating
    execution to the provided agent.

    The executor does not manage workflow
    lifecycle or state transitions.
    """

    @staticmethod
    def execute(
        workflow: Workflow,
        agent: BaseAgent,
    ) -> WorkflowResult:
        """
        Execute a single workflow stage.
        """

        return agent.execute(workflow)