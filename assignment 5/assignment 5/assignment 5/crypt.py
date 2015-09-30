while True:
    #97 ~ 122
    inp = raw_input("enter a phrase: \n")
    key = input("enter a key: \n")

    cryp = ""
    upper = bool

    def crypt(a, b):
        new = ord(b) + a
        while new > 122:
            new -= 26
        return new


    for i in range (0, len(inp)):
        if inp[i].isalpha():
            if inp[i].isupper():
                upper = True;
            elif inp[i].islower():
                upper = False;

            if upper:
                cryp += str.upper(chr(crypt(key, inp[i])))
            elif not upper:
                cryp += str.lower(chr(crypt(key, inp[i])))
        else:
            cryp += inp[i]
    print cryp