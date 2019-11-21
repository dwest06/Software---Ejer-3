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

    def __repr__(self):
        return '<Proceso ' + str(self.id) + ' ' + self.name +'>'

class Grupos_Procesos(db.Model):
    __tablename__ = 'grupos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    # habilitadora_id = db.Column(db.Integer, db.ForeignKey('habilitadora.id'), nullable=False)
    # habilitadora = db.relationship("Habilitadora", backref=db.backref("Grupos_Procesos", lazy=True))

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