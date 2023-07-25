from pydantic_settings import BaseSettings, SettingsConfigDict

from core.enums.env_enum import EnvEnum


class Config(BaseSettings):
    ENV: EnvEnum
    SECRET_KEY: str
    APP_HOST: str
    APP_PORT: int
    DB_URL: str
    REDIS_URL: str

    TEST_DB_URL: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


config = Config()
