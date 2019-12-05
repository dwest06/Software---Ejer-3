# Import flask and template operators
from flask import Flask, render_template, url_for,redirect

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Login
from flask_login import LoginManager, current_user
# Admin
from flask_admin import AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView



# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.usuarios.views import usuarios as usuarios_module
from app.usuarios.models import User
from app.gestion.views import gestion as gestion_module
from app.gestion.models import (Grupos_Procesos, Procesos, Soporte, 
    Soporte_G, Habilitadora, Tecnicas, Herramientas, Actores, Portafolio)
# Register blueprint(s)
app.register_blueprint(usuarios_module)
app.register_blueprint(gestion_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

# LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# ADMIN

class CustomAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self):
        return redirect(url_for("login"))


admin = Admin(app, index_view=CustomAdminView())
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Grupos_Procesos, db.session))
admin.add_view(ModelView(Procesos, db.session))
admin.add_view(ModelView(Soporte, db.session))
admin.add_view(ModelView(Soporte_G, db.session))
admin.add_view(ModelView(Habilitadora, db.session))
admin.add_view(ModelView(Tecnicas,db.session))
admin.add_view(ModelView(Herramientas,db.session))
admin.add_view(ModelView(Actores,db.session))
admin.add_view(ModelView(Portafolio,db.session))

try:
    u = User.query.filter_by(username='admin').first()
    u.username
    print('Ya existente', u)
except:
    u = User(username='admin', email='admin@admin.com', password='da123456', permiso=1)
    db.session.add(u)
    db.session.commit()
    print('Creado')