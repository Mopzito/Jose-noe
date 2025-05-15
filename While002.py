# total=0
# carrito=0
# while True:
#     print('''
#              1.- Nombre
#              2.- Comprar
#              3.- Salir''')

#     op=int(input())

#     match op:
#         case 1:
#             nombre=input("Ingrese nombre")
#         case 2:
#             while True:

#                 print('''Lista de productos disponibles
#                          1.- Sandia = 3670
#                          2.- Miel   = 5000
#                          3.- Salsa de soya = 4000
#                          si compro o no compro presione "4" para salir''')
                
#                 opc=int(input())

#                 match opc:
#                     case 1:
#                         carrito+=3670
#                         total+=1
#                     case 2:
#                         carrito+=5000
#                         total+=1
#                     case 3:
#                         carrito+=4000
#                         total+=1
#                     case 4:
#                         print(f"Su total de producto es {total}")
#                         print(f"su total es {carrito}")
#                         print(f"su total con IVA es {carrito*1.19}")
#                         break
#                     case _:
#                         print("Opción invalida")
               
#         case 3:
#             print(f"Hola {nombre}")
#             print(f"Su total de producto es {total}")
#             print(f"su total es {carrito}")
#             print(f"su total con IVA es {carrito*1.19}")


#             break


