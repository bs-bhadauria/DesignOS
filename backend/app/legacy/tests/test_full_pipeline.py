from app.agents.planner import PlannerAgent
from app.agents.designer import DesignerAgent
from app.agents.renderer import RendererAgent
from app.agents.reviewer import ReviewerAgent

from app.workflow.models import (
    Workflow,
    WorkflowDefinition,
    WorkflowContext,
)

from app.workflow.state import WorkflowState

from app.ddom.builder import DDOMBuilder
from app.workflow.engine import WorkflowEngine
from app.knowledge.repository import KnowledgeRepository


def print_header(title: str):

    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def main():

    # ==========================================================
    # Create Workflow
    # ==========================================================

    definition = WorkflowDefinition(
        workflow_id="pipeline_test",
        name="Complete DesignOS Pipeline",
    )

    context = WorkflowContext(
        workflow_id="pipeline_test",
        user_prompt=(
            "Create an investment pitch deck for an "
            "AI Education Platform."
        ),
    )

    workflow = Workflow(
        definition=definition,
        context=context,
        state=WorkflowState(),
    )

    WorkflowEngine.create(workflow)
    WorkflowEngine.start(workflow)

    # ==========================================================
    # Load Knowledge
    # ==========================================================

    print_header("LOADING KNOWLEDGE")

    repo = KnowledgeRepository()

    workflow.context.shared_data["knowledge"] = {
        "identity": repo.get("identity").content,
        "design_principles": repo.get("design_principles").content,
        "design_language": repo.get("design_language").content,
        "information_architecture": repo.get(
            "information_architecture"
        ).content,
    }

    print("Knowledge Loaded ✓")

    # ==========================================================
    # Planner
    # ==========================================================

    print_header("PLANNER")

    planner_result = PlannerAgent().execute(workflow)

    print(planner_result)

    WorkflowEngine.advance(workflow)

    # ==========================================================
    # Designer
    # ==========================================================

    print_header("DESIGNER")

    designer_result = DesignerAgent().execute(workflow)

    print(designer_result)

    WorkflowEngine.advance(workflow)

    # ==========================================================
    # DDOM
    # ==========================================================

    print_header("DDOM")

    plan = workflow.context.shared_data["plan"]
    design = workflow.context.shared_data["design"]

    ddom = DDOMBuilder.build(
        plan,
        design,
    )

    workflow.context.shared_data["ddom"] = ddom

    print(ddom)

    WorkflowEngine.advance(workflow)

    # ==========================================================
    # Renderer
    # ==========================================================

    print_header("RENDERER")

    renderer_result = RendererAgent().execute(workflow)

    print(renderer_result)

    # ==========================================================
    # Reviewer
    # ==========================================================

    print_header("REVIEWER")

    reviewer_result = ReviewerAgent().execute(workflow)

    print(reviewer_result)

    WorkflowEngine.complete(workflow)

    # ==========================================================
    # Final Summary
    # ==========================================================

    print_header("PIPELINE SUMMARY")

    print("Workflow ID :", workflow.definition.workflow_id)

    print(
        "Current Stage :",
        workflow.state.current_stage,
    )

    print(
        "Current Status :",
        workflow.state.current_status,
    )

    print()

    print(
        "Plan Generated :",
        "plan" in workflow.context.shared_data,
    )

    print(
        "Design Generated :",
        "design" in workflow.context.shared_data,
    )

    print(
        "DDOM Generated :",
        "ddom" in workflow.context.shared_data,
    )

    print(
        "HTML Generated :",
        "html" in workflow.context.shared_data,
    )

    print(
        "Review Generated :",
        "review" in workflow.context.shared_data,
    )

    print()

    if reviewer_result.success:

        print("PIPELINE EXECUTED SUCCESSFULLY ✅")

    else:

        print("PIPELINE FAILED ❌")


if __name__ == "__main__":
    main()