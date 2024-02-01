import pygame

class Ladrillo :
    def __innit__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y

ladrillo = Ladrillo()
ladrillo.x = 230
ladrillo.y = 200