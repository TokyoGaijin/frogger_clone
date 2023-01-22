import pygame
import colorswatch as cs
import pixel

class Building(object):
    def __init__(self, surface, posX, posY):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.building_pattern = ["---00000000",
                                 "--011111110",
                                 "-0111111101",
                                 "01111111101",
                                 "00000000011",
                                 "0OO00OO0011",
                                 "0OO00OO0011",
                                 "00000000011",
                                 "0OO00OO0011",
                                 "0OO00OO0011",
                                 "00000000011",
                                 "0OO00OO0011",
                                 "0OO00OO0011",
                                 "00000000011",
                                 "0000000001-"]
        
        self.main_color = cs.gray["pygame"]
        self.shade_color = cs.night_gray["pygame"]
        self.lights = cs.yellow["pygame"]
        self.main_building = []
        self.pixel = pygame.Rect(self.posX, self.posY, 10, 10)
        self.main_pixel = self.pixel

        # Build the building itself
        self.startX = self.posX


    def build_building(self):
        pixel_size = 10

        
        for row in self.building_pattern:
            for col in row:
                if col == "0":
                    self.main_building.append(pixel.Pixel(self.surface, self.posX, self.posY, color = self.main_color))
                if col == "1":
                    self.main_building.append(pixel.Pixel(self.surface, self.posX, self.posY, color = self.shade_color))
                if col == "O":
                    self.main_building.append(pixel.Pixel(self.surface, self.posX, self.posY, color = self.lights))

                self.posX += pixel_size

            self.posY += pixel_size
            self.posX = self.startX



    def update(self):
        pass

    
    def draw(self):
        for pixel in self.main_building:
            pixel.draw()