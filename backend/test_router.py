import asyncio
import sys

from app.core.dependencies import get_llm

async def main():
    print("Testing LLM Router...")
    llm = get_llm()
    
    prompt = "Write a 1-sentence funny joke about a programmer."
    
    print(f"Sending prompt to router: {prompt}")
    
    # We use asyncio.to_thread because the agent uses it for synchronous LLMs
    response = await asyncio.to_thread(llm.generate, prompt)
    
    print("\n--- Response ---")
    print(response)
    print("----------------")

if __name__ == "__main__":
    asyncio.run(main())
