while True:    
    inp = int(input("enter a number: \n"))
    shape  = ""

    for i in range (0, inp):
        for j in range(0, inp * 2):
            if inp - i < j and inp + i > j:
                shape += "*"
            else:
                shape += " "
        shape += "\n"
    print shape