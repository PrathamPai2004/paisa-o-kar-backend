import enum
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from backend root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

class Roles(enum.Enum):
    ADMIN="ADMIN"
    SUPER_ADMIN="SUPER_ADMIN"
    STUDENT="STUDENT"
    CLASS_REPRESENTATIVE="CLASS_REPRESENTATIVE"
    ALUMINI="ALUMINI"




class Settings:
    APP_NAME = os.getenv("APP_NAME","Faculty Backend") 
    DEBUG = os.getenv("DEBUG")

    MONGODB_URI = os.getenv("MONGODB_URI")
    POSTGRES_URI = os.getenv("POSTGRES_URI")

    JWT_SECRET = os.getenv("JWT_SECRET")
    ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

settings = Settings()