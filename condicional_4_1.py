def cambio_monedas ():
    answer = input ("Cuantos euros quieres cambiar (numero): ")
    answer_2 = raw_input ("Quieres cambiar a libras o a dolares: ")
    if (answer_2 == "libras"):
        print "Obtendras " + str(answer*0.88) + " libras"
    else:
        print "Obtendras " + str(answer*1.15) + " dolares"

cambio_monedas()
