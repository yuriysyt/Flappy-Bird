import pygame
from func_image.find_img import images
from functions.calculations.calculation import calculations
from levels.level_1 import maps

class LevelRenderer:
    def create_level(self):
        for ipos in range(len(maps.pos)):
            pos = maps.pos[ipos]
            if pos + self.tube_pos[0] > -400 and pos + self.tube_pos[0] < self.screen.get_height() + 1000:
                width = maps.height[ipos]
                updown = maps.updown[ipos]
                height = maps.height[ipos]
                param_scale = width, height
                scaled_image = pygame.transform.scale(images.tubeImg, param_scale)
                scaled_image_rotate = pygame.transform.scale(images.rotateTubeImg, param_scale)
                scaled_image = scaled_image if updown == 0 else scaled_image_rotate
                screen_position = (pos + self.tube_pos[0], self.screen.get_height() - 200 if updown == 0 else self.screen.get_height() / 1500)
                self.screen.blit(scaled_image, screen_position)
                calculations.lose_game(self, scaled_image.get_rect(topleft=screen_position), self.player_pos)
