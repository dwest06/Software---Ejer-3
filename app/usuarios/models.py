# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from flask_login import UserMixin
from flask_validator import (ValidateEmail, ValidateLessThanOrEqual, ValidateGreaterThanOrEqual)
from app.gestion.models import Portafolio

portafolio_user = db.Table('portafolio_user',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('portafolio_id', db.Integer, db.ForeignKey('portafolio.id'))
)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    PERMISOS = {
        1 : 'Admin',
        2 : 'Gerente',
        3 : 'Especialista',
        4 : 'Empleado'
    }

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    permiso = db.Column(db.Integer)
    portafolio = db.relationship("Portafolio",
        secondary=portafolio_user, backref=db.backref('user_portafolio', lazy=True))
    

    def is_admin(self):
        return self.permiso == 1

    def is_gerente(self):
        return self.permiso == 2

    def is_especialista(self):
        return self.permiso == 3

    def __repr__(self):
        return f"User('{self.id}' ,'{self.username}', '{self.email}')"

    @classmethod
    def __declare_last__(cls):
        ValidateLessThanOrEqual(User.permiso, 3)
        ValidateGreaterThanOrEqual(User.permiso, 1)
        ValidateEmail(User.email, True, True, "El E-mail no es valido. Por favor revisalo.")

