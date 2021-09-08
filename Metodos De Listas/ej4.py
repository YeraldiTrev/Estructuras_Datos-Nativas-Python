import os
LimpiarPantalla = lambda: os.system('cls')
lista_palabras = []
'''
Escriba un programa que permita crear dos listas de palabras y que,
a continuación, elimine de la primera lista los nombres de la segunda lista
'''

LimpiarPantalla()
print('\n=============================================================================')
while True :
    palabra = input('\nIngresa Un Nombre (Presiona "X" para termiar) -> ').title()
    if(palabra) == 'X':
        print('\nFinalizando Etapa de Ingreso de Datos...')
        break
    lista_palabras.append(palabra)

LimpiarPantalla()
print('\n=============================================================================\n')
print(f'Lista de Palabras Creada: {lista_palabras}')
print('\n=============================================================================')

while True :
    limite = int(input("\nInserta la Cantidad de Palabras a Eliminar -> "))
    print('\n===========================================================================\n')
    if limite < 1 or limite > len(lista_palabras):
        print("\n¡Error!, Ingrese un Numero Valido.\n")
    else:
        eliminar = []
        for i in range(limite):
            palabra = input(f"\nInsertar la palabra numero {i + 1} -> ").title()
            eliminar += [palabra]
        print('\n===========================================================================')
        print(f"\nPalabras a Eliminar: {eliminar}")
        print('\n===========================================================================\n')
        input()
        break

for i in eliminar:
    for j in range(len(lista_palabras) - 1, -1, -1):
        if lista_palabras[j] == i:
            del lista_palabras[j]
print(f"Lista Actualizada: {lista_palabras}")
print('\n===========================================================================\n')