from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from Models.tareas import TareaModel

class TareaRequestDto(SQLAlchemyAutoSchema):
    class Meta: 

        model=TareaModel

        include_fk =True
