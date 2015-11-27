class Empty:
    def __init__(self):
        self.isEmpty = True

class Node:
    def __init__(self, value, tail): 
        self.isEmpty = False
        self.Value = value
        self.Tail = tail


length = int(input("how long do you like it?: "))
l = Empty()
    

for i in range(length):
    val = input("welke waarde?: ")
    l = Node(val, l)
x = l
y = Empty()

while x.isEmpty == False:
    print (x.Value)
    x = x.Tail

