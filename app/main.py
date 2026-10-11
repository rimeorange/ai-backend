from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.get("/hello")
def hello():
    return {"message": "hello"}

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "message": request.prompt
    }