while True:
    tri = ""
    inp = int(input("voer een nummer in: \n"))
     
    for i in range (0, inp):
        for j in range (0, inp * 2):
            if inp-i < j and (inp+i) > j:
                tri += "*"
            else:
                tri += " "
        tri += "\n"
    print tri