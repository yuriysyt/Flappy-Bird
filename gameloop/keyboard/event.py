import pygame

from gameloop.calculations.init_pos import position
from menu.actions.options_manager import LevelOptionsUpdater

"""
This class is created to handle user actions

If they click on exit, then quit the game completely
If the user loses or wins and clicks the button, then respawn the player from the beginning
In other words, update their position to the initial one and allow them to play and press keys again
"""
class EventHandling:
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and (self.losing or self.winning):
                position.init_object_position(self)
                self.time_start_game = pygame.time.get_ticks()
                if self.winning:
                    self.file_handler.set_level_completed(self.path_to_selected_level.__module__, True)
                    if self.selected_option + 1 < 5:

                        self.path_to_selected_level = LevelOptionsUpdater.update_options(self.selected_option + 1)
                        self.selected_option += 1
                        position.init_object_position(self)
                    else:
                        return
                    
                self.losing, self.winning = False, False
