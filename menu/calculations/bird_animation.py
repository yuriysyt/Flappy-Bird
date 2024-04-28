import pygame
"""
Here is a very simple class for calculating the bird's position.
First, it checks if enough time has passed 
since the last "wing flap" of the bird to perform a new flap.

Then we have the variable self.up, which tells the bird where to move.
If self.up = True - then up (self.bird_rect.centery -= 1.5)
If self.up = False - then down (self.bird_rect.centery += 1.4)

We also set the minimum (240) and maximum (290) coordinates
within which the bird should move.

If it reaches 290, then the bird needs to move up.
If it reaches 240, then the bird should move down.

"""
class BirdAnimator:

    def animate_bird(self):
        if self.up:
            self.bird_rect.centery -= 1.5
        else:
            self.bird_rect.centery += 1.4
        if self.bird_rect.centery < 240:
            self.up = False
        elif self.bird_rect.centery > 290:
            self.up = True

