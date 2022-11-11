from flask_restful import Resource,request
from config import conexion
from Models.usuarios import UsuarioModel


class UsuariosController(Resource):

    def get(self):
        usuarios = conexion.session.query(UsuarioModel).all()

        print(usuarios)
        print(usuarios[0].nombre)

        usuariosFinales=[]

        for usuario in usuarios:

            usuarioDicionario ={

                'id':usuario.id,
                'nombre':usuario.nombre,
                'correo':usuario.correo,
                'telefono':usuario.telefono,

             }
            usuariosFinales.append(usuarioDicionario)



        return{ 
            
            "message": "los usuarios son:",
            "content": usuariosFinales
        }

    def post(self):
        body = request.get_json()

        try:

            nuevoUsuario = UsuarioModel()

            nuevoUsuario.correo = body.get('correo')
            nuevoUsuario.nombre = body.get('nombre')
            nuevoUsuario.telefono = body.get('telefono')
            
            
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            
            print(body)
            
            return{ 
                
                "message": " usuario creado exitosamente"
            }
        except Exception as error:
            print(error)
            return{
                "mesage": "error al crear el usuario"
            }
