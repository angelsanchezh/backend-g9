
from email import message
from flask import Flask, request
from datetime import datetime
from flask_cors import CORS
# name, solo muestra si es el archivo principal del proyecto
#reuqest es tdoa la informaion que que se puede verl del usuario a traves dl body
#print(__name__)

usuarios=[{

'correo':'angelsanchezh@gmail.com',
'nombre':'angel',
'apellido':'sanchez'

} ,{
'correo':'julioperez@gmail.com',
'nombre':'julio',
'apellido':'perez'

},{
'correo':'juangarcia@gmail.com',
'nombre':'juan',
'apellido':'garcia'

}
]







app=Flask(__name__)

#el metod run sirve para correr nuestro servidor en odo de desarrollo

CORS(app)

# si declaramos algo depues del metodo run ,este nunca se llamara , por que aca se quedara pegado esperando peticiones del cliente
# el endponit , es cuando definimos una ruta para que pueda ser accedidia 
@app.route('/',methods=['GET'])
def inicio():
    #controlador (controller) es la funcionalidad que tendra mi endpoint, es mi primer controlador
    print('ingreso al endpoitn principal')
    #siempre el controladro debe retornar algo
    return 'bienvenido a mi primera api semana 02'

@app.route('/estado',methods=['GET'])
def estado():
    hora_servidor= datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
    return{

        'estado':'True',
        'Hora':hora_servidor
 }

@app.route('/registrarse',methods=['POST'])
def resgitro():
    print(request.data)
    print(request.get_json())
    body= request.get_json()

    for usuario in usuarios:
        print(usuario)
        correo=usuario.get('correo')
        if correo ==body.get('correo'):
            return{

                'message':'el usuario ya esta registrado'
            }

    # request data > el body en formato bytes (puro bytes )
    #el requets json devuelven y transforma la informacion caputarad en formato json para que pueda ser usado pot python
    usuarios.append(body)
    return{
        
        'message':'registrado exitosamente'
    }

@app.route('/listar_usuarios',methods=['GET'])
        
def listar():
        return{
                'content':usuarios
            }

app.run(debug=True)



