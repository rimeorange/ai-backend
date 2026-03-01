import logging
from app.core.config import settings
from app.clients.openai_client import OpenAIClient

logger = logging.getLogger(__name__)

class ChatService:
    def __init__(self):
        self.llm = OpenAIClient()

    def reply(self, message: str) -> str:
        msg = message.strip()
        if not msg:
            raise ValueError("message is empty")

        #1) 기본은 echo 모드
        if settings.llm_mode.lower() != "on":
            logger.info("echo mode")
            return f"echo: {msg}"

        #2) LLM 모드인데 키가 없으몀 안내
        if not settings.openai_api_key:
            logger.warning("LLM mode is on but OPENAI_API_KEY is missing")
            return "LLM_MODE=on 이지만 OPENAI_API_KEY가 없습니다. .env에 키를 설정하세요."

        #3) 키가 있으면 LLM 호출
        logger.info("llm mode")
        return self.llm.chat(msg)
