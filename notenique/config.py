import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv(dotenv_path="C:/Users/HP/Downloads/notenique/.env")

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')  # Load directly from the environment variable
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('DEBUG') == 'True'
    TESTING = os.getenv('TESTING') == 'True'