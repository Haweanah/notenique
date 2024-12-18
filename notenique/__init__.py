from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa95e726010ac65ea9a882fa1e0bcd3'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Get the project directory
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "site.db")}'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from notenique import routes