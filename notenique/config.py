import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecretkey')

    SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    os.getenv('SQLALCHEMY_DATABASE_URI')
)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('DEBUG') == 'True'
    TESTING = os.getenv('TESTING') == 'True'