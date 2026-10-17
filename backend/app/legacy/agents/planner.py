import json

from app.agents.base import BaseAgent
from app.services.llm.gemini import GeminiClient
from app.services.prompt_loader import PromptLoader
from app.workflow.models import Workflow, WorkflowResult


class PlannerAgent(BaseAgent):
    """
    Planner Agent responsible for creating
    a structured document plan.
    """

    def __init__(self) -> None:
        self.prompt_loader = PromptLoader()
        self.llm = GeminiClient()

    def execute(
        self,
        workflow: Workflow,
    ) -> WorkflowResult:
        """
        Execute the planning stage.
        """

        system_prompt = self.prompt_loader.load("planner_prompt")

        final_prompt = (
            f"{system_prompt}\n\n"
            f"User Request:\n"
            f"{workflow.context.user_prompt}"
        )

        response = self.llm.generate(final_prompt)

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
            plan = json.loads(clean_response)
        except json.JSONDecodeError:
            return WorkflowResult(
                success=False,
                error="Planner returned invalid JSON."
            )

        workflow.context.shared_data["plan"] = plan

        return WorkflowResult(
            success=True,
            output=plan,
        )