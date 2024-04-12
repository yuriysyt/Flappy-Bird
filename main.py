import pygame
from pygame.locals import *
from utils.calculations.calculation import Calculations
from utils.draw import DrawingTool
from utils.keyboard.keyboard import KeyboardManager
from utils.screen.screen import DisplayManager

class Menu:
    def __init__(self):
        pygame.init()  # Initialize Pygame here
        DisplayManager.init(self)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)  # Now it's safe to create font objects
        self.options = ["Start Game", "Choose Level", "Quit"]
        self.selected_option = 0

    def draw_menu(self):
        self.screen.fill((0, 0, 0))
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (200, 200 + i * 50))

    def menu_loop(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.draw_menu()
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
                            game = GameLoop()
                            game.game_loop()
                        elif self.selected_option == 1:
                            pass
                        elif self.selected_option == 2:
                            pygame.quit()
                            return

            self.clock.tick(30)

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
    menu = Menu()
    menu.menu_loop()
    pygame.quit()