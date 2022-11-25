from rest_framework.generics import CreateAPIView, ListCreateAPIView,UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioModel,PlatoModel
from .serializers import UsuarioSerializer, PlatoSerializer


# Create your views here.

class RegistroUsuarioApiView(CreateAPIView):

    queryset = UsuarioModel.objetcs.all()
    serializer_class = UsuarioSerializer

    def post(self,request: Request):
        informacion = self.serializer_class(data= request.data)

        es_valida = informacion.is_valid()

        if not es_valida:
            return Response(data={
                'message' : 'error al crear el usuario',
                'content': informacion.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        else:

            nuevoUsuario = informacion.save()
            nuevoUsuarioSerializado = self.serializer_class(instance=nuevoUsuario)

            return Response(data={

                'message': 'ususrio creado exitosamente, ya se puede logear',
                'content': nuevoUsuarioSerializado.data
            },status=status.HTTP_400_BAD_REQUEST)


class PlatosApiView(ListCreateAPIView):

    queryset= PlatoModel.objects.all()
    serializer_class = PlatoSerializer

    def post (self,request:Request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)

        nuevoPlato = data.save()

        return Response (data={
            'message' : 'plato creado exitosamente',
            'content' : self.serializer_class(instance=nuevoPlato).data

        })

    def get(self, request:Request):
            platos = PlatoModel.objects.filter(disponibilidad=True).all()

            platosSerializados =  self.serializer_class(instance=platos,many=True)

            return Response(data={
                'message': 'los platos son',
                'content': platosSerializados.data

            })

class PlatoToggleApiView(UpdateAPIView):
    queryset = PlatoModel.objects.all()

    serializer_class= PlatoSerializer
    def put(self,request:Request,id):

        PlatoEncontrado = PlatoModel.objects.filter(id=id).first()
        if PlatoEncontrado is None :
            return Response (data={
                'message': 'plato encontrado'
            },status=status.HTTP_404_NOT_FOUND)

        PlatoEncontrado.disponibilidad = not PlatoEncontrado.disponibilidad

        PlatoEncontrado.save()

        return Response(data={
            'message' :'plato actualizado exitosamente',
            'content': self.serializer_class(instance=PlatoEncontrado).data
        },status=status.HTTP_201_CREATED ) 

class PlatoUpdateApiView(UpdateAPIView):
    queryset= PlatoModel.objects.all()
    serializer_class=PlatoSerializer








