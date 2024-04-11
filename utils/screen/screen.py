import pygame

class DisplayManager:
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 650))