import pygame
from pygame.locals import *
from gameloop.calculations.calculation import Calculations
from gameloop.draw import DrawingTool
from gameloop.keyboard.keyboard import KeyboardManager
from gameloop.screen.screen import DisplayManager

class GameLoop:
    def __init__(self, selected_level):
        self.running = True 
        self.selected_level = selected_level

        DisplayManager.init(self)
        Calculations.init(self) 

    def game_loop(self):
        while self.running: 
            Calculations.calculate(self)
            KeyboardManager.handle_keyboard(self)
            DrawingTool.draw(self)