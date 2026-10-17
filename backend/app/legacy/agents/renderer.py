import json

from app.agents.base import BaseAgent
from app.knowledge.manager import KnowledgeManager
from app.services.llm.gemini import GeminiClient
from app.services.prompt_loader import PromptLoader
from app.workflow.models import Workflow, WorkflowResult


class RendererAgent(BaseAgent):
    """
    Converts a validated DDOM into production-quality HTML.
    """

    def __init__(self):

        self.llm = GeminiClient()

        self.prompt_loader = PromptLoader()

        self.knowledge = KnowledgeManager()

    def execute(
        self,
        workflow: Workflow,
    ) -> WorkflowResult:

        ddom = workflow.context.shared_data.get("ddom")

        if ddom is None:

            return WorkflowResult(
                success=False,
                error="DDOM not found.",
            )

        renderer_prompt = self.prompt_loader.load(
            "renderer_prompt"
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
{renderer_prompt}

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
TASK
==========================================================

Render the validated DDOM into a complete production-ready
HTML document.

Return ONLY HTML.

Begin immediately with:

<!DOCTYPE html>
"""

        response = self.llm.generate(
            final_prompt
        )

        html = response.strip()

        if html.startswith("```html"):
            html = html[7:]

        elif html.startswith("```"):
            html = html[3:]

        if html.endswith("```"):
            html = html[:-3]

        html = html.strip()

        workflow.context.shared_data["html"] = html

        return WorkflowResult(
            success=True,
            output=html,
        )