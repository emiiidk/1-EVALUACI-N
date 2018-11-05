def bucle_12_1 ():
    nfinal = input ("Hasta que numero quieres que sume: ")
    x = 0 
    y = 0 
    for i in range (nfinal + 1):
        if (i%2 == 0):
            x = x + i
        else:
            y = y + i

    print "La suma de los pares es: " + str(x)
    print "La suma de los impares es: " + str(y)
    print "La suma total de pares e impares es: " + str(x + y)


bucle_12_1 ()
