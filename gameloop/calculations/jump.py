import pygame

class JumpCalculator:
    @staticmethod
    def calculate_jump(self):
        self.player_pos[1] -= 50
        self.is_jumping = True
        self.current_time = pygame.time.get_ticks()