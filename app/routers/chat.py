from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.services.llm_service import LLMServices
from app.services.chat_service import ChatServices
from app.repositories.memory_repository import MemoryRepository

router = APIRouter()
llm_service = LLMServices()
memory_repository = MemoryRepository()
chat_service = ChatServices(llm_service, memory_repository)

@router.post("/chat")
def chat(request: ChatRequest):
    answer = chat_service.chat(request.user_id, request.prompt)
    
    return {
        "message": answer
    }