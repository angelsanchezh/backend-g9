def prueba(**argumentos):

    print(argumentos)

prueba(nombre='angel',apellido ='de rivero')

persona = {

    'nombre':'angel',
    'apellido':'sanchez'
}

prueba (persona=persona)

prueba(**persona)

prueba(nombre=persona['nombre'],apellido=persona['apellido'])