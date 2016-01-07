class Empty:
    def __init__(self):
        self.isEmpty = True

class Node:
    def __init__(self, value, tail):
        self.isEmpty = False
        self.Value = value
        self.Tail = tail

def add(l):
    val = 0
    while not l.isEmpty:
        val += l.Value



total = add(Node(10, Node(1,Node(2,Node(3,Empty)))))
print (total)