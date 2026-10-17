from app.agents.renderer import RendererAgent
from app.ddom.builder import DDOMBuilder
from app.ddom.validator import DDOMValidator
from app.workflow.context import WorkflowContext
from app.workflow.engine import WorkflowEngine
from app.workflow.executor import WorkflowExecutor
from app.workflow.models import Workflow, WorkflowDefinition
from app.workflow.state import WorkflowState


def main():

    planner_output = {
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
    }

    designer_output = {
        "page": {
            "size": "A4",
            "orientation": "portrait",
            "margin": "normal",
        },
        "theme": {
            "primary_color": "#2563eb",
            "secondary_color": "#f8fafc",
            "background": "#ffffff",
        },
        "typography": {
            "heading_font": "Inter",
            "body_font": "Inter",
            "heading_size": 32,
            "body_size": 16,
        },
        "sections": [
            {
                "component": "hero",
            },
            {
                "component": "content_focus",
            },
            {
                "component": "feature_showcase",
            },
            {
                "component": "data_summary",
            },
        ],
    }

    ddom = DDOMBuilder.build(
        planner_output,
        designer_output,
    )

    DDOMValidator.validate(ddom)

    workflow = Workflow(
        definition=WorkflowDefinition(
            workflow_id="renderer-test",
            name="Renderer Test",
        ),
        context=WorkflowContext(
            workflow_id="renderer-test",
            user_prompt="Generate an investment pitch deck.",
            shared_data={
                "ddom": ddom,
            },
        ),
        state=WorkflowState(),
    )

    engine = WorkflowEngine()

    workflow = engine.create(workflow)

    workflow = engine.start(workflow)

    renderer = RendererAgent()

    result = WorkflowExecutor.execute(
        workflow=workflow,
        agent=renderer,
    )

    print("=" * 60)
    print("Renderer Result")
    print("=" * 60)

    print(result)

    print()

    print("=" * 60)
    print("Generated HTML")
    print("=" * 60)

    html = workflow.context.shared_data.get("html")

    if html is None:

        print("No HTML generated.")

    else:

        print(html[:2500])

        print()

        print("=" * 60)
        print("HTML Length")
        print("=" * 60)

        print(len(html))


if __name__ == "__main__":
    main()