# Handles the game GUI

import pygame
import pygame.freetype
import lifeIcon
import colorswatch as cs


class GameManager(object):
    def __init__(self, surface):
        self.surface = surface
        self.life_list = [lifeIcon.LifeIcon(self.surface) for i in range(0,4)]
        self.score = 0
        self.level = 0
        self.lives = 4 # 3, 2, 1, 0 like a reverse array
        self.kill_points = [100, 250, 500, 1000]
        self.isGameOver = False
        self.font_file = "TOS_Title.TTF"
        self.font_size = 25
        self.font_color = cs.white["pygame"]
        self.render_font = pygame.font.Font(self.font_file, self.font_size)


    def add_points(self, ufo = False):
        if ufo:
            self.score += self.kill_points[3]
        else:
            self.score += self.kill_points[self.level]



    def take_life(self):
        if len(self.life_list) >= 0 and self.lives != 0:
            self.lives -= 1
            self.life_list.remove(0)
        if self.lives < 0:
            self.isGameOver = True


    def level_up(self, rank):
        self.level = rank


    def draw(self):
        self.life_list[0].draw(600 - (70 * 4), 30)
        self.life_list[1].draw(600 - (70 * 3), 30)
        self.life_list[2].draw(600 - (70 * 2), 30)

        renderText = self.render_font.render(f"SCORE: {self.score}", self.font_size, self.font_color)
        self.surface.blit(renderText, (10, 10))
