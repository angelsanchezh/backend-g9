from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from Models.usuarios import  UsuarioModel

class UsuarioRequestDto(SQLAlchemyAutoSchema):

    class Meta:


        model = UsuarioModel

