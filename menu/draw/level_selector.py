class LevelSelector:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.selected_option = 0
        self.selected_level = None

    def select_level(self):
        # Start from the first level option
        self.selected_option = 0  
        
        while True:
            # Clear the screen
            self.screen.fill((0, 0, 0))
            
            # Generate text for each level option
            selected_level_text = [f"Level {i}: {getattr(eval(f'level_{i}'), 'maps', None)}" for i in range(1, 6)]
            
            # Display each level option on the screen
            for i, level_text in enumerate(selected_level_text):
                # Determine text color based on selection
                color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
                
                # Render the text for the level option
                text = self.font.render(level_text, True, color)
                
                # Position the text on the screen
                text_position = (250, 200 + i * 50)
                
                # Blit the text onto the screen
                self.screen.blit(text, text_position)
            
            # Update the display
            pygame.display.flip()

            # Handle events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == KEYDOWN:
                    # Navigate through level options
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % 5
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % 5
                    elif event.key == pygame.K_RETURN:
                        # Select the chosen level
                        if self.selected_option >= 0:  
                            self.selected_level = getattr(eval(f"level_{self.selected_option + 1}"), "maps", None)
                            return
