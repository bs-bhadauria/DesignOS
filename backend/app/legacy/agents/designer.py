import json

from app.agents.base import BaseAgent
from app.services.llm.gemini import GeminiClient
from app.services.prompt_loader import PromptLoader
from app.workflow.models import Workflow, WorkflowResult


class DesignerAgent(BaseAgent):
    """
    Converts the planner output into a structured
    Design DSL representation.
    """

    def __init__(self):
        self.llm = GeminiClient()
        self.prompt_loader = PromptLoader()

    def execute(
        self,
        workflow: Workflow,
    ) -> WorkflowResult:

        system_prompt = self.prompt_loader.load(
            "designer_prompt"
        )

        planner_output = workflow.context.shared_data.get(
            "plan"
        )

        if planner_output is None:
            return WorkflowResult(
                success=False,
                error="Planner output not found."
            )

        final_prompt = (
            f"{system_prompt}\n\n"
            f"Planner Output:\n"
            f"{json.dumps(planner_output, indent=2)}"
        )

        response = self.llm.generate(final_prompt)

        print()
        print("=" * 60)
        print("RAW DESIGNER RESPONSE")
        print("=" * 60)
        print(response)
        print()

        clean_response = response.strip()

        if clean_response.startswith("```json"):
            clean_response = clean_response[7:]

        elif clean_response.startswith("```"):
            clean_response = clean_response[3:]

        if clean_response.endswith("```"):
            clean_response = clean_response[:-3]

        clean_response = clean_response.strip()

        try:
            design = json.loads(clean_response)

        except json.JSONDecodeError:

            return WorkflowResult(
                success=False,
                error="Designer returned invalid JSON."
            )

        workflow.context.shared_data["design"] = design

        return WorkflowResult(
            success=True,
            output=design,
        )