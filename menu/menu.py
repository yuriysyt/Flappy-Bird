import pygame
from screen.screen import DisplayManager
from pygame.locals import *
from menu.actions.level_actions import LevelSelector
from menu.actions.menu_actions import MenuHandler
from menu.calculations.bird_animation import BirdAnimator
from menu.draw.draw import MenuDrawer
from menu.keyboard.event import MenuEventHandling
from images.find_img import images
from ErrorHandling.error_handling import ErrorHandler

class Menu:
    def __init__(self):
        pygame.init()
        DisplayManager.init(self)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.options = ["Start Game", "Choose Level", "Quit"]
        self.page = 'menu'
        self.running = True
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
        try:
            while self.running:
                MenuDrawer.draw_menu(self)
                BirdAnimator.animate_bird(self)
                pygame.display.flip()   
                MenuEventHandling.handle_key_press(self)


                self.clock.tick(30)
        except Exception as e:
                ErrorHandler.menu_loop_error_handler(self, e)

    def handle_return_key_press(self):
        if self.page == 'menu':
            MenuHandler.menu_actions(self)
        elif self.page == 'level_choose':
            LevelSelector.select_level_actions(self)
