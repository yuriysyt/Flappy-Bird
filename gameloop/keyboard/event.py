import pygame

from gameloop.calculations.init_pos import position

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
                self.losing, self.winning = False, False
