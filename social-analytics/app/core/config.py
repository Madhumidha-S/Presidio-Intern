from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()  

class Settings(BaseSettings):
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_host: str = os.getenv("DB_HOST")
    db_port: str = os.getenv("DB_PORT")
    db_name: str = os.getenv("DB_NAME")

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    PROJECT_NAME: str = "Social Media Analytics API"

    class Config:
        env_file = ".env"

settings = Settings()
