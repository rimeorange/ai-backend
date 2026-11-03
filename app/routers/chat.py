from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.services.llm_service import LLMServices
from app.services.chat_service import ChatServices
from app.repositories.memory_repository import MemoryRepository
from fastapi.responses import StreamingResponse

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
    
@router.post("/chat/stream")
def chat_stream(request: ChatRequest):
    
    generator = chat_service.chat_stream(
        request.user_id,
        request.prompt
    )
    
    return StreamingResponse(
        generator,
        media_type="text/plain; charset=utf-8"
    )