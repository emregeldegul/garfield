from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('views/main/index.html', title='Home')


@main.route('/about')
def about():
    return render_template('views/main/about.html', title='About')