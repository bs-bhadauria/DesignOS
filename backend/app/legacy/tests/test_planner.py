from app.agents.planner import PlannerAgent
from app.workflow.context import WorkflowContext
from app.workflow.engine import WorkflowEngine
from app.workflow.executor import WorkflowExecutor
from app.workflow.models import Workflow, WorkflowDefinition
from app.workflow.state import WorkflowState


def main():

    workflow = Workflow(
        definition=WorkflowDefinition(
            workflow_id="workflow-001",
            name="Startup Pitch Deck",
        ),
        context=WorkflowContext(
            workflow_id="workflow-001",
            user_prompt="Create a startup pitch deck for an AI education platform.",
        ),
        state=WorkflowState(),
    )

    engine = WorkflowEngine()

    workflow = engine.create(workflow)

    workflow = engine.start(workflow)

    planner = PlannerAgent()

    result = WorkflowExecutor.execute(
        workflow=workflow,
        agent=planner,
    )

    print("=" * 60)
    print("Planner Result")
    print("=" * 60)

    print(result)

    print()

    print("=" * 60)
    print("Workflow Context")
    print("=" * 60)

    print(workflow.context.shared_data)


if __name__ == "__main__":
    main()