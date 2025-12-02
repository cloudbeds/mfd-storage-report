import logging
import os

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    class Config:
        case_sensitive = True

    FACT_API_URL: str = os.getenv("FACT_API_URL", "https://api.fact.com")
    FACT_API_TOKEN: str = os.getenv("FACT_API_TOKEN", "some-random-token")
    LOG_LEVEL: int = int(os.getenv("LOG_LEVEL", logging.INFO))


settings = AppSettings()
