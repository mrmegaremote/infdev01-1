import time
from threading import Thread
import os, pygame
import time
import random
from Tile import *
from Node import *
from Car import *

pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 30
board_size = 15
car_texture = pygame.image.load("Content\car.png").convert()
board = build_square_matrix(board_size, offset)

def Map(l, f):
    if l.IsEmpty == True:
        return Empty()
    else:
        return Node(l.Update(), map(l.Tail))

def Count(l):
    if l.IsEmpty == True:
        return 0
    else:
        return 1 + Count(l.Tail)
    

def Update(cars):
    newcars = Empty
    i = cars
    while i.IsEmpty == False:
        if i.Value.isArrived() == False:
            newcars = Node(i.Value, newcars)
        i = i.Tail

    if Count(newcars) < 6:
        newcars = Node(Car(board), newcars)

    carstoupdate = newcars
    while carstoupdate.IsEmpty == False:
        carstoupdate.Value.Update()
        carstoupdate = carstoupdate.Tail
    return newcars

def Draw(cars, screen):
    
    while cars.IsEmpty == False:
        _width = int(offset / 3)
        screen.blit(pygame.transform.scale(car_texture, (_width, _width)), 
                            (_width +  cars.Value.Position.Position[0] * offset, 
                            _width + cars.Value.Position.Position[1] * offset))
        
        cars = cars.Tail

def Main():
  start = time.time()
  cars = Empty
  cars = Node(Car(board), cars)
  while True:    
    screen.fill(green)  
    board.Reset()
    board.Draw(screen)
    
    cars = Update(cars)
    Draw(cars, screen)

    pygame.display.flip()
    time.sleep(1)
    
Main()

