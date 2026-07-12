import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("Interrogating Google API for available models...")
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
response = requests.get(url).json()

if 'error' in response:
    print(f"API Error: {response['error']['message']}")
else:
    print("\n--- AVAILABLE GENERATIVE MODELS ---")
    for model in response.get('models', []):
        # We only want models that support text generation
        if 'generateContent' in model.get('supportedGenerationMethods', []):
            # Print the exact string needed for the URL
            print(model['name'])