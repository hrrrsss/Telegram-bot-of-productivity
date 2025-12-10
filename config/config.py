from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    log_level: str
    log_format: str

    acces_token: str
    receiver: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()