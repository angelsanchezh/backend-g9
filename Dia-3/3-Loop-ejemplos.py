alumnos = [
  {
    "id": 1,
    "nombre": "Eduardo",
    "dni": 76543210,
    "status": True
  },
  {
    "id": 2,
    "nombre": "Jorge",
    "dni": 76543354,
    "status": True
  },
  {
    "id": 3,
    "nombre": "Raul",
    "dni": 76543233,
    "status": True
  },
  {
    "id": 4,
    "nombre": "Miguel",
    "dni": 24543210,
    "status": False
  },
  {
    "id": 5,
    "nombre": "Jose",
    "dni": 76663210,
    "status": False
  }
]

def extraerNombre(lista_alumnos):
    for alumno in lista_alumnos:
        if alumno["status"]==True:
            print(alumno['nombre'])
        else:
            pass

#extraerNombre(alumnos)   aqui extrae los alumnos activos  por que salen true

#-------------------------------------------------

alumnos_activos = []

def obtenerAlumnosAcitvos(lista_alumnos):
    for alumno in lista_alumnos:
        if alumno['status'] == True:
            alumnos_activos.append(alumno)

obtenerAlumnosAcitvos(alumnos)

pass
#print(alumnos_activos) aqui se imprime los que pasaron el filtro

#funcion que cuente las palabras que contengan una frase 

pass

def obtenerpalabras():
    frase = input('ingrese una frase')
    espacios = 1
    for letra in frase:
        if letra == ' ':

            espacios = espacios+1
    return espacios

print(obtenerpalabras())




