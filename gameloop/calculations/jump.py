import pygame

"""
Used to calculate the jump and how far the bird needs to jump.
We set the value that the user has jumped and also determine the number of ticks.
"""
class JumpCalculator:
    @staticmethod
    def calculate_jump(self):
        self.player_pos[1] -= 50
        self.is_jumping = True
        self.current_time = pygame.time.get_ticks()
