import requests

class LLMServices:
    
    def ask(self, messages: list[dict[str, str]]) -> str:
        payload = {
            "model": "qwen2.5:3b",
            "messages": messages,
            "stream": False
        }
        
        response = requests.post(
            "http://localhost:11434/api/chat",
            json=payload
        )
        
        data = response.json()
        
        return data["message"]["content"]