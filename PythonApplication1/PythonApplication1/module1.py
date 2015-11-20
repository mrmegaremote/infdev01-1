while True:    
    inp = str(raw_input("Enter some text: \n"))
    new = ""
    for i in inp:
        if i.isupper():
            new += i
    print new