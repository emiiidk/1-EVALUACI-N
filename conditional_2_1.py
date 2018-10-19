def horas():
    time = raw_input ("Dime la hora (numero): ")
    if (int(time) > 24):
        print "introduce una hora valida (reinicia el programa)"
    elif (int(time) >= 21 ):
        print "Buenas noches"
    elif (int(time) >= 14):
        print "Buenas tardes"
    elif (int(time) >= 0):
        print "Buenos días"
  
horas ()
