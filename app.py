from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# DATABASE
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.id}' ,'{self.username}', '{self.email}')"


# VIEWS

@app.route("/")
def home():
    return render_template("home.html")

# Register form
@app.route("/register", methods=["GET","POST"])
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

    return render_template("register.html")

# Login 
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        #secure_password = sha256_crypt.encrypt(str(password)) # Encriptar

        user = User.query.filter_by(username=username).first()
        if user is not None:
            return render_template("home.html", user = user)
        
            # flash("Credenciales Invalidas", "error")
        else:
            flash("Usuario no encontrado", "error")

    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)