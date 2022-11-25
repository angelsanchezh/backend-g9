from .models import UsuarioModel,PlatoModel
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):

    def save (self):

        nuevoUsuario = UsuarioModel(**self.validated_data)

        nuevoUsuario.set_password(self.validated_data.get('password'))
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        fields = '__all__'
        model = UsuarioModel

        extra_kwargs = {
            
        'password':{
            'write_only':True
        },
            'id':{
                'read_only':True
            }
        }


class PlatoSerializer(serializers.ModelSerializer):

    class Meta:
        model =  PlatoModel
        fields = '__all__'

        extra_kwargs={
            'disponibilidad': {
                'read_only': True
            }

        }
