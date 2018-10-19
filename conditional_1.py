def condicional_1():
    name = raw_input("Dime tu nombre: ")
    answer = raw_input( name + ", ¿vienes o te vas? ")
    if(answer == "voy"):
        print "Hola " + name
    else:
        print "Adios " + name

condicional_1()
