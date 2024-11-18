from src.core.server import run_uvicorn_server
from src.core import get_app_settings, get_uvicorn_settings
from src.api import init_app


def main():
    app_settings = get_app_settings()
    uvicorn_settings = get_uvicorn_settings()

    app = init_app(app_settings)
    run_uvicorn_server(app, uvicorn_settings)


if __name__ == '__main__':
    main()