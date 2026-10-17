from app.agents.designer import DesignerAgent

from app.workflow.context import WorkflowContext
from app.workflow.engine import WorkflowEngine
from app.workflow.executor import WorkflowExecutor
from app.workflow.models import (
    Workflow,
    WorkflowDefinition,
    WorkflowResult,
)
from app.workflow.state import WorkflowState


def main():

    workflow = Workflow(
        definition=WorkflowDefinition(
            workflow_id="designer-test",
            name="Designer Test",
        ),
        context=WorkflowContext(
            workflow_id="designer-test",
            user_prompt="Generate an investment pitch deck for an AI education platform.",
            shared_data={
                "plan": {
                    "document_type": "Pitch Deck",
                    "title": "AI Education Platform",
                    "objective": "Secure investment",
                    "audience": "Investors",
                    "sections": [
                        {
                            "title": "Introduction",
                            "purpose": "Introduce the company",
                        },
                        {
                            "title": "Problem",
                            "purpose": "Explain the market problem",
                        },
                        {
                            "title": "Solution",
                            "purpose": "Present the solution",
                        },
                        {
                            "title": "Business Model",
                            "purpose": "Explain revenue generation",
                        },
                    ],
                    "constraints": [],
                    "metadata": {},
                }
            },
        ),
        state=WorkflowState(),
    )

    engine = WorkflowEngine()

    workflow = engine.create(workflow)

    workflow = engine.start(workflow)

    designer = DesignerAgent()

    result = WorkflowExecutor.execute(
        workflow=workflow,
        agent=designer,
    )

    print("=" * 60)
    print("Designer Result")
    print("=" * 60)

    print(result)

    print()

    print("=" * 60)
    print("Workflow Context")
    print("=" * 60)

    print(workflow.context.shared_data)


if __name__ == "__main__":
    main()