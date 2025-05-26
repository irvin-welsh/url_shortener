from pydantic import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    env_name: str = os.getenv('ENV_NAME')
    base_url: str = os.getenv('BASE_URL')
    db_url: str = os.getenv('DB_URL')

@lru_cache
def get_setting() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
