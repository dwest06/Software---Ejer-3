from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from ..usuarios.models import User 
from .models import Procesos, Soporte, Grupos_Procesos, Tecnicas, Herramientas, Actores
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
    return render_template('generic_add.html', view = "Agregar Grupo de Procesos")

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

# TECNICAS Y HERRAMIENTAS

@login_required
@gestion.route("/tec-her")
def tec_her():
    tecs = Tecnicas.query.all()
    tools = Herramientas.query.all()
    add_tecs = url_for('gestion.tecs_add')
    add_tools  = url_for('gestion.tools_add')
    update_tecs = url_for('gestion.tecs_update')
    update_tools  = url_for('gestion.tools_update')
    delete_tecs = url_for('gestion.tecs_delete')
    delete_tools  = url_for('gestion.tools_delete')
    return render_template('tecs-tools.html', 
                            tecs = tecs, 
                            her = tools, 
                            add_tecs = add_tecs, 
                            add_her = add_tools, 
                            update_tecs = update_tecs,
                            update_her = update_tools,
                            delete_tecs = delete_tecs, 
                            delete_her = delete_tools)

@login_required
@gestion.route("/tec-her/tecs/add", methods=['POST', 'GET'])
def tecs_add():
    if request.method == "POST":
        desc = request.form.get("name")
        p = Tecnicas(desc=desc)
        db.session.add(p)
        db.session.commit()
        flash("T�cnica agregada.","success")
        return redirect(url_for('gestion.tec_her'))
    return render_template('generic_add.html',view="Agregar Tecnicas")


@login_required
@gestion.route("/tec-her/her/add", methods=['POST', 'GET'])
def tools_add():
    if request.method == "POST":
        desc = request.form.get("name")
        p = Herramientas(desc=desc)
        db.session.add(p)
        db.session.commit()
        flash("Herramienta agregada.","success")
        return redirect(url_for('gestion.tec_her'))
    return render_template('generic_add.html',view="Agregar Herramientas")

@login_required
@gestion.route("/tec-her/tecs/update", methods=['POST'])
def tecs_update():
    if request.method == "POST":
        pk = request.form.get('id')
        desc = request.form.get('desc')
        p = Tecnicas.query.get(pk)
        p.desc = desc
        db.session.commit()
        flash("Tecnica actualizada.","success")
    return redirect(url_for('gestion.tec_her'))

@login_required
@gestion.route("/tec-her/hertecs/update", methods=['POST'])
def tools_update():
    if request.method == "POST":
        pk = request.form.get('id')
        desc = request.form.get('desc')
        p = Herramientas.query.get(pk)
        p.desc = desc
        db.session.commit()
        flash("Herramienta actualizada.","success")
    return redirect(url_for('gestion.tec_her'))

@login_required
@gestion.route("/tec-her/tecs/delete", methods=['POST'])
def tecs_delete():
    if request.method == "POST":
        pk = request.form.get("id")
        tecs = Tecnicas.query.get(pk)
        db.session.delete(tecs)
        db.session.commit()
        return redirect(url_for("gestion.tec_her"))
    return redirect(url_for('gestion.tec_her')) 

@login_required
@gestion.route("/tec-her/her/delete", methods=['POST'])
def tools_delete():
    if request.method == "POST":
        pk = request.form.get("id")
        her = Herramientas.query.get(pk)
        db.session.delete(her)
        db.session.commit()
        return redirect(url_for("gestion.tec_her"))
    return redirect(url_for('gestion.tec_her')) 

# ACTORES

@login_required
@gestion.route("/actores")
def actores():
    actores = Actores.query.all()
    add = url_for('gestion.actores_add')
    update = url_for('gestion.actores_update')
    delete = url_for('gestion.actores_delete')
    return render_template('actores.html', form = actores, add = add, update = update, delete = delete)

@login_required
@gestion.route("/actores/add", methods=['POST', 'GET'])
def actores_add():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        roles = request.form.get("rol")
        p = Actores(fname=fname,lname=lname,rol=roles)
        db.session.add(p)
        db.session.commit()
        flash("Actor agregado.","success")
        return redirect(url_for('gestion.actores'))
    return render_template('actores_add.html')

@login_required
@gestion.route("/actores/update", methods=['POST'])
def actores_update():
    if request.method == "POST":
        pk = request.form.get('id')
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        rol = rol.request.form.get("rol")
        p = Actores.query.get(pk)
        p.fname = fname
        p.lname = lname
        p.rol = rol
        db.session.commit()
        flash("Actor actualizado","success")
    return redirect(url_for('gestion.actores'))

@login_required
@gestion.route("/actores/delete", methods=['POST'])
def actores_delete():
    if request.method == "POST":
        pk = request.form.get("id")
        actor = Actores.query.get(pk)
        db.session.delete(actor)
        db.session.commit()
        return redirect(url_for("gestion.actores"))
    return redirect(url_for('gestion.actores')) 
