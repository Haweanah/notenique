from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa95e726010ac65ea9a882fa1e0bcd3'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Get the project directory
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "site.db")}'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'yenyenyen@gmail.com'
app.config['MAIL_PASSWORD'] = 'iamacuteprincess'
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@notenique.com'
mail = Mail(app)
from notenique import routes