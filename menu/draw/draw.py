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
