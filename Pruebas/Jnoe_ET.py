productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JJFFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'FGDXFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JJFFHD': [424990,1],
'FGDXFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 
}

def mostrar_productos(goku):
    for i in goku:
        producto=productos[i]+productos[i[0]].sort
        print(producto)
        
def stock_marca(marca):
    busqueda_stockmarca=input("ingrese marca: ").upper()
    if busqueda_stockmarca in marca:
        stock[busqueda_stockmarca][1]
        print(f"El stock de esta marca es {marca[busqueda_stockmarca][1]}")
    else:
        print("el stock y marca no existen")

def busqueda_precio(vegeta, sandia):
    resultado=[f"{productos.get(m, ['desconocida'])[0]}--{m}"]
    for m, (precio, cant) in stock.items():
        if vegeta<=precio<=sandia and cant>0:
            if resultado:
                print("Los notebooks entre los precios consultados son: "), sorted(resultado) 
            else:
                "No hay notebooks en ese rango"
        

while True:
    try:
        op=int(input('''    
                        *** MENU PRINCIPAL ***
                            1. Stock marca.
                            2. Búsqueda por precio.
                            3. Actualizar precio.
                            4. Salir
                            Ingrese opción: '''))
        match op:
            case 1:
                stock_marca(stock)
            case 2:
                busqueda_precio(p_min, p)
            case 3:
                print("")
            case 4:
                print("programa finalizado")
                break
            case _:
                print("opcion invalida")
    except Exception as e:
        print("Ha ocurrido un error: ", e)