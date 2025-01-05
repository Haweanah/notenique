from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa95e726010ac65ea9a882fa1e0bcd3'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Get the project directory
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "site.db")}'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from notenique.users.routes import users
from notenique.notes.routes import notes
from notenique.main.routes import main

app.register_blueprint(users)
app.register_blueprint(notes)
app.register_blueprint(main)