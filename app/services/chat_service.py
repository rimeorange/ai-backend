from app.services.llm_service import LLMServices
from app.repositories.memory_repository import MemoryRepository

class ChatServices:
    
    def __init__(self, 
                 llm_service: LLMServices,
                 memory_repository: MemoryRepository):
        self.llm_service = llm_service
        self.memory_repository = memory_repository
        
    def chat(self, user_id:str, prompt: str) -> str:
        messages = self.memory_repository.find_by_user_id(user_id)
        
        messages.append({
            "role": "user",
            "content": prompt
        })
        
        answer = self.llm_service.ask(messages)
        
        messages.append({
            "role": "assistant",
            "content": answer
        })
        
        self.memory_repository.save(user_id, messages)
        
        return answer