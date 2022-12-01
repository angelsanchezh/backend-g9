from rest_framework.generics import CreateAPIView, ListCreateAPIView,UpdateAPIView,ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioModel,PlatoModel
from .serializers import UsuarioSerializer, PlatoSerializer
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view

#IsAuthenticated > Solamente verifica que en la peticion este enviando una token valida 
# # IsAuthenticatedOrReadOnly > Solamente para los metodos QUE NO SEAN GET pedira una token valida 
# # IsAdminUser > Verifica que el usuario de la token sea un usuario administrador (is_superuser = True) 
# # AllowAny > Permite el libre acceso a todo el mundo

from rest_framework.permissions import IsAuthenticated

from .permissions import SoloAdmin
from django.db import connection


# Create your views here.

class RegistroUsuarioApiView(CreateAPIView):

    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes =[SoloAdmin]

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
    permission_classes=[IsAuthenticatedOrReadOnly]

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
    permission_classes= [IsAuthenticated]

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
    permission_classes= [IsAuthenticated]


class VistaProtegidaPlatosApiView(ListAPIView):
    queryset=PlatoModel.objects.all()
    serializer_class= PlatoSerializer

    authentication_classes = [JWTAuthentication]

    permission_classes = [SoloAdmin]

    def get(self,request:Request):

        #request.auth > me devolverla lo que se esta utilizando para la autenticacion (la JWT)
        print('el auth es:', request.auth)

        #request.user > una vez que ya comprobo que el usuario existe y la token es correcta, ahora en el request.user se almacenara el usuario que esta utilizando esa token (gracias al parametro 'USER_ID_CLAIM')

        print('eluser es:',request.user)


        return Response(data={
            'message' : 'hola',
            'usuario':{
                    'id':request.user.id,
                    'correo':request.user.correo
            }

        } )

@api_view (http_method_names=['GET'])
def mostrar_usuario_raw(request):
    with connection.cursor()as cursor:

        cursor.execute('CALL DevolverTodosLosUsarios()')
        resultado = cursor.fetchall()
        print(resultado)
        for usuario in resultado:
            print(usuario[3])

        cursor.execute("CALL DevolverUsuarioSegunTipo('ADMIN',@usuarioID)")
        cursor.execute('SELECT @usuarioID')

        resultado2= cursor.fetchone()
        print(resultado2)


        return Response(data={
            'message': 'procedimiento alamacenado exitosamente'
        })






