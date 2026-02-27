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
