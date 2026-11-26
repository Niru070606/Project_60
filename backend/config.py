import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "mysql+pymysql://project60_admin:Project60Admin123@127.0.0.1:3306/project60"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False