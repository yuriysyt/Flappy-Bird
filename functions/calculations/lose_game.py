import pygame

class CollisionDetector:
    @staticmethod
    def check_collision(image_rect, player_pos):
        player_rect = pygame.Rect(player_pos[0], player_pos[1], 100, 50)
        return image_rect.colliderect(player_rect)

class GameOutcomeHandler:
    def lose_game(self, image_rect, player_pos):
        if CollisionDetector.check_collision(image_rect, player_pos):
            self.losing = True