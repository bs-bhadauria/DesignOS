from abc import ABC, abstractmethod

from app.workflow.models import Workflow, WorkflowResult


class BaseAgent(ABC):
    """
    Base interface for all DesignOS agents.

    Every intelligent agent must implement
    the execute() contract.
    """

    @abstractmethod
    def execute(
        self,
        workflow: Workflow,
    ) -> WorkflowResult:
        """
        Execute one stage of the workflow.
        """
        raise NotImplementedError