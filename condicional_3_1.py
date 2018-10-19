def condicional_3 ():
    edad = input ("Cual es tu edad: ")
    if (edad >= 18):
        print "Sala alcholica"
    else:
        if (edad >=15):
            print "Sala adolescente"
        else:
            print "Sala infantil"

condicional_3()
