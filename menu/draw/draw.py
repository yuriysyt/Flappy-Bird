class MenuDrawer:
    def draw_menu(self):
        # Fill the screen with a specified color
        self.screen.fill((78, 192, 202))  # Use a named color or RGB tuple for clarity
        
        # Draw each option in the menu
        for i, option in enumerate(self.options):
            # Determine color based on whether the option is selected or not
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            
            # Render the text for the option
            text_surface = self.font.render(option, True, color)
            
            # Position the text on the screen
            text_position = (250, 200 + i * 50)  # Adjust positioning as needed
            
            # Blit the text onto the screen
            self.screen.blit(text_surface, text_position)
        
        # Blit the bird image onto the screen
        self.screen.blit(self.bird_img, self.bird_rect)
