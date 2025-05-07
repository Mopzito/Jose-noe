# # #street fighter

# # #Dejar importado random y time

# import random
# import time

# # Asignar Vida
# Ryu = 50
# Chunli = 50

# # Asignar daño de ataques
# Golpes_Ryu = random.randint(1, 10)
# Golpes_Chunli = random.randint(1, 10)
# Hadouken_Ryu = random.randint(7, 14)
# Hyakuretsukyaku_Chunli = random.randint(7, 14)

# # Sistema de turnos
# while Ryu > 0 and Chunli > 0:
#     # Turno de Ryu
#     print("Turno de Ryu")
#     print("1.- Golpes", "2.- Hadouken")
#     op = int(input("¿Con qué atacará? "))
#     if op == 1:
#         Chunli -= Golpes_Ryu
#         print(f"Ryu atacó con Golpes y dejó a Chunli con {Chunli} HP")
#         time.sleep(5)
#     elif op == 2:
#         Chunli -= Hadouken_Ryu
#         print(f"Ryu atacó con Hadouken y dejó a Chunli con {Chunli} HP")
#         time.sleep(5)
#     else:
#         print("Opción no válida, pierde el turno.")
#         time.sleep(5)
#     # Verificar si Chunli ha perdido
#     if Chunli <= 0:
#         print("¡Ryu gana!")
#         exit()
        
#      # Turno de Chunli
#     print("Turno de Chunli")
#     ataque = random.choice(["Golpes", "Hyakuretsukyaku"])
#     if ataque == "Golpes":
#         Ryu -= Golpes_Chunli
#         print(f"Chunli atacó con Golpes y dejó a Ryu con {Ryu} HP")
#         time.sleep(5)
#     else:
#         Ryu -= Hyakuretsukyaku_Chunli
#         print(f"Chunli atacó con Hyakuretsukyaku y dejó a Ryu con {Ryu} HP")
#         time.sleep(5)

#      # Verificar si Ryu ha perdido
#     if Ryu <= 0:
#         print("¡Chunli gana!")
#         exit()

        