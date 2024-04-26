import pygame
from gameloop.calculations.lose_game import CollisionDetector
from images.find_img import images

class LevelRenderer:

    def create_level(self):
        if self.path_to_selected_level:
            for ipos in range(len(self.path_to_selected_level.pos)):
                pos = self.path_to_selected_level.pos[ipos]
                if pos + self.tube_pos[0] > -400 and pos + self.tube_pos[0] < self.screen.get_height() + 1000:
                    width, updown, height = self.path_to_selected_level.height[ipos], self.path_to_selected_level.updown[ipos], self.path_to_selected_level.height[ipos]
                    param_scale = width, height
                    scaled_image = pygame.transform.scale(images.tubeImg, param_scale)
                    scaled_image_rotate = pygame.transform.scale(images.rotateTubeImg, param_scale)
                    scaled_image = scaled_image if updown == 0 else scaled_image_rotate
                    screen_position = (pos + self.tube_pos[0], self.screen.get_height() - 200 if updown == 0 else self.screen.get_height() / 1500)
                    self.screen.blit(scaled_image, screen_position)
                    CollisionDetector.lose_game(self, scaled_image.get_rect(topleft=screen_position), self.player_pos)
