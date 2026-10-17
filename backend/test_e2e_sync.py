import requests
import io
from PIL import Image

def test():
    img = Image.new('RGB', (100, 100), color = 'red')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_bytes = img_byte_arr.getvalue()
    
    files = {'files': ('designos_idea.png', img_bytes, 'image/png')}
    data = {'prompt': 'Create a presentation deck for DesignOS based on this image.'}
    
    print("Sending request to 8001...")
    r = requests.post("http://127.0.0.1:8001/api/v1/generate", data=data, files=files)
    print(r.status_code)
    print(r.text[:500])

if __name__ == "__main__":
    test()
