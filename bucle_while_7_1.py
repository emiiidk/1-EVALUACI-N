def cuenta_atras ():
    n = input ("Desde que numero quieres que haga la cuenta atras: ")
    print "Primera variante:"
    for i in range(n,0-1,-1):
        print str(i)

    print "Segunda variante:"
    while n >= 0:
        print str(n)
        n = n-1 



cuenta_atras ()
