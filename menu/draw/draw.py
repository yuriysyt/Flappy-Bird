"""
Here we draw all our menu with calculated values (Data visualization)
First, we fill the screen with blue color.
Then, we check which option the user wants to select and color it white.
If the option is selected - white, if not selected - gray.
We also render the font on which our menu will be displayed
And set its position.
After that, we draw our text with the specified position.
And then, we draw the bird with its position.
"""

class MenuDrawer:
    def draw_menu(self):
        if self.running:
            self.screen.fill((78, 192, 202)) 
            for i, option in enumerate(self.options):
                color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
                text_surface = self.font.render(option, True, color)
                text_position = (250, 200 + i * 50)
                self.screen.blit(text_surface, text_position)
            self.screen.blit(self.bird_img, self.bird_rect)
