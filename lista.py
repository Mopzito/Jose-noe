# # Uso y explicacion de listas
#    # -6 -5 -4 -3 -2  -1
# lista=[5, 7, 2, 9, 10 ,2]
# #      0  1  2  3  4   5


# print(lista[-6])
# print(lista[0])

# #muestra toda la lista
# print(lista)

# for num in lista:
#     print(num)

# # Hacer una lista de 5 notas
# # luego sacar su promedio
# # Las notas deben ser valores int
# ej: 55, 67, 34

# notas=[50,70,55,45,65]
# c=0
# suma=0
# for nota in notas:
#     suma+=nota
#     c+=1
# prom=suma/c
# print("El promedio es ", round(prom))

# nombres=["Robin","Noelia","Coni"]
# apellido=["Hood","Maldonado","Chan"]

# print(len(nombres))

# for i in range(len(nombres)):
#     print(f"Su nombre es {nombres[i]} {apellido[i]}")

# frutas=["Sandia", "Melon", "Chirimoya"]

# for fruta in frutas:
#     print(f"La {fruta} tiene {len(fruta)} caracteres")

# autos=["Audi", "Toyota", "BWM", "KIA", "Mercedez"]

# for auto in autos:
    # print(auto)
    # if "a" in auto.lower():
    #     print("la marca tiene una a")
    # else:
    #     print("Ni una a encontrada")

# notas=[50,70,55,35,65]
# c=0
# suma=0
# for nota in notas:
#     suma+=nota
#     c+=1
#     print(nota)
#     if "rojos" in nota.():
#         print("la nota es un rojo")
#     else:
#         print("La nota es un azul")
# prom=suma/c
# print("El promedio es ", round(prom))

#      0 1 2 3  4  5
# Numeros=[2,4,6,8,10,12]
# #     -6 -5 -4 -3-2-1

# print(Numeros)

# Numeros.append(20)
# print(Numeros)



# nombres=[]
# apellidos=[]
# while True:
#     print('''
#           1.- Insertar nombre y apellido
#           2.- Buscar nombre
#           3.- Mostrar nombre
#           4.- Salir
#         ''')
#     op=int(input("Seleccione una opcion "))
#     match op:
#         case 1:
#             nom=input("Ingrese un nombre ")
#             nombres.append(nom)
#             print(nombres)
#             ape=input("Ingrese un apellido ")
#             apellidos.append(ape)
#             print(apellidos)
#         case 2:
#          buscar=input("Ingrese el nombre a buscar")
#          if buscar in nombres:
#              print(f"El nombre {buscar} se encuentra en la lista")
#          else:
#              print(f"El nombre {buscar} se encuentra en la lista")
#         case 3:
#             cont=0
#             for i in nombres:

#                 print(cont+1, ".-", nombres[cont], apellidos[cont])
#                 cont+=1

#         case 4:
#             print("Saliendo...")
#             break
#         case _:
#             print("Invalido")

productos=[]
precios=[]
carrito=[]
while True:
    print('''
          1.- Ingresar productos
          2.- Comprar
          3.- crear boleta
          4.- Salir
           ''')
    op=int(input("Ingrese su opcion: "))

    match op:
        case 1:
            print("Ha ingresado a comprar productos")
            produc_tos=int(input('''
                                 1.- Sandia 2500
                                 2.- Pollo Asado 2500
                                 3.- Jugo Watts 1500'''
                                    ))
            productos.append(produc_tos)
            carrito.append(produc_tos)
            precios.append(produc_tos)
            if produc_tos==1:
                Sandia+=2500
            elif produc_tos==2:
                Pollo_Asado+=2500
            else:
                JugoWatts+=1500
        case 2:
            print()        