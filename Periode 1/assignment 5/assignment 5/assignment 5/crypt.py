while True:
    #97 ~ 122

    #definitions
    inp = raw_input("enter a phrase: \n")
    key = input("enter a key: \n")

    cryp = ""
    upper = bool

    #encrypting the letter
    def crypt(a, b):
        new = ord(b) + a
        while new > 122:
            new -= 26
        while new < 97:
            new += 26
        return new


    #finding weather the character should be encrypted
    for i in range (0, len(inp)):
        if inp[i].isalpha():
            if inp[i].isupper():
                upper = True;
            elif inp[i].islower():
                upper = False;

            if upper:
                cryp += str.upper(chr(crypt(key, str.lower(inp[i]))))
            elif not upper:
                cryp += str.lower(chr(crypt(key, inp[i])))
        else:
            cryp += inp[i]

    #printing the encrypted password
    print cryp