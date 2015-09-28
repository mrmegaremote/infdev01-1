a = True
while a == True:
    deg = input("how many degrees celsius to kelvin?")
    pre = deg
    deg = deg + 273.15
    try:
        if deg < 0:
            raise ValueError('deg is niet goed')
        print "%s degrees celsius is %s K" % (pre, deg)
        a = False
    except:
        print"that's not a correct entry"