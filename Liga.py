# Categorizar jugadores 
# En una liga amateour, se paga a lo jugadores de futbol
# Cuando anota mas goles recibe nu bono en su paga
# Entre 1-3 goles, 4%; entre 4-6 goles 6%, 7 goles o mas 8%
# Si su equipo queda entre los 3 primeros, +3000 
# Si su equipo queda entre 4-8, +2000 
# Si su equipo queda entre 9 y mas, +1000 
# El pago base por 

#Importar Random

import random

#Categorizar jugadores
# Pan_con_queso_Futbol_Club=11
Arquero=57000
Defensa=55000
Mediocampistas=54500
Delanteros=62000

# Pago base

print("Pago base de los jugadores " \
"Arquero=57.000 " \
"Defensa=55.000 " \
"Mediocampistas=54.500 " \
"Delanteros=62.000 ")



op=int(input("Ingrese cantidad de goles 1.- 1-3 goles 4% 2.- 4-6 goles 6% 3.- 7 o más goles 8%"))

if op==1:
    Arquero*=0.04
    Defensa*=0.04
    Mediocampistas*=0.04
    Delanteros*=0.04
elif op==2:
    Arquero*=0.06
    Defensa*=0.06
    Mediocampistas*=0.06
    Delanteros*=0.06
elif op==3:
    Arquero*=0.08
    Defensa*=0.08
    Mediocampistas*=0.08
    Delanteros*=0.08

print(f"el bono por gol del arquero seria {Arquero} ", f"el bono por gol del defensa seria {Defensa} ", f"el bono por gol de los Mediocampistas son {Mediocampistas} ", f"el bono por gol de los delanteros es {Delanteros}")

op=int(input("Ingrese puesto" "1.- 9 o más +1000" "2.- 4-8 +2000" "3.- los 3 mejores +3000"))

if op==1:
    Arquero+=1000
    Defensa+=1000
    Mediocampistas+=1000
    Delanteros+=1000
elif op==2:
    Arquero+=2000
    Defensa+=2000
    Mediocampistas+=2000
    Delanteros+=2000
elif op==3:
    Arquero+=3000
    Defensa+=3000
    Mediocampistas+=3000
    Delanteros+=3000

print(f"el bono por posicion del equipo, el arquero tendria {Arquero} ", f"el bono por posicion del equipo, el defensa tendria {Defensa} ", f"el bono por posicion del equipo, el Mediocampista tendria {Mediocampistas} ", f"el bono por posicion de equipo, el Delantero tendria {Delanteros}")
