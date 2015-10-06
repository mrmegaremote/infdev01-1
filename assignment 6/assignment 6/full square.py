while True:
    inp = input("insert a number: \n")
    shape = ""
    for i in range(0, int(inp)):
        for j in range (0, int(inp)):
            shape += "*"
        shape += "\n"
    print shape