import pygame

class CollisionDetector:
    def lose_game(self, image_rect, player_pos):
        player_rect = pygame.Rect(player_pos[0], player_pos[1], 100, 50) 
        if image_rect.colliderect(player_rect):
            self.losing = True