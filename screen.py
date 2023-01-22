import pygame

class Screen(object):
    def __init__(self, width, height, FPS, bg_color = (0, 0, 0), caption = None):

        self.WIDTH = width
        self.HEIGHT = height
        self.SCREEN_SIZE = (self.WIDTH, self.HEIGHT)

        self.WINDOW = pygame.display.set_mode(self.SCREEN_SIZE)

        if caption != None:
            self.GAME_NAME = caption
            pygame.display.set_caption(self.GAME_NAME)

        self.BG_COLOR = bg_color
        self.CLOCK = pygame.time.Clock()
        self.FPS = FPS
        self.inPlay = True

        

    def kill_screen(self):
        if self.inPlay:
            self.inPlay = False


    def screen_update(self):
        self.CLOCK.tick(self.FPS)
        pygame.display.update()
        self.WINDOW.fill(self.BG_COLOR)