import os
LimpiarPantalla = lambda: os.system('cls')
lista_palabras = []
'''
Escriba un programa que permita crear una lista de palabras y que, a continuación,
cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la 
lista al revés, sino de crear una lista distinta).
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

invertida = []
for i in lista_palabras:
    invertida = [i] + invertida
print(f"\nLista Inversa: {invertida}")
print('\n=============================================================================')