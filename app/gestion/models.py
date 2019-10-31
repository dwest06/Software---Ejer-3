from app import db

class Procesos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __rep__(self):
        return '<Proceso ' + str(self.id) + ' ' + self.name +'>'    


class Soporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __rep__(self):
        return '<Proceso ' + str(self.id) + ' ' + self.name +'>'