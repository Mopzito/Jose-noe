personas={
    1:{"nombre": "Steve",
       "Telefono": 982938862,
       "Estado civil": "Soltero",
       "Ciudadano": True},
    2:{"nombre": "Jane doe",
       "Telefono": 982872162,
       "Estado civil": "Soltero",
       "Ciudadano": True},
    3:{"nombre": "Bocchi",
       "Telefono": 982982762,
       "Estado civil": "Soltero",
       "Ciudadano": True},
    4:{"nombre": "Goku",
       "Telefono": 983958862,
       "Estado civil": "Soltero",
       "Ciudadano": True},
    5:{"nombre": "XD",
       "Telefono": 982643862,
       "Estado civil": "Soltero",
       "Ciudadano": True},
}

while True:
    try:
        print('''
              1.- Ingresar Persona
              2.- Mostrar listado
              3.- Actualizar persona
              4.- Borrar persona
              5.- Salir
              ''')
        op=int(input("Seleccione una opcion "))
        match op:
            case 1:
                per=input("Ingrese la persona que quiere agregar: ")
                Telefono=int(input("Ingrese el numero: "))
                Estado_Civil=input('''Ingrese si esta casado o no con
                                        1.- Casado
                                        2.- Soltero
                                        ''')
                if Estado_Civil==1:
                    EstadoCivil="Casado"
                elif Estado_Civil==2:
                    EstadoCivil="Soltero"
                
                ciudadano=input('''Ingrese si es ciudadano o no con
                                        1.- Si es
                                        2.- No es
                                        ''')
                if ciudadano==1:
                    ciudada=True
                else:
                    ciudada=False
                ld=len(personas)+1
                personas[ld]=                  {"nombre": per,
                                                "Telefono": Telefono,
                                                "Estado civil": EstadoCivil,
                                                "Ciudadano": ciudada},
            case 2:
                print(personas)
    except Exception as e:
        print("El error es este: ", e)