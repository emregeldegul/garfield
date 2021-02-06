from flask import Blueprint, render_template
from flask_login import login_required

from app import db
from app.models.word import Word

word = Blueprint('word', __name__, url_prefix='/word')


@word.route('/')
@word.route('/index')
@login_required
def index():
    return render_template('views/word/index.html', title='Search Word')