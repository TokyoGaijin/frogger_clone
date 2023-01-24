import pixel
import random
import colorswatch as cs

class Explosion(object):
    def __init__(self, surface, color = cs.fuchsia["pygame"]):
        self.surface = surface
        self.color = color
        self.block = [["1111111111"],
                      ["1111111111"],
                      ["1111111111"]]
        self.skip_size = 5
        self.bomb = []


    def build_bomb(self, posX, posY):
        for row in self.block:
            for col in row:
                if col == "1":
                    self.bomb.append(pixel.Pixel(self.surface, posX, posY))

                posX += self.skip_size
            posY += self.skip_size
            posX = 0


    def update(self, posX, posY):
        print(f"Frags: {len(self.bomb)}")
        for pixel in self.bomb:
            pixel.pixelRect.y += random.randrange(3, 11)

            if pixel.pixelRect.y >= posY + 50:
                self.bomb.remove(pixel)


    def draw(self):
        for pixel in self.bomb:
            pixel.draw()