from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    app_env:str
    openai_api_key: str
    llm_mode: str = "off"

    class Config:
        env_file = ".env"

settings = Settings()