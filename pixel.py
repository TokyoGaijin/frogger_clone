import pygame
import colorswatch as cs

class Pixel(object):
    def __init__(self, surface, posX, posY, color = cs.green["pygame"], pixel_size = 10):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.color = color
        
        self.pixelRect = pygame.Rect(self.posX, self.posY, pixel_size, pixel_size)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.pixelRect)
