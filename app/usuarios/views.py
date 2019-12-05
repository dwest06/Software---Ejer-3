from flask import Blueprint, render_template, request, url_for,redirect,flash
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
# from werkzeug import check_password_hash, generate_password_hashd
from app import db
from .models import User
from app.gestion.models import Grupos_Procesos, Portafolio

usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# VIEWS

@login_required
@usuarios.route('/perfiles', methods=['GET'])
def perfiles():
    if request.method == "GET":
        users = User.query.all()
        proyectos = Portafolio.query.all()
    return render_template('perfiles_usuarios.html', users = users, cargos= User.PERMISOS, proyectos = proyectos, groups = Grupos_Procesos.query.all() )    

@login_required
@usuarios.route('/update',methods=["POST"])
def update():
    if request.method == "POST":
        pk = request.form.get("id")
        newusername = request.form.get("newusername")
        newemail = request.form.get("newemail")
        cargo = request.form.get("cargo")
        proyecto = Portafolio.query.get(request.form.get('proyecto'))
        user = User.query.get(pk)

        user.username = newusername
        user.email = newemail
        user.permiso = int(cargo)
        if proyecto != "":
            user.portafolio.append(proyecto)

        db.session.commit()
        return redirect(url_for("gestion.home2"))

@login_required
@usuarios.route('/delete',methods=["POST"])
def delete():
    pk = request.form.get("id")
    user = User.query.get(pk)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("gestion.home2"))


# Register form
@usuarios.route("/register", methods=["GET","POST"])
@login_required
def register():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        proyecto = Portafolio.query.get(request.form.get('proyecto'))
        if password == confirm:
            # Creamos el user
            user = User(username = username, email = email, password = password, permiso=3)

            if proyecto != "":
                user.portafolio.append(proyecto)

            # Guardamos en la db
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("gestion.home2"))
        else:
            flash("password does not match","error")
            return render_template("register.html")
    else:
        if current_user.is_admin():
            proyectos = Portafolio.query.all()
            return render_template("register.html", proyectos = proyectos )
        else:
            flash("Acceso no permitido", "error")
            return redirect(url_for("gestion.home2"))

# Login 
@usuarios.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user is not None:
            if user.password == password:
                login_user(user)
                return redirect(url_for("gestion.home2"))
        
            # flash("Credenciales Invalidas", "error")
        else:
            flash("Usuario no encontrado", "error")

    return render_template("login.html")

@usuarios.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("gestion.home2"))
