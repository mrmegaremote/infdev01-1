import pygame
from Node import *
import random

class Car:
    def __init__(self, pos):
        self.Position = pos
        self.prevspot = pos

    def Update(self):
        dir = random.randint(0, 3)

        if dir == 0 and self.Position.Right != None and self.Position.Right.Traverseable == True:
            if self.Position.Right:
                self.Position = self.Position.Right 
        elif dir == 1 and self.Position.Left != None and self.Position.Left.Traverseable == True:
            if self.Position.Left:
                self.Position = self.Position.Left 
        elif dir == 2 and self.Position.Up != None and self.Position.Up.Traverseable == True:
            if self.Position.Up:
                self.Position = self.Position.Up 
        elif dir == 3 and self.Position.Down != None and self.Position.Down.Traverseable == True:
            if self.Position.Down:
                self.Position = self.Position.Down 
        else:
            self.Update()
        return Car(self.Position)

    def isArrived(self):
        return self.Position.Park == True
