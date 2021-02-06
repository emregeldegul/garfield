from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()], render_kw={'placeholder': 'Enter The Word'})
    submit = SubmitField('Search')

