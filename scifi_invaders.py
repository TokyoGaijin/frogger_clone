import pygame
import keyboard
import pyautogui
import colorswatch as cs
import screen
import player_tank
import bullet
import building


pygame.init()

game_screen = screen.Screen(600, 800, 60, bg_color = cs.black["pygame"], caption = "Frogger Clone (Working Title)")
game_size = (600, 600)
board_coords = (0, 200)

# Easy to reference surface declaration
WINDOW = game_screen.WINDOW


# Game Objects
player = player_tank.Player(WINDOW, 300, 700)
building_1 = building.Building(WINDOW, 25, 480)
building_2 = building.Building(WINDOW, 250, 480)
building_3 = building.Building(WINDOW, 465, 480)

city = [building_1, building_2, building_3]



def collide_building():
    for buildings in city:
        for pixels in buildings.main_building:
            for bullet in player.magazine:
                if bullet.bulletRect.colliderect(pixels.pixelRect):
                    player.magazine.remove(bullet)
                    buildings.main_building.remove(pixels)



def update():
    game_screen.screen_update()
    player.update()
    for building in city:
        building.update()
    collide_building()


    
def draw():
    player.draw()
    for building in city:
        building.draw()


def main_game():
    for building in city:
        building.build_building()

    while game_screen.inPlay:

    

        if keyboard.is_pressed('escape'):
            game_screen.inPlay = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_screen.kill_screen()

    
        draw()
        update()


if __name__ == '__main__':
    main_game()