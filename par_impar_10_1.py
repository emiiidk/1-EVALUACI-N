def bucle_10():
    nfinal = input ("Hasta que numero quieres que cuente: ")
    for number in range(nfinal+1):
        if (number%2 == 0):
            print str(number) + " es par"
        else:
            print str(number) + " es impar"
            


bucle_10 ()
