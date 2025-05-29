#Uso y explicacion de listas
#     -6 -5 -4 -3 -2  -1
# lista=[5, 7, 2, 9, 10 ,2]
# #      0  1  2  3  4   5


# print(lista[-6])
# print(lista[0])

# #muestra toda la lista
# print(lista)

# for num in lista:
#     print(num)

#Hacer una lista de 5 notas
#luego sacar su promedio
#Las notas deben ser valores int
#ej: 55, 67, 34

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
#     print(auto)
#     if "a" in auto.lower():
#         print("la marca tiene una a")
#     else:
#         print("Ni una a encontrada")

notas=[50,70,55,35,65]
c=0
suma=0
for nota in notas:
    suma+=nota
    c+=1
    print(nota)
    if "rojos" in nota.():
        print("la nota es un rojo")
    else:
        print("La nota es un azul")
prom=suma/c
print("El promedio es ", round(prom))