from openai import OpenAI, api_key
from app.core.config import settings

class OpenAIClient:
    """
    OpenAI API 호출을 담당하는 클래스.
    - API 키 로딩/연결을 여기서만 처리
    - 나중에 타임아웃, 재시도, 모델 변경도 여기서
    """
    def __init__(self):
        # settings.openai_api_key는 .env에서 얽힌 값
        self.client = OpenAIClient(api_key=settings.open_api_key)

        def chat(self, user_message: str) -> str:
            """
            사용자 메시지를 받아 LLM 응답 텍스트만 변환
            """
            resp = self.client.chat.completions.create(
                model="gpt-4o-mini",
                message=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ],
            )

            # OpenAI 응답에서 가장 첫 번째 답변 텍스트만 꺼냄
            return resp.choices[0].message.content