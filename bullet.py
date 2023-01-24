import pygame
import colorswatch as cs

class Bullet(object):
    def __init__(self, surface, posX, posY, direction = "up"):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.color = cs.light_gray["pygame"]
        self.bulletRect = pygame.Rect(self.posX, self.posY, 5, 25)
        self.speed = 5
        self.direction = direction


    def update(self):
        # On create
        if self.direction == "down":
            self.bulletRect.y += self.speed
        else: 
            self.bulletRect.y -= self.speed


    def draw(self):
        # On create
        pygame.draw.rect(self.surface, self.color, self.bulletRect)
