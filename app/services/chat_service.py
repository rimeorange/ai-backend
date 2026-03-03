import logging
import time
from app.core.config import settings
from app.clients.openai_client import OpenAIClient, LLMAuthError, LLMRateLimitError, LLMTemporaryError, LLMError

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

        #2) LLM 모드인데 키가 없으면 안내
        if not settings.openai_api_key:
            logger.warning("LLM mode is on but OPENAI_API_KEY is missing")
            return "LLM_MODE=on 이지만 OPENAI_API_KEY가 없습니다. .env에 키를 설정하세요."

        #3) 키가 있으면 LLM 호출
        if self.llm is None:
            self.llm = OpenAIClient()

        start = time.time()

        try:
            result =  self.llm.chat(msg)
            duration = round((time.time() - start) * 1000, 2) # ms 단위
            logger.info("LLM success | duration_ms=%s", duration)
            return result

        except LLMAuthError as e:
            logger.warning("LLM auth error: %s", e)
            return "LLM 인증에 실패했습니다. OPENAI_API_KEY를 확인하세요."

        except LLMRateLimitError as e:
            logger.warning("LLM rate limit: %s", e)
            return "요청이 많아 잠시 후 다시 시도해주세요."

        except LLMTemporaryError as e:
            logger.warning("LLM temporary error: %s", e)
            return "LLM 연결이 불안정합니다. 잠시 후 다시 시도해주세요."

        except LLMError as e:
            logger.exception("LLM error: %s", e)
            return "LLM 처리 중 오류가 발생했습니다."