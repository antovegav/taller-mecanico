countV = 0
continuar = "si"
bencina = "Bencina"
diesel = "Diesel"
electrico = "Electrico"
hibrido = "Hibrido"

print("--"*25)
print("")
print("\tBienvenido a ServiExpress")
print("")
print("--"*25)
print("")
print("\t\tMenu")
print("")
print("--"*25)

while continuar == "si" or continuar == "Si" or continuar == "SI" or continuar == "s" or continuar == "S":
    menu = int(input("1. Registrar Automovil \n2. Registro Mantenimiento \n3. Consulta Automovil \n4. Salir\n"))
    print("--"*25)
    if menu == 1:
        patente = str(input("Ingrese su patente en cualquiera de los siguientes formatos:\nAA1000 \nBBBB10\n"))
        print("--"*25)
        anoFab = int(input("Ingrese el año de fabricacion del vehiculo, debe estar entre los siguientes años: 1900 - 2021\n"))
        print("--"*25)
        tipoV = str(input("Ingrese la letra del tipo de combustible que utiliza:\nb) Bencina\nd) Diesel\ne) Electrico\nh) Hibrido\n\n"))
        if tipoV == "b" or tipoV == "B":
            tipoV = bencina
        elif tipoV == "d" or tipoV == "D":
            tipoV == diesel
        elif tipoV == "e" or tipoV == "E":
            tipoV == electrico
        elif tipoV == "h" or tipoV == "H":
            tipoV == hibrido
        else:
            print("\tError - Respuesta no valida")
            tipoV = str(input("b) Bencina\nd) Diesel\ne) Electrico\nh) Hibrido\n"))
            if tipoV == "b" or tipoV == "B":
                tipoV = bencina
            elif tipoV == "d" or tipoV == "D":
                tipoV == diesel
            elif tipoV == "e" or tipoV == "E":
                tipoV == electrico
            elif tipoV == "h" or tipoV == "H":
                tipoV == hibrido
        print("--"*25)
        marca = str(input("Ingrese la marca del vehiculo\n\n"))
        print("--"*25)
        modelo = str(input("Ingrese el modelo del vehiculo\n\n"))
        print("--"*25)
        countV = countV + 1
        continuar = str(input("¿Desea continuar?\n\n"))
    elif menu == 2:
        soliPat = str(input("Ingrese la patente de su vehiculo\n"))
        if soliPat == patente:
            print("--"*25)
            print("\tSe ha verificado su pantete con exito")
            print("--"*25)
            ingresoFec = str(input("Ingrese la fecha de observacion: dia/mes/año\n"))
            print("--"*25)
            observaciones = str(input("Ingrese las observaciones:\n"))
            print("--"*25)
            registro = "Fecha:\t",ingresoFec,"\nObservaciones:\n",observaciones
            print("--"*25)
            countV = countV +1
            continuar = str(input("¿Desea continuar?\n"))
        else:
            print("\tError - Patente mal ingresada")
    elif menu == 3:
        if countV == 1 or countV == 2 or countV == 3 or countV == 4:
            print("\tDatos del vehiculo")
            print("--"*25)
            print("Patente:\t\t",patente,"\nAño de Fabricacion:\t",anoFab,"\nTipo de Vehiculo:\t",tipoV,"\nMarca del Vehiculo:\t",marca,"\nModelo:\t\t\t",modelo)
            print("--"*25)
            if countV == 2 or countV == 3 or countV >= 4:
                print("Fecha de Observacion:\t",ingresoFec,"\nObservaciones:\t\t",observaciones)
                print("--"*25)
                continuar = str(input("¿Desea continuar?\n"))
            else:
                print("")
        else:
            print("No tiene ningun Vehiculo Registrado")
    elif menu == 4:
        print("Hasta la proxima")
        break
    else:
        print("Su vehiculo no esta registrado")
print("--"*25)
print("Cerrando Sesion")
print("--"*25)