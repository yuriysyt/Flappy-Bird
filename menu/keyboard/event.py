import sys
import pygame
from pygame.locals import *

"""
Here we catch which key the user pressed.

First, we check if a key was pressed or not.

Then we look at which key is pressed and make calculations.

If the user presses the up key, then we say that the user selected the option above.
We update its value, and only after we update it, it becomes white.

If the user presses the down key, then we say that the user selected the option below.
We update its value, and only after we update it, it becomes white.

But if the user presses Enter, then we start calculations with the selected option.
Options are calculated in the main menu.py file.

If the user presses to close the program (not in the menu, but closes the window itself),
Then we end the loop in menu_loop.
Then we simply exit pygame.

"""
class MenuEventHandling:
    @staticmethod
    def handle_key_press(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit(1)
                    
            if event.type == KEYDOWN:
                    
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.handle_return_key_press()
