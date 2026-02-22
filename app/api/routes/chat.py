import logging
from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest

router = APIRouter(tags=["chat"])
logger = logging.getLogger(__name__)

@router.post("/chat")
def chat(req: ChatRequest):
    msg = req.message.strip()
    if not msg:
        raise HTTPException(status_code=400, detail="message is empty")

    logger.info("message: %s", msg)
    return {"reply": f"echo: {msg}"}