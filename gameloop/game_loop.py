import pygame
from pygame.locals import *
from ErrorHandling.error_handling import ErrorHandler
from gameloop.calculations.calculation import Calculations
from gameloop.draw.draw import DrawingTool
from gameloop.keyboard.keyboard import KeyboardManager
from screen.screen import DisplayManager

class GameLoop:
    def __init__(self, selected_level):
        self.running = True 
        self.selected_level = selected_level

        DisplayManager.init(self)
        Calculations.init(self) 

    def game_loop(self):
        try:
            while self.running: 
                Calculations.calculate(self)
                KeyboardManager.handle_keyboard(self)
                DrawingTool.draw(self)
        except Exception as e:
                ErrorHandler.main_error_handler(e)

            