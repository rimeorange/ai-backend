from app.services.llm_service import LLMServices

class ChatServices:
    
    def __init__(self, llm_service: LLMServices):
        self.llm_service = llm_service
        self.histories = {}
        
    def chat(self, user_id:str, prompt: str) -> str:
        messages = self.histories.get(user_id, [])
        
        messages.append({
            "role": "user",
            "content": prompt
        })
        
        answer = self.llm_service.ask(messages)
        
        messages.append({
            "role": "assistant",
            "content": answer
        })
        
        self.histories[user_id] = messages
        
        return answer