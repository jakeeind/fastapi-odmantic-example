from functools import lru_cache
from typing import Dict, Any, List
from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DEBUG: bool = True
    TITLE: str = "FastAPI-React"
    VERSION: str = "0.0.1"

    SECRET_KEY: str = "thisissecretkey"
    JWT_TOKEN_PREFIX: str = "TOKEN"

    MONGODB_DB: str="fastapi_react_db"
    MONGODB_HOST: str="localhost"
    MONGODB_PORT=27017

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 24 * 60  # 1 day
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 7 * 24 * 60  # 7 days
    ALGORITHM = "HS256"

    ALLOWED_HOSTS: List[str] = ["*"]

    ROUTER_ROOT: str = "app/api/"
    API_PREFIX: str = "/api"

    class Config:
        env_file = ".env"
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {"debug": self.DEBUG, "title": self.TITLE, "version": self.VERSION}


@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()
