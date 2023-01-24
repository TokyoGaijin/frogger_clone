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
                                 "00000000011"]
        
        self.main_color = cs.gray["pygame"]
        self.shade_color = cs.night_gray["pygame"]
        self.lights = cs.yellow["pygame"]
        self.main_building = []

        # Build the building itself
        self.startX = self.posX


    def build_building(self):
        pixel_width = 5

        
        for row in self.building_pattern:
            for col in row:
                if col == "0":
                    self.main_building.append(pixel.Pixel(self.surface, self.posX, self.posY, color = self.main_color, pixel_size = pixel_width))
                if col == "1":
                    self.main_building.append(pixel.Pixel(self.surface, self.posX, self.posY, color = self.shade_color, pixel_size = pixel_width))
                if col == "O":
                    self.main_building.append(pixel.Pixel(self.surface, self.posX, self.posY, color = self.lights, pixel_size = pixel_width))

                self.posX += pixel_width

            self.posY += pixel_width
            self.posX = self.startX



    def update(self):
        pass

    
    def draw(self):
        for pixel in self.main_building:
            pixel.draw()