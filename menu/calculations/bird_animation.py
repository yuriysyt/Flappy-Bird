import pygame

class BirdAnimator:

    def animate_bird(self):
        # Check if it's time to flap based on the interval
        if pygame.time.get_ticks() - self.flap_timer > self.flap_interval:
            # Adjust the bird's position based on the flap direction
            if self.up:
                self.bird_rect.centery -= 1.5
            else:
                self.bird_rect.centery += 1.4

            # Print the bird's vertical position for debugging
            print(self.bird_rect.centery)

            # Change flap direction when reaching certain positions
            if self.bird_rect.centery < 240:
                self.up = False
            elif self.bird_rect.centery > 290:
                self.up = True

            # Update the flap timer
            self.flap_timer = pygame.time.get_ticks()
