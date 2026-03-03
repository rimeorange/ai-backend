from openai import OpenAI
from openai import AuthenticationError, RateLimitError, APIConnectionError, APITimeoutError
from app.core.config import settings

class LLMError(Exception):
    """LLM 호출 실패의 공통 베이스 예외"""
    pass

class LLMAuthError(LLMError):
    """API 키/인증 문제"""
    pass

class LLMRateLimitError(LLMError):
    """레이트리밋/쿼터 문제"""
    pass

class LLMTemporaryError(LLMError):
    """일시적 장애(네트워크/타임아웃 등)"""
    pass

class OpenAIClient:
    def __init__(self):
        # OpenAI는 SDK 클래스(공식)
        # timeout은 초 단위(예: 10초)
        self.client = OpenAI(
            api_key=settings.openai_api_key,
            timeout=10
        )

    def chat(self, user_message: str) -> str:
        last_err = None

        #최대 2회 시도 (1회 실패하면 1번 더)
        for attempt in range(2):
            try:
                resp = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_message},
                    ],
                )
                return resp.choices[0].message.content

            except AuthenticationError as e:
                # 키가 잘못됏거나 권한 없음
                raise LLMAuthError("OPENAI_API_KEY가 유효하지 않습니다.") from e

            except RateLimitError as e:
                # 너무 많은 요청/쿼터 부족
                raise LLMRateLimitError("요청이 너무 많습니다.(레이트리밋/쿼터). 잠시 후 다시 시도하세요.") from e

            except (APITimeoutError, APIConnectionError) as e:
                # 타임아웃/네트워크 문제
                raise  LLMTemporaryError("LLM 서버 연결이 불안정합니다. 잠시 후 다시 시도하세요.") from e

            except Exception as e:
                # 그 외는 일단 공통 에러로
                raise LLMError("LLM 호출 중 알 수 없는 오류가 발생했습니다.") from e

        # 여긴 사실상 도달하지 않지만, 안전장치
        raise LLMTemporaryError("LLM 호출 재시도에 실패했습니다.") from last_err