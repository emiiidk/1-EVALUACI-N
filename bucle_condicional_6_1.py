def contador_100_par_multiplo3 ():
    for i in range (100+1):
        if (i%3 == 0):
            print "El numero " + str(i) + " es un numero par. Ademas el numero " + str (i) + " es multiplo de 3."
        elif (i%2 == 0):
            print "El numero " + str(i) + " es un numero par"
        elif (i%2 != 0):
            print "El numero " + str(i) + " es un numero impar"


contador_100_par_multiplo3 ()
        
        
