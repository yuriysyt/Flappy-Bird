import pygame
from screen.screen import DisplayManager
from pygame.locals import *
from menu.actions.level_actions import LevelSelector
from menu.actions.menu_actions import MenuHandler
from menu.calculations.bird_animation import BirdAnimator
from menu.draw.draw import MenuDrawer
from menu.keyboard.event import MenuEventHandling
from images.find_img import images

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
                pygame.K_RETURN: lambda: MenuHandler.menu_actions(self) if self.page == 'menu' else LevelSelector.select_level_actions(self),
            })


            self.clock.tick(30)
