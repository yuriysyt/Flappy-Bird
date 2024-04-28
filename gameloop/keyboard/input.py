import pygame

from gameloop.calculations.jump import JumpCalculator

"""
This class is similar to event.py, but here we define key presses
Such as esc, w

Esc - exits the game
W - makes the player jump if they decide to jump
"""
class InputHandling:

    def handle_input(self):
        self.keys = pygame.key.get_pressed()

        if not self.losing and not self.winning:
            InputHandling.handle_escape(self)
            InputHandling.handle_jump(self)

    def handle_escape(self):
        if self.keys[pygame.K_ESCAPE]:
            self.running = False

    def handle_jump(self):
        if self.keys[pygame.K_w] and not self.is_jumping:
            JumpCalculator.calculate_jump(self)
