import pygame
import keyboard
import pyautogui
import colorswatch as cs
import screen
import player_tank
import bullet
import building
import enemy
import enemy_manager
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



# Game element managers
wave_manager = enemy_manager.WaveManager(WINDOW)





def collide_building():
    for buildings in city:
        for pixels in buildings.main_building:
            for bullet in player.magazine:
                if bullet.bulletRect.colliderect(pixels.pixelRect):
                    player.magazine.remove(bullet)
                    buildings.main_building.remove(pixels)

            for bullet in wave_manager.bullet_list:
                if bullet.bulletRect.colliderect(pixels.pixelRect):
                    wave_manager.bullet_list.remove(bullet)
                    buildings.main_building.remove(pixels)




def update():
    game_screen.screen_update()
    player.update()
    wave_manager.update()
    for building in city:
        building.update()
 
    collide_building()    
    wave_manager.collide_with(player.magazine)
    wave_manager.bullet_collide_with(player.player_rect)


    
def draw():
    player.draw()
    wave_manager.draw()
    for building in city:
        building.draw()
    


def main_game():
    for building in city:
        building.build_building()

    wave_manager.get_waves()
    wave_manager.build_enemies()
        



    while game_screen.inPlay:

        if len(wave_manager.bullet_list) < 1:
            wave_manager.fire(player)

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