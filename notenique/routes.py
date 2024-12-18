from flask import render_template, url_for, flash, redirect
from notenique import app
from notenique.forms import RegistrationForm, LoginForm
from notenique.models import User, Note


notes = [
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
  return render_template('home.html', notes=notes)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', notes=notes)

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account successfully created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('Logged in successfully!', 'success')
      return redirect(url_for('dashboard'))
    else:
      flash('Failed to Login. Please check your email and password', 'danger')
  return render_template('login.html', title='Register', form=form)
