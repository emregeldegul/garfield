"""
This script will be deleted. The flask-migration will be added.
"""
from json import loads, dumps
from app import create_app
from app import db

from app.models.word import Word
from app.models.user import User

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

user = User()
user.email = 'user@test.com'
user.first_name = 'Test'
user.last_name = 'User'
user.generate_password_hash("123456789")
db.session.add(user)

definition_one = [
    {
        "definition": "the quantity a flask will hold",
        "partOfSpeech": "noun"
    },
    {
        "definition": "bottle that has a narrow neck",
        "partOfSpeech": "noun"
    }
]

definition_two = [
    {
        "definition": "the quantity contained in a bottle",
        "partOfSpeech": "noun"
    },
    {
        "definition": "a vessel fitted with a flexible teat and filled with milk or formula; used as a substitute for breast feeding infants and very young children",
        "partOfSpeech": "noun"
    },
    {
        "definition": "a glass or plastic vessel used for storing drinks or other liquids; typically cylindrical without handles and with a narrow neck that can be plugged or capped",
        "partOfSpeech": "noun"
    },
    {
        "definition": "put into bottles",
        "partOfSpeech": "verb"
    },
    {
        "definition": "store (liquids or gases) in bottles",
        "partOfSpeech": "verb"
    }
]

word_one = Word()
word_one.word = "flask"
word_one.definitions = definition_one


word_two = Word()
word_two.word = "bottle"
word_two.definitions = definition_two


db.session.add(word_one)
db.session.add(word_two)

db.session.commit()
