from gameloop.calculations.lose_game import CollisionDetector
from images.find_img import images

"""
This class is used to generate infinite ground that acts as the floor

First, we load the selected level (maps =)
Then we set up a For Loop where we get the number of all obstacles through len(maps.pos)

Next, we determine the number of floor elements, depending on the size of our level
So, for example, the longer the level, the longer the ground will be

We also use if-else statements to render only the visible part of the ground, not the entire ground

Then we simply draw it on our screen using blit
"""
class BackgroundRenderer:
    def create_background(self):
        maps = self.path_to_selected_level
        last_pos = None 
        for ipos in range(len(maps.pos)):
            current_pos = (400 * ipos) + self.background_pos[0]
            if current_pos > -1000 and current_pos < self.screen.get_height() + 1000:
                background_rect = images.backgroundImg.get_rect(topleft=((400 * ipos) + self.background_pos[0], self.background_pos[1]))
                self.screen.blit(images.backgroundImg, background_rect)
                CollisionDetector.lose_game(self, background_rect, self.player_pos)
                last_pos = current_pos
                
        """
        If all obstacles are passed, indicate that the player has completed the level.
        """
        if last_pos and last_pos + 400 < 0:
            self.winning = True