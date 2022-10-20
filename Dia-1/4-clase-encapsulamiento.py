


class Producto:
    def __init__(self,nombre,precio,cantidad):

        self.nombre = nombre 
        self.precio = precio 
        self.cantidad = cantidad 
#con el atributo __ > estaremos indicando que sera privado y que por ende no puede ser accedido desde fuera de la clase ES PRIVADO

        self.__ventas =[]
#con el atributo _  > PROTEGIDO en python mas que todo funciona para cuando queremos utilizar este atributo como herencia
        self._precio_mayorista=100

    def generar_venta(self,fecha ,cliente,cantidad):
        venta={

            'fecha': fecha,
            'cliente': cliente,
            'cantidad': cantidad,
        }
        self.__ventas.append(venta)

        print('Venta registrada exitosamente')
    
    def mostrar_ventas(self):

        #retornar las ventas registradas de ese producto 
        return self.__ventas




detergente = Producto(nombre='Detergente Sapito',precio=4.50 , cantidad=50)
detergente.nombre = 'detergente lechuga'
print(detergente.nombre)

detergente.generar_venta(fecha='2022-10-19', cliente='Eduardo de Rivero', cantidad=10)
detergente.generar_venta(fecha='2022-10-29', cliente='Julissa Perez', cantidad=30)
detergente.generar_venta(fecha='2022-10-30', cliente='Franco Portugal', cantidad=20)
detergente.generar_venta(fecha='2022-11-02', cliente='Michelle Ordoñez', cantidad=15)
#print(detergente.__ventas)

print(detergente.nombre)