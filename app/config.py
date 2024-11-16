from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    rate_limit_per_minute: int = 60

    class Config:
        env_file = ".env"

settings = Settings()
