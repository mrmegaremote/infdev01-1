while True:    
    inp = int(input("enter a number: \n"))
    shape  = ""

    for i in range (0, inp):
        for j in range (i, inp):
            shape += " "
        for x in range (0, j):
            shape += "*"
        shape += "\n"

    print shape