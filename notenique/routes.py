import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from notenique import app, db, bcrypt
from notenique.forms import RegistrationForm, LoginForm, UpdateAccountForm, NoteForm
from notenique.models import User, Note
from flask_login import login_user, current_user, logout_user, login_required



@app.route("/")
@app.route("/home")
def home():
  page = request.args.get('page', 1, type=int)
  notes = Note.query.paginate(page=page, per_page=2)
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

def save_picture(form_picture):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(form_picture.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(app.root_path, 'static/photo', picture_fn)

  output_size = (125, 125)
  i = Image.open(form_picture)
  i.thumbnail(output_size)
  i.save(picture_path)

  return picture_fn

@app.route("/account", methods=['GET', 'POST'])
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
    return redirect(url_for('account'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.email.data = current_user.email
  image_file = url_for('static', filename = 'photo/' + (current_user.image_file or 'default.jpg'))
  print(f"Generated image file path: {image_file}")
  return render_template('account.html', title='Account', image_file = image_file, form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_note():
    form = NoteForm()
    
    if form.validate_on_submit():
        # Capture the HTML content from Quill editor
        content = form.content.data  # This is the content passed from the form (which will be Quill content)

        # Save the new note with the content (HTML)
        note = Note(title=form.title.data, content=content, author=current_user)
        db.session.add(note)
        db.session.commit()

        flash('Your note has been created!', 'success')
        return redirect(url_for('home'))
    
    return render_template('create_note.html', title='New Note', form=form, legend='New Note')

@app.route("/note/<int:note_id>")
def note(note_id):
  note = Note.query.get_or_404(note_id)
  return render_template('note.html', title=note.title, note=note)

@app.route("/note/<int:note_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
  note = Note.query.get_or_404(note_id)
  if note.author != current_user:
    abort(403)
  form = NoteForm()
  if form.validate_on_submit():
    note.title = form.title.data
    note.content = form.content.data
    db.session.commit()
    flash('Your note has been edited', 'success')
    return redirect(url_for('note', note_id=note.id))
  elif request.method == 'GET':
    form.title.data = note.title
    form.content.data = note.content
  return render_template('create_note.html', title='Edit Note', form=form, legend='Edit Note')

@app.route("/note/<int:note_id>/delete", methods=['POST'])
@login_required
def delete_note(note_id):
  note = Note.query.get_or_404(note_id)
  if note.author != current_user:
    abort(403)
  db.session.delete(note)
  db.session.commit()
  flash('Your note has been deleted', 'success')
  return redirect(url_for('home'))
    