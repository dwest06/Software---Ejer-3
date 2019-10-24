from flask import Blueprint, render_template
from ..usuarios.models import User 

gestion = Blueprint('gestion', __name__)

@gestion.route("/")
def home():
    return render_template("home.html")

@gestion.route('/crud')
def home2():
    users = User.query.all()
    return render_template('index.html', users = users)