import unittest
import os

#from flask_testing import TestCase
#from flask import abort, url_for
#import app.db
from app import app
from flask_testing import TestCase
from app.usuarios.models import User
from app.gestion.models import Procesos, Soporte
from app import db

TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASE_DIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
    # executed after each test
    def tearDown(self):
        pass

    ########################
    #### helper methods ####
    ########################
 
    def register(self, username, email, password, confirm):
        return self.app.post(
            '/usuarios/register',
            data=dict(username=username, email=email, password=password, permiso=confirm),
            follow_redirects=True
        )
    
    def login(self, username, password):
        return self.app.post(
            '/usuarios/login',
            data=dict(username=username, password=password),
            follow_redirects=True
        )
    
    def logout(self):
        return self.app.get(
            '/usuarios/login',
            follow_redirects=True)
 
 
    ###############
    #### tests ####
    ###############
 
    def test_main_page(self):
        #response = self.register('hola','patkennedy79@gmail.com', 'da123456', 1)
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Thanks for registering!', response.data)

if __name__ == "__main__":
    unittest.main()