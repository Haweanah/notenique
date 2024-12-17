from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'aaa95e726010ac65ea9a882fa1e0bcd3'

posts = [
  {
    'author': 'Nana Hauwa',
    'title': 'My First Blog Post',
    'content': 'This is my first ever post on Notenique app and I hope to make the best of it',
    'date_posted': 'Jan 9, 1999'
  },

  {
    'author': 'Fola Adeola',
    'title': 'My Second Blog Post',
    'content': 'This is my second post on Notenique app and I hope you find it interesting',
    'date_posted': 'Jan 28, 1999'
  }
]

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html', posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/register")
def register():
  form = RegistrationForm()
  return render_template('register.html', title='Register', form=form)
@app.route("/login")
def login():
  form = LoginForm()
  return render_template('login.html', title='Register', form=form)

if __name__ == '__main__':
  app.run(debug=True)