import pygame

"""
Here we calculate the player's score, how much they have earned since the beginning of the game.
If they haven't lost or won, the score will simply stop updating.
"""
class ScoreCalculator:
    def get_score(self):
        if not self.losing and not self.winning:
            self.last_score = pygame.time.get_ticks() - self.time_start_game
        return str(self.last_score)
