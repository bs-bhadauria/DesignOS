import asyncio
import aiohttp
import os
from PIL import Image
import io

async def test_end_to_end():
    # 1. Create a dummy image in memory
    print("Creating dummy image...")
    img = Image.new('RGB', (100, 100), color = 'red')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_bytes = img_byte_arr.getvalue()
    
    # 2. Prepare the multipart form data
    print("Preparing upload...")
    form = aiohttp.FormData()
    form.add_field('prompt', 'Create a presentation deck for DesignOS based on this image.')
    form.add_field('files', img_bytes, filename='designos_idea.png', content_type='image/png')
    
    # 3. Send the request to the FastAPI backend
    print("Sending request to http://127.0.0.1:8001/api/v1/generate ...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post("http://127.0.0.1:8001/api/v1/generate", data=form, timeout=120) as response:
                print(f"Status Code: {response.status}")
                result = await response.json()
                print("Result:")
                print(result.get("html", "No HTML returned")[:500] + "...\n[HTML truncated for brevity]")
                print("SUCCESS!")
    except Exception as e:
        print(f"Error during request: {e}")

if __name__ == "__main__":
    asyncio.run(test_end_to_end())
