from app.workflow.context import WorkflowContext
from app.workflow.engine import WorkflowEngine
from app.workflow.models import (
    Workflow,
    WorkflowDefinition,
)
from app.workflow.state import WorkflowState


def main():

    # --------------------------------------------------
    # Create Workflow
    # --------------------------------------------------

    workflow = Workflow(

        definition=WorkflowDefinition(
            workflow_id="engine_test",
            name="Engine Integration Test",
        ),

        context=WorkflowContext(
            workflow_id="engine_test",
            user_prompt="Generate a startup pitch deck."
        ),

        state=WorkflowState(),
    )

    print("=" * 70)
    print("INITIAL WORKFLOW")
    print("=" * 70)

    print("Stage :", workflow.state.current_stage)
    print("Status:", workflow.state.current_status)

    # --------------------------------------------------
    # Create
    # --------------------------------------------------

    WorkflowEngine.create(workflow)

    print()
    print("=" * 70)
    print("AFTER CREATE")
    print("=" * 70)

    print("Stage :", workflow.state.current_stage)
    print("Status:", workflow.state.current_status)

    # --------------------------------------------------
    # Start
    # --------------------------------------------------

    WorkflowEngine.start(workflow)

    print()
    print("=" * 70)
    print("AFTER START")
    print("=" * 70)

    print("Stage :", workflow.state.current_stage)
    print("Status:", workflow.state.current_status)

    # --------------------------------------------------
    # Planner -> Designer
    # --------------------------------------------------

    WorkflowEngine.advance(workflow)

    print()
    print("=" * 70)
    print("AFTER ADVANCE #1")
    print("=" * 70)

    print("Stage :", workflow.state.current_stage)
    print("Status:", workflow.state.current_status)

    # --------------------------------------------------
    # Designer -> Renderer
    # --------------------------------------------------

    WorkflowEngine.advance(workflow)

    print()
    print("=" * 70)
    print("AFTER ADVANCE #2")
    print("=" * 70)

    print("Stage :", workflow.state.current_stage)
    print("Status:", workflow.state.current_status)

    # --------------------------------------------------
    # Renderer -> Reviewer
    # --------------------------------------------------

    WorkflowEngine.advance(workflow)

    print()
    print("=" * 70)
    print("AFTER ADVANCE #3")
    print("=" * 70)

    print("Stage :", workflow.state.current_stage)
    print("Status:", workflow.state.current_status)

    # --------------------------------------------------
    # Complete
    # --------------------------------------------------

    WorkflowEngine.complete(workflow)

    print()
    print("=" * 70)
    print("AFTER COMPLETE")
    print("=" * 70)

    print("Stage :", workflow.state.current_stage)
    print("Status:", workflow.state.current_status)

    print()
    print("=" * 70)
    print("ENGINE TEST PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()