
from utils.images.find_img import images


class position:
    def init_object_position(self):
        (self.player_pos, self.ground_pos, self.tree_pos, 
         self.sky_pos, self.tube_pos, self.background_pos, 
         self.gameover_pos, self.welcome_pos, self.win_pos) = images.get_pos(self.screen)