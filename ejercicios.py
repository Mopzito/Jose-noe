import random
while True:
    try:
        cant=int(input("ingrese un numero de perros: "))
        cuota=3
        cumple=0
        for i in range(cant):
            con=random.randint(0,5)
            print(f"El perro {i+1} trajo {con} conejos")
            if con>=cuota:
                print("El perro gana filete")
                cumple+=1
            else:
                print("Se queda sin carne de res")
        print(f" La cantida de perro que cuplieron la cuota es {cumple}")
        print(f" La cantida de perro que NO cuplieron la cuota es {cant-cumple}")
        break
    except Exception:
        print("Solo se aceptan numeros enteros")
