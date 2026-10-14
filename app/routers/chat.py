from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.services.llm_service import LLMServices

router = APIRouter()
llm_service = LLMServices()

@router.post("/chat")
def chat(request: ChatRequest):
    answer = llm_service.ask(request.prompt)
    
    return {
        "message": answer
    }