import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Base configuration class for the application."""

    # Secret key for session management and security
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # Base directory for project files
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Database URI: Read from environment variable or default to SQLite
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        f"sqlite:///{os.path.join(BASE_DIR, 'site.db')}"
    )

    # Optional: Additional configurations
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't', 'yes']
    TESTING = os.getenv('TESTING', 'False').lower() in ['true', '1', 't', 'yes']
