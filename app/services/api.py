from urllib.parse import quote_plus

from flask import current_app
from requests import request

from app import db
from app.models.word import Word


class ApiService():
    def __init__(self):
        self.url = "https://wordsapiv1.p.rapidapi.com/words/{}/definitions"
        self.headers = {
            'x-rapidapi-key': current_app.config['X_RAPIDAPI_KEY'],
            'x-rapidapi-host': current_app.config['X_RAPIDAPI_HOST']
        }

    def request(self, word):
        last_url = self.url.format(quote_plus(word))
        response = request("GET", last_url, headers=self.headers)

        return response

    def translate(self, value):
        value = value.strip().lower()

        word = Word.query.filter_by(word=value).first()

        if word:
            return {'success': True, 'model': word}

        response = self.request(value)

        if response.status_code != 200:
            return {'success': False, 'message': response.json()['message']}

        word = Word()
        word.word = value
        word.definitions = response.json()['definitions']

        db.session.add(word)
        db.session.commit()

        return {'success': True, 'model': word}

