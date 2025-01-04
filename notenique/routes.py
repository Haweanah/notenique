import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from notenique import app, db, bcrypt
from notenique.forms import RegistrationForm, LoginForm, UpdateAccountForm, NoteForm
from notenique.models import User, Note
from flask_login import login_user, current_user, logout_user, login_required





  note = Note.query.get_or_404(note_id)
  if note.author != current_user:
    abort(403)
  db.session.delete(note)
  db.session.commit()
  flash('Your note has been deleted', 'success')
  return redirect(url_for('home'))

  if current_user.is_authenticated:
    return redirect(url_for('home'))
  user = User.verify_reset_token(token)
  if user is None:
    flash('Invalid or expired token', 'warning')
    return redirect(url_for('reset_request'))
  form = ResetPasswordForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user.password = hashed_password
    db.session.commit()
    flash(f'Password successfully updated!, You can now log in to create your notes', 'success')
    return redirect(url_for('login'))
  return render_template('reset_token.html', title= 'Reset Password', form=form)