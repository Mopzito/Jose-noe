
perros=int(input("Ingrese los perros que irán a la caza"))
import random
cumple=0
cuota=3
print("comienza la caza")
while True:
    try:
        for p in range(perros):
            conejos=random.randint(0,6)       
            if conejos>=cuota:
                print(f"El perro {p+1} trajo {conejos} conejos")
                print("Fileteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                cumple+=1
            else:
                print(f"El perro {p+1} trajo {conejos} conejos")
                print("No hay filete pipipi")
            
            
            print(f"la cantidad de perros que cumplieron la cuota son {cumple}")
            print(f"la cantidad de perros que no cumplieron la cuota son {cumple-perros}")
    except Exception:
        print("Introduzca un numero entero")
