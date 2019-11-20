from app import db

class Procesos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __rep__(self):
        return '<Proceso ' + str(self.id) + ' ' + self.name +'>'    


class Soporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __rep__(self):
        return '<Soporte ' + str(self.id) + ' ' + self.name +'>'

class Grupos_Procesos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __rep__(self):
        return '<Grupo de proceso ' + str(self.id) + ' ' + self.name +'>'

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
    # Necesito saber qué son los roles
    def __rep__(self):
        return '<Actor ' + str(self.id) + ' ' + self.fname + ' ' + self.lname + '>'