import pygame

class BirdAnimator:

    def animate_bird(self):
        if pygame.time.get_ticks() - self.flap_timer > self.flap_interval:
            if self.up:
                self.bird_rect.centery -= 1.5
            else:
                self.bird_rect.centery += 1.4
            if self.bird_rect.centery < 240:
                self.up = False
            elif self.bird_rect.centery > 290:
                self.up = True

            # Update the flap timer
            self.flap_timer = pygame.time.get_ticks()
