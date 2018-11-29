# Este programa sirve para introducir 10 numeros y que me devuelva el menor
def programa():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    num4 = float(input("Enter fourth number: "))
    num5 = float(input("Enter fifth number: "))
    num6 = float(input("Enter sixth number: "))
    num7 = float(input("Enter seventh number: "))
    num8 = float(input("Enter eighth number: "))
    num9 = float(input("Enter nineth number: "))
    num10 = float(input("Enter tenth number: "))
    for i in range (10000):
        if (num1 <= i):
            print str(num1)
            break
        elif (num2 <= i):
            print str(num2)
            break
        elif (num3 <= i):
            print str(num3)
            break
        elif (num4 <= i):
            print str(num4)
            break
        elif (num5 <= i):
            print str(num5)
            break
        elif (num5 <= i):
            print str(num5)
            break 
        elif (num6 <= i):
            print str(num6)
            break
        elif (num7 <= i):
            print str(num7)
            break
        elif (num8 <= i):
            print str(num8)
            break
        elif (num9 <= i):
            print str(num9)
            break
        elif (num10 <= i):
            print str(num10)
            break



programa ()

#En primer lugar obtengo los diez primeros numeros a traves de la funcion input y definiendo las variables de cada valor introducido, tomando de referencia el programa que tu nos proporcionas el cual nos pregunta de forma seguida los numeros, estableciendo 10 variables distintas (numeros).
#En segundo lugar establezco un bucle, hasta 10000, ya que considero que el usuario no va a introducir numeros mayores a este.
#En tercer lugar, establezco 10 condiciones, con ayuda de la funcion if y elif. Cada una de ellas evaluara en cada proceso del for si ese numero es menor que la variable contadora i.
#Por lo tanto, al evaluar esta condicion de forma reiterada, si alguno de los valores introducido es menor que la variable contadora i, entrara en el condicional, y mostrara en pantalla en numero en cuestion.
#Por ultimo, con la funcion break, al entrar en un condicional le estare indicando que tiene que detener el bucle, ya que solo busco que me muestre el numero en cuestion una vez en la pantalla, siendo este el menor de los numeros introducidos.

