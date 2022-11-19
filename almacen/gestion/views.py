from rest_framework.decorators import api_view
from  rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializer import PruebaSerializer,DepartamentoSerializer
from rest_framework import status
from .models import DepartamentoModel

# request > es la información que me llega desde el cliente
@api_view(http_method_names=['GET', 'POST'])
def saludar(request:Request):

    #request.data  es el cuerpo (bouyd)  informacion que em envia el cliente


    print(request.data)

    print(request.query_params)
    if request.method == 'GET':

          return Response(data={

            'message':'bienvenido a mi api'
          })

    elif request.method == 'POST':
          body = request .data 
          nombre = body.get('nombre')
          return Response(data={

            'message': f'hola {nombre}'
          })

@api_view(http_method_names=['GET'])
def parametros(request:Request,nombre):
    print(nombre)
    return Response (data={

      'message':'bienvenido al endpoint de parametros'

    }   )


class PruebaApiView(ListCreateAPIView):
      serializer_class=PruebaSerializer
      queryset =[{
        'nombre':'angel',
        'apellidos':'sanchez'
        },{
          'nombre':'julio',
          'apellidos':'perez'

        },{

          'nombre':'juan',
          'apellidos':'rengifo'
        }]

      def post (self, request:Request):
          print (request.data)
          body= request.data
          serializador = PruebaSerializer(data=body)
          dataValida = serializador.is_valid()
          if not  dataValida:
            return Response(data={
              "message": "data incorrecta ",
              "content": serializador.errors


          })

          else:
            print(serializador.validated_data)
            self.queryset.append(serializador.validated_data)
          return Response(data={
            "message":"usuario agregado exitosamente"
          },status= status.HTTP_201_CREATED)

class DepartamentosApiView(ListCreateAPIView):
      serializer_class = DepartamentoSerializer

      queryset = DepartamentoModel.objects.all()


class DepartamentoApiview(RetrieveUpdateDestroyAPIView):
      serializer_class = DepartamentoSerializer

      queryset = DepartamentoModel.objects.all()





      

  