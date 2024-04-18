from levels import level_1, level_2, level_3, level_4, level_5 

class LevelSelector:
    def select_level_actions(self):
        if self.selected_option >= 0:  
            self.selected_level = getattr(eval(f"level_{self.selected_option + 1}"), "maps", None)
            self.options = ["Start Game", "Choose Level", "Quit"]
            self.page = 'menu'
            self.menu_loop()  
