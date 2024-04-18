import pygame
from gameloop.calculations.create_level import LevelRenderer
from gameloop.game_loop import GameLoop
from gameloop.screen.screen import DisplayManager
from pygame.locals import *
from menu.calculations.bird_animation import BirdAnimator
from menu.draw.draw import MenuDrawer
from menu.keyboard.event import MenuEventHandling
from .images.find_img import images
from levels import level_1, level_2, level_3, level_4, level_5 

class Menu:
    def __init__(self):
        pygame.init()
        DisplayManager.init(self)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.options = ["Start Game", "Choose Level", "Quit"]
        self.page = 'menu'
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
            MenuDrawer.draw_menu(self)
            BirdAnimator.animate_bird(self)
            pygame.display.flip()
            MenuEventHandling.handle_events({
                pygame.K_UP: lambda: setattr(self, 'selected_option', (self.selected_option - 1) % len(self.options)),
                pygame.K_DOWN: lambda: setattr(self, 'selected_option', (self.selected_option + 1) % len(self.options)),
                pygame.K_RETURN: lambda: self.menu_actions() if self.page == 'menu' else self.select_level_actions(),
            })


            self.clock.tick(30)

    def menu_actions(self):
        if self.selected_option == 0:
            path_to_level_1 =  getattr(eval(f'level_{1}'), 'maps', None)
            game = GameLoop(self.selected_level if self.selected_level else path_to_level_1)
            game.game_loop()
        elif self.selected_option == 1:
            self.selected_option = 0
            self.page = 'level_choose'
            self.options = [f"Level {i}: {getattr(eval(f'level_{i}'), 'maps', None)}" for i in range(1, 6)]
            self.menu_loop()
        elif self.selected_option == 2:
            pygame.quit()
            return

    def select_level_actions(self):
        if self.selected_option >= 0:  # Ensure selected_option is non-negative
            self.selected_level = getattr(eval(f"level_{self.selected_option + 1}"), "maps", None)
            self.options = ["Start Game", "Choose Level", "Quit"]
            self.page = 'menu'
            self.menu_loop()  # Return to the menu loop after selecting a level
