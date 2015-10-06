from math import *

while True:
    cir = ""
    inp = input("enter a number: \n")

    for i in range(0, inp):
        for j in range (0, inp):
            di = inp / 2
            dj = inp / 2 
            dist = sqrt(di ** di + dj ** dj)
            if inp <= dist:
                cir += "*"
            else:
                cir += " "
        cir += "\n"
    print cir