def contador_par_impar ():
    nfinal = input ("Hasta que numero quieres que analice: ")
    x = 0
    y = 0
    for i in range (nfinal + 1):
        if (i%2 == 0):
            x = x + 1
        else:
            y = y + 1

    print "Hay " + str(x) + " pares"
    print "Hay " + str(y) + " impares"
    print "Y en total hay " + str(x+y) + " numeros (contando con el 0)"

contador_par_impar ()
