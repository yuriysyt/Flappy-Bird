import pygame

"""
Here we initialize the pygame screen
We tell the program that we need FULLSCREEN

This is used in game_loop.py and menu_loop.py
"""
class DisplayManager:
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 700))