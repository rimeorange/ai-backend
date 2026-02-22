from fastapi import FastAPI
from pydantic import BaseModel
import logging

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    logger.info(f"message: {req.message}")
    return {"reply": f"echo: {req.message}"}