# for i in range(1,11):
#  print("repeticion numero", i)

# num=int(input("ingrese un numero"))
# for i in range (1,11):
#     print(num, "x",i, "=", num*i)

# for i in range(10,0,-1):
#     print(i )

# pida al usuario 3 notas y saque promedio
# uso de for obligatorio


# cant=int(input("ingrese la cantidad de notas "))

# suma=0
# for i in range (cant): 
#     n1=int(input("ingrese la nota "))
#     suma=suma+n1
# prom=suma/cant
# print("el promedio es", round(prom))

# cant=int(input("ingrese la cantidad de numeros "))
# suma=0
# for i in range (cant):
#     n1=int(input("ingrese numeros "))
#     suma+=n1
# print("la suma de todos los numeros es ", suma)

# Sistema de votos

# c1="hola"
# c2="adios"

# cantvotos1=0
# cantvotos2=0

# cantV=int(input("ingrese la cant de votantes :"))

# for i in range (cantV):
#     # print("por quien votara: 1.- "(c1), 2.-"(c2)")
#     print(f"porquien votara: 1.- {c1}, 2.- {c2}")
#     voto=input()
    
#     if voto=="1":
#         print (f"usted voto por{c1}")
#         cantvotos1+=1
#     else:
#         print(f"usted voto por {c2}")
#         cantvotos2+=1

# print(f"La cantidad de votos de {c1} es {cantvotos1}")
# print(f"La cantidad de votos de {c2} es {cantvotos2}")

# if cantvotos1>cantvotos2:
#     print(f"gano {c1}")
# elif cantvotos2>cantvotos1:
#     print(f"gano {c2}")
# else:
#     print ("votacion empatada")

# print("ingrese la cant de notas")
# suma=0
# cantN=int(input())

# for i in range (cantN):
#     print("ingrese la nota ",i +1)
#     nota=float(input())
#     # suma+=nota
#     suma=suma+nota
# prom=suma/cantN
# print("Su promedio es ", prom)

# if prom>=40 :
#     print("aprobado")
# else:
#     print("reprobado")

# print("ingrese notas")
# suma=0
# notas_azules=0
# cantN=int(input())
# for i in range (cantN):
#     print("ingrese la nota",i +1)
#     nota=float(input()) 
#     if nota>

# nombre=input("ingrese su nombre")

# for i in nombre:
#     print(i)

# pida al usuario una frase y cuente los caracteres

# letra=input("ingrese una frase")
# totalletra=0

# for i in letra:
#     print(i)
#     totalletra+=1
# print("el numero de letras de la frase es", totalletra)

# solucion con la funcion len()
# cont=len(letra)

# print (f"la cantidad de caracteres es {cont}")

# de pseint a python 

# cant=int(input("Cuantos productos llevará?"))
# total=0
# for i in range(cant):



# frase=input("Ingrese una frase ")
# cantcar=0
# v=0
# cons=0
# e=0
# for i in frase:
#     print(i)
#     cantcar+=1
#     if i.lower() in "aeiouáéíóú":
#         v+=1
#         # v=v+1
#     elif i==1:
#         e+=1
#         # e=e+1
#     else:
#         cons+=1
#         # cons=cons+1
# print(f"el total de caracteres es {cantcar}")
# print(f"el total de vocales es {v}")
# print(f"el total de consonantes es {cons}")
# print(f"el total de espacios es {e}")