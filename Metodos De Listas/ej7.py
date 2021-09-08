'''
Escriba un programa que permita crear dos listas de palabras y que,
a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):

Lista de palabras que aparecen en las dos listas.
Lista de palabras que aparecen en la primera lista, pero no en la segunda.
Lista de palabras que aparecen en la segunda lista, pero no en la primera.
Lista de palabras que aparecen en ambas listas.
Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los
elementos repetidos en cada lista.
'''

def main():
    numero = int(input("Dígame cuántas palabras tiene la primera lista: "))

    if numero < 1:
        print("¡Imposible!")
    else:
        primera = []
        for i in range(numero):
            palabra = input(f"Dígame la palabra {i + 1}: ")
            primera += [palabra]
        print(f"La primera lista es: {primera}")

        for i in range(len(primera) - 1, -1, -1):
            if primera[i] in primera[:i]:
                del primera[i]

        numero2 = int(input("Dígame cuántas palabras tiene la segunda lista: "))

        if numero2 < 1:
            print("¡Imposible!")
        else:
            segunda = []
            for i in range(numero2):
                palabra = input(f"Dígame la palabra {i + 1}: ")
                segunda += [palabra]
            print(f"La segunda lista es: {segunda}")

            for i in range(len(segunda) - 1, -1, -1):
                if segunda[i] in segunda[:i]:
                    del segunda[i]

            comunes = []
            for i in primera:
                if i in segunda:
                    comunes += [i]
            print(f"Palabras que aparecen en las dos listas: {comunes}")

            soloPrimera = []
            for i in primera:
                if i not in segunda:
                    soloPrimera += [i]
            print(f"Palabras que sólo aparecen en la primera lista: {soloPrimera}")

            soloSegunda = []
            for i in segunda:
                if i not in primera:
                    soloSegunda += [i]
            print(f"Palabras que sólo aparecen en la segunda lista: {soloSegunda}")

            todas = comunes + soloPrimera + soloSegunda
            print(f"Todas las palabras: {todas}")


if __name__ == "__main__":
    main()