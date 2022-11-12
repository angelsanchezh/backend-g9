from flask_restful import Resource,request
from config import conexion
from  Models.tareas import TareaModel
from Models.usuarios import UsuarioModel
from  Dtos.tareasDto import TareaRequestDto

class TareasController(Resource):

    def post (self):
        body = request.get_json()   
        try:
            serializador = TareaRequestDto()
            dataSerializada = serializador.load(body)

            usuarioEncontrado=conexion.session.query(UsuarioModel).filter_by(id=dataSerializada.get ('usuarioId')).first()

            if not usuarioEncontrado:
                raise Exception('Usario no existe')

            nuevaTarea = TareaModel(**dataSerializada)
            conexion.session.add(nuevaTarea)
            conexion.session.commit()

            return{

                'message':"tarea agregada extitosamente"
            }

        except  Exception as error:

            return{

                'message':"erro al cargar la tarea",
                "content": error.args
            }

class TareaController(Resource):
    def get(self,usuarioId):

        TareasEncontradas= conexion.session.query(TareaModel).filter_by(usuarioId=usuarioId).all()
        serializador = TareaRequestDto(many=True)

        data=serializador.dump (TareasEncontradas)

        return{

            'message':'las tareas son',
            'content': data
        }
        


