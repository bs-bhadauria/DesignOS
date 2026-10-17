import asyncio
from app.core.dependencies import get_document_agent

async def test_pipeline():
    print("=" * 80)
    print("TESTING 2-STAGE LEAN DOCUMENT PIPELINE")
    print("=" * 80)
    
    agent = get_document_agent()
    prompt = "Create a startup pitch deck for an AI in Agriculture startup focusing on precision farming."
    
    print(f"User Prompt: '{prompt}'")
    print("\nRunning generation...")
    
    try:
        html = await agent.generate(prompt)
        print("\nSUCCESS! HTML Generated Successfully.")
        print(f"Output HTML Length: {len(html)} characters")
        print("\nPreview of Generated HTML (first 500 chars):")
        print("-" * 60)
        print(html[:500])
        print("-" * 60)
    except Exception as e:
        print("\nFAILED with error:")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_pipeline())
