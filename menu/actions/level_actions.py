from menu.actions.options_manager import LevelOptionsUpdater 

class LevelSelector:
    def select_level_actions(self):
        if self.selected_option >= 0:  
            self.path_to_selected_level = LevelOptionsUpdater.update_options(self.selected_option)
            self.options = ["Start Game", "Choose Level", "Quit"]
            self.page = 'menu'
            self.menu_loop()  
