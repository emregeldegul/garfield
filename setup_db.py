"""
This script will be deleted. The flask-migration will be added.
"""

from app import create_app
from app import db

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

db.session.commit()
