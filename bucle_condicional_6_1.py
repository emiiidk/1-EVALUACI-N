def contador_100_pares_m3 ():
    for i in range(101):
        if (i%2 == 0):
            print "El numero " + str(i) + " es un numero par.",
            if (i%3 == 0):
                print "Ademas es multiplo de 3"
            print "\n"
        else:
            print "El numero " + str(i) + " es un numero impar.",
            if (i%3 == 0):
                print "Ademas es multiplo de 3"
            print "\n"
  
contador_100_pares_m3 ()
