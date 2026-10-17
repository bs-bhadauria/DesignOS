from app.agents.reviewer import ReviewerAgent
from app.ddom.builder import DDOMBuilder
from app.workflow.context import WorkflowContext
from app.workflow.models import (
    Workflow,
    WorkflowDefinition,
)
from app.workflow.state import WorkflowState
from app.workflow.types import (
    WorkflowStage,
    WorkflowStatus,
)


def main():

    # ==========================================================
    # Planner Output
    # ==========================================================

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

    # ==========================================================
    # Designer Output
    # ==========================================================

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

    # ==========================================================
    # Workflow
    # ==========================================================

    workflow = Workflow(

        definition=WorkflowDefinition(

            workflow_id="reviewer_test",

            name="Reviewer Test",

            stage=WorkflowStage.REVIEWER,

            status=WorkflowStatus.CREATED,
        ),

        context=WorkflowContext(

            workflow_id="reviewer_test",

            user_prompt="Create an investment pitch deck for an AI Education Platform.",
        ),

        state=WorkflowState(),
    )

    # ==========================================================
    # Knowledge
    # ==========================================================

    workflow.context.shared_data["knowledge"] = {

        "identity": """
DesignOS creates premium professional documents.
""",

        "design_principles": """
Hierarchy
Whitespace
Consistency
Accessibility
""",

        "design_language": """
Premium
Minimal
Modern
Professional
""",

        "information_architecture": """
Think first.
Then design.
Never directly generate HTML.
""",
    }

    # ==========================================================
    # DDOM
    # ==========================================================

    ddom = DDOMBuilder.build(

        planner_output,

        designer_output,
    )

    workflow.context.shared_data["ddom"] = ddom

    # ==========================================================
    # Dummy HTML
    # ==========================================================

    workflow.context.shared_data["html"] = """
<!DOCTYPE html>

<html>

<head>

<title>AI Education Platform</title>

</head>

<body>

<section>

<h1>Introduction</h1>

<p>Introduce the company</p>

</section>

<section>

<h2>Problem</h2>

<p>Explain the market problem</p>

</section>

<section>

<h2>Solution</h2>

<p>Present the solution</p>

</section>

<section>

<h2>Business Model</h2>

<p>Explain revenue generation</p>

</section>

</body>

</html>
"""

    # ==========================================================
    # Execute Reviewer
    # ==========================================================

    result = ReviewerAgent().execute(workflow)

    print()

    print("=" * 70)

    print("Reviewer Result")

    print("=" * 70)

    print(result)

    print()

    print("=" * 70)

    print("Review JSON")

    print("=" * 70)

    print(workflow.context.shared_data["review"])


if __name__ == "__main__":
    main()