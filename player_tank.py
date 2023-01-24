import pygame
import keyboard
import colorswatch as cs
import bullet
import explosion

class Player(object):
    def __init__(self, surface, posX, posY):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.speed = 5
        self.color = cs.green["pygame"]
        self.death_color = cs.fuchsia["pygame"]
        self.player_rect = pygame.Rect(self.posX, self.posY, 50, 20)
        self.player_gun = pygame.Rect(self.player_rect.x + 23, self.player_rect.y - 20, 5, 20)
        self.isAlive = True
        self.right_limit = 600 - self.player_rect.width
        self.magazine= []
        self.isAlive = True
        self.bomb = explosion.Explosion(self.surface)



        
    def fire(self):
        if len(self.magazine) < 1:
            self.magazine.append(bullet.Bullet(self.surface, self.player_gun.x, self.player_gun.y))


    def die(self):
        self.isAlive = False
        explosion.Explosion.build_bomb(self.posX, self.posY)
        #self.bomb.build_bomb(self.posX, self.posY)


    def update(self):

        def move(direction):
            if direction == "left":
                self.player_rect.x -= self.speed
                self.player_gun.x -= self.speed
            if direction == "right":
                self.player_rect.x += self.speed
                self.player_gun.x += self.speed


        if self.isAlive:
            if keyboard.is_pressed('left_arrow') or keyboard.is_pressed('a'):
                move("left")
            if keyboard.is_pressed('right_arrow') or keyboard.is_pressed('d'):
                move("right")
            if keyboard.is_pressed('space'):
                self.fire()
        else:
            #self.bomb.update(self.posX, self.posY)
            explosion.Explosion.update(self.posX, self.posY)



        # boundary check
        if self.player_rect.x <= 0:
            self.player_rect.x = 0
            self.player_gun.x = self.player_rect.x + 23
        if self.player_rect.x >= self.right_limit:
            self.player_rect.x = self.right_limit
            self.player_gun.x = self.player_rect.x + 23

        self.posX = self.player_rect.x
        
       


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
            self.bomb.draw()

