import pygame

"""
Здесь мы иннициализируем pygame screen
Говорим программе, что нам нужно FULLSCREEN

Это используется в game_loop.py и в menu_loop.py
"""
class DisplayManager:
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)