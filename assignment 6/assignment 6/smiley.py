from math import *

while True:
    cir = ""
    inp = input("enter a number: \n")

    for i in range(0, inp * 2):
        for j in range (0, inp * 2):
            di = (i - inp) ** 2
            dj = (j - inp) ** 2 
            dist = sqrt(di + dj)
            if inp > dist and inp * 0.8 < dist: 
                cir += "*"
            elif j == inp - inp / 3 and i == inp - (inp / 4) or j == inp + inp / 3 and i == inp - (inp / 4):
                cir += "#"
            #elif 
            else:
                cir += " "
            
        cir += "\n"
    print cir
            
