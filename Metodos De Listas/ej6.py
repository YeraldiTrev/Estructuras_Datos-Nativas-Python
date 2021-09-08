import os
LimpiarPantalla = lambda: os.system('cls')
lista_palabras = []
'''
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, elimine los elementos repetidos (dejando únicamente 
el primero de los elementos repetidos).
'''
LimpiarPantalla()
while True :
    palabra = input('\nIngresa Un Nombre (Presiona "X" para termiar) -> ').title()
    if(palabra) == 'X':
        print('\nFinalizando Etapa de Ingreso de Datos...')
        break
    lista_palabras.append(palabra)
print('\n=============================================================================')
print(f"\nLa lista creada es: {lista_palabras}")
print('\n=============================================================================')


for i in range(len(lista_palabras) - 1, -1, -1):
    if lista_palabras[i] in lista_palabras[:i]:
        del lista_palabras[i]
print(f"\nLa lista sin repeticiones es: {lista_palabras}")
print('\n=============================================================================')

