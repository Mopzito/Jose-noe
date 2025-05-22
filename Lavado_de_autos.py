import random
import time
Diamantes=0
Carbon=0
Palo=0
Inventario_Diamantes=0
Inventario_Carbon=0
Inventario_Palo=0
espada_Diamante=0
while True:
    op=int(input('''Que hago?
                    1.- Minar
                    2.- Inventario
                    3.- Ir a casa y a craftear
                    4.- Dormir
                    
                    entonces que hacer? = '''))
    match op:
        case 1:
            print("Minar")
            Minar=random.randint(1,7)
            if Minar<1 and 2:
                Inventario_Palo=Palo+1
                print(f"Conseguiste {Inventario_Palo} palo")
                time.sleep(2)
            elif Minar==3 and 4 and 5 and 6:
                Inventario_Carbon=Carbon+1
                print(f"Conseguiste {Inventario_Carbon} carbon")
                time.sleep(2)
            else:
                Inventario_Diamantes=Diamantes+1
                print(f"Conseguiste {Inventario_Diamantes} Diamantes")
                time.sleep(2)
        case 2:
            print(f'''tienes
                       {Inventario_Diamantes} Diamantes
                       {Inventario_Carbon} Carbon
                       {Inventario_Palo} Palos''')
        case 3:
            print("Volvio a casa, esta algo lag por sus granjas automaticas, desea craftear algo?")
            if Inventario_Diamantes>2 and Inventario_Palo>1:
                espada_Diamante=Inventario_Diamantes+Inventario_Palo
                print(f"Haz crafteado {espada_Diamante} espada de diamante")

            
       
    


