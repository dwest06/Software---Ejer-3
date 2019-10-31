# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from flask_login import UserMixin
from flask_validator import (ValidateEmail, ValidateLessThanOrEqual, ValidateGreaterThanOrEqual

class User(db.Model, UserMixin):
    PERMISOS = {
        1 : 'Admin',
        2 : 'Gerente',
        3 : 'Empleado'
    }

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    permiso = db.Column(db.Integer)
    

    def is_admin(self):
        return self.permiso == 1

    def __repr__(self):
        return f"User('{self.id}' ,'{self.username}', '{self.email}')"

    @classmethod
    def __declare_last__(cls):
        ValidateLessThanOrEqual(User.permiso, 3)
        ValidateGreaterThanOrEqual(User.permiso, 1)
        ValidateEmail(User.email, true, true, "El E-mail no es valido. Por favor revisalo.")


# class Permisos(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), unique=True, nullable=False)
#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return '<Permiso ' + self.name + '>'
