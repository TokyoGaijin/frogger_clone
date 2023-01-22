import pygame
import colorswatch as cs
import keyboard

class Frog(object):
    def __init__(self, surface, posX, posY):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.jump = 25
        self.frog_size = 20
        self.frogImage = None # for later if sprites to be used. Delete if not
        self.frogRect = pygame.Rect(self.posX, self.posY, self.frog_size, self.frog_size)
        self.frog_color = cs.green["pygame"]
        self.death_rect = pygame.Rect(self.posX, self.posY, 50, 50)
        self.death_color = cs.red["pygame"]

        self.isAlive = True


    def update(self):
        
        # Movement
        def move(direction):

            targetX, targetY = None, None

            if direction == "left":
                targetX = self.frogRect.x - self.jump
                #self.frogRect.x -= self.jump
            if direction == "right":
                targetX = self.frogRect.x + self.jump
                #self.frogRect.x += self.jump
            if direction == "up":
                targetY = self.frogRect.y - self.jump
                #self.frogRect.y = targetY
            if direction == "down":
                targetY = self.frogRect.y + self.jump
                #self.frogRect.y += self.jump

            self.frogRect.x, self.frogRect.y = targetX, targetY

        if self.isAlive:
            if keyboard.is_pressed('up_arrow') or keyboard.is_pressed('w'):
                move("up")
            if keyboard.is_pressed('down_arrow') or keyboard.is_pressed('s'):
                move("down")
            if keyboard.is_pressed('left_arrow') or keyboard.is_pressed('a'):
                move("left")
            if keyboard.is_pressed('right_arrow') or keyboard.is_pressed('d'):
                move("right")

            # Debug Key for death simulation
            if keyboard.is_pressed('space'):
                self.isAlive = False

        # Update coordinates to kill frog
        self.death_rect.x, self.death_rect.y = self.frogRect.x, self.frogRect.y



    def draw(self):
        if self.isAlive:
            pygame.draw.rect(self.surface, self.frog_color, self.frogRect)
        else:
            pygame.draw.rect(self.surface, self.death_color, self.death_rect)
