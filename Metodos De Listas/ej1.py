"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, 
pida una palabra y diga cuántas veces aparece esa palabra en la lista.
"""

nombres = []
while True :
    nombre = input('\nIngresa Un Nombre (Presiona "X" para termiar) -> ').title()
    if(nombre) == 'X':
        print('\nFinalizando Etapa de Ingreso de Datos...')
        break
    nombres.append(nombre)

print('\n================================================================================')
print('\nLista de Nombres Creada: ', nombres)
print('\n================================================================================\n')

buscarNombre = input('Ingresa el Nombre a Buscar -> ').title()

if nombres.count(buscarNombre) == 1:
    print('\n================================================================================')
    print(f'\nEl nombre {buscarNombre} aparece {nombres.count(buscarNombre)} vez en la lista. ')
    print('\n================================================================================')
elif nombres.count(buscarNombre) >= 2:
    print('\n===================================================================================')
    print(f'\nEl nombre {buscarNombre} aparece {nombres.count(buscarNombre)} veces en la lista. ')
    print('\n===================================================================================')
elif not(buscarNombre in nombres):
    print('\n================================================================================')
    print(f'\nEl nombre {buscarNombre} No esta en la lista')
    print('\n================================================================================')