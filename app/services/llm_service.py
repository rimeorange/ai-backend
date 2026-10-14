import requests

class LLMServices:
    
    def ask(self, prompt: str) -> str:
        payload = {
            "model": "qwen2.5:3b",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        }
        
        response = requests.post(
            "http://localhost:11434/api/chat",
            json=payload
        )
        
        data = response.json()
        
        return data["message"]["content"]