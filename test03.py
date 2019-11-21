import unittest
import os

#from flask_testing import TestCase
#from flask import abort, url_for
#import app.db
from app import app
from flask_testing import TestCase
from app.usuarios.models import User
from app.gestion.models import Procesos, Soporte
from config import *
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
 
    def test_register(self):
        return self.app.post(
            '/usuarios/register',
            #data=dict(username=username, email=email, password=password, permiso=confirm),
            follow_redirects=True
        )
    
    def test_login(self):
        return self.app.post(
            '/usuarios/login',
            #data=dict(username=username, password=password),
            follow_redirects=True
        )
    
    def test_logout(self):
        return self.app.get(
            '/usuarios/login',
            follow_redirects=True)
    
    def test_procesos(self):
        return self.app.get(
            '/procesos',
            follow_redirects=True)

    def test_soporte(self):
        return self.app.get(
            '/soporte',
            follow_redirects=True)

    def test_gruposp(self):
        return self.app.get(
            '/gruposp',
            follow_redirects=True)

    def test_techer(self):
        return self.app.get(
            '/tec-her',
            follow_redirects=True)
    
    def test_actores(self):
        return self.app.get(
            '/actores',
            follow_redirects=True)
    
    def test_perfiles(self):
        return self.app.get(
            '/perfiles',
            follow_redirects=True)
 
    ###############
    #### tests ####
    ###############
 
    def test_main_page(self):
        response = self.test_register()
        response = self.app.get('/usuarios/register', follow_redirects=True)

        response = self.test_login()
        response = self.app.get('/usuarios/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.test_logout()
        response = self.app.get('/usuarios/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.test_procesos()
        response = self.app.get('/procesos', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.test_soporte()
        response = self.app.get('/soporte', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.test_gruposp()
        response = self.app.get('test_gruposp', follow_redirects=True)

        response = self.test_techer()
        response = self.app.get('/tec-her', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.test_actores()
        response = self.app.get('/actores', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.test_perfiles() 
        response = self.app.get('/perfiles', follow_redirects=True)
        
        #self.assertIn('Thanks for registering!', response.data)

if __name__ == "__main__":
    unittest.main()