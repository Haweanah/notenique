import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecretkey')

    database_url = os.getenv("DATABASE_URL")

    SQLALCHEMY_DATABASE_URI = (
        database_url.replace(
            "postgresql://",
            "postgresql+psycopg2://"
        )
        if database_url else None
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('DEBUG') == 'True'
    TESTING = os.getenv('TESTING') == 'True'