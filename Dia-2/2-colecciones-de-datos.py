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
