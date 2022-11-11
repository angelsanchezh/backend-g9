from flask_restful import Resource,request
from marshmallow.exceptions import ValidationError
from Dtos.prueba  import PruebaDto 


class PruebaController(Resource):
    def post(self):

        try:
            data = request.get_json()
            validador=  PruebaDto()

            dataValidada=validador.load(data)
            print(dataValidada)        
            return{
                'message':'ok'

            }

        except ValidationError as error:

            return{

                'message':'error al hacer consulta',
                'content': error.args
               }