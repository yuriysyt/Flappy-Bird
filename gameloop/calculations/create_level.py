import pygame
from gameloop.calculations.lose_game import CollisionDetector
from images.find_img import images

"""
This class is used to generate obstacles from the selected level in the levels folder

First, we have a condition that if the level is selected, then we continue further

The For Loop determines the number of elements in the selected level and its length using len()
pos - gets all the positions of elements

There is also a condition that if the position is within our field of view, then we calculate only its position
We load width, updown, height - from our levels folder
Then we set the value for how we need to change the object depending on the screen

Then we change the values depending on the screen values ​​through scale 

Next, we determine whether the obstacle (pipe) is located on top or bottom and change it accordingly

The object is drawn and the class for collision detection with our obstacles (pipes) is enabled
"""
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
                
