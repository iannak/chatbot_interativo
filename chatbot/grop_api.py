import requests
import os

class GroqLLM:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_base = "https://api.groq.com/openai/v1" 
    
    def generate(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        model = "llama-3.3-70b-versatile" 
        
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(f"{self.api_base}/chat/completions", json=data, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data["choices"][0]["message"]["content"].strip()
        else:
            return f"Error: {response.status_code} - {response.text}"
