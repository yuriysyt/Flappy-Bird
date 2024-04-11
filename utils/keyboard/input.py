import pygame

class InputHandling:
    def handle_input(self):
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
                self.player_pos[1] -= 50 * self.dt
                self.fall_speed = 1
            else:
                self.fall_speed -= self.gravity
                self.player_pos[1] -= self.fall_speed
