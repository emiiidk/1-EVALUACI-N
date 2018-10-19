def while_tablas_multiplicar ():
    n = input ("Que tabla quieres que haga(numero): ")
    x = 0
    print "Tabla del " + str(n) + ":"
    while x <= 10:
        print str(x) + ") " + str(x) + " * " + str (n) + ": " + str(n*x)
        x = x + 1


while_tablas_multiplicar ()
               
