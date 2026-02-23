from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter(tags=["chat"])
chat_service = ChatService()

@router.post("/chat")
def chat(req: ChatRequest):
    try:
        reply = chat_service.echo(req.message)
        return {"reply" : reply}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))