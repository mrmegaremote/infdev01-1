while True:
    inp = raw_input("input some text: \n")
    rev = ""

    #inversing the order of the characters
    for i in range (len(inp) -1, -1, -1):
        rev += inp[i]
    print rev
