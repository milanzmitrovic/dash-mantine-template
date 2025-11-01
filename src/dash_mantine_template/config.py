"""
Purpose of this file is to help with
loading .env file at the beginning of
project initialization.

Otherwise, env vars could be used
before they are loaded.
"""

import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseModel):
    POSTGRES_USER: str = None
    POSTGRES_PASSWORD: str = None
    POSTGRES_HOST: str = None
    POSTGRES_PORT: int = None
    POSTGRES_DB: str = None


class EnvContext(BaseSettings):
    debug: bool = None
    app_env: str = None
    app_port: int = None
    log_file_location: str = None
    assets_folder: str = None
    pages_folder: str = None
    database: DatabaseSettings = DatabaseSettings()

    class Config:
        # Pick .test_env if running under pytest, else use .env
        env_file = "./tests/.test_env" if os.getenv("PYTEST_RUNNING") else "./src/.env"
        env_nested_delimiter = "__"  # <— important for nested env vars


env = EnvContext()
