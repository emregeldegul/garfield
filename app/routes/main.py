from flask import Blueprint, render_template, jsonify
from flask_login import login_required

from app.services.api import ApiService

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('views/main/index.html', title='Home')


@main.route('/about')
def about():
    return render_template('views/main/about.html', title='About')


@main.route('/test/<string:value>')
def test(value):
    api = ApiService()
    word = api.translate(value)

    if word['success']:
        return jsonify(word['model'].definitions)

    return jsonify(word)
