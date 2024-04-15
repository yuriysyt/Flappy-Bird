import pygame
from gameloop.calculations.create_level import LevelRenderer
from gameloop.game_loop import GameLoop
from gameloop.screen.screen import DisplayManager
from pygame.locals import *

from menu.calculations.bird_animation import BirdAnimator
from menu.draw.draw import MenuDrawer
from menu.draw.level_selector import LevelSelector
from .images.find_img import images
from levels import level_1, level_2, level_3, level_4, level_5 

class Menu:
    def __init__(self):
        pygame.init()
        DisplayManager.init(self)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.options = ["Start Game", "Choose Level", "Quit"]
        self.selected_option = 0
        self.bird_img = images.flippyImg 
        self.bird_rect = self.bird_img.get_rect()
        self.bird_rect.centerx = 150
        self.bird_rect.centery = 290
        self.flap_timer = 0
        self.flap_interval = 10
        self.up = True
        self.selected_level = None

    def menu_loop(self):
        while True:
            self.screen.fill((0, 0, 0))
            MenuDrawer.draw_menu(self)
            BirdAnimator.animate_bird(self)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:
                            game = GameLoop(self.selected_level)
                            game.game_loop()
                        elif self.selected_option == 1:
                            LevelSelector.select_level()
                        elif self.selected_option == 2:
                            pygame.quit()
                            return

            self.clock.tick(30)



