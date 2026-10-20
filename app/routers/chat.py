from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.services.llm_service import LLMServices
from app.services.chat_service import ChatServices

router = APIRouter()
llm_service = LLMServices()
chat_service = ChatServices(llm_service)

@router.post("/chat")
def chat(request: ChatRequest):
    answer = chat_service.chat(request.prompt)
    
    return {
        "message": answer
    }