import pygame
from pygame.locals import *

class MenuEventHandling:
    @staticmethod
    def handle_events(actions):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key in actions:
                    actions[event.key]()