from random import shuffle
from flask import Blueprint, render_template, flash, session, redirect, url_for, request
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import func

from app import db
from app.models.word import Word
from app.models.quiz import Quiz

quiz = Blueprint('quiz', __name__, url_prefix='/quiz')


@quiz.route('/')
@quiz.route('/index')
@login_required
def index():
    session['quiz_words'] = [word.word for word in current_user.dictionary.order_by(func.random()).limit(10).all()]
    session['quiz_point'] = 0

    exams = Quiz.query.filter_by(user=current_user).order_by(Quiz.created_at.desc()).all()
    session['start'] = False

    if len(session['quiz_words']) > 10:
        session['start'] = True

    return render_template('views/quiz/index.html', title="Quiz", exams=exams)


@quiz.route('/question')
@login_required
def question():
    if len(session['quiz_words']) == 0:
        return redirect(url_for('quiz.finish'))

    if not session['start']:
        flash('Not Enough Words To Start The Exam!', 'danger')
        return redirect(url_for('quiz.index'))

    session['quiz_word'] = session['quiz_words'].pop()
    word = Word.query.filter_by(word=session['quiz_word']).first()
    definition_one = word.definitions[0]
    definition_two = Word.query.filter(Word.word != word.word).order_by(func.random()).limit(1).first()
    definition_three = Word.query.filter(Word.word != word.word).filter(Word.word != definition_two.word).order_by(
        func.random()).limit(1).first()
    mix = [definition_three.definitions[0], definition_two.definitions[0], definition_one]

    shuffle(mix)

    return render_template('views/quiz/question.html', title='Question', word=session['quiz_word'], mix=mix)


@quiz.route('/answer', methods=['POST'])
@login_required
def answer():
    word = request.form.get('word')
    wote = request.form.get('wote')

    word = Word.query.filter_by(word=word).first()

    for i in word.definitions:
        if wote == i['definition']:
            session['quiz_point'] += 1
            return 'Success! 1 Point Added'

    session['quiz_point'] -= 2
    return 'Failed! 1 Points Deleted'


@quiz.route('/finish')
@login_required
def finish():
    point = session['quiz_point']

    quiz_model = Quiz()
    quiz_model.point = point
    quiz_model.user = current_user

    db.session.add(quiz_model)
    db.session.commit()

    flash('Quiz Finished! Point: {}'.format(point), 'success')

    session.pop('quiz_point')

    return redirect(url_for('quiz.index'))
