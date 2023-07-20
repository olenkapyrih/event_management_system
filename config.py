from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool
    SECRET_KEY: str

    HOST: str
    PORT: int

    CORS_ALLOW_ALL_ORIGINS: bool

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int

    PGADMIN_DEFAULT_EMAIL: str
    PGADMIN_DEFAULT_PASSWORD: str
    PGADMIN_PORT: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


