import requests
import json
from collections.abc import Iterator

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
    
    def ask_stream(self, messages: list[dict[str, str]]) -> Iterator[str]:
        payload = {
            "model": "qwen2.5:3b",
            "messages": messages,
            "stream": True
        }
        
        with requests.post(
            "http://localhost:11434/api/chat",
            json=payload,
            stream=True,
            timeout=120
        ) as response:
            
            response.raise_for_status()
            
            for line in response.iter_lines():
                
                if not line:
                    continue
                
                data = json.loads(line)
                
                if data.get("done"):
                    break
                
                content = data["message"]["content"]
                
                if content:
                    yield content
            
        