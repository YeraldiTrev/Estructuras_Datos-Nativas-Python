import os
'''
Escriba un programa que permita crear una lista de palabras y que, a continuación,
pida una palabra y elimine esa palabra de la lista.
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
    eliminar = input('\nIngresa la Palabra a Eliminar -> ').title()
    print('\n================================================================================')
    if eliminar in lista_palabras:
        indice = lista_palabras.index(eliminar)
        lista_palabras.pop(indice)
        print(f'Eliminando la Palabra "{eliminar}" de la Lista...')
        print('\nPalabra Eliminada...')
        print('\n================================================================================\n')
        break
    else:
        print('Esta Palabra No Esta en la Lista. Intente de Nuevo, Por Favor...')
        print('\n================================================================================')

print(f'Lista de Palabras Actualizada: {lista_palabras}')
print('\n================================================================================')