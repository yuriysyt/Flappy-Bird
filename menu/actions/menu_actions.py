import pygame
from gameloop.game_loop import GameLoop
from levels import level_1, level_2, level_3, level_4, level_5 


class MenuHandler:
    def __init__(self, selected_option, selected_level, page, options):
        self.selected_option = selected_option
        self.selected_level = selected_level
        self.page = page
        self.options = options

    def menu_actions(self):
        if self.selected_option == 0:
            path_to_level_1 = getattr(eval(f'level_{1}'), 'maps', None)
            game = GameLoop(self.selected_level if self.selected_level else path_to_level_1)
            game.game_loop()
        elif self.selected_option == 1:
            self.selected_option = 0
            self.page = 'level_choose'
            self.options = [f"Level {i}: {getattr(eval(f'level_{i}'), 'maps', None)}" for i in range(1, 6)]
            self.menu_loop()
        elif self.selected_option == 2:
            pygame.quit()
            return
