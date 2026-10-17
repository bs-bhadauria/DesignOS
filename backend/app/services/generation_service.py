import uuid

from app.agents.document_agent import DocumentAgent
from app.schemas.generate import GenerateRequest, GenerateResponse


class GenerationService:
    """
    Coordinates document generation.

    Dependencies are injected from the outside.
    """

    def __init__(
        self,
        agent: DocumentAgent,
    ):
        self.agent = agent

    async def generate(
        self,
        prompt: str,
        files: list = None,
    ) -> GenerateResponse:

        parsed_files = []
        if files:
            for file in files:
                content = await file.read()
                parsed_files.append({
                    "mime_type": file.content_type,
                    "data": content
                })

        html = await self.agent.generate(
            user_prompt=prompt,
            files=parsed_files
        )

        return GenerateResponse(
            success=True,
            request_id=str(uuid.uuid4()),
            status="completed",
            html=html,
        )