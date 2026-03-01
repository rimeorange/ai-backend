from openai import OpenAI, api_key
from app.core.config import settings

class OpenAIClient:
    def __init__(self):
        # OpenAI는 SDK 클래스(공식)
        self.client = OpenAI(api_key=settings.openai_api_key)

    def chat(self, user_message: str) -> str:
        resp = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
        )
        return resp.choices[0].message.content