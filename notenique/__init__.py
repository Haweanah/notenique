from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from notenique.config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)
    

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

     # Initialize migration after app is created
    migrate = Migrate(app, db)

    from notenique.users.routes import users
    from notenique.notes.routes import notes
    from notenique.main.routes import main
    from notenique.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(notes)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
