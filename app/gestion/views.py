from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from ..usuarios.models import User 
from .models import Procesos, Soporte, Grupos_Procesos
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

@login_required
@gestion.route("/procesos")
def procesos():
    disciplinas = Procesos.query.all()
    add = url_for('gestion.procesos_add')
    update = url_for('gestion.procesos_update')
    delete = url_for('gestion.procesos_delete')
    return render_template('generic.html', view = "Disciplina de Procesos", forms = disciplinas, add = add, update = update, delete = delete)

@login_required
@gestion.route("/procesos/add", methods=['POST', "GET"])
def procesos_add():
    if request.method == "POST":
        name = request.form.get("name")
        p = Procesos(name=name)
        db.session.add(p)
        db.session.commit()
        flash("Proceso agregado.","success")
        return redirect(url_for('gestion.procesos'))
    return render_template('generic_add.html', view = "Agregar Disciplina de Procesos")

@login_required
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


@login_required
@gestion.route("/procesos/delete", methods=['POST'])
def procesos_delete():
    pk = request.form.get("id")
    proceso = Procesos.query.get(pk)
    db.session.delete(proceso)
    db.session.commit()
    flash("Proceso Modificado.","success")
    return redirect(url_for("gestion.procesos"))


# DICIPLINAS DE SOPORTE

@login_required
@gestion.route("/soporte")
def soporte():
    disciplinas = Soporte.query.all()
    add = url_for('gestion.soporte_add')
    update = url_for('gestion.soporte_update')
    delete = url_for('gestion.soporte_delete')
    return render_template('generic.html', view = "Disciplinas de Soporte", forms = disciplinas, add = add, update = update, delete = delete)

@login_required
@gestion.route("/soporte/add", methods=['POST', 'GET'])
def soporte_add():
    if request.method == "POST":
        name = request.form.get("name")
        p = Soporte(name=name)
        db.session.add(p)
        db.session.commit()
        flash("Proceso agregado.","success")
        return redirect(url_for('gestion.soporte'))
    return render_template('generic_add.html', view = "Agregar Disciplinas de Soporte")

@login_required
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

@login_required
@gestion.route("/soporte/delete", methods=['POST'])
def soporte_delete():
    pk = request.form.get("id")
    soporte = Soporte.query.get(pk)
    db.session.delete(soporte)
    db.session.commit()
    return redirect(url_for("gestion.soporte"))

# GRUPOS DE PROCESOS

@login_required
@gestion.route("/gruposp")
def gruposp():
    grupos = Grupos_Procesos.query.all()
    add = url_for('gestion.gruposp_add')
    update = url_for('gestion.gruposp_update')
    delete = url_for('gestion.gruposp_delete')
    return render_template('generic.html', view = "Grupos de Procesos", forms = grupos, add = add, update = update, delete = delete)

@login_required
@gestion.route("/gruposp/add", methods=['POST', 'GET'])
def gruposp_add():
    if request.method == "POST":
        name = request.form.get("name")
        p = Grupos_Procesos(name=name)
        db.session.add(p)
        db.session.commit()
        flash("Grupo de Proceso agregado.","success")
        return redirect(url_for('gestion.gruposp'))
    return render_template('generic_add.html', view = "Añadir Grupo de Procesos")

@login_required
@gestion.route("/gruposp/update", methods=['POST'])
def gruposp_update():
    if request.method == "POST":
        pk = request.form.get('id')
        name = request.form.get("name")
        p = Grupos_Procesos.query.get(pk)
        p.name = name
        db.session.commit()
        flash("Proceso agregado.","success")
    return redirect(url_for('gestion.gruposp'))

@login_required
@gestion.route("/gruposp/delete", methods=['POST'])
def gruposp_delete():
    if request.method == "POST":
        pk = request.form.get("id")
        gruposp = Grupos_Procesos.query.get(pk)
        db.session.delete(gruposp)
        db.session.commit()
        return redirect(url_for("gestion.gruposp"))
    return redirect(url_for('gestion.gruposp')) 