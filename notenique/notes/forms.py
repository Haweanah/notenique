from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField,  SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])  # This will be populated by Quill's content
    submit = SubmitField('Save')
    
    def validate_content(self, content):
        pass

