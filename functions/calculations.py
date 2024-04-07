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
        keys = pygame.key.get_pressed()
        if not self.losing:
            if keys[pygame.K_ESCAPE]:
                self.running = False
            if keys[pygame.K_w] and not self.is_jumping:
                self.player_pos[1] -= 50
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

        if self.sky_pos[0] < -600:
            self.sky_pos[0] = 0
        
        if self.tree_pos[0] < -300:
            self.tree_pos[0] = (self.screen.get_width()) + 50

    def create_level(self):
        for ipos in range(len(maps.pos)):
            pos = maps.pos[ipos]
            if pos + (self.tube_pos[0]) > -400 and pos + (self.tube_pos[0]) < self.screen.get_height() + 1000:
                width = maps.height[ipos]
                updown = maps.updown[ipos]
                height = maps.height[ipos]
                param_scale = width, height
                scaled_image = pygame.transform.scale(images.tubeImg, param_scale)
                scaled_image_rotate = pygame.transform.scale(images.rotateTubeImg, param_scale)
                scaled_image = scaled_image if updown == 0 else scaled_image_rotate
                screen_position = (pos + self.tube_pos[0], self.screen.get_height() - 200 if updown == 0 else self.screen.get_height() / 1500)
                self.screen.blit(scaled_image, screen_position)
                calculations.lose_game(self, scaled_image, screen_position)


    def create_background(self):
        for ipos in range(len(maps.pos)):
            current_pos = (400 * ipos) + self.background_pos[0]
            if current_pos > - 1000 and current_pos < self.screen.get_height() + 1000:
                self.screen.blit(images.backgroundImg, ((400 * ipos) + self.background_pos[0], self.background_pos[1]))

    def lose_game(self, scaled_image, screen_position):
        image_rect = scaled_image.get_rect(topleft=screen_position)
        player_rect = pygame.Rect(self.player_pos[0], self.player_pos[1], 100, 50) 
        if image_rect.colliderect(player_rect):
            self.losing = True