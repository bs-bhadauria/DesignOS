from app.ddom.builder import DDOMBuilder
from app.ddom.validator import DDOMValidator
from app.workflow.models import Workflow, WorkflowResult


class DDOMStage:
    """
    Workflow stage responsible for constructing
    the internal DesignOS Document Object Model (DDOM).

    Responsibilities
    ----------------
    - Read Planner output
    - Read Designer output
    - Build the DDOM
    - Validate the DDOM
    - Store the validated DDOM inside the workflow context

    This stage performs NO rendering.

    It performs NO LLM calls.

    It simply converts structured planning +
    structured design into the canonical
    internal document representation.
    """

    @staticmethod
    def execute(workflow: Workflow) -> WorkflowResult:

        plan = workflow.context.shared_data.get("plan")
        design = workflow.context.shared_data.get("design")

        if plan is None:
            return WorkflowResult(
                success=False,
                error="Planner output not found."
            )

        if design is None:
            return WorkflowResult(
                success=False,
                error="Designer output not found."
            )

        try:

            ddom = DDOMBuilder.build(
                plan=plan,
                design=design,
            )

            DDOMValidator.validate(ddom)

        except Exception as error:

            return WorkflowResult(
                success=False,
                error=str(error),
            )

        workflow.context.shared_data["ddom"] = ddom

        return WorkflowResult(
            success=True,
            output=ddom,
        )