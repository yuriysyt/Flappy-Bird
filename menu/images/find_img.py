import pygame
import os

image_folder = os.path.join(os.path.dirname(__file__), 'images')

class images:
    flippyImg = pygame.image.load(os.path.join(image_folder, "flippy.png")) 
    flippyImg = pygame.transform.scale(flippyImg, (100, 60))

    def get_pos(screen):
        width_for_img, height_for_img = screen.get_width(), screen.get_height()
        player_pos = pygame.Vector2(width_for_img / 1000, height_for_img / 2)


        return player_pos

