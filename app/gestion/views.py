from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from ..usuarios.models import User 
from .models import Procesos, Soporte
from app import db

gestion = Blueprint('gestion', __name__)

@gestion.route("/")
def home():
    return render_template("home.html")

@gestion.route('/crud')
def home2():
    if current_user.is_authenticated:
        return redirect(url_for('usuarios.perfiles'))
    else:
        return redirect(url_for('usuarios.login'))


# DICIPLINA DE PROCESOS

@gestion.route("/procesos")
def procesos():
    diciplinas = Procesos.query.all()
    add = url_for('gestion.procesos_add')
    update = url_for('gestion.procesos_update')
    delete = url_for('gestion.procesos_delete')
    return render_template('procesos.html', diciplinas = diciplinas, add = add, update = update, delete = delete)

@gestion.route("/procesos/add", methods=['POST', "GET"])
def procesos_add():
    if request.method == "POST":
        name = request.form.get("name")
        p = Procesos(name=name)
        db.session.add(p)
        db.session.commit()
        flash("Proceso agregado.","success")
        return redirect(url_for('gestion.procesos'))
    return render_template('procesos_add.html')

@gestion.route("/procesos/update", methods=['POST'])
def procesos_update():
    if request.method == "POST":
        pk = request.form.get('id')
        name = request.form.get("name")
        p = Procesos.query.get(pk)
        p.name = name
        db.session.commit()
        flash("Proceso Modificado.","success")
    return redirect(url_for('gestion.procesos'))


@gestion.route("/procesos/delete", methods=['POST'])
def procesos_delete():
    pk = request.form.get("id")
    proceso = Procesos.query.get(pk)
    db.session.delete(proceso)
    db.session.commit()
    flash("Proceso Modificado.","success")
    return redirect(url_for("gestion.procesos"))


# DICIPLINAS DE SOPORTE

@gestion.route("/soporte")
def soporte():
    diciplinas = Soporte.query.all()
    add = url_for('gestion.soporte_add')
    update = url_for('gestion.soporte_update')
    delete = url_for('gestion.soporte_delete')
    return render_template('procesos.html', diciplinas = diciplinas, add = add, update = update, delete = delete)

@gestion.route("/soporte/add", methods=['POST', 'GET'])
def soporte_add():
    if request.method == "POST":
        name = request.form.get("name")
        p = Soporte(name=name)
        db.session.add(p)
        db.session.commit()
        flash("Proceso agregado.","success")
        return redirect(url_for('gestion.soporte'))
    return render_template('procesos_add.html')

@gestion.route("/soporte/update", methods=['POST'])
def soporte_update():
    if request.method == "POST":
        pk = request.form.get('id')
        name = request.form.get("name")
        p = Soporte.query.get(pk)
        p.name = name
        db.session.commit()
        flash("Proceso agregado.","success")
    return redirect(url_for('gestion.soporte'))

@gestion.route("/soporte/delete", methods=['POST'])
def soporte_delete():
    pk = request.form.get("id")
    soporte = Soporte.query.get(pk)
    db.session.delete(soporte)
    db.session.commit()
    return redirect(url_for("gestion.soporte"))