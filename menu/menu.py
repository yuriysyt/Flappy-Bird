import pygame
from gameloop.calculations.create_level import LevelRenderer
from gameloop.game_loop import GameLoop
from gameloop.screen.screen import DisplayManager
from pygame.locals import *

from menu.calculations.bird_animation import BirdAnimator
from menu.draw.draw import MenuDrawer
from .images.find_img import images
from levels import level_1, level_2, level_3, level_4, level_5 

class Menu:
    def __init__(self):
        pygame.init()
        DisplayManager.init(self)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.options = ["Start Game", "Choose Level", "Quit"]
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
            self.screen.fill((0, 0, 0))
            MenuDrawer.draw_menu(self)
            BirdAnimator.animate_bird(self)
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
                            path_to_level_1 =  getattr(eval(f'level_{1}'), 'maps', None)
                            print(path_to_level_1)
                            game = GameLoop(self.selected_level if self.selected_level else path_to_level_1)
                            game.game_loop()
                        elif self.selected_option == 1:
                            self.select_level()
                        elif self.selected_option == 2:
                            pygame.quit()
                            return

            self.clock.tick(30)

    def select_level(self):
        self.selected_option = 0  # Start from the first level option
        while True:
            self.screen.fill((0, 0, 0))
            selected_level_text = [f"Level {i}: {getattr(eval(f'level_{i}'), 'maps', None)}" for i in range(1, 6)]
            for i, level_text in enumerate(selected_level_text):
                color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)  # Adjust index here
                text = self.font.render(level_text, True, color)
                self.screen.blit(text, (250, 200 + i * 50))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % 5
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % 5
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option >= 0:  # Ensure selected_option is non-negative
                            self.selected_level = getattr(eval(f"level_{self.selected_option + 1}"), "maps", None)
                            return


