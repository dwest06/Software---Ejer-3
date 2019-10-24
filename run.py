# from flask import Flask
# from .usuarios.views import usuarios

# app = Flask(__name__)
# app.register_blueprint(usuarios, url_prefix='/usuarios')

from app import app
app.run(host='0.0.0.0', port=8000, debug=True)