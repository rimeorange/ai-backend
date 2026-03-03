# AI Backend Starter

FastAPI 기반의 AI 백엔드 전환 프로젝트.
(현재는 기본 API + 프로젝트 구조/아키텍처 정리 단계)


## Project Structure
- `app/main.py` : FastAPI 앱 생성 및 라우터 등록(조립 역활)
- `app/api/routes` : API 엔드포인트(라우터)
- `app/schemas/` : Request/Response 모델(Pydantic)
- `app/services` : 비지니스 로직(라우터는 얇게 유지)
- `app/core/config.py` : `.env` 기반 설정 로딩
- `app/core/logging.py` : 로깅 설정 초기화
- 
## Run (Local)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # (없으면 아래 pip install 참고)
uvicorn app.main:app --reload
```

## LLM Integration (Week2)
- LLM_MODE 환경 변수로 echo / LLM 모드 전환
- OpenAIClient에서 외부 API 호출 전담
- 인증/레이트리밋/네트워크 오류를 도메인 예외로 변환
- ChatService에서 예외를 사용자 친화 메시지로 처리
- Timeout(10s) + 1회 재시도 적용
- request_id 및 duration(ms) 로깅


### Architecture Summary
- Router는 요청/응답 처리만 담당
- Service는 비지니스 로직 담당
- Client는 외부 API 호출 담당
- Core는 설정 및 로깅 담당