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

# Definir cant, total, op Como Entero
# 	Escribir "Cuantos productos llevará?"
# 	Leer cant
	
# 	Para i<-1 Hasta cant Con Paso 1 Hacer
# 		Escribir "Que producto llevará?"
# 		Escribir "1.- Diazepam $9000"
# 		Escribir "2.- Metametozona $18500"
# 		Escribir "3.- Oblea China $1000"
# 		Leer op
		
# 		Si op==1 Entonces
# 			Escribir "Usted lleva dIAZEPAM"
# 			total=total+9000
# 		SiNo
# 			Si op==2 Entonces
# 				Escribir "Usted lleva Metametozona"
# 				total=total+18500
# 			SiNo
# 				Si op==3 Entonces
# 					Escribir "Usted lleva Oblea China"
# 					total=total+1000
# 				SiNo
# 					Escribir "Error, selecione una opcion valida (1,2,3)"
# 				Fin Si
# 			Fin Si
# 		Fin Si
		
# 	Fin Para
	
# 	Escribir "EL total neto es ", total
# 	Escribir "EL total mas IVA es ", total*1.19