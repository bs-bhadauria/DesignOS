import asyncio
import traceback
from app.services.llm.gemini import GeminiClient

def test():
    try:
        client = GeminiClient()
        print(client.generate(["Hello"]))
        print("SUCCESS")
    except Exception as e:
        traceback.print_exc()

test()