# Funciones definidas por el usuario 

def miFuncion():
    print('Hola Mundo')

def suma(a,b):
    return (a + b)

print(suma(3,5))


#edad = input()  aqui ingresar valor

def comprobarEdad (edad):
    if( edad >= 18):
        return 'eres mayor de edad'   
    else:
        return 'no eres mayor de edad,entonces no puedes ingresar'

#edad=input()
#edad=int(edad)

#print(comprobarEdad(edad))
alumnos = ['eduardo','Pepe','Jose ','Miguel','jULIA','raul']

def buscarNombre():
    if 'eduardo' in alumnos:
        return  True
    return False

#print(buscarNombre())  aqui busca nombre

#ingresar una lista  de nombres(5 nombres) y que una funcion haga la busqueda del ultimo nombre



alumnosdecodigo = []

primer_nombre = input('ingrese el primer nombre')
segundo_nombre = input('ingrese el segundo nombre')
tercer_nombre = input('ingrese el tercero nombre')
cuarto_nombre = input('ingrese el cuartonombre')
quinto_nombre = input('ingrese el quinto nombre')

alumnosdecodigo.append(primer_nombre)
alumnosdecodigo.append(segundo_nombre)
alumnosdecodigo.append(tercer_nombre)
alumnosdecodigo.append(cuarto_nombre)
alumnosdecodigo.append(quinto_nombre)

nombre_a_buscar = input('ingrese el valor a buscar')

def buscarPersona(nombre):
    if nombre in alumnosdecodigo:
        return '{} ha sido  encontrado' .format (nombre)
    
    return f'No pudimos encontra a {nombre}'

# print(buscarPersona(nombre_a_buscar))   aqui buscamos el nombre que se solicita 

alumnosdecodigo = []

todos_los_nombres = input('ingrese el primer nombre')

alumnosdecodigo.append(quinto_nombre)

nombre_a_buscar = input('ingrese el valor a buscar')

def buscarPersona(nombre):
    if nombre in alumnosdecodigo:
        return '{} ha sido  encontrado' .format (nombre)
    
    return f'No pudimos encontra a {nombre}'

#-----------------------------------------------------------------------
todos_lo_nombres = input('Ingrese nombres separados por comas: ')

nombre_a_buscar = input('Ingrese el nombre a buscar: ')

def separarNombres(lista_nombres):
  nombres = lista_nombres.split(',')
  return nombres


def buscarPersona(nombre):
  array_nombres = separarNombres(todos_lo_nombres)

  if nombre in array_nombres:
    return '{} ha sido encontrado {}'.format(nombre, '😃')
  return f'No pudimos encontrar a {nombre} {"😢"}'

print(buscarPersona(nombre_a_buscar))

# el metodo split para dividir con comas una lista de nombres 
# el metodo format es para agregar lo atrapado en una varibale agregarlo a otra variable 
#La función format nos permite incluir en una cadena, texto ordinario y caracteres de formateo, que representan un tipo en particular de datos, tales como entero, cadena o flotante (Beazley, 2009). En el ejemplo siguiente tenemos dos variables de cadena, y una tercera variable que contiene el texto a presentar. Se utilizan los corchetes para marcar dónde queremos insertar las variables, y se utiliza .format para especificar los nombres de las variables que se van a insertar.



