from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    algorithm: str | None = None
    secret_key: str | None = None
    logo_folder: Path = Path(__file__).parent / "static" / "logo"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_config() -> Settings:
    return Settings()
