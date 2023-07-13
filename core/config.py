import enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvVariables(enum.Enum):
    DEVELOPMENT: str = 'development'
    PRODUCTION: str = 'production'


class Config(BaseSettings):
    ENV: EnvVariables
    SECRET_KEY: str
    APP_HOST: str
    APP_PORT: int
    DB_URL: str
    TEST_DB_URL: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


config = Config()
