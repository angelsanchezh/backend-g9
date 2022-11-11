from flask import Flask
from config import conexion
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_restful import Api

from Models.usuarios import UsuarioModel
from Models.tareas import TareaModel
from Controllers.usuarioController import UsuariosController

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

#inicializamos la instancia de flask-sqlalqchemy con las propiedades seteadas en la apliacaion de flask

api = Api(app)

conexion.init_app(app)

#inicializamos la clase migrate con la confirguracion de nuetsra base de datos y aplicaion flask 

migrate = Migrate(app,conexion)


api.add_resource(UsuariosController,'/usuarios')
if __name__ == '__main__':

    app.run(debug=True)