from flask import Blueprint, render_template, flash, jsonify
from flask_login import login_required, current_user

from app import db
from app.models.word import Word
from app.forms.word import SearchForm
from app.services.api import ApiService

word = Blueprint('word', __name__, url_prefix='/word')


@word.route('/')
@word.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form, model = SearchForm(), False

    if form.validate_on_submit():
        api = ApiService()
        response = api.translate(form.word.data)

        if response['success']:
            model = response['model']
        else:
            flash(response['message'], 'danger')

    return render_template('views/word/index.html', title='Search Word', form=form, model=model)


@word.route('/<int:id>/add')
@login_required
def add_word(id):
    word = Word.query.filter_by(id=id).first_or_404()
    current_user.dictionary.append(word)
    db.session.commit()
    return 'ok'


@word.route('/<int:id>/remove')
@login_required
def remove_word(id):
    word = Word.query.filter_by(id=id).first_or_404()
    current_user.dictionary.remove(word)
    db.session.commit()
    return 'ok'


@word.route('/my_words')
@login_required
def my_words():
    words = current_user.dictionary.all()
    return render_template('views/word/my_words.html', title='My Words', words=words)
