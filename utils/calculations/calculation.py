import pygame
from utils.calculations.init_pos import position
from levels.level_1 import maps
from utils.calculations.score_calculator import ScoreCalculator

class Calculations:

    def init(self):  
            position.init_object_position(self)
            self.losing = False
            self.winning = False
            self.is_jumping = False
            self.running = True
            self.current_time = pygame.time.get_ticks()
            self.time_start_game = pygame.time.get_ticks()
            self.clock = pygame.time.Clock() 
            self.last_score = 0
            self.down_time = 0  
            self.dt = self.clock.tick(60) / 1000
            self.gravity = 0.2
            self.jump_strength = -0.3
            self.fall_speed = 0.2
        
    def calculate(self):
        
        if not self.losing and not self.winning:

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
        
        if self.player_pos[1] < 0 or self.player_pos[1] > self.screen.get_width() - self.screen.get_width() / 4:
            self.losing = True

        if self.sky_pos[0] < -600:
            self.sky_pos[0] = 0
        
        if self.tree_pos[0] < -300:
            self.tree_pos[0] = (self.screen.get_width()) + 50

        if self.is_jumping:
                self.player_pos[1] -= 50 * self.dt
                self.fall_speed = 1
        else:
            self.fall_speed -= self.gravity
            self.player_pos[1] -= self.fall_speed