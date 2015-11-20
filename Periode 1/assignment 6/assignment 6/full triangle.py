while True:
    inp = int(input("enter a number: \n"))
    tri = ""

    for j in range (0, inp):
        for i in range (0, inp):
            if i < j:
                tri += "*"
            else:
                tri += " "
        tri += "\n"
    print tri