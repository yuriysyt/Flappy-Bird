import pygame

class ScoreCalculator:
    def get_score(self, game_instance):
        if not game_instance.losing and not game_instance.winning:
            self.last_score = pygame.time.get_ticks() - game_instance.time_start_game
        return str(self.last_score)
