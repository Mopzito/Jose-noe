# def cal_iva(n):
#     return n*0.19
# def cal_desc(precio, porc):
#     return precio*(porc/100)


# productos=[
#     {"nombre" :"portamina", "precio" : 2000},
#     {"nombre":"Goma", "precio": 1600}
# ]

# print(productos[0]["precio"])

producto=[
    {"nombre" :"portamina", "precio" : 2000},
    {"nombre":"Goma", "precio": 1600}
]

def muestra_lista(lista):
    for n,producto in enumerate(lista):
        print(n+1, producto["nombre"], producto["precio"])
def agregar():
                nombre=input("ingrese el nombre del articulo")
                precio=int(input("ingrese el nombre del precio"))
                producto.append({"nombre":nombre, "precio": precio})
def actualizar():
      act=int(input("seleccione cual desea actualizar "))
      nombre=input("Ingrese nombre del articulo: ")
      precio=int(input("ingrese el nombre del precio: "))
      producto[act-1] ["nombre"]=nombre
      producto[act-1] ["precio"]=precio
def borrar():
      borrar=int(input("Ingrese cual quiere eliminar: "))
      producto.pop(borrar-1)
while True:
    try:
        print('''
              1.- Agregar articulos
              2.- Borrar articulos
              3.- Actualizar articulos
              4.- Mostrar listado de articulos
              5.- Salir
              ''')
        op=int(input("Elija su opcion "))

        match op:
            case 1:
                    agregar(producto)
            case 2:
                    borrar(producto)
            case 3:
                    actualizar(producto)
            case 4:
                    muestra_lista(producto)
            case 5:
                    print("Saliendo...")
                    break
            case _:
                print("Seleccione una opcion valida")
    except Exception as error:
          print("El error es: ", error)
