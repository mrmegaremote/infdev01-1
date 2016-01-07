import pygame

class Tile:
    def __init__(self, ):
        #self.Right = r
        #self.Left = l
        #self.Up = u
        #self.Down = d
        #sprite


class Car:
    def __init__(self, posx, posy):
        self.Position = Vector2(posx, posy)
        self.Sprite = pygame.image.load('sprite.png')

class Vector2:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

vehicle = Car(0, 0)
screen = pygame.display.set_mode((800, 600))

for i in range (10):
    for j in range (10):
        t = Tile()

while True:
    screen.fill((0, 0, 0))

    screen.blit(vehicle.Sprite, (vehicle.Position.X, vehicle.Position.Y))
   
    pygame.display.flip()
