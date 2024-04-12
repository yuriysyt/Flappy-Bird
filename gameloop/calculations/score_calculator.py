import pygame

class ScoreCalculator:
    def get_score(self):
        if not self.losing and not self.winning:
            self.last_score = pygame.time.get_ticks() - self.time_start_game
        return str(self.last_score)
