# El numero de asteriscos = 2 por la fila en la que estoy -1
# El numero de espacios = altura de la piramide - fila en la que estoy

def piramide ():
    h = input("De que altura quieres la piramide(numero): ")
    for i in range (h+1):
        asteriscos = 2*i - 1
        espacios = h - i
        print " " * espacios + "*" * asteriscos

piramide()


