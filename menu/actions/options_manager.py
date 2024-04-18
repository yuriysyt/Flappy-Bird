from levels import level_1, level_2, level_3, level_4, level_5 

class LevelOptionsUpdater:

    def update_options(selected_option):
        return getattr(eval(f"level_{selected_option + 1}"), "maps", None)
