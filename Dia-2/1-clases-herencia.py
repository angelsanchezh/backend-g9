# la herencia sirve para reutilizar una clase previamente definida

class Usuario:
    def __init__(self,nombre,apellido,correo):
        self.nombre =nombre
        self.apellido = apellido
        self.correo = correo

    def mostrar_resumen(self):
        return{

            'nombre':self.nombre,
            'apellido':self.apellido,
            'correo':self.correo

        }

class Alumno(Usuario):
    def __init__(self,nombre,apellido,correo,telefono_emergencia):
        self.telefono_emergencia=telefono_emergencia
        super().__init__(nombre,apellido,correo)

    def saludar (self):
        print('yo soy la clase alumno y el nombre es {}'.format(self.nombre))

    def mostrar_resumen(self):
        #polimorfismo > poli > muchas| morfa | = formas , o mucho significados la forma ne la cual un metodo dependiendo de donde se utilice va a trabajar de una forma u otra.
        resumen=super().mostrar_resumen()
        resumen['telefono_emergencia']=self.telefono_emergencia
        return resumen

usuario01 = Usuario(nombre='Eduardo',apellido='De rivero',correo='ederiveroman@gmail.com')
usuario02 = Usuario('alejandra','perez','aperez@gmail.com')

print(usuario01.mostrar_resumen())

alumno01 = Alumno('juan','martinez','jmartinez@gamil.com','946589821')
alumno01.saludar()
print(alumno01.mostrar_resumen())