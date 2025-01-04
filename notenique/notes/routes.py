from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from notenique import db
from notenique.models import Note
from notenique.notes.forms import NoteForm


notes = Blueprint('notes', __name__)

@notes.route("/post/new", methods=['GET', 'POST'])
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

@notes.route("/note/<int:note_id>")
def note(note_id):
  note = Note.query.get_or_404(note_id)
  return render_template('note.html', title=note.title, note=note)

@notes.route("/note/<int:note_id>/edit", methods=['GET', 'POST'])
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

@notes.route("/note/<int:note_id>/delete", methods=['POST'])
@login_required
def delete_note(note_id):