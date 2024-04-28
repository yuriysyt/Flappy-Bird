from levels import level_1, level_2, level_3, level_4, level_5 

"""
This class is created to update the selected level.
That is, it takes a variable representing which option the user selected (which level they chose)
And then assigns a path to this level to be used later in game_loop
That is the path to the files in levels (where level_1, level_2, etc., are located).

It takes and returns: <class 'levels.level_1.maps'>
"""
class LevelOptionsUpdater:

    def update_options(selected_option):
        return getattr(eval(f"level_{selected_option + 1}"), "maps", None)
