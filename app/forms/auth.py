from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models.user import User


class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Password Confirm', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Register')

    @staticmethod
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('User is available.')

        return True
