import pygame

from utils.calculations.jump import JumpCalculator

class InputHandling:

    def handle_input(self):
        self.keys = pygame.key.get_pressed()

        if not self.losing and not self.winning:
            self.handle_escape(self)
            self.handle_jump(self)

    def handle_escape(self):
        if self.keys[pygame.K_ESCAPE]:
            self.running = False

    def handle_jump(self):
        if self.keys[pygame.K_w] and not self.is_jumping:
            JumpCalculator.calculate_jump(self)
