import pygame
import colorswatch as cs
import pixel
import random
import bullet




class Enemy(object):
    def __init__(self, surface, posX, posY, enemy_type = "taito_0"):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.enemy_type = enemy_type
        self.life_color = cs.white["pygame"]
        self.ashes = cs.night_gray["pygame"]
        self.move_direction = "left"
        self.speed = 1
        self.clock = pygame.time.Clock()
        self.isAlive = True
        if self.enemy_type == "taito_UFO":
            self.boundingBox = pygame.Rect(self.posX, self.posY, 44,18)
        else:
            self.boundingBox = pygame.Rect(self.posX, self.posY, 27, 27)

        self.taito_0 = ["----1----",
                        "---111---",
                        "--11111--",
                        "-1--1--1-",
                        "-1111111-",
                        "-1111111-",
                        "--1-1-1--",
                        "-1-----1-",
                        "--1---1--"]

        self.taito_1 = ["-1-----1-",
                        "--1---1--",
                        "---111---",
                        "--1-1-1--",
                        "-1111111-",
                        "1-11111-1",
                        "1--111--1",
                        "-1-----1-",
                        "--11-11--"]

        self.taito_2 = ["---111---",
                        "-1111111-",
                        "111111111",
                        "1---1---1",
                        "111111111",
                        "111---111",
                        "1-11111-1",
                        "1-------1",
                        "-11---11-"]

    
        self.taito_ufo = ["----1111111111----",
                          "--111-11-11--111--",
                          "-1111111111111111-",
                          "111111111111111111",
                          "-1111--1111--1111-",
                          "--11111111111111--",]


        self.enemy_icon = []
        self.enemy_pattern = []
        self.startX = self.posX
        self.bullet_list = []


    def build_enemy(self):
        if self.isAlive:
            if self.enemy_type == "taito_0":
                self.enemy_pattern = self.taito_0
            elif self.enemy_type == "taito_1":
                self.enemy_pattern = self.taito_1
            elif self.enemy_type == "taito_2":
                self.enemy_pattern = self.taito_2
            elif self.enemy_type == "taito_UFO":
                self.enemy_pattern = self.taito_ufo
        else:
            self.enemy_pattern = self.death_ashes

        pixel_width = 3
        
        for row in self.enemy_pattern:
            for col in row:
                if col == "1":
                    self.enemy_icon.append(pixel.Pixel(self.surface, self.posX, self.posY, color = self.life_color, pixel_size = pixel_width))

                self.posX += pixel_width

            self.posY += pixel_width
            self.posX = self.startX

            

    def fire(self):
        if len(self.bullet_list) < 1:
            self.bullet_list.append(bullet.Bullet(self.surface, self.posX, self.posY, direction = "down"))



    def update(self):
        if self.isAlive:
            if self.enemy_type == "taito_UFO":
                for pixel in self.enemy_icon:
                    pixel.pixelRect.x -= self.speed
            else:
                leftmost_x = min([pixel.pixelRect.x for pixel in self.enemy_icon])
                rightmost_x = max([pixel.pixelRect.x for pixel in self.enemy_icon])

                if self.move_direction == "left":
                    for pixel in self.enemy_icon:
                        pixel.pixelRect.x -= self.speed
                 
                    if leftmost_x <= 0:
                        self.move_direction = "right"
                        for pixel in self.enemy_icon:
                            pixel.pixelRect.y += 40

                elif self.move_direction == "right":
                    for pixel in self.enemy_icon:
                        pixel.pixelRect.x += self.speed

                    if rightmost_x >= 600 - 21:
                       self.move_direction = "left"
                       for pixel in self.enemy_icon:
                            pixel.pixelRect.y += 40
        else:
            for pixel in self.enemy_icon:
                pixel.pixelRect.y += random.randrange(5, 10)

                if pixel.pixelRect.y >= self.posY - 100:
                    self.enemy_icon.remove(pixel)



            

            

    def draw(self):
         for pixel in self.enemy_icon:
            pixel.draw()