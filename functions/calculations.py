import pygame
import numpy as np
from levels.level_1 import maps
from func_image.find_img import images

class calculations:
    def __init__(self):
        # Initialize positions using NumPy arrays
        self.player_pos = np.array([0, 0])
        self.ground_pos = np.array([0, 0])
        self.background_pos = np.array([0, 0])
        self.sky_pos = np.array([0, 0])
        self.tree_pos = np.array([0, 0])
        self.tube_pos = np.array([0, 0])

        # Initialize other variables
        self.running = True
        self.losing = False
        self.is_jumping = False
        self.current_time = pygame.time.get_ticks()
        self.dt = 1
        self.gravity = 0.2
        self.fall_speed = 0
        
    def calculate(self):
        pass