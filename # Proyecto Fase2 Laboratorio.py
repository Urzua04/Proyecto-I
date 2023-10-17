# Proyecto de laboratorio No.1
# Indice de eficiencia de una línea de producción en un aserradero 
# Santiago Urzúa y Hans Westphal 
print("¡Bienvenido al Sistema de Evaluación de Eficiencia en Líneas de Producción!")
x = ""
while x != 4:
    print("1. Comparación entre 2 líneas")
    print("2. Comparación entre 3 líneas")
    print("3. Comparación entre 4 líneas")
    print("4. Salida")
    print()
    x= int(input("Ingrese una opción: "))
    print()

    if x == 1:
        Nolinea=int(input("-Ingrese el numero de la primera línea: "))
        PrecioMetro2 = float(input("-Ingrese el precio de metro cuadrado: "))
        VentaMetro2 = int(input("-Ingrese la cantidad de metros cuadrados vendidos en el mes: "))
        NoEmpleados = int(input("-Número de empleados (maxímo 20): "))
        if NoEmpleados > 20: 
            print()
            print("El maximo de empleados es 20")
            print()
            continue
        EmpleadoHora = float(input("-Costo del empleado por hora: "))
        print()
        if EmpleadoHora < 144: 
            print()
            print("El empleado no está ganando el salario minimo")
            print()
            continue
        Costo1 = NoEmpleados*EmpleadoHora
        Ingresos1 = PrecioMetro2*VentaMetro2
        Ganancia1 = Ingresos1-Costo1
        Eficiencia1= Ganancia1/NoEmpleados
        Nolinea2=int(input("-Ingrese el numero de la segunda línea: "))
        PrecioMetro22 = float(input("-Ingrese el precio de metro cuadrado: "))
        VentaMetro22 = int(input("-Ingrese la cantidad de metros cuadrados vendidos en el mes en la segunda línea: "))
        NoEmpleados2 = int(input("-Número de empleados (maxímo 20): "))
        if NoEmpleados2 > 20:
            print() 
            print("El maximo de empleados es 20")
            print()
            continue
        EmpleadoHora2 = float(input("-Costo del empleado por hora: "))
        if EmpleadoHora2 < 144: 
            print()
            print("El empleado no está ganando el salario minimo")
            print()
            continue
        Costo2 = NoEmpleados2*EmpleadoHora2
        Ingresos2 = PrecioMetro22*VentaMetro22
        Ganancia2 = Ingresos2-Costo2
        Eficiencia2=Ganancia2/NoEmpleados2
        print()
        print("En la línea", Nolinea, "se tuvo una ganacia de", Ganancia1, "con una eficiencia de", Eficiencia1)
        print("En la línea", Nolinea2,"se tuvo una ganacia de", Ganancia2,"con una eficiencia de", Eficiencia2)
        print()
        if Ganancia1 > Ganancia2:
            print("La línea", Nolinea,"tuvo una mayor eficincia")
        elif Ganancia2 > Ganancia1:
            print("La línea",Nolinea2,"tuvo una mayor eficiencia" )
        else: 
            print("Las dos líneas tiene la misma eficiencia")
            print()
            continue
        print()
        print()
        print("Por favor, seleccione nuevamente una opción del menú para continuar.")

    elif x == 2: 
        Nolinea=int(input("-Ingrese el numero de la primera línea: "))
        PrecioMetro2 = float(input("-Ingrese el precio de metro cuadrado: "))
        VentaMetro2 = int(input("-Ingrese la cantidad de metros cuadrados vendidos en el mes: "))
        NoEmpleados = int(input("-Número de empleados (maxímo 20): "))
        if NoEmpleados > 20:
            print()
            print("El maximo de empleados es 20")
            print()
            continue
        EmpleadoHora = float(input("-Costo del empleado por hora: "))
        if EmpleadoHora < 144: 
            print()
            print("El empleado no está ganando el salario minimo")
            print()
            continue
        Costo1 = NoEmpleados*EmpleadoHora
        Ingresos1 = PrecioMetro2*VentaMetro2
        Ganancia1 = Ingresos1-Costo1
        Eficiencia1= Ganancia1/NoEmpleados
        print()
        Nolinea2=int(input("-Ingrese el numero de la segunda línea: "))
        PrecioMetro22 = float(input("-Ingrese el precio de metro cuadrado: "))
        VentaMetro22 = int(input("-Ingrese la cantidad de metros cuadrados vendidos en el mes en la segunda línea: "))
        NoEmpleados2 = int(input("-Número de empleados (maxímo 20): "))
        if NoEmpleados2 > 20: 
            print()
            print("El maximo de empleados es 20")
            print()
            continue
        EmpleadoHora2 = float(input("-Costo del empleado por hora: "))
        if EmpleadoHora2 < 144: 
            print()
            print("El empleado no está ganando el salario minimo")
            print()
            continue
        Costo2 = NoEmpleados2*EmpleadoHora2
        Ingresos2 = PrecioMetro22*VentaMetro22
        Ganancia2 = Ingresos2-Costo2
        Eficiencia2=Ganancia2/NoEmpleados2
        print()
        Nolinea3=int(input("-Ingrese el número de la tercera línea: "))
        PrecioMetro23 = float(input("-Ingrese el precio de metro cuadrado: "))
        VentaMetro23 = int(input("-Ingrese la cantidad de metros cuadrados vendidos en el mes en la tercera línea: "))
        NoEmpleados3 = int(input("-Número de empleados (maxímo 20): "))
        if NoEmpleados3 > 20:
            print() 
            print("El maximo de empleados es 20")
            print()
            continue
        EmpleadoHora3 = float(input("-Costo del empleado por hora: "))
        if EmpleadoHora3 < 144: 
            print()
            print("El empleado no está ganando el salario minimo")
            print()
            continue
        Costo3 = NoEmpleados3*EmpleadoHora3
        Ingresos3 = PrecioMetro23*VentaMetro23
        Ganancia3 = Ingresos3-Costo3
        Eficiencia3=Ganancia3/NoEmpleados3
        print()
        print("En la línea", Nolinea, "se tuvo una ganacia de", Ganancia1, "con una eficiencia de", Eficiencia1)
        print("En la línea", Nolinea2,"se tuvo una ganacia de", Ganancia2,"con una eficiencia de", Eficiencia2)
        print("En la línea", Nolinea3,"se tuvo una ganacia de", Ganancia3,"con una eficiencia de", Eficiencia3)
        print()
        if Ganancia1 > Ganancia2 and Ganancia1> Ganancia3:
            print("La línea", Nolinea,"tuvo la mayor eficincia")
        elif Ganancia2 > Ganancia1 and Ganancia2 > Ganancia3:
            print("La línea",Nolinea2,"tuvo la mayor eficiencia" )
        elif Ganancia3> Ganancia1 and Ganancia3 > Ganancia2:
            print("La línea", Nolinea3,"tuvo la mayor eficiencia")
        else: 
            print("las tres líneas tiene la misma eficiencia")
            print()
            continue
        print()
        print()
        print("Por favor, seleccione nuevamente una opción del menú para continuar.")

    elif x == 3: 
        Nolinea=int(input("-Ingrese el numero de la primera línea: "))
        PrecioMetro2 = float(input("-Ingrese el precio de metro cuadrado: "))
        VentaMetro2 = int(input("-Ingrese la cantidad de metros cuadrados vendidos en el mes: "))
        NoEmpleados = int(input("-Número de empleados (maxímo 20): "))
        if NoEmpleados > 20: 
            print()
            print("El maximo de empleados es 20")
            print()
            continue
        EmpleadoHora = float(input("-Costo del empleado por hora: "))
        if EmpleadoHora < 144: 
            print()
            print("El empleado no está ganando el salario minimo")
            print()
            continue
        Costo1 = NoEmpleados*EmpleadoHora
        Ingresos1 = PrecioMetro2*VentaMetro2
        Ganancia1 = Ingresos1-Costo1
        Eficiencia1= Ganancia1/NoEmpleados
        print()
        Nolinea2=int(input("-Ingrese el numero de la segunda línea: "))
        PrecioMetro22 = float(input("-Ingrese el precio de metro cuadrado: "))
        VentaMetro22 = int(input("-Ingrese la cantidad de metros cuadrados vendidos en el mes en la segunda línea: "))
        NoEmpleados2 = int(input("-Número de empleados (maxímo 20): "))
        if NoEmpleados2 > 20: 
            print()
            print("El maximo de empleados es 20")
            print()
            continue
        EmpleadoHora2 = float(input("-Costo del empleado por hora: "))
        if EmpleadoHora2 < 144: 
            print()
            print("El empleado no está ganando el salario minimo")
            print()
            continue
        Costo2 = NoEmpleados2*EmpleadoHora2
        Ingresos2 = PrecioMetro22*VentaMetro22
        Ganancia2 = Ingresos2-Costo2
        Eficiencia2=Ganancia2/NoEmpleados2
        print()
        Nolinea3=int(input("-Ingrese el numero de la tercera línea: "))
        PrecioMetro23 = float(input("-Ingrese el precio de metro cuadrado: "))
        VentaMetro23 = int(input("-Ingrese la cantidad de metros cuadrados vendidos en el mes en la tercera línea: "))
        NoEmpleados3 = int(input("-Número de empleados (maxímo 20): "))
        if NoEmpleados3 > 20: 
            print()
            print("El maximo de empleados es 20")
            print()
            continue
        EmpleadoHora3 = float(input("-Costo del empleado por hora: "))
        if EmpleadoHora3 < 144: 
            print()
            print("El empleado no está ganando el salario minimo")
            print()
            continue
        Costo3 = NoEmpleados3*EmpleadoHora3
        Ingresos3 = PrecioMetro23*VentaMetro23
        Ganancia3 = Ingresos3-Costo3
        Eficiencia3=Ganancia3/NoEmpleados3
        print()
        Nolinea4=int(input("-Ingrese el numero de la cuarta línea: "))
        PrecioMetro24 = float(input("-Ingrese el precio de metro cuadrado: "))
        VentaMetro24 = int(input("-Ingrese la cantidad de metros cuadrados vendidos en el mes en la cuarta línea: "))
        NoEmpleados4 = int(input("-Número de empleados (maxímo 20): "))
        if NoEmpleados4 > 20: 
            print()
            print("El maximo de empleados es 20")
            print()
            continue
        EmpleadoHora4 = float(input("Costo del empleado por hora: "))
        if EmpleadoHora4 < 144: 
            print()
            print("El empleado no está ganando el salario minimo")
            print()
            continue
        Costo4 = NoEmpleados4*EmpleadoHora4
        Ingresos4 = PrecioMetro24*VentaMetro24
        Ganancia4 = Ingresos4-Costo4
        Eficiencia4=Ganancia4/NoEmpleados4
        print()
        print("En la línea", Nolinea, "se tuvo una ganacia de", Ganancia1, "con una eficiencia de", Eficiencia1)
        print("En la línea", Nolinea2,"se tuvo una ganacia de", Ganancia2,"con una eficiencia de", Eficiencia2)
        print("En la línea", Nolinea3,"se tuvo una ganacia de", Ganancia3,"con una eficiencia de", Eficiencia3)
        print("En la línea", Nolinea4,"se tuvo una ganacia de", Ganancia4,"con una eficiencia de", Eficiencia4)
        print()
        if Ganancia1 > Ganancia2 and Ganancia1> Ganancia3 and Ganancia1 > Ganancia4:
            print("La línea", Nolinea,"tuvo la mayor eficincia")
        elif Ganancia2 > Ganancia1 and Ganancia2 > Ganancia3 and Ganancia2 > Ganancia4:
            print("La línea",Nolinea2,"tuvo la mayor eficiencia" )
        elif Ganancia3> Ganancia1 and Ganancia3 > Ganancia2 and Ganancia3 > Ganancia4:
            print("La línea", Nolinea3,"tuvo la mayor eficiencia")
        elif Ganancia4> Ganancia1 and Ganancia4 > Ganancia2 and Ganancia4 > Ganancia3:
            print("La línea", Nolinea4,"tuvo la mayor eficiencia")
        else: 
            print("Las cuatro líneas tiene la misma eficiencia")
            print()
            continue
        print()
        print()
        print("Por favor, seleccione nuevamente una opción del menú para continuar.")
        
    elif x == 4:
        print()
        print("Gracias por utilizar nuestro servicio. ¡Hasta luego!")

    else:
        print("Ingresa una opción valida")

