from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

from passlib.hash import sha256_crypt

# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine('sqlite:///foo.db')
db = scoped_session(sessionmaker(bin=engine))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# Register form
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        secure_password = sha256_crypt.encrypt(str(password)) # Encriptar

        if password == confirm:
            db.execute("INSERT INTO users(name,username,password) VALUES(:name,:username,:password)",
                                    {"name":name,"username":username,"password":secure_password})
            db.commit()
            return redirect(url_for('login'))
        else:
            flash("password does not match","danger")
            return render_template("register.html")

    return render_template("register.html")

# Login 
@app.route("/login")
def login():
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)