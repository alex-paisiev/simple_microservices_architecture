from pydantic import ConfigDict
from pydantic_settings import BaseSettings


# Environment variables
class Settings(BaseSettings):
    PORT: int = 5000
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    OPENAI_MODEL_MAX_TOKENS: int = 100
    OPENAI_MODEL_TEMPERATURE: float = 0.7
    ALLOWED_CORS_ORIGINS: list = ["http://backend-service:4000"]
    LOG_LEVEL: str = "DEBUG"

    model_config = ConfigDict(env_file=None)


settings = Settings()
