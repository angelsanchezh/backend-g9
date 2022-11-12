from flask_restful import Resource,request
from config import conexion
from Models.usuarios import UsuarioModel
from Dtos.usuarioDto import UsuarioRequestDto


class UsuariosController(Resource):

    def get(self):
        usuarios = conexion.session.query(UsuarioModel).all()
        
        serializador = UsuarioRequestDto(many=True)

        data = serializador.dump(usuarios)

        

#        usuariosFinales=[]

 #       for usuario in usuarios:

  #          usuarioDicionario ={

   #             'id':usuario.id,
    #            'nombre':usuario.nombre,
     #           'correo':usuario.correo,
      #          'telefono':usuario.telefono,

       #      }
        #    usuariosFinales.append(usuarioDicionario)



        return{ 
            
            "message": "los usuarios son:",
            "content": data
        }

    def post(self):
        body = request.get_json()

        try:
            serializador = UsuarioRequestDto()
            dataSerializada = serializador.load(body)
            print(dataSerializada)

            nuevoUsuario = UsuarioModel()

            #nuevoUsuario.correo = body.get('correo')
            #nuevoUsuario.nombre = body.get('nombre')
            #nuevoUsuario.telefono = body.get('telefono')
            
            nuevoUsuario = UsuarioModel(**dataSerializada)
            
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            
            print(body)
            
            return{ 
                
                "message": " usuario creado exitosamente"
            }
        except Exception as error:
            print(error)
            return{
                "mesage": "error al crear el usuario",
                'content': error.args
            }


class UsuarioController(Resource):
    def get(self,id):

        usuarioEncontrado= conexion.session.query(UsuarioModel).filter_by(id=id).first()

        serializador = UsuarioRequestDto()
        data = serializador.dump(usuarioEncontrado)
        return{

            'content':data
        }




    def put(self,id):
        try:
            
            usuarioEncontrado= conexion.session.query(UsuarioModel).filter_by(id=id).first()

            if usuarioEncontrado is None:
                raise Exception("usuario no existe")

            body = request.get_json()
            serializador = UsuarioRequestDto()
            data =serializador.load(body)
            
            telefono = usuarioEncontrado.telefono
            try:
                telefono = data['telefono']
            except:
                pass

            usuarioEncontrado.nombre =data.get('nombre')
            usuarioEncontrado.correo =data.get('correo')
            usuarioEncontrado.telefono=data.get('telefono')

            conexion.session.commit()

            return{

                "message":"usuario actualizado exitosamente"
            }

        except Exception as error:
            return{

                "message": "error al actulizar el usuario",
                "content": error.args
            }

    def delete(self,id):
        try:
            usuarioEncontrado= conexion.session.query(UsuarioModel).filter_by(id=id).first()
            if usuarioEncontrado is None:


                raise Exception('Usuario no existe ')
            conexion.session.delete(usuarioEncontrado)
            conexion.session.commit()
            return{

                'message':'el usuario se elimino exitosamente '

            }
        except Exception as error:
            return{

                'message':'error al eliminar usuario',
                'content': error.args
            }
