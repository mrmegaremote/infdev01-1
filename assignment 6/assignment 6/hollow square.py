﻿while True:
    inp = input("insert a number: \n")
    shape = ""
    for i in range(0, int(inp)):
        for j in range (0, int(inp * 2)):
            if i == 0 or i == inp - 1 or j == 0 or j == inp * 2 - 1:
                shape += "*"
            else:
                shape += " "
            
        shape += "\n"
    print shape