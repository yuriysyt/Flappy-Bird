import pygame

from utils.calculations.calculation import Calculations
from utils.draw import DrawingTool
from utils.keyboard.keyboard import KeyboardManager
from utils.screen.screen import DisplayManager

class GameLoop:
    def __init__(self):
        self.running = True 

        DisplayManager.init(self)
        Calculations.init(self) 

    def game_loop(self):
        while self.running:
            Calculations.calculate(self)
            KeyboardManager.handle_keyboard(self)
            DrawingTool.draw(self)

if __name__ == "__main__":
    game = GameLoop()
    game.game_loop()

pygame.quit()