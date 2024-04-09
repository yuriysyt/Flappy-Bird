import pygame
from functions.calculations.score_calculator import ScoreCalculator
from levels.level_1 import maps

class calculations:
    def __init__(self):
        # Initialize positions using NumPy arrays
        self.player_pos = [0, 0]
        self.ground_pos = [0, 0]
        self.background_pos = [0, 0]
        self.sky_pos = [0, 0]
        self.tree_pos = [0, 0]
        self.tube_pos = [0, 0]

        # Initialize other variables
        self.running = True
        self.losing = False
        self.is_jumping = False
        self.current_time = pygame.time.get_ticks()
        self.time_start_game = pygame.time.get_ticks()
        self.last_score = 0
        self.dt = 1
        self.gravity = 0.2
        self.fall_speed = 0
        
    def calculate(self):
        keys = pygame.key.get_pressed()

        
        if not self.losing and not self.winning:
            if keys[pygame.K_ESCAPE]:
                self.running = False
                
            if keys[pygame.K_w] and not self.is_jumping:
                self.player_pos[1] -= 50
                print(self.player_pos[1])
                self.is_jumping = True
                self.current_time = pygame.time.get_ticks()
        
            if self.is_jumping:
                self.player_pos[1] -= 10 * self.dt
                self.fall_speed = 1
            else:
                self.fall_speed -= self.gravity
                self.player_pos[1] -= self.fall_speed

            # Update positions using NumPy array operations
            self.ground_pos[0] -= 5
            self.background_pos[0] -= 5
            self.sky_pos[0] -= 5
            self.tree_pos[0] -= 5
            self.tube_pos[0] -= 5

            if pygame.time.get_ticks() > self.current_time + 300:
                self.is_jumping = False

        if self.ground_pos[0] < -300:
            self.ground_pos[0] = 0

        if int(ScoreCalculator.get_score(self)) > maps.finish_ticks:
            self.winning = True
        
        if self.player_pos[1] < 0 or self.player_pos[1] > self.screen.get_width() - self.screen.get_width() / 2:
            self.losing = True

        if self.sky_pos[0] < -600:
            self.sky_pos[0] = 0
        
        if self.tree_pos[0] < -300:
            self.tree_pos[0] = (self.screen.get_width()) + 50
    
    def lose_game(self, image_rect, player_pos):
        player_rect = pygame.Rect(player_pos[0], player_pos[1], 100, 50) 
        if image_rect.colliderect(player_rect):
            self.losing = True