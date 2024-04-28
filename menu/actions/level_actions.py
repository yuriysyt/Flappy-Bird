from menu.actions.options_manager import LevelOptionsUpdater 
import re
"""
If the user has chosen a level, this function is triggered.
First, we update the path where the selected level is located (more details in the class itself).
Then, we take the user to the main menu, where they will have the opportunity to start the game
with the selected level, and then we tell the program that we are in the main menu.
This is required for menu.py, where the program uses different functions for different menu pages.
"""
class LevelSelector:
    def select_level_actions(self):
        if self.selected_option >= 0:  
            match = re.search(r'\d+', str(self.options[self.selected_option]))
            self.level_number = int(match.group()) - 1
            self.path_to_selected_level = LevelOptionsUpdater.update_options(self.level_number)
            self.options = ["Start Game", "Choose Level", "Quit"]
            self.page = 'menu'
            self.menu_loop()  
