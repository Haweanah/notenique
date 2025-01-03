from datetime import datetime, timezone
from itsdangerous import URLSafeTimedSerializer
from notenique import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(20), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(70), nullable=False)
  notes = db.relationship('Note', backref='author', lazy=True)

  def get_reset_token(self, expires_sec=1800):
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id}, salt='reset-password')

  @staticmethod
  def verify_reset_token(token):
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, salt='reset-password', max_age=1800)['user_id']
        except Exception as e:
            print(f"Token verification error: {e}")
            return None
        return User.query.get(user_id)   

  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
  content = db.Column(db.Text, nullable=False, )
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


  def __repr__(self):
    return f"Note('{self.title}', '{self.date_posted}')"
