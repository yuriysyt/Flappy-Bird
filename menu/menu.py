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
    """
    Here is where the class is initialized from main.py
    We create variables that will be used to display the menu.

    DisplayManager.init - initialize the screen from the screen folder
    pygame.time.Clock() - get time
    self.options - Set the values of options for the user: Start Game, Choose Level, Quit
    self.page - Specify that the user is currently in the main menu, not in the level selection
    self.running - Set to True to start the While Loop in menu_loop
    self.selected_option - Set to 0 so that the user starts with "Start Game", making it simply white
    self.bird_img - Import the bird image from images.flippyImg
    self.bird_rect - Get the initial dimensions of the bird image
    self.bird_rect.centery - Set the initial x-axis coordinates of the bird
    self.bird_rect.centery - Set the initial y-axis coordinates of the bird
    self.up - Tell the program that the bird needs to move upward
    self.path_to_selected_level - Tell that the level is not yet selected
    """
    def __init__(self):
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
        self.up = True
        self.path_to_selected_level = None

    def menu_loop(self):
        """
        From the beginning, we catch errors from the ErrorHandling folder
        I use try-except for this purpose
        If an error is found, we activate the function from ErrorHandling
        Which makes our error readable for humans
        """

        """
        Next, I start a While Loop
        Where I begin to call functions from classes.
        MenuDrawer.draw_menu - responsible for drawing the menu
        BirdAnimator.animate_bird - responsible for the bird movement in the menu
        MenuEventHandling.handle_key_press - where I capture all user pressed keys
        """
        while self.running:
            MenuDrawer.draw_menu(self)
            BirdAnimator.animate_bird(self)
            pygame.display.flip()   
            MenuEventHandling.handle_key_press(self)

            self.clock.tick(30)


    """
    Here we check which window the user is currently on
    They are either in the main menu or choosing which level to play.
    After the program understands where we are, it begins to perform calculations.

        MenuHandler - if the user is in the main menu.
        LevelSelector - if the user is in the level selection process.
    """
    def handle_return_key_press(self):
        if self.page == 'menu':
            MenuHandler.menu_actions(self)
        elif self.page == 'level_choose':
            LevelSelector.select_level_actions(self)