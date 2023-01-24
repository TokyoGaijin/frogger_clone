import enemy
import bullet as bt


## This class handles the enemy waves

class WaveManager(object):
    def __init__(self, surface):
        self.surface = surface
        self.wave = ["1-1-1-1-1-1-1-1-1-1-1"]
        self.skip_size = 45
        self.startX = 30
        self.enemy_list = []
        self.saucer_list = []
        self.saucer_launch_timer = 0
        self.saucer_launch_factor = 600
        self.speed_factor = 2
        self.bullet_list = []
        


    def get_waves(self):
        for slots in self.wave[0]:
            if slots == "1":
                self.enemy_list.append(enemy.Enemy(self.surface, self.startX, 85, enemy_type = "taito_0"))
                self.enemy_list.append(enemy.Enemy(self.surface, self.startX, 85 * 2, enemy_type = "taito_1"))
                self.enemy_list.append(enemy.Enemy(self.surface, self.startX, 85 * 3, enemy_type = "taito_2"))

                self.startX += self.skip_size

        self.saucer_list.append(enemy.Enemy(self.surface, 850, 60, enemy_type = "taito_UFO"))



    def level_up(self):
        for enemy in self.enemy_list:
            if len(self.enemy_list) <= 20:
                enemy.speed = 2
            if len(self.enemy_list) <= 10:
                enemy.speed = 3
            if len(self.enemy_list) <= 5:
                enemy.speed = 4
            if len(self.enemy_list) <= 2:
                enemy.speed = 5



    def collide_with(self, target):
        for enemy in self.enemy_list:
            for pixel in enemy.enemy_icon:
                for bullet in target:
                    if bullet.bulletRect.colliderect(pixel.pixelRect):
                        target.remove(bullet)
                        enemy.isAlive = False

            if len(enemy.enemy_icon) <= 0:
                self.enemy_list.remove(enemy)


        for UFO in self.saucer_list:
            for pixel in UFO.enemy_icon:
                for bullet in target:
                    if bullet.bulletRect.colliderect(pixel.pixelRect):
                        target.remove(bullet)
                        enemy.isAlive = False

        self.level_up()


    def bullet_collide_with(self, target):
        for bullet in self.bullet_list:
            if bullet.bulletRect.colliderect(target):
                self.bullet_list.remove(bullet)



    def fire(self, target):
        for enemy in self.enemy_list:
            for pixel in enemy.enemy_icon:
                if pixel.pixelRect.x == target.posX:
                    if len(self.bullet_list) <= 2:
                        self.bullet_list.append(bt.Bullet(self.surface, pixel.pixelRect.x, pixel.pixelRect.y, direction = "down"))


        



    def build_enemies(self):
        for enemy in self.enemy_list:
            enemy.build_enemy()

        for UFO in self.saucer_list:
            UFO.build_enemy()







    def update(self):

        self.saucer_launch_timer += 60

        for enemy in self.enemy_list:
            enemy.update()

        if self.saucer_launch_timer % self.saucer_launch_factor == 0:
            if len(self.saucer_list) < 1:
                for UFO in self.saucer_list:
                    UFO.update()

        for bullet in self.bullet_list:
            bullet.update()

        for bullet in self.bullet_list:
            if bullet.bulletRect.y >= 900:
                self.bullet_list.remove(bullet)



    def draw(self):
        for enemy in self.enemy_list:
            enemy.draw()

        for UFO in self.saucer_list:
            UFO.draw()

        for bullet in self.bullet_list:
            bullet.draw()


