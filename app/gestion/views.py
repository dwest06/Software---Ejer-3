from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from ..usuarios.models import User 
from .models import (Procesos, Soporte, Grupos_Procesos, 
    Tecnicas, Herramientas, Actores, Habilitadora, 
    Soporte_G, Portafolio, ActividadesH, ActividadesS )
from flask_weasyprint import HTML, render_pdf
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

# HABILITADORAS
@login_required
@gestion.route("/gruposp2h")
def gruposp2h():
    grupos = Grupos_Procesos.query.all()
    inicio = Grupos_Procesos.query.filter_by(name='Inicio').first()
    planificacion = Grupos_Procesos.query.filter_by(name='Planificacion').first()
    ejecucion = Grupos_Procesos.query.filter_by(name='Ejecucion').first()
    cym = Grupos_Procesos.query.filter_by(name='Control y monitoreo').first()
    cierre = Grupos_Procesos.query.filter_by(name='Cierre').first()

    return render_template('grupos_procesos_habilitadora.html', view = "Grupos de Procesos", 
        forms = grupos, groups = Grupos_Procesos.query.all(), inicio=inicio, planificacion=planificacion,
        ejecucion = ejecucion, cym = cym, cierre=cierre
        )

@login_required
@gestion.route("/gruposp2/addacth", methods=['POST', 'GET'])
def gruposp2_add_acth():
    if request.method == "POST":
        id = request.form.get("id")
        descripcion = request.form.get("descripcion")
        h = Habilitadora.query.get(id)

        act = ActividadesH(descripcion=descripcion, habilitadora = h)
        db.session.add(act)
        db.session.commit()
    return redirect(url_for('gestion.gruposp2h'))

# SOPORTE
@login_required
@gestion.route("/gruposp2s")
def gruposp2s():
    grupos = Grupos_Procesos.query.all()
    inicio = Grupos_Procesos.query.filter_by(name='Inicio').first()
    planificacion = Grupos_Procesos.query.filter_by(name='Planificacion').first()
    ejecucion = Grupos_Procesos.query.filter_by(name='Ejecucion').first()
    cym = Grupos_Procesos.query.filter_by(name='Control y monitoreo').first()
    cierre = Grupos_Procesos.query.filter_by(name='Cierre').first()

    return render_template('grupos_procesos_soporte.html', view = "Grupos de Procesos", 
        forms = grupos, groups = Grupos_Procesos.query.all(), inicio=inicio, planificacion=planificacion,
        ejecucion = ejecucion, cym = cym, cierre=cierre
        )

@login_required
@gestion.route("/gruposp2/addacts", methods=['POST', 'GET'])
def gruposp2_add_acts():
    if request.method == "POST":
        id = request.form.get("id")
        descripcion = request.form.get("descripcion")
        h = Soporte_G.query.get(id)

        act = ActividadesS(descripcion=descripcion, soporte_g = h)
        db.session.add(act)
        db.session.commit()
    return redirect(url_for('gestion.gruposp2s'))

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
                            delete_her = delete_tools, groups = Grupos_Procesos.query.all())

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
    return render_template('generic_add.html',view="Agregar Tecnicas", groups = Grupos_Procesos.query.all())

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
    return render_template('generic_add.html',view="Agregar Herramientas", groups = Grupos_Procesos.query.all())

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
    return render_template('actores.html', form = actores, 
        add = add, update = update, delete = delete, groups = Grupos_Procesos.query.all())

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
    return render_template('actores_add.html', groups = Grupos_Procesos.query.all())

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


# PORTAFOLIO DE PROYECTOS

@login_required
@gestion.route("/portafolio")
def portafolio():
    portafolio = Portafolio.query.all()
    add = url_for('gestion.portafolio_add')
    update = url_for('gestion.portafolio_update')
    delete = url_for('gestion.portafolio_delete')
    return render_template('portafolio.html', forms = portafolio,
        add = add, update = update, delete = delete, groups = Grupos_Procesos.query.all())

@login_required
@gestion.route("/portafolio/add", methods=['POST', 'GET'])
def portafolio_add():
    if request.method == "POST":
        descripcion = request.form.get('descripcion')
        p = Portafolio(descripcion=descripcion)
        db.session.add(p)
        db.session.commit()
        flash("Proyecto agregado.","success")
        return redirect(url_for('gestion.portafolio'))
    return render_template('portafolio_add.html', groups = Grupos_Procesos.query.all())

@login_required
@gestion.route("/portafolio/update", methods=['POST'])
def portafolio_update():
    if request.method == "POST":
        pk = request.form.get('id')
        descripcion = request.form.get('descripcion')
        p = Portafolio.query.get(pk)
        p.descripcion = descripcion
        db.session.commit()
        flash("Proyecto actualizado","success")
    return redirect(url_for('gestion.portafolio'))

@login_required
@gestion.route("/portafolio/delete", methods=['POST'])
def portafolio_delete():
    if request.method == "POST":
        pk = request.form.get("id")
        actor = Portafolio.query.get(pk)
        db.session.delete(actor)
        db.session.commit()
        flash("Proyecto actualizado","success")
    return redirect(url_for('gestion.portafolio')) 

@login_required
@gestion.route("/portafolio/informe", methods=['POST'])
def informe_portafolio():
    if request.method == "POST":
        portafolio = Portafolio.query.all()
        html = render_template('hello.html', portafolio=portafolio)
        return render_pdf(HTML(string=html))
    return redirect(url_for('gestion.home2'))
