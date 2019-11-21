from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from ..usuarios.models import User 
from .models import Procesos, Soporte, Grupos_Procesos, Habilitadora, Soporte_G
from app import db

gestion = Blueprint('gestion', __name__)

@gestion.route("/")
def home():
    return render_template("home.html", groups = Grupos_Procesos.query.all())

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
    return render_template('generic.html', 
        view = "Disciplina de Procesos", forms = disciplinas, add = add, 
        update = update, delete = delete, groups = Grupos_Procesos.query.all())

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
    return render_template('generic_add.html', 
        view = "Agregar Disciplina de Procesos", groups = Grupos_Procesos.query.all())

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
    return render_template('generic.html', view = "Disciplinas de Soporte", 
        forms = disciplinas, add = add, update = update, delete = delete, groups = Grupos_Procesos.query.all())

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
    return render_template('generic_add.html', 
        view = "Agregar Disciplinas de Soporte", groups = Grupos_Procesos.query.all())

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
    return render_template('generic.html', view = "Grupos de Procesos", 
        forms = grupos, add = add, update = update, delete = delete, groups = Grupos_Procesos.query.all())

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
    return render_template('generic_add.html', 
        view = "Añadir Grupo de Procesos", groups = Grupos_Procesos.query.all())

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

# VIEW GENERICA DE CADA GRUPO
@login_required
@gestion.route("/gruposp/<grupo>")
def custom_group(grupo):
    g = Grupos_Procesos.query.get(grupo)
    h = Habilitadora.query.with_parent(g).all()
    sg = Soporte_G.query.with_parent(g).all()
    p = Procesos.query.all()
    s = Soporte.query.all()
    return render_template("custom-group.html", habilitadoras=h, soporte=sg,procesos = p, sop=s, 
        grupo=g, groups = Grupos_Procesos.query.all())

@login_required
@gestion.route("/gruposp/addh/<grupo>", methods=['POST', 'GET'])
def custom_group_add_h(grupo):
    if request.method == "POST":
        g = Grupos_Procesos.query.get(grupo)
        p = request.form.get("disciplina")
        proceso = Procesos.query.get(p)
        des = request.form.get("descripcion")
        h = Habilitadora(descripcion=des, procesos = proceso, grupos = g)
        db.session.add(h)
        db.session.commit()
        return redirect(url_for('gestion.custom_group', grupo=grupo))
    else:
        p = Procesos.query.all()
        g = Grupos_Procesos.query.get(grupo)
        return render_template('custom-group-add.html', disciplinas=p, grupo=g, a="Habilitadora", groups = Grupos_Procesos.query.all())
    

@login_required
@gestion.route("/gruposp/modifyh/<grupo>", methods=["POST"])
def custom_group_modify_h(grupo):
    if request.method == "POST":
        g = Grupos_Procesos.query.get(grupo)
        pk = request.form.get("id")
        h = Habilitadora.query.get(pk)
        p = request.form.get("disciplina")
        proceso = Procesos.query.get(p)
        des = request.form.get("descripcion")
        h.descripcion = des
        h.procesos = proceso
        db.session.commit()
    return redirect(url_for('gestion.custom_group', grupo=grupo))

@login_required
@gestion.route("/gruposp/deleteh/<grupo>", methods=["POST"])
def custom_group_delete_h(grupo):
    if request.method == "POST":
        pk = request.form.get("id")
        h = Habilitadora.query.get(pk)
        db.session.delete(h)
        db.session.commit()
        flash("Disciplina Habilitadora eliminada exitosamente.","success")
    return redirect(url_for('gestion.custom_group', grupo=grupo))

@login_required
@gestion.route("/gruposp/adds/<grupo>", methods=['POST', 'GET'])
def custom_group_add_s(grupo):
    if request.method == "POST":
        g = Grupos_Procesos.query.get(grupo)
        s = request.form.get("disciplina")
        soporte = Soporte.query.get(s)
        des = request.form.get("descripcion")
        h = Soporte_G(descripcion=des, soporte = soporte, grupos = g)
        db.session.add(h)
        db.session.commit()
        return redirect(url_for('gestion.custom_group', grupo=grupo))
    else:
        p = Soporte.query.all()
        g = Grupos_Procesos.query.get(grupo)
        return render_template('custom-group-add.html', disciplinas=p, grupo=g, a="Soporte", groups = Grupos_Procesos.query.all())

@login_required
@gestion.route("/gruposp/modifys/<grupo>", methods=["POST"])
def custom_group_modify_s(grupo):
    if request.method == "POST":
        pk = request.form.get("id")
        h = Soporte_G.query.get(pk)
        p = request.form.get("disciplina")
        soporte = Soporte.query.get(p)
        des = request.form.get("descripcion")
        h.descripcion = des
        h.soporte = soporte
        db.session.commit()
    return redirect(url_for('gestion.custom_group', grupo=grupo))

@login_required
@gestion.route("/gruposp/deletes/<grupo>", methods=["POST"])
def custom_group_delete_s(grupo):
    if request.method == "POST":
        pk = request.form.get("id")
        h = Soporte_G.query.get(pk)
        db.session.delete(h)
        db.session.commit()
        flash("Disciplina de Soporte eliminada exitosamente.","success")
    return redirect(url_for('gestion.custom_group', grupo=grupo))