#operadores aritmeticos

numero1, numero2 =10 , 50

#suma
#nota: solamente se suma si lad so variable son numericas ,si es que son string se haran concatenacion
#y adenas no se puede sumar numero y string 

print(numero1 + numero2)

#resta solamente para numero 
#solamente para numeros 

print(numero1-numero2)
# print('ab' - 'bc')

#multipliacion 
#nota : solo si se usa la multipliacion en un strign , entonces este repetira el numeero de veces entre un string y un numero de veces 

print(numero1 * numero2)
print('hola' * 5)

#division
print(numero1 / numero2)

#modulo 
print(numero1 % numero2)

#cociente 
print (numero1//numero2)

#exponente
# 10^50
print(numero1 ** numero2)

# RAIZ CUADRADA usando exponente
print(numero1 ** 0.5)


# -----------------------------------
# OPERADORES ASIGNACION
# IGUAL asignar un nuevo valor a una variable
numero1 = 100

# INCREMENTO
numero1 += 1 # incrementando el valor del numero1 en una unidad
print(numero1)

# DECREMENTO
numero1 -= 1 # numero1 = numero1 - 1
print(numero1)

# MULTIPLICADOR
numero1 *= 2
print(numero1)

# DIVIDENDO
numero1 /= 5 # numero1 = numero1 / 5


# -------------------------------------
# OPERADORES DE COMPARACION Siempre retornaran un booleano (si es verdadero o si es falso)

# IGUAL QUE
# Nota: en python, a diferencia de JS, no existe el triple igual (comparador de tipos de datos)
print(numero1) # Float
print(numero2) # Int
print(numero1 == numero2)
print(int(40.7))
print(type(numero1) == type(numero2))

# MAYOR | MAYOR O IGUAL
print(10 > 9.58)
print(10 > int('5'))
print(50 >= 30)

# MENOR | MENOR O IGUAL
print(50 < 80)
print(50 <= 50)
print(50 <= 50)
# Nota: siempre va el simbolo de mayor(>) o menor(<) antes del igual, nunca al revez porque sino python entiende que se esta tratando de una asignacion

print (100>= float("40.24"))
