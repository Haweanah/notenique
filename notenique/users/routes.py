from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from notenique import db, bcrypt
from notenique.models import User, Note
from notenique.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from notenique.users.utils import save_picture


from flask import Blueprint

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash(f'Account successfully created!, You can now log in to create your notes', 'success')
    return redirect(url_for('users.login'))
  return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('main.home'))
    else:
      flash('Login Unsuccessful. Please check your email and password', 'danger')
  return render_template('login.html', title='Login', form=form)

@users.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
  form = UpdateAccountForm()
  if form.validate_on_submit():
    if form.picture.data:
      picture_file = save_picture(form.picture.data)
      current_user.image_file = picture_file
    current_user.username = form.username.data
    current_user.email = form.email.data
    db.session.commit()
    flash('Your profile has been successfully updated!', 'success')
    return redirect(url_for('users.account'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.email.data = current_user.email
  image_file = url_for('static', filename = 'photo/' + (current_user.image_file or 'default.jpg'))
  print(f"Generated image file path: {image_file}")
  return render_template('account.html', title='Account', image_file = image_file, form=form)

