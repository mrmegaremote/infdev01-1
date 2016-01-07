import pygame
from pygame.locals import *
import os, sys, random
pygame.init()

class Car:
    def __init__ (self, startx, starty): 
        self.Sprite = pygame.image.load('sprite.png')
        self.position = Vector2(startx, starty)

class Empty:
        def __init__(self):
            self.isEmpty = True

class Node:
    def __init__(self, c, tail):
        self.isEmpty = False
        self.Tail = tail
        self.car = c

class Vector2:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

vehicle = Car(-100, random.randint(0, 400))
v2 = Car(-100, random.randint(0, 400))
v3  = Car(-100, random.randint(0, 400))
v4  = Car(-100, random.randint(0, 400))
v5  = Car(-100, random.randint(0, 400))

screen = pygame.display.set_mode((800, 600))

#screen.blit(vehicle.Sprite, (0,0))

while True:
    vehicle.position.X += 0.3
    screen.fill((0, 0, 0))

    screen.blit(vehicle.Sprite, (vehicle.position.X, vehicle.position.Y))
   
    pygame.display.flip()


    if vehicle.position.X > 900:
        vehicle.position.X = -100
        vehicle.position.Y = random.randint(0, 400)

