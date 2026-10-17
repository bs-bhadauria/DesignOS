import requests
import io
from PIL import Image

def test():
    files_list = []
    for i in range(8):
        img = Image.new('RGB', (100, 100), color = 'blue')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_bytes = img_byte_arr.getvalue()
        # requests allows passing a list of tuples for multiple files with the same key
        files_list.append(('files', (f'image_{i}.jpg', img_bytes, 'image/jpeg')))
    
    data = {'prompt': 'Create a presentation deck for DesignOS based on this image.'}
    
    print("Sending 8 images request to 8001...")
    try:
        r = requests.post("http://127.0.0.1:8001/api/v1/generate", data=data, files=files_list, timeout=150)
        print("Status:", r.status_code)
        if r.status_code != 200:
            print(r.text)
        else:
            print("SUCCESS")
    except Exception as e:
        print("Exception:", e)

if __name__ == "__main__":
    test()
