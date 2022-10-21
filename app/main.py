from typing import Any, Dict
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import register_routers
from app.core.db import init_mongo_engine
from .settings import AppSettings, get_app_settings


def init_app() -> FastAPI:
    settings: AppSettings = get_app_settings()
    app: FastAPI = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    register_routers(app, root=settings.ROUTER_ROOT)

    @app.get("/")
    def health() -> Dict[str, Any]:
        return {
            "title": settings.TITLE,
            "status": "Good",
        }

    return app
