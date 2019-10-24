# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    def is_admin(self):
        return self.admin

    def __repr__(self):
        return f"User('{self.id}' ,'{self.username}', '{self.email}')"