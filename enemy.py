import pygame
import colorswatch as cs
from enum import Enum
import pixel

class EnemyState(Enum):
    TAITO_0: 0
    TAITO_1: 1
    TAITO_2: 2
    TAITO_UFO: 5


class LifeState(Enum):
    ALIVE: 0
    DEAD: 1




class Enemy(object):
    def __init__(self, surface, posX, posY, type = EnemyState.TAITO_0):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.type = type
        self.life_state = LifeState.ALIVE
        self.life_color = cs.white["pygame"]
        self.ashes = cs.night_gray["pygame"]

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

        self.death_ashes = ["---------",
                            "---------",
                            "---------",
                            "---------",
                            "----1----",
                            "---1111--",
                            "-1111111-",
                            "111111111",
                            "111111111"]

        self.enemy_icon = []
        self.enemy_pattern = []
        self.startX = self.posX


    def build_enemy(self):
        
        if self.life_state == LifeState.ALIVE:
            if self.type == EnemyState.TAITO_0:
                self.enemy_pattern = self.taito_0
            elif self.type == EnemyState.TAITO_1:
                self.enemy_pattern = self.taito_1
            elif self.type == EnemyState.TAITO_2:
                self.enemy_pattern = self.taito_2
            elif self.type == EnemyState.TAITO_UFO:
                self.enemy_pattern = self.taito_ufo
        else:
            self.enemy_pattern = self.death_ashes

        pixel_width = 10
        
        for row in self.enemy_pattern:
            for col in row:
                if col == "1":
                    self.enemy_icon.append(pixel.Pixel(self.window, self.posX, self.posY, color = self.life_color))

                self.posX += pixel_width

            self.posY += pixel_width
            self.posX = self.startX

    def update(self):
        pass
        #TODO: Do movement here

    def draw(self):
        for pixel in self.enemy_icon:
            pixel.draw()