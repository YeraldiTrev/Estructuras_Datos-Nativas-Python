mtzAlumnos = []
lstAlumno = []
while (True):
    print("=Sistema de Alumnos=")
    print("")
    print("1.- Alta Registro")
    print("2.- Mostrar Base de Datos")
    print("3.- Borrar Registro")
    print("4.- Reporte de Promedio de edades")
    print("5.- Salir del sistema")
    Opc = int(input("Ingrese la opción a realizar: "))
    if(Opc == 1):
        print()
        print("=Alta de Registro=")
        lstAlumno.append(int(input("Ingresa la Matricula: ")))
        lstAlumno.append(str(input("Ingresa el Nombre: ")))
        lstAlumno.append(int(input("Ingresa la Edad: ")))
        mtzAlumnos.append(list(lstAlumno))
        lstAlumno.clear()
        print()
        print("Registros capturado")
        print()

    elif(Opc == 2):
        print()
        print("=Reporte de ALumnos")
        
        print("|Matricula | Nombre  |  Edad|")
        for Ren in range(0,len(mtzAlumnos)):
            print("|" + str(mtzAlumnos[Ren][0]) + "        | " + str(mtzAlumnos[Ren][1]) + "    |  " + str(mtzAlumnos[Ren][2]) + "  |")

        print()
    elif(Opc == 3):
        print()
        print("=Borrar de ALumnos")
        Matricula = int(input("Ingrese la Matricula del registro a borrar: "))
        
        #Recorrer los renglones para encontrar en donde esta 
        for Ren in range(0,len(mtzAlumnos)):
            if mtzAlumnos[Ren][0] == Matricula:
                Renglon = Ren
        
        mtzAlumnos.pop(Renglon)

    elif(Opc == 4):
        print()
        print("=Reporte de Promedio de edades=")
        print()
        SumaEdades = 0
        for Ren in range(0,len(mtzAlumnos)):
            SumaEdades += int(mtzAlumnos[Ren][2])

        print("El promedio es: " + str(SumaEdades / len(mtzAlumnos)))

    elif(Opc == 5):
        print()
        print("Saliendo del sistema...")
        print()
        exit()
    else:
        print()
        print("La opción ingresada no es valida..")
        print()