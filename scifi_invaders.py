import pygame
import keyboard
import pyautogui
import colorswatch as cs
import screen
import player_tank
import bullet
import building
import enemy
import threading


pygame.init()

game_screen = screen.Screen(600, 800, 60, bg_color = cs.black["pygame"], caption = "Frogger Clone (Working Title)")
game_size = (600, 600)
board_coords = (0, 200)

# Easy to reference surface declaration
WINDOW = game_screen.WINDOW


# Game Objects
player = player_tank.Player(WINDOW, 300, 700)
building_1 = building.Building(WINDOW, 25, 550)
building_2 = building.Building(WINDOW, 200, 550)
building_3 = building.Building(WINDOW, 375, 550)
building_4 = building.Building(WINDOW, 525, 550)

city = [building_1, building_2, building_3, building_4]


wave = ["1-1-1-1-1-1-1-1-1-1-1"]


enemy_list = []

def get_waves():
    global enemy_list
    skip_size = 45
    startX = 30

    for slots in wave[0]:
        if slots == "1":
            enemy_list.append(enemy.Enemy(WINDOW, startX, 85, enemy_type = "taito_0"))
            enemy_list.append(enemy.Enemy(WINDOW, startX, 85 * 2, enemy_type = "taito_1"))
            enemy_list.append(enemy.Enemy(WINDOW, startX, 85 * 3, enemy_type = "taito_2"))

            startX += skip_size



def collide_building():
    for buildings in city:
        for pixels in buildings.main_building:
            for bullet in player.magazine:
                if bullet.bulletRect.colliderect(pixels.pixelRect):
                    player.magazine.remove(bullet)
                    buildings.main_building.remove(pixels)



def collide_enemy():
    for enemy in enemy_list:
        for pixel in enemy.enemy_icon:
            for bullet in player.magazine:
                if bullet.bulletRect.colliderect(pixel.pixelRect ):
                    player.magazine.remove(bullet)
                    enemy.isAlive = False




def update():
    game_screen.screen_update()
    player.update()
    for building in city:
        building.update()
    for enemy in enemy_list:
        enemy.update()
    collide_building()    
    collide_enemy()


    
def draw():
    player.draw()
    for building in city:
        building.draw()
    for enemy in enemy_list:
        enemy.draw()


def main_game():
    for building in city:
        building.build_building()

    get_waves()
    for enemy in enemy_list:
        enemy.build_enemy()
    

    while game_screen.inPlay:

    

        if keyboard.is_pressed('escape'):
            game_screen.inPlay = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_screen.kill_screen()

    
        thread = threading.Thread(target=draw())
        thread.start()
        update_thread = threading.Thread(target=update())
        update_thread.start()


if __name__ == '__main__':
    main_game()