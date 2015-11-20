while True:
    
    inp = input ("pick a number: ")
    
    if inp < 0:
        print "the absolute of %s is %s" % (inp, inp * -1)
    else:
        print "the absolute value is %s" % inp