# Sumatoria de Numeros.
def sumatoria(lista):
    suma = 0 
    for i in lista:
        suma+=i
    return suma

# Deteccion de numeros menores.
def numerosMenores(lista, limite):
    # Creo una lista nueva
    nueva=[]
    # Recorro la lista original para encontrar los numeros menores
    for n in lista:
        # Si el numero es menor al limite se agrega a la lista.
        if n<limite:
            nueva.append(n)
    # Finalmente se retorna la lista.
    return nueva

# Frecuencias de repeticiones
def frecuencias(lista):
    # Creo una lista nueva 
    nueva_lista=[]
    # Recorro la lista original
    for n in lista:
        # si el conteo del numero, no esta en la lista, agrego eso a la lista nueva.
        if [n, lista.count(n)] not in nueva_lista:
            nueva_lista.append([n, lista.count(n)])
    # Finalmente retorno el valor de la lista como una tupla.
    return tuple(nueva_lista)

# Creacion de la lista de numeros.
lista_numeros = []

print("\n-------------------------Parte A---------------------------------")

# Ingreso de los numeros.
# Se crea un bucle infinito
while True:
    # Pedimos que se ingrese el numero.
    ingreso_numeros = input("\nIngresa un numero(ingresa cero para finalizar el proceso) -> ")

    # Convertimos el valor a entero
    ingreso_numeros = int(ingreso_numeros)

    # Lo agregamos a la lista de numeros (append agrega elemtos a la lista).
    lista_numeros.append(ingreso_numeros)

    # Si el numero es cero, se dejara de repetir este proceso.
    if ingreso_numeros == 0:
        print("\nFinalizando Proceso de entrada...")
        break
    # De lo contrario se seguira repitiendo.

lista_numeros.remove(0)
print("\n-------------------------Parte B---------------------------------")

# Creamos un bucle infinito
while True:
    # Pedimos un numero para eliminar.
    eliminar_numero = int(input("\nIngresa un numero a eliminar -> "))

    # Verificamos que el numero este en la lista y que no sea el cero.
    if eliminar_numero in lista_numeros:

        # Si esta en la lista eliminara el numero ingresado
        print(f"\nEliminando numero {eliminar_numero}...")
        print(f"\nNumero {eliminar_numero} eliminado...")

        #* Linea de codigo que elimina el dato.
        # Remove, elimina un elemento especifico que se encuentre en la lista
        # si esta repetido eliminara el primer elemento que se encuentre en la lista.
        lista_numeros.remove(eliminar_numero)

        # Rompemos el bucle una vez finalizado.
        break
    else:
        # De lo contrario muestra un mensaje de error, y lo vuelve a pedir
        # hasta que encuentre un numero que este en la lista.
        print("""
        El numero ingresado no esta en la lista, o no es valido, intenta de nuevo
        Por favor...
        """)

print("\n-------------------------Parte C---------------------------------")

# Se utiliza la funcion creada para sumar.
print("\nLa suma de los numeros en la lista es de: ",sumatoria(lista_numeros))

print("\n-------------------------Parte D---------------------------------")

# Parte D explicada en la funcion
limite=int(input("\nFiltrar números menores a -> "))
print("\nNumeros filtrados: ")
for n in numerosMenores(lista_numeros, limite):
    print(n)

print("\n-------------------------Parte E---------------------------------")

# parte E explicada en la funcion.
for tupla in frecuencias(lista_numeros):
    print(f'Repeticiones de {tupla[0]}: {tupla[1]}')