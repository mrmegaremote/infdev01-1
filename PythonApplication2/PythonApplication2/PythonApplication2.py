class Vector2:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

v = Vector2(input("speed on the x: "), input("speed on the y: "))

if v.X < 0:
    print"You're going to die"
elif abs(v.Y) > 0:
    print"Hello guardrail, my old friend"
elif v.X > 0:
    print"Muy esta bien"
input("")