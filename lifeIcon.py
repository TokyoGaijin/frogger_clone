import pygame
import colorswatch as cs

class LifeIcon(object):
    def __init__(self, surface):
        self.surface = surface
        self.color = cs.green["pygame"]
        self.life_rect = pygame.Rect(0, 0, 50, 20)
        
    def draw(self, posX, posY):
        self.life_rect.x = posX
        self.life_rect.y = posY
        pygame.draw.rect(self.surface, self.color, self.life_rect)
        pygame.draw.rect(self.surface, self.color, (self.life_rect.x + 23, self.life_rect.y - 20, 5, 20))

