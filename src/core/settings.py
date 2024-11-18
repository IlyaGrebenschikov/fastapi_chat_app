from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath


def get_root_dir_path() -> Path:
    return Path(__file__).resolve().parent.parent.parent


class AppSettings(BaseSettings):
    root_dir_path: DirectoryPath = get_root_dir_path()
    model_config = SettingsConfigDict(
        env_file=f'{root_dir_path}/.env',
        env_file_encoding='utf-8',
        env_prefix='app_',
        extra='ignore'
    )

    title: Optional[str] = 'FastAPI'
    docs_url: Optional[str] = '/api/docs'
    redoc_url: Optional[str] = '/api/redoc'
    description: Optional[str] = 'Simple FastAPI application'
    debug: Optional[bool] = False


class UvicornSettings(BaseSettings):
    root_dir_path: DirectoryPath = get_root_dir_path()
    model_config = SettingsConfigDict(
        env_file=f'{root_dir_path}/.env',
        env_file_encoding='utf-8',
        env_prefix='uvicorn_',
        extra='ignore'
    )

    host: Optional[str] = '0.0.0.0'
    port: Optional[int] = 8080
    reload: Optional[bool] = False


class KafkaSettings(BaseSettings):
    root_dir_path: DirectoryPath = get_root_dir_path()
    model_config = SettingsConfigDict(
        env_file=f'{root_dir_path}/.env',
        env_file_encoding='utf-8',
        env_prefix='kafka_',
        extra='ignore'
    )

    host: str
    port: int

    @property
    def get_url(self) -> str:
        return f'{self.host}:{self.port}'



def get_app_settings() -> AppSettings:
    return AppSettings()


def get_uvicorn_settings() -> UvicornSettings:
    return UvicornSettings()


def get_kafka_settings() -> KafkaSettings:
    return KafkaSettings()
