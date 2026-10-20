from app.services.llm_service import LLMServices

class ChatServices:
    
    def __init__(self, llm_service: LLMServices):
        self.llm_service = llm_service
        
        
    def chat(self, prompt: str) -> str:
        return self.llm_service.ask(prompt)