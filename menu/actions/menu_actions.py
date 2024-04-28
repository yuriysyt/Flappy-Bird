import pygame
from SortingAlgorithm.sorting import LevelSorter
from gameloop.game_loop import GameLoop
from levels import level_1, level_2, level_3, level_4, level_5
from menu.actions.options_manager import LevelOptionsUpdater
import sys


"""
This class is used to perform calculations in the main menu.
When the user presses Enter, the program checks which option the user selected.
If they chose 0, the generation and transition to the selected level will begin.
If they chose 1, they will go to the level selection menu.
If they chose 2, the game will exit.
"""
class MenuHandler:

    def menu_actions(self):
        if self.selected_option == 0:
            """
            path_to_level_1 - We add a path for the first level in case the user didn't choose any level
            game = GameLoop() - Then, we initialize GameLoop, to which we pass information about the selected level
            If the user selected a level self.path_to_selected_level, then the selected level will be generated
            If not, the default level path_to_level_1 will be used
            And so we pass the integer option self.selected_option, which is usually one less than the actual level
            game.game_loop() - Then we start GameLoop with the specified parameters
            And proceed to level generation in the GameLoop class
            """
            path_to_level_1 = LevelOptionsUpdater.update_options(0)
            game = GameLoop((self.path_to_selected_level if self.path_to_selected_level else path_to_level_1), self.selected_option)
            game.game_loop()
        elif self.selected_option == 1: # Choose level
            """
            This is if the user wants to choose a level
            selected_option = 0 - We tell our program to reset the selection from the beginning
            self.page = 'level_choose' - Then we say that we are in the level_choose stage for our function in menu.py
            self.options - Then we generate a list of 5 levels and show them to the user
            self.menu_loop() - And then we rerun menu_loop to display the levels
            """
            self.selected_option = 0
            self.page = 'level_choose'
            sorted_levels = LevelSorter.sorting_cfg('config.cfg')
            self.options = sorted_levels
            
            self.menu_loop()
        elif self.selected_option == 2: # Quit
            """
            End the menu_loop cycle
            And exit pygame
            """
            self.running = False
            pygame.quit()
            sys.exit(1)
