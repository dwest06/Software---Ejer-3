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

    # buttons
    def test_register_buttons(self):
        return self.app.post(
            '/usuarios/register',
            #data=dict(username=username, email=email, password=password, permiso=confirm),
            follow_redirects=True
        )
    
    def test_login_buttons(self):
        return self.app.post(
            '/usuarios/login',
            #data=dict(username=username, password=password),
            follow_redirects=True
        )
    
    def test_logout_buttons(self):
        return self.app.get(
            '/usuarios/login',
            follow_redirects=True)
    
    def test_procesos_buttons(self):
        return self.app.get(
            '/procesos',
            follow_redirects=True)

    def test_soporte_buttons(self):
        return self.app.get(
            '/soporte',
            follow_redirects=True)

    def test_gruposp_buttons(self):
        return self.app.get(
            '/gruposp',
            follow_redirects=True)

    def test_techer_buttons(self):
        return self.app.get(
            '/tec-her',
            follow_redirects=True)
    
    def test_actores_buttons(self):
        return self.app.get(
            '/actores',
            follow_redirects=True)
    
    def test_perfiles_buttons(self):
        return self.app.get(
            '/perfiles',
            follow_redirects=True)

    # database
    def test_register_database(self):
        return self.app.post(
            '/usuarios/register',
            #data=dict(username=username, email=email, password=password, permiso=confirm),
            follow_redirects=True
        )
    
    def test_login_database(self):
        return self.app.post(
            '/usuarios/login',
            #data=dict(username=username, password=password),
            follow_redirects=True
        )
    
    def test_logout_database(self):
        return self.app.get(
            '/usuarios/login',
            follow_redirects=True)
    
    def test_procesos_database(self):
        return self.app.get(
            '/procesos',
            follow_redirects=True)

    def test_soporte_database(self):
        return self.app.get(
            '/soporte',
            follow_redirects=True)

    def test_gruposp_database(self):
        return self.app.get(
            '/gruposp',
            follow_redirects=True)

    def test_techer_database(self):
        return self.app.get(
            '/tec-her',
            follow_redirects=True)
    
    def test_actores_database(self):
        return self.app.get(
            '/actores',
            follow_redirects=True)
    
    def test_perfiles_database(self):
        return self.app.get(
            '/perfiles',
            follow_redirects=True)

    # add
    def test_register_add(self):
        return self.app.post(
            '/usuarios/register',
            #data=dict(username=username, email=email, password=password, permiso=confirm),
            follow_redirects=True
        )
    
    def test_login_add(self):
        return self.app.post(
            '/usuarios/login',
            #data=dict(username=username, password=password),
            follow_redirects=True
        )
    
    def test_logout_add(self):
        return self.app.get(
            '/usuarios/login',
            follow_redirects=True)
    
    def test_procesos_add(self):
        return self.app.get(
            '/procesos',
            follow_redirects=True)

    def test_soporte_add(self):
        return self.app.get(
            '/soporte',
            follow_redirects=True)

    def test_gruposp_add(self):
        return self.app.get(
            '/gruposp',
            follow_redirects=True)

    def test_techer_add(self):
        return self.app.get(
            '/tec-her',
            follow_redirects=True)
    
    def test_actores_add(self):
        return self.app.get(
            '/actores',
            follow_redirects=True)
    
    def test_perfiles_add(self):
        return self.app.get(
            '/perfiles',
            follow_redirects=True)

    # update
    def test_register_update(self):
        return self.app.post(
            '/usuarios/register',
            #data=dict(username=username, email=email, password=password, permiso=confirm),
            follow_redirects=True
        )
    
    def test_login_update(self):
        return self.app.post(
            '/usuarios/login',
            #data=dict(username=username, password=password),
            follow_redirects=True
        )
    
    def test_logout_update(self):
        return self.app.get(
            '/usuarios/login',
            follow_redirects=True)
    
    def test_procesos_update(self):
        return self.app.get(
            '/procesos',
            follow_redirects=True)

    def test_soporte_update(self):
        return self.app.get(
            '/soporte',
            follow_redirects=True)

    def test_gruposp_update(self):
        return self.app.get(
            '/gruposp',
            follow_redirects=True)

    def test_techer_update(self):
        return self.app.get(
            '/tec-her',
            follow_redirects=True)
    
    def test_actores_update(self):
        return self.app.get(
            '/actores',
            follow_redirects=True)
    
    def test_perfiles_update(self):
        return self.app.get(
            '/perfiles',
            follow_redirects=True)

    # deleted
    def test_register_deleted(self):
        return self.app.post(
            '/usuarios/register',
            #data=dict(username=username, email=email, password=password, permiso=confirm),
            follow_redirects=True
        )
    
    def test_login_deleted(self):
        return self.app.post(
            '/usuarios/login',
            #data=dict(username=username, password=password),
            follow_redirects=True
        )
    
    def test_logout_deleted(self):
        return self.app.get(
            '/usuarios/login',
            follow_redirects=True)
    
    def test_procesos_deleted(self):
        return self.app.get(
            '/procesos',
            follow_redirects=True)

    def test_soporte_deleted(self):
        return self.app.get(
            '/soporte',
            follow_redirects=True)

    def test_gruposp_deleted(self):
        return self.app.get(
            '/gruposp',
            follow_redirects=True)

    def test_techer_deleted(self):
        return self.app.get(
            '/tec-her',
            follow_redirects=True)
    
    def test_actores_deleted(self):
        return self.app.get(
            '/actores',
            follow_redirects=True)
    
    def test_perfiles_deleted(self):
        return self.app.get(
            '/perfiles',
            follow_redirects=True)
 
    # border case
    def test_register_border_case(self):
        return self.app.post(
            '/usuarios/register',
            #data=dict(username=username, email=email, password=password, permiso=confirm),
            follow_redirects=True
        )
    
    def test_login_border_case(self):
        return self.app.post(
            '/usuarios/login',
            #data=dict(username=username, password=password),
            follow_redirects=True
        )
    
    def test_logout_border_case(self):
        return self.app.get(
            '/usuarios/login',
            follow_redirects=True)
    
    def test_procesos_border_case(self):
        return self.app.get(
            '/procesos',
            follow_redirects=True)

    def test_soporte_border_case(self):
        return self.app.get(
            '/soporte',
            follow_redirects=True)

    def test_gruposp_border_case(self):
        return self.app.get(
            '/gruposp',
            follow_redirects=True)

    def test_techer_border_case(self):
        return self.app.get(
            '/tec-her',
            follow_redirects=True)
    
    def test_actores_border_case(self):
        return self.app.get(
            '/actores',
            follow_redirects=True)
    
    def test_perfiles_border_case(self):
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