from fastapi import FastAPI
from pydantic import BaseModel

from app.api.routes.health import router as health_router

import logging

app = FastAPI(title="AI Backend Starter")

app.include_router(health_router)

class ChatRequest(BaseModel):
    message: str

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/chat")
def chat(req: ChatRequest):
    logger.info(f"message: {req.message}")
    return {"reply": f"echo: {req.message}"}