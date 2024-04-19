import pygame
from gameloop.game_loop import GameLoop
from levels import level_1, level_2, level_3, level_4, level_5
from menu.actions.options_manager import LevelOptionsUpdater


class MenuHandler:

    def menu_actions(self):
        if self.selected_option == 0:
            path_to_level_1 = LevelOptionsUpdater.update_options(1)
            game = GameLoop(self.selected_level if self.selected_level else path_to_level_1)
            game.game_loop()
        elif self.selected_option == 1:
            self.selected_option = 0
            self.page = 'level_choose'
            self.options = [f"Level {i}: {LevelOptionsUpdater.update_options(self.selected_option)}" for i in range(1, 6)]
            self.menu_loop()
        elif self.selected_option == 2:
            pygame.quit()
            return
