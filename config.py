# url_shortener/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "local"
    base_url: str = "http://localhost:8000"
    db_url: str= "sqlite:///./shorterner.db"

def get_setting() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
