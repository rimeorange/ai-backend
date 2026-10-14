from fastapi import FastAPI
from app.routers.chat import router

app = FastAPI()

app.include_router(router)

@app.get("/hello")
def hello():
    return {"message": "hello"}

