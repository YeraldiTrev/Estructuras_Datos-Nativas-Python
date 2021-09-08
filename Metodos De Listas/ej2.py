import os
'''
Escriba un programa que permita crear una lista de palabras y que, a continuación,
pida dos palabras y sustituya la primera por la segunda en la lista.
'''
LimpiarPantalla = lambda: os.system('cls')
lista_palabras = []

# Inicio del programa
LimpiarPantalla()
while True :
    palabra = input('\nIngresa Un Nombre (Presiona "X" para termiar) -> ').title()
    if(palabra) == 'X':
        print('\nFinalizando Etapa de Ingreso de Datos...')
        break
    lista_palabras.append(palabra)

LimpiarPantalla()
print('\n================================================================================\n')
print(f'Lista de Palabras Creada: {lista_palabras}')
print('\n================================================================================\n')

while True :
    sustituir = input('\nIngresa la Palabra a Sustituir -> ').title()
    print('\n================================================================================')
    if sustituir in lista_palabras:
        sustituto = input('\nIngresa el Sustituto de la Palabra -> ').title()
        print('\n================================================================================\n')
        indice = lista_palabras.index(sustituir)
        lista_palabras.pop(indice)
        lista_palabras.insert(indice, sustituto)
        print(f'Sustituyendo {sustituir} Por {sustituto} en la Lista...')
        print('\nPalabra sustituida...')
        print('\n================================================================================\n')
        break
    else:
        print('Esta Palabra No Esta en la Lista. Intente de Nuevo, Por Favor...')
        print('\n================================================================================')

print(f'Lista de Palabras Actualizada: {lista_palabras}')
print('\n================================================================================')
