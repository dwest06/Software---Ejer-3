import unittest
import os

#from flask_testing import TestCase
#from flask import abort, url_for
#import app.db
from flask_testing import TestCase
from app.usuarios.models import User
from app.gestion.models import Procesos, Soporte
from config import *

TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):

    def create_app(self):

		#pass in test configurations 
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///')
        return app

    def setUp (self):
        db.create_all()
		# create test admin user 
        admin = User(username="admin2",  email='asd@asd.com', password="da123456", permiso=1)

		# create test non_admin user
        #employee = Employee(username="test_user", password="test2016")

		# save user to database
        db.session.add(admin)
        #db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == "__main__":
    unittest.main()