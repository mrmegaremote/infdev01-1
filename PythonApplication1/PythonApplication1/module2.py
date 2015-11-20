while True:    
    inp = int(input("enter a number: \n"))
    shape  = ""

    for i in range (0, inp):
        for j in range(0, inp):
            if i > j:
                shape += "*"
        shape += "\n"
    print shape