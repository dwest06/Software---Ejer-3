from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required
from flask_admin import AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView
from passlib.hash import sha256_crypt

# CONFIGS
app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# DATABASE
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

# ADMIN

class CustomAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self):
        return redirect(url_for("login"))


admin = Admin(app, index_view=CustomAdminView())
admin.add_view(ModelView(User, db.session))

# VIEWS

@app.route("/")
def home():
    return render_template("home.html")

# Register form
@app.route("/register", methods=["GET","POST"])
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
@app.route("/login", methods=["GET","POST"])
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

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run(debug=True)