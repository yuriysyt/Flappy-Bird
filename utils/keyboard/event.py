import pygame

from utils.calculations.init_pos import position

class EventHandling:
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and (self.losing or self.winning):
                position.init_object_position(self)
                self.time_start_game = pygame.time.get_ticks()
                self.losing, self.winning = False, False
