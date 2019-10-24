from flask import Blueprint, render_template, request, url_for,redirect,flash
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
# from werkzeug import check_password_hash, generate_password_hashd
from app import db
from .models import User

usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# VIEWS

@usuarios.route('/create-user', methods=['POST'])
def create():
    new_user = User(
        username=request.form['username'], 
        email=request.form['email'], 
        password=request.form['password'], 
        admin=False)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home2'))    

@usuarios.route('/update',methods=["POST"])
def update():
    newusername = request.form.get("newusername")
    oldusername = request.form.get("oldusername")
    newemail = request.form.get("newemail")
    user = User.query.filter_by(username=oldusername).first()
    user.username = newusername
    user.email = newemail
    db.session.commit()
    return redirect(url_for('home2'))

@usuarios.route('/delete',methods=["POST"])
def delete():
    username = request.form.get("username")
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home2'))


# Register form
@usuarios.route("/register", methods=["GET","POST"])
@login_required
def register():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        #secure_password = sha256_crypt.encrypt(str(password)) # Encriptar
        print(email, username, password, confirm)
        print("--------------------------")

        if password == confirm:
            # Creamos el user
            user = User(username = username, email = email, password = password)

            # Guardamos en la db
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash("password does not match","error")
            return render_template("register.html")
    else:
        if current_user.is_admin():
            return render_template("register.html")
        else:
            flash("Acceso no permitido", "error")
            return redirect(".home")

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
                return render_template("home.html")
        
            # flash("Credenciales Invalidas", "error")
        else:
            flash("Usuario no encontrado", "error")

    return render_template("login.html")

@usuarios.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
