import pygame
from gameloop.game_loop import GameLoop
from levels import level_1, level_2, level_3, level_4, level_5
from menu.actions.options_manager import LevelOptionsUpdater


class MenuHandler:

    def menu_actions(self):
        if self.selected_option == 0:
            path_to_level_1 = LevelOptionsUpdater.update_options(0)
            game = GameLoop((self.path_to_selected_level if self.path_to_selected_level else path_to_level_1), self.selected_option)
            game.game_loop()
        elif self.selected_option == 1: #Choose level
            self.selected_option = 0
            self.page = 'level_choose'
            self.options = [f"Level {i}: " for i in range(1, 6)]
            self.menu_loop()
        elif self.selected_option == 2: #Quit
            self.running = False
            pygame.quit()
