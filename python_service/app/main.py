import logging

from app.api.routers import generate
from app.core.config import settings
from app.core.logging_config import configure_logging
from app.core.middlewares import add_cors_middleware
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
configure_logging()
LOGGER = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI LLM Service", version="1.0.0")
    LOGGER.info("FastAPI application created.")

    app.include_router(generate.router)
    LOGGER.info("Added generate router.")

    add_cors_middleware(app, allowed_origins=settings.ALLOWED_CORS_ORIGINS)
    LOGGER.info("Added CORS middleware")
    return app


app = create_app()
