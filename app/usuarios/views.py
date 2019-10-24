from flask import Blueprint, render_template, request, url_for,redirect,flash
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
# from werkzeug import check_password_hash, generate_password_hashd
from app import db
from .models import User

usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# VIEWS

@usuarios.route('/perfiles', methods=['GET'])
def perfiles():
    if request.method == "GET":
        users = User.query.all()
    return render_template('perfiles_usuarios.html', users = users)    

@usuarios.route('/update',methods=["POST"])
def update():
    if request.method == "POST":
        pk = request.form.get("id")
        newusername = request.form.get("newusername")
        newemail = request.form.get("newemail")

        user = User.query.get(pk)

        user.username = newusername
        user.email = newemail

        db.session.commit()
        return redirect(url_for("gestion.home2"))

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

        if password == confirm:
            # Creamos el user
            user = User(username = username, email = email, password = password)

            # Guardamos en la db
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("gestion.home2"))
        else:
            flash("password does not match","error")
            return render_template("register.html")
    else:
        if current_user.is_admin():
            return render_template("register.html")
        else:
            flash("Acceso no permitido", "error")
            return redirect(url_for("gestion.home2"))

# Login 
@usuarios.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        #secure_password = sha256_crypt.encrypt(str(password)) # Encriptar

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
