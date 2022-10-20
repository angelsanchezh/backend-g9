# el try va de la mano con el  except no pueden ir separados
#try:

   # print (10/0)   si no hay un error jamas entrara al except
    
 #  print(10/1) 
#except:

  #  print('hubo un error al dividir entre cero')  aqui se corto para que continue funcionando 

#print('yo no soy un error') aqui se corto para que continue funcionando 



try:
    int('a')
except ZeroDivisionError:
    #aca ingresra si el error es de de tipo zerodivison error
    print('hubo error al dividir entre zero ')

except ValueError:
    #aca entrara  si el error es de conversion
    print('error al convertir el numero')

except Exception as error:
    #aca entrara si el error es otro, generico
    #args > es el atributo de toda instancia de exception que em devolvera el porque se dio el error (argumentos )

    print(error.args)
    print('hubo un error al dividr entre cero')
print('yo no soy un error')


try:
        # args son los argumnetos que nosotros indicaremos o recibiremos cunado se da un error , en este atributo se podran obtener los argumentos  del por que se dio el error 
    raise Exception('ere smenor de edad','no eres peruano','no eres femenino')  # es como el Trow error de JAVA SCRIPT 
except Exception as error:
    print(error.args)



try:
    resultado=5/1
    raise Exception('error desconocido')

except Exception as error:
    print(error.args)

else:
    # en el caso  que el codigo se ejecutase sin ningun error(sin ingresar al except) 
    print('la operacion se realizo exitosamente ')

finally:
   
    #ingresa si la ejecucion estuvo bien o si ingresa el except
   
    print('si la operacion estuvo bien o mal , igual se ejecuta')


#ejercicio: 
#recibir por teclado un numero 

numero = input('ingresa un numero')
#Luego tratar de convertir ese  numero a un entero (si no se puede indicar que el valor es incorrecto)
#sumar 10 mas a ese numero ingresado e imprimir resultado.

try:
   numeroEntero= int(numero)

except ValueError:

    print('el valor ingresao es incorecto')
else:
    print(numeroEntero + 10)