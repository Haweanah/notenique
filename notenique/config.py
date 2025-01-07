from dotenv import load_dotenv
import os

# Specify the full path to the .env file (adjust the path accordingly)
load_dotenv(dotenv_path="C:/Users/HP/Downloads/notenique/.env")

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', r'sqlite:///C:/Users/HP/Downloads/notenique/site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('DEBUG') == 'True'
    TESTING = os.getenv('TESTING') == 'True'