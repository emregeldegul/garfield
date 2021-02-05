from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from app import db
from app.models.user import User
from app.forms.auth import LoginForm, RegisterForm

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/')
@auth.route('/index')
def index():
    return 'ok'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login Failed', 'danger')
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main.index'))

    return render_template('views/auth/login.html', title='User Login', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(email=form.email.data, first_name=form.first_name.data, last_name=form.last_name.data)
        user.generate_password_hash(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Registered Successfully, Please Login', 'success')

    return render_template('views/auth/register.html', title='User Register', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('Logout Successfully', 'success')
    return redirect(url_for('auth.login'))
