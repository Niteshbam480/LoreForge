from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = ".env")
    

    APP_NAME: str = "LoreForge"
    APP_VERSION: str = "0.1.0"
    SECRET_KEY: str = "xyz"
    DEBUG: bool = True
    DATABASE_URL: str = ""

settings = Settings()