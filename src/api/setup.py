from typing import Any

from fastapi import FastAPI

from src.core import AppSettings


def init_app(
        settings: AppSettings,
        **kwargs: Any,
) -> FastAPI:
    return FastAPI(
        title=settings.title,
        description=settings.description,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
        debug=settings.debug,
        **kwargs
    )
