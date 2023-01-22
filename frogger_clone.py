import pygame
import keyboard
import pyautogui
import colorswatch as cs
import screen
import frog

pygame.init()

game_screen = screen.Screen(600, 800, 60, bg_color = cs.black["pygame"], caption = "Frogger Clone (Working Title)")
game_size = (400, 600)
board_coords = (0, 200)

# Easy to reference surface declaration
WINDOW = game_screen.WINDOW


# Game Objects
player_frog = frog.Frog(WINDOW, 300, 500)


def update():
    game_screen.screen_update()



def draw():
    player_frog.draw()



while game_screen.inPlay:

    

    if keyboard.is_pressed('escape'):
        game_screen.inPlay = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_screen.kill_screen()

    
    draw()
    update()

