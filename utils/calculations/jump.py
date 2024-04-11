import pygame

class JumpCalculator:
    @staticmethod
    def calculate_jump(game):
        game.player_pos[1] -= 50
        print(game.player_pos[1])
        game.is_jumping = True
        game.current_time = pygame.time.get_ticks()
