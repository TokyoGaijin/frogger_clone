import pygame
import keyboard
import pyautogui
import colorswatch as cs
import screen
import player_tank
import bullet


pygame.init()

game_screen = screen.Screen(600, 800, 60, bg_color = cs.black["pygame"], caption = "Frogger Clone (Working Title)")
game_size = (600, 600)
board_coords = (0, 200)

# Easy to reference surface declaration
WINDOW = game_screen.WINDOW


# Game Objects
player = player_tank.Player(WINDOW, 300, 700)


def update():
    game_screen.screen_update()
    player.update()


    
def draw():
    player.draw()



while game_screen.inPlay:

    

    if keyboard.is_pressed('escape'):
        game_screen.inPlay = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_screen.kill_screen()

    
    draw()
    update()

