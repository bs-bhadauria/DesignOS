import json

from app.agents.base import BaseAgent
from app.knowledge.manager import KnowledgeManager
from app.services.llm.gemini import GeminiClient
from app.services.prompt_loader import PromptLoader
from app.workflow.models import Workflow, WorkflowResult


class ReviewerAgent(BaseAgent):
    """
    Final Quality Assurance Agent.

    Reviews the generated HTML against

    - DesignOS Identity
    - Design Principles
    - Design Language
    - Information Architecture
    - Validated DDOM

    Produces a structured review JSON.
    """

    def __init__(self):

        self.llm = GeminiClient()

        self.prompt_loader = PromptLoader()

        self.knowledge = KnowledgeManager()

    def execute(
        self,
        workflow: Workflow,
    ) -> WorkflowResult:

        html = workflow.context.shared_data.get("html")
        ddom = workflow.context.shared_data.get("ddom")

        if html is None:

            return WorkflowResult(
                success=False,
                error="Rendered HTML not found."
            )

        if ddom is None:

            return WorkflowResult(
                success=False,
                error="DDOM not found."
            )

        review_prompt = self.prompt_loader.load(
            "reviewer_prompt"
        )

        identity = self.knowledge.get(
            "identity"
        ).content

        design_principles = self.knowledge.get(
            "design_principles"
        ).content

        design_language = self.knowledge.get(
            "design_language"
        ).content

        information_architecture = self.knowledge.get(
            "information_architecture"
        ).content

        ddom_json = json.dumps(
            ddom.model_dump(),
            indent=2,
        )

        final_prompt = f"""
{review_prompt}

==========================================================
IDENTITY
==========================================================

{identity}

==========================================================
DESIGN PRINCIPLES
==========================================================

{design_principles}

==========================================================
DESIGN LANGUAGE
==========================================================

{design_language}

==========================================================
INFORMATION ARCHITECTURE
==========================================================

{information_architecture}

==========================================================
VALIDATED DDOM
==========================================================

{ddom_json}

==========================================================
GENERATED HTML
==========================================================

{html}

==========================================================
TASK
==========================================================

Review the generated HTML against the DDOM and the
DesignOS knowledge.

Return ONLY valid JSON.
"""

        response = self.llm.generate(
            final_prompt
        )

        print()

        print("=" * 70)
        print("RAW REVIEW RESPONSE")
        print("=" * 70)
        print(response)

        clean_response = response.strip()

        if clean_response.startswith("```json"):
            clean_response = clean_response[7:]

        elif clean_response.startswith("```"):
            clean_response = clean_response[3:]

        if clean_response.endswith("```"):
            clean_response = clean_response[:-3]

        clean_response = clean_response.strip()

        try:

            review = json.loads(
                clean_response
            )

        except json.JSONDecodeError:

            return WorkflowResult(
                success=False,
                error="Reviewer returned invalid JSON."
            )

        workflow.context.shared_data["review"] = review

        return WorkflowResult(
            success=True,
            output=review,
        )