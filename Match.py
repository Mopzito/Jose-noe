# #uso y explicacion de match
# def suma_2(n1,n2,n3):
#     print("El resultado de la suma es", n1+n2*n3)
# def suma():
#     n1=int(input("ingrese un numero "))
#     n2=int(input("Otro numero "))
#     print("El resultado de la suma es ", n1+n2)
# def resta():
#     n1=int(input("ingrese un numero "))
#     n2=int(input("Otro numero "))
#     print("El resultado de la resta es ", n1-n2)
# def dividir():
#     n1=int(input("ingrese un numero "))
#     n2=int(input("Otro numero "))
#     print("El resultado de la divicion es ", n1/n2) 
# def multiplicar():
#     n1=int(input("ingrese un numero "))
#     n2=int(input("Otro numero "))
#     print("El resultado de la multiplicacion es ", n1*n2)

# def calcu():
#     while True:
#         op=int(input('''seleccione una opcion
#                     1.- suma
#                     2.- resta
#                     3.- dividir
#                     4.- multiplicar
#                     5.- salida
#                     '''))
#         match op:
#             case 1:
#                 print("suma")
#                 suma()
#             case 2:
#                 print("resta")
#                 resta()
#             case 3:
#                 print("Dividir")
#                 dividir()
#             case 4:
#                 print("Multiplicar")
#                 multiplicar()
#             case 5:
#                 print("salida")
#                 break
#             case _:
#                 print("opcion invalida")


# # calcu()
# suma_2(7,9,2)

# nuevo menu
# smash bros



def personajes(Jugador)
    while True:
        print("Super Smash Bros Ultimate")
        op=int(input(f'''{Jugador}Seleccione Personaje
                     1.- Mario
                     2.- Pikachu
                     3.- Sonic
                     4.- Link
                     5.- Steve
                     6.- Snake
                     7.- Luigi
                     8.- Yoshi'''))
        match op:
            case 1:
                personaje="Mario!"
            case 2:
                print("Pikachu")
            case 3:
                print("Sonic!")
            case 4:
                print("Link!")
            case 5:
                print("Steve!")
            case 6:
                print("Snake!")
            case 7:
                print("Luigi!")
            case 8:
                print("Yoshi!")
    
pj1=input("Ingrese nombre")
pj2=input("Ingrese nombre")

personaje_1=personajes(pj1)
personaje_2=personajes(pj2)

print(f"el jugador 1 {pj1} elije a {personaje_1} y el jugador 2 {pj2} elije a {personaje_2}")