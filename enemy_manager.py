#import pygame
import enemy

## This class handles the enemy waves

class WaveManager(object):
    def __init__(self, surface):
        self.surface = surface
        self.wave = ["1-1-1-1-1-1-1-1-1-1-1"]
        self.skip_size = 45
        self.startX = 30
        self.enemy_list = []
        self.saucer_list = []
        


    def get_waves(self):
        for slots in self.wave[0]:
            if slots == "1":
                self.enemy_list.append(enemy.Enemy(self.surface, self.startX, 85, enemy_type = "taito_0"))
                self.enemy_list.append(enemy.Enemy(self.surface, self.startX, 85 * 2, enemy_type = "taito_1"))
                self.enemy_list.append(enemy.Enemy(self.surface, self.startX, 85 * 3, enemy_type = "taito_2"))

                self.startX += self.skip_size

        self.saucer_list.append(enemy.Enemy(self.surface, 850, 60, enemy_type = "taito_UFO"))


    def collide_with(self, target):
        for enemy in self.enemy_list:
            for pixel in enemy.enemy_icon:
                for bullet in target:
                    if bullet.bulletRect.colliderect(pixel.pixelRect):
                        target.remove(bullet)
                        enemy.isAlive = False


    def build_enemies(self):
        for enemy in self.enemy_list:
            enemy.build_enemy()


    def update(self):
        for enemy in self.enemy_list:
            enemy.update()



    def draw(self):
        for enemy in self.enemy_list:
            enemy.draw()


