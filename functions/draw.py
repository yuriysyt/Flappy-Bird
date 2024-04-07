from levels.level_1 import maps
from func_image.find_img import images
import pygame
from functions.calculations import calculations

class DrawingTool():
    def draw(self):
        self.screen.fill('#4ec0ca')

        calculations.create_background(self)
        
        if self.is_jumping:
            self.screen.blit(images.upCarImg, self.player_pos)
        else:
            self.screen.blit(images.downCarImg, self.player_pos)

        for i in range(-2, 7):
            self.screen.blit(images.groundImg, (self.ground_pos.x + 300 * i, self.ground_pos.y))
           # self.screen.blit(images.skyImg, (self.sky_pos.x + 600 * i, self.sky_pos.y))

        calculations.create_level(self)
       