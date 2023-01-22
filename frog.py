import pygame
import colorswatch as cs
import keyboard

class Frog(object):
    def __init__(self, surface, posX, posY):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.jump = 5
        self.frog_size = 20
        self.frogImage = None # for later if sprites to be used. Delete if not
        self.frogRect = pygame.Rect(self.posX, self.posY, self.frog_size, self.frog_size)
        self.frog_color = cs.green["pygame"]


    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.surface, self.frog_color, self.frogRect)
