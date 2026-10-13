from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.get("/hello")
def hello():
    return {"message": "hello"}

@app.post("/chat")
def chat(request: ChatRequest):
    payload = {
        "model" : "qwen2.5:3b",
        "messages": [
            {
                "role": "user",
                "content": request.prompt
            }
        ],
        "stream": False
    }
    
    response = requests.post(
        "http://localhost:11434/api/chat",
        json=payload
    )
  
    data = response.json()
    
    return {
        "message": data["message"]["content"]
    }