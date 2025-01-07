from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from notenique.config import Config

# Initialize the extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
migrate = Migrate()

def create_app(config_class=Config):
    # Load environment variables from .env file
    load_dotenv()  # This loads the environment variables from the .env file

    # Create the Flask app instance
    app = Flask(__name__, static_folder='static')
    
    # Load app configuration from the Config class
    app.config.from_object(config_class)

    # Initialize the extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)  # Initialize migration

    # Register Blueprints (Your routes for different parts of the app)
    from notenique.users.routes import users
    from notenique.notes.routes import notes
    from notenique.main.routes import main
    from notenique.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(notes)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
