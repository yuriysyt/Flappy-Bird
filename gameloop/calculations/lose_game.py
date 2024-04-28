import pygame

"""
The class is created to determine the collision of the player. If the player touches the barrier,
then the game will end by setting the value of self.losing to True.
"""
class CollisionDetector:
    def lose_game(self, image_rect, player_pos):
        player_rect = pygame.Rect(player_pos[0], player_pos[1], 100, 50) 
        if image_rect.colliderect(player_rect):
            self.losing = True
