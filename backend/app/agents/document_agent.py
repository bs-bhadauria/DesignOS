from app.services.prompt_loader import PromptLoader
from app.services.llm.router import LLMRouter


class DocumentAgent:
    """
    AI Agent responsible for generating
    document content using an LLM.
    """

    def __init__(
        self,
        prompt_loader: PromptLoader,
        llm: LLMRouter,
    ):
        self.prompt_loader = prompt_loader
        self.llm = llm

    async def generate(self, user_prompt: str, files: list = None) -> str:
        """
        Generate a document from a user prompt using a 2-stage pipeline:
        Stage 1: Content Outline Generation (JSON)
        Stage 2: Visual HTML Rendering (Tailwind CSS)
        """
        import re
        import asyncio

        # --- Stage 1: Content Planning ---
        planner_template = self.prompt_loader.load("content_planner")
        planner_prompt = planner_template.replace("{{prompt}}", user_prompt)
        
        # Call LLM to get structured JSON content
        # Prepare multimodal payload
        payload = [planner_prompt]
        if files:
            for f in files:
                payload.append(f)
                
        raw_json_response = await asyncio.to_thread(self.llm.generate, payload)
        
        # Clean potential markdown JSON formatting using regex
        cleaned_json = raw_json_response.strip()
        json_match = re.search(r"```(?:json)?\s*(.*?)\s*```", cleaned_json, re.DOTALL | re.IGNORECASE)
        if json_match:
            cleaned_json = json_match.group(1).strip()
        else:
            # Fallback to extracting just the JSON braces
            brace_match = re.search(r"(\{.*\}|\[.*\])", cleaned_json, re.DOTALL)
            if brace_match:
                cleaned_json = brace_match.group(1).strip()

        # --- Stage 2: Visual HTML Generation ---
        renderer_template = self.prompt_loader.load("startup_pitch")
        renderer_prompt = renderer_template.replace("{{json_outline}}", cleaned_json).replace("{{user_prompt}}", user_prompt)
        
        # Call LLM to render JSON outline into Tailwind HTML
        html_response = await asyncio.to_thread(self.llm.generate, renderer_prompt)
        
        # Clean potential markdown HTML formatting using regex
        cleaned_html = html_response.strip()
        html_match = re.search(r"```(?:html)?\s*(.*?)\s*```", cleaned_html, re.DOTALL | re.IGNORECASE)
        if html_match:
            cleaned_html = html_match.group(1).strip()
        else:
            # Fallback to extracting everything from the first < to the last >
            tag_match = re.search(r"(<.*>)", cleaned_html, re.DOTALL)
            if tag_match:
                cleaned_html = tag_match.group(1).strip()
        
        return cleaned_html.strip()