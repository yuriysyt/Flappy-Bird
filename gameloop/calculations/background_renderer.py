from gameloop.calculations.lose_game import CollisionDetector
from images.find_img import images

class BackgroundRenderer:
    def create_background(self):
        maps = self.selected_level
        for ipos in range(len(maps.pos)):
            current_pos = (400 * ipos) + self.background_pos[0]
            if current_pos > -1000 and current_pos < self.screen.get_height() + 1000:
                background_rect = images.backgroundImg.get_rect(topleft=((400 * ipos) + self.background_pos[0], self.background_pos[1]))
                self.screen.blit(images.backgroundImg, background_rect)
                CollisionDetector.lose_game(self, background_rect, self.player_pos)
