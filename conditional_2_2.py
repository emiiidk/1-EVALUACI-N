def condicional_2():
    time = input ("Dime la hora (numero): ")
    if (time > 24):
        print "introduce una hora valida (reinicia el programa)"
    elif (time >= 21 ):
        print "Buenas noches"
    elif (time >= 14):
        print "Buenas tardes"
    elif (time >= 0):
        print "Buenos días"


condicional_2 ()
