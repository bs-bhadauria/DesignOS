import asyncio
import traceback
from app.services.generation_service import GenerationService
from app.agents.document_agent import DocumentAgent
from app.services.prompt_loader import PromptLoader
from app.services.llm.gemini import GeminiClient

async def test():
    try:
        agent = DocumentAgent(prompt_loader=PromptLoader(), llm=GeminiClient())
        service = GenerationService(agent=agent)
        res = await service.generate(prompt="Test prompt", files=[])
        print("SUCCESS")
    except Exception as e:
        traceback.print_exc()

asyncio.run(test())
