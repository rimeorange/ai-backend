from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest
from app.services.chat_service import ChatService
import uuid

router = APIRouter(tags=["chat"])
chat_service = ChatService()

@router.post("/chat")
def chat(req: ChatRequest):
    reuest_id = str(uuid.uuid4())

    try:
        reply = chat_service.reply(req.message)
        return {
            "request_id": reuest_id,
            "reply" : reply
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))