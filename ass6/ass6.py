import os
from dotenv import load_dotenv
import requests
from PIL import Image
from io import BytesIO

load_dotenv()

API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-2"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "image/png"
}

def generate_image(prompt: str):
    payload = {
        "inputs": prompt,
        "options": {
            "wait_for_model": True
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        print(response.text)
        return f"Error: {response.status_code}"

    image = Image.open(BytesIO(response.content))
    image.save("generated_image.png")
    return "Image generated and saved as generated_image.png"

# Test
prompt = "A small house near a river with mountains in the background"
print(generate_image(prompt))
