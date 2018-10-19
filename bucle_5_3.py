def tabla_multiplicar ():
    n = input ("Que tabla de multiplicar quieres que haga(numero): ")
    print "Tabla del " + str(n) + ":"
    for i in range (10+1):
        print str(i) + ") " + str(n) +  " * " + str(i) + " = " + str(n * i)

tabla_multiplicar ()

