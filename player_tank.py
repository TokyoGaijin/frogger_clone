import pygame
import keyboard
import colorswatch as cs
import pixel
import bullet
import random

class Player(object):
    def __init__(self, surface, posX, posY):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.speed = 5
        self.pixel_width = 5
        self.color = cs.green["pygame"]
        self.death_color = cs.fuchsia["pygame"]
        self.player_rect = pygame.Rect(self.posX, self.posY, 50, 20)
        self.player_gun = pygame.Rect(self.player_rect.x + 23, self.player_rect.y - 20, 5, 20)
        self.isAlive = True
        self.right_limit = 600 - self.player_rect.width
        self.magazine = []
        self.isAlive = True
        
        self.block = [["----11----"],
                      ["----11----"],
                      ["1111111111"],
                      ["1111111111"]]

        self.bomb = []


    def build_bomb(self):
        startX = self.posX

        for row in self.block:
            for col in row:
                if col == "1":
                    self.bomb.append(pixel.Pixel(self.surface, self.posX, self.posY, pixel_size = self.pixel_width))
                
                self.posX += self.pixel_width

            self.posY += self.pixel_width
            self.posX = startX



        
    def fire(self):
        if len(self.magazine) < 1:
            self.magazine.append(bullet.Bullet(self.surface, self.player_gun.x, self.player_gun.y))



    def die(self):
        self.isAlive = False
        self.build_bomb()




    def update(self):
        if self.isAlive:
            print(f"Player position x: {self.posX} y: {self.posY}")
            def move(direction):
                if direction == "left":
                    self.player_rect.x -= self.speed
                    self.player_gun.x -= self.speed
                if direction == "right":
                    self.player_rect.x += self.speed
                    self.player_gun.x += self.speed


            
            if keyboard.is_pressed('left_arrow') or keyboard.is_pressed('a'):
                move("left")
            if keyboard.is_pressed('right_arrow') or keyboard.is_pressed('d'):
                move("right")
            if keyboard.is_pressed('space'):
                self.fire()
        
            


            # boundary check
            if self.player_rect.x <= 0:
                self.player_rect.x = 0
                self.player_gun.x = self.player_rect.x + 23
            if self.player_rect.x >= self.right_limit:
                self.player_rect.x = self.right_limit
                self.player_gun.x = self.player_rect.x + 23

            self.posX = self.player_rect.x

        else:
            print(f"Died at x: {self.posX} y: {self.posY} Frags: {len(self.bomb)}") 
            for pixels in self.bomb:
                pixels.pixelRect.y += random.randrange(3, 11)

                if pixels.pixelRect.y >= self.posY + 50:
                    self.bomb.remove(pixels)
       


        # eliminate bullet if it goes off screen
        for bullet in self.magazine:
            bullet.update()
            if bullet.bulletRect.y + bullet.bulletRect.height <= 100:
                self.magazine.remove(bullet)


        


    def draw(self):
        for bullet in self.magazine:
            bullet.draw()

        if self.isAlive:
            pygame.draw.rect(self.surface, self.color, self.player_rect)
            pygame.draw.rect(self.surface, self.color, self.player_gun)
        else:
            for pixels in self.bomb:
                pixels.draw()

