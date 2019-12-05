from app import db
class Procesos(db.Model):
    __tablename__ = 'procesos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Proceso ' + str(self.id) + ' ' + self.name +'>'

class Soporte(db.Model):
    __tablename__ = 'soporte'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __rep__(self):
        return '<Soporte ' + str(self.id) + ' ' + self.name +'>'

class Grupos_Procesos(db.Model):
    __tablename__ = 'grupos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Grupo de proceso ' + str(self.id) + ' ' + self.name +'>'

class Habilitadora(db.Model):
    __tablename__ = 'habilitadora'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=True)

    # ForeingKey to Grupos
    grupos_id = db.Column(db.Integer, db.ForeignKey('grupos.id'), nullable=False)
    grupos = db.relationship("Grupos_Procesos", backref=db.backref("Habilitadora", lazy=True))

    # ForeingKey to Procesos
    procesos_id = db.Column(db.Integer, db.ForeignKey('procesos.id'), nullable=False)
    procesos = db.relationship("Procesos", backref=db.backref("Habilitadora", lazy=True))

    def __repr__(self):
        return "<Grupo Habilitador " + str(self.id)

class ActividadesH(db.Model):
    __tablename__ = 'actividadesh'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=True)

    # ForeingKey to Habilitadoras
    habilitadora_id = db.Column(db.Integer, db.ForeignKey('habilitadora.id'), nullable=False)
    habilitadora = db.relationship("Habilitadora", backref=db.backref("actividades", lazy=True))

class TareasH(db.Model):
    __tablename__ = 'tareash'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=True)

    # ForeingKey to Habilitadoras
    actividadesh_id = db.Column(db.Integer, db.ForeignKey('actividadesh.id'), nullable=False)
    actividadesh = db.relationship("ActividadesH", backref=db.backref("tareas", lazy=True))


class Soporte_G(db.Model):
    __tablename__ = 'soporte_g'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=True)

    # ForeingKey to Grupos
    grupos_id = db.Column(db.Integer, db.ForeignKey('grupos.id'), nullable=False)
    grupos = db.relationship("Grupos_Procesos", backref=db.backref("Soporte_G", lazy=True))

    # ForeingKey to Soporte
    soporte_id = db.Column(db.Integer, db.ForeignKey('soporte.id'), nullable=False)
    soporte = db.relationship("Soporte", backref=db.backref("Soporte_G", lazy=True))

    def __repr__(self):
        return "<Grupo Habilitador " + str(self.id)

class ActividadesS(db.Model):
    __tablename__ = 'actividadess'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=True)

    # ForeingKey to Soporte_G
    soporte_g_id = db.Column(db.Integer, db.ForeignKey('soporte_g.id'), nullable=False)
    soporte_g = db.relationship("Soporte_G", backref=db.backref("actividades", lazy=True))

class TareasS(db.Model):
    __tablename__ = 'tareass'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=True)

    # ForeingKey to ActividadesS
    actividadess_id = db.Column(db.Integer, db.ForeignKey('actividadess.id'), nullable=False)
    actividadess = db.relationship("ActividadesS", backref=db.backref("tareas", lazy=True))

class Tecnicas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(100), nullable=False)

    def __rep__(self):
        return '<Tecnica ' + str(self.id) + ' ' + self.desc +'>'

class Herramientas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(100), nullable=False)

    def __rep__(self):
        return '<Herramienta ' + str(self.id) + ' ' + self.desc +'>'

class Actores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(100), nullable=False)
    
    def __rep__(self):
        return '<Actor ' + str(self.id) + ' ' + self.fname + ' ' + self.lname + '>'

class Portafolio(db.Model):
    __tablename__ = 'portafolio'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)

    def __rep__(self):
        return '<Proyecto ' + str(self.id) + ' ' + self.desc +'>'
