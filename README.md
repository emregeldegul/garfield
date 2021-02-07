# Garfield
Personal Dictionary and Word Memorizing APP

## Installation

```bash
~$ git clone https://github.com/emregeldegul/garfield.git && cd garfield
~$ python3 -m virtualenv venv
~$ source venv/bin/activate
~$ pip install -r requirements.txt
~$ flask db upgrade
~$ cp .env.example .env
~$ python setup_db.py
~$ flask run
```

Note One: Please don't forget to edit the .env file.

Note Two: Please check the "screenshots" folder for images.

## Used Technologies

* [flask] - Micro web framework
* [flask-sqlalchemy] - An extension for Flask that adds support for SQLAlchemy to your application.
* [flask-bcrypt] - Flask extension that provides bcrypt hashing utilities for your application.
* [flask-login] - Provides user session management for Flask.
* [flask-migrate] - An extension that handles SQLAlchemy database migrations for Flask applications using Alembic
* [flask-wtf] - Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.
* [bootstrap] -  For fast and responsive front-end design.


[flask]: <http://flask.pocoo.org>
[flask-sqlalchemy]: <https://flask-sqlalchemy.palletsprojects.com/en/2.x>
[flask-bcrypt]: <https://flask-bcrypt.readthedocs.io/en/latest>
[flask-login]: <https://flask-login.readthedocs.io/en/latest>
[flask-wtf]: <https://flask-wtf.readthedocs.io/en/stable>
[flask-Migrate]: <https://flask-migrate.readthedocs.io/en/latest/>
[bootstrap]: <https://getbootstrap.com/>