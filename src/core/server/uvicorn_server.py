from typing import Any

import uvicorn
from fastapi import FastAPI

from src.core import UvicornSettings


def run_uvicorn_server(
        app: FastAPI,
        settings: UvicornSettings,
        **kwargs: Any
) -> None:
    uvicorn_config = uvicorn.Config(
        app,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        **kwargs,
    )
    server = uvicorn.Server(uvicorn_config)

    server.run()
