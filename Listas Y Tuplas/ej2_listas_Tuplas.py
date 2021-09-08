# Area de Importacion de Modulos.
import os

#Area de creacion de variables Globales. 
LimpiarPantalla = lambda: os.system('cls')
ciudades = [
    ("Mexico","Mexico"),("Buenos Aires", "Argentina"),("Kabul","Afganistan"),
    ("San Salvador","El Salvador"),("Madrid","España"), ("Nueva York","Estados Unidos"),
    ("Tokio","Japon"), ("Moscu","Rusia"), ("Londres","Reino Unido")
    ]
pasajeros = [
    ('Yeraldi', 2079052 ,'Londres'),('Adolfo', 2089050 ,'Tokio'), 
    ('Debanhi', 2089078 ,'Londres'),('Andrea', 1908976 ,'Nueva York'), 
    ('Alejandra', 2190876 ,'Tokio'),('Leonardo', 2089065 ,'Tokio'),
    ('Angel', 2908976 ,'Madrid'),('Lizbeth', 3908790 ,'Madrid'),
    ('Antonio', 9078908 ,'Madrid'),('Erick', 1789067 ,'Madrid')
    ]

# Area de Funciones
def muestra_tabular_ciudades():
    # Tabular
    print("{:>20} {:>20}".format( 
        "CIUDAD",
        "PAIS"))
    print("{:>20} {:>20}".format( 
        "-----------------",
        "-----------------"))
    for elemento in ciudades:
        print("{:>20} {:>20}".format( 
        elemento[0], elemento[1]))

def muestra_tabular_pasajeros():
    # Tabular
    print("{:>20} {:>20} {:>20}".format( 
        "NOMBRE",
        "DNI",
        "DESTINO"))

    print("{:>20} {:>20} {:>20}".format( 
        "-----------------",
        "-----------------",
        "-----------------"))

    for elemento in pasajeros:
        print("{:>20} {:>20} {:>20}".format( 
        elemento[0], elemento[1], elemento[2]))

def agregarCiudades():
    while True:
        print("\nIngresa 'X' Para Terminar...\n")
        ingresoCiudad = input("Ingresa Nombre de la ciudad -> ").title()
        if  ingresoCiudad == "X":
            #ciudades.pop(-1)
            break
        ingresoPais = input("Ingresa el Pais de Donde Es La Ciudad -> ").title()
        ciudades.append((ingresoCiudad,ingresoPais))
    return ciudades

def agregarPasajeros():
    # Funcion privada que permite buscar las ciudades que tenemos en la lista.
    def ciudadLista(destino):
        for ciudadPais in ciudades:
            for ciudad in ciudadPais:
                if destino in ciudad:
                    return True
    nombre = input("\nIngrese El Nombre y Apellidos -> ").title()
    dni = int(input("\nIngrese El DNI -> "))
    # Bucle infinito para agregar ciudad valida.
    while True:
        destino = input("Ingrese El Destino -> ").title()
        if ciudadLista(destino) == True:
            print("\nAgregando Pasajero a la lista...")
            pasajeros.append((nombre,dni,destino))
            print("\nPasajero agregado")
            break
        else:
            print("Ingrese una ciudad valida, o añadala al catalago de destinos...")

def buscarCiudad(pasajeros, dni):
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""

def cantidadPasajerosCiudad(ciudad):
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad

def buscarPaisDestino(pasajeros, ciudades, dni):
    buscada=buscarCiudad(pasajeros, dni)
    for ciudad in ciudades:
        if ciudad[0]==buscada:
            return ciudad[1]
    return ""

def cantidadPasajerosPais(pasajeros, ciudades, pais):
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad

LimpiarPantalla()
# Presentacion del Programa
print('================================================================================')
print('================================================================================')
print('================================================================================')
print('=========================Software De Registro De Viajes=========================')
print('============================©Yeraldi Treviño Herrera============================')
print('================================================================================')
print('================================================================================')
print('================================================================================')
input()

# Funcionamiento Principal del Programa.
while True:
    LimpiarPantalla()
    # Menu de opciones
    print("\n--------------------Menu de Opciones--------------------")
    print("1. Agregar pasajeros.")
    print("2. Agregar Ciudades A La Lista(Solo Admin).")
    print("3. Mostrar Ciudad De Viaje Del Pasajero.")
    print("4. Mostrar Total De Personas Que Viajaran A Una Ciudad.")
    print("5. Mostrar Pais De Viaje Del Pasajero.")
    print("6. Mostrar Total De Personas Que Viajaran A Un Pais.")
    print("7. Mostrar Lista De Pasajeros.")
    print("8. Mostrar Lista De Ciudades Y Paises Disponibles")
    print("X. Salir Del Programa.")
    # Entrada de datos del usuario para el menu.
    opcion_menu = input("Ingresa Una Opcion -> ").upper()
    # Agregar Pasajeros.
    if opcion_menu == '1':
        LimpiarPantalla()
        print('                           Agregar Pasajeros')
        print('\n================================================================================')
        agregarPasajeros() 
        print('\n================================================================================')
        input('\nPresiona Enter Para Continuar...\n')
        print('\n================================================================================')
    # Agregar Ciudades.
    elif opcion_menu == '2':
        LimpiarPantalla()
        print('                           Agregar Ciudaes')
        print('================================================================================')
        contrasena = input('\nIngresa La Contraseña De Administrador -> ')
        if contrasena == 'Yeraldi_trev':
            print('\nIngresando..... ')
            print('\n================================================================================')
            input('..')
            LimpiarPantalla()
            print('                           Agregar Ciudaes')
            print('================================================================================')
            agregarCiudades()
            print('================================================================================')
        else:
            print('\nContrasñea Incorrecta...')
            input('\nPresiona Enter Para Continuar...\n')
    # Buscar ciudad a donde viajara un pasajero.
    elif opcion_menu == '3':
        LimpiarPantalla()
        print('                    Mostrar Ciudad De Viaje Del Pasajero')
        print('\n================================================================================')
        dni = int(input('\nIngresa El DNI Del Pasajero -> '))
        print('================================================================================')
        LimpiarPantalla()
        print('                    Mostrar Ciudad De Viaje Del Pasajero')
        print('\n================================================================================')
        if buscarCiudad(pasajeros,dni) == '':
            print("\nEl Pasajero Ingresado No Esta Registrado\n")
        else:
            print(f"\nEl Pasajero Con El DNI '{dni}' Viajara A {buscarCiudad(pasajeros,dni)}\n")
        print('================================================================================')
        input('\nPresiona Enter Para Continuar...\n')
    # Total de pasajeros que viajaran a una ciudad.
    elif opcion_menu == '4':
        LimpiarPantalla()
        print('                Total de pasajeros que viajaran a una ciudad')
        print('\n================================================================================')
        ciudad = input('\nIngrese El Nombre De La Ciudad -> ').title()
        print('\n================================================================================')
        LimpiarPantalla()
        print('                Total de pasajeros que viajaran a una ciudad')
        print('================================================================================')
        print(f"\nTotal De Pasajeros Que Viajaran A '{ciudad}': {cantidadPasajerosCiudad(ciudad)}\n")
        print('================================================================================')
        input('\nPresione Enter Para Continuar...')
    # Buscar Pais a Donde Viajara el Pasajero.
    elif opcion_menu == '5':
        LimpiarPantalla()
        print('                       Mostrar Pais De Viaje Del Pasajero')
        print('\n================================================================================')
        dni = int(input('\nIngresa El DNI Del Pasajero -> '))
        print('================================================================================')
        LimpiarPantalla()
        print('                       Mostrar Pais De Viaje Del Pasajero')
        print('\n================================================================================')
        if buscarPaisDestino(pasajeros,ciudades,dni) == '':
            print("\nEl Pasajero Ingresado No Esta Registrado\n")
        else:
            print(f"\nEl Pasajero Con El DNI '{dni}' Viajara A {buscarPaisDestino(pasajeros,ciudades,dni)}\n")
        print('================================================================================')
        input('\nPresiona Enter Para Continuar...\n')
    # Total de Pasajeros que Viajaran a un Pais.,]
    elif opcion_menu == '6':
        LimpiarPantalla()
        print("                  Mostrar Total De Personas Que Viajaran A Un Pais")
        print('\n================================================================================')
        pais = input('\nIngrese El Nombre Del Pais -> ').title()
        print('\n================================================================================')
        LimpiarPantalla()
        print("                  Mostrar Total De Personas Que Viajaran A Un Pais")
        print('================================================================================')
        print(f"\nTotal De Pasajeros Que Viajaran A '{pais}': {cantidadPasajerosPais(pasajeros,ciudades,pais)}\n")
        print('================================================================================')
        input('\nPresiona Enter Para Continuar...\n')
    # Mostrar Listado de Pasajeros
    elif opcion_menu == '7':
        LimpiarPantalla()
        print("                        Mostrar Lista De Pasajeros")
        print('\n================================================================================\n')
        muestra_tabular_pasajeros()
        print('\n================================================================================')
        input('\nPresiona Enter Para Continuar...\n')
    # Mostrar Lista de Pises y Ciudades.
    elif opcion_menu == '8':
        LimpiarPantalla()
        print("                       Mostrar Lista De Ciudades Y Paises")
        print('\n================================================================================\n')
        muestra_tabular_ciudades()
        print('\n================================================================================')
        input('\nPresiona Enter Para Continuar...\n')
    # Finalizar Programa.
    elif opcion_menu == 'X':
        # Presentacion de la finalizacion del programa.
        print("\nFinalizando Programa...")
        LimpiarPantalla()
        print('================================================================================')
        print('================================================================================')
        print('================================================================================')
        print('=========================Software De Registro De Viajes=========================')
        print('============================©Yeraldi Treviño Herrera============================')
        print('================================================================================')
        print('================================================================================')
        print('================================================================================')
        exit()