from flask import render_template, url_for, flash, redirect, request
from notenique import app, db, bcrypt
from notenique.forms import RegistrationForm, LoginForm
from notenique.models import User, Note
from flask_login import login_user, current_user, logout_user, login_required


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

@app.route("/register", methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash(f'Account successfully created!, You can now log in to create your notes', 'success')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
      flash('Login Unsuccessful. Please check your email and password', 'danger')
  return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('home'))

@app.route("/dashboard")
@login_required
def dashboard():
  return render_template('dashboard.html', title='Dashboard')