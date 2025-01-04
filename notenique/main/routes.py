from flask import render_template, request, Blueprint
from notenique.models import Note

main = Blueprint('main', __name__)

@main.route("/")
@main.route('/home', methods=['GET'])
def home():
    page = request.args.get('page', 1, type=int)  # Get the current page number from the request
    per_page = 5
    if current_user.is_authenticated:
        notes = Note.query.filter_by(author=current_user).paginate(page=page, per_page=per_page, error_out=False)

    else:
        notes = Note.query.paginate(page=page, per_page=5)
    return render_template('home.html', notes=notes)

@main.route("/about")
def about():
  return render_template('about.html', title='About')
