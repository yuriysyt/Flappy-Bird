import pygame
from levels.level_1 import maps
from func_image.find_img import images
import pygame


class calculations:
    def calculate(self):
        keys = pygame.key.get_pressed()
        if not self.losing:
            if keys[pygame.K_w] and not self.is_jumping:
                self.player_pos.y -= 50
                self.is_jumping = True
                self.current_time = pygame.time.get_ticks()
        
            if self.is_jumping:
                self.player_pos.y -= 10 * self.dt
                self.fall_speed = 1
            else:
                self.fall_speed -= self.gravity
                self.player_pos.y -= self.fall_speed

            self.ground_pos.x -= 5
            self.background_pos.x -= 5
            self.sky_pos.x -= 5
            self.tree_pos.x -= 5
            self.tube_pos.x -= 5

            if pygame.time.get_ticks() > self.current_time + 300:
                self.is_jumping = False
                self.down_time =pygame.time.get_ticks()

        if self.ground_pos.x < -300:
            self.ground_pos.x = 0

        if self.sky_pos.x < -600:
            self.sky_pos.x = 0
        
        if self.tree_pos.x < -300:
            self.tree_pos.x =  (self.screen.get_width()) + 50
            
    def create_level(self):
        for ipos in range(0,len(maps.pos)):
            pos = maps.pos[ipos]
            if pos + (self.tube_pos.x) > -400 and pos + (self.tube_pos.x) < self.screen.get_height() + 1000:
                width = maps.height[ipos]
                updown = maps.updown[ipos]
                height = maps.height[ipos]
                param_scale = width, height
                scaled_image = pygame.transform.scale(images.tubeImg, param_scale)
                scaled_image_rotate = pygame.transform.scale(images.rotateTubeImg, param_scale)
                scaled_image = scaled_image if updown == 0 else scaled_image_rotate
                screen_position = (pos + self.tube_pos.x, 500 if updown == 0 else self.screen.get_height() / 1500)
                self.screen.blit(scaled_image, screen_position)
                calculations.lose_game(self, scaled_image, screen_position)

    def create_background(self):
         for ipos in range(0,len(maps.pos)):
            current_pos = (400 * ipos) + self.background_pos.x
            if current_pos > - 1000 and current_pos <  self.screen.get_height() + 1000:
                self.screen.blit(images.backgroundImg, ((400 * ipos) + self.background_pos.x, self.background_pos.y))
    
    def lose_game(self, scaled_image, screen_position):
                image_rect = scaled_image.get_rect(topleft=screen_position)
                player_rect = pygame.Rect(self.player_pos.x, self.player_pos.y, 100, 50) 
                if image_rect.colliderect(player_rect):
                    self.losing = True