import pygame
from pygame.locals import *
from ErrorHandling.error_handling import ErrorHandler
from gameloop.calculations.calculation import Calculations
from gameloop.draw.draw import DrawingTool
from gameloop.keyboard.keyboard import KeyboardManager
from screen.screen import DisplayManager

"""
Start of the GameLoop class
"""
class GameLoop:
    """
    Here we set the values of the self.running variable to True for our For Loop
    Next, we define the path to the selected level from menu_loop
    And also get the level in numerical value, 1, 2, 3, etc.
    """
    def __init__(self, path_to_selected_level, selected_option):
        self.running = True
        self.path_to_selected_level = path_to_selected_level 
        self.selected_option = selected_option

        DisplayManager.init(self)
        Calculations.init(self) 

    """
    Start the calculation, key press detection, and drawing
    If something goes wrong, an error from ErrorHandling will be displayed
    """

    def game_loop(self):
        try:
            while self.running: 
                Calculations.calculate(self)
                KeyboardManager.handle_keyboard(self)
                DrawingTool.draw(self)
        except Exception as e:
                ErrorHandler.main_error_handler(e)
