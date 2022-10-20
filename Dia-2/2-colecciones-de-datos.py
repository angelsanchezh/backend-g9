# lista de colleciones de datos  ordenadas y modificables

from locale import normalize


nombre =['angel','carmen','sofia','adolfo','henry','felipe']

#en python sus lista pueden tener diferentes tipos de datos 
miscelaneo =['jueves', 13 ,'soleado','false ', [1,2,3]]
#podemos acceder a su contenido mediante las posisicones

print(nombre[0])

#longitud > cantida de elemento que hay en esa coleccion
#psosicion > ubiacion de un elemento que siempre empieza ne cero
#len () > devuelve el numero de items de un contendedor, puede ser un string ( y retornara los numero de caracteres)
#o una coleccion de datos y retornara los items
print(len(nombre))

longitud = len(nombre)
print(nombre[longitud-1])

#de frente para obtner la ultima posicion de la lista 
print(nombre[-1])
print(nombre[-2])

# desde la psosicion 1 hasta menor que 4

print(nombre[1:4])

#desde la posicion 1 hasta el final 
print(nombre[1:])

#desde el inicion hatsa menor de 5 
print(nombre[:5])

#copiar el contenido de un arrelo (colocandolo en ootra posicion de memoria)
print(nombre[:])
print(id(nombre))
alumnos_lima = nombre
print(id(alumnos_lima))
# SI CAMBAIMOS EL CONTENIDO DE UAN POSCION DE MEMMORIA AGREGAMOS O ELIMINAMOS EL CONTENIOD SE VERA REFLEJADO , TANTO EN VARIANBLE ORIGINAL COMO EN VARIABEL HUESPED
nombre[0] = 'felix'
# SI CAMBIAMOS EL CONTENIDO DE LA VARIABLE , AHI SI LA VARIABLE HUSPEDE ALUMNOS LIMA , AHI SI CAMBIARA SU UBIACION EN LA MEMORIA 
print([1,2,3]+[4,5,6])
nombre = 'HOLA MUNDO'
print(alumnos_lima)




#en base a la concatenacion y a la subbusqueda de arreglos como podria mostrar sin sofia (2)
nombre = ['angel','carmen', 'sofia','adolfo','henry','felipe']

#mostrar solo a angel y carmen , luego mostrar a adolfo , henry y felipe y luego concatera la dos lista

print(nombre[:2]+ nombre[3:])

#AGREGAR un nuevo eemento a la lista 
nombre.append('juan pablo')

print(nombre)

# metodos para eliminar un elemento segun el indice
alumno_eliminado =  nombre.pop(0)
print(alumno_eliminado)
print(nombre)

# remove (valor) > si no existe el valor emitira un error, si si exite , lo eliminara no devuelve nada 

alumno_eliminado_2=nombre.remove('adolfo')
print(nombre)
print(alumno_eliminado_2)

#del elimina la posciion (muy parecido al pop pero o develve nada )
del nombre[0]
print(nombre)

#limpia por completo al lista 

nombre.clear()
print(nombre)

#tuplas, las tuplas son inmutables 

# Tuplas
# son ordenadas PERO no se pueden modificar (una vez definidas no se puede alterar)

cursos = ('backend', 'frontend')
mix = (1, 80.2, False, 'Eduardo', (1,2,3))

print(cursos[0])

print(cursos[:1])
# ni agregar
# cursos.append('design')

# ni editar
# cursos[0] = 'mobile'

# ni eliminar
# del cursos[0]

print(cursos)
print(len(cursos))


# Para mas informacion: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences



#Conjunto set 
#coleccion de datos desorndenada , una vez creada ya no se puede acceder mediante sus posiciones

primos= {1,3,5,7,11,13,17,19}
estaciones={'verano','otono','primaver','invierno'}
print(primos)
print(estaciones)
#print(primos[0]) no lo va a reconocer

# se puede agregar 

primos.add(23)
print(primos)

#sepuede eliminar 
primos.pop()
print(primos)
#------------------------
#Dicicionario
#coleccion ordenada pero se usa con llaves (no por indice ) y editable , actua algo asi como un json ( key. value)

persona={
'nombre':'eduardo',
'apellido':'suarez',
'correo':'angelsanchezh@gmail.com',
'telefono':'946589821'
}

print(persona['nombre'])
print(persona.get('direccion','no hay'))

#devuelve una lista con todas las llaves
print(persona.keys())

#devuelve una lista con todos los valores

print(persona.values())


persona['nombre']='luis'

persona['direccion']='calle los ruisenores 1070a'
#persona.get (direccion) = agrega calle los rusisenores 
print(persona)

#remueve el valro de esa llave  y opcionalemte lo puede almacenar en otra  varible  
correo_eliminado=persona.pop('correo')
print(persona)
print(correo_eliminado)



