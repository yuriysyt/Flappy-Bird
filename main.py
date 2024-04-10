import pygame
from func_image.find_img import images
from functions.calculations.calculation import calculations
from functions.draw import DrawingTool

class GameLoop:
    def __init__(self):
        self.running = True 
        calculations.init(self)
                

    def game_loop(self):
        while self.running:
            calculations.calculate(self)
            calculations.input(self)
            DrawingTool.draw(self)


if __name__ == "__main__":
    game = GameLoop()
    game.game_loop()

pygame.quit()