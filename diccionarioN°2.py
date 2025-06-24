#crud de diccionario

def mostrar_juegos(dic):
    for j, datos in dic.items():
        print(j, datos)

juegos={
    1:{"nombre": "Call Of Duty Black Ops 2",
       "precio": 30000,
       "code": "CoDBo2012"
    
    },
    2:{"nombre": "Minecraft",
       "precio": 27000,
       "code": "MC2011"
    }
    
}
mostrar_juegos(juegos)
ultima=list(juegos.keys())[-1]
nombre=input("ingrese el nombre del juego: ")
precio=int(input("ingrese el precio del juego: "))
code=input("ingrese el codigo del juego: ")
juegos[ultima+1]={
    "nombre": nombre,
    "precio": precio,
    "code":code
    }

mostrar_juegos(juegos)

def valida_pass(clave):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula=+1
        if palabra.islower():
            Minuscula=+1
        if palabra.isdigit():
            Numero=+1
    if Mayuscula and Minuscula==2 and Numero==4
        print("la clave está bien escrita")
        return True
    else:
        print("la clave está mal escrita")
        return False

valida_pass(clave)