import pygame
from pygame.locals import *

class MenuEventHandling:
    @staticmethod
    def handle_key_press(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.handle_return_key_press()
                elif event.type == QUIT:
                    self.running = False
                    pygame.quit()