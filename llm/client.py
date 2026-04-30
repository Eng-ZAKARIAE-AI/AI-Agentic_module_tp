import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class LLMClient:
    def __init__(self, api_key: str = None):
        """
        Initialize with a direct API key string or from environment.
        """
        if api_key is None:
            api_key = "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"
        
        # Clean the key immediately to remove any accidental quotes or spaces
        self.api_key = api_key.replace('"', '').replace("'", "").strip()
        self.url = "https://openrouter.ai/api/v1/chat/completions"

        if not self.api_key:
            logger.error("LLMClient initialized with an empty API Key!")
        else:
            # Masked print for security verification
            print(f"✅ Client initialized with key ending in: ...{self.api_key[-4:]}")

    def predict(self, prompt: str) -> str:
        if not self.api_key:
            return "Error: No API Key provided to client."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000", 
            "X-Title": "SMA Client"
        }

        data = {
            "model": "google/gemini-2.0-flash-001", 
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(self.url, headers=headers, json=data)
            
            if response.status_code == 200:
                result = response.json()
                if 'choices' in result:
                    return result['choices'][0]['message']['content']
                return "Error: Unexpected response format."
            
            else:
                # Return the full error message from OpenRouter for debugging
                return f"Error {response.status_code}: {response.text}"
                
        except Exception as e:
            return f"An error occurred during request: {str(e)}"

# Global client instance for llm_predict
_client = None

def llm_predict(prompt: str) -> str:
    global _client
    if _client is None:
        _client = LLMClient()
    return _client.predict(prompt)

if __name__ == "__main__":
    # --- INJECT YOUR KEY HERE ---
    MY_INJECTED_KEY = "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"
    
    client = LLMClient(MY_INJECTED_KEY)
    
    print("\n--- Testing client.py with Direct Injection ---")
    print(f"Result: {client.predict('Connection Successful')}")