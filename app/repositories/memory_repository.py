
class MemoryRepository:
    
    def __init__(self):
        self.histories = {}
        
    def find_by_user_id(self, user_id: str) -> list[dict[str,str]]:
        return self.histories.get(user_id, [])    
    
    def save(self, user_id:str, messages: list[dict[str, str]]) -> None:
        self.histories[user_id] = messages