#calcular el puntaje de credito
#debe de calcular que tanto credito tiene una persona en cierta entidad financiera, debera considerar cantidad de ingresos, nivel educacional y nacionalidad
#cantidad de ingresos
#500.000 a 1.000.000 : 300.000
# 1.000.000 a 1.500.000: 650.000
# 1.500.001 o mas: 1.000.000
# nivel educacional
# Basico: x1, medio: x1.3, superior: x1.5
# Nacionalidad
# Chilena: +300.000, extranjero: +0


creditos=0


print(" Elija su monto")
print(" 1.- 500.000 - 1.000.000"
" 2.- 1.000.001 - 1.500.000 " " 3.- 1.500.001 - más" )
 
op=int(input())
if op==1:
    creditos+=300000
elif op==2:
    creditos+=650000
elif op==3:
    creditos+=1000000
else:
    print("opcion no valida")

print(f"su monto actual es {creditos}")

print("ingrese su nivel de educación")
print(" 1.- Basica"
" 2.- Media " " 3.- Superior" )

op=int(input())
if op==1:
    creditos*=1
elif op==2:
    creditos*=1.3
elif op==3:
    creditos*=1.5
else:
    print("seleccione opcion valida")

print(f"Su monto de creditos actual es {creditos}")

print("Ingrese su nacionalidad")

op=int(input())
if op==1:
    creditos+=300000
elif op==2:
    creditos+=0
else:
    print("seleccione opcion valida")

print(f"su monto de creditos es {creditos}")
# print(f"su monto es ", creditos)

# int(input())

# ''' desayuno '''
# import time


# pan=250 



# while pan!=0:
#     print("ñam le queda", pan, "grs de pan")
#     pan-=50
#     time.sleep(2)

# import time


# chocolate=True
# chocolate=250

# if chocolate != 0:
#     print("Puedo comprar")
# else:
#     print("No puede comprar")

# while chocolate!= 0:
#     print("Chocolate rico queda", chocolate, "gramos de este chocolate")
#     chocolate-=50
#     time.sleep(4)

# if chocolate==0:
#    print("Tengo diabetes D:")

#pida al usuario 2 digitos verificando que el segundo sea mayor
#genere un numero aleatorio entre esos digitos
# e imprima la cantidad de veces el simbolo ▄ (alt+220(pad numerico de la derecha)

# import random

# from random import randint

# print("Hola, ingrese 2 numeros, que el 2do numero/digito sea mayor por favor")

# digit1=int(input("Ingrese digito 1"))
# digit2=int(input("Ingrese digito 2")) 

# while digit1>digit2:
#     print("invalido, razón: El segundo digito tiene que ser mayor al primer digito")
#     digit2=int(input("Digito 2 por favor"))

# digit=randint(digit1, digit2)
# print("▄"*digit)

# print("Ingrese 2 digitos")

# d1=int(input("Numero 1: "))
# d2=int(input("Numero 2: "))

# while