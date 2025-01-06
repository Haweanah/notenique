import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecretkey')  # Secure key for your app
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///C:/Users/HP/Downloads/notenique/site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional: disable tracking modifications to reduce overhead
