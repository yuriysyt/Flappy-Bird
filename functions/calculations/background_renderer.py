import pygame
from func_image.find_img import images
from levels.level_1 import maps
from .calculation import calculations

class BackgroundRenderer:
    def create_background(self):
        for ipos in range(len(maps.pos)):
            current_pos = (400 * ipos) + self.background_pos[0]
            if current_pos > -1000 and current_pos < self.screen.get_height() + 1000:
                background_rect = images.backgroundImg.get_rect(topleft=((400 * ipos) + self.background_pos[0], self.background_pos[1]))
                self.screen.blit(images.backgroundImg, background_rect)
                calculations.lose_game(self, background_rect, self.player_pos)
